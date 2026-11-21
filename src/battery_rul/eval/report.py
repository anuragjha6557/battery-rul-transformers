"""Aggregate FINISHED unit runs of an experiment into result tables (PROTOCOL §8).

Metrics are recomputed **per cell** from each unit run's ``predictions.parquet`` artifact (the
runner's logged metrics are pooled over a test split and cannot support cell-level statistics):

* NASA / CALCE (LOCO, 4 cells): per-cell mean over seeds -> mean over cells with a 95 %
  cluster-bootstrap CI over cells, plus direction consistency vs the best baseline
  ("k/4 cells, k/n cell-seeds").
* Toyota: one value per test cell (separately for test1 and test2), mean + cluster-bootstrap CI
  over **cells**, plus a paired two-sided Wilcoxon signed-rank test vs the best baseline
  (Holm-adjusted across the non-baseline models of the same row group).
* Mean rank of every model across (dataset x task x headline metric) conditions.

"Best baseline" is the level-0 model (:data:`BASELINES`) with the best mean in the same row
group (dataset, task, split, policy, kind, metric); signed metrics (``rul_bias``) have no
direction and get no comparison.
"""

from __future__ import annotations

import hashlib
import logging
import re
from pathlib import Path

import numpy as np
import pandas as pd

from battery_rul.eval.metrics import alpha_lambda_accuracy, horizon_errors, rul_errors
from battery_rul.eval.stats import (
    cluster_bootstrap_ci,
    direction_consistency,
    mean_rank,
    wilcoxon_vs_baseline,
)
from battery_rul.splits.loco import independent_fold_cells
from battery_rul.utils import REPORTS_DIR

log = logging.getLogger("battery_rul.report")

NOTE = (
    "n = 4 cells per NASA/CALCE dataset, so the 95 % cluster-bootstrap CI is wide by "
    "construction. Toyota rows are over test cells (test1 / test2 separately) with a cell-level "
    "bootstrap CI and a Holm-adjusted Wilcoxon p vs the best baseline. All metrics are computed "
    "per cell from the logged predictions."
)
#: Level-0 reference models; the best of these (per row group) is the comparison baseline.
BASELINES = ("persistence", "last_slope", "prev_soh", "param_linear", "param_exp2", "param_power")
HEADLINE = ("rmse_h1", "rmse_h10", "rmse_h50")  # forecast headline (kept for compatibility)
HEADLINE_BY_TASK = {
    "forecast": HEADLINE,
    "soh": ("rmse",),
    "rul": ("rul_mae",),
}
HEADLINE_ALL = tuple(m for ms in HEADLINE_BY_TASK.values() for m in ms)
HIGHER_BETTER = ("alpha_lambda_acc",)
NO_DIRECTION = ("rul_bias",)

_PRED_COL = re.compile(r"^y_h(\d+)$")


def _runs(experiment_name: str, tracking_uri: str) -> pd.DataFrame:
    import mlflow

    mlflow.set_tracking_uri(tracking_uri)
    df = mlflow.search_runs(
        experiment_names=[experiment_name], filter_string="attributes.status = 'FINISHED'"
    )
    if df.empty or "tags.unit_key" not in df:
        raise ValueError(f"no finished unit runs in experiment {experiment_name!r}")
    return with_arm_labels(df[df["tags.unit_key"].notna()])


def with_arm_labels(runs: pd.DataFrame) -> pd.DataFrame:
    """Add ``arm``: the model name, plus the ``model.*`` params that differ between runs of the
    same (task, model). Ablations run one model in several arms (e.g. Huber vs MSE); grouping by
    model name alone would pool them. Benchmark entries (one config per task/model) keep the
    bare name."""
    runs = runs.copy()
    runs["arm"] = runs["params.model"].astype(str)
    # lookback is logged as a top-level param (not model.*) but is a model setting too
    pcols = [c for c in runs.columns if c.startswith("params.model.") or c == "params.lookback"]
    for _, g in runs.groupby(["params.task", "params.model"], sort=False):
        varying = [c for c in pcols if len(set(g[c].fillna("<default>"))) > 1]
        if not varying:
            continue
        for idx, r in g.iterrows():
            tag = ",".join(
                f"{c.removeprefix('params.model.').removeprefix('params.')}={r[c]}"
                for c in varying
                if pd.notna(r[c])
            )
            runs.loc[idx, "arm"] = f"{r['params.model']}[{tag or 'default'}]"
    return runs


# --------------------------------------------------------------------------------------
# Per-cell metrics from prediction frames
# --------------------------------------------------------------------------------------
def _horizons(frame: pd.DataFrame) -> list[int]:
    return sorted(int(m.group(1)) for c in frame.columns if (m := _PRED_COL.match(c)))


def _group_metrics(g: pd.DataFrame, task: str, kind: str, horizons: list[int]) -> dict[str, float]:
    y = g[[f"y_h{h}" for h in horizons]].to_numpy(dtype=np.float64)
    p = g[[f"point_h{h}" for h in horizons]].to_numpy(dtype=np.float64)
    ym = g[[f"y_mask_h{h}" for h in horizons]].to_numpy(dtype=bool)
    out: dict[str, float] = {}
    if task == "forecast":
        for h, v in horizon_errors(y, p, ym, horizons).items():
            out[f"rmse_h{h}"] = v["rmse"]
    elif task == "soh":
        sel = ym[:, 0]
        if sel.any():
            out["rmse"] = float(np.sqrt(np.mean((p[sel, 0] - y[sel, 0]) ** 2)) * 100.0)
    else:
        sel = ym[:, 0] & (y[:, 0] > 0)
        if sel.any():
            e = rul_errors(y[sel, 0], p[sel, 0])
            out["rul_mae"], out["rul_bias"] = e.mae, e.bias
            if kind.startswith("frac:"):
                out["alpha_lambda_acc"] = alpha_lambda_accuracy(y[sel, 0], p[sel, 0])
    return {k: float(v) for k, v in out.items() if np.isfinite(v)}


def cell_metrics(frame: pd.DataFrame, task: str) -> pd.DataFrame:
    """Per-cell metrics from one unit run's prediction frame.

    Returns rows ``(split, policy, kind, cell, metric, value)`` where ``kind`` is ``overall``
    or a start kind (``fixed:100``, ``frac:0.5``, ...); ``split`` is the frame's split tag
    (``test`` is renamed ``loco``).
    """
    horizons = _horizons(frame)
    rows: list[dict[str, object]] = []
    keys = ["split", "origin_policy", "cell_id"]
    for (split, policy, cell), g in frame.groupby(keys, sort=True):
        kinds = g["start_kind"].astype(str).to_numpy()
        groups = {"overall": g}
        for k in sorted(set(kinds) - {"all"}):
            groups[k] = g[kinds == k]
        for kind, gk in groups.items():
            for metric, v in _group_metrics(gk, task, kind, horizons).items():
                rows.append(
                    {
                        "split": "loco" if split == "test" else split,
                        "policy": policy,
                        "kind": kind,
                        "cell": str(cell),
                        "metric": metric,
                        "value": v,
                    }
                )
    return pd.DataFrame(rows, columns=["split", "policy", "kind", "cell", "metric", "value"])


def _long(runs: pd.DataFrame) -> pd.DataFrame:
    """Per-cell long table over all runs (run x split x policy x kind x cell x metric)."""
    import mlflow

    parts = []
    for _, r in runs.iterrows():
        try:
            path = mlflow.artifacts.download_artifacts(
                run_id=r["run_id"], artifact_path="predictions.parquet"
            )
        except Exception as e:  # missing artifact: report the gap instead of failing the table
            log.warning("run %s has no predictions artifact (%s); skipped", r["run_id"], e)
            continue
        cm = cell_metrics(pd.read_parquet(path), str(r["params.task"]))
        cm = cm.assign(
            dataset=r["params.dataset"],
            task=r["params.task"],
            model=r.get("arm", r["params.model"]),
            seed=int(r["params.seed"]),
            run_id=r["run_id"],
        )
        parts.append(cm)
    if not parts:
        raise ValueError("no prediction artifacts found for any finished run")
    return pd.concat(parts, ignore_index=True)


# --------------------------------------------------------------------------------------
# Aggregation
# --------------------------------------------------------------------------------------
def _group_id(run_ids: list[str]) -> str:
    return hashlib.sha256(",".join(sorted(run_ids)).encode()).hexdigest()[:8]


def _direction(metric: str) -> str | None:
    if metric in NO_DIRECTION:
        return None
    return "higher" if metric in HIGHER_BETTER else "lower"


def _aggregate_group(ds: str, task: str, keys: tuple[str, ...], grp: pd.DataFrame) -> list[dict]:
    """Rows for one (split, policy, kind, metric) group: one row per model."""
    split, policy, kind, metric = keys
    direction = _direction(metric)
    by_model: dict[str, pd.DataFrame] = {str(m): g for m, g in grp.groupby("model", sort=True)}
    cell_mean = {m: g.groupby("cell")["value"].mean() for m, g in by_model.items()}
    seed_vals = {
        m: {str(c): dict(zip(cg["seed"], cg["value"], strict=True)) for c, cg in g.groupby("cell")}
        for m, g in by_model.items()
    }
    base: str | None = None
    cands = [m for m in cell_mean if m in BASELINES]
    if direction is not None and cands:
        sign = 1.0 if direction == "lower" else -1.0
        base = min(cands, key=lambda m: sign * float(cell_mean[m].mean()))

    toyota = ds == "toyota"
    # Toyota Wilcoxon: paired over cells common to every model in the group, Holm over models.
    p_adj: dict[str, float] = {}
    if toyota and base is not None and len(cell_mean) > 1:
        common = sorted(set.intersection(*(set(s.index) for s in cell_mean.values())))
        others = {m: cell_mean[m].loc[common].to_numpy() for m in cell_mean if m != base}
        if len(common) >= 2 and others:
            try:
                p_adj = wilcoxon_vs_baseline(cell_mean[base].loc[common].to_numpy(), others)
            except ValueError as e:
                log.warning("wilcoxon skipped for %s/%s %s: %s", ds, task, keys, e)

    rows = []
    for model, g in by_model.items():
        pc = cell_mean[model]
        ids = sorted(g["run_id"].unique())
        row: dict[str, object] = {
            "dataset": ds,
            "task": task,
            "split": split,
            "policy": policy,
            "kind": kind,
            "metric": metric,
            "model": model,
            "n_cells": len(pc),
            "n_seeds": g["seed"].nunique(),
            "mean": float(pc.mean()),
            "ci_lo": np.nan,
            "ci_hi": np.nan,
            "independent": np.nan,
            "baseline": base if base != model else "",
            "consistency": "",
            "k_cells": np.nan,
            "k_pairs": np.nan,
            "n_pairs": np.nan,
            "p_holm": p_adj.get(model, np.nan),
            "run_group": _group_id(ids),
            "run_ids": ",".join(ids),
        }
        if len(pc) >= 2:
            ci = cluster_bootstrap_ci({str(c): [v] for c, v in pc.items()})
            row["ci_lo"], row["ci_hi"] = ci.lo, ci.hi
        if split == "loco" and ds == "nasa":
            ind = [c for c in pc.index if c in independent_fold_cells("nasa")]
            if ind:
                row["independent"] = float(pc[ind].mean())
        if not toyota and base is not None and model != base:
            cells = sorted(set(seed_vals[model]) & set(seed_vals[base]))
            if cells:
                mv: dict[str, list[float]] = {}
                bv: dict[str, list[float]] = {}
                for c in cells:
                    seeds = sorted(seed_vals[model][c])
                    mv[c] = [seed_vals[model][c][s] for s in seeds]
                    bmean = float(cell_mean[base][c])
                    # baselines with fewer seeds (deterministic models) are broadcast
                    bv[c] = [seed_vals[base][c].get(s, bmean) for s in seeds]
                cons = direction_consistency(mv, bv, lower_is_better=direction == "lower")
                row["consistency"] = (
                    f"{cons.k_cells}/{cons.n_cells} cells, {cons.k_pairs}/{cons.n_pairs} cell-seeds"
                )
                row["k_cells"], row["k_pairs"], row["n_pairs"] = (
                    cons.k_cells,
                    cons.k_pairs,
                    cons.n_pairs,
                )
        rows.append(row)
    return rows


def make_tables(experiment_name: str, tracking_uri: str) -> dict[str, pd.DataFrame]:
    """``{"<dataset>_<task>": table}``; one row per (split, policy, kind, metric, model)."""
    long = _long(_runs(experiment_name, tracking_uri))
    return tables_from_long(long)


def tables_from_long(long: pd.DataFrame) -> dict[str, pd.DataFrame]:
    out: dict[str, pd.DataFrame] = {}
    for (ds, task), sub in long.groupby(["dataset", "task"], sort=True):
        rows: list[dict] = []
        for keys, grp in sub.groupby(["split", "policy", "kind", "metric"], sort=True):
            rows += _aggregate_group(str(ds), str(task), tuple(map(str, keys)), grp)
        out[f"{ds}_{task}"] = pd.DataFrame(rows)
    return out


def rank_table(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Mean rank per model over (dataset, task, split, policy, headline metric) conditions.

    Only ``kind == overall`` rows of the headline metrics enter; lower is better.
    """
    all_rows = pd.concat(tables.values(), ignore_index=True)
    sel = all_rows[(all_rows["kind"] == "overall") & all_rows["metric"].isin(HEADLINE_ALL)]
    if sel.empty:
        return pd.DataFrame(columns=["model", "mean_rank", "n_conditions", "n_missing"])
    cond = sel[["dataset", "task", "split", "policy", "metric"]].astype(str).agg("/".join, axis=1)
    mat = sel.assign(cond=cond.to_numpy()).pivot_table(
        index="model", columns="cond", values="mean", aggfunc="first", dropna=False
    )
    ranks = mean_rank(mat)
    miss = ranks.attrs["n_missing"]
    out = pd.DataFrame(
        {
            "model": ranks.index,
            "mean_rank": ranks.to_numpy(),
            "n_conditions": [int(mat.loc[m].notna().sum()) for m in ranks.index],
            "n_missing": [miss[str(m)] for m in ranks.index],
        }
    )
    return out.sort_values("mean_rank").reset_index(drop=True)


# --------------------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------------------
def _vs_baseline(r: pd.Series) -> str:
    if not r["baseline"]:
        return ""
    if r["consistency"]:
        return f"{r['consistency']} (vs {r['baseline']})"
    if not pd.isna(r["p_holm"]):
        return f"p={r['p_holm']:.3g} (vs {r['baseline']})"
    return f"(vs {r['baseline']})"


def _fmt(df: pd.DataFrame) -> str:
    d = df.copy()
    d["mean [95% CI]"] = [
        f"{m:.3f}" if np.isnan(lo) else f"{m:.3f} [{lo:.3f}, {hi:.3f}]"
        for m, lo, hi in zip(d["mean"], d["ci_lo"], d["ci_hi"], strict=True)
    ]
    d["vs best baseline"] = [_vs_baseline(r) for _, r in d.iterrows()]
    d["indep. (B0018)"] = d["independent"].map(lambda v: "" if pd.isna(v) else f"{v:.3f}")
    cols = [
        "split",
        "policy",
        "kind",
        "metric",
        "model",
        "mean [95% CI]",
        "vs best baseline",
        "indep. (B0018)",
        "n_cells",
        "n_seeds",
        "run_group",
    ]
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    lines += ["| " + " | ".join(str(v) for v in r) + " |" for r in d[cols].itertuples(index=False)]
    return "\n".join(lines)


def _fmt_rank(df: pd.DataFrame) -> str:
    lines = ["| model | mean rank | conditions | missing |", "|---|---|---|---|"]
    lines += [
        f"| {r.model} | {r.mean_rank:.2f} | {r.n_conditions} | {r.n_missing} |"
        for r in df.itertuples(index=False)
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------------------
# Calibration (PROTOCOL §5): raw vs CQR-calibrated interval metrics, reliability diagrams
# --------------------------------------------------------------------------------------
CAL_PALETTE = ("#2a78d6", "#eb6834", "#1baf7a")
CAL_COLS = ["raw_picp", "cal_picp", "raw_mpiw", "cal_mpiw", "raw_iscore", "cal_iscore"]


def calibration_long(runs: pd.DataFrame) -> pd.DataFrame:
    """Per-cell raw/calibrated PICP, MPIW, interval score from ``calibrated_predictions``.

    Rows: ``(dataset, task, model, seed, run_id, split, policy, kind, cell, horizon)`` with
    columns ``raw_picp, cal_picp, raw_mpiw, cal_mpiw, raw_iscore, cal_iscore`` (MPIW and interval
    score in %SOH for soh/forecast, cycles for rul).
    """
    import mlflow

    from battery_rul.uq.metrics_uq import interval_table, scale_for

    parts = []
    keys = ["split", "policy", "kind", "cell", "horizon"]
    for _, r in runs.iterrows():
        try:
            path = mlflow.artifacts.download_artifacts(
                run_id=r["run_id"], artifact_path="calibrated_predictions.parquet"
            )
        except Exception:
            continue
        cp = pd.read_parquet(path)
        task, alpha = str(r["params.task"]), float(cp["alpha"].iloc[0])
        sc = scale_for(task)
        tabs = {}
        if cp["lo"].notna().any():
            tabs["raw"] = interval_table(cp, "lo", "hi", alpha, sc)
        if cp["lo_cal"].notna().any():
            tabs["cal"] = interval_table(cp, "lo_cal", "hi_cal", alpha, sc)
        if not tabs:
            continue
        merged: pd.DataFrame | None = None
        for tag, t in tabs.items():
            t = t[[*keys, "picp", "mpiw", "iscore"]].rename(
                columns={m: f"{tag}_{m}" for m in ("picp", "mpiw", "iscore")}
            )
            merged = t if merged is None else merged.merge(t, on=keys, how="outer")
        assert merged is not None
        for c in CAL_COLS:
            if c not in merged:
                merged[c] = np.nan
        parts.append(
            merged.assign(
                dataset=r["params.dataset"],
                task=task,
                model=r.get("arm", r["params.model"]),
                seed=int(r["params.seed"]),
                run_id=r["run_id"],
            )
        )
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()


def calibration_table(long: pd.DataFrame) -> pd.DataFrame:
    """Mean over seeds per cell, then mean + 95 % cluster-bootstrap CI over cells.

    One row per ``(dataset, task, split, policy, kind, horizon, model)``; CI columns are
    ``<metric>_lo/_hi`` (NaN with < 2 cells).
    """
    if long.empty:
        return pd.DataFrame()
    rows = []
    gk = ["dataset", "task", "split", "policy", "kind", "horizon", "model"]
    for key, g in long.groupby(gk, sort=True):
        row: dict[str, object] = dict(zip(gk, key, strict=True))
        row["n_cells"] = g["cell"].nunique()
        for c in CAL_COLS:
            pc = g.groupby("cell")[c].mean().dropna()
            row[c] = float(pc.mean()) if len(pc) else np.nan
            lo = hi = np.nan
            if len(pc) >= 2:
                ci = cluster_bootstrap_ci({str(k): [v] for k, v in pc.items()})
                lo, hi = ci.lo, ci.hi
            row[f"{c}_lo"], row[f"{c}_hi"] = lo, hi
        row["run_ids"] = ",".join(sorted(g["run_id"].unique()))
        rows.append(row)
    return pd.DataFrame(rows)


def _ci(m: float, lo: float, hi: float) -> str:
    if np.isnan(m):
        return "-"
    return f"{m:.3f}" if np.isnan(lo) else f"{m:.3f} [{lo:.3f}, {hi:.3f}]"


def _fmt_cal(df: pd.DataFrame) -> str:
    cols = ["dataset", "task", "policy", "horizon", "model", "PICP raw", "PICP cal"]
    cols += ["MPIW raw", "MPIW cal", "cells"]
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for d in df.to_dict("records"):
        cells = [
            d["dataset"], d["task"], d["policy"], d["horizon"], d["model"],
            _ci(d["raw_picp"], d["raw_picp_lo"], d["raw_picp_hi"]),
            _ci(d["cal_picp"], d["cal_picp_lo"], d["cal_picp_hi"]),
            _ci(d["raw_mpiw"], d["raw_mpiw_lo"], d["raw_mpiw_hi"]),
            _ci(d["cal_mpiw"], d["cal_mpiw_lo"], d["cal_mpiw_hi"]),
            d["n_cells"],
        ]  # fmt: skip
        lines.append("| " + " | ".join(str(c) for c in cells) + " |")
    return "\n".join(lines)


def reliability_long(runs: pd.DataFrame) -> pd.DataFrame:
    """Per-run reliability rows (``calibration_reliability.parquet``) with run identifiers."""
    import mlflow

    parts = []
    for _, r in runs.iterrows():
        try:
            path = mlflow.artifacts.download_artifacts(
                run_id=r["run_id"], artifact_path="calibration_reliability.parquet"
            )
        except Exception:
            continue
        parts.append(
            pd.read_parquet(path).assign(
                dataset=r["params.dataset"],
                task=r["params.task"],
                model=r.get("arm", r["params.model"]),
            )
        )
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()


def plot_reliability(rel: pd.DataFrame, out_dir: Path, experiment: str) -> list[Path]:
    """One PNG per dataset: empirical vs nominal coverage, raw (dashed) and calibrated (solid).

    Pooled over tasks, horizons, cells and seeds (``policy == "all"`` when present). One y-axis,
    diagonal = perfect calibration, colour = model.
    """
    if rel.empty:
        return []
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for ds, d in rel.groupby("dataset", sort=True):
        if (d["policy"] == "all").any():
            d = d[d["policy"] == "all"]
        agg = (
            d.assign(nominal=1.0 - d["alpha"])
            .groupby(["model", "nominal"], sort=True)[["raw_picp", "cal_picp"]]
            .mean()
            .reset_index()
        )
        with plt.rc_context(
            {
                "axes.spines.top": False,
                "axes.spines.right": False,
                "axes.grid": True,
                "grid.alpha": 0.3,
                "legend.frameon": False,
                "legend.fontsize": 8,
            }
        ):
            fig, ax = plt.subplots(figsize=(4.6, 4.2))
            ax.plot([0, 1], [0, 1], color="#76746f", lw=1, label="ideal")
            models = sorted(agg["model"].unique())
            for i, m in enumerate(models):
                a = agg[agg["model"] == m]
                col = CAL_PALETTE[i % len(CAL_PALETTE)]
                for var, ls in (("cal_picp", "-"), ("raw_picp", "--")):
                    v = a.dropna(subset=[var])
                    if len(v):
                        ax.plot(v["nominal"], v[var], ls, color=col, marker="o", ms=4, lw=1.6)
            handles = [Line2D([], [], color="#76746f", lw=1, label="ideal")]
            handles += [
                Line2D([], [], color=CAL_PALETTE[i % len(CAL_PALETTE)], lw=1.6, label=m)
                for i, m in enumerate(models)
            ]
            handles += [
                Line2D([], [], color="#3b3a37", ls="-", label="calibrated (CQR)"),
                Line2D([], [], color="#3b3a37", ls="--", label="raw quantiles"),
            ]
            ax.set(
                xlim=(0, 1),
                ylim=(0, 1),
                xlabel="nominal coverage",
                ylabel="empirical coverage (PICP)",
                title=f"{ds}: reliability",
            )
            ax.legend(handles=handles, loc="upper left")
            p = out_dir / f"{experiment}_reliability_{ds}.png"
            fig.savefig(p, dpi=150, bbox_inches="tight")
            plt.close(fig)
        paths.append(p)
    return paths


def write_report(
    experiment_name: str, tracking_uri: str, out_dir: Path | None = None
) -> tuple[Path, Path]:
    runs = _runs(experiment_name, tracking_uri)
    tables = tables_from_long(_long(runs))
    ranks = rank_table(tables)
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
    body = ["## Headline (kind = overall; RMSE in %SOH, RUL MAE in cycles)", ""]
    full = ["## Full tables", ""]
    for key, t in tables.items():
        h = t[t["metric"].isin(HEADLINE_ALL) & (t["kind"] == "overall")]
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
    rank_md = ["## Mean rank (dataset x task x split x policy x headline metric)", ""]
    rank_md += [_fmt_rank(ranks), ""] if not ranks.empty else ["_no headline conditions_", ""]
    cal_md: list[str] = []
    cal_long = calibration_long(runs)
    if not cal_long.empty:
        cal = calibration_table(cal_long)
        sel = cal[(cal["kind"] == "overall") & (cal["split"].isin(["loco", "test1", "test2"]))]
        figs = plot_reliability(reliability_long(runs), out_dir.parent / "figures", experiment_name)
        cal_md = [
            "## Calibration (90 % intervals; PICP target 0.90 +/- 0.05; MPIW in %SOH or cycles)",
            "",
            "Raw = stored (0.05, 0.95) quantiles; cal = CQR with pooled inner-val residuals "
            "(PROTOCOL §3/§5). Models without inner-val predictions (GPR) have raw only. "
            "mean [95% cluster-bootstrap CI over cells].",
            "",
            _fmt_cal(sel),
            "",
            *[f"![reliability]({f.relative_to(out_dir.parent)})" for f in figs],
            "",
        ]
        cal.to_csv(out_dir / f"{experiment_name}_calibration.csv", index=False)
    md = out_dir / f"{experiment_name}.md"
    md.write_text("\n".join(head + body + rank_md + cal_md + full))
    csv = out_dir / f"{experiment_name}.csv"
    pd.concat(tables.values(), ignore_index=True).to_csv(csv, index=False)
    ranks.to_csv(out_dir / f"{experiment_name}_ranks.csv", index=False)
    return md, csv
