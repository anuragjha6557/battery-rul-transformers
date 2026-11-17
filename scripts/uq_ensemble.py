"""ADR-0011 arm "5-seed deep ensemble": ensemble benchmark seeds, then raw and CQR intervals.

For every benchmark unit (dataset, task, model, fold) of a probabilistic model, the K = 5 seed
runs' ``predictions.parquet`` and ``inner_val_predictions.parquet`` are averaged with
:func:`battery_rul.uq.ensemble.ensemble_frames` (per-level quantile averaging). The ensemble is
then calibrated exactly like a single run (:func:`battery_rul.uq.calibrate.calibrate_run`:
pooled split-conformal CQR on the ensembled inner-val predictions, rule 7 enforced).

Per-cell interval metrics are aggregated like ``report.calibration_table`` (mean over cells +
95 % cluster-bootstrap CI). Output: ``reports/tables/<experiment>_ensemble_calibration.csv``.

Usage: uv run python scripts/uq_ensemble.py [--experiment benchmark] [--alpha 0.1]
"""

from __future__ import annotations

import argparse
import logging
import os
from pathlib import Path

import mlflow
import numpy as np
import pandas as pd

from battery_rul.eval.stats import cluster_bootstrap_ci
from battery_rul.uq.calibrate import _load, calibrate_run
from battery_rul.uq.ensemble import ensemble_frames
from battery_rul.uq.metrics_uq import interval_table, scale_for

log = logging.getLogger("uq_ensemble")
URI = os.environ.get("MLFLOW_TRACKING_URI", f"sqlite:///{Path.cwd() / 'mlflow.db'}")
METRICS = ("picp", "mpiw", "iscore")


def unit_rows(runs: pd.DataFrame, alpha: float) -> list[pd.DataFrame]:
    out = []
    keys = ["params.dataset", "params.task", "params.model", "params.fold"]
    for (ds, task, model, fold), g in runs.groupby(keys, sort=True):
        preds = [_load(r, "predictions.parquet") for r in g["run_id"]]
        inner = [_load(r, "inner_val_predictions.parquet") for r in g["run_id"]]
        if any(p is None for p in preds) or any(i is None for i in inner):
            log.warning("%s/%s/%s/%s: missing artifacts; skipped", ds, task, model, fold)
            continue
        if not any(c.startswith("q") for c in preds[0].columns):
            continue  # point-only model: no raw interval, ensemble arm not defined
        try:
            ens_p, ens_i = ensemble_frames(preds), ensemble_frames(inner)
            res = calibrate_run(ens_p, ens_i, str(task), alpha)
        except ValueError as e:
            log.warning("%s/%s/%s/%s: %s", ds, task, model, fold, e)
            continue
        if res is None:
            continue
        long, *_ = res
        scale = scale_for(str(task))
        for arm, lo, hi in (("ens_raw", "lo", "hi"), ("ens_cal", "lo_cal", "hi_cal")):
            t = interval_table(long, lo, hi, alpha, scale, per_cell=True)
            out.append(t.assign(dataset=ds, task=task, model=model, arm=arm, n_members=len(g)))
        print(f"{ds}/{task}/{model}/{fold}: {len(g)} members", flush=True)
    return out


def aggregate(per_cell: pd.DataFrame) -> pd.DataFrame:
    rows = []
    gk = ["dataset", "task", "split", "policy", "kind", "horizon", "model", "arm"]
    for key, g in per_cell.groupby(gk, sort=True):
        row = dict(zip(gk, key, strict=True)) | {"n_cells": g["cell"].nunique()}
        for m in METRICS:
            by_cell = {
                c: np.array([v]) for c, v in g.groupby("cell")[m].mean().items() if np.isfinite(v)
            }
            if len(by_cell) >= 2:
                ci = cluster_bootstrap_ci(by_cell)
                row |= {m: ci.estimate, f"{m}_lo": ci.lo, f"{m}_hi": ci.hi}
            elif by_cell:
                row |= {m: float(next(iter(by_cell.values()))[0])}
        rows.append(row)
    return pd.DataFrame(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--experiment", default="benchmark")
    ap.add_argument("--alpha", type=float, default=0.1)
    args = ap.parse_args()
    logging.basicConfig(level=logging.WARNING)
    mlflow.set_tracking_uri(URI)
    runs = mlflow.search_runs(
        experiment_names=[args.experiment], filter_string="attributes.status = 'FINISHED'"
    )
    runs = runs[runs["tags.unit_key"].notna()]
    per_cell = pd.concat(unit_rows(runs, args.alpha), ignore_index=True)
    agg = aggregate(per_cell)
    out = Path("reports/tables") / f"{args.experiment}_ensemble_calibration.csv"
    agg.to_csv(out, index=False)
    print(f"wrote {out} ({len(agg)} rows)")


if __name__ == "__main__":
    main()
