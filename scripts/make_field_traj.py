"""Whole-life held-out predictions of the FIELD-setting models (no SOH history) for the dashboard.

Field counterpart of ``make_demo_compare.trajectories``: reads the seed-0 runs of the MLflow
experiment ``field_final`` (ADR-0020/0021; NASA/CALCE leave-one-cell-out, Toyota official split),
takes every held-out ``origin_policy == 'all'`` origin with the CQR-calibrated 90 % interval
(``calibrated_predictions.parquet``, as written by ``battery-rul calibrate``), and writes, per cell,
``app/examples/traj_field/<ds>_<cell>_{compare.json,full.csv,eol.json}`` plus ``cells.json``, in
the same schema as ``app/examples/traj`` so ``web/traj.mjs`` loads either. Model keys are the
families (itransformer, lstm, transformer, lgbm, elasticnet, patchtst, age_only).

Cells: every NASA/CALCE cell (each is the test cell of one LOCO fold); for Toyota, 3 cells per
official split (shortest, median and longest cycle life among the split's cells, deterministic),
plus ``b3c44`` when it is a test cell.

Usage: uv run python scripts/make_field_traj.py [--tracking-uri URI] [--seed 0] [--data DIR]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import mlflow
import pandas as pd

import make_demo_compare as mdc

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "app" / "examples" / "traj_field"
LABELS = {
    "age_only": "Age only (SOH vs cycle count)",
    "itransformer": "iTransformer",
    "transformer": "Transformer",
    "lstm": "LSTM",
    "lgbm": "LightGBM",
    "elasticnet": "ElasticNet",
    "patchtst": "PatchTST",
}
MUST_INCLUDE = "b3c44"
DS_LABEL = mdc.DS_LABEL


def pick_toyota(eol: pd.DataFrame, split: pd.Series, per_split: int = 3) -> list[str]:
    """Deterministic: per split, cells at evenly spaced life quantiles; MUST_INCLUDE kept."""
    chosen: list[str] = []
    for sp in ("test1", "test2"):
        cells = sorted(
            eol.loc[split[split == sp].index.intersection(eol.index), "eol_cycle"]
            .dropna()
            .sort_values()
            .index
        )
        cells = sorted(cells, key=lambda c: (eol.loc[c, "eol_cycle"], c))
        if not cells:
            continue
        idx = sorted({round(i * (len(cells) - 1) / (per_split - 1)) for i in range(per_split)})
        pick = [cells[i] for i in idx]
        if MUST_INCLUDE in cells and MUST_INCLUDE not in pick:
            pick[len(pick) // 2] = MUST_INCLUDE
        chosen += pick
    return chosen


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tracking-uri", default=f"sqlite:///{ROOT / 'mlflow.db'}")
    ap.add_argument("--seed", default="0")
    ap.add_argument("--data", type=Path, default=ROOT / "data" / "processed")
    a = ap.parse_args()
    from battery_rul.data.io import read_tables
    from battery_rul.tasks.labels import eol_table

    mlflow.set_tracking_uri(a.tracking_uri)
    runs = mlflow.search_runs(
        experiment_names=["field_final"],
        filter_string=f"params.seed='{a.seed}'",
        max_results=10000,
    )

    def events(ds: str, cell: str) -> dict:
        c = tables[ds].cycles
        c = c[c["cell_id"].astype(str) == cell]
        rest = c[c["rest_before_s"] > 6 * 3600]["cycle_idx"].astype(int).tolist()
        skip = c[c["cv_time_s"] < 300]["cycle_idx"].astype(int).tolist() if ds != "toyota" else []
        return {"long_rest": rest, "cv_skip": skip}

    tables = {d: read_tables(d, a.data, curves=False) for d in ("nasa", "calce", "toyota")}
    mdc.events = events  # make_demo_compare.events reads the repo-local data dir
    mdc.MODELS = dict(LABELS)  # families only; no '+rest' arms exist in field_final
    OUT.mkdir(parents=True, exist_ok=True)
    cells = []
    for ds in ("nasa", "calce", "toyota"):
        t = tables[ds]
        eol = eol_table(t.cycles, t.cells, 0.8).set_index("cell_id")
        eol.index = eol.index.astype(str)
        split = t.cells.assign(cell_id=t.cells.cell_id.astype(str)).set_index("cell_id")["split"]
        names = pick_toyota(eol, split) if ds == "toyota" else sorted(t.cells.cell_id.astype(str))
        for cell in names:
            name = f"{ds}_{cell}"
            cmp = mdc.build(name, runs)
            if not cmp["models"]:
                print("skip (no runs)", name)
                continue
            cmp["note"] = (
                "Held-out FIELD-setting predictions (MLflow experiment 'field_final', seed "
                f"{a.seed}, origin_policy=all; no SOH/capacity history as input, ADR-0018/0020). "
                "SOH = integer/scale as a fraction; RUL in cycles; lo/hi = CQR-calibrated 90% "
                "interval. forecast.* are [origin][horizon]."
            )
            (OUT / f"{name}_compare.json").write_text(json.dumps(cmp, separators=(",", ":")))
            c = t.cycles[t.cycles.cell_id.astype(str) == cell][["cycle_idx", "capacity_ah"]]
            c.dropna().sort_values("cycle_idx").astype({"cycle_idx": int}).to_csv(
                OUT / f"{name}_full.csv", index=False
            )
            (OUT / f"{name}_eol.json").write_text(
                json.dumps({"eol_cycle": float(eol.loc[cell, "eol_cycle"])})
            )
            where = (
                f"official {split.get(cell)} split"
                if ds == "toyota"
                else "leave-one-cell-out test cell"
            )
            cells.append({"name": name, "label": f"{DS_LABEL[ds]} {cell} ({where})", "live": False})
            size = (OUT / f"{name}_compare.json").stat().st_size / 1e3
            print("traj_field", name, f"{size:.0f} kB", sorted(cmp["models"]))
    (OUT / "cells.json").write_text(json.dumps(cells, indent=1))


if __name__ == "__main__":
    main()
