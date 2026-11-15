"""Severson et al. 2019 early-cycle features (Nature Energy 4, 383-391), from the first 100 cycles.

Inputs are the canonical ``cycles`` / ``curves`` tables of one cell (no labels). Everything reads
cycles <= ``last_cycle`` (default 100) only. Cycle numbers follow the data provider's count; the
processed Toyota tables start at cycle 2 (cycle 1 is absent), as in the paper's cycle-2 features.

Features (names as columns of the returned frame):
    dq_min, dq_var, dq_skew, dq_kurt    log10 |.| of min/variance/skewness/kurtosis of
                                        dQ(V) = Q_100(V) - Q_10(V) (discharge curve, voltage grid)
    q2                                  discharge capacity at cycle 2 (Ah)
    qmax_minus_q2                       max capacity over cycles 2..100 minus capacity at cycle 2
    fade_slope, fade_intercept          linear fit of capacity vs cycle over cycles 91..100
    charge_time_mean_2_6                mean charge time over cycles 2..6 (s)
    ir_min                              min internal resistance over cycles 2..100 (ohm)
    ir_delta                            IR(100) - IR(2) (ohm)
    temp_integral                       trapezoid integral of temperature over cycles 2..100
                                        (deg C * cycles)

Deviations from the paper, forced by the processed data: the paper integrates the within-cycle
temperature-vs-time curve; the Toyota tables only carry ``discharge_temp_max_c`` per cycle, so the
integral is over that per-cycle maximum across cycles (NaN-safe: NaN cycles are skipped). Internal
resistance is the per-cycle ``ir_ohm`` (paper: measured at 80 % SOC, 10 ms pulse).
"""

from __future__ import annotations

from typing import Final

import numpy as np
import pandas as pd
from scipy import stats

FEATURE_NAMES: Final = (
    "dq_min",
    "dq_var",
    "dq_skew",
    "dq_kurt",
    "q2",
    "qmax_minus_q2",
    "fade_slope",
    "fade_intercept",
    "charge_time_mean_2_6",
    "ir_min",
    "ir_delta",
    "temp_integral",
)
_EPS: Final = 1e-12


def _log10abs(x: float) -> float:
    return float(np.log10(max(abs(x), _EPS)))


def delta_q_features(q_late: np.ndarray, q_early: np.ndarray) -> dict[str, float]:
    """log10|min|, |var|, |skew|, |kurtosis| of dQ = q_late - q_early on a shared voltage grid.

    Kurtosis is the Pearson (non-excess) kurtosis, as in the paper's code (``scipy.stats.kurtosis``
    with ``fisher=False``). NaN grid points are ignored.
    """
    dq = np.asarray(q_late, dtype=np.float64) - np.asarray(q_early, dtype=np.float64)
    dq = dq[np.isfinite(dq)]
    if dq.size < 4:
        return dict.fromkeys(("dq_min", "dq_var", "dq_skew", "dq_kurt"), np.nan)
    return {
        "dq_min": _log10abs(float(dq.min())),
        "dq_var": _log10abs(float(dq.var(ddof=1))),
        "dq_skew": _log10abs(float(stats.skew(dq))),
        "dq_kurt": _log10abs(float(stats.kurtosis(dq, fisher=False))),
    }


def _curve(curves: pd.DataFrame, cycle: int) -> np.ndarray | None:
    g = curves[(curves["cycle_idx"] == cycle) & (curves["phase"] == "discharge")]
    if g.empty:
        return None
    return g.sort_values("sample_idx")["charge_ah"].to_numpy(dtype=np.float64)


def severson_features(
    cycles: pd.DataFrame,
    curves: pd.DataFrame,
    *,
    early: int = 10,
    last_cycle: int = 100,
) -> dict[str, float]:
    """Severson feature dict for ONE cell (``cycles``/``curves`` already filtered to the cell).

    Missing inputs yield NaN for the affected features rather than raising.
    """
    cyc = cycles[cycles["cycle_idx"] <= last_cycle].sort_values("cycle_idx")
    out: dict[str, float] = dict.fromkeys(FEATURE_NAMES, np.nan)

    q_late, q_early = _curve(curves, last_cycle), _curve(curves, early)
    if q_late is not None and q_early is not None and len(q_late) == len(q_early):
        out.update(delta_q_features(q_late, q_early))

    cap = cyc.set_index("cycle_idx")["capacity_ah"]
    if 2 in cap.index:
        out["q2"] = float(cap.loc[2])
        out["qmax_minus_q2"] = float(cap.max() - out["q2"])
    tail = cap[(cap.index >= last_cycle - 9) & (cap.index <= last_cycle)]
    if len(tail) >= 2:
        slope, intercept = np.polyfit(tail.index.to_numpy(dtype=np.float64), tail.to_numpy(), 1)
        out["fade_slope"], out["fade_intercept"] = float(slope), float(intercept)

    ct = cyc[(cyc["cycle_idx"] >= 2) & (cyc["cycle_idx"] <= 6)]["charge_time_s"].dropna()
    if len(ct):
        out["charge_time_mean_2_6"] = float(ct.mean())

    ir = cyc.set_index("cycle_idx")["ir_ohm"].dropna()
    ir = ir[ir.index >= 2]
    if len(ir):
        out["ir_min"] = float(ir.min())
        if 2 in ir.index and last_cycle in ir.index:
            out["ir_delta"] = float(ir.loc[last_cycle] - ir.loc[2])

    temp = cyc[cyc["cycle_idx"] >= 2][["cycle_idx", "discharge_temp_max_c"]].dropna()
    if len(temp) >= 2:
        out["temp_integral"] = float(
            np.trapezoid(temp["discharge_temp_max_c"], temp["cycle_idx"].astype(float))
        )
    return out


def severson_feature_table(cycles: pd.DataFrame, curves: pd.DataFrame, **kw: int) -> pd.DataFrame:
    """One row per cell (index ``cell_id``) with all Severson features."""
    rows = {}
    curve_groups = {k: g for k, g in curves.groupby("cell_id", sort=False)}
    for cell, g in cycles.groupby("cell_id", sort=False):
        rows[str(cell)] = severson_features(g, curve_groups.get(cell, curves.iloc[:0]), **kw)
    return pd.DataFrame.from_dict(rows, orient="index", columns=list(FEATURE_NAMES)).rename_axis(
        "cell_id"
    )
