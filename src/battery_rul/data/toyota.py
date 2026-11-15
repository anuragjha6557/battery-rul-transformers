"""Toyota / MIT / Stanford fast-charging loader (Severson et al., Nature Energy 2019).

124 A123 APR18650M1A LFP/graphite cells (1.1 Ah) in three batches, MATLAB v7.3 (HDF5).
Parsed into the canonical tables of :mod:`battery_rul.data.schema`.

Raw layout (verified on all three files): ``f['batch']`` holds per-cell ``(N, 1)`` object-reference
arrays. ``summary`` has ``IR, QCharge, QDischarge, Tavg, Tmax, Tmin, chargetime, cycle`` (each
``(1, n)``); ``cycles`` has ``I, Qc, Qd, Qdlin, T, Tdlin, V, discharge_dQdV, t`` (each ``(n, 1)``
refs). Summary index ``k`` is aligned with ``cycles[k]``. **Index 0 of every cell is an all-zero
dummy** (``QDischarge == 0``); the capacity filter removes it.

Units, as measured on the data (differs from the brief in places):

* ``t`` and ``chargetime`` are in **minutes** (median sample step 0.0833 min = 5 s).
* Raw ``I`` is in **C-rate** (multiples of 1.1 A), not amps; it is only used here to locate the
  charge segment (curves carry no current).
* ``chargetime`` is the **time to reach 80 % of 1.1 Ah**, a protocol property, *not* the total
  charge duration. It is deliberately **not** used. ``charge_time_s`` is the raw total duration
  of the charge segment, so ``cc_time_s + cv_time_s == charge_time_s`` as for NASA/CALCE.
* ``Vdlin`` is a 1000-point grid from 3.5 V down to 2.0 V; ``Qdlin``/``Tdlin`` live on it.

Official cleaning (public BuildPkl_Batch1/2/3 notebooks of rdbraatz/data-driven-prediction-of-
battery-cycle-life-before-capacity-degradation), re-implemented:

* batch 1: drop b1c8, b1c10, b1c12, b1c13, b1c22 (never reached 80 %).
* batch 1 cells b1c0..b1c4 continue in batch 2 as b2c7, b2c8, b2c9, b2c15, b2c16
  (``add_len = [662, 981, 1060, 208, 482]``): ``cycle_life += add_len``, summary arrays are
  concatenated with batch-2 cycle numbers offset by the batch-1 cycle count, cycles appended;
  the five batch-2 cells are then dropped.
* batch 3: drop b3c37, b3c2, b3c23, b3c32, b3c42, b3c43 (noisy channels).
* official split: ordering batch 1, 2, 3 (ascending cell index); with 84 cells in batches 1+2,
  ``test1`` = even indices plus the last (83), ``train`` = odd indices 1..81, ``test2`` = batch 3.

Mapping decisions: ``cycle_idx`` is the summary ``cycle`` value (gaps for dropped cycles are kept);
a cycle is kept iff ``0.1 < QDischarge < 1.3`` Ah (drops the cycle-0 dummy and capacity spikes);
``IR <= 0`` becomes NaN; whole-cycle temperatures contain discharge, so only ``Tmax`` is stored, in
``discharge_temp_max_c``. Curves are discharge-only (charge curves are protocol-confounded, see
PROTOCOL section 2): every 10th point of the 1000-point grid, 100 samples per cycle.
"""

from __future__ import annotations

import logging
import re
from collections import Counter
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, Final

import numpy as np
import pandas as pd

from battery_rul.data.io import DatasetTables, finalize_and_validate, write_tables
from battery_rul.utils import PROCESSED_DIR, RAW_DIR

log = logging.getLogger(__name__)

DATASET: Final = "toyota"
CHEMISTRY: Final = "LFP/graphite (A123 APR18650M1A)"
NOMINAL_CAPACITY_AH: Final = 1.1
AMBIENT_TEMP_C: Final = 30.0
V_MAX: Final = 3.6
V_MIN: Final = 2.0
DISCHARGE_PROTOCOL: Final = "CC 4C to 2.0V"

#: batch number -> file-name date prefix
BATCH_DATES: Final = {1: "2017-05-12", 2: "2017-06-30", 3: "2018-04-12"}

CAP_MIN_AH: Final = 0.1
CAP_MAX_AH: Final = 1.3
CURVE_STRIDE: Final = 10
I_CHARGE_MIN: Final = 0.01  # C-rate; |I| above this counts as active charge/discharge
CV_TOL_V: Final = 0.005

DROP_B1: Final = ("b1c8", "b1c10", "b1c12", "b1c13", "b1c22")
DROP_B3: Final = ("b3c37", "b3c2", "b3c23", "b3c32", "b3c42", "b3c43")
#: batch-1 cell -> (batch-2 continuation, cycles added to cycle_life)
CONTINUATIONS: Final = {
    "b1c0": ("b2c7", 662),
    "b1c1": ("b2c8", 981),
    "b1c2": ("b2c9", 1060),
    "b1c3": ("b2c15", 208),
    "b1c4": ("b2c16", 482),
}


@dataclass(frozen=True)
class RawCycle:
    """Raw arrays of one cycle. ``t`` in minutes, ``i`` in C-rate, ``v`` in V."""

    t: np.ndarray
    v: np.ndarray
    i: np.ndarray
    qdlin: np.ndarray  # Ah on the cell's Vdlin grid
    tdlin: np.ndarray  # degC on the cell's Vdlin grid


@dataclass(frozen=True)
class RawCell:
    """One parsed cell. ``loaders[k]`` lazily returns the raw cycle aligned with summary index k."""

    cell_id: str
    batch: str  # date string
    source_file: str
    policy: str
    cycle_life: float
    summary: dict[str, np.ndarray]
    vdlin: np.ndarray
    loaders: Sequence[Callable[[], RawCycle]] = field(repr=False)


# --------------------------------------------------------------------------- HDF5 I/O


def _decode(arr: np.ndarray) -> str:
    return "".join(chr(int(c)) for c in np.asarray(arr).ravel() if 0 < int(c) < 0x110000)


def read_batch(path: Path) -> dict[str, RawCell]:
    """Open one batch file and return every cell (``b<batch>c<k>``, original indices).

    Only summaries are read eagerly; raw cycles load lazily through closures, so the HDF5 file
    stays open for as long as the returned cells are used.
    """
    import h5py

    date = path.name[:10]
    batch_no = next((n for n, d in BATCH_DATES.items() if d == date), None)
    if batch_no is None:
        raise ValueError(f"unrecognised Toyota batch file: {path.name}")
    f = h5py.File(path, "r")
    b = f["batch"]
    cells: dict[str, RawCell] = {}
    for k in range(b["summary"].shape[0]):
        s = f[b["summary"][k, 0]]
        summary = {name: np.asarray(s[name][0], dtype=float) for name in s}
        cl = np.asarray(f[b["cycle_life"][k, 0]][()], dtype=float).ravel()
        cyc = f[b["cycles"][k, 0]]
        refs = {name: cyc[name][:, 0] for name in ("V", "I", "t", "Qdlin", "Tdlin")}

        def make(j: int, refs: dict[str, Any] = refs) -> Callable[[], RawCycle]:
            def load() -> RawCycle:
                def g(key: str, refs: dict[str, Any] = refs) -> np.ndarray:
                    return np.asarray(f[refs[key][j]][()], dtype=float).ravel()

                return RawCycle(g("t"), g("V"), g("I"), g("Qdlin"), g("Tdlin"))

            return load

        n = summary["cycle"].size
        cid = f"b{batch_no}c{k}"
        cells[cid] = RawCell(
            cell_id=cid,
            batch=date,
            source_file=path.name,
            policy=_decode(f[b["policy_readable"][k, 0]][()]),
            cycle_life=float(cl[0]) if cl.size else float("nan"),
            summary=summary,
            vdlin=np.asarray(f[b["Vdlin"][k, 0]][()], dtype=float).ravel(),
            loaders=[make(j) for j in range(n)],
        )
    return cells


# --------------------------------------------------------------------------- pure cleaning


def drop_cells(cells: Mapping[str, RawCell], ids: Iterable[str]) -> dict[str, RawCell]:
    """Copy of ``cells`` without ``ids`` (ids that are absent raise ``KeyError``)."""
    ids = set(ids)
    missing = ids - set(cells)
    if missing:
        raise KeyError(f"cannot drop unknown cells: {sorted(missing)}")
    return {k: v for k, v in cells.items() if k not in ids}


def merge_continuations(
    batch1: Mapping[str, RawCell],
    batch2: Mapping[str, RawCell],
    mapping: Mapping[str, tuple[str, int]] = CONTINUATIONS,
) -> dict[str, RawCell]:
    """Append each batch-2 continuation onto its batch-1 cell; returns the new batch-1 dict.

    ``cycle_life += add_len``; summary arrays are concatenated, with the continuation's ``cycle``
    numbers offset by the batch-1 cycle count; raw cycle loaders are appended. The batch-2 cells
    are left untouched (drop them afterwards with :func:`drop_cells`).
    """
    out = dict(batch1)
    for c1, (c2, add_len) in mapping.items():
        a, b = batch1[c1], batch2[c2]
        n2 = b.summary["cycle"].size
        if n2 != add_len:
            raise ValueError(f"{c2}: expected {add_len} continuation cycles, found {n2}")
        n1 = a.summary["cycle"].size
        summary = {
            k: np.concatenate([a.summary[k], b.summary[k] + (n1 if k == "cycle" else 0)])
            for k in a.summary
        }
        out[c1] = replace(
            a,
            cycle_life=a.cycle_life + add_len,
            summary=summary,
            loaders=[*a.loaders, *b.loaders],
            source_file=f"{a.source_file}+{b.source_file}",
        )
    return out


def _cell_number(cell_id: str) -> int:
    m = re.fullmatch(r"b\d+c(\d+)", cell_id)
    if m is None:
        raise ValueError(f"bad cell id {cell_id!r}")
    return int(m.group(1))


def assign_split(ordered_ids: Sequence[str], n_batch12: int | None = None) -> dict[str, str]:
    """Severson's official split for cells ordered batch 1, 2, 3.

    The first ``n_batch12`` cells (default: all cells whose id starts with b1 or b2) are split by
    index: odd -> ``train`` except the very last of them, even -> ``test1`` (so with 84 cells:
    train = odd 1..81, test1 = even 0..82 plus 83). Everything after is ``test2``.
    """
    if n_batch12 is None:
        n_batch12 = sum(1 for c in ordered_ids if not c.startswith("b3"))
    out: dict[str, str] = {}
    for i, cid in enumerate(ordered_ids):
        if i >= n_batch12:
            out[cid] = "test2"
        elif i == n_batch12 - 1 or i % 2 == 0:
            out[cid] = "test1"
        else:
            out[cid] = "train"
    return out


# --------------------------------------------------------------------------- per-cell tables


def charge_times(t_min: np.ndarray, v: np.ndarray, i: np.ndarray) -> tuple[float, float, float]:
    """(total, cc, cv) charge duration in s from one raw cycle (NaNs if no charge/discharge).

    The charge segment runs from the first sample with ``I > 0.01`` C to the last such sample
    before the first discharge sample (``I < -0.01``). The CC phase ends at the first sample with
    ``V >= 3.6 - 0.005`` V (CC = whole charge if never reached).
    """
    nan = float("nan")
    pos = np.flatnonzero(i > I_CHARGE_MIN)
    if pos.size == 0:
        return nan, nan, nan
    neg = np.flatnonzero((i < -I_CHARGE_MIN) & (np.arange(i.size) > pos[0]))
    if neg.size == 0:
        return nan, nan, nan
    seg = pos[pos < neg[0]]
    p0, p1 = int(seg[0]), int(seg[-1])
    total = float(t_min[p1] - t_min[p0]) * 60.0
    reach = np.flatnonzero(v[p0 : p1 + 1] >= V_MAX - CV_TOL_V)
    cc = float(t_min[p0 + reach[0]] - t_min[p0]) * 60.0 if reach.size else total
    return total, cc, total - cc


def cell_row(cell: RawCell, split: str | None) -> dict[str, Any]:
    pol = cell.policy
    return {
        "dataset": DATASET,
        "cell_id": cell.cell_id,
        "chemistry": CHEMISTRY,
        "nominal_capacity_ah": NOMINAL_CAPACITY_AH,
        "charge_protocol": f"fast-charge {pol}, then CC-CV 1C to {V_MAX}V",
        "discharge_protocol": DISCHARGE_PROTOCOL,
        "ambient_temp_c": AMBIENT_TEMP_C,
        "v_max": V_MAX,
        "v_min": V_MIN,
        "batch": cell.batch,
        "split": split,
        "reported_cycle_life": cell.cycle_life if np.isfinite(cell.cycle_life) else None,
        "source_file": cell.source_file,
    }


def cell_tables(
    cell: RawCell, stats: Counter[str] | None = None
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """``(cycles, curves)`` for one cell (before ``soh``; see :mod:`battery_rul.data.schema`).

    Keeps cycles with finite ``0.1 < QDischarge < 1.3`` Ah. ``stats`` (optional) accumulates
    ``kept``, ``dropped_low`` (non-finite or <= 0.1 Ah), ``dropped_high`` (>= 1.3 Ah) and
    ``qdlin_clipped`` (negative Qdlin samples set to 0).
    """
    st: Counter[str] = stats if stats is not None else Counter()
    s = cell.summary
    qd = s["QDischarge"]
    finite = np.isfinite(qd)
    low = ~finite | (qd <= CAP_MIN_AH)
    high = finite & (qd >= CAP_MAX_AH)
    keep = np.flatnonzero(~low & ~high)
    st["kept"] += int(keep.size)
    st["dropped_low"] += int(low.sum())
    st["dropped_high"] += int(high.sum())

    n_keep = keep.size
    vgrid = cell.vdlin[::CURVE_STRIDE]
    m = vgrid.size
    rows: list[dict[str, Any]] = []
    q_block = np.empty((n_keep, m))
    t_block = np.empty((n_keep, m))
    for r, k in enumerate(keep):
        raw = cell.loaders[int(k)]()
        total, cc, cv = charge_times(raw.t, raw.v, raw.i)
        q = raw.qdlin[::CURVE_STRIDE]
        st["qdlin_clipped"] += int((q < 0).sum())
        q_block[r] = np.clip(q, 0.0, None)
        t_block[r] = raw.tdlin[::CURVE_STRIDE]
        ir = s["IR"][k]
        rows.append(
            {
                "dataset": DATASET,
                "cell_id": cell.cell_id,
                "cycle_idx": round(s["cycle"][k]),
                "capacity_ah": float(qd[k]),
                "charge_time_s": total,
                "cc_time_s": cc,
                "cv_time_s": cv,
                "charge_throughput_ah": float(s["QCharge"][k]),
                "discharge_temp_max_c": float(s["Tmax"][k]),
                "ir_ohm": float(ir) if np.isfinite(ir) and ir > 0 else float("nan"),
            }
        )
    cycles = pd.DataFrame(rows)
    idx = cycles["cycle_idx"].to_numpy(dtype=np.int64) if n_keep else np.empty(0, np.int64)
    n_rows = n_keep * m
    curves = pd.DataFrame(
        {
            "dataset": pd.Series(DATASET, index=range(n_rows), dtype="string"),
            "cell_id": pd.Series(cell.cell_id, index=range(n_rows), dtype="string"),
            "cycle_idx": np.repeat(idx, m),
            "phase": pd.Series("discharge", index=range(n_rows), dtype="string"),
            "sample_idx": np.tile(np.arange(m, dtype=np.int64), n_keep),
            "t_s": np.full(n_rows, np.nan),
            "voltage_v": np.tile(vgrid, n_keep),
            "current_a": np.full(n_rows, np.nan),
            "temp_c": t_block.ravel(),
            "charge_ah": q_block.ravel(),
        }
    )
    return cycles, curves


# --------------------------------------------------------------------------- build


def assemble_cells(raw_dir: Path) -> list[RawCell]:
    """Read the three batches and apply the official cleaning; ordered batch 1, 2, 3."""
    paths = {n: next(raw_dir.glob(f"{d}_*.mat"), None) for n, d in BATCH_DATES.items()}
    absent = [BATCH_DATES[n] for n, p in paths.items() if p is None]
    if absent:
        raise FileNotFoundError(f"Toyota batch files missing in {raw_dir}: {absent}")
    b1, b2, b3 = (read_batch(paths[n]) for n in (1, 2, 3))  # type: ignore[arg-type]
    n_raw = (len(b1), len(b2), len(b3))
    b1 = merge_continuations(b1, b2)
    b1 = drop_cells(b1, DROP_B1)
    b2 = drop_cells(b2, [c2 for c2, _ in CONTINUATIONS.values()])
    b3 = drop_cells(b3, DROP_B3)
    log.info("cells raw %s -> cleaned %s", n_raw, (len(b1), len(b2), len(b3)))
    out: list[RawCell] = []
    for b in (b1, b2, b3):
        out.extend(sorted(b.values(), key=lambda c: _cell_number(c.cell_id)))
    return out


def build_with_stats(
    raw_dir: Path = RAW_DIR / "toyota", out_root: Path = PROCESSED_DIR, write: bool = True
) -> tuple[DatasetTables, dict[str, Counter[str]]]:
    """Full build; also returns per-cell counters (kept / dropped / clipped)."""
    cells = assemble_cells(raw_dir)
    split = assign_split([c.cell_id for c in cells])
    cells_rows, cyc_parts, cur_parts = [], [], []
    per_cell: dict[str, Counter[str]] = {}
    for c in cells:
        st: Counter[str] = Counter()
        cyc, cur = cell_tables(c, st)
        per_cell[c.cell_id] = st
        cells_rows.append(cell_row(c, split[c.cell_id]))
        cyc_parts.append(cyc)
        cur_parts.append(cur)
        log.info("%s: %d cycles kept (%s)", c.cell_id, len(cyc), dict(st))
    tables = finalize_and_validate(
        pd.DataFrame(cells_rows),
        pd.concat(cyc_parts, ignore_index=True),
        pd.concat(cur_parts, ignore_index=True),
    )
    if write:
        write_tables(DATASET, tables, out_root)
    return tables, per_cell


def build(raw_dir: Path = RAW_DIR / "toyota", out_root: Path = PROCESSED_DIR) -> DatasetTables:
    """Parse, clean, validate and write ``<out_root>/toyota/*.parquet`` (3 tables)."""
    return build_with_stats(raw_dir, out_root)[0]
