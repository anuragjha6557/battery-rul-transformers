"""Paired comparison of two benchmark arms under the PLAN §6.5 decision rule.

An arm is ``experiment:model_label`` (labels as written by ``battery-rul report``, e.g.
``abl_norm_loss:itransformer[loss=huber]`` or ``benchmark:itransformer``). For every dataset and
split, runs are paired on (test cell, seed); the reported delta is candidate minus reference
(negative = candidate better for error metrics).

- Toyota: cluster-bootstrap 95 % CI of the per-cell delta + Wilcoxon signed-rank on per-cell means.
- NASA/CALCE: k/4 cells (and k/20 cell-seed pairs) where the candidate is better.

Usage:
    uv run python scripts/compare_arms.py --task forecast --metric rmse_h50 \
        --pair abl_norm_loss:itransformer[loss=huber] abl_norm_loss:itransformer[loss=mse] ...
Writes reports/tables/<out>.csv and .md.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

from battery_rul.eval.report import _long, _runs
from battery_rul.eval.stats import cluster_bootstrap_ci, direction_consistency

URI = os.environ.get("MLFLOW_TRACKING_URI", f"sqlite:///{Path.cwd() / 'mlflow.db'}")
_cache: dict[str, pd.DataFrame] = {}


def arm_long(arm: str, task: str, metric: str, policy: str) -> pd.DataFrame:
    exp, label = arm.split(":", 1)
    if exp not in _cache:
        _cache[exp] = _runs(exp, URI)
    runs = _cache[exp]
    runs = runs[(runs["params.task"] == task) & (runs["arm"] == label)]
    if runs.empty:
        raise SystemExit(f"no runs for {arm} ({task})")
    lg = _long(runs)
    lg = lg[(lg["metric"] == metric) & (lg["policy"] == policy) & (lg["kind"] == "overall")]
    return lg[["dataset", "split", "cell", "seed", "value"]]


def compare(cand: str, ref: str, task: str, metric: str, policy: str) -> list[dict]:
    a, b = arm_long(cand, task, metric, policy), arm_long(ref, task, metric, policy)
    m = a.merge(b, on=["dataset", "split", "cell", "seed"], suffixes=("_c", "_r"))
    out = []
    for (ds, split), g in m.groupby(["dataset", "split"], sort=True):
        g = g[g["cell"] != "__all__"] if "__all__" in set(g["cell"]) else g
        seeds = sorted(set.intersection(*(set(s) for _, s in g.groupby("cell")["seed"])))
        g = g[g["seed"].isin(seeds)].sort_values(["cell", "seed"])
        cand_by = {c: cg["value_c"].to_numpy() for c, cg in g.groupby("cell")}
        ref_by = {c: cg["value_r"].to_numpy() for c, cg in g.groupby("cell")}
        delta = {c: cand_by[c] - ref_by[c] for c in cand_by}
        ci = cluster_bootstrap_ci(delta)
        cons = direction_consistency(cand_by, ref_by)
        per_cell = np.array([d.mean() for d in delta.values()])
        p = float(wilcoxon(per_cell).pvalue) if len(per_cell) >= 10 else np.nan
        out.append(
            {
                "candidate": cand,
                "reference": ref,
                "dataset": ds,
                "split": split,
                "metric": metric,
                "policy": policy,
                "cand_mean": float(np.mean(np.concatenate(list(cand_by.values())))),
                "ref_mean": float(np.mean(np.concatenate(list(ref_by.values())))),
                "delta": ci.estimate,
                "ci_lo": ci.lo,
                "ci_hi": ci.hi,
                "k_cells": f"{cons.k_cells}/{cons.n_cells}",
                "k_pairs": f"{cons.k_pairs}/{cons.n_pairs}",
                "wilcoxon_p": p,
                "n_seeds": len(seeds),
            }
        )
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--metric", action="append", required=True)
    ap.add_argument("--policy", default="all")
    ap.add_argument("--pair", nargs=2, action="append", metavar=("CAND", "REF"), required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    rows = [
        r
        for metric in args.metric
        for cand, ref in args.pair
        for r in compare(cand, ref, args.task, metric, args.policy)
    ]
    df = pd.DataFrame(rows)
    out = Path("reports/tables") / args.out
    df.to_csv(out.with_suffix(".csv"), index=False)
    md = df.assign(
        **{
            "delta [95% CI]": [
                f"{d:+.3f} [{lo:+.3f}, {hi:+.3f}]"
                for d, lo, hi in zip(df.delta, df.ci_lo, df.ci_hi, strict=True)
            ]
        }
    )[
        [
            "candidate",
            "reference",
            "dataset",
            "split",
            "metric",
            "cand_mean",
            "ref_mean",
            "delta [95% CI]",
            "k_cells",
            "k_pairs",
            "wilcoxon_p",
        ]
    ]
    fmt = md.map(lambda v: f"{v:.3g}" if isinstance(v, float) else str(v))
    lines = ["| " + " | ".join(fmt.columns) + " |", "|" + "---|" * len(fmt.columns)]
    lines += ["| " + " | ".join(row) + " |" for row in fmt.to_numpy().tolist()]
    out.with_suffix(".md").write_text("\n".join(lines) + "\n")
    print(md.to_string(index=False))


if __name__ == "__main__":
    main()
