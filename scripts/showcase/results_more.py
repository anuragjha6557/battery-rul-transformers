# ruff: noqa: E501
"""Build web/showcase/data/results_more.json: SOH/RUL dot plots, RUL scatter, calibration, ablations.

Units: SOH errors and interval widths in %SOH, RUL in cycles. MLflow is read-only (item 3 only).
"""

from __future__ import annotations

import json
from pathlib import Path

import mlflow
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / "reports/tables"
OUT = ROOT / "web/showcase/data/results_more.json"
mlflow.set_tracking_uri(f"sqlite:///{ROOT / 'mlflow.db'}")

PANELS = [
    ("calce", "loco", "CALCE"),
    ("nasa", "loco", "NASA"),
    ("toyota", "test1", "Toyota test 1"),
    ("toyota", "test2", "Toyota test 2"),
]
SCATTER_MODELS = ["itransformer", "lgbm", "itransformer_sc"]
SEEDS = [0, 1, 2, 3, 4]


def r(x: float, d: int = 4) -> float | None:
    return None if x is None or pd.isna(x) else round(float(x), d)


bench = pd.read_csv(T / "benchmark.csv")
local = pd.read_csv(T / "benchmark_local.csv")
calib = pd.read_csv(T / "benchmark_calibration.csv")
ranks = pd.read_csv(T / "benchmark_ranks.csv").sort_values(["mean_rank", "model"])
ORDER = ranks.model.tolist()
rank_of = dict(zip(ranks.model, ranks.mean_rank, strict=True))


def sel(df: pd.DataFrame, ds: str, sp: str, **kw: str) -> pd.DataFrame:
    q = df[(df.dataset == ds) & (df.split == sp)]
    for k, v in kw.items():
        q = q[q[k] == v]
    return q


def dot_panels(task: str, metric: str, policy: str, with_local: bool) -> list[dict]:
    out = []
    for ds, sp, label in PANELS:
        rows = []
        srcs = [(bench, False)] + ([(local, True)] if with_local else [])
        for df, is_local in srcs:
            q = sel(df, ds, sp, task=task, metric=metric, policy=policy, kind="overall")
            for _, x in q.iterrows():
                rows.append(
                    {
                        "model": x.model,
                        "mean": r(x["mean"]),
                        "lo": r(x.ci_lo),
                        "hi": r(x.ci_hi),
                        "local": is_local,
                    }
                )
        out.append({"label": label, "rows": rows})
    return out


# ---------------------------------------------------------------- 1, 2
soh = dot_panels("soh", "rmse", "all", False)
rul = dot_panels("rul", "rul_mae", "start_points", True)
local_models = sorted(set(local[local.metric == "rul_mae"].model))
order_rul = ORDER + local_models

# ---------------------------------------------------------------- 3: scatter
runs = mlflow.search_runs(
    experiment_names=["benchmark"],
    filter_string="params.task = 'rul' and params.dataset = 'toyota'",
    max_results=100000,
)
runs = runs[runs["status"] == "FINISHED"]
scatter: dict[str, dict] = {}
for _, run in runs.iterrows():
    if run["params.model"] not in SCATTER_MODELS or int(run["params.seed"]) not in SEEDS:
        continue
    p = mlflow.artifacts.download_artifacts(run_id=run.run_id, artifact_path="predictions.parquet")
    df = pd.read_parquet(p)
    df = df[(df.origin_policy == "start_points") & (df.start_kind == "fixed:100")]
    df = df[["cell_id", "split", "y_h0", "point_h0"]].assign(model=run["params.model"])
    scatter.setdefault("frames", []).append(df)  # type: ignore[arg-type]
allp = pd.concat(scatter["frames"], ignore_index=True)
sc_out: dict[str, dict[str, list]] = {}
for split in ["test1", "test2"]:
    sc_out[split] = {}
    for m in SCATTER_MODELS:
        q = allp[(allp.split == split) & (allp.model == m)]
        g = q.groupby("cell_id").agg(
            true=("y_h0", "mean"), pred=("point_h0", "mean"), n=("point_h0", "size")
        )
        g = g[g["true"] > 0].sort_index()
        sc_out[split][m] = [
            {"cell": str(c), "true": r(x["true"], 1), "pred": r(x.pred, 1), "n": int(x.n)}
            for c, x in g.iterrows()
        ]

# ---------------------------------------------------------------- 4, 5: calibration (h = 50)
c50 = calib[
    (calib.task == "forecast")
    & (calib.policy == "all")
    & (calib.kind == "overall")
    & (calib.horizon == 50)
]
quantile_models = [
    m for m in ORDER if m in set(c50.model) and (c50[c50.model == m].raw_mpiw > 0).any()
]
calib_out = []
for ds, sp, label in PANELS:
    rows = []
    for m in quantile_models:
        q = sel(c50, ds, sp, model=m)
        if q.empty:
            continue
        x = q.iloc[0]
        rows.append(
            {
                "model": m,
                "raw_picp": r(x.raw_picp),
                "cal_picp": r(x.cal_picp),
                "raw_mpiw": r(x.raw_mpiw, 3),
                "cal_mpiw": r(x.cal_mpiw, 3),
            }
        )
    calib_out.append({"label": label, "rows": rows})
WIDTH_MODELS = ["itransformer", "itransformer_sc", "lgbm", "patchtst", "lstm"]

# ---------------------------------------------------------------- 6: ablation forest
norm = pd.read_csv(T / "abl_norm_loss_paired.csv")
cf = pd.read_csv(T / "abl_curve_paired_forecast.csv")
cs = pd.read_csv(T / "abl_curve_paired_soh.csv")
tr = pd.read_csv(T / "transfer_paired_all.csv")
NL = "abl_norm_loss:"
SC = "transfer:itransformer+scratch"
SPECS = [
    ("RevIN · Transformer", norm, NL + "transformer", "benchmark:transformer", "rmse_h50"),
    ("RevIN · LSTM", norm, NL + "lstm[revin=True]", "benchmark:lstm", "rmse_h50"),
    (
        "Huber vs MSE · iTransformer",
        norm,
        NL + "itransformer[loss=huber]",
        NL + "itransformer[loss=mse]",
        "rmse_h50",
    ),
    (
        "Huber vs MSE · LSTM",
        norm,
        NL + "lstm[quantiles=None,loss=huber]",
        NL + "lstm[quantiles=None,loss=mse]",
        "rmse_h50",
    ),
    (
        "Point MSE vs quantile head · iTransformer",
        norm,
        NL + "itransformer[loss=mse]",
        "benchmark:itransformer",
        "rmse_h50",
    ),
    ("Curve features · LightGBM (forecast)", cf, "abl_curve:lgbm", "benchmark:lgbm", "rmse_h50"),
    (
        "Curve features · iTransformer (forecast)",
        cf,
        "abl_curve:itransformer",
        "benchmark:itransformer",
        "rmse_h50",
    ),
    ("Curve features · LightGBM (SOH)", cs, "abl_curve:lgbm", "benchmark:lgbm", "rmse"),
    (
        "Curve features · iTransformer (SOH)",
        cs,
        "abl_curve:itransformer",
        "benchmark:itransformer",
        "rmse",
    ),
    (
        "Toyota pre-train + full fine-tune (forecast)",
        tr,
        "transfer:itransformer+ft_full",
        SC,
        "rmse_h50",
    ),
    (
        "Toyota pre-train, head-only fine-tune (forecast)",
        tr,
        "transfer:itransformer+ft_head",
        SC,
        "rmse_h50",
    ),
    ("Toyota zero-shot (forecast)", tr, "transfer:itransformer+zero_shot", SC, "rmse_h50"),
]
abl_out = []
for label, df, cand, ref, metric in SPECS:
    cells = []
    for ds, sp, _ in PANELS:
        q = sel(df, ds, sp, candidate=cand, reference=ref, metric=metric, policy="all")
        if q.empty:
            cells.append(None)
            continue
        assert len(q) == 1, (label, ds, sp)
        x = q.iloc[0]
        cells.append(
            {
                "cand": r(x.cand_mean),
                "ref": r(x.ref_mean),
                "delta": r(x.delta),
                "lo": r(x.ci_lo),
                "hi": r(x.ci_hi),
                "k": str(x.k_cells),
            }
        )
    abl_out.append(
        {"label": label, "candidate": cand, "reference": ref, "metric": metric, "cells": cells}
    )

# ---------------------------------------------------------------- 7: direct vs recursive
rec = pd.read_csv(T / "abl_recursive.csv")
rec_out = []
for ds, sp, label in PANELS:
    if ds != "toyota" or sp == "test1":
        pass
    series: dict[str, list] = {"direct": [], "recursive": []}
    q = sel(rec, ds, sp, policy="all", kind="overall")
    for h in sorted({int(m.split("_h")[1]) for m in q.metric}):
        for name, src in [
            (
                "direct",
                sel(
                    bench,
                    ds,
                    sp,
                    task="forecast",
                    model="itransformer",
                    policy="all",
                    kind="overall",
                ),
            ),
            ("recursive", q),
        ]:
            x = src[src.metric == f"rmse_h{h}"]
            if len(x):
                x = x.iloc[0]
                series[name].append(
                    {"h": h, "mean": r(x["mean"]), "lo": r(x.ci_lo), "hi": r(x.ci_hi)}
                )
    rec_out.append({"label": label, "dataset": ds, **series})
rec_out = [p for p in rec_out]

# ---------------------------------------------------------------- 8: transfer
tf = pd.read_csv(T / "transfer.csv")
ARMS = ["scratch", "zero_shot", "ft_head", "ft_full", "few_shot"]
ARM_LABEL = {
    "scratch": "From scratch",
    "zero_shot": "Zero-shot",
    "ft_head": "Head-only fine-tune",
    "ft_full": "Full fine-tune",
    "few_shot": "Few-shot",
}


def arms(task: str, metric: str, policy: str, kind: str, which: list[str]) -> dict:
    res: dict[str, list] = {}
    for ds, name in [("nasa", "NASA"), ("calce", "CALCE")]:
        rows = []
        for a in which:
            q = tf[
                (tf.dataset == ds)
                & (tf.task == task)
                & (tf.metric == metric)
                & (tf.policy == policy)
                & (tf.kind == kind)
                & (tf.model == f"itransformer+{a}")
            ]
            assert len(q) == 1, (ds, task, a, len(q))
            x = q.iloc[0]
            rows.append(
                {
                    "arm": a,
                    "label": ARM_LABEL[a],
                    "mean": r(x["mean"], 3),
                    "lo": r(x.ci_lo, 3),
                    "hi": r(x.ci_hi, 3),
                }
            )
        res[name] = rows
    return res


transfer_out = {
    "forecast": arms("forecast", "rmse_h50", "start_points", "overall", ARMS),
    "rul": arms("rul", "rul_mae", "all", "overall", ["scratch", "zero_shot", "ft_full"]),
}

data = {
    "order": ORDER,
    "order_rul": order_rul,
    "ranks": {m: r(v, 3) for m, v in rank_of.items()},
    "soh": soh,
    "rul": rul,
    "local_models": local_models,
    "scatter": sc_out,
    "calib": calib_out,
    "width_models": WIDTH_MODELS,
    "ablation": abl_out,
    "recursive": rec_out,
    "transfer": transfer_out,
}
OUT.write_text(json.dumps(data, separators=(",", ":"), allow_nan=False))
print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.1f} KB)")
