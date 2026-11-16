"""``battery-rul calibrate``: post-hoc CQR / split-conformal calibration of finished unit runs.

For every FINISHED unit run of an experiment, reads ``predictions.parquet`` (test cells) and
``inner_val_predictions.parquet`` (each cross-fit sub-model on its own inner-val cell), calibrates
at ``alpha`` (:func:`battery_rul.uq.conformal.calibrate_cv_plus`) and logs on the **same run**:

* metrics ``raw/<split>/<policy>/<kind>/{picp,mpiw,iscore}[_h<H>]`` (stored quantile interval at
  ``(alpha/2, 1 - alpha/2)``; only for probabilistic models) and ``cal/...`` (calibrated);
* artifacts ``calibrated_predictions.parquet`` (long, with ``lo``, ``hi``, ``lo_cal``,
  ``hi_cal``, ``correction``, ``n_cal``) and ``calibration_reliability.parquet``;
* tag ``calibrated_alpha`` (idempotence: skipped when equal to the requested alpha).

Models without inner-val predictions (``cross_fit = False``, e.g. GPR) cannot be calibrated
without breaking rule 7; they get ``raw/`` metrics only (tag ``calibrated_alpha = raw_only``).
Point-only models without inner-val predictions are skipped.
"""

from __future__ import annotations

import logging
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from battery_rul.uq.conformal import calibrate_cv_plus
from battery_rul.uq.metrics_uq import (
    interval_table,
    mlflow_metrics,
    reliability_table,
    scale_for,
    wide_to_long,
)

log = logging.getLogger("battery_rul.uq")

TAG = "calibrated_alpha"
RAW_ONLY = "raw_only"


@dataclass
class CalibrationSummary:
    n_calibrated: int = 0
    n_raw_only: int = 0
    n_already: int = 0
    n_skipped: int = 0
    n_failed: int = 0


def _load(run_id: str, name: str) -> pd.DataFrame | None:
    import mlflow

    try:
        return pd.read_parquet(
            mlflow.artifacts.download_artifacts(run_id=run_id, artifact_path=name)
        )
    except Exception:
        return None


def calibrate_run(
    preds: pd.DataFrame, inner: pd.DataFrame | None, task: str, alpha: float
) -> tuple[pd.DataFrame, dict[str, float], pd.DataFrame, str] | None:
    """Pure core: ``(long frame, metrics, reliability, status)`` or None if nothing to do."""
    test = wide_to_long(preds, alpha)
    probabilistic = bool(test["lo"].notna().any())
    if inner is None and not probabilistic:
        return None
    scale = scale_for(task)
    test["alpha"] = alpha
    metrics: dict[str, float] = {}
    if inner is not None:
        out = calibrate_cv_plus(wide_to_long(inner, alpha), test, alpha=alpha)
        status = f"{alpha:g}"
        cal_t = interval_table(out, "lo_cal", "hi_cal", alpha, scale, per_cell=False)
        metrics.update(mlflow_metrics(cal_t, task, "cal"))
    else:
        out = test.assign(lo_cal=float("nan"), hi_cal=float("nan"))
        out["correction"], out["n_cal"] = float("nan"), 0
        status = RAW_ONLY
    if probabilistic:
        raw_t = interval_table(out, "lo", "hi", alpha, scale, per_cell=False)
        metrics.update(mlflow_metrics(raw_t, task, "raw"))
    rel = reliability_table(inner, preds, scale=scale)
    return out, metrics, rel, status


def calibrate_experiment(
    experiment: str, tracking_uri: str, alpha: float = 0.1
) -> CalibrationSummary:
    import mlflow
    from mlflow.entities import Metric
    from mlflow.tracking import MlflowClient

    mlflow.set_tracking_uri(tracking_uri)
    runs = mlflow.search_runs(
        experiment_names=[experiment], filter_string="attributes.status = 'FINISHED'"
    )
    s = CalibrationSummary()
    if runs.empty or "tags.unit_key" not in runs:
        raise ValueError(f"no finished unit runs in experiment {experiment!r}")
    client = MlflowClient()
    want = f"{alpha:g}"
    for _, r in runs[runs["tags.unit_key"].notna()].iterrows():
        rid = str(r["run_id"])
        have = r.get(f"tags.{TAG}")
        if have == want or (
            have == RAW_ONLY and _load(rid, "inner_val_predictions.parquet") is None
        ):
            s.n_already += 1
            continue
        preds = _load(rid, "predictions.parquet")
        if preds is None:
            s.n_skipped += 1
            continue
        inner = _load(rid, "inner_val_predictions.parquet")
        try:
            res = calibrate_run(preds, inner, str(r["params.task"]), alpha)
        except Exception as e:  # one bad unit must not stop the sweep
            log.warning("run %s: calibration failed (%s)", rid, e)
            s.n_failed += 1
            continue
        if res is None:
            s.n_skipped += 1
            continue
        out, metrics, rel, status = res
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            out.to_parquet(d / "calibrated_predictions.parquet", index=False)
            client.log_artifact(rid, str(d / "calibrated_predictions.parquet"))
            if not rel.empty:
                rel.to_parquet(d / "calibration_reliability.parquet", index=False)
                client.log_artifact(rid, str(d / "calibration_reliability.parquet"))
        ts = int(time.time() * 1000)
        ms = [Metric(k, v, ts, 0) for k, v in metrics.items()]
        for i in range(0, len(ms), 900):  # MLflow caps a batch at 1000 metrics
            client.log_batch(rid, metrics=ms[i : i + 900])
        client.set_tag(rid, TAG, status)
        if status == RAW_ONLY:
            s.n_raw_only += 1
        else:
            s.n_calibrated += 1
    return s
