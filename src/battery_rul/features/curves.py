"""Physics-informed per-cycle curve features: voltage-grid Q(V), ICA (dQ/dV) and dQ(V) vs a
causal reference (PLAN §6.5 row B).

Every feature is tagged with the phase of the curve it was computed from, in its column prefix:

``chg_*``  computed from the **charge** curve of cycle k (NASA, CALCE). Charge of cycle k precedes
           discharge k, so Task A may use it as a current-cycle input (PROTOCOL §2).
``dis_*``  computed from the **discharge** curve of cycle k (Toyota). Near-copy of the target
           capacity: history-only for Task A (leakage rule 3). The sample builder enforces this.

Columns (``<p>`` = ``chg`` or ``dis``):
    <p>_ica_peak_v   voltage (V) of the dQ/dV maximum inside the dataset's peak-search window
    <p>_ica_peak_h   dQ/dV at the peak (Ah/V)
    <p>_ica_area     capacity (Ah) inside peak +- half-width (integral of dQ/dV)
    <p>_dq_var       variance (Ah^2) of dQ(V) = Q_k(V) - Q_ref(V) over the grid
    <p>_dq_min       min of dQ(V) (Ah)
    <p>_dq_mean      mean of dQ(V) (Ah)

Grids / windows (documented per dataset, :data:`SPECS`):
    nasa, calce  charge constant-current segment only (the CV part carries no voltage information),
                 grid 3.80-4.19 V in 5 mV steps, Q measured from the 3.80 V crossing (so partial
                 charges that start higher or lower do not shift the curve). Peak search
                 3.85-4.15 V, area window +-40 mV. A cycle whose CC segment does not cover the whole
                 grid gets NaN features.
    toyota       discharge Q(V) on the stored 100-point grid (3.5 -> 2.0 V), resampled to an
                 ascending 2.02-3.5 V grid; peak search 2.6-3.4 V, area +-100 mV.

ICA: Savitzky-Golay (window 9 points, order 3, first derivative) on the grid. dQ(V) uses the
**causal reference** Q_ref(V) = mean Q(V) over the cell's first 5 valid cycles. Rows before the
fifth valid cycle get NaN dQ features, so no row ever depends on a cycle later than itself
(leakage rule 2). Charge-direction sign convention: ICA values are positive for both phases.

This module never reads labels, EOL or quality flags (leakage rule 5).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Final

import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

from battery_rul.utils import PROCESSED_DIR

KEY: Final = ["dataset", "cell_id", "cycle_idx"]
N_REF: Final = 5  # reference cycles (same as the SOH reference, schema.SOH_REFERENCE_CYCLES)
SG_WINDOW: Final = 9
SG_ORDER: Final = 3
FEATURES: Final = ("ica_peak_v", "ica_peak_h", "ica_area", "dq_var", "dq_min", "dq_mean")


@dataclass(frozen=True)
class CurveSpec:
    phase: str  # curves.phase to read
    prefix: str  # chg | dis
    v_lo: float
    v_hi: float
    step: float
    peak_lo: float
    peak_hi: float
    area_half_width: float
    cc_only: bool  # truncate at the first sample reaching v_hi (charge CC segment)
    sign: float  # +1 if Q grows with V (charge), -1 if it shrinks (discharge)
    relative: bool  # measure Q from the v_lo crossing

    @property
    def grid(self) -> np.ndarray:
        n = round((self.v_hi - self.v_lo) / self.step) + 1
        return np.linspace(self.v_lo, self.v_hi, n)


_CHG = CurveSpec("charge", "chg", 3.80, 4.19, 0.005, 3.85, 4.15, 0.04, True, 1.0, True)
_DIS = CurveSpec("discharge", "dis", 2.02, 3.5, 0.015, 2.6, 3.4, 0.10, False, -1.0, False)
SPECS: Final[dict[str, CurveSpec]] = {"nasa": _CHG, "calce": _CHG, "toyota": _DIS}


def feature_columns(prefix: str) -> list[str]:
    return [f"{prefix}_{f}" for f in FEATURES]


# --------------------------------------------------------------------------------------
# Q(V) on a grid
# --------------------------------------------------------------------------------------
def _segments(curves: pd.DataFrame, phase: str) -> tuple[pd.DataFrame, np.ndarray]:
    """Rows of one phase sorted by (cell, cycle, sample) and segment start offsets."""
    sub = curves.loc[
        curves["phase"] == phase,
        ["cell_id", "cycle_idx", "sample_idx", "voltage_v", "charge_ah"],
    ]
    codes = pd.factorize(sub["cell_id"])[0]
    order = np.lexsort((sub["sample_idx"].to_numpy(), sub["cycle_idx"].to_numpy(), codes))
    sub = sub.iloc[order].reset_index(drop=True)
    cc = codes[order]
    ci = sub["cycle_idx"].to_numpy()
    brk = np.flatnonzero((np.diff(cc) != 0) | (np.diff(ci) != 0)) + 1
    return sub, np.concatenate([[0], brk, [len(sub)]])


def resample_curve(v: np.ndarray, q: np.ndarray, spec: CurveSpec) -> np.ndarray | None:
    """Q on ``spec.grid`` for one (cycle, phase) curve, or None when the grid is not fully covered.

    Charge: only the CC segment (up to the first sample at/above ``v_hi``), voltage made monotone
    non-decreasing, Q measured from the ``v_lo`` crossing. Discharge: voltage reversed to ascending.
    """
    ok = np.isfinite(v) & np.isfinite(q)
    v, q = v[ok], q[ok]
    if v.size < 5:
        return None
    if spec.cc_only:
        hit = np.flatnonzero(v >= spec.v_hi)
        if hit.size == 0:
            return None
        v, q = v[: hit[0] + 2], q[: hit[0] + 2]
        v = np.maximum.accumulate(v)
    else:
        v, q = v[::-1], q[::-1]  # discharge voltage falls -> ascending
        v = np.maximum.accumulate(v)
    grid = spec.grid
    if v[0] > grid[0] + 1e-9 or v[-1] < grid[-1] - 1e-9:
        return None
    out = np.interp(grid, v, q)
    if spec.relative:
        out = out - out[0]
    return np.asarray(out, dtype=np.float64)


def grid_curves(curves: pd.DataFrame, spec: CurveSpec) -> tuple[pd.DataFrame, np.ndarray]:
    """(keys, Q matrix (n_cycles, n_grid)); rows with incomplete grid coverage are NaN."""
    sub, bounds = _segments(curves, spec.phase)
    v_all = sub["voltage_v"].to_numpy(dtype=np.float64)
    q_all = sub["charge_ah"].to_numpy(dtype=np.float64)
    n = len(bounds) - 1
    mat = np.full((n, len(spec.grid)), np.nan)
    for i in range(n):
        a, b = bounds[i], bounds[i + 1]
        r = resample_curve(v_all[a:b], q_all[a:b], spec)
        if r is not None:
            mat[i] = r
    first = bounds[:-1]
    keys = sub.iloc[first][["cell_id", "cycle_idx"]].reset_index(drop=True)
    return keys, mat


# --------------------------------------------------------------------------------------
# ICA and dQ(V)
# --------------------------------------------------------------------------------------
def ica_features(q_mat: np.ndarray, spec: CurveSpec) -> np.ndarray:
    """(n, 3) peak voltage, peak height, area for each Q(V) row (NaN rows stay NaN)."""
    grid = spec.grid
    dv = float(grid[1] - grid[0])
    out = np.full((len(q_mat), 3), np.nan)
    good = np.isfinite(q_mat).all(axis=1)
    if not good.any():
        return out
    d = spec.sign * savgol_filter(
        q_mat[good], SG_WINDOW, SG_ORDER, deriv=1, delta=dv, axis=1, mode="interp"
    )
    win = (grid >= spec.peak_lo) & (grid <= spec.peak_hi)
    idx = np.flatnonzero(win)
    sub = d[:, idx]
    j = sub.argmax(axis=1)
    rows = np.arange(len(d))
    jj = np.clip(j, 1, len(idx) - 2)
    y0, y1, y2 = sub[rows, jj - 1], sub[rows, jj], sub[rows, jj + 1]
    denom = y0 - 2 * y1 + y2
    with np.errstate(divide="ignore", invalid="ignore"):
        off = np.where(np.abs(denom) > 1e-12, 0.5 * (y0 - y2) / denom, 0.0)
    off = np.where(j == jj, np.clip(off, -1.0, 1.0), 0.0)  # parabolic refinement (interior only)
    pv = grid[idx[jj]] + off * dv
    ph = y1 - 0.25 * (y0 - y2) * off
    mask = np.abs(grid[None, :] - pv[:, None]) <= spec.area_half_width + 1e-9
    area = (np.where(mask, d, 0.0)).sum(axis=1) * dv
    out[good] = np.column_stack([pv, ph, area])
    return out


def delta_q_stats(dq: np.ndarray) -> np.ndarray:
    """(n, 3) variance, min, mean of each dQ(V) row; NaN rows stay NaN."""
    out = np.full((len(dq), 3), np.nan)
    good = np.isfinite(dq).all(axis=1)
    if good.any():
        out[good] = np.column_stack(
            [dq[good].var(axis=1), dq[good].min(axis=1), dq[good].mean(axis=1)]
        )
    return out


def _causal_dq(q_mat: np.ndarray) -> np.ndarray:
    """dQ rows for ONE cell (ordered by cycle): Q - mean(Q of first N_REF valid cycles).

    Rows up to and including the (N_REF-1)-th valid cycle have no complete reference yet, so they
    are NaN; the row of the N_REF-th valid cycle is the first with a reference (which contains
    itself and earlier cycles only).
    """
    valid = np.flatnonzero(np.isfinite(q_mat).all(axis=1))
    dq = np.full_like(q_mat, np.nan)
    if len(valid) < N_REF:
        return dq
    ref = q_mat[valid[:N_REF]].mean(axis=0)
    start = valid[N_REF - 1]
    dq[start:] = q_mat[start:] - ref
    return dq


def curve_features(curves: pd.DataFrame, dataset: str) -> pd.DataFrame:
    """Per-cycle curve features for one dataset, keyed (dataset, cell_id, cycle_idx).

    ``curves`` is the canonical long-format curves table (only the columns ``cell_id, cycle_idx,
    phase, sample_idx, voltage_v, charge_ah`` are read). Output columns are
    ``<chg|dis>_<feature>`` (see module docstring); cycles whose curve is unusable are NaN.
    """
    spec = SPECS[dataset]
    keys, q_mat = grid_curves(curves, spec)
    ica = ica_features(q_mat, spec)
    dq = np.full_like(q_mat, np.nan)
    cell = keys["cell_id"].to_numpy()
    cyc = keys["cycle_idx"].to_numpy()
    for c in pd.unique(cell):
        idx = np.flatnonzero(cell == c)
        idx = idx[np.argsort(cyc[idx], kind="stable")]
        dq[idx] = _causal_dq(q_mat[idx])
    stats = delta_q_stats(dq)
    cols = feature_columns(spec.prefix)
    out = pd.DataFrame(np.hstack([ica, stats]), columns=cols)
    out.insert(0, "dataset", dataset)
    out.insert(1, "cell_id", keys["cell_id"].to_numpy())
    out.insert(2, "cycle_idx", keys["cycle_idx"].to_numpy())
    return out.sort_values(KEY).reset_index(drop=True)


# --------------------------------------------------------------------------------------
# Cache
# --------------------------------------------------------------------------------------
def cache_path(dataset: str, root: Path = PROCESSED_DIR) -> Path:
    return root / dataset / "curve_features.parquet"


def build_curve_features(dataset: str, root: Path = PROCESSED_DIR) -> pd.DataFrame:
    """Read ``curves.parquet``, compute the features and write ``curve_features.parquet``."""
    src = root / dataset / "curves.parquet"
    if not src.exists():
        raise FileNotFoundError(f"{src} missing; run `battery-rul build-data {dataset}`")
    cols = ["cell_id", "cycle_idx", "phase", "sample_idx", "voltage_v", "charge_ah"]
    curves = pd.read_parquet(src, columns=cols)
    feats = curve_features(curves, dataset)
    feats.to_parquet(cache_path(dataset, root), index=False)
    return feats


def load_curve_features(dataset: str, root: Path = PROCESSED_DIR) -> pd.DataFrame:
    p = cache_path(dataset, root)
    if not p.exists():
        raise FileNotFoundError(f"{p} missing; run `battery-rul build-features {dataset}`")
    return pd.read_parquet(p)
