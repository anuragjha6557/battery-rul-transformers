"""PLAN_PHASE2 §4.1 / ADR-0019: adaptive conformal intervals, re-scored post hoc on existing runs.

No retraining: every benchmark unit stores test predictions (``predictions.parquet``) and each
cross-fit sub-model's predictions on its own held-out training cell
(``inner_val_predictions.parquet``). From those, four calibration methods are compared:

* ``cqr``         one additive correction per horizon (the current method);
* ``mondrian``    one additive correction per (horizon, bin of the model's own predicted SOH);
                  bins are quartiles of the calibration predictions, so the rule is causal;
* ``scaled``      multiplicative CQR: scores ``max(lo-y, y-hi) / (hi-lo)``, interval
                  ``[lo - c w, hi + c w]`` with ``w = hi - lo`` (wider where the model says so);
* ``mondrian_scaled`` both. For RUL, ``log`` calibrates in log1p(cycles) space instead.

Metrics on the held-out cells: marginal PICP, mean width, the worst PICP over life-stage bins
(origin / EOL in [0, .25, .5, .75, 1], evaluation only), and the share of "useful" forecast
intervals (width < 50 % of the predicted distance to 80 % SOH).

Usage: uv run python scripts/interval_rescoring.py [--experiment benchmark]
    [--models ...] [--out NAME]
Writes reports/tables/<out>{,_summary}.csv (default out: interval_rescoring)
"""

from __future__ import annotations

import argparse
import math
import os
from pathlib import Path

import mlflow
import numpy as np
import pandas as pd

from battery_rul.uq.metrics_uq import wide_to_long

ALPHA = 0.1
MODELS = ("itransformer", "itransformer_sc", "lgbm", "lstm", "patchtst")
MIN_BIN = 30
LIFE_BINS = (0.0, 0.25, 0.5, 0.75, 1.0)


def _q(scores: np.ndarray) -> float:
    n = len(scores)
    k = math.ceil(round((n + 1) * (1 - ALPHA), 9))
    return float(np.sort(scores)[k - 1]) if 0 < k <= n else float("inf")


def _ok(d: pd.DataFrame) -> pd.DataFrame:
    m = d["mask"].astype(bool) & np.isfinite(d["y"]) & np.isfinite(d["lo"]) & np.isfinite(d["hi"])
    d = d[m].copy()
    d["lo"], d["hi"] = np.fmin(d["lo"], d["hi"]), np.fmax(d["lo"], d["hi"])
    return d


def calibrate(inner: pd.DataFrame, test: pd.DataFrame, method: str) -> pd.DataFrame:
    """Return ``test`` with lo_c / hi_c for one method (all horizons)."""
    out = []
    for h, te in test.groupby("horizon"):
        ca = inner[inner["horizon"] == h]
        te = te.copy()
        if method == "log":
            f, finv = np.log1p, np.expm1
            y, lo, hi = f(ca.y.clip(lower=0)), f(ca.lo.clip(lower=0)), f(ca.hi.clip(lower=0))
            c = _q(np.maximum(lo - y, y - hi).to_numpy())
            te["lo_c"] = finv(f(te.lo.clip(lower=0)) - c)
            te["hi_c"] = finv(f(te.hi.clip(lower=0)) + c)
            out.append(te)
            continue
        scaled = method in ("scaled", "mondrian_scaled")
        if method.startswith("mondrian") and len(ca) >= 2 * MIN_BIN:
            edges = np.unique(np.quantile(ca.point, [0, 0.25, 0.5, 0.75, 1]))
            nb = max(1, len(edges) - 1)
            ca_bin = np.clip(np.searchsorted(edges, ca.point, side="right") - 1, 0, nb - 1)
            te_bin = np.clip(np.searchsorted(edges, te.point, side="right") - 1, 0, nb - 1)
        else:
            ca_bin = np.zeros(len(ca), int)
            te_bin = np.zeros(len(te), int)
        lo_c, hi_c = te.lo.to_numpy().copy(), te.hi.to_numpy().copy()
        for b in np.unique(te_bin):
            cs = ca[ca_bin == b] if (ca_bin == b).sum() >= MIN_BIN else ca
            w = (cs.hi - cs.lo).clip(lower=1e-6) if scaled else 1.0
            c = _q((np.maximum(cs.lo - cs.y, cs.y - cs.hi) / w).to_numpy())
            sel = te_bin == b
            wt = (te.hi - te.lo).clip(lower=1e-6).to_numpy()[sel] if scaled else 1.0
            lo_c[sel] -= c * wt
            hi_c[sel] += c * wt
        te["lo_c"], te["hi_c"] = np.fmin(lo_c, hi_c), np.fmax(lo_c, hi_c)
        out.append(te)
    return pd.concat(out)


def score(d: pd.DataFrame, task: str) -> dict:
    cov = (d.y >= d.lo_c) & (d.y <= d.hi_c)
    width = d.hi_c - d.lo_c
    frac = (d.origin_cycle / d.eol_cycle).clip(0, 0.9999)
    life = pd.cut(frac, LIFE_BINS, include_lowest=True)
    per_bin = cov.groupby(life, observed=True).mean()
    r = {
        "picp": float(cov.mean()),
        "width": float(width.mean() * (100 if task != "rul" else 1)),
        "picp_worst_life_bin": float(per_bin.min()) if len(per_bin) else np.nan,
        "n": len(d),
    }
    if task != "rul":
        dist = (d.point - 0.8).clip(lower=0.005)
        r["useful_share"] = float((width < 0.5 * dist).mean())
    return r


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--experiment", default="benchmark")
    ap.add_argument("--models", nargs="*", default=list(MODELS))
    ap.add_argument("--out", default="interval_rescoring")
    args = ap.parse_args()
    mlflow.set_tracking_uri(
        os.environ.get("MLFLOW_TRACKING_URI", f"sqlite:///{Path.cwd() / 'mlflow.db'}")
    )
    runs = mlflow.search_runs(experiment_names=[args.experiment], max_results=10000)
    runs = runs[runs["tags.unit_key"].notna() & runs["params.model"].isin(args.models)]
    runs = runs[runs["params.task"].isin(["forecast", "rul"])]
    rows = []
    for _, r in runs.iterrows():
        try:
            p = pd.read_parquet(
                mlflow.artifacts.download_artifacts(
                    run_id=r.run_id, artifact_path="predictions.parquet"
                )
            )
            iv = pd.read_parquet(
                mlflow.artifacts.download_artifacts(
                    run_id=r.run_id, artifact_path="inner_val_predictions.parquet"
                )
            )
        except Exception:
            continue
        task = r["params.task"]
        test = _ok(wide_to_long(p[p.origin_policy == "all"], ALPHA))
        inner = _ok(wide_to_long(iv, ALPHA))
        if test.empty or inner.empty:
            continue
        methods = (
            ("cqr", "scaled", "log")
            if task == "rul"
            else ("cqr", "mondrian", "scaled", "mondrian_scaled")
        )
        for meth in methods:
            d = calibrate(inner, test, meth)
            for (split, h), g in d.groupby(["split", "horizon"]):
                rows.append(
                    {
                        "dataset": r["params.dataset"],
                        "split": split,
                        "task": task,
                        "model": r["params.model"],
                        "seed": r["params.seed"],
                        "horizon": h,
                        "method": meth,
                        **score(g, task),
                    }
                )
    res = pd.DataFrame(rows)
    out = Path(f"reports/tables/{args.out}.csv")
    res.to_csv(out, index=False)
    keep = res[(res.task == "rul") | (res.horizon == 50)]
    summ = (
        keep.groupby(["task", "dataset", "split", "method"])[
            ["picp", "picp_worst_life_bin", "width", "useful_share"]
        ]
        .mean()
        .round(3)
    )
    summ.to_csv(out.with_name(f"{args.out}_summary.csv"))
    print(summ.to_string())


if __name__ == "__main__":
    main()
