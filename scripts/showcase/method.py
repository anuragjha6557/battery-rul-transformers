"""Showcase part `method`: data for the three-tasks schematic, drawn on a real CALCE cell.

Writes web/showcase/data/method.json: one cell's SOH trajectory (11-cycle rolling median for
readability), an example origin, the look-back window, forecast horizons and the EOL label.
"""

from __future__ import annotations

import json
from pathlib import Path

from battery_rul.data.io import read_tables
from battery_rul.tasks.labels import eol_table

CELL, ORIGIN, LOOKBACK, HORIZONS = "CS2_36", 300, 32, (1, 10, 25, 50, 100)


def main() -> None:
    t = read_tables("calce", Path("data/processed"), curves=False)
    c = t.cycles[t.cycles["cell_id"] == CELL].sort_values("cycle_idx")
    eol = float(eol_table(t.cycles, t.cells, 0.8).set_index("cell_id").loc[CELL, "eol_cycle"])
    smooth = c["soh"].rolling(11, center=True, min_periods=1).median()
    keep = c["cycle_idx"] <= eol + 120
    out = {
        "cell": f"CALCE {CELL}",
        "cycle": c["cycle_idx"][keep].astype(int).tolist(),
        "soh": (smooth[keep] * 100).round(3).tolist(),
        "origin": ORIGIN,
        "lookback": LOOKBACK,
        "horizons": list(HORIZONS),
        "eol": eol,
        "theta": 80.0,
    }
    dest = Path("web/showcase/data/method.json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out))
    print(f"wrote {dest}: {len(out['cycle'])} points, EOL {eol:.0f}")


if __name__ == "__main__":
    main()
