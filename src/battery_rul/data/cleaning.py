"""Outlier policy for the field study (ADR-0018).

Two kinds of outlier, two kinds of rule:

* **Label outliers** are invalid *capacity measurements*: the measured capacity of that cycle
  does not reflect the cell's health. The cycle is dropped from training targets, evaluation
  targets and conformal calibration. These rules may look at neighbouring cycles (hindsight),
  because labels are only used offline.
  - ``cv_skip`` (CALCE): the charger's CV step ended after one sample (cv_time_s < 300 s), so
    the next discharge reads ~10 % low (ADR-0017).
  - ``partial_charge``: charge throughput < 50 % of its local median (top-up/truncated charge).
  - ``isolated_glitch``: a one-cycle excursion in either direction whose two neighbours agree
    with each other. Real regeneration (a jump that persists and decays over several cycles) is
    *not* matched, by construction.
* **Input outliers** are corrupt *feature values*. They are set to missing (the models'
  forward-fill and mask channel handle them). These rules are **causal**: they read only the
  current and past cycles of the cell, so they can run on a live battery.
  - ``charge_pause``: charge_time_s > 3 x the median of the cell's past cycles (paused or
    interrupted charge; Toyota). All charge-duration-derived inputs of that cycle are masked.
  - ``robust_z``: |x - median of the past 25 cycles| > 8 x max(MAD, 2 % of |median|) per feature,
    i.e. at least a 16 % deviation. Cycles right
    after a long rest are exempt, because a regeneration shifts the signals on purpose.

Everything else is kept as a real signal: regeneration, the Toyota break-in rise (SOH up to
1.008) and the knee.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Final

import numpy as np
import pandas as pd

from battery_rul.data.quality import LONG_REST_S, SKIPPED_CV_S, flag_anomalies

GLITCH_MIN_REL: Final = 0.01  #: minimum excursion, fraction of the cell's median capacity
GLITCH_MAD_K: Final = 5.0  #: excursion > k x local median |Δcapacity|
GLITCH_AGREE: Final = 0.3  #: neighbours must agree within this fraction of the excursion
PAUSE_FACTOR: Final = 3.0
ROBUST_WINDOW: Final = 25
ROBUST_K: Final = 8.0
ROBUST_MIN_HISTORY: Final = 10
#: MAD floor as a fraction of |median|: with ROBUST_K = 8 a value must deviate >= 16 % from
#: its recent median (quantised signals such as IR otherwise have MAD ~ 0).
ROBUST_REL_FLOOR: Final = 0.02

#: Smooth physical quantities checked with the causal robust rule. Durations (CC/CV split) are
#: deliberately NOT: they switch regime as a cell ages (Toyota CV time jumps 625 -> 1260 s when
#: 3.6 V is reached earlier within the fixed charge timer), which is health information.
ROBUST_COLS: Final = (
    "ir_ohm",
    "charge_temp_max_c",
    "charge_temp_mean_c",
    "fld_r_dc",
    "fld_chg_temp_max_c",
    "fld_chg_temp_mean_c",
)
#: Physical plausibility ranges (inclusive); values outside are sensor/parse errors.
PHYSICAL_RANGES: Final = {
    "ir_ohm": (1e-4, 1.0),
    "fld_r_dc": (1e-4, 1.0),
    "charge_temp_max_c": (-20.0, 80.0),
    "charge_temp_mean_c": (-20.0, 80.0),
    "fld_chg_temp_max_c": (-20.0, 80.0),
    "fld_chg_temp_mean_c": (-20.0, 80.0),
    "fld_relax_v0": (2.0, 4.4),
    "fld_relax_v1": (2.0, 4.4),
}

#: Inputs derived from the charge duration; masked together on a paused charge.
CHARGE_DURATION_COLS: Final = ("charge_time_s", "cc_time_s", "cv_time_s")
CHARGE_DURATION_PREFIXES: Final = ("fld_win_", "fld_q_v", "fld_cv_", "fld_ica_", "fld_relax_")


@dataclass
class CleaningReport:
    label_counts: dict[str, int] = field(default_factory=dict)
    input_counts: dict[str, int] = field(default_factory=dict)
    n_rows_in: int = 0
    n_rows_out: int = 0


def isolated_glitch(capacity: np.ndarray) -> np.ndarray:
    """One-cycle capacity excursions whose neighbours agree (hindsight rule; labels only)."""
    c = np.asarray(capacity, dtype=np.float64)
    out = np.zeros(c.size, dtype=bool)
    if c.size < 3:
        return out
    prev, nxt = c[:-2], c[2:]
    dev = c[1:-1] - (prev + nxt) / 2.0
    d = np.abs(np.diff(c))
    scale = pd.Series(d).rolling(ROBUST_WINDOW, center=True, min_periods=3).median().to_numpy()
    scale = np.nan_to_num(scale, nan=np.nanmedian(d) if d.size else 0.0)
    # scale of the step into cycle k (index k-1 of diff), floored by the relative threshold
    thr = np.maximum(GLITCH_MAD_K * scale[:-1], GLITCH_MIN_REL * np.nanmedian(c))
    agree = np.abs(nxt - prev) < GLITCH_AGREE * np.abs(dev)
    out[1:-1] = (np.abs(dev) > thr) & agree
    return out


def label_outliers(cycles: pd.DataFrame) -> pd.DataFrame:
    """Boolean columns per label rule (+ ``any``), aligned with ``cycles.index``."""
    flags = flag_anomalies(cycles)
    out = pd.DataFrame(index=cycles.index)
    out["cv_skip"] = (cycles["dataset"] == "calce") & (cycles["cv_time_s"] < SKIPPED_CV_S)
    out["partial_charge"] = flags["flag_partial_charge"].to_numpy()
    glitch = pd.Series(False, index=cycles.index)
    for _, g in cycles.groupby(["dataset", "cell_id"], sort=False):
        g = g.sort_values("cycle_idx")
        glitch.loc[g.index] = isolated_glitch(g["capacity_ah"].to_numpy())
    out["isolated_glitch"] = glitch & ~out["cv_skip"]  # count each cycle under one rule
    out["any"] = out.any(axis=1)
    return out


def _past_median(s: pd.Series, window: int) -> pd.Series:
    return s.shift(1).rolling(window, min_periods=ROBUST_MIN_HISTORY).median()


def input_outliers(cycles: pd.DataFrame, cols: Sequence[str]) -> dict[str, pd.Series]:
    """Causal input masks: ``{"charge_pause": bool series, "<col>": bool series, ...}``."""
    masks: dict[str, pd.Series] = {}
    pause = pd.Series(False, index=cycles.index)
    per_col = {c: pd.Series(False, index=cycles.index) for c in cols if c in cycles}
    for _, g in cycles.groupby(["dataset", "cell_id"], sort=False):
        g = g.sort_values("cycle_idx")
        if "charge_time_s" in g:
            med = g["charge_time_s"].shift(1).expanding(min_periods=3).median()
            pause.loc[g.index] = (g["charge_time_s"] > PAUSE_FACTOR * med).fillna(False)
        after_rest = (
            g.get("rest_before_s", pd.Series(np.nan, index=g.index)) > LONG_REST_S
        ).fillna(False)
        for c in per_col:
            x = g[c].astype(float)
            med = _past_median(x, ROBUST_WINDOW)
            mad = (
                (x - med)
                .abs()
                .shift(1)
                .rolling(ROBUST_WINDOW, min_periods=ROBUST_MIN_HISTORY)
                .median()
            )
            mad = (
                mad.where(mad > ROBUST_REL_FLOOR * med.abs(), ROBUST_REL_FLOOR * med.abs()) + 1e-12
            )
            bad = ((x - med).abs() > ROBUST_K * mad) & ~after_rest
            per_col[c].loc[g.index] = bad.fillna(False)
    masks["charge_pause"] = pause
    masks.update(per_col)
    return masks


def clean_cycles(
    cycles: pd.DataFrame, input_cols: Sequence[str] = ROBUST_COLS
) -> tuple[pd.DataFrame, CleaningReport]:
    """Apply ADR-0018: drop label-outlier cycles; set input outliers to NaN (causal rules)."""
    lab = label_outliers(cycles)
    out, counts = clean_inputs(cycles, input_cols)
    rep = CleaningReport(n_rows_in=len(cycles), input_counts=counts)
    rep.label_counts = {k: int(lab[k].sum()) for k in lab.columns}
    out = out[~lab["any"].to_numpy()].reset_index(drop=True)
    rep.n_rows_out = len(out)
    return out, rep


def clean_inputs(
    cycles: pd.DataFrame, input_cols: Sequence[str] = ROBUST_COLS
) -> tuple[pd.DataFrame, dict[str, int]]:
    """The causal input rules of ADR-0018 only (no capacity needed; used when serving).

    Returns a copy with input outliers set to NaN (rows and index unchanged) and the counts.
    """
    counts: dict[str, int] = {}
    out = cycles.copy()
    for c, (lo, hi) in PHYSICAL_RANGES.items():
        if c in out:
            bad = (out[c] < lo) | (out[c] > hi)
            counts[f"range:{c}"] = int(bad.sum())
            out.loc[bad, c] = np.nan
    masks = input_outliers(out, input_cols)
    pause = masks.pop("charge_pause")
    counts["charge_pause"] = int(pause.sum())
    dur_cols = [
        c
        for c in out.columns
        if (c in CHARGE_DURATION_COLS or c.startswith(CHARGE_DURATION_PREFIXES))
        and pd.api.types.is_float_dtype(out[c])  # never flags such as fld_win_valid (bool)
    ]
    out.loc[pause, dur_cols] = np.nan
    for c, m in masks.items():
        m = m & ~pause  # already masked
        counts[c] = int(m.sum())
        out.loc[m, c] = np.nan
    return out, counts
