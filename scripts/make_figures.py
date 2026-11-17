"""Generate result figures into ``reports/figures/results/`` from the CSV tables and MLflow."""

from __future__ import annotations

import os
from pathlib import Path

os.environ.setdefault("MLFLOW_DISABLE_AGENT_HINT", "1")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "reports" / "tables"
OUT = ROOT / "reports" / "figures" / "results"
MLFLOW_URI = "sqlite:////Users/anuragjha/RUL_project/mlflow.db"
DPI = 150

NAMES = {
    "itransformer": "iTransformer (MC)",
    "itransformer_sc": "iTransformer (SC)",
    "lgbm": "LightGBM",
    "elasticnet": "ElasticNet",
    "patchtst": "PatchTST",
    "nlinear": "NLinear",
    "dlinear": "DLinear",
    "rlinear": "RLinear",
    "lstm": "LSTM",
    "gru": "GRU",
    "transformer": "Transformer",
    "persistence": "Persistence",
    "last_slope": "Last slope",
    "prev_soh": "Previous SOH",
}
# Okabe-Ito colour-blind-safe palette plus neutrals; one fixed colour per model.
_PAL = [
    "#0072B2",
    "#D55E00",
    "#009E73",
    "#CC79A7",
    "#E69F00",
    "#56B4E9",
    "#F0E442",
    "#882255",
    "#44AA99",
    "#117733",
    "#AA4499",
    "#999999",
    "#555555",
    "#000000",
]
COLOR = dict(zip(NAMES, _PAL, strict=True))
COLS = [
    ("calce", "loco", "CALCE"),
    ("nasa", "loco", "NASA"),
    ("toyota", "test1", "Toyota test1"),
    ("toyota", "test2", "Toyota test2"),
]


def save(fig: plt.Figure, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{name}.png", dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT / name}.png")


def mean_rank() -> None:
    rk = pd.read_csv(TABLES / "benchmark_ranks.csv").sort_values("mean_rank", ascending=False)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.barh(
        [NAMES.get(m, m) for m in rk.model],
        rk.mean_rank,
        color=[COLOR.get(m, "#999999") for m in rk.model],
    )
    for i, v in enumerate(rk.mean_rank):
        ax.text(v + 0.05, i, f"{v:.2f}", va="center", fontsize=8)
    ax.set_xlabel("Mean rank (lower is better)")
    ax.set_title("Mean rank across benchmark conditions")
    save(fig, "mean_rank")


def forecast_h50() -> None:
    bm = pd.read_csv(TABLES / "benchmark.csv")
    d = bm[
        (bm.task == "forecast")
        & (bm.metric == "rmse_h50")
        & (bm.policy == "all")
        & (bm.kind == "overall")
    ]
    ranks = pd.read_csv(TABLES / "benchmark_ranks.csv")
    ranks = ranks[~ranks.model.isin(["persistence", "last_slope", "prev_soh"])]
    models = [*ranks.sort_values("mean_rank").model.head(6), "persistence"]
    fig, axes = plt.subplots(1, 4, figsize=(15, 4.2))
    for ax, (ds, sp, label) in zip(axes, COLS, strict=True):
        sub = d[(d.dataset == ds) & (d.split == sp)].set_index("model")
        ms = [m for m in models if m in sub.index]
        mean = sub.loc[ms, "mean"].to_numpy()
        err = [mean - sub.loc[ms, "ci_lo"].to_numpy(), sub.loc[ms, "ci_hi"].to_numpy() - mean]
        ax.bar(range(len(ms)), mean, yerr=err, capsize=3, color=[COLOR[m] for m in ms])
        ax.set_xticks(range(len(ms)))
        ax.set_xticklabels([NAMES[m] for m in ms], rotation=60, ha="right", fontsize=8)
        ax.set_title(label)
        ax.grid(axis="y", alpha=0.3)
    axes[0].set_ylabel("Forecast RMSE at h=50 (%SOH)")
    fig.suptitle("Capacity forecast error at horizon 50 (95 % CI)")
    fig.tight_layout()
    save(fig, "forecast_h50")


def calibration_h50() -> None:
    cal = pd.read_csv(TABLES / "benchmark_calibration.csv")
    d = cal[
        (cal.task == "forecast")
        & (cal.horizon == 50)
        & (cal.policy == "all")
        & (cal.kind == "overall")
    ]
    models = ["itransformer", "itransformer_sc", "lgbm", "patchtst", "lstm"]
    fig, axes = plt.subplots(1, 4, figsize=(15, 4.2), sharey=True)
    w = 0.38
    for ax, (ds, sp, label) in zip(axes, COLS, strict=True):
        sub = d[(d.dataset == ds) & (d.split == sp)].set_index("model")
        ms = [m for m in models if m in sub.index]
        x = range(len(ms))
        ax.axhspan(0.85, 0.95, color="#BBBBBB", alpha=0.35, zorder=0)
        ax.axhline(0.90, ls="--", color="k", lw=1)
        ax.bar(
            [i - w / 2 for i in x],
            sub.loc[ms, "raw_picp"],
            w,
            color="#E69F00",
            label="Raw",
            zorder=2,
        )
        ax.bar(
            [i + w / 2 for i in x],
            sub.loc[ms, "cal_picp"],
            w,
            color="#0072B2",
            label="CQR",
            zorder=2,
        )
        ax.set_xticks(list(x))
        ax.set_xticklabels([NAMES[m] for m in ms], rotation=60, ha="right", fontsize=8)
        ax.set_title(label)
        ax.set_ylim(0, 1.05)
    axes[0].set_ylabel("PICP (target 0.90)")
    fig.legend(*axes[0].get_legend_handles_labels(), loc="upper right", ncol=2, fontsize=9)
    fig.suptitle("Interval coverage at h=50: raw vs conformalised (CQR)")
    fig.tight_layout()
    save(fig, "calibration_h50")


def forecast_example() -> None:
    import mlflow

    mlflow.set_tracking_uri(MLFLOW_URI)
    runs = mlflow.search_runs(
        experiment_names=["benchmark"],
        filter_string=(
            "params.model = 'itransformer' and params.task = 'forecast' and params.seed = '0'"
        ),
    )
    targets = [
        ("NASA B0018", "nasa", "B0018", "B0018", None),
        ("CALCE CS2_35", "calce", "CS2_35", "CS2_35", None),
        ("Toyota test1", "toyota", "test1+test2", None, "test1"),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.3))
    for ax, (title, ds, tc, cell, split) in zip(axes, targets, strict=True):
        run = runs[(runs["params.dataset"] == ds) & (runs["params.test_cell"] == tc)]
        if run.empty:
            ax.set_title(f"{title}: no run")
            continue
        path = mlflow.artifacts.download_artifacts(
            run_id=run.run_id.iloc[0], artifact_path="calibrated_predictions.parquet"
        )
        df = pd.read_parquet(path)
        df = df[(df.origin_policy == "all") & (df.horizon == 50) & df["mask"].astype(bool)]
        if split is not None:
            df = df[df.split == split]
            cell = sorted(df.cell_id.unique())[0]
        df = df[df.cell_id == cell].sort_values("origin_cycle")
        t = df.origin_cycle + 50
        ax.plot(t, df.y * 100, color="k", lw=1.5, label="True SOH")
        ax.fill_between(
            t,
            df.lo_cal * 100,
            df.hi_cal * 100,
            color="#0072B2",
            alpha=0.25,
            label="90 % CQR interval",
        )
        ax.plot(t, df.point * 100, color="#D55E00", lw=1.2, label="iTransformer h=50")
        ax.set_title(title if cell in title else f"{title} ({cell})")
        ax.set_xlabel("Target cycle (origin + 50)")
        ax.grid(alpha=0.3)
    axes[0].set_ylabel("SOH (%)")
    axes[0].legend(fontsize=8, loc="lower left")
    fig.suptitle("iTransformer (MC), seed 0: h=50 forecasts with calibrated 90 % intervals")
    fig.tight_layout()
    save(fig, "forecast_example")


def main() -> None:
    mean_rank()
    forecast_h50()
    calibration_h50()
    forecast_example()


if __name__ == "__main__":
    main()
