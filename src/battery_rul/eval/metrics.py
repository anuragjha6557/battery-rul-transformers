"""Evaluation metrics (PROTOCOL.md §5 and §7). numpy in, python floats / small dataclasses out.

Conventions
-----------
* SOH values are *fractions* (1.0 = 100 %); %SOH metrics multiply by 100 on output.
* RUL values are in cycles. Error ``e = pred - true``; **positive = late = optimistic**.
* Interval / quantile inputs are in whatever unit the target is in; the output unit follows.
* Everything is computed in float64.
* No function ignores NaN or inf: they raise ``ValueError``. Censored cells (no EOL at the
  chosen threshold), right-censored predictions and masked horizons are the *caller's* job
  to filter or flag explicitly before calling; metrics never decide that silently. The one
  exception is :func:`horizon_errors`, whose ``mask`` is the explicit mechanism, and which
  only inspects entries where ``mask`` is True.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

import numpy as np
from numpy.typing import ArrayLike, NDArray

FloatArray = NDArray[np.float64]

#: Largest ensemble size for which CRPS uses the exact O(S^2) pairwise form.
CRPS_EXACT_MAX_SAMPLES = 200
#: Relative slack on the alpha bound so |e| == alpha * RUL is not lost to float rounding.
_ALPHA_RTOL = 1e-12


# --------------------------------------------------------------------------------------
# input validation
# --------------------------------------------------------------------------------------
def _array(name: str, x: ArrayLike, ndim: int | None = None) -> FloatArray:
    """Convert to float64, rejecting empty input, wrong rank and non-finite values."""
    a = np.asarray(x, dtype=np.float64)
    if ndim is not None and a.ndim != ndim:
        raise ValueError(f"{name} must be {ndim}-D, got shape {a.shape}")
    if a.size == 0:
        raise ValueError(f"{name} is empty")
    if not np.all(np.isfinite(a)):
        raise ValueError(f"{name} contains NaN or inf; filter or mask explicitly before scoring")
    return a


def _pair(name_a: str, a: ArrayLike, name_b: str, b: ArrayLike) -> tuple[FloatArray, FloatArray]:
    """Validate two equally-shaped 1-D arrays."""
    x = _array(name_a, a, ndim=1)
    y = _array(name_b, b, ndim=1)
    if x.shape != y.shape:
        raise ValueError(f"shape mismatch: {name_a} {x.shape} vs {name_b} {y.shape}")
    return x, y


def _quantiles(quantiles: ArrayLike) -> FloatArray:
    q = _array("quantiles", quantiles, ndim=1)
    if np.any(q <= 0.0) or np.any(q >= 1.0):
        raise ValueError("quantiles must lie strictly inside (0, 1)")
    return q


def _y_and_q(
    y: ArrayLike, q_pred: ArrayLike, quantiles: ArrayLike
) -> tuple[FloatArray, FloatArray, FloatArray]:
    yy = _array("y", y, ndim=1)
    qp = _array("q_pred", q_pred, ndim=2)
    qs = _quantiles(quantiles)
    if qp.shape != (yy.shape[0], qs.shape[0]):
        raise ValueError(
            f"q_pred shape {qp.shape} does not match (n={yy.shape[0]}, Q={qs.shape[0]})"
        )
    return yy, qp, qs


# --------------------------------------------------------------------------------------
# SOH point errors (Tasks A and B)
# --------------------------------------------------------------------------------------
def rmse_pct(y_true: ArrayLike, y_pred: ArrayLike) -> float:
    """Root-mean-square error in %SOH. Inputs are SOH fractions (1.0 = 100 %)."""
    t, p = _pair("y_true", y_true, "y_pred", y_pred)
    return float(np.sqrt(np.mean((p - t) ** 2)) * 100.0)


def mae_pct(y_true: ArrayLike, y_pred: ArrayLike) -> float:
    """Mean absolute error in %SOH. Inputs are SOH fractions (1.0 = 100 %)."""
    t, p = _pair("y_true", y_true, "y_pred", y_pred)
    return float(np.mean(np.abs(p - t)) * 100.0)


def horizon_errors(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    mask: ArrayLike,
    horizons: Sequence[int],
) -> dict[int, dict[str, float]]:
    """Per-horizon RMSE / MAE in %SOH over entries where ``mask`` is True (Task B).

    Args:
        y_true, y_pred: ``(n, H)`` SOH fractions; column ``j`` is horizon ``horizons[j]``.
        mask: ``(n, H)`` bool, True where the truth exists (horizons past the end of a
            trajectory are masked, never padded). Only masked-in entries are checked for NaN,
            so masked-out padding may be NaN.
        horizons: the ``H`` horizon values (cycles), unique.

    Returns:
        ``{h: {"rmse": ..., "mae": ..., "n": ...}}``. A horizon with no valid entries maps to
        NaN for rmse / mae and ``n = 0`` (explicit, not an error).
    """
    t = np.asarray(y_true, dtype=np.float64)
    p = np.asarray(y_pred, dtype=np.float64)
    m = np.asarray(mask)
    if t.ndim != 2:
        raise ValueError(f"y_true must be 2-D (n, H), got shape {t.shape}")
    if t.size == 0:
        raise ValueError("y_true is empty")
    if t.shape != p.shape or t.shape != m.shape:
        raise ValueError(f"shape mismatch: y_true {t.shape}, y_pred {p.shape}, mask {m.shape}")
    if m.dtype != np.bool_:
        raise ValueError("mask must be a bool array")
    hs = [int(h) for h in horizons]
    if len(hs) != t.shape[1]:
        raise ValueError(f"len(horizons)={len(hs)} but arrays have H={t.shape[1]} columns")
    if len(set(hs)) != len(hs):
        raise ValueError("horizons must be unique")
    if not (np.all(np.isfinite(t[m])) and np.all(np.isfinite(p[m]))):
        raise ValueError("y_true / y_pred contain NaN or inf at unmasked entries")

    out: dict[int, dict[str, float]] = {}
    for j, h in enumerate(hs):
        sel = m[:, j]
        n = int(sel.sum())
        if n == 0:
            out[h] = {"rmse": float("nan"), "mae": float("nan"), "n": 0.0}
            continue
        err = p[sel, j] - t[sel, j]
        out[h] = {
            "rmse": float(np.sqrt(np.mean(err**2)) * 100.0),
            "mae": float(np.mean(np.abs(err)) * 100.0),
            "n": float(n),
        }
    return out


# --------------------------------------------------------------------------------------
# RUL (Task C)
# --------------------------------------------------------------------------------------
@dataclass(frozen=True)
class RULErrors:
    """RUL error summary. ``mae`` and ``bias`` in cycles; ``rel_mae`` dimensionless."""

    mae: float  #: mean |e|, cycles
    bias: float  #: mean signed e = pred - true, cycles (positive = late / optimistic)
    rel_mae: float  #: mean(|e| / rul_true)
    n: int


def rul_errors(rul_true: ArrayLike, rul_pred: ArrayLike) -> RULErrors:
    """MAE, signed bias and relative error of RUL predictions (cycles).

    ``e = rul_pred - rul_true``; positive = late = optimistic (the dangerous direction).
    ``rul_true`` must be strictly positive (censored cells are excluded by the caller).
    """
    t, p = _pair("rul_true", rul_true, "rul_pred", rul_pred)
    if np.any(t <= 0.0):
        raise ValueError("rul_true must be > 0 (drop censored / already-failed starts first)")
    e = p - t
    return RULErrors(
        mae=float(np.mean(np.abs(e))),
        bias=float(np.mean(e)),
        rel_mae=float(np.mean(np.abs(e) / t)),
        n=int(t.size),
    )


def _within_alpha(t: FloatArray, p: FloatArray, alpha: float) -> NDArray[np.bool_]:
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must lie in (0, 1)")
    bound = alpha * t
    return np.abs(p - t) <= bound + _ALPHA_RTOL * np.abs(t)


def alpha_lambda_accuracy(rul_true: ArrayLike, rul_pred: ArrayLike, alpha: float = 0.2) -> float:
    """Fraction of predictions with ``|e| <= alpha * rul_true`` (Saxena et al. 2008).

    One call scores one fraction-of-life start lambda; pool (cell, seed) predictions for that
    lambda into the arrays. ``rul_true`` (cycles) must be > 0.
    """
    t, p = _pair("rul_true", rul_true, "rul_pred", rul_pred)
    if np.any(t <= 0.0):
        raise ValueError("rul_true must be > 0")
    return float(np.mean(_within_alpha(t, p, alpha)))


def prognostic_horizon(
    t_p: ArrayLike,
    rul_true: ArrayLike,
    rul_pred: ArrayLike,
    eol: float,
    alpha: float = 0.2,
) -> float:
    """Prognostic horizon of ONE cell, in cycles.

    Over the cell's sweep of start points ``t_p`` (cycles; any order, sorted internally),
    find the earliest ``t_p`` such that the prediction there *and at every later start point*
    satisfies ``|rul_pred - rul_true| <= alpha * rul_true``. Returns ``eol - t_p`` of that
    start, or NaN if even the last start point fails. ``rul_true`` (cycles) must be >= 0.
    """
    tp = _array("t_p", t_p, ndim=1)
    t, p = _pair("rul_true", rul_true, "rul_pred", rul_pred)
    if tp.shape != t.shape:
        raise ValueError(f"shape mismatch: t_p {tp.shape} vs rul_true {t.shape}")
    if not np.isfinite(eol):
        raise ValueError("eol must be finite")
    if np.any(t < 0.0):
        raise ValueError("rul_true must be >= 0")
    order = np.argsort(tp, kind="stable")
    tp, t, p = tp[order], t[order], p[order]
    ok = _within_alpha(t, p, alpha)
    if not ok[-1]:
        return float("nan")
    bad = np.flatnonzero(~ok)
    first = 0 if bad.size == 0 else int(bad[-1]) + 1
    return float(eol - tp[first])


# --------------------------------------------------------------------------------------
# Uncertainty (PROTOCOL §5)
# --------------------------------------------------------------------------------------
def _check_interval(lo: ArrayLike, hi: ArrayLike) -> tuple[FloatArray, FloatArray]:
    lo_a, hi_a = _pair("lo", lo, "hi", hi)
    if np.any(lo_a > hi_a):
        raise ValueError("interval has lo > hi; fix crossing (rearrange) before scoring")
    return lo_a, hi_a


def picp(y: ArrayLike, lo: ArrayLike, hi: ArrayLike) -> float:
    """Prediction-interval coverage probability: fraction of ``lo <= y <= hi`` (in [0, 1])."""
    lo_a, hi_a = _check_interval(lo, hi)
    y_a, _ = _pair("y", y, "lo", lo_a)
    return float(np.mean((y_a >= lo_a) & (y_a <= hi_a)))


def mpiw(lo: ArrayLike, hi: ArrayLike) -> float:
    """Mean prediction-interval width, in the units of the inputs."""
    lo_a, hi_a = _check_interval(lo, hi)
    return float(np.mean(hi_a - lo_a))


def pinball_loss(y: ArrayLike, q_pred: ArrayLike, quantiles: ArrayLike) -> float:
    """Mean pinball (quantile) loss over samples and quantile levels, in target units.

    ``y``: ``(n,)``; ``q_pred``: ``(n, Q)``; ``quantiles``: ``(Q,)`` strictly inside (0, 1).
    Per entry: ``max(tau * (y - q), (tau - 1) * (y - q))``.
    """
    yy, qp, qs = _y_and_q(y, q_pred, quantiles)
    d = yy[:, None] - qp
    return float(np.mean(np.maximum(qs[None, :] * d, (qs[None, :] - 1.0) * d)))


def _crps_exact_rows(y: FloatArray, x: FloatArray) -> FloatArray:
    """Per-row CRPS via the exact pairwise energy form (chunked to bound memory)."""
    n, s = x.shape
    out = np.empty(n, dtype=np.float64)
    chunk = max(1, 4_000_000 // (s * s))
    for a in range(0, n, chunk):
        xs = x[a : a + chunk]
        term1 = np.mean(np.abs(xs - y[a : a + chunk, None]), axis=1)
        pair = np.abs(xs[:, :, None] - xs[:, None, :]).mean(axis=(1, 2))
        out[a : a + chunk] = term1 - 0.5 * pair
    return out


def _crps_sorted_rows(y: FloatArray, x: FloatArray) -> FloatArray:
    """Per-row CRPS using sorted samples: sum_ij |xi - xj| = 2 sum_i (2i - S - 1) x_(i)."""
    _, s = x.shape
    xs = np.sort(x, axis=1)
    term1 = np.mean(np.abs(xs - y[:, None]), axis=1)
    w = 2.0 * np.arange(1, s + 1, dtype=np.float64) - s - 1.0
    half_pair = (xs @ w) / (s * s)  # = 0.5 * mean_ij |xi - xj|
    return term1 - half_pair


def crps_from_samples(y: ArrayLike, samples: ArrayLike) -> float:
    """Mean CRPS of an ensemble forecast, in target units (energy form, not 'fair').

    ``CRPS = E|X - y| - 0.5 E|X - X'|`` with ``X, X'`` iid draws from the empirical ensemble
    (the ``1/S^2`` convention, identical to ``properscoring.crps_ensemble``). Exact pairwise
    sum for ``S <= 200``, otherwise the equivalent sorted O(S log S) formula.

    Args:
        y: ``(n,)`` observations.
        samples: ``(n, S)`` ensemble members.
    """
    yy = _array("y", y, ndim=1)
    x = _array("samples", samples, ndim=2)
    if x.shape[0] != yy.shape[0]:
        raise ValueError(f"shape mismatch: y {yy.shape} vs samples {x.shape}")
    if x.shape[1] <= CRPS_EXACT_MAX_SAMPLES:
        rows = _crps_exact_rows(yy, x)
    else:
        rows = _crps_sorted_rows(yy, x)
    return float(np.mean(rows))


def crps_from_quantiles(y: ArrayLike, q_pred: ArrayLike, quantiles: ArrayLike) -> float:
    """Approximate mean CRPS from predicted quantiles, in target units.

    Uses ``CRPS = 2 * integral_0^1 pinball_tau dtau`` and approximates the integral by the
    plain mean over the supplied levels, i.e. ``2 * mean pinball``. This is only accurate when
    ``quantiles`` is a dense, roughly uniform grid on (0, 1) (e.g. 0.01..0.99); with the five
    protocol levels it is a coarse, biased summary and must not be compared with
    :func:`crps_from_samples`.
    """
    return 2.0 * pinball_loss(y, q_pred, quantiles)


def rearrange_quantiles(q_pred: ArrayLike) -> FloatArray:
    """Fix quantile crossing by sorting along the quantile axis (Chernozhukov et al. 2010).

    ``q_pred``: ``(n, Q)`` with columns ordered by increasing level. Returns a sorted copy.
    """
    qp = _array("q_pred", q_pred, ndim=2)
    return np.sort(qp, axis=1)


def quantile_crossing_rate(q_pred: ArrayLike) -> float:
    """Fraction of rows (samples) in which any quantile is below the preceding level's.

    ``q_pred``: ``(n, Q)`` with columns ordered by increasing level. In [0, 1].
    """
    qp = _array("q_pred", q_pred, ndim=2)
    return float(np.mean(np.any(np.diff(qp, axis=1) < 0.0, axis=1)))
