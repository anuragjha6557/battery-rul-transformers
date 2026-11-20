"""BMS-measurable, charge-side per-cycle "field" features (PLAN_PHASE2 section 2, Stage 0b).

None of these use a capacity measurement: no discharge capacity/curve, no charge throughput from
empty, no total/CC charge time from empty (they depend on the starting SOC). Columns (NaN where not
applicable):

``fld_relax_v0/v1/dv/s``  rest voltage (V) at start/end of a rest, dv = v1 - v0 (V), duration (s).
    NASA: the pre-charge rest is not a trace; v0 = v1 = sample-0 voltage (relaxed OCV), dv = NaN,
    s = ``rest_before_s``. A sensor spike (> :data:`V_SPIKE`) or a non-resting sample 0 -> NaN.
    CALCE: the CC->CV rest (I ~ 0 between CC and CV).
``fld_r_dc``  NASA: DC resistance (Ohm) from the start-up current pulse (sample 0 -> sample 1).
``fld_win_*``, ``fld_q_v00..15``, ``fld_ica_v/h``  CC-charge window [3.85, 4.15] V: charge (Ah)
    passed since the 3.85 V crossing, time (s) 3.85 -> 4.15 V, charge at 16 equispaced voltages,
    validity (window fully covered by the CC segment, i.e. the charge started at or below 3.85 V),
    and the largest dQ/dV peak (V, Ah/V) in 3.87-4.13 V (Savitzky-Golay, as ``curves.py``).
``fld_cv_s``  CV duration (s), defined exactly like ``cv_time_s``.
``fld_chg_temp_max_c/mean_c``  NASA only, whole charge.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Final

import numpy as np
import pandas as pd

from battery_rul.data.io import read_tables
from battery_rul.features.curves import CurveSpec, ica_features
from battery_rul.utils import PROCESSED_DIR

KEY: Final = ["dataset", "cell_id", "cycle_idx"]
V_LO: Final = 3.85  # 3.80 covered only 67 % of NASA (loaded start voltage rises with age)
V_HI: Final = 4.15
N_GRID: Final = 16
V_SPIKE: Final = 4.3  # a Li-ion cell cannot rest above this; NASA cycle-31 sample 0 reads 8.1-8.4 V
I_REST: Final = 0.02  # A, |I| below this counts as rest
I_CC_MIN: Final = 0.1  # A, charge current above this counts as the CC segment
R_RANGE: Final = (0.02, 0.30)  # Ohm, plausibility range of the pulse resistance
MIN_REST_S: Final = 20.0
CV_V_END: Final = {"nasa": 4.2 - 0.01, "calce": 4.19}
CV_MIN_IDX: Final = {"nasa": 3, "calce": 0}
_ICA = CurveSpec("charge", "fld", V_LO, V_HI, 0.005, 3.87, 4.13, 0.04, True, 1.0, True)

Q_COLS: Final = [f"fld_q_v{i:02d}" for i in range(N_GRID)]
RELAX_COLS: Final = ["fld_relax_v0", "fld_relax_v1", "fld_relax_dv", "fld_relax_s"]
WIN_COLS: Final = ["fld_win_dq_ah", "fld_win_dt_s", *Q_COLS, "fld_ica_v", "fld_ica_h"]
FIELD_COLS: Final = [
    *RELAX_COLS,
    "fld_r_dc",
    *WIN_COLS,
    "fld_win_valid",
    "fld_cv_s",
    "fld_chg_temp_max_c",
    "fld_chg_temp_mean_c",
]
_NAN: Final = float("nan")


def relaxation_features(
    dataset: str, t: np.ndarray, v: np.ndarray, i: np.ndarray, rest_before_s: float = _NAN
) -> tuple[float, float, float, float]:
    """(v0, v1, dv, s) of the field relaxation signal for one charge record (units: V, V, V, s)."""
    nan4 = (_NAN, _NAN, _NAN, _NAN)
    if len(t) < 2:
        return nan4
    if dataset == "nasa":
        v0 = float(v[0])
        if not np.isfinite(v0) or v0 > V_SPIKE or abs(i[0]) > 0.05:
            return nan4
        return v0, v0, _NAN, float(rest_before_s)
    # CALCE: first interior run of rest samples that is followed by charging again
    idx = np.flatnonzero(np.abs(i) < I_REST)
    if idx.size == 0:
        return nan4
    for r in np.split(idx, np.flatnonzero(np.diff(idx) > 1) + 1):
        a, b = int(r[0]), int(r[-1])
        if a == 0 or b >= len(t) - 1 or not (i[b + 1 :] > I_REST).any():
            continue
        if not (i[:a] > I_CC_MIN).any():
            continue
        s = float(t[b] - t[a])
        if s < MIN_REST_S:
            continue
        return float(v[a]), float(v[b]), float(v[b] - v[a]), s
    return nan4


def pulse_resistance(v: np.ndarray, i: np.ndarray) -> float:
    """DC resistance (Ohm) from sample 0 -> sample 1 of a charge record; NaN if implausible."""
    if len(v) < 2 or v[0] > V_SPIKE:
        return _NAN
    di = float(i[1] - i[0])
    if not np.isfinite(di) or abs(di) < 1.0:
        return _NAN
    r = float((v[1] - v[0]) / di)
    return r if R_RANGE[0] <= r <= R_RANGE[1] else _NAN


def _cc_segment(
    t: np.ndarray, v: np.ndarray, i: np.ndarray, v_hi: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Charging samples (I > I_CC_MIN) up to and including the first that reaches ``v_hi``."""
    ok = np.isfinite(t) & np.isfinite(v) & np.isfinite(i) & (i > I_CC_MIN) & (v < V_SPIKE)
    t, v, i = t[ok], v[ok], i[ok]
    hit = np.flatnonzero(v >= v_hi)
    if hit.size:
        n = int(hit[0]) + 1
        t, v, i = t[:n], v[:n], i[:n]
    return t, np.maximum.accumulate(v), i


def window_features(
    t: np.ndarray,
    v: np.ndarray,
    i: np.ndarray,
    v_lo: float = V_LO,
    v_hi: float = V_HI,
    n_grid: int = N_GRID,
) -> tuple[dict[str, float], bool]:
    """Fixed-voltage-window features of one charge record (t s, v V, i A, charge positive).

    Q is the trapezoid integral of I dt over the CC segment, measured from the ``v_lo`` crossing.
    Returns (features without validity, valid); all-NaN and valid=False when the CC segment does
    not span [v_lo, v_hi] (e.g. the charge started above ``v_lo``).
    """
    out = {k: _NAN for k in WIN_COLS}
    ts, vs, is_ = _cc_segment(t, v, i, v_hi)
    if len(ts) < 5 or vs[0] > v_lo or vs[-1] < v_hi:
        return out, False
    q = np.concatenate([[0.0], np.cumsum(0.5 * (is_[1:] + is_[:-1]) * np.diff(ts))]) / 3600.0
    # drop flat voltage repeats (keep the last of each) so np.interp sees a strictly rising xp
    keep = np.concatenate([vs[1:] > vs[:-1], [True]])
    vk, qk, tk = vs[keep], q[keep], ts[keep]
    grid = np.linspace(v_lo, v_hi, n_grid)
    qg = np.interp(grid, vk, qk)
    qg = np.maximum.accumulate(qg - qg[0])
    t_lo, t_hi = np.interp([v_lo, v_hi], vk, tk)
    out["fld_win_dq_ah"] = float(qg[-1])
    out["fld_win_dt_s"] = float(t_hi - t_lo)
    for name, val in zip(Q_COLS, qg, strict=False):
        out[name] = float(val)
    fine = np.interp(_ICA.grid, vk, qk)
    pv, ph, _ = ica_features((fine - fine[0])[None, :], _ICA)[0]
    out["fld_ica_v"], out["fld_ica_h"] = float(pv), float(ph)
    return out, True


def cv_duration(dataset: str, t: np.ndarray, v: np.ndarray) -> float:
    """CV duration (s), same definition as ``cv_time_s`` (end of record minus first V >= 4.19)."""
    if len(t) < 2:
        return _NAN
    lo = CV_MIN_IDX[dataset]
    reached = np.flatnonzero(v[lo:] >= CV_V_END[dataset])
    if reached.size == 0:
        return _NAN if dataset == "calce" else 0.0
    return float(t[-1] - t[lo + reached[0]])


def _row(
    dataset: str,
    t: np.ndarray,
    v: np.ndarray,
    i: np.ndarray,
    temp: np.ndarray,
    rest_before_s: float,
) -> dict[str, float | bool]:
    r0, r1, dv, rs = relaxation_features(dataset, t, v, i, rest_before_s)
    win, valid = window_features(t, v, i)
    row: dict[str, float | bool] = dict(zip(RELAX_COLS, (r0, r1, dv, rs), strict=True))
    row["fld_r_dc"] = pulse_resistance(v, i) if dataset == "nasa" else _NAN
    row.update(win)
    row["fld_win_valid"] = valid
    row["fld_cv_s"] = cv_duration(dataset, t, v)
    if dataset == "nasa" and np.isfinite(temp).any():
        row["fld_chg_temp_max_c"] = float(np.nanmax(temp))
        row["fld_chg_temp_mean_c"] = float(np.nanmean(temp))
    else:
        row["fld_chg_temp_max_c"] = row["fld_chg_temp_mean_c"] = _NAN
    return row


def build_field_features(dataset: str, processed_dir: Path = PROCESSED_DIR) -> pd.DataFrame:
    """Field features for every (cell, cycle) of ``cycles.parquet`` (NaN when no charge curve)."""
    tabs = read_tables(dataset, processed_dir, curves=True)
    cyc = tabs.cycles[[*KEY, "rest_before_s"]]
    ch = tabs.curves[tabs.curves["phase"] == "charge"].sort_values(
        ["cell_id", "cycle_idx", "sample_idx"]
    )
    rest = cyc.set_index(["cell_id", "cycle_idx"])["rest_before_s"]
    rows = []
    for (cell, k), g in ch.groupby(["cell_id", "cycle_idx"], sort=False):
        rb = rest.get((cell, k), _NAN)
        r = _row(
            dataset,
            g["t_s"].to_numpy(float),
            g["voltage_v"].to_numpy(float),
            g["current_a"].to_numpy(float),
            g["temp_c"].to_numpy(float),
            float(rb) if pd.notna(rb) else _NAN,
        )
        rows.append({"cell_id": cell, "cycle_idx": k, **r})
    feats = pd.DataFrame(rows)
    out = cyc[KEY].merge(feats, on=["cell_id", "cycle_idx"], how="left")
    out["fld_win_valid"] = out["fld_win_valid"].fillna(False).astype(bool)
    return out[[*KEY, *FIELD_COLS]].sort_values(KEY).reset_index(drop=True)


def _git_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def write_field_features(dataset: str, processed_dir: Path = PROCESSED_DIR) -> pd.DataFrame:
    """Build and write ``field_features.parquet`` / ``.json`` next to the dataset's tables."""
    df = build_field_features(dataset, processed_dir)
    out = processed_dir / dataset
    df.to_parquet(out / "field_features.parquet", index=False)
    meta = {
        "dataset": dataset,
        "window_v": [V_LO, V_HI],
        "n_grid": N_GRID,
        "grid_v": np.linspace(V_LO, V_HI, N_GRID).round(5).tolist(),
        "rules": {
            "v_spike": V_SPIKE,
            "i_rest_a": I_REST,
            "i_cc_min_a": I_CC_MIN,
            "r_range_ohm": list(R_RANGE),
            "min_rest_s": MIN_REST_S,
            "ica_peak_search_v": [_ICA.peak_lo, _ICA.peak_hi],
        },
        "n_rows": len(df),
        "coverage": {c: float(df[c].notna().mean()) for c in FIELD_COLS},
        "git_sha": _git_sha(),
    }
    (out / "field_features.json").write_text(json.dumps(meta, indent=2))
    return df


def main() -> None:
    ap = argparse.ArgumentParser(description="Compute BMS-measurable field features.")
    ap.add_argument("--dataset", default="all", choices=["nasa", "calce", "all"])
    ap.add_argument("--processed", type=Path, default=PROCESSED_DIR)
    a = ap.parse_args()
    for ds in ["nasa", "calce"] if a.dataset == "all" else [a.dataset]:
        df = write_field_features(ds, a.processed)
        print(ds, len(df), "rows; window valid", f"{df['fld_win_valid'].mean():.3f}")


if __name__ == "__main__":
    main()
