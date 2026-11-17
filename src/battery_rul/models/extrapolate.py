"""Level-1/2 "local" baselines: fit each sample's own SOH history and extrapolate (PLAN §6.4).

No global training: ``fit`` is a no-op. For every sample the valid entries of channel 0
(SOH, fraction of nominal) are fit against the *position index* ``t = 0..n-1`` within the
valid history (never the absolute ``cycle_idx``, leakage rule 4) and extrapolated.

* :class:`PrevSOH` - Task A analogue of persistence.
* :class:`ParamFit` - linear / double-exponential (He et al. 2011) / power-law fit; Tasks B, C.
* :class:`GPRExtrap` - per-sample Gaussian process (Richardson et al. 2017); Tasks B, C,
  probabilistic.

These models need long histories to be meaningful; run them with a large lookback (config
default ``lookback = 512``; the runner reads that per-model param). Samples with fewer than
``MIN_POINTS`` valid points fall back to persistence (forecast) or to a right-censored RUL
prediction (``max_horizon``); the count is exposed as ``n_short_`` and the fallback to
persistence/censoring is logged.

RUL convention (PROTOCOL §2, Task C): the prediction is the first step ``s >= 1`` ahead of the
last observed cycle whose predicted SOH is below ``meta["theta"]``. If the extrapolation never
crosses within ``max_horizon`` steps the prediction is ``max_horizon`` and the entry of
``last_censored_`` is True (scored as ``pred = H_max``, never dropped).
"""

from __future__ import annotations

import logging
import warnings
from typing import ClassVar, Literal

import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import norm

from battery_rul.models.base import (
    DEFAULT_QUANTILES,
    FitInfo,
    Prediction,
    SampleSet,
    TaskName,
)
from battery_rul.models.persistence import SOH_CHANNEL, _last_valid

log = logging.getLogger(__name__)

MIN_POINTS = 3
MAX_SAMPLES_WARNING = 5_000
Kind = Literal["linear", "exp2", "power"]


MIN_HORIZON = 50


def _horizon_from_labels(train: SampleSet, default: int) -> int:
    """H_max = 2 x the longest training RUL (floor 50); ``default`` if no finite labels.

    Uses only training-cell labels (``meta["eol_cycle"] - meta["origin_cycle"]``).
    """
    meta = train.meta
    if "eol_cycle" not in meta.columns or "origin_cycle" not in meta.columns:
        return default
    rul = (meta["eol_cycle"] - meta["origin_cycle"]).to_numpy(dtype=np.float64)
    rul = rul[np.isfinite(rul)]
    if rul.size == 0:
        return default
    return max(MIN_HORIZON, int(np.ceil(2 * rul.max())))


def _warn_many(n: int, name: str) -> None:
    if n > MAX_SAMPLES_WARNING:
        log.warning(
            "%s is a per-sample (local) model and was asked for %d samples (> %d); "
            "this will be slow. Use start-point origins.",
            name,
            n,
            MAX_SAMPLES_WARNING,
        )


def _history(samples: SampleSet, i: int) -> np.ndarray:
    """Valid SOH entries (float64, oldest first) of sample ``i``."""
    return samples.x_hist[i, :, SOH_CHANNEL][samples.hist_mask[i]].astype(np.float64)


def _thetas(samples: SampleSet) -> np.ndarray:
    if "theta" not in samples.meta.columns:
        raise ValueError("RUL extrapolation needs meta['theta']")
    return samples.meta["theta"].to_numpy(dtype=np.float64)


def _first_crossing(traj: np.ndarray, theta: float) -> int | None:
    """1-based step of the first entry of ``traj`` (steps 1..K) below ``theta``, else None."""
    below = traj < theta
    if not below.any():
        return None
    return int(np.argmax(below)) + 1


class PrevSOH:
    """Task A: SOH_k = last observed SOH (= SOH_{k-1})."""

    name: ClassVar[str] = "prev_soh"
    supported_tasks: ClassVar[frozenset[TaskName]] = frozenset({"soh"})
    probabilistic: ClassVar[bool] = False
    cross_fit: ClassVar[bool] = False
    tunable: ClassVar[bool] = False

    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        return FitInfo(n_train=len(train), n_val=len(val) if val is not None else 0)

    def predict(self, samples: SampleSet) -> Prediction:
        last = _last_valid(samples.x_hist[:, :, SOH_CHANNEL], samples.hist_mask)
        return Prediction(point=last[:, None].astype(np.float64))


# --- parametric curves; time is rescaled to u = t / scale for conditioning -----------------


def _exp2(u: np.ndarray, a: float, b: float, c: float, d: float) -> np.ndarray:
    return a * np.exp(np.clip(b * u, -50, 50)) + c * np.exp(np.clip(d * u, -50, 50))


def _power(u: np.ndarray, a: float, b: float, p: float) -> np.ndarray:
    return a - b * np.power(np.maximum(u, 0.0), p)


#: Physical SOH range for forecast outputs of the local extrapolators.
SOH_MIN, SOH_MAX = 0.0, 1.2


class ParamFit:
    """Per-sample parametric fade curve, extrapolated for Task B (forecast) and C (rul).

    Args:
        kind: ``linear`` (a + b t), ``exp2`` (a e^{bt} + c e^{dt}, He et al. 2011) or
            ``power`` (a - b t^c, c in [0.5, 3]).
        fit_window: if set, only the most recent ``fit_window`` valid points are fit
            (``t`` still counts positions from the start of the valid history).
        max_horizon: fallback RUL extrapolation limit (cycles). ``fit`` replaces it by
            ``max_horizon_`` = 2 x the longest training RUL (floor 50, PROTOCOL §2 H_max) when
            the training samples carry finite ``eol_cycle`` labels. Censored predictions equal
            ``max_horizon_``.

    Attributes after ``predict``: ``last_censored_`` (n,) bool (RUL only), ``n_fallback_``
    (curve fit failed -> linear), ``n_short_`` (< MIN_POINTS valid points).
    """

    name: ClassVar[str] = "param_fit"
    supported_tasks: ClassVar[frozenset[TaskName]] = frozenset({"forecast", "rul"})
    probabilistic: ClassVar[bool] = False
    cross_fit: ClassVar[bool] = False
    tunable: ClassVar[bool] = False

    def __init__(
        self, kind: Kind = "linear", fit_window: int | None = None, max_horizon: int = 3000
    ) -> None:
        if kind not in ("linear", "exp2", "power"):
            raise ValueError(f"unknown kind {kind!r}")
        if fit_window is not None and fit_window < MIN_POINTS:
            raise ValueError("fit_window must be >= 3")
        if max_horizon < 1:
            raise ValueError("max_horizon must be >= 1")
        self.kind: Kind = kind
        self.fit_window = fit_window
        self.max_horizon = max_horizon
        self.max_horizon_ = max_horizon
        self.last_censored_: np.ndarray = np.zeros(0, dtype=bool)
        self.n_fallback_ = 0
        self.n_short_ = 0

    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        """No parameters are learned; only H_max (``max_horizon_``) is set from training labels."""
        self.max_horizon_ = _horizon_from_labels(train, self.max_horizon)
        return FitInfo(
            n_train=len(train),
            n_val=len(val) if val is not None else 0,
            extra={"kind": self.kind, "max_horizon": self.max_horizon_},
        )

    # -- one-sample curve fitting -----------------------------------------------------------
    def _fit_one(self, y: np.ndarray) -> tuple[object, bool]:
        """Return (curve, fell_back): ``curve(t)`` evaluates SOH at position index ``t``."""
        n = len(y)
        lo = max(0, n - self.fit_window) if self.fit_window else 0
        t = np.arange(lo, n, dtype=np.float64)
        yy = y[lo:]
        coef = np.polyfit(t, yy, 1)

        def linear(tq: np.ndarray) -> np.ndarray:
            return coef[1] + coef[0] * tq

        if self.kind == "linear":
            return linear, False
        scale = float(max(n - 1, 1))
        u = t / scale
        y0, y1 = float(yy[0]), float(yy[-1])
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                if self.kind == "exp2":
                    p0 = [0.05 * y1, 1.0, y1, -0.3 * max(y0 - y1, 1e-3) / max(y1, 1e-3)]
                    popt, _ = curve_fit(
                        _exp2,
                        u,
                        yy,
                        p0=p0,
                        bounds=([-5, -30, -5, -30], [5, 30, 5, 30]),
                        maxfev=2000,
                    )
                    fn = lambda tq: _exp2(tq / scale, *popt)  # noqa: E731
                else:
                    p0 = [y0 + 1e-3, max(y0 - y1, 1e-3), 1.0]
                    popt, _ = curve_fit(
                        _power,
                        u,
                        yy,
                        p0=p0,
                        bounds=([0, 0, 0.5], [5, 50, 3.0]),
                        maxfev=2000,
                    )
                    fn = lambda tq: _power(tq / scale, *popt)  # noqa: E731
            if not np.all(np.isfinite(fn(np.array([0.0, float(n), 2.0 * n])))):
                raise RuntimeError("non-finite fit")
            return fn, False
        except (RuntimeError, ValueError):
            return linear, True

    def predict(self, samples: SampleSet) -> Prediction:
        n = len(samples)
        _warn_many(n, f"ParamFit[{self.kind}]")
        self.n_fallback_ = 0
        self.n_short_ = 0
        is_rul = samples.task == "rul"
        h = np.asarray(samples.horizons, dtype=np.float64)
        point = np.empty((n, len(h)))
        self.last_censored_ = np.zeros(n, dtype=bool)
        thetas = _thetas(samples) if is_rul else None
        steps = np.arange(1, self.max_horizon_ + 1, dtype=np.float64)
        for i in range(n):
            y = _history(samples, i)
            if len(y) < MIN_POINTS:
                self.n_short_ += 1
                if is_rul:
                    point[i] = self.max_horizon_
                    self.last_censored_[i] = True
                else:
                    point[i] = y[-1] if len(y) else np.nan
                continue
            curve, fell_back = self._fit_one(y)
            self.n_fallback_ += int(fell_back)
            t_last = float(len(y) - 1)
            if thetas is None:
                # Clip to the physical SOH range: an exp2 fit with a positive growth term can
                # extrapolate to astronomically large values (seen on NASA: RMSE ~1e8).
                point[i] = np.clip(curve(t_last + h), SOH_MIN, SOH_MAX)  # type: ignore[operator]
            else:
                step = _first_crossing(curve(t_last + steps), float(thetas[i]))  # type: ignore[operator]
                if step is None:
                    point[i] = self.max_horizon_
                    self.last_censored_[i] = True
                else:
                    point[i] = step
        if self.n_short_:
            log.warning(
                "ParamFit[%s]: %d samples with < %d valid points -> persistence/censored",
                self.kind,
                self.n_short_,
                MIN_POINTS,
            )
        return Prediction(point=point)


class GPRExtrap:
    """Per-sample Gaussian-process regression on (t, SOH) (Richardson et al. 2017).

    Kernel ``C*DotProduct + C*Matern(nu=1.5) + White``, ``normalize_y=True``,
    ``n_restarts_optimizer=2``. Cost is O(m^3) in the number of fit points, so only the most
    recent ``fit_window`` valid points are used (default 200; ~0.1 s/sample).

    Forecast: Gaussian quantiles of the posterior at ``t_last + h`` (point = mean).
    RUL: ``n_paths`` joint posterior trajectories on a ``grid_step``-cycle grid up to
    ``max_horizon``; each path's first crossing of theta is linearly interpolated between grid
    points; paths that never cross count as ``max_horizon`` (censored). Quantiles are the
    quantiles of those times; the point is their median
    (``last_censored_`` flags the point being censored, i.e. >= half the paths never cross).
    """

    name: ClassVar[str] = "gpr"
    supported_tasks: ClassVar[frozenset[TaskName]] = frozenset({"forecast", "rul"})
    probabilistic: ClassVar[bool] = True
    cross_fit: ClassVar[bool] = False
    tunable: ClassVar[bool] = False

    def __init__(
        self,
        fit_window: int | None = 200,
        max_horizon: int = 3000,
        n_paths: int = 200,
        grid_step: int = 10,
        seed: int = 0,
        quantile_levels: tuple[float, ...] = DEFAULT_QUANTILES,
    ) -> None:
        if fit_window is not None and fit_window < MIN_POINTS:
            raise ValueError("fit_window must be >= 3")
        self.fit_window = fit_window
        self.max_horizon = max_horizon
        self.max_horizon_ = max_horizon
        self.n_paths = n_paths
        self.grid_step = grid_step
        self.seed = seed
        self.quantile_levels = quantile_levels
        self.last_censored_: np.ndarray = np.zeros(0, dtype=bool)
        self.n_short_ = 0
        self.n_fallback_ = 0

    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        """Only H_max (``max_horizon_``, 2 x longest training RUL, floor 50) is set from labels;
        the constructor ``max_horizon`` is the fallback when no finite labels are present."""
        self.max_horizon_ = _horizon_from_labels(train, self.max_horizon)
        return FitInfo(
            n_train=len(train),
            n_val=len(val) if val is not None else 0,
            extra={"max_horizon": self.max_horizon_},
        )

    def _gp(self, y: np.ndarray, i: int):
        from sklearn.gaussian_process import GaussianProcessRegressor
        from sklearn.gaussian_process.kernels import (
            ConstantKernel,
            DotProduct,
            Matern,
            WhiteKernel,
        )

        n = len(y)
        lo = max(0, n - self.fit_window) if self.fit_window else 0
        scale = float(max(n - 1, 1))
        u = (np.arange(lo, n, dtype=np.float64) / scale)[:, None]
        kernel = (
            ConstantKernel(1.0) * DotProduct(1.0)
            + ConstantKernel(1.0)
            * Matern(length_scale=0.5, length_scale_bounds=(1e-2, 1e2), nu=1.5)
            + WhiteKernel(1e-3, (1e-8, 1e0))
        )
        gp = GaussianProcessRegressor(
            kernel=kernel,
            normalize_y=True,
            n_restarts_optimizer=2,
            random_state=self.seed + i,
        )
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            gp.fit(u, y[lo:])
        return gp, scale

    def predict(self, samples: SampleSet) -> Prediction:
        n = len(samples)
        _warn_many(n, "GPRExtrap")
        q = np.asarray(self.quantile_levels)
        is_rul = samples.task == "rul"
        h = np.asarray(samples.horizons, dtype=np.float64)
        H = len(h)
        point = np.empty((n, H))
        quant = np.empty((n, H, len(q)))
        self.last_censored_ = np.zeros(n, dtype=bool)
        self.n_short_ = 0
        self.n_fallback_ = 0
        thetas = _thetas(samples) if is_rul else None
        grid = np.arange(self.grid_step, self.max_horizon_ + self.grid_step, self.grid_step)
        grid = grid.astype(np.float64)
        z = norm.ppf(q)
        for i in range(n):
            y = _history(samples, i)
            if len(y) < MIN_POINTS:
                self.n_short_ += 1
                if is_rul:
                    point[i] = self.max_horizon_
                    quant[i] = self.max_horizon_
                    self.last_censored_[i] = True
                else:
                    last = y[-1] if len(y) else np.nan
                    point[i] = last
                    quant[i] = last
                continue
            try:
                gp, scale = self._gp(y, i)
            except Exception:
                self.n_fallback_ += 1
                gp, scale = None, 1.0
            t_last = float(len(y) - 1)
            if gp is None:
                if is_rul:
                    point[i] = self.max_horizon_
                    quant[i] = self.max_horizon_
                    self.last_censored_[i] = True
                else:
                    point[i] = y[-1]
                    quant[i] = y[-1]
                continue
            if thetas is None:
                mean, std = gp.predict(((t_last + h) / scale)[:, None], return_std=True)
                point[i] = mean
                quant[i] = mean[:, None] + std[:, None] * z[None, :]
                continue
            theta = float(thetas[i])
            tq = np.concatenate([[0.0], grid])  # step 0 = last observed point
            mean, cov = gp.predict(((t_last + tq) / scale)[:, None], return_cov=True)
            cov = 0.5 * (cov + cov.T)
            rng = np.random.default_rng(self.seed + i)
            try:
                chol = np.linalg.cholesky(
                    cov + 1e-9 * np.eye(len(tq)) * max(cov.diagonal().max(), 1e-12)
                )
            except np.linalg.LinAlgError:
                w, v = np.linalg.eigh(cov)
                chol = v * np.sqrt(np.clip(w, 0.0, None))
            paths = mean[None, :] + rng.standard_normal((self.n_paths, len(tq))) @ chol.T
            times = np.array([self._cross_time(tq, p, theta) for p in paths])
            quant[i, 0] = np.quantile(times, q)
            point[i, 0] = float(np.median(times))
            self.last_censored_[i] = point[i, 0] >= self.max_horizon_
        if self.n_short_:
            log.warning("GPRExtrap: %d samples with < %d valid points", self.n_short_, MIN_POINTS)
        return Prediction(point=point, quantiles=quant, quantile_levels=tuple(self.quantile_levels))

    def _cross_time(self, tq: np.ndarray, path: np.ndarray, theta: float) -> float:
        """First crossing below theta (linearly interpolated), clipped to [1, max_horizon]."""
        below = path[1:] < theta
        if not below.any():
            return float(self.max_horizon_)
        j = int(np.argmax(below)) + 1  # index into tq / path
        a, b = path[j - 1], path[j]
        frac = 0.0 if a == b else float(np.clip((a - theta) / (a - b), 0.0, 1.0))
        return float(np.clip(tq[j - 1] + frac * (tq[j] - tq[j - 1]), 1.0, self.max_horizon_))
