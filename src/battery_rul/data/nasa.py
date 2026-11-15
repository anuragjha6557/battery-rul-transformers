"""NASA PCoE Li-ion battery loader (B0005, B0006, B0007, B0018).

Parses the raw MATLAB files into the canonical tables of :mod:`battery_rul.data.schema`.
The loader is a *faithful parse*: capacity outliers are kept (outlier policy is a Phase 2
decision) and no label (EOL / RUL) is derived here.

Cycle construction (leakage-relevant, see PLAN §6.2):

* Entries are walked in file order. Every ``discharge`` entry with a finite, positive
  ``Capacity`` is one aging cycle; ``cycle_idx`` is 1, 2, 3, ... in that order.
* Cycle ``k`` is paired with the *last* ``charge`` entry between the previous discharge
  entry and this discharge. Without such a charge, charge features are NaN and no charge
  curve is emitted.
* ``ir_ohm`` (Re + Rct, Ohm) comes from the latest impedance (EIS) entry that *started
  before* the cycle's charge (or discharge if unpaired) started; never from a later EIS.
* ``rest_before_s`` is the idle gap (s) between the end of the previous cycle's discharge
  and the start of this cycle's charge.

Units: current in A (charge positive, discharge negative -- NASA already uses this
convention, no flip is applied), voltage in V, temperature in degC, time in s, charge in Ah.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from scipy.integrate import cumulative_trapezoid
from scipy.io import loadmat

from battery_rul.data.io import DatasetTables, finalize_and_validate, write_tables
from battery_rul.utils import PROCESSED_DIR, RAW_DIR

log = logging.getLogger(__name__)

DATASET = "nasa"
V_MAX = 4.2  # V, charge cut-off (README)
CV_TOL_V = 0.01  # V below v_max that marks the end of the CC phase
MIN_CC_SAMPLE = 3  # first samples contain start-up transients; CC end is searched from here
NOMINAL_CAPACITY_AH = 2.0
CHEMISTRY = "unknown (commercial 18650 Li-ion; not documented by NASA)"
CHARGE_PROTOCOL = "CC 1.5A to 4.2V, CV to 20mA"
#: Discharge cut-off voltage per cell (V), from the NASA README.
V_MIN: dict[str, float] = {"B0005": 2.7, "B0006": 2.5, "B0007": 2.2, "B0018": 2.5}
CELLS: tuple[str, ...] = tuple(V_MIN)


def _arr(x: Any) -> np.ndarray:
    """Field -> 1-D float array (empty array if missing)."""
    if x is None:
        return np.empty(0)
    return np.atleast_1d(np.asarray(x, dtype=float)).ravel()


def _datevec_to_s(vec: Any) -> float:
    """MATLAB datevec [Y M D h m s] -> seconds since the Unix epoch (naive clock, as UTC)."""
    try:
        v = np.atleast_1d(np.asarray(vec, dtype=float)).ravel()
        if v.size < 6 or not np.isfinite(v[:6]).all():
            return float("nan")
        base = datetime(int(v[0]), int(v[1]), int(v[2]), int(v[3]), int(v[4]), tzinfo=UTC)
        return base.timestamp() + float(v[5])
    except (ValueError, OverflowError, TypeError):
        return float("nan")


def _clean_series(data: dict[str, Any]) -> dict[str, np.ndarray] | None:
    """Extract V/I/T/t of one operation, dropping samples with non-finite or non-increasing time.

    Returns None if fewer than 2 usable samples remain.
    """
    t = _arr(data.get("Time"))
    v = _arr(data.get("Voltage_measured"))
    i = _arr(data.get("Current_measured"))
    temp = _arr(data.get("Temperature_measured"))
    n = min(t.size, v.size, i.size, temp.size)
    if n < 2:
        return None
    t, v, i, temp = t[:n], v[:n], i[:n], temp[:n]
    finite = np.isfinite(t)
    if not finite.all():
        log.warning("dropping %d samples with non-finite time", int((~finite).sum()))
        t, v, i, temp = t[finite], v[finite], i[finite], temp[finite]
    if t.size < 2:
        return None
    # keep a sample only if its time strictly exceeds every earlier kept time
    prev_max = np.concatenate(([-np.inf], np.maximum.accumulate(t)[:-1]))
    keep = t > prev_max
    if not keep.all():
        log.warning("dropping %d duplicate/backward-time samples", int((~keep).sum()))
        t, v, i, temp = t[keep], v[keep], i[keep], temp[keep]
    if t.size < 2:
        return None
    return {"t": t, "v": v, "i": i, "temp": temp}


def _charge_features(s: dict[str, np.ndarray], v_max: float = V_MAX) -> dict[str, float]:
    t, v, i, temp = s["t"], s["v"], s["i"], s["temp"]
    t_rel = t - t[0]
    charge_time = float(t_rel[-1])
    reached = np.flatnonzero(v[MIN_CC_SAMPLE:] >= v_max - CV_TOL_V)
    cc_time = float(t_rel[reached[0] + MIN_CC_SAMPLE]) if reached.size else charge_time
    return {
        "charge_time_s": charge_time,
        "cc_time_s": cc_time,
        "cv_time_s": charge_time - cc_time,
        "charge_throughput_ah": float(np.trapezoid(np.maximum(i, 0.0), t) / 3600.0),
        "charge_temp_max_c": float(np.max(temp)),
        "charge_temp_mean_c": float(np.trapezoid(temp, t) / charge_time),
    }


def _discharge_features(s: dict[str, np.ndarray]) -> dict[str, float]:
    t, v, i, temp = s["t"], s["v"], s["i"], s["temp"]
    return {
        "discharge_time_s": float(t[-1] - t[0]),
        "discharge_temp_max_c": float(np.max(temp)),
        "discharge_energy_wh": float(np.trapezoid(v * np.abs(i), t) / 3600.0),
    }


def _curve_arrays(
    s: dict[str, np.ndarray], cell_id: str, cycle_idx: int, phase: str
) -> dict[str, np.ndarray]:
    t, v, i, temp = s["t"], s["v"], s["i"], s["temp"]
    n = t.size
    return {
        "cell_id": np.full(n, cell_id, dtype=object),
        "cycle_idx": np.full(n, cycle_idx, dtype=np.int64),
        "phase": np.full(n, phase, dtype=object),
        "sample_idx": np.arange(n, dtype=np.int64),
        "t_s": t - t[0],
        "voltage_v": v,
        "current_a": i,
        "temp_c": temp,
        "charge_ah": cumulative_trapezoid(np.abs(i), t, initial=0.0) / 3600.0,
    }


def _scalar(x: Any) -> float:
    """First real element of ``x`` as float (NaN if empty/unparseable)."""
    try:
        a = np.atleast_1d(np.asarray(x)).ravel()
        return float(np.real(a[0])) if a.size else float("nan")
    except (TypeError, ValueError):
        return float("nan")


def _impedance_table(entries: list[dict[str, Any]]) -> tuple[np.ndarray, np.ndarray]:
    """(start time s, Re+Rct in Ohm) of every impedance entry, in file order."""
    starts, ir = [], []
    for e in entries:
        if e["type"] != "impedance":
            continue
        d = e.get("data") or {}
        val = _scalar(d.get("Re")) + _scalar(d.get("Rct"))
        starts.append(_datevec_to_s(e["time"]))
        ir.append(val if np.isfinite(val) and val > 0 else float("nan"))
    return np.asarray(starts, dtype=float), np.asarray(ir, dtype=float)


def _latest_ir(imp_t: np.ndarray, imp_ir: np.ndarray, anchor_s: float) -> float:
    """Re+Rct of the most recent EIS that started strictly before ``anchor_s`` (NaN if none)."""
    if not np.isfinite(anchor_s) or imp_t.size == 0:
        return float("nan")
    ok = np.isfinite(imp_t) & (imp_t < anchor_s)
    if not ok.any():
        return float("nan")
    idx = np.flatnonzero(ok)
    return float(imp_ir[idx[np.argmax(imp_t[idx])]])


def load_cell(mat_path: Path, cell_id: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Parse one NASA ``.mat`` into ``(cycles, curves)`` DataFrames.

    Columns follow :mod:`battery_rul.data.schema` (before ``finalize_and_validate``, i.e.
    without ``soh``). Capacity is in Ah, times in s, currents in A (charge positive,
    discharge negative), temperatures in degC.
    """
    m = loadmat(str(mat_path), simplify_cells=True)
    entries = [dict(e) for e in np.atleast_1d(m[cell_id]["cycle"])]
    imp_t, imp_ir = _impedance_table(entries)
    v_max = V_MAX

    rows: list[dict[str, Any]] = []
    curve_parts: list[dict[str, np.ndarray]] = []
    pending_charge: dict[str, Any] | None = None
    prev_discharge_end = float("nan")  # end (s) of the previous cycle's discharge
    cycle_idx = 0

    for e in entries:
        kind = e["type"]
        if kind == "charge":
            pending_charge = e  # keep only the last charge before the next discharge
            continue
        if kind != "discharge":
            continue

        charge, pending_charge = pending_charge, None  # any discharge consumes pending charges
        data = e.get("data") or {}
        cap = _scalar(data.get("Capacity"))
        if not (np.isfinite(cap) and cap > 0):
            continue
        dis = _clean_series(data)
        cycle_idx += 1
        dis_start = _datevec_to_s(e["time"])

        row: dict[str, Any] = {
            "dataset": DATASET,
            "cell_id": cell_id,
            "cycle_idx": cycle_idx,
            "capacity_ah": cap,
        }
        if dis is not None:
            row.update(_discharge_features(dis))
            curve_parts.append(_curve_arrays(dis, cell_id, cycle_idx, "discharge"))

        anchor = dis_start
        ch = _clean_series(charge["data"]) if charge is not None else None
        if charge is not None and ch is not None:
            ch_start = _datevec_to_s(charge["time"])
            anchor = ch_start
            row.update(_charge_features(ch, v_max))
            curve_parts.append(_curve_arrays(ch, cell_id, cycle_idx, "charge"))
            rest = ch_start - prev_discharge_end
            row["rest_before_s"] = rest if np.isfinite(rest) and rest >= 0 else float("nan")
        row["ir_ohm"] = _latest_ir(imp_t, imp_ir, anchor)
        rows.append(row)

        dur = float(dis["t"][-1]) if dis is not None else float("nan")
        prev_discharge_end = dis_start + dur

    cycles = pd.DataFrame(rows)
    if curve_parts:
        curves = pd.DataFrame(
            {k: np.concatenate([p[k] for p in curve_parts]) for k in curve_parts[0]}
        )
        curves.insert(0, "dataset", DATASET)
    else:  # pragma: no cover - defensive
        curves = pd.DataFrame(
            columns=[
                "dataset",
                "cell_id",
                "cycle_idx",
                "phase",
                "sample_idx",
                "t_s",
                "voltage_v",
                "current_a",
                "temp_c",
                "charge_ah",
            ]
        )
    return cycles, curves


def _ambient_temp(mat_path: Path, cell_id: str) -> float:
    """Median ambient temperature (degC) over the cell's discharge entries."""
    m = loadmat(str(mat_path), simplify_cells=True)
    temps = [
        _scalar(e["ambient_temperature"])
        for e in np.atleast_1d(m[cell_id]["cycle"])
        if e["type"] == "discharge"
    ]
    arr = np.asarray(temps, dtype=float)
    return float(np.nanmedian(arr)) if np.isfinite(arr).any() else float("nan")


def _cell_row(cell_id: str, source_file: str, ambient_c: float) -> dict[str, Any]:
    v_min = V_MIN[cell_id]
    return {
        "dataset": DATASET,
        "cell_id": cell_id,
        "chemistry": CHEMISTRY,
        "nominal_capacity_ah": NOMINAL_CAPACITY_AH,
        "charge_protocol": CHARGE_PROTOCOL,
        "discharge_protocol": f"CC 2A to {v_min}V",
        "ambient_temp_c": ambient_c,
        "v_max": V_MAX,
        "v_min": v_min,
        "batch": None,
        "split": None,
        "reported_cycle_life": None,
        "source_file": source_file,
    }


def build(raw_dir: Path = RAW_DIR / "nasa", out_root: Path = PROCESSED_DIR) -> DatasetTables:
    """Parse B0005/06/07/18; validate and write ``<out_root>/nasa/*.parquet`` (3 tables)."""
    cells_rows, cycles_parts, curves_parts = [], [], []
    for cell_id in CELLS:
        path = raw_dir / f"{cell_id}.mat"
        cyc, cur = load_cell(path, cell_id)
        cycles_parts.append(cyc)
        curves_parts.append(cur)
        cells_rows.append(_cell_row(cell_id, path.name, _ambient_temp(path, cell_id)))
        log.info("%s: %d cycles, %d curve rows", cell_id, len(cyc), len(cur))
    tables = finalize_and_validate(
        pd.DataFrame(cells_rows),
        pd.concat(cycles_parts, ignore_index=True),
        pd.concat(curves_parts, ignore_index=True),
    )
    write_tables(DATASET, tables, out_root)
    return tables
