"""Field-realistic (BMS-measurable, capacity-free) charge-side features for Toyota / Severson.

Every Toyota cell charges with its own multi-step fast-charge policy up to ~80 % SOC (the
experimental variable), rests ~60 s at I = 0, charges at 1C CC up to 3.6 V and then holds 3.6 V
(CV) until the current has decayed. Only the **protocol-common** part (rest + 1C CC + CV) is used,
so the features do not encode the policy and need no capacity measurement:

``fld_relax_v0/v1/dv/s``  voltage at the start of the I ~ 0 rest and ``RELAX_AT_S`` = 8 s into
                          it, their difference (V), and the rest duration (s, diagnostic only;
                          protocol-dependent). NaN without such a rest.
``fld_win_*``             a fixed voltage window ``[V_LO, V_HI]`` inside the 1C CC segment:
                          charge passed (Ah, from the raw ``Qc`` counter differences, a coulomb
                          count a BMS can do on a partial charge) and time (s) inside it;
                          ``fld_q_v00..15`` is the charge from ``V_LO`` at 16 equally spaced
                          voltages; ``fld_win_valid`` says the window is fully covered.
``fld_ica_v/h``           location (V) and height (Ah/V) of the largest dQ/dV peak in the window.
``fld_cv_s``              duration (s) of the 3.6 V CV phase that follows the 1C CC segment.
``fld_chg_temp_max_c`` / ``fld_chg_temp_mean_c``  max / time-weighted mean cell temperature
                          (degC) over the 1C CC + CV segment.

Units: ``t`` minutes, ``v`` V, ``i`` C-rate (1C = 1.1 A), ``qc`` Ah (as in the raw files).
Capacity-derived quantities (discharge capacity, discharge curves, throughput from empty, total
charge time) are never used.
"""

from __future__ import annotations

import argparse
import json
import logging
import subprocess
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Final

import numpy as np
import pandas as pd

from battery_rul.data.toyota import (
    BATCH_DATES,
    CAP_MAX_AH,
    CAP_MIN_AH,
    CONTINUATIONS,
    DATASET,
    I_CHARGE_MIN,
    V_MAX,
    RawCell,
    assemble_cells,
)
from battery_rul.features.curves import CurveSpec, ica_features
from battery_rul.utils import PROCESSED_DIR, RAW_DIR

log = logging.getLogger(__name__)

KEY: Final = ["dataset", "cell_id", "cycle_idx"]
#: voltage window inside the 1C CC segment (chosen empirically, see ``field_features.json``)
V_LO: Final = 3.50
V_HI: Final = 3.58
N_GRID: Final = 16
#: ICA grid step (V); the Savitzky-Golay filter of ``features.curves`` then uses 9 points
ICA_STEP: Final = 0.0025
I_REST: Final = 0.02  # C-rate; |I| below this is a rest
#: shortest accepted rest; measured rest length: ~10 s batch 3, ~56 s batch 1, ~296 s batch 2
REST_MIN_S: Final = 5.0
#: Relaxation is read at this fixed elapsed time after the rest starts. Batch 2018-04-12 (the
#: official test2 cells) rests ~10 s instead of ~60 s, so "V at the end of the rest" measures a
#: different relaxation stage there; a fixed elapsed time common to every protocol does not.
RELAX_AT_S: Final = 8.0
I_1C_HI: Final = 1.25  # C-rate; the step after the rest is 1C (at most this)
CV_TOL_V: Final = 0.005
AH_PER_C: Final = 1.1

Q_COLS: Final = [f"fld_q_v{k:02d}" for k in range(N_GRID)]
FEATURE_COLS: Final = [
    "fld_relax_v0",
    "fld_relax_v1",
    "fld_relax_dv",
    "fld_relax_s",
    "fld_win_dq_ah",
    "fld_win_dt_s",
    *Q_COLS,
    "fld_win_valid",
    "fld_ica_v",
    "fld_ica_h",
    "fld_cv_s",
    "fld_chg_temp_max_c",
    "fld_chg_temp_mean_c",
]


@dataclass(frozen=True)
class Segments:
    """Sample indices of one charge. ``None`` = segment not found.

    ``start``/``end`` bound the whole charge (first/last ``I > 0.01`` C before the discharge).
    The fast step is ``[start, rest0)``; the rest is ``[rest0, rest1]`` (inclusive, ``I ~ 0``);
    the 1C CC segment is ``[cc0, cv0)`` and the CV segment ``[cv0, end]``.
    """

    start: int
    end: int
    rest0: int | None = None
    rest1: int | None = None
    cc0: int | None = None
    cv0: int | None = None


def segment_charge(t: np.ndarray, v: np.ndarray, i: np.ndarray) -> Segments | None:
    """Locate fast step / rest / 1C CC / CV in one raw cycle (None if there is no charge).

    The charge runs from the first ``I > 0.01`` C sample to the last one before the first
    discharge sample. The protocol rest is the *last* run of ``|I| < 0.02`` C lasting at least 20 s
    that is followed within 3 samples by charging at up to 1.25 C. The 1C CC segment starts at
    that sample and ends at the first sample with ``V >= 3.595`` V (CV start; the CV runs to the
    end of the charge). A charge whose fast step already reached 3.6 V is handled the same way
    (the CC segment is then short).
    """
    pos = np.flatnonzero(i > I_CHARGE_MIN)
    if pos.size == 0:
        return None
    neg = np.flatnonzero((i < -I_CHARGE_MIN) & (np.arange(i.size) > pos[0]))
    if neg.size == 0:
        return None
    seg = pos[pos < neg[0]]
    p0, p1 = int(seg[0]), int(seg[-1])
    base = Segments(p0, p1)
    idx = np.arange(p0, p1 + 1)
    zero = np.abs(i[idx]) < I_REST
    if not zero.any():
        return base
    edges = np.flatnonzero(np.diff(np.concatenate([[0], zero.astype(np.int8), [0]])))
    starts, stops = edges[0::2], edges[1::2] - 1  # inclusive runs inside idx
    for a, b in zip(starts[::-1], stops[::-1], strict=True):
        a_i, b_i = int(idx[a]), int(idx[b])
        if b_i >= p1:
            continue
        if (t[b_i] - t[a_i]) * 60.0 < REST_MIN_S:
            continue
        # first charging sample after the rest: at most 1C (the 1C step ramps up over 1-3 samples;
        # in late life it decays at once when V is already at 3.6 V, so there is no lower bound
        # beyond "charging"). A higher current means this was a fast-step-internal pause.
        cand = [
            k for k in (b_i + 1, b_i + 2, b_i + 3) if k <= p1 and I_CHARGE_MIN < i[k] <= I_1C_HI
        ]
        if not cand or i[b_i + 1] > I_1C_HI:
            continue
        nxt = cand[0]
        hit = np.flatnonzero(v[nxt : p1 + 1] >= V_MAX - CV_TOL_V)
        cv0 = nxt + int(hit[0]) if hit.size else None
        return Segments(p0, p1, a_i, b_i, nxt, cv0)
    return base


def relaxation_features(t: np.ndarray, v: np.ndarray, seg: Segments) -> dict[str, float]:
    """Relaxation block: V at rest start / end, their difference (V) and duration (s)."""
    nan = float("nan")
    if seg.rest0 is None or seg.rest1 is None:
        return {"fld_relax_v0": nan, "fld_relax_v1": nan, "fld_relax_dv": nan, "fld_relax_s": nan}
    # v0 = first rest sample (V relaxes fast); v1 = V at RELAX_AT_S after the rest starts,
    # linearly interpolated (protocol-invariant: every policy rests at least ~10 s). If the rest
    # is shorter than that, v1 is the last rest sample.
    v0 = float(v[seg.rest0])
    tr = (t[seg.rest0 : seg.rest1 + 1] - t[seg.rest0]) * 60.0
    vr = v[seg.rest0 : seg.rest1 + 1]
    v1 = float(np.interp(RELAX_AT_S, tr, vr)) if tr[-1] >= RELAX_AT_S else float(vr[-1])
    return {
        "fld_relax_v0": v0,
        "fld_relax_v1": v1,
        "fld_relax_dv": v1 - v0,
        "fld_relax_s": float((t[seg.rest1] - t[seg.rest0]) * 60.0),
    }


def _cross(vm: np.ndarray, x: np.ndarray, level: float) -> float:
    """``x`` linearly interpolated at the first crossing of ``level`` by non-decreasing ``vm``."""
    k = int(np.searchsorted(vm, level, side="left"))
    if k == 0:
        return float(x[0])
    dv = vm[k] - vm[k - 1]
    w = 0.0 if dv <= 0 else (level - vm[k - 1]) / dv
    return float(x[k - 1] + w * (x[k] - x[k - 1]))


def window_features(
    t: np.ndarray,
    v: np.ndarray,
    qc: np.ndarray,
    cc0: int | None,
    cv0: int | None,
    v_lo: float = V_LO,
    v_hi: float = V_HI,
    n_grid: int = N_GRID,
) -> dict[str, Any]:
    """Window block from the 1C CC samples ``[cc0, cv0)`` (``cv0=None``: up to the charge end).

    ``qc`` is the cumulative charge counter (Ah). The window is *covered* iff the first CC sample
    is at or below ``v_lo`` and the CC voltage reaches ``v_hi``; otherwise every window value is
    NaN and ``fld_win_valid`` is False. Voltage is made monotone (running maximum) before the
    crossings are interpolated. The ICA peak comes from ``features.curves.ica_features``.
    """
    nan = float("nan")
    out: dict[str, Any] = {
        "fld_win_dq_ah": nan,
        "fld_win_dt_s": nan,
        **dict.fromkeys(Q_COLS, nan),
        "fld_win_valid": False,
        "fld_ica_v": nan,
        "fld_ica_h": nan,
    }
    if cc0 is None:
        return out
    stop = len(v) if cv0 is None else cv0
    # include the CV-start sample so a crossing in the last CC interval can be interpolated
    sl = slice(cc0, min(stop + 1, len(v)))
    vm = np.maximum.accumulate(v[sl])
    if vm.size < 3 or vm[0] > v_lo or vm[-1] < v_hi:
        return out
    tt, qq = t[sl] * 60.0, qc[sl]
    grid = np.linspace(v_lo, v_hi, n_grid)
    q_at = np.array([_cross(vm, qq, g) for g in grid])
    q_rel = q_at - q_at[0]
    out["fld_win_dq_ah"] = float(q_rel[-1])
    out["fld_win_dt_s"] = _cross(vm, tt, v_hi) - _cross(vm, tt, v_lo)
    out.update(zip(Q_COLS, q_rel.tolist(), strict=True))
    out["fld_win_valid"] = True
    n_fine = round((v_hi - v_lo) / ICA_STEP) + 1
    fine = np.linspace(v_lo, v_hi, n_fine)
    q_fine = np.array([_cross(vm, qq, g) for g in fine]) - q_at[0]
    spec = CurveSpec("charge", "fld", v_lo, v_hi, ICA_STEP, v_lo, v_hi, 0.0, True, 1.0, True)
    peak = ica_features(q_fine[None, :], spec)[0]
    out["fld_ica_v"], out["fld_ica_h"] = float(peak[0]), float(peak[1])
    return out


def common_temperature(t: np.ndarray, temp: np.ndarray, seg: Segments) -> tuple[float, float]:
    """(max, time-weighted mean) temperature in degC over the 1C CC + CV segment."""
    nan = float("nan")
    if seg.cc0 is None or seg.end - seg.cc0 < 2:
        return nan, nan
    tt = t[seg.cc0 : seg.end + 1]
    x = temp[seg.cc0 : seg.end + 1]
    ok = np.isfinite(x)
    if ok.sum() < 2 or tt[-1] <= tt[0]:
        return nan, nan
    tt, x = tt[ok], x[ok]
    mean = float(np.trapezoid(x, tt) / (tt[-1] - tt[0]))
    return float(x.max()), mean


def cycle_features(
    t: np.ndarray, v: np.ndarray, i: np.ndarray, temp: np.ndarray, qc: np.ndarray
) -> dict[str, Any]:
    """All ``fld_*`` features of one raw cycle."""
    nan = float("nan")
    seg = segment_charge(t, v, i)
    if seg is None:
        row: dict[str, Any] = dict.fromkeys(FEATURE_COLS, nan)
        row["fld_win_valid"] = False
        return row
    row = {**relaxation_features(t, v, seg), **window_features(t, v, qc, seg.cc0, seg.cv0)}
    row["fld_cv_s"] = float((t[seg.end] - t[seg.cv0]) * 60.0) if seg.cv0 is not None else nan
    row["fld_chg_temp_max_c"], row["fld_chg_temp_mean_c"] = common_temperature(t, temp, seg)
    return {k: row[k] for k in FEATURE_COLS}


# --------------------------------------------------------------------------- raw streaming


class _RawSource:
    """Per-cell lazy access to ``t, V, I, T, Qc`` (adds T and Qc to ``toyota.read_batch``).

    Cell ids / continuation merging follow :func:`toyota.assemble_cells` exactly: a merged
    batch-1 cell yields its own cycles followed by those of its batch-2 continuation.
    """

    FIELDS: Final = ("t", "V", "I", "T", "Qc")

    def __init__(self, raw_dir: Path) -> None:
        import h5py

        self.files: dict[int, Any] = {}
        for n, d in BATCH_DATES.items():
            path = next(raw_dir.glob(f"{d}_*.mat"))
            self.files[n] = h5py.File(path, "r")

    def close(self) -> None:
        for f in self.files.values():
            f.close()

    def _loaders(self, batch: int, k: int) -> list[Callable[[], dict[str, np.ndarray]]]:
        f = self.files[batch]
        cyc = f[f["batch"]["cycles"][k, 0]]
        refs = {name: cyc[name][:, 0] for name in self.FIELDS}

        def make(j: int) -> Callable[[], dict[str, np.ndarray]]:
            return lambda: {
                n: np.asarray(f[refs[n][j]][()], dtype=float).ravel() for n in self.FIELDS
            }

        return [make(j) for j in range(refs["t"].shape[0])]

    def cell_loaders(self, cell_id: str) -> list[Callable[[], dict[str, np.ndarray]]]:
        batch, k = (int(x) for x in cell_id[1:].split("c"))
        out = self._loaders(batch, k)
        if cell_id in CONTINUATIONS:
            c2 = CONTINUATIONS[cell_id][0]
            out += self._loaders(2, int(c2.split("c")[1]))
        return out


def kept_cycles(cell: RawCell) -> list[tuple[int, int]]:
    """``(summary index, cycle_idx)`` of the cycles in ``cycles.parquet`` (same keep rule)."""
    qd = cell.summary["QDischarge"]
    keep = np.isfinite(qd) & (qd > CAP_MIN_AH) & (qd < CAP_MAX_AH)
    return [(int(k), round(float(cell.summary["cycle"][k]))) for k in np.flatnonzero(keep)]


def cell_features(cell: RawCell, source: _RawSource) -> pd.DataFrame:
    """One row per kept cycle of ``cell`` (loads a single cycle at a time)."""
    loaders = source.cell_loaders(cell.cell_id)
    if len(loaders) != cell.summary["cycle"].size:
        raise ValueError(f"{cell.cell_id}: {len(loaders)} raw cycles vs summary mismatch")
    rows = []
    for k, cyc in kept_cycles(cell):
        r = loaders[k]()
        feats = cycle_features(r["t"], r["V"], r["I"], r["T"], r["Qc"])
        rows.append({"dataset": DATASET, "cell_id": cell.cell_id, "cycle_idx": cyc, **feats})
    return pd.DataFrame(rows, columns=[*KEY, *FEATURE_COLS])


def build_field_features(
    raw_dir: Path = RAW_DIR / "toyota",
    processed_dir: Path = PROCESSED_DIR / "toyota",
    cells: Iterable[str] | None = None,
) -> pd.DataFrame:
    """Stream the 3 batches cell by cell and return the feature table.

    Keys are checked against ``<processed_dir>/cycles.parquet`` (full runs must match exactly).
    """
    wanted = set(cells) if cells is not None else None
    all_cells = assemble_cells(raw_dir)
    source = _RawSource(raw_dir)
    parts: list[pd.DataFrame] = []
    try:
        for c in all_cells:
            if wanted is not None and c.cell_id not in wanted:
                continue
            parts.append(cell_features(c, source))
            log.info("%s: %d cycles", c.cell_id, len(parts[-1]))
    finally:
        source.close()
    df = pd.concat(parts, ignore_index=True)
    ref_path = processed_dir / "cycles.parquet"
    if ref_path.exists():
        ref = pd.read_parquet(ref_path, columns=KEY)
        if wanted is not None:
            ref = ref[ref["cell_id"].isin(wanted)]
        a = df[KEY].sort_values(KEY).reset_index(drop=True)
        b = ref.sort_values(KEY).reset_index(drop=True)
        a["cell_id"], b["cell_id"] = a["cell_id"].astype(str), b["cell_id"].astype(str)
        if not a.equals(b[KEY]):
            raise ValueError("field-feature keys differ from cycles.parquet")
    return df


def _git_sha() -> str:
    try:
        r = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            cwd=__file__ and Path(__file__).parent,
        )
        return r.stdout.strip()
    except Exception:
        return "unknown"


def summary_json(df: pd.DataFrame) -> dict[str, Any]:
    """Window / grid / rules / coverage description written next to the parquet."""
    cov = {c: float(df[c].notna().mean()) for c in FEATURE_COLS if c != "fld_win_valid"}
    per_cell = df.groupby("cell_id")["fld_win_valid"].mean()
    return {
        "code_git_sha": _git_sha(),
        "n_rows": len(df),
        "n_cells": int(df["cell_id"].nunique()),
        "window_v": [V_LO, V_HI],
        "n_grid": N_GRID,
        "ica_step_v": ICA_STEP,
        "window_valid_frac": float(df["fld_win_valid"].mean()),
        "window_valid_frac_per_cell_min": float(per_cell.min()),
        "non_null_frac": cov,
        "rules": {
            "charge": "first I>0.01C to last I>0.01C before first I<-0.01C",
            "rest": f"last run of |I|<{I_REST}C lasting >={REST_MIN_S}s followed by charging "
            f"at <= {I_1C_HI}C",
            "cc_1c": "from first 1C sample after rest until V>=3.595V",
            "cv": "from first V>=3.595V in the 1C segment to charge end",
            "q": "differences of the raw Qc counter inside the window",
            "temperature": "raw T over 1C CC + CV; mean is time-weighted (trapezoid)",
        },
    }


def main(argv: Sequence[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raw-dir", type=Path, default=RAW_DIR / "toyota")
    ap.add_argument("--processed-dir", type=Path, default=PROCESSED_DIR / "toyota")
    ap.add_argument("--cells", nargs="*", default=None, help="subset of cell ids (testing)")
    ap.add_argument("--out", type=Path, default=None, help="output parquet path")
    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    out = args.out or args.processed_dir / "field_features.parquet"
    df = build_field_features(args.raw_dir, args.processed_dir, args.cells)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    out.with_suffix(".json").write_text(json.dumps(summary_json(df), indent=2))
    log.info("wrote %s (%d rows)", out, len(df))


if __name__ == "__main__":
    main()
