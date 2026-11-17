"""Build web/showcase/data/eda.json for the showcase EDA section (deterministic)."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from battery_rul.data.io import read_tables
from battery_rul.data.quality import LONG_REST_S, SKIPPED_CV_S
from battery_rul.features.severson import severson_features
from battery_rul.tasks.labels import eol_table

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "web/showcase/data/eda.json"
PROC = ROOT / "data/processed"
FEATURES = {
    "charge_time_s": "charge time",
    "cc_time_s": "CC time",
    "cv_time_s": "CV time",
    "charge_throughput_ah": "charge throughput",
    "charge_temp_max_c": "max charge temp",
    "charge_temp_mean_c": "mean charge temp",
    "ir_ohm": "internal resistance",
    "rest_before_s": "rest before cycle",
}
MAX_PTS = 250


def r4(x) -> float | None:
    return None if x is None or not np.isfinite(x) else round(float(x), 4)


def lst(a) -> list:
    return [r4(v) for v in a]


def downsample(n: int, k: int) -> np.ndarray:
    return np.unique(np.linspace(0, n - 1, min(n, k)).round().astype(int))


def main() -> None:
    tabs = {ds: read_tables(ds, PROC, curves=False) for ds in ("nasa", "calce", "toyota")}
    out: dict = {"thresholds": {"skipped_cv_s": SKIPPED_CV_S, "long_rest_s": LONG_REST_S}}

    # 1. table
    rows, eols = [], {}
    for ds, t in tabs.items():
        eol = eol_table(t.cycles, t.cells, 0.8)
        eols[ds] = eol
        life = eol["eol_cycle"].dropna()
        cells = t.cells
        rows.append(
            {
                "dataset": ds,
                "chemistry": str(cells["chemistry"].iloc[0]),
                "nominal_ah": r4(cells["nominal_capacity_ah"].median()),
                "cells": len(cells),
                "cycles": len(t.cycles),
                "life_min": r4(life.min()),
                "life_median": r4(life.median()),
                "life_max": r4(life.max()),
                "censored": int(eol["censored"].sum()),
                "protocol": {
                    "nasa": "CC-CV charge 1.5 A to 4.2 V; 2 A discharge to 2.7 V at 24 C",
                    "calce": "CC-CV charge 0.5C to 4.2 V; 1C discharge at room temp",
                    "toyota": "Fast-charge policies (6 start rates); 4C discharge; 30 C chamber",
                }[ds],
                "split": "official 41/43/40" if ds == "toyota" else "leave-one-cell-out",
                "charge_protocols": sorted(cells["charge_protocol"].astype(str).unique())[:8],
            }
        )
    out["table"] = rows

    # 2. SOH curves
    soh = {}
    for ds, t in tabs.items():
        eol = eols[ds].set_index("cell_id")["eol_cycle"]
        lst_cells = []
        for cid, g in t.cycles.sort_values("cycle_idx").groupby("cell_id", sort=True):
            idx = downsample(len(g), MAX_PTS)
            gg = g.iloc[idx]
            lst_cells.append(
                {
                    "cell": str(cid),
                    "cycle": [int(c) for c in gg["cycle_idx"]],
                    "soh": lst(gg["soh"] * 100),
                    "life": r4(eol.get(cid)),
                }
            )
        soh[ds] = lst_cells
    out["soh"] = soh

    # 3. Toyota life by split
    tc = tabs["toyota"].cells.merge(eols["toyota"], on="cell_id")
    out["life"] = [
        {"cell": r.cell_id, "split": r.split, "life": r4(r.eol_cycle)} for r in tc.itertuples()
    ]

    # 4. early-life feature (needs cycles 10 and 100 discharge curves)
    full = read_tables("toyota", PROC, curves=True)
    cur = full.curves[full.curves["cycle_idx"].isin([10, 100])]
    cgroups = dict(tuple(cur.groupby("cell_id", sort=False)))
    early = []
    for r in tc.itertuples():
        g = full.cycles[full.cycles["cell_id"] == r.cell_id]
        f = severson_features(g, cgroups.get(r.cell_id, cur.iloc[:0]))
        if np.isfinite(f["dq_var"]) and np.isfinite(r.eol_cycle):
            early.append(
                {
                    "cell": r.cell_id,
                    "split": r.split,
                    "x": r4(f["dq_var"]),
                    "y": r4(np.log10(r.eol_cycle)),
                    "life": r4(r.eol_cycle),
                }
            )
    del full, cur
    e = pd.DataFrame(early)
    tr = e[e["split"] == "train"]
    slope, intercept, *_ = stats.linregress(tr["x"], tr["y"])
    out["early"] = {
        "points": early,
        "slope": r4(slope),
        "intercept": r4(intercept),
        "pearson_train": r4(stats.pearsonr(tr["x"], tr["y"])[0]),
        "pearson_all": r4(stats.pearsonr(e["x"], e["y"])[0]),
        "n_train": len(tr),
    }

    # 5. NASA regen
    nasa = tabs["nasa"].cycles
    regen = []
    for cid in ("B0005", "B0018"):
        g = nasa[nasa["cell_id"] == cid].sort_values("cycle_idx")
        m = g["rest_before_s"] > 1e5
        regen.append(
            {
                "cell": cid,
                "cycle": [int(c) for c in g["cycle_idx"]],
                "soh": lst(g["soh"] * 100),
                "rest_cycle": [int(c) for c in g.loc[m, "cycle_idx"]],
                "rest_soh": lst(g.loc[m, "soh"] * 100),
                "rest_s": lst(g.loc[m, "rest_before_s"]),
            }
        )
    out["nasa_regen"] = regen

    # 6. CALCE dips
    calce = tabs["calce"].cycles
    g = calce[calce["cell_id"] == "CS2_35"].sort_values("cycle_idx")
    m = g["cv_time_s"] < SKIPPED_CV_S
    out["calce_dips"] = {
        "cell": "CS2_35",
        "cycle": [int(c) for c in g["cycle_idx"]],
        "soh": lst(g["soh"] * 100),
        "art_cycle": [int(c) for c in g.loc[m, "cycle_idx"]],
        "art_soh": lst(g.loc[m, "soh"] * 100),
        "art_cv_s": lst(g.loc[m, "cv_time_s"]),
    }

    # 7. EOL rule gap
    best = None
    for cid, g in calce.sort_values("cycle_idx").groupby("cell_id", sort=True):
        below = g.loc[g["soh"] < 0.8, "cycle_idx"]
        raw = float(below.iloc[0]) if len(below) else np.nan
        lab = float(eols["calce"].set_index("cell_id").loc[cid, "eol_cycle"])
        gap = lab - raw
        if np.isfinite(gap) and (best is None or gap > best["gap"]):
            roll = g["soh"].rolling(11, center=True, min_periods=1).median() * 100
            best = {
                "cell": str(cid),
                "raw_cross": raw,
                "eol": lab,
                "gap": gap,
                "cycle": [int(c) for c in g["cycle_idx"]],
                "soh": lst(g["soh"] * 100),
                "roll": lst(roll),
            }
    out["eol"] = best

    # 8. correlations
    corr = []
    for ds, t in tabs.items():
        df = t.cycles
        for col, lab in FEATURES.items():
            d = df[[col, "soh"]].dropna()
            if len(d) < 50 or d[col].nunique() < 3:
                continue
            rho = stats.spearmanr(d[col], d["soh"])[0]
            corr.append({"dataset": ds, "feature": lab, "rho": r4(rho), "n": len(d)})
    out["corr"] = corr

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, separators=(",", ":"), sort_keys=True))
    print(f"wrote {OUT} ({OUT.stat().st_size / 1e6:.2f} MB)")
    print(json.dumps({k: out[k] for k in ("table",)}, indent=1)[:3000])
    print({k: v for k, v in out["early"].items() if k != "points"})
    print({k: v for k, v in best.items() if k in ("cell", "raw_cross", "eol", "gap")})
    print(pd.DataFrame(corr).to_string())


if __name__ == "__main__":
    main()
