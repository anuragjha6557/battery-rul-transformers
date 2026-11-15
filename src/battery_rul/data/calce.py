"""CALCE CS2 (LiCoO2 / graphite, 1.1 Ah prismatic) loader: Arbin ``.xlsx`` -> canonical tables.

Raw layout (verified on CS2_35 ... CS2_38): one directory per cell with 25-28 workbooks
``CS2_<cell>_<M>_<D>_<YY>.xlsx``. Each workbook is one *test session* with sheets ``Info`` and
``Channel_1-0xx`` (plus sometimes ``Statistics_...``); the channel sheet is the time series.

Facts the parser relies on (all measured on the real files, see ``docs`` / the Phase 2 data
quality report):

* ``Cycle_Index``, ``Step_Index`` and the Arbin capacity/energy counters **restart in every
  session**. Within a session the ``Charge_/Discharge_Capacity`` and ``*_Energy`` counters are
  *cumulative over the whole session* (not per cycle), so a cycle's discharge capacity is the
  counter *difference* across its discharge phase.
* Filenames are ``M_D_YY`` without zero padding: lexical order is wrong, and the file date is
  not the session start (``CS2_35_10_15_10`` starts 2010-10-08, it is the *end* date). Sessions
  are ordered by the first row's ``Date_Time``.
* Logging is every ~30 s in CC phases and sparser (down to ~100 s) in the CV phase.
* No temperature channel exists -> every temperature column is NaN.
* Protocol: CC charge 0.55 A (0.5C) to 4.2 V, 2 min rest, CV 4.2 V until I < 0.05 A, rest,
  CC discharge 1.1 A (1C) to 2.7 V, rest.

Parsing rules (faithful; no outlier removal - that is a Phase 2 decision):

1. Samples with ``|I| > 0.01 A`` are grouped into alternating blocks of the same sign (rest
   samples inside a block do not split it, so CC + rest + CV is one charge block). Each
   discharge block is paired with the charge block *immediately preceding* it in time (schema
   contract); a charge block with no discharge after it ends the session (partial cycle).
   Current sign is used instead of Arbin's ``Step_Index``/``Cycle_Index`` because those
   restart per session and a cycle can straddle Arbin's own cycle boundary; the sign test
   needs no assumption about the schedule.
2. A candidate cycle is **kept** iff its discharge ends at <= 2.8 V (full discharge to the 2.7 V
   cut-off) and delivers >= 0.1 Ah and a preceding charge exists. Everything else is dropped
   and classified (``partial``: session ended in a charge or mid-discharge; ``other``).
3. ``capacity_ah`` = difference of the Arbin discharge counter across the discharge phase
   (baseline = the sample just before the first discharge sample); cross-checked against the
   trapezoid integral of |I| (falls back to the integral if the counter is unusable or the two
   disagree by > 1 %).
4. ``cycle_idx`` = 1, 2, ... over *kept* cycles in chronological order across all sessions.
"""

from __future__ import annotations

import logging
import time
import zipfile
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Final

import numpy as np
import pandas as pd

from battery_rul.data.io import DatasetTables, finalize_and_validate, write_tables
from battery_rul.utils import PROCESSED_DIR, RAW_DIR

log = logging.getLogger(__name__)

DATASET: Final = "calce"
CELL_IDS: Final = ("CS2_35", "CS2_36", "CS2_37", "CS2_38")

# --- parsing constants -------------------------------------------------------------------
I_THRESH_A: Final = 0.01  # |I| above this counts as charging / discharging (rest noise < 1e-3 A)
MIN_DISCHARGE_AH: Final = 0.1  # smaller discharges are not capacity measurements
MAX_END_VOLTAGE_V: Final = 2.8  # a full discharge ends at the 2.7 V cut-off
CC_END_VOLTAGE_V: Final = 4.19  # first sample >= this ends the CC part (cut-off is 4.2 V)
COUNTER_AGREEMENT_TOL: Final = 0.01  # counter vs integral relative tolerance
NO_CV_TIME_S: Final = (
    300.0  # normal CV phase lasts 1500-3800 s; < 300 s = Arbin skipped the CV step
)

# --- raw column names --------------------------------------------------------------------
C_TIME: Final = "Test_Time(s)"
C_DATE: Final = "Date_Time"
C_CUR: Final = "Current(A)"
C_VOLT: Final = "Voltage(V)"
C_DCAP: Final = "Discharge_Capacity(Ah)"
C_DENG: Final = "Discharge_Energy(Wh)"
C_IR: Final = "Internal_Resistance(Ohm)"
C_GLOBAL: Final = "global_time_s"
REQUIRED_COLUMNS: Final = (C_TIME, C_DATE, C_CUR, C_VOLT, C_DCAP, C_DENG, C_IR)

# --- cycle statuses ----------------------------------------------------------------------
KEPT: Final = "kept"
NO_DISCHARGE: Final = "partial_no_discharge"  # session ended during/after a charge
INCOMPLETE_DISCHARGE: Final = "partial_discharge"  # discharge did not reach the cut-off
LOW_CAPACITY: Final = "other_low_capacity"  # reached <= 2.8 V but delivered < 0.1 Ah
NO_CHARGE: Final = "other_no_charge"  # discharge with no charge before it
PARTIAL_STATUSES: Final = (NO_DISCHARGE, INCOMPLETE_DISCHARGE)

CHARGE_PROTOCOL: Final = "CC 0.55 A (0.5C) to 4.2 V, rest, CV 4.2 V until I < 0.05 A"
DISCHARGE_PROTOCOL: Final = "CC 1.1 A (1C) to 2.7 V"


# =========================================================================================
# Records
# =========================================================================================
@dataclass
class CycleRecord:
    """One candidate cycle: a (possibly empty) charge window and a (possibly empty) discharge.

    ``charge`` / ``discharge`` are row slices of the session frame (raw columns plus
    ``global_time_s``), contiguous in time. The charge window spans the first to the last
    ``I > +0.01 A`` sample (it therefore contains the short rest between CC and CV).
    """

    session: int
    source_file: str
    charge: pd.DataFrame
    discharge: pd.DataFrame
    status: str
    capacity_counter_ah: float = float("nan")
    capacity_integral_ah: float = float("nan")
    capacity_ah: float = float("nan")
    energy_counter_wh: float = float("nan")
    energy_integral_wh: float = float("nan")
    discharge_end_v: float = float("nan")
    ir_ohm: float = float("nan")
    capacity_source: str = ""  # "counter" | "integral"

    @property
    def kept(self) -> bool:
        return self.status == KEPT


@dataclass
class CellStats:
    """Bookkeeping of what the parser did for one cell (feeds the data-quality report)."""

    cell_id: str
    n_files: int = 0
    n_sessions_used: int = 0
    dedupe_report: list[str] = field(default_factory=list)
    n_kept: int = 0
    dropped: Counter[str] = field(default_factory=Counter)
    n_counter_integral_mismatch: int = 0
    max_counter_integral_rel_diff: float = 0.0
    n_kept_no_cv: int = 0  # kept cycles whose charge has no CV segment (cv_time_s ~ 0)
    seconds: float = 0.0

    @property
    def n_dropped_partial(self) -> int:
        return sum(v for k, v in self.dropped.items() if k in PARTIAL_STATUSES)

    @property
    def n_dropped_other(self) -> int:
        return sum(v for k, v in self.dropped.items() if k not in PARTIAL_STATUSES)


@dataclass
class CellLoad:
    cycles: pd.DataFrame
    curves: pd.DataFrame
    stats: CellStats


# =========================================================================================
# I/O: one workbook -> DataFrame
# =========================================================================================
def read_session(xlsx_path: Path) -> pd.DataFrame:
    """Read the ``Channel_*`` sheet of one Arbin workbook (+ a ``source_file`` column).

    Uses the calamine engine (Rust, ~50x faster than openpyxl on these 15k-row sheets). Only
    the channel sheet is parsed; ``Info`` and ``Statistics_*`` are ignored.
    """
    xlsx_path = Path(xlsx_path)
    with pd.ExcelFile(xlsx_path, engine="calamine") as xl:
        sheets = [s for s in xl.sheet_names if str(s).startswith("Channel")]
        if len(sheets) != 1:
            raise ValueError(f"{xlsx_path.name}: expected exactly one Channel sheet, got {sheets}")
        df = pd.read_excel(xl, sheet_name=sheets[0])
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"{xlsx_path.name}: missing columns {missing}")
    df[C_DATE] = pd.to_datetime(df[C_DATE])
    df["source_file"] = xlsx_path.name
    return df.reset_index(drop=True)


# =========================================================================================
# Ordering + dedupe
# =========================================================================================
def order_and_dedupe(sessions: list[pd.DataFrame]) -> pd.DataFrame:
    """Order sessions chronologically by first ``Date_Time`` and remove duplicated data.

    * Order is by the *first row's* ``Date_Time`` (never the filename; ties broken by longer
      session, then ``source_file``, so the result is deterministic).
    * A session whose time span lies inside the span already covered by earlier sessions is a
      duplicate and is dropped whole (CS2_35/38 ``2_4_11`` == ``2_10_11``, byte-identical data).
      A session that only partially overlaps has its overlapping rows (``Date_Time <=`` the
      covered end) trimmed.
    * Output: one frame, rows in time order, with an integer ``session`` (0..n-1, restarts
      counters), and ``global_time_s`` = seconds since the Unix epoch, anchored on the session's
      first ``Date_Time`` and advanced by ``Test_Time(s)`` (sub-second resolution).

    What was dropped is recorded in ``out.attrs["dedupe_report"]`` (list of strings).
    """
    prepared: list[pd.DataFrame] = []
    for df in sessions:
        if df.empty:
            continue
        d = df.copy()
        d[C_DATE] = pd.to_datetime(d[C_DATE])
        if "source_file" not in d.columns:
            d["source_file"] = "<unknown>"
        prepared.append(d.reset_index(drop=True))

    def sort_key(d: pd.DataFrame) -> tuple[pd.Timestamp, int, str]:
        return (d[C_DATE].iloc[0], -len(d), str(d["source_file"].iloc[0]))

    prepared.sort(key=sort_key)

    report: list[str] = []
    kept: list[pd.DataFrame] = []
    covered_end: pd.Timestamp | None = None
    for d in prepared:
        name = str(d["source_file"].iloc[0])
        start, end = d[C_DATE].iloc[0], d[C_DATE].iloc[-1]
        if covered_end is not None and start <= covered_end:
            if end <= covered_end:
                report.append(
                    f"{name}: duplicate (span {start}..{end} inside covered span), dropped"
                )
                continue
            keep_rows = d[C_DATE] > covered_end
            report.append(
                f"{name}: overlaps earlier data until {covered_end}; "
                f"trimmed {int((~keep_rows).sum())} rows"
            )
            d = d.loc[keep_rows].reset_index(drop=True)
            start = d[C_DATE].iloc[0]
        d["session"] = len(kept)
        t0 = float(d[C_TIME].iloc[0])
        anchor = (start - pd.Timestamp("1970-01-01")).total_seconds()
        d[C_GLOBAL] = anchor + (d[C_TIME].astype(float) - t0)
        kept.append(d)
        covered_end = end if covered_end is None else max(covered_end, end)

    if not kept:
        out = pd.DataFrame(columns=[*REQUIRED_COLUMNS, "source_file", "session", C_GLOBAL])
    else:
        out = pd.concat(kept, ignore_index=True)
    for line in report:
        log.warning(line)
    out.attrs["dedupe_report"] = report
    return out


# =========================================================================================
# Cycle splitting
# =========================================================================================
def _trapz(y: np.ndarray, t: np.ndarray) -> float:
    if len(y) < 2:
        return 0.0
    return float(np.sum(0.5 * (y[1:] + y[:-1]) * np.diff(t)))


def _empty_like(s: pd.DataFrame) -> pd.DataFrame:
    return s.iloc[0:0]


def _discharge_measurements(
    s: pd.DataFrame, a: int, b: int
) -> tuple[float, float, float, float, float]:
    """Counter and integral capacity / energy for the discharge rows ``s[a:b]``.

    The Arbin counter already contains the first logging interval at row ``a``, so the baseline
    is the counter at row ``a - 1`` (0 if the discharge starts the session). The integral is the
    trapezoid over rows ``a-1 .. b-1`` (the ``a-1`` row is a ~0 A rest sample), the same window.
    Returns ``(cap_counter, cap_integral, eng_counter, eng_integral, end_voltage)``.
    """
    lo = max(a - 1, 0)
    dcap = s[C_DCAP].to_numpy(float)
    deng = s[C_DENG].to_numpy(float)
    cap_counter = float(dcap[b - 1] - (dcap[a - 1] if a > 0 else 0.0))
    eng_counter = float(deng[b - 1] - (deng[a - 1] if a > 0 else 0.0))
    t = s[C_TIME].to_numpy(float)[lo:b]
    i = np.abs(s[C_CUR].to_numpy(float)[lo:b])
    v = s[C_VOLT].to_numpy(float)[lo:b]
    cap_integral = _trapz(i, t) / 3600.0
    eng_integral = _trapz(i * v, t) / 3600.0
    return cap_counter, cap_integral, eng_counter, eng_integral, float(v[-1])


def _choose_capacity(counter: float, integral: float) -> tuple[float, str]:
    ok = (
        np.isfinite(counter)
        and counter > 0
        and abs(counter - integral) <= COUNTER_AGREEMENT_TOL * max(integral, 1e-12)
    )
    return (counter, "counter") if ok else (integral, "integral")


def _ir_median(frames: Iterable[pd.DataFrame]) -> float:
    vals = np.concatenate([f[C_IR].to_numpy(float) for f in frames] or [np.empty(0)])
    vals = vals[np.isfinite(vals) & (vals > 0)]
    return float(np.median(vals)) if len(vals) else float("nan")


def _phase_blocks(cur: np.ndarray) -> list[tuple[int, int, int]]:
    """Alternating charge / discharge blocks as ``(sign, first_row, stop_row)``.

    Rest samples (|I| <= threshold) are ignored when deciding block membership: consecutive
    same-sign samples belong to one block even if rest samples sit between them, and an
    isolated opposite-sign sample sandwiched between two same-sign samples is discarded as a
    glitch. A charge block therefore spans CC + rest + CV, and a stray one-sample sign blip
    next to a real phase is absorbed into that phase's block when no opposite-sign sample
    intervenes.
    """
    sign = np.where(cur > I_THRESH_A, 1, np.where(cur < -I_THRESH_A, -1, 0))
    nz = np.flatnonzero(sign != 0)
    if len(nz) == 0:
        return []
    # a single sample whose sign differs from both active neighbours (which agree) is a glitch
    if len(nz) >= 3:
        sg = sign[nz]
        glitch = np.zeros(len(nz), dtype=bool)
        glitch[1:-1] = (sg[1:-1] != sg[:-2]) & (sg[:-2] == sg[2:])
        nz = nz[~glitch]
    changes = np.flatnonzero(np.diff(sign[nz]) != 0) + 1
    first = np.concatenate(([0], changes))
    last = np.concatenate((changes - 1, [len(nz) - 1]))
    return [
        (int(sign[nz[f]]), int(nz[f]), int(nz[last_k]) + 1)
        for f, last_k in zip(first, last, strict=True)
    ]


def _split_session(s: pd.DataFrame, session: int) -> list[CycleRecord]:
    s = s.reset_index(drop=True)
    source = str(s["source_file"].iloc[0]) if "source_file" in s.columns else "<unknown>"
    blocks = _phase_blocks(s[C_CUR].to_numpy(float))
    records: list[CycleRecord] = []
    for j, (sign, a, b) in enumerate(blocks):
        prev_is_charge = j > 0 and blocks[j - 1][0] > 0
        if sign > 0:
            if j == len(blocks) - 1:  # session ended before this cycle's discharge
                records.append(
                    CycleRecord(
                        session=session,
                        source_file=source,
                        charge=s.iloc[a:b],
                        discharge=_empty_like(s),
                        status=NO_DISCHARGE,
                    )
                )
            continue
        charge = s.iloc[blocks[j - 1][1] : blocks[j - 1][2]] if prev_is_charge else _empty_like(s)
        discharge = s.iloc[a:b]
        cap_c, cap_i, eng_c, eng_i, end_v = _discharge_measurements(s, a, b)
        cap, src = _choose_capacity(cap_c, cap_i)
        if end_v > MAX_END_VOLTAGE_V:
            status = INCOMPLETE_DISCHARGE
        elif cap < MIN_DISCHARGE_AH:
            status = LOW_CAPACITY
        elif charge.empty:
            status = NO_CHARGE
        else:
            status = KEPT
        records.append(
            CycleRecord(
                session=session,
                source_file=source,
                charge=charge,
                discharge=discharge,
                status=status,
                capacity_counter_ah=cap_c,
                capacity_integral_ah=cap_i,
                capacity_ah=cap,
                energy_counter_wh=eng_c,
                energy_integral_wh=eng_i,
                discharge_end_v=end_v,
                ir_ohm=_ir_median([charge]),  # charge only: discharge k measures the target
                capacity_source=src,
            )
        )
    return records


def split_cycles(df: pd.DataFrame) -> list[CycleRecord]:
    """Split an ordered multi-session frame into candidate cycles (kept and dropped).

    ``df`` is the output of :func:`order_and_dedupe` (needs ``session`` and the raw columns in
    ``REQUIRED_COLUMNS`` except ``Date_Time``). Cycles never span sessions: counters and Arbin
    indices restart per session and sessions are separated by hours to days of idle time.
    Records come back in chronological order; ``record.kept`` selects the cycles to export.
    """
    records: list[CycleRecord] = []
    for session, s in df.groupby("session", sort=True):
        records.extend(_split_session(s, int(str(session))))
    return records


# =========================================================================================
# Tables
# =========================================================================================
def _cumulative_ah(i: np.ndarray, t: np.ndarray) -> np.ndarray:
    """Cumulative trapezoid of |I| dt / 3600, starting at 0 (Ah)."""
    if len(i) == 0:
        return np.empty(0)
    a = np.abs(i)
    inc = 0.5 * (a[1:] + a[:-1]) * np.diff(t) / 3600.0
    return np.concatenate(([0.0], np.cumsum(inc)))


def _curve_frame(
    ph: pd.DataFrame, cell_id: str, cycle_idx: int, phase: str
) -> tuple[pd.DataFrame, np.ndarray]:
    t_abs = ph[C_TIME].to_numpy(float)
    t = t_abs - t_abs[0]
    i = ph[C_CUR].to_numpy(float)
    ah = _cumulative_ah(i, t)
    out = pd.DataFrame(
        {
            "dataset": DATASET,
            "cell_id": cell_id,
            "cycle_idx": cycle_idx,
            "phase": phase,
            "sample_idx": np.arange(len(ph), dtype=np.int64),
            "t_s": t,
            "voltage_v": ph[C_VOLT].to_numpy(float),
            "current_a": i,
            "temp_c": np.nan,
            "charge_ah": ah,
        }
    )
    return out, ah


def _charge_features(ph: pd.DataFrame, ah: np.ndarray) -> dict[str, float]:
    t = ph[C_TIME].to_numpy(float)
    t = t - t[0]
    v = ph[C_VOLT].to_numpy(float)
    reached = np.flatnonzero(v >= CC_END_VOLTAGE_V)
    total = float(t[-1])
    cc = float(t[reached[0]]) if len(reached) else float("nan")
    return {
        "charge_time_s": total,
        "cc_time_s": cc,
        "cv_time_s": total - cc if np.isfinite(cc) else float("nan"),
        "charge_throughput_ah": float(ah[-1]),
    }


def cycles_and_curves(
    records: list[CycleRecord], cell_id: str
) -> tuple[pd.DataFrame, pd.DataFrame, CellStats]:
    """Turn candidate cycles into the ``cycles`` / ``curves`` tables (kept cycles only)."""
    stats = CellStats(cell_id=cell_id)
    rows: list[dict[str, object]] = []
    curve_parts: list[pd.DataFrame] = []
    prev_discharge_end: float | None = None
    for rec in records:
        if not rec.kept:
            stats.dropped[rec.status] += 1
            continue
        idx = len(rows) + 1
        ch_curve, ch_ah = _curve_frame(rec.charge, cell_id, idx, "charge")
        di_curve, _ = _curve_frame(rec.discharge, cell_id, idx, "discharge")
        curve_parts += [ch_curve, di_curve]
        feats = _charge_features(rec.charge, ch_ah)
        charge_start = float(rec.charge[C_GLOBAL].iloc[0])
        rest = np.nan if prev_discharge_end is None else charge_start - prev_discharge_end
        prev_discharge_end = float(rec.discharge[C_GLOBAL].iloc[-1])
        energy = rec.energy_counter_wh
        if not np.isfinite(energy) or energy <= 0:
            energy = rec.energy_integral_wh
        rows.append(
            {
                "dataset": DATASET,
                "cell_id": cell_id,
                "cycle_idx": idx,
                "capacity_ah": rec.capacity_ah,
                **feats,
                "discharge_time_s": float(
                    rec.discharge[C_TIME].iloc[-1] - rec.discharge[C_TIME].iloc[0]
                ),
                "discharge_energy_wh": energy,
                "ir_ohm": rec.ir_ohm,
                "rest_before_s": rest,
            }
        )
        denom = max(rec.capacity_integral_ah, 1e-12)
        rel = abs(rec.capacity_counter_ah - rec.capacity_integral_ah) / denom
        stats.max_counter_integral_rel_diff = max(stats.max_counter_integral_rel_diff, rel)
        if rec.capacity_source != "counter":
            stats.n_counter_integral_mismatch += 1
        if feats["cv_time_s"] < NO_CV_TIME_S:
            stats.n_kept_no_cv += 1
    stats.n_kept = len(rows)
    cycles = pd.DataFrame(rows)
    curves = pd.concat(curve_parts, ignore_index=True) if curve_parts else pd.DataFrame()
    return cycles, curves, stats


def _xlsx_files(cell_dir: Path) -> list[Path]:
    return sorted(p for p in cell_dir.glob("*.xlsx") if not p.name.startswith("~$"))


def load_cell_detailed(cell_dir: Path, cell_id: str) -> CellLoad:
    """Parse every workbook of one cell once and build its cycles / curves + parse statistics."""
    t0 = time.perf_counter()
    files = _xlsx_files(Path(cell_dir))
    if not files:
        raise FileNotFoundError(f"no .xlsx files in {cell_dir}")
    sessions = [read_session(p) for p in files]
    ordered = order_and_dedupe(sessions)
    records = split_cycles(ordered)
    cycles, curves, stats = cycles_and_curves(records, cell_id)
    stats.n_files = len(files)
    stats.n_sessions_used = int(ordered["session"].nunique())
    stats.dedupe_report = list(ordered.attrs.get("dedupe_report", []))
    stats.seconds = time.perf_counter() - t0
    return CellLoad(cycles=cycles, curves=curves, stats=stats)


def load_cell(cell_dir: Path, cell_id: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return ``(cycles, curves)`` for one cell (see :func:`load_cell_detailed` for stats)."""
    res = load_cell_detailed(cell_dir, cell_id)
    return res.cycles, res.curves


def cells_row(cell_id: str) -> dict[str, object]:
    return {
        "dataset": DATASET,
        "cell_id": cell_id,
        "chemistry": "LiCoO2/graphite",
        "nominal_capacity_ah": 1.1,
        "charge_protocol": CHARGE_PROTOCOL,
        "discharge_protocol": DISCHARGE_PROTOCOL,
        "ambient_temp_c": float("nan"),  # not logged
        "v_max": 4.2,
        "v_min": 2.7,
        "batch": None,
        "split": None,
        "reported_cycle_life": None,
        "source_file": f"{cell_id}.zip",
    }


def _ensure_extracted(raw_dir: Path, cell_id: str) -> Path:
    cell_dir = raw_dir / cell_id
    if cell_dir.is_dir() and any(cell_dir.glob("*.xlsx")):
        return cell_dir
    zpath = raw_dir / f"{cell_id}.zip"
    if not zpath.exists():
        raise FileNotFoundError(
            f"neither {cell_dir} nor {zpath} exists; run `battery-rul download calce`"
        )
    with zipfile.ZipFile(zpath) as zf:
        zf.extractall(raw_dir)
    return cell_dir


def build(
    raw_dir: Path = RAW_DIR / "calce",
    out_root: Path = PROCESSED_DIR,
    cell_ids: Iterable[str] = CELL_IDS,
) -> DatasetTables:
    """Parse all CALCE CS2 cells, validate against the schema and write the parquet tables."""
    cells: list[dict[str, object]] = []
    cycle_parts: list[pd.DataFrame] = []
    curve_parts: list[pd.DataFrame] = []
    for cell_id in cell_ids:
        res = load_cell_detailed(_ensure_extracted(Path(raw_dir), cell_id), cell_id)
        s = res.stats
        log.info(
            "%s: %d files, %d sessions, %d kept, dropped %s, %.1fs",
            cell_id,
            s.n_files,
            s.n_sessions_used,
            s.n_kept,
            dict(s.dropped),
            s.seconds,
        )
        cells.append(cells_row(cell_id))
        cycle_parts.append(res.cycles)
        curve_parts.append(res.curves)
    tables = finalize_and_validate(
        pd.DataFrame(cells),
        pd.concat(cycle_parts, ignore_index=True),
        pd.concat(curve_parts, ignore_index=True),
    )
    write_tables(DATASET, tables, out_root)
    return tables
