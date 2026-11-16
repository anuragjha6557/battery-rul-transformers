"""Conformalised quantile regression (CQR) with CV+-style pooled calibration.

References: Romano, Patterson & Candes 2019 (CQR); Barber et al. 2021 (CV+).
PROTOCOL.md §3 (cross-fitting), §4 rule 7 (calibration disjoint from test), §5 (UQ).

What is, and is not, guaranteed
-------------------------------
Exact CV+ (Barber et al. 2021) builds the test interval from the *leave-fold-out* predictors:
``{mu_{-k(i)}(x) +/- R_i}`` over calibration points ``i``, each residual ``R_i`` computed with the
sub-model ``k(i)`` that did not see point ``i``, and takes quantiles of the resulting set; its
worst-case guarantee is coverage >= 1 - 2*alpha (>= 1 - alpha only for stable algorithms).

This module implements the **pooled-score approximation** used by the benchmark runner:

* The runner's test prediction is the *mean* of the K sub-model predictions (point and quantiles
  per level), and the conformity scores are computed from each sub-model's predictions on its own
  held-out cell. One scalar correction per group (horizon) is added to / subtracted from the
  averaged interval. This is NOT the CV+ jackknife construction, so the CV+ 1 - 2*alpha bound
  does not formally transfer. In particular the scores come from K different predictors while the
  test interval comes from their average.
* What does hold is **split-conformal validity conditional on the pooled scores**: if the pooled
  scores and the test score are exchangeable, then P(y in [lo - q, hi + q]) >= 1 - alpha
  (finite-sample, distribution-free; the +1 in the quantile level is the finite-sample term).
* Exchangeability is only approximate here. Samples within a cell are strongly autocorrelated
  (many origins per cell) and a test cell is not exchangeable with the inner cells (different
  cell, possibly different degradation regime), so the *effective* calibration size is the
  number of inner cells (2-5), not the number of rows. Empirical PICP on held-out cells is the
  evidence, not the theorem.

A negative correction is allowed: if the raw quantile interval over-covers on the calibration
residuals, CQR shrinks it (``E = max(lo - y, y - hi)`` is negative when y lies strictly inside).
"""

from __future__ import annotations

import logging
import math
from collections.abc import Sequence

import numpy as np
import pandas as pd

log = logging.getLogger("battery_rul.uq")

#: Columns required in the long frames handled below.
LONG_COLS = ("cell_id", "horizon", "y", "mask", "point", "lo", "hi")


def cqr_correction(y: np.ndarray, q_lo: np.ndarray, q_hi: np.ndarray, alpha: float) -> float:
    """Finite-sample CQR correction (Romano et al. 2019, eq. 6).

    Conformity score ``E_i = max(q_lo_i - y_i, y_i - q_hi_i)``; returns the
    ``ceil((n + 1) * (1 - alpha))``-th smallest score (i.e. the empirical quantile at level
    ``ceil((n+1)(1-alpha))/n``). Units are those of ``y``. May be negative.

    Returns ``+inf`` when ``n`` is too small for the requested level
    (``ceil((n+1)(1-alpha)) > n``, e.g. n < 9 at alpha = 0.1): no finite correction is valid, so
    the interval is infinitely wide rather than silently under-covering.
    """
    if not 0.0 < alpha < 1.0:
        raise ValueError(f"alpha must be in (0, 1), got {alpha}")
    y_a, lo, hi = (np.asarray(a, dtype=np.float64) for a in (y, q_lo, q_hi))
    if not (y_a.shape == lo.shape == hi.shape and y_a.ndim == 1):
        raise ValueError("y, q_lo, q_hi must be 1-D arrays of equal length")
    n = len(y_a)
    # round() guards (n+1)*(1-alpha) landing a hair above an integer in floating point
    k = math.ceil(round((n + 1) * (1.0 - alpha), 9))
    if n == 0 or k > n:
        return float("inf")
    scores = np.maximum(lo - y_a, y_a - hi)
    return float(np.sort(scores)[k - 1])


def _prep(frame: pd.DataFrame, name: str) -> pd.DataFrame:
    missing = set(LONG_COLS) - set(frame.columns)
    if missing:
        raise ValueError(f"{name} frame is missing columns {sorted(missing)}")
    out = frame.copy()
    lo = out["lo"].to_numpy(dtype=np.float64)
    hi = out["hi"].to_numpy(dtype=np.float64)
    out["lo"], out["hi"] = np.fmin(lo, hi), np.fmax(lo, hi)  # rearrangement of crossed pairs
    return out


def calibrate_cv_plus(
    inner: pd.DataFrame,
    test: pd.DataFrame,
    alpha: float = 0.1,
    by: Sequence[str] = ("horizon",),
) -> pd.DataFrame:
    """Calibrate test intervals with CQR on the pooled inner-val residuals (see module docs).

    Both frames are *long*: one row per (sample, horizon) with columns ``cell_id, horizon, y,
    mask, point, lo, hi`` (``lo``/``hi`` NaN for point-only models); target units are arbitrary
    but must agree. Rows with ``mask`` False or non-finite ``y``/``point`` are not used for
    calibration. ``inner`` holds every sub-model's predictions on its own held-out cell(s).

    Probabilistic models: CQR around ``[lo, hi]`` (correction may be negative).
    Point-only models (``lo``/``hi`` all NaN in both frames): split conformal on absolute
    residuals, interval ``point +/- q`` (symmetric, ``q >= 0``; ``+inf`` for tiny n).

    Returns a copy of ``test`` with ``lo_cal``, ``hi_cal`` (``lo_cal <= hi_cal``; if a negative
    correction would cross them they collapse to their midpoint), ``correction`` and ``n_cal``.

    Raises:
        ValueError: if any ``cell_id`` of ``test`` appears in ``inner`` (PROTOCOL §4 rule 7), a
            required column is missing, or exactly one of the frames is point-only.
    """
    if not 0.0 < alpha < 1.0:
        raise ValueError(f"alpha must be in (0, 1), got {alpha}")
    leak = set(test["cell_id"].astype(str)) & set(inner["cell_id"].astype(str))
    if leak:
        raise ValueError(f"rule 7 violated: calibration data contains test cells {sorted(leak)}")
    inner, test = _prep(inner, "inner"), _prep(test, "test")
    by = list(by)
    for b in by:
        if b not in inner.columns or b not in test.columns:
            raise ValueError(f"grouping column {b!r} missing")
    inner_pt = bool(inner["lo"].isna().all())
    test_pt = bool(test["lo"].isna().all())
    if inner_pt != test_pt:
        raise ValueError("inner and test must both be probabilistic or both point-only")
    if inner_pt:
        inner["lo"] = inner["hi"] = inner["point"]
        test["lo"] = test["hi"] = test["point"]

    ok = inner["mask"].astype(bool) & np.isfinite(inner["y"]) & np.isfinite(inner["point"])
    ok &= np.isfinite(inner["lo"]) & np.isfinite(inner["hi"])
    cal = inner[ok]
    corr: dict[tuple, tuple[float, int]] = {}
    for key, g in cal.groupby(by, sort=False):
        k = key if isinstance(key, tuple) else (key,)
        corr[k] = (
            cqr_correction(g["y"].to_numpy(), g["lo"].to_numpy(), g["hi"].to_numpy(), alpha),
            len(g),
        )

    keys = list(zip(*(test[b] for b in by), strict=True))
    qhat = np.empty(len(test))
    ncal = np.zeros(len(test), dtype=int)
    for i, k in enumerate(keys):
        q, n = corr.get(tuple(k), (float("inf"), 0))
        qhat[i], ncal[i] = q, n
    if np.isinf(qhat).any():
        log.warning(
            "some groups have too few calibration rows for alpha=%s: infinite interval", alpha
        )

    lo_c = test["lo"].to_numpy() - qhat
    hi_c = test["hi"].to_numpy() + qhat
    cross = lo_c > hi_c
    with np.errstate(invalid="ignore"):  # inf - inf only where the interval is infinite anyway
        mid = 0.5 * (lo_c + hi_c)
    lo_c, hi_c = np.where(cross, mid, lo_c), np.where(cross, mid, hi_c)
    out = test.copy()
    out["lo_cal"], out["hi_cal"] = lo_c, hi_c
    out["correction"], out["n_cal"] = qhat, ncal
    return out
