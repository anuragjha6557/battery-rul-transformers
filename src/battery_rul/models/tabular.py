"""Hand-crafted-feature baselines: ElasticNet and LightGBM (PLAN §6.4, model 3).

Both models share one design matrix and one target convention (mirroring ``neural.py``):

- **Design matrix** (per sample): ``x_tab`` (SUMMARY_FEATURES for Tasks B/C; ``now_*`` charge
  features + last SOH for Task A) + the last ``n_lags`` SOH values from ``x_hist`` channel 0
  (most recent first, NaN where the cell has fewer past cycles) + the last-step value of every
  other history channel. LightGBM consumes the NaNs natively; ElasticNet median-imputes them with
  *training* medians (the imputer is part of the fitted pipeline, so test rows never influence it).
- **Targets:** soh/forecast are learned as the residual ``y - last observed SOH`` (persistence is
  the zero function). RUL is learned as ``log1p(rul)`` and inverted with ``expm1``: RUL is
  right-skewed and its errors are multiplicative (being 50 cycles off matters at RUL 100, not at
  RUL 1000), so the log scale equalises them and keeps predictions non-negative. The inverse is
  monotone, so quantiles fitted in log space map to the same quantiles in cycles.
- **Direct multi-horizon:** one regressor per horizon; rows whose target is masked
  (horizon beyond end of life) are dropped for that horizon only.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

if TYPE_CHECKING:  # lightgbm is imported lazily: see models/registry.py (OpenMP isolation)
    import lightgbm as lgb

from battery_rul.models.base import (
    DEFAULT_QUANTILES,
    FitInfo,
    Prediction,
    SampleSet,
    TaskName,
)

SOH_CHANNEL = 0
EARLY_STOPPING_ROUNDS = 50


def last_soh(samples: SampleSet) -> np.ndarray:
    """Last observed SOH per sample (fraction); raises if a sample has no valid history."""
    mask = samples.hist_mask
    if not mask.any(axis=1).all():
        raise ValueError("every sample needs at least one valid history point")
    last = mask.shape[1] - 1 - np.argmax(mask[:, ::-1], axis=1)
    return samples.x_hist[np.arange(len(samples)), last, SOH_CHANNEL].astype(np.float64)


def _has_soh(samples: SampleSet) -> bool:
    return bool(samples.channel_names) and samples.channel_names[0] == "soh"


def _field_design(samples: SampleSet) -> tuple[np.ndarray, tuple[str, ...]]:
    """Field setting (no SOH channel): last value, window mean and window change per channel."""
    x = np.where(samples.hist_mask[..., None], samples.x_hist.astype(np.float64), np.nan)
    with np.errstate(all="ignore"):
        last = x[:, -1, :]
        mean = np.nanmean(x, axis=1)
        first_idx = np.argmax(samples.hist_mask, axis=1)
        first = x[np.arange(len(x)), first_idx, :]
    cols = np.hstack([samples.x_tab.astype(np.float64), last, mean, last - first])
    names = (
        *samples.feature_names,
        *[f"last_{c}" for c in samples.channel_names],
        *[f"mean_{c}" for c in samples.channel_names],
        *[f"delta_{c}" for c in samples.channel_names],
    )
    return cols, names


def design_matrix(samples: SampleSet, n_lags: int) -> tuple[np.ndarray, tuple[str, ...]]:
    """(n, F + n_lags + C - 1) float64 design matrix and its column names (NaN = unavailable)."""
    if not _has_soh(samples):
        return _field_design(samples)
    soh = samples.x_hist[:, :, SOH_CHANNEL].astype(np.float64)
    mask = samples.hist_mask
    soh = np.where(mask, soh, np.nan)
    lags = soh[:, ::-1][:, :n_lags]  # lag 0 = most recent
    if lags.shape[1] < n_lags:
        pad = np.full((lags.shape[0], n_lags - lags.shape[1]), np.nan)
        lags = np.hstack([lags, pad])
    other = samples.x_hist[:, -1, 1:].astype(np.float64)
    x = np.hstack([samples.x_tab.astype(np.float64), lags, other])
    names = (
        *samples.feature_names,
        *[f"soh_lag{k}" for k in range(n_lags)],
        *[f"last_{c}" for c in samples.channel_names[1:]],
    )
    return x, names


class _Const:
    """Fallback for a horizon with no unmasked training rows: predicts a constant."""

    def __init__(self, value: float) -> None:
        self.value = value

    def predict(self, x: np.ndarray) -> np.ndarray:
        return np.full(len(x), self.value)


class TabularModel:
    """Shared fit/predict skeleton; subclasses implement the two ``_*_horizon`` hooks."""

    name: ClassVar[str] = "tabular"
    supported_tasks: ClassVar[frozenset[TaskName]] = frozenset({"soh", "forecast", "rul"})
    probabilistic: ClassVar[bool] = False
    cross_fit: ClassVar[bool] = True
    tunable: ClassVar[bool] = True

    n_lags: int
    quantile_levels: tuple[float, ...] | None = None

    # -- target transforms --------------------------------------------------------------------
    @staticmethod
    def to_target(s: SampleSet) -> np.ndarray:
        """(n, H) regression target: SOH residual vs last observed SOH, or log1p(RUL)."""
        y = s.y.astype(np.float64)
        if s.task == "rul":
            return np.log1p(np.maximum(y, 0.0))
        if not _has_soh(s):  # field setting: absolute SOH
            return y
        return y - last_soh(s)[:, None]

    @staticmethod
    def from_target(s: SampleSet, t: np.ndarray) -> np.ndarray:
        """Invert :meth:`to_target` on an array of shape (n, H, ...)."""
        if s.task == "rul":
            return np.maximum(np.expm1(t), 0.0)
        if not _has_soh(s):
            return t
        extra = (1,) * (t.ndim - 1)
        return t + last_soh(s).reshape(-1, *extra)

    # -- to implement -------------------------------------------------------------------------
    def _fit_horizon(
        self,
        h: int,
        x: np.ndarray,
        y: np.ndarray,
        xv: np.ndarray | None,
        yv: np.ndarray | None,
    ) -> dict[str, Any]:
        raise NotImplementedError

    def _predict_horizon(self, h: int, x: np.ndarray) -> np.ndarray:
        """(n, Q) predictions in target space (Q = 1 for point models)."""
        raise NotImplementedError

    # -- Model protocol -----------------------------------------------------------------------
    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        self._task = train.task
        self._n_h = len(train.horizons)
        x, self.feature_names_ = design_matrix(train, self.n_lags)
        y = self.to_target(train)
        xv = yv = None
        if val is not None:
            xv, _ = design_matrix(val, self.n_lags)
            yv = self.to_target(val)
        self._fitted_h: list[int] = []
        extras: list[dict[str, Any]] = []
        for h in range(self._n_h):
            m = train.y_mask[:, h]
            vm = val.y_mask[:, h] if val is not None else None
            xv_h = yv_h = None
            if xv is not None and yv is not None and vm is not None and vm.any():
                xv_h, yv_h = xv[vm], yv[vm, h]
            extras.append(self._fit_horizon(h, x[m], y[m, h], xv_h, yv_h))
            self._fitted_h.append(h)
        losses = [e["val_loss"] for e in extras if e.get("val_loss") is not None]
        return FitInfo(
            n_train=len(train),
            n_val=len(val) if val is not None else 0,
            epochs=None,
            best_val_loss=float(np.mean(losses)) if losses else None,
            extra={"per_horizon": extras},
        )

    def predict(self, samples: SampleSet) -> Prediction:
        if not hasattr(self, "_fitted_h"):
            raise RuntimeError("fit() first")
        if len(samples.horizons) != self._n_h:
            raise ValueError("samples have a different number of horizons than at fit time")
        x, _ = design_matrix(samples, self.n_lags)
        t = np.stack([self._predict_horizon(h, x) for h in range(self._n_h)], axis=1)  # (n,H,Q)
        y = self.from_target(samples, t)
        if self.quantile_levels is None:
            return Prediction(point=y[..., 0])
        y = np.sort(y, axis=2)  # rearrangement: monotone quantiles
        median = y[..., self.quantile_levels.index(0.5)]
        return Prediction(point=median, quantiles=y, quantile_levels=self.quantile_levels)

    def feature_importances(self) -> pd.DataFrame:
        """Long table ``horizon_idx, feature, importance`` (subclass-defined importance)."""
        raise NotImplementedError


class ElasticNetModel(TabularModel):
    """ElasticNet on the shared design matrix, point predictions only.

    Pipeline per horizon: median imputation (training medians) -> standardise -> ElasticNet.
    ``alpha`` / ``l1_ratio`` follow sklearn's definitions on standardised features and targets
    in the units above (SOH fraction residual, or log1p cycles).
    """

    name: ClassVar[str] = "elasticnet"
    probabilistic: ClassVar[bool] = False

    def __init__(
        self,
        alpha: float = 1e-3,
        l1_ratio: float = 0.5,
        n_lags: int = 10,
        max_iter: int = 20000,
    ) -> None:
        self.alpha, self.l1_ratio, self.n_lags, self.max_iter = alpha, l1_ratio, n_lags, max_iter
        self.pipelines_: dict[int, Pipeline | _Const] = {}

    def _fit_horizon(
        self,
        h: int,
        x: np.ndarray,
        y: np.ndarray,
        xv: np.ndarray | None,
        yv: np.ndarray | None,
    ) -> dict[str, Any]:
        if len(y) == 0:
            self.pipelines_[h] = _Const(0.0)
            return {"n_rows": 0}
        pipe = Pipeline(
            [
                ("impute", SimpleImputer(strategy="median", keep_empty_features=True)),
                ("scale", StandardScaler()),
                (
                    "enet",
                    ElasticNet(alpha=self.alpha, l1_ratio=self.l1_ratio, max_iter=self.max_iter),
                ),
            ]
        )
        pipe.fit(x, y)
        self.pipelines_[h] = pipe
        val_loss = None
        if xv is not None and yv is not None:
            val_loss = float(np.mean((pipe.predict(xv) - yv) ** 2))
        return {"n_rows": len(y), "val_loss": val_loss}

    def _predict_horizon(self, h: int, x: np.ndarray) -> np.ndarray:
        return self.pipelines_[h].predict(x)[:, None]

    def feature_importances(self) -> pd.DataFrame:
        """Absolute standardised coefficients per horizon (``importance`` = |coef|)."""
        rows = []
        for h, p in self.pipelines_.items():
            if isinstance(p, Pipeline):
                coef = p.named_steps["enet"].coef_
                rows += [
                    {"horizon_idx": h, "feature": f, "importance": float(abs(c))}
                    for f, c in zip(self.feature_names_, coef, strict=True)
                ]
        return pd.DataFrame(rows, columns=["horizon_idx", "feature", "importance"])


class LGBMModel(TabularModel):
    """LightGBM point model (L2) plus optional per-level quantile models.

    The L2 model early-stops on ``val`` (50 rounds) when val is given; every quantile model then
    reuses its ``best_iteration`` as ``n_estimators`` to keep cost bounded. With
    ``quantile=True`` the reported point is the (rearranged) median quantile model.
    Subsampling is active (``subsample_freq=1``); training is deterministic given ``seed``.
    """

    name: ClassVar[str] = "lgbm"
    probabilistic: ClassVar[bool] = True

    def __init__(
        self,
        num_leaves: int = 31,
        learning_rate: float = 0.05,
        n_estimators: int = 1000,
        min_child_samples: int = 20,
        subsample: float = 0.8,
        colsample_bytree: float = 0.8,
        reg_lambda: float = 1.0,
        n_lags: int = 10,
        quantile: bool = True,
        num_threads: int = 2,
        seed: int = 0,
        quantiles: tuple[float, ...] = DEFAULT_QUANTILES,
    ) -> None:
        if quantile and 0.5 not in quantiles:
            raise ValueError("quantiles must include the median 0.5")
        self.params: dict[str, Any] = {
            "num_leaves": num_leaves,
            "learning_rate": learning_rate,
            "min_child_samples": min_child_samples,
            "subsample": subsample,
            "subsample_freq": 1,
            "colsample_bytree": colsample_bytree,
            "reg_lambda": reg_lambda,
            "n_jobs": num_threads,
            "random_state": seed,
            "deterministic": True,
            "force_row_wise": True,
            "verbose": -1,
        }
        self.n_estimators, self.n_lags, self.quantile = n_estimators, n_lags, quantile
        self.levels = tuple(sorted(quantiles))
        self.quantile_levels = self.levels if quantile else None
        self.point_: dict[int, lgb.LGBMRegressor | _Const] = {}
        self.quantile_: dict[int, list[lgb.LGBMRegressor | _Const]] = {}

    def _fit_horizon(
        self,
        h: int,
        x: np.ndarray,
        y: np.ndarray,
        xv: np.ndarray | None,
        yv: np.ndarray | None,
    ) -> dict[str, Any]:
        import lightgbm as lgb  # lazy: OpenMP isolation (models/registry.py)

        if len(y) == 0:
            self.point_[h] = _Const(0.0)
            self.quantile_[h] = [_Const(0.0) for _ in self.levels]
            return {"n_rows": 0}
        point = lgb.LGBMRegressor(objective="l2", n_estimators=self.n_estimators, **self.params)
        if xv is not None and yv is not None and len(yv):
            point.fit(
                x,
                y,
                eval_set=[(xv, yv)],
                callbacks=[lgb.early_stopping(EARLY_STOPPING_ROUNDS, verbose=False)],
            )
            best = int(point.best_iteration_ or self.n_estimators)
            val_loss = float(point.best_score_["valid_0"]["l2"])
        else:
            point.fit(x, y)
            best, val_loss = self.n_estimators, None
        self.point_[h] = point
        if self.quantile:
            qs: list[lgb.LGBMRegressor | _Const] = []
            for q in self.levels:
                m = lgb.LGBMRegressor(
                    objective="quantile", alpha=q, n_estimators=best, **self.params
                )
                m.fit(x, y)
                qs.append(m)
            self.quantile_[h] = qs
        return {"n_rows": len(y), "best_iteration": best, "val_loss": val_loss}

    def _predict_horizon(self, h: int, x: np.ndarray) -> np.ndarray:
        if self.quantile:
            return np.stack([m.predict(x) for m in self.quantile_[h]], axis=1)
        return np.asarray(self.point_[h].predict(x))[:, None]

    def feature_importances(self) -> pd.DataFrame:
        """Gain importance of the L2 point model per horizon, normalised to sum to 1."""
        import lightgbm as lgb

        rows = []
        for h, m in self.point_.items():
            if isinstance(m, lgb.LGBMRegressor):
                gain = m.booster_.feature_importance(importance_type="gain").astype(np.float64)
                gain = gain / gain.sum() if gain.sum() > 0 else gain
                rows += [
                    {"horizon_idx": h, "feature": f, "importance": float(g)}
                    for f, g in zip(self.feature_names_, gain, strict=True)
                ]
        return pd.DataFrame(rows, columns=["horizon_idx", "feature", "importance"])
