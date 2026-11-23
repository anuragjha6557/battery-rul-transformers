"""Write the field-mode demo uploads (ADR-0022) to ``app/examples/field``.

Demo cells are the **held-out** cells of each deployed field model (``field_meta.json``
``cells.heldout``): NASA B0018, CALCE CS2_38 and, for Toyota, the same three test1 + three test2
cells as the trajectories page (``app/examples/traj_field/cells.json``), which include b3c44.

Each CSV holds the protocol's raw input columns (``field_meta.json["inputs"]``), the optional
``charge_time_s`` when the dataset has it, and a display-only ``soh_measured`` column. The model
never reads ``soh_measured`` (validate_field ignores unknown columns); the page uses it only to
draw the measured curve next to the forecast, labelled as not used by the model.

Usage: uv run python scripts/make_field_examples.py [--processed DIR] [--deploy DIR] [--out DIR]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from battery_rul.tasks.samples import merge_field_features
from battery_rul.train.runner import dataset_ctx

PROTOCOLS = ("nasa", "calce", "toyota")
LABELS = {
    "nasa": "NASA {cell} (held out from the field model)",
    "calce": "CALCE {cell} (held out from the field model)",
    "toyota": "Toyota/MIT {cell} (official {split} split, held out)",
}
TOYOTA_FALLBACK = {"test1": 3, "test2": 3}


def toyota_cells(heldout: dict[str, list[str]], traj_cells: Path) -> list[tuple[str, str]]:
    """(cell, split): the trajectories page's cells when available, else a deterministic pick."""
    split_of = {c: s for s, cs in heldout.items() for c in cs}
    if traj_cells.exists():
        names = [
            d["name"].removeprefix("toyota_")
            for d in json.loads(traj_cells.read_text())
            if d["name"].startswith("toyota_")
        ]
        picked = [(c, split_of[c]) for c in names if c in split_of]
        if len(picked) == 6:
            return picked
    out: list[tuple[str, str]] = []
    for s, n in TOYOTA_FALLBACK.items():
        cs = sorted(heldout[s])
        keep = ["b3c44"] if s == "test2" else []
        out += [(c, s) for c in [*keep, *[c for c in cs if c not in keep]][:n]]
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--processed", default="data/processed")
    ap.add_argument("--deploy", default="artifacts/deploy_field")
    ap.add_argument("--out", default="app/examples/field")
    ap.add_argument("--traj-cells", default="app/examples/traj_field/cells.json")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*"):
        old.unlink()
    demos = []
    for proto in PROTOCOLS:
        meta = json.loads((Path(args.deploy) / proto / "field_meta.json").read_text())
        held = meta["cells"]["heldout"]
        cells = (
            toyota_cells(held, Path(args.traj_cells))
            if proto == "toyota"
            else [(c, "test") for c in held["test"]]
        )
        cyc = dataset_ctx(proto, args.processed, 0.8).cycles
        feats = pd.read_parquet(Path(args.processed) / proto / "field_features.parquet")
        cyc = merge_field_features(cyc, feats)
        for cell, split in cells:
            g = cyc[cyc["cell_id"].astype(str) == cell].sort_values("cycle_idx")
            if g.empty:
                raise SystemExit(f"{proto}/{cell}: not in the processed cycles")
            cols = list(meta["inputs"])
            if "charge_time_s" in g and g["charge_time_s"].notna().any():
                cols.append("charge_time_s")
            df = g[cols].copy()
            df["cycle_idx"] = df["cycle_idx"].astype(int)
            df["soh_measured"] = g["soh"].to_numpy()
            name = f"{proto}_{cell}"
            df.to_csv(out / f"{name}.csv", index=False, float_format="%.8g")
            demos.append(
                {
                    "name": name,
                    "protocol": proto,
                    "cell": cell,
                    "split": split,
                    "n_cycles": len(df),
                    "label": LABELS[proto].format(cell=cell, split=split),
                }
            )
            print(f"{name}: {len(df)} cycles, columns {cols}")
    (out / "demos.json").write_text(json.dumps(demos, indent=1))


if __name__ == "__main__":
    main()
