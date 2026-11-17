"""Write the demo CSVs for the Space (calibration cells only: never trained on).

For each cell: ``<name>.csv`` (first ~55 % of cycles, what the user "uploads") and
``<name>_full.csv`` (whole trajectory, used only to overlay ground truth in the demo plot) and
``<name>_eol.json`` (the benchmark EOL label of the cell, ADR-0005).
Columns: cycle_idx, capacity_ah (Ah).

Usage: uv run python scripts/make_examples.py [--processed DIR] [--meta deploy_meta.json]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from battery_rul.data.io import read_tables
from battery_rul.tasks.labels import eol_table, label_source

FRAC = 0.55


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--processed", default="/Users/anuragjha/RUL_project/data/processed")
    ap.add_argument("--meta", default="artifacts/deploy/deploy_meta.json")
    ap.add_argument("--out", default="app/examples")
    args = ap.parse_args()
    meta = json.loads(Path(args.meta).read_text())
    cal = {ds: sorted(meta["cells"][ds]["cal"]) for ds in ("nasa", "calce", "toyota")}
    picks = [
        ("nasa", "B0018", "nasa_B0018"),
        ("calce", "CS2_38", "calce_CS2_38"),
        ("toyota", cal["toyota"][0], f"toyota_{cal['toyota'][0]}"),
    ]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for ds, cell, name in picks:
        if cell not in cal[ds]:
            raise SystemExit(f"{cell} is not a calibration cell of {ds}")
        t = read_tables(ds, Path(args.processed), curves=False)
        cyc = t.cycles
        eol = eol_table(cyc, t.cells, 0.8).set_index("cell_id")["eol_cycle"]
        label = (
            "reported cycle life (0.88 Ah), the Toyota training label"
            if label_source(ds) != "rule"
            else "80 % SOH sustained for 5 cycles, the training label"
        )
        (out / f"{name}_eol.json").write_text(
            json.dumps({"eol_cycle": float(eol.get(cell, float("nan"))), "label": label})
        )
        df = cyc[cyc["cell_id"].astype(str) == cell][["cycle_idx", "capacity_ah"]]
        df = df.dropna().sort_values("cycle_idx").reset_index(drop=True)
        df["cycle_idx"] = df["cycle_idx"].astype(int)
        n = max(10, round(FRAC * len(df)))
        df.to_csv(out / f"{name}_full.csv", index=False)
        df.iloc[:n].to_csv(out / f"{name}.csv", index=False)
        print(f"{name}: {n}/{len(df)} cycles")


if __name__ == "__main__":
    main()
