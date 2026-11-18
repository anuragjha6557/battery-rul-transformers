"""Showcase part `regen`: capacity regeneration (ADR-0016) and CALCE artifact cycles (ADR-0017).

Writes web/showcase/data/regen.json from:
* reports/tables/abl_future_rest_events.csv: error at regeneration targets, benchmark vs
  rest-aware, h = 1 and 10;
* MLflow `benchmark` Task A (SOH estimation) predictions: bias at regeneration cycles, the
  setting where the rest has already happened;
* app/examples/nasa_B0018_compare.json: held-out LSTM vs LSTM + planned rests forecasts at
  origins just before a long rest (example fans);
* reports/tables/abl_future_rest_paired.csv and abl_calce_clean_paired.csv: paired deltas.
"""

from __future__ import annotations

import json
from pathlib import Path

import mlflow
import numpy as np
import pandas as pd

from battery_rul.data.io import read_tables

ROOT = Path(__file__).resolve().parents[2]
T = ROOT / "reports" / "tables"
MODELS = ["transformer", "lstm", "elasticnet", "lgbm", "itransformer", "itransformer_sc"]


def task_a_bias() -> list[dict]:
    """SOH-estimation bias (%SOH) at NASA regeneration cycles vs other cycles, 5 seeds."""
    mlflow.set_tracking_uri(f"sqlite:///{ROOT / 'mlflow.db'}")
    c = read_tables("nasa", ROOT / "data" / "processed", curves=False).cycles
    long = c[c.rest_before_s > 6 * 3600]
    ev = set(zip(long.cell_id, long.cycle_idx, strict=True))
    runs = mlflow.search_runs(
        experiment_names=["benchmark"], filter_string="params.task='soh' and params.dataset='nasa'"
    )
    out = []
    for m in [*MODELS, "prev_soh"]:
        g = runs[runs["params.model"] == m]
        if g.empty:
            continue
        fr = pd.concat(
            pd.read_parquet(
                mlflow.artifacts.download_artifacts(run_id=r, artifact_path="predictions.parquet")
            )
            for r in g.run_id
        )
        fr = fr[fr.origin_policy == "all"]
        sel = np.array([(a, b) in ev for a, b in zip(fr.cell_id, fr.origin_cycle, strict=True)])
        e = (fr.point_h0 - fr.y_h0).to_numpy() * 100
        out.append(
            {
                "model": m,
                "bias": float(e[sel].mean()),
                "rmse": float(np.sqrt((e[sel] ** 2).mean())),
                "rmse_other": float(np.sqrt((e[~sel] ** 2).mean())),
                "n": int(sel.sum()),
            }
        )
    return out


def fans() -> dict:
    j = json.loads((ROOT / "app" / "examples" / "nasa_B0018_compare.json").read_text())
    full = pd.read_csv(ROOT / "app" / "examples" / "nasa_B0018_full.csv")
    ref = full.capacity_ah.iloc[:5].mean()
    origins = [o for o in (45, 55) if o in j["origin"]["forecast"]]
    panels = []
    for o in origins:
        i = j["origin"]["forecast"].index(o)
        p = {"origin": o, "series": {}}
        for m in ("lstm", "lstm+rest", "persistence"):
            if m in j["models"]:
                p["series"][m] = {
                    "label": j["models"][m]["label"],
                    "soh": [v / j["scale"] * 100 for v in j["models"][m]["forecast"]["point"][i]],
                }
        panels.append(p)
    return {
        "cell": "NASA B0018",
        "h": j["h"],
        "truth": {
            "cycle": full.cycle_idx.tolist(),
            "soh": (full.capacity_ah / ref * 100).round(3).tolist(),
        },
        "rests": j["events"]["long_rest"],
        "panels": panels,
    }


def main() -> None:
    ev = pd.read_csv(T / "abl_future_rest_events.csv")
    paired = pd.read_csv(T / "abl_future_rest_paired.csv")
    paired = paired[paired.metric.isin(["rmse_h1", "rmse_h10", "rmse_h50"])]
    paired["model"] = paired.candidate.str.split(":").str[1]
    clean = pd.read_csv(T / "abl_calce_clean_paired.csv")
    out = {
        "events": ev.round(4).to_dict(orient="records"),
        "task_a": task_a_bias(),
        "fans": fans(),
        "rest_paired": paired[
            [
                "model",
                "dataset",
                "metric",
                "cand_mean",
                "ref_mean",
                "delta",
                "ci_lo",
                "ci_hi",
                "k_cells",
            ]
        ]
        .round(4)
        .to_dict(orient="records"),
        "clean_paired": clean.round(4).to_dict(orient="records"),
    }
    dest = ROOT / "web" / "showcase" / "data" / "regen.json"
    dest.write_text(json.dumps(out))
    print(f"wrote {dest} ({dest.stat().st_size / 1e3:.0f} kB)")


if __name__ == "__main__":
    main()
