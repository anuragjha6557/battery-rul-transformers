"""ADR-0020 Stage 2 selection rule: each model's lookback for Stage 3, leakage-free.

For every (dataset, task, model, lookback) the score is the mean, over runs (test unit x seed),
of the RMSE of the cross-fit sub-models on their own held-out *training* cells
(``inner_val_predictions.parquet``). Test predictions are never read. Headline horizon: h0 for
soh, h50 for forecast. The selected lookback is the one with the lowest score.

Usage: uv run python scripts/select_lookback.py [--experiment field_lookback] [--exclude 512]
Writes reports/tables/<experiment>_selection.csv and .md.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import mlflow
import numpy as np
import pandas as pd

HEADLINE = {"soh": 0, "forecast": 50}


def run_score(run_id: str, task: str) -> float:
    p = pd.read_parquet(
        mlflow.artifacts.download_artifacts(
            run_id=run_id, artifact_path="inner_val_predictions.parquet"
        )
    )
    h = HEADLINE[task]
    m = p[f"y_mask_h{h}"].astype(bool) & np.isfinite(p[f"y_h{h}"]) & np.isfinite(p[f"point_h{h}"])
    e = (p.loc[m, f"point_h{h}"] - p.loc[m, f"y_h{h}"]).to_numpy()
    return float(np.sqrt(np.mean(e**2)) * 100) if len(e) else float("nan")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--experiment", default="field_lookback")
    ap.add_argument("--exclude", type=int, nargs="*", default=[512])
    args = ap.parse_args()
    mlflow.set_tracking_uri(
        os.environ.get("MLFLOW_TRACKING_URI", f"sqlite:///{Path.cwd() / 'mlflow.db'}")
    )
    runs = mlflow.search_runs(experiment_names=[args.experiment], max_results=10000)
    runs = runs[runs["tags.unit_key"].notna() & (runs["status"] == "FINISHED")]
    runs = runs[~runs["params.lookback"].astype(int).isin(args.exclude)]
    rows = [
        {
            "dataset": r["params.dataset"],
            "task": r["params.task"],
            "model": r["params.model"],
            "lookback": int(r["params.lookback"]),
            "inner_rmse": run_score(r.run_id, r["params.task"]),
        }
        for _, r in runs.iterrows()
        if r["params.task"] in HEADLINE
    ]
    df = pd.DataFrame(rows)
    agg = (
        df.groupby(["dataset", "task", "model", "lookback"])["inner_rmse"]
        .agg(["mean", "count"])
        .reset_index()
    )
    agg["selected"] = agg["mean"] == agg.groupby(["dataset", "task", "model"])["mean"].transform(
        "min"
    )
    out = Path(f"reports/tables/{args.experiment}_selection.csv")
    agg.round(4).to_csv(out, index=False)
    lines = [
        "| dataset | task | model | lookback | inner-val RMSE (% SOH) | runs | selected |",
        "|---|---|---|---|---|---|---|",
    ]
    for _, r in agg.iterrows():
        lines.append(
            f"| {r.dataset} | {r.task} | {r.model} | {r.lookback} | {r['mean']:.3f} | "
            f"{r['count']} | {'**yes**' if r.selected else ''} |"
        )
    out.with_suffix(".md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
