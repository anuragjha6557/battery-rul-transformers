"""Aggregate FINISHED unit runs of an experiment into result tables (PROTOCOL §8).

NASA/CALCE: per-cell mean over seeds, then mean + 95 % cluster-bootstrap CI over cells.
Toyota: one row per official test split (mean over seeds; no cell-level CI is available
because metrics are logged per split, not per cell).
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import numpy as np
import pandas as pd

from battery_rul.eval.stats import cluster_bootstrap_ci
from battery_rul.splits.loco import independent_fold_cells
from battery_rul.utils import REPORTS_DIR

NOTE = (
    "n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by "
    "construction. Toyota rows are per official test split (mean over seeds, no CI)."
)
HEADLINE = ("rmse_h1", "rmse_h10", "rmse_h50")
ROW_KEYS = ["dataset", "task", "split", "policy", "kind", "metric", "model"]


def _runs(experiment_name: str, tracking_uri: str) -> pd.DataFrame:
    import mlflow

    mlflow.set_tracking_uri(tracking_uri)
    df = mlflow.search_runs(
        experiment_names=[experiment_name], filter_string="attributes.status = 'FINISHED'"
    )
    if df.empty or "tags.unit_key" not in df:
        raise ValueError(f"no finished unit runs in experiment {experiment_name!r}")
    return df[df["tags.unit_key"].notna()]


def _long(runs: pd.DataFrame) -> pd.DataFrame:
    rows = []
    mcols = [c for c in runs.columns if c.startswith("metrics.") and c.count("/") == 3]
    for _, r in runs.iterrows():
        for c in mcols:
            v = r[c]
            if pd.isna(v):
                continue
            split, policy, kind, metric = c.removeprefix("metrics.").split("/")
            fold = r["params.fold"]
            cell = fold if split == "test" else split
            rows.append(
                {
                    "dataset": r["params.dataset"],
                    "task": r["params.task"],
                    "model": r["params.model"],
                    "split": "loco" if split == "test" else split,
                    "cell": cell,
                    "seed": int(r["params.seed"]),
                    "policy": policy,
                    "kind": kind,
                    "metric": metric,
                    "value": float(v),
                    "run_id": r["run_id"],
                    "independent": r["params.independent_fold"] == "True",
                }
            )
    return pd.DataFrame(rows)


def _group_id(run_ids: list[str]) -> str:
    return hashlib.sha256(",".join(sorted(run_ids)).encode()).hexdigest()[:8]


def make_tables(experiment_name: str, tracking_uri: str) -> dict[str, pd.DataFrame]:
    """``{"<dataset>_<task>": table}`` with one row per (split, policy, kind, metric, model)."""
    runs = _runs(experiment_name, tracking_uri)
    long = _long(runs)
    out: dict[str, pd.DataFrame] = {}
    for (ds, task), sub in long.groupby(["dataset", "task"], sort=True):
        rows = []
        for keys, g in sub.groupby(["split", "policy", "kind", "metric", "model"], sort=True):
            split, policy, kind, metric, model = keys
            per_cell = g.groupby("cell")["value"].mean()
            ids = sorted(g["run_id"].unique())
            row: dict[str, object] = {
                "dataset": ds,
                "task": task,
                "split": split,
                "policy": policy,
                "kind": kind,
                "metric": metric,
                "model": model,
                "n_cells": len(per_cell),
                "n_seeds": g["seed"].nunique(),
                "mean": float(per_cell.mean()),
                "ci_lo": np.nan,
                "ci_hi": np.nan,
                "independent": np.nan,
                "run_group": _group_id(ids),
                "run_ids": ",".join(ids),
            }
            if split == "loco" and len(per_cell) >= 2:
                ci = cluster_bootstrap_ci({str(c): [v] for c, v in per_cell.items()})
                row["ci_lo"], row["ci_hi"] = ci.lo, ci.hi
            if split == "loco" and ds == "nasa":
                ind = [c for c in per_cell.index if c in independent_fold_cells("nasa")]
                if ind:
                    row["independent"] = float(per_cell[ind].mean())
            rows.append(row)
        out[f"{ds}_{task}"] = pd.DataFrame(rows)
    return out


def _fmt(df: pd.DataFrame) -> str:
    d = df.copy()
    d["mean [95% CI]"] = [
        f"{m:.3f}" if np.isnan(lo) else f"{m:.3f} [{lo:.3f}, {hi:.3f}]"
        for m, lo, hi in zip(d["mean"], d["ci_lo"], d["ci_hi"], strict=True)
    ]
    d["indep. (B0018)"] = d["independent"].map(lambda v: "" if pd.isna(v) else f"{v:.3f}")
    cols = [
        "split",
        "policy",
        "kind",
        "metric",
        "model",
        "mean [95% CI]",
        "indep. (B0018)",
        "n_cells",
        "n_seeds",
        "run_group",
    ]
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    lines += ["| " + " | ".join(str(v) for v in r) + " |" for r in d[cols].itertuples(index=False)]
    return "\n".join(lines)


def write_report(
    experiment_name: str, tracking_uri: str, out_dir: Path | None = None
) -> tuple[Path, Path]:
    runs = _runs(experiment_name, tracking_uri)
    tables = make_tables(experiment_name, tracking_uri)
    out_dir = out_dir or REPORTS_DIR / "tables"
    out_dir.mkdir(parents=True, exist_ok=True)
    shas = sorted(set(runs["params.git_sha"].dropna().str[:10]))
    head = [
        f"# Benchmark tables: {experiment_name}",
        "",
        f"- Protocol version: {', '.join(sorted(set(runs['params.protocol_version'].dropna())))}",
        f"- Git SHA: {', '.join(shas)}",
        f"- Seeds: {runs['params.seed'].nunique()}  |  unit runs: {len(runs)}",
        f"- Note: {NOTE}",
        "",
    ]
    body = ["## Headline (forecast RMSE, %SOH, kind = overall)", ""]
    full = ["## Full tables", ""]
    for key, t in tables.items():
        h = t[t["metric"].isin(HEADLINE) & (t["kind"] == "overall")]
        if not h.empty:
            body += [f"### {key}", "", _fmt(h), ""]
        full += [
            f"<details><summary>{key} ({len(t)} rows)</summary>",
            "",
            _fmt(t),
            "",
            "</details>",
            "",
        ]
    md = out_dir / f"{experiment_name}.md"
    md.write_text("\n".join(head + body + full))
    csv = out_dir / f"{experiment_name}.csv"
    pd.concat(tables.values(), ignore_index=True).to_csv(csv, index=False)
    return md, csv
