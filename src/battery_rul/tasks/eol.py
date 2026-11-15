"""Candidate end-of-life (EOL) labelling rules on a SOH trajectory.

LEAKAGE NOTE: every rule here looks at the *whole* trajectory (including cycles after the
candidate EOL, centered windows, masks derived from the full cell). That is legitimate for
computing **labels** in hindsight, and never legitimate for model **inputs**. Anything fed to a
model at prediction time must use only cycles <= the prediction point.

Conventions: ``soh`` is dimensionless (1 = reference capacity), ``cycle_idx`` is the cell's
1-based cycle count (gaps allowed); ``eol_cycle`` is a ``cycle_idx`` value, not a position.
A trajectory that never satisfies the rule is censored (``eol_cycle=None``).
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class EOLResult:
    eol_cycle: int | None
    censored: bool
    rule: str
    threshold: float


def _check(cycle_idx: np.ndarray, soh: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    cycle_idx = np.asarray(cycle_idx)
    soh = np.asarray(soh, dtype=float)
    if cycle_idx.ndim != 1 or cycle_idx.shape != soh.shape:
        raise ValueError("cycle_idx and soh must be 1-D arrays of equal length")
    if not bool(np.all(np.diff(cycle_idx) > 0)):
        raise ValueError("cycle_idx must be strictly increasing")
    return cycle_idx, soh


def _result(cycle_idx: np.ndarray, pos: int | None, rule: str, threshold: float) -> EOLResult:
    if pos is None:
        return EOLResult(None, True, rule, threshold)
    return EOLResult(int(cycle_idx[pos]), False, rule, threshold)


def eol_raw(cycle_idx: np.ndarray, soh: np.ndarray, threshold: float) -> EOLResult:
    """First cycle with ``soh < threshold`` (sensitive to single-cycle dips)."""
    cycle_idx, soh = _check(cycle_idx, soh)
    hits = np.flatnonzero(soh < threshold)
    return _result(cycle_idx, int(hits[0]) if hits.size else None, "raw", threshold)


def eol_rolling_median(
    cycle_idx: np.ndarray, soh: np.ndarray, threshold: float, window: int = 5
) -> EOLResult:
    """First cycle whose centered rolling median (``min_periods=1``) is below ``threshold``."""
    cycle_idx, soh = _check(cycle_idx, soh)
    med = pd.Series(soh).rolling(window, center=True, min_periods=1).median().to_numpy()
    hits = np.flatnonzero(med < threshold)
    return _result(cycle_idx, int(hits[0]) if hits.size else None, "rolling_median", threshold)


def eol_sustained(
    cycle_idx: np.ndarray, soh: np.ndarray, threshold: float, n: int = 5
) -> EOLResult:
    """First ``i`` with ``soh[i:i+n]`` all below ``threshold``; EOL is the run's first cycle.

    A run truncated by the end of the record (fewer than ``n`` cycles left) does not count.
    """
    cycle_idx, soh = _check(cycle_idx, soh)
    below = soh < threshold
    pos: int | None = None
    if len(soh) >= n:
        run = np.convolve(below.astype(int), np.ones(n, dtype=int), mode="valid")
        hits = np.flatnonzero(run == n)
        pos = int(hits[0]) if hits.size else None
    return _result(cycle_idx, pos, "sustained", threshold)


def eol_masked(
    cycle_idx: np.ndarray,
    soh: np.ndarray,
    threshold: float,
    mask: np.ndarray,
    base: Callable[..., EOLResult] = eol_sustained,
) -> EOLResult:
    """Drop cycles where ``mask`` is True (flagged anomalies), then apply ``base``."""
    cycle_idx, soh = _check(cycle_idx, soh)
    mask = np.asarray(mask, dtype=bool)
    if mask.shape != soh.shape:
        raise ValueError("mask must match soh")
    res = base(cycle_idx[~mask], soh[~mask], threshold)
    return EOLResult(res.eol_cycle, res.censored, f"masked_{res.rule}", threshold)


RULES: dict[str, Callable[..., EOLResult]] = {
    "raw": eol_raw,
    "rolling_median": eol_rolling_median,
    "sustained": eol_sustained,
    "masked": eol_masked,
}
