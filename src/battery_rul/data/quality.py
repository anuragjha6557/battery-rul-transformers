"""Derived anomaly flags for the per-cycle table.

The faithful-parse tables written by the loaders are never modified; everything here is
*derived* and recomputable. Flags are diagnostics for (a) masking cycles when building EOL
labels in hindsight (``battery_rul.tasks.eol``) and (b) explaining odd SOH values. Flags that
need a cell-level reference (median, rolling median) use the whole trajectory, so they must
never be used as *model inputs* at prediction time; a model that needs "was the last charge
partial?" should recompute it causally from the cycle's own features.

Thresholds below were chosen by inspecting NASA (B0005/06/07/18) and CALCE (CS2_35..38):

- ``skipped_cv``: CALCE cv_time_s has a clean gap, 26 to 31 cycles per cell lie below 80 s and
  the next-smallest value is > 1300 s, so 300 s sits safely in the empty region. NASA: none.
- ``long_rest``: rest_before_s is bimodal in CALCE (215 s vs >= 1e4 s) and NASA (~2e3 s or
  ~1e2 s vs >= 1e4 s); 6 h separates ordinary inter-cycle idle from session/weekend breaks.
- ``partial_charge``: the spec's "0.5 x the cell median" flagged 52 to 150 CALCE cycles per cell
  because charge throughput legitimately tracks capacity and CALCE cells were cycled to
  ~15 % SOH. A *local* (centered 21-cycle rolling median) reference flags only genuine
  truncated charges (3 to 6 per CALCE cell; NASA cycle 1 top-up and cycle 31).
- ``capacity_jump``: the spec's "|d capacity| > 4 x cell-median |d|" flagged 17 % of CALCE
  cycles because |d| is heteroscedastic (noise grows with age). The reference is therefore a
  centered 25-cycle rolling median of |d| with factor 6 (informational only).
- ``charge_pause``: charge_time_s > 3 x the cell's median. Toyota has 45 cycles above 4000 s
  (median ~1730 s) from paused or interrupted charges; at 1.5x, 2x, 3x and 4x NASA and CALCE
  have 0 hits (their charge time is protocol-fixed or shrinks with age) and Toyota has 45, 45,
  45, 44, so the data are bimodal and 3 sits in an empty region. Informational and an
  input-cleaning flag (the charge-time feature is corrupt on those cycles); not an EOL mask.
  It uses the whole-cell median (a trajectory-level reference, not a centred window).

Causality (ADR-0005 section 6): ``NON_CAUSAL_FLAGS`` lists the flags computed with a *centred*
rolling window, which looks at future cycles. They must not be model inputs as-is.
"""

from __future__ import annotations

from typing import Final

import numpy as np
import pandas as pd

KEY_COLS: Final = ("dataset", "cell_id", "cycle_idx")

#: CV step shorter than this is an Arbin artifact (CV ends after one sample).
SKIPPED_CV_S: Final = 300.0
#: Rest longer than this (6 h) is a session break: the capacity-regeneration driver.
LONG_REST_S: Final = 6 * 3600.0
#: Charge throughput below this fraction of its local rolling median is a partial charge.
PARTIAL_CHARGE_FRAC: Final = 0.5
PARTIAL_CHARGE_WINDOW: Final = 21
#: |capacity change| above this multiple of the local rolling-median |change| is a jump.
JUMP_FACTOR: Final = 6.0
JUMP_WINDOW: Final = 25
#: Floor on the local scale, as a fraction of the cell's global median |change|.
JUMP_SCALE_FLOOR: Final = 0.25

#: charge_time_s above this multiple of the cell's median is a paused/interrupted charge.
CHARGE_PAUSE_FACTOR: Final = 3.0

FLAG_COLS: Final = (
    "flag_no_paired_charge",
    "flag_partial_charge",
    "flag_skipped_cv",
    "flag_long_rest",
    "flag_capacity_jump",
    "flag_charge_pause",
)

#: Flags that use a centred rolling window (future cycles): never model inputs as-is.
# Centred windows (partial_charge, capacity_jump) or a whole-cell median (charge_pause) read
# future cycles: fine for labels and reports, never as model inputs as-is.
NON_CAUSAL_FLAGS: Final = ("flag_partial_charge", "flag_capacity_jump", "flag_charge_pause")


def _flags_one_cell(g: pd.DataFrame) -> pd.DataFrame:
    """Flags for a single cell, ``g`` sorted by cycle_idx."""
    out = pd.DataFrame(index=g.index)
    out["flag_no_paired_charge"] = g["charge_time_s"].isna()

    thr = (
        g["charge_throughput_ah"]
        .rolling(PARTIAL_CHARGE_WINDOW, center=True, min_periods=3)
        .median()
    )
    out["flag_partial_charge"] = (g["charge_throughput_ah"] < PARTIAL_CHARGE_FRAC * thr).fillna(
        False
    )

    out["flag_skipped_cv"] = (g["cv_time_s"] < SKIPPED_CV_S).fillna(False)
    out["flag_long_rest"] = (g["rest_before_s"] > LONG_REST_S).fillna(False)

    d = g["capacity_ah"].diff().abs()
    scale = d.rolling(JUMP_WINDOW, center=True, min_periods=3).median()
    scale = scale.clip(lower=JUMP_SCALE_FLOOR * d.median())
    out["flag_capacity_jump"] = (d > JUMP_FACTOR * scale).fillna(False)
    med = g["charge_time_s"].median()
    out["flag_charge_pause"] = (g["charge_time_s"] > CHARGE_PAUSE_FACTOR * med).fillna(False)
    return out.astype(bool)


def flag_anomalies(cycles: pd.DataFrame) -> pd.DataFrame:
    """Return key columns + boolean ``flag_*`` columns + ``flag_reasons`` (';'-joined, '' if clean).

    Works on one or many cells (grouped by dataset and cell_id). The row order and index of
    ``cycles`` are preserved. NaN inputs never trigger a flag except ``no_paired_charge``.
    """
    parts = []
    for _, g in cycles.groupby(["dataset", "cell_id"], sort=False):
        parts.append(_flags_one_cell(g.sort_values("cycle_idx")))
    flags = pd.concat(parts).reindex(cycles.index) if parts else pd.DataFrame(index=cycles.index)
    for col in FLAG_COLS:
        if col not in flags:
            flags[col] = False
    flags = flags[list(FLAG_COLS)].astype(bool)

    names = np.array([c.removeprefix("flag_") for c in FLAG_COLS])
    values = flags.to_numpy()
    reasons = [";".join(names[row]) for row in values]
    out = cycles[list(KEY_COLS)].copy()
    out = pd.concat([out, flags], axis=1)
    out["flag_reasons"] = reasons
    return out
