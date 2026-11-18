"""Precompute held-out benchmark predictions of every model for the demo cells.

For each cell in ``app/examples/demos.json`` this reads the seed-0 runs of the MLflow experiment
``benchmark`` (the models never saw that cell: NASA/CALCE leave-one-cell-out folds with the cell
as test cell; Toyota official test split, filtered by ``cell_id``) and writes
``app/examples/<demo>_compare.json`` for the dashboard (web/app.mjs).

Per model and task: point + calibrated 90 % interval (``lo_cal``/``hi_cal`` from
``calibrated_predictions.parquet``) at every ``origin_policy == 'all'`` origin. Models without a
calibrated interval (persistence, last_slope) carry point forecasts only; they have no RUL head.
Classical curve fits (experiment ``benchmark_local``) only evaluate start points, so they are not
included. MLflow is opened read-only (SELECT via the sqlite store; nothing is logged).

Encoding: SOH values are integers in units of 1e-4 of a fraction (scale 10000, so 9871 = 98.71 %);
RUL values are whole cycles (``null`` = no prediction at that origin).

Usage: uv run python scripts/make_demo_compare.py [--tracking-uri URI] [--seed 0]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import mlflow
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
EX = ROOT / "app" / "examples"
MODELS = {
    "persistence": "Persistence (SOH stays the same)",
    "last_slope": "Last slope",
    "prev_soh": "Previous SOH",
    "elasticnet": "ElasticNet",
    "lgbm": "LightGBM",
    "nlinear": "NLinear",
    "dlinear": "DLinear",
    "rlinear": "RLinear",
    "lstm": "LSTM",
    "gru": "GRU",
    "transformer": "Transformer",
    "patchtst": "PatchTST",
    "itransformer": "iTransformer (MC)",
    "itransformer_sc": "iTransformer (SC)",
}
SCALE = 10000


def _art(run_id: str, name: str) -> pd.DataFrame | None:
    try:
        return pd.read_parquet(
            mlflow.artifacts.download_artifacts(run_id=run_id, artifact_path=f"{name}.parquet")
        )
    except Exception:  # artifact absent (e.g. persistence has no calibrated file)
        return None


def _enc(a: np.ndarray, scale: float) -> list:
    out = np.where(np.isfinite(a), np.rint(a * scale), np.nan)
    return (
        [None if np.isnan(v) else int(v) for v in out.ravel()]
        if a.ndim == 1
        else [[None if np.isnan(v) else int(v) for v in row] for row in out]
    )


REST_SUFFIX = "+rest"  # ADR-0016 rest-aware variants (experiment abl_future_rest)


def events(ds: str, cell: str) -> dict:
    """Cycles after a long rest (> 6 h, regeneration) and CV-skip artifact cycles (ADR-0017)."""
    from battery_rul.data.io import read_tables

    c = read_tables(ds, ROOT / "data" / "processed", curves=False).cycles
    c = c[c["cell_id"].astype(str) == cell]
    rest = c[c["rest_before_s"] > 6 * 3600]["cycle_idx"].astype(int).tolist()
    skip = c[c["cv_time_s"] < 300]["cycle_idx"].astype(int).tolist() if ds != "toyota" else []
    return {"long_rest": rest, "cv_skip": skip}


def build(demo: str, runs: pd.DataFrame) -> dict:
    ds, cell = demo.split("_", 1)
    sel = runs[runs["params.dataset"] == ds]
    if ds != "toyota":
        sel = sel[sel["params.test_cell"] == cell]
    models: dict[str, dict] = {}
    origins: dict[str, list[int]] = {}
    horizons: list[int] = []
    for task in ("forecast", "rul"):
        for _, r in sel[sel["params.task"] == task].iterrows():
            m = r["params.model"]
            if m not in MODELS:
                continue
            rest = str(r.get("params.future_rest", "False")) == "True"
            key = m + REST_SUFFIX if rest else m
            pred = _art(r.run_id, "predictions")
            if pred is None:
                continue
            pred = pred[(pred.cell_id == cell) & (pred.origin_policy == "all")]
            pred = pred.drop_duplicates("origin_cycle").sort_values("origin_cycle")
            if pred.empty:
                continue
            cal = _art(r.run_id, "calibrated_predictions")
            if cal is not None:
                cal = cal[(cal.cell_id == cell) & (cal.origin_policy == "all")]
            hs = sorted(int(c.split("_h")[1]) for c in pred.columns if c.startswith("point_h"))
            org = pred.origin_cycle.astype(int).tolist()
            origins.setdefault(task, org)
            assert origins[task] == org, f"origin mismatch {demo} {task} {m}"
            pt = np.stack([pred[f"point_h{h}"].to_numpy(float) for h in hs], 1)
            lo = hi = None
            if cal is not None and len(cal):
                for name in ("lo_cal", "hi_cal"):
                    w = cal.pivot_table(index="origin_cycle", columns="horizon", values=name)
                    w = w.reindex(index=pred.origin_cycle, columns=hs).to_numpy(float)
                    if name == "lo_cal":
                        lo = w
                    else:
                        hi = w
            e = models.setdefault(
                key, {"label": MODELS[m] + (" + planned rests" if rest else ""), "base": m}
            )
            if task == "forecast":
                horizons = hs
                e["forecast"] = {"point": _enc(pt, SCALE)}
                if lo is not None:
                    e["forecast"]["lo"], e["forecast"]["hi"] = _enc(lo, SCALE), _enc(hi, SCALE)
            else:
                e["rul"] = {"point": _enc(pt[:, 0], 1)}
                if lo is not None:
                    e["rul"]["lo"], e["rul"]["hi"] = _enc(lo[:, 0], 1), _enc(hi[:, 0], 1)
    return {
        "demo": demo,
        "scale": SCALE,
        "h": horizons,
        "origin": origins,
        "models": models,
        "events": events(ds, cell),
        "note": (
            "Held-out benchmark predictions (MLflow experiment 'benchmark', seed 0, "
            "origin_policy=all; '+rest' = abl_future_rest, ADR-0016). "
            "SOH = integer/scale as a fraction; RUL in cycles; lo/hi = "
            "calibrated split-conformal 90% interval. forecast.* are [origin][horizon]."
        ),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tracking-uri", default=f"sqlite:///{ROOT / 'mlflow.db'}")
    ap.add_argument("--seed", default="0")
    a = ap.parse_args()
    mlflow.set_tracking_uri(a.tracking_uri)
    runs = mlflow.search_runs(
        experiment_names=["benchmark", "abl_future_rest"],
        filter_string=f"params.seed='{a.seed}'",
        max_results=10000,
    )
    for d in json.loads((EX / "demos.json").read_text()):
        out = build(d["name"], runs)
        p = EX / f"{d['name']}_compare.json"
        p.write_text(json.dumps(out, separators=(",", ":")))
        print(p.name, f"{p.stat().st_size / 1e3:.0f} kB", sorted(out["models"]))
    trajectories(runs)


#: Cells for the whole-life trajectories page (web/trajectories.html). Every NASA/CALCE cell is a
#: leave-one-cell-out test cell of the benchmark; the Toyota cells are official-split test cells
#: (median iTransformer error at the half-life start point, see the showcase fan chart).
TRAJ_CELLS = [
    *(("nasa", c) for c in ("B0005", "B0006", "B0007", "B0018")),
    *(("calce", c) for c in ("CS2_35", "CS2_36", "CS2_37", "CS2_38")),
    ("toyota", "b1c31"),
    ("toyota", "b3c20"),
    ("toyota", "b3c44"),
]
DS_LABEL = {"nasa": "NASA", "calce": "CALCE", "toyota": "Toyota/MIT"}


def trajectories(runs: pd.DataFrame) -> None:
    """Compare files + full trajectories + EOL labels for every TRAJ_CELLS cell."""
    from battery_rul.data.io import read_tables
    from battery_rul.tasks.labels import eol_table

    out_dir = EX / "traj"
    out_dir.mkdir(exist_ok=True)
    meta = json.loads((ROOT / "artifacts" / "deploy" / "deploy_meta.json").read_text())
    cells = []
    for ds in ("nasa", "calce", "toyota"):
        t = read_tables(ds, ROOT / "data" / "processed", curves=False)
        eol = eol_table(t.cycles, t.cells, 0.8).set_index("cell_id")
        split = t.cells.set_index("cell_id")["split"] if "split" in t.cells else None
        for _, cell in (x for x in TRAJ_CELLS if x[0] == ds):
            name = f"{ds}_{cell}"
            cmp = build(name, runs)
            (out_dir / f"{name}_compare.json").write_text(json.dumps(cmp, separators=(",", ":")))
            c = t.cycles[t.cycles.cell_id.astype(str) == cell][["cycle_idx", "capacity_ah"]]
            c.dropna().sort_values("cycle_idx").astype({"cycle_idx": int}).to_csv(
                out_dir / f"{name}_full.csv", index=False
            )
            e = float(eol.loc[cell, "eol_cycle"])
            (out_dir / f"{name}_eol.json").write_text(json.dumps({"eol_cycle": e}))
            where = (
                f"official {split.get(cell)} split"
                if ds == "toyota" and split is not None
                else "leave-one-cell-out test cell"
            )
            cells.append(
                {
                    "name": name,
                    "label": f"{DS_LABEL[ds]} {cell} ({where})",
                    # the deployed model never trained on its calibration cells
                    "live": cell in meta["cells"][ds]["cal"],
                }
            )
            print("traj", name, f"{(out_dir / f'{name}_compare.json').stat().st_size / 1e3:.0f} kB")
    (out_dir / "cells.json").write_text(json.dumps(cells, indent=1))


if __name__ == "__main__":
    main()
