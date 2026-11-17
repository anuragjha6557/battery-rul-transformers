"""Write the demo cells and the held-out accuracy summary for the demo pages.

Demo cells are **calibration cells** (never trained on, ADR-0015) and are chosen by rule, not by
eye:

* cut-off = max(50 % of the cell's life, 64 cycles of history), i.e. the benchmark's
  half-life start point (PROTOCOL §3), but never before the model has a full input window;
* NASA: B0018 (the only rig-independent NASA cell); CALCE: CS2_38 (the only CALCE cal cell);
* Toyota: of the 25 calibration cells, the one with the **median** relative RUL error at its
  cut-off, so the demo is representative rather than best-case.

Writes to ``app/examples``: ``<name>.csv`` (input up to the cut-off), ``<name>_full.csv`` (whole
trajectory, ground-truth overlay only), ``<name>_eol.json`` (the benchmark EOL label,
ADR-0005), ``demos.json`` (demo list + labels) and ``accuracy.json`` (RUL error and 90 %
interval coverage over every calibration cell at the same rule, per dataset).

Usage: uv run python scripts/make_examples.py [--processed DIR] [--meta deploy_meta.json]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from battery_rul.data.io import read_tables
from battery_rul.serve.predictor import Predictor
from battery_rul.tasks.labels import eol_table, label_source

FRAC, MIN_HISTORY = 0.5, 64
LABELS = {
    "nasa": "NASA {cell} (18650, LiCoO₂-type)",
    "calce": "CALCE {cell} (LiCoO₂ prismatic)",
    "toyota": "Toyota/MIT {cell} (LFP, fast charge)",
}


def cut_cycle(df: pd.DataFrame, eol: float) -> int:
    return max(round(FRAC * eol), int(df["cycle_idx"].iloc[min(MIN_HISTORY, len(df)) - 1]))


def evaluate(pred: Predictor, df: pd.DataFrame, eol: float) -> dict:
    r = pred.predict(df[df["cycle_idx"] <= cut_cycle(df, eol)])
    true = eol - r["last_cycle"]
    return {
        "cut": r["last_cycle"],
        "true": true,
        "pred": r["rul"]["cycles"],
        "abs_err": abs(r["rul"]["cycles"] - true),
        "rel_err": abs(r["rul"]["cycles"] - true) / max(true, 1.0),
        "covered": bool(r["rul"]["lo"] <= true <= r["rul"]["hi"]),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--processed", default="data/processed")
    ap.add_argument("--weights", default="artifacts/deploy")
    ap.add_argument("--out", default="app/examples")
    args = ap.parse_args()
    pred = Predictor(args.weights)
    cal = {ds: sorted(pred.meta["cells"][ds]["cal"]) for ds in ("nasa", "calce", "toyota")}
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*"):
        old.unlink()

    accuracy, demos = {}, []
    for ds in ("nasa", "calce", "toyota"):
        t = read_tables(ds, Path(args.processed), curves=False)
        eols = eol_table(t.cycles, t.cells, 0.8).set_index("cell_id")["eol_cycle"]
        frames, rows = {}, []
        for cell in cal[ds]:
            eol = float(eols.get(cell, np.nan))
            if not np.isfinite(eol):
                continue  # censored: no RUL truth
            df = t.cycles[t.cycles["cell_id"].astype(str) == cell][["cycle_idx", "capacity_ah"]]
            df = df.dropna().sort_values("cycle_idx").reset_index(drop=True)
            df["cycle_idx"] = df["cycle_idx"].astype(int)
            frames[cell] = (df, eol)
            rows.append({"cell": cell, **evaluate(pred, df, eol)})
        res = pd.DataFrame(rows)
        accuracy[ds] = {
            "n_cells": len(res),
            "median_abs_err": float(res["abs_err"].median()),
            "median_rel_err": float(res["rel_err"].median()),
            "coverage": float(res["covered"].mean()),
        }
        if ds == "toyota":  # the median-error cell (lower median for even counts)
            order = res.sort_values("rel_err").reset_index(drop=True)
            cell = str(order.loc[(len(order) - 1) // 2, "cell"])
        else:
            cell = {"nasa": "B0018", "calce": "CS2_38"}[ds]
        df, eol = frames[cell]
        name = f"{ds}_{cell}"
        cut = cut_cycle(df, eol)
        df.to_csv(out / f"{name}_full.csv", index=False)
        df[df["cycle_idx"] <= cut].to_csv(out / f"{name}.csv", index=False)
        label = (
            "dataset's official cycle life: 0.88 Ah, ≈ 82% of initial"
            if label_source(ds) != "rule"
            else "first sustained drop below 80% SOH"
        )
        (out / f"{name}_eol.json").write_text(json.dumps({"eol_cycle": eol, "label": label}))
        demos.append({"name": name, "label": LABELS[ds].format(cell=cell)})
        print(f"{name}: cut {cut}, EOL {eol:.0f}; {ds} accuracy {accuracy[ds]}")
    (out / "demos.json").write_text(json.dumps(demos, indent=1))
    (out / "accuracy.json").write_text(
        json.dumps(
            {
                "rule": f"cut-off = max({FRAC:.0%} of life, {MIN_HISTORY} cycles); "
                "calibration cells (never trained on)",
                "datasets": accuracy,
            },
            indent=1,
        )
    )


if __name__ == "__main__":
    main()
