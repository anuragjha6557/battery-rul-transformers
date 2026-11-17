"""Recursive one-step rollout wrapper (ADR-0010 arm b; the source paper's forecasting scheme).

The base model is trained as a one-step (h = 1) forecaster. At predict time it is applied
repeatedly: its own SOH prediction is appended to the SOH channel of the history window (the
oldest step dropped), and the forecast for horizon ``h`` is the output of the ``h``-th step.

**Exogenous handling (declared mode ``exog="hold"``, PROTOCOL §2):** every non-SOH history
channel is held at its *last observed value* for all rolled-forward steps (the step is appended
with that value and mask = True), and the tabular features ``x_tab`` (summaries at the origin)
are kept fixed. Nothing about the future of the exogenous channels is forecast. The alternative
declared mode (joint forecast of all channels) is not implemented.

Output is a point forecast (the median when the base model is probabilistic); ``quantiles`` is
``None`` because quantiles cannot be propagated through the rollout without a sampling scheme.

Not tunable: at benchmark time the base params are the tuned params of the direct base model.
Only the ``forecast`` task is supported (rollout needs horizons >= 1).
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal

import numpy as np

from battery_rul.models.base import FitInfo, Prediction, SampleSet, TaskName
from battery_rul.models.registry import MODELS, accepts_kwarg, make_model


def _one_step(s: SampleSet | None, h_train: tuple[int, ...]) -> SampleSet | None:
    """Re-slice targets to ``h_train`` (must include horizon 1)."""
    if s is None:
        return None
    if 1 not in s.horizons:
        raise ValueError(f"recursive training needs horizon 1; sample set has {s.horizons}")
    cols = [s.horizons.index(h) for h in h_train]
    return SampleSet(
        task=s.task,
        x_hist=s.x_hist,
        hist_mask=s.hist_mask,
        x_tab=s.x_tab,
        y=s.y[:, cols],
        y_mask=s.y_mask[:, cols],
        horizons=tuple(h_train),
        channel_names=s.channel_names,
        feature_names=s.feature_names,
        meta=s.meta,
    )


class RecursiveWrapper:
    """``base_name``/``base_params``: any registered point/quantile model on the forecast task."""

    name: ClassVar[str] = "recursive"
    supported_tasks: ClassVar[frozenset[TaskName]] = frozenset({"forecast"})
    probabilistic: ClassVar[bool] = False
    cross_fit: ClassVar[bool] = True
    tunable: ClassVar[bool] = False

    def __init__(
        self,
        *,
        base_name: str,
        base_params: dict[str, Any] | None = None,
        horizons_train: tuple[int, ...] = (1,),
        exog: Literal["hold"] = "hold",
        device: str | None = None,
    ) -> None:
        if base_name not in MODELS:
            raise KeyError(f"unknown base model {base_name!r}")
        if base_name == "recursive":
            raise ValueError("cannot nest recursive wrappers")
        if 1 not in horizons_train:
            raise ValueError("horizons_train must include 1")
        if exog != "hold":
            raise ValueError("only exog='hold' is implemented")
        self.base_name = base_name
        self.base_params = dict(base_params or {})
        self.horizons_train = tuple(int(h) for h in horizons_train)
        self.exog = exog
        self.device = device
        self.base: Any = None

    def _make_base(self) -> Any:
        params = dict(self.base_params)
        if (
            self.device is not None
            and "device" not in params
            and accepts_kwarg(MODELS[self.base_name], "device")
        ):
            params["device"] = self.device
        return make_model(self.base_name, **params)

    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        self.base = self._make_base()
        return self.base.fit(
            _one_step(train, self.horizons_train),
            _one_step(val, self.horizons_train),
        )

    def predict(self, samples: SampleSet) -> Prediction:
        if self.base is None:
            raise RuntimeError("fit() first")
        hs = samples.horizons
        if min(hs) < 1:
            raise ValueError("recursive rollout needs horizons >= 1")
        n, L, _ = samples.x_hist.shape
        x = samples.x_hist.copy()
        mask = samples.hist_mask.copy()
        if not mask.any(axis=1).all():
            raise ValueError("every sample needs at least one valid history point")
        last = L - 1 - np.argmax(mask[:, ::-1], axis=1)
        held = x[np.arange(n), last, :].copy()  # (n, C): last observed value of each channel
        step_col = self.horizons_train.index(1)
        preds: dict[int, np.ndarray] = {}
        dummy_y = np.zeros((n, len(self.horizons_train)), dtype=np.float32)
        for step in range(1, max(hs) + 1):
            cur = SampleSet(
                task=samples.task,
                x_hist=x,
                hist_mask=mask,
                x_tab=samples.x_tab,
                y=dummy_y,
                y_mask=np.ones_like(dummy_y, dtype=bool),
                horizons=self.horizons_train,
                channel_names=samples.channel_names,
                feature_names=samples.feature_names,
                meta=samples.meta,
            )
            soh = self.base.predict(cur).point[:, step_col]
            if step in hs:
                preds[step] = soh.copy()
            new = held.copy()
            new[:, 0] = soh  # exogenous channels stay at their last observed value
            x = np.concatenate([x[:, 1:], new[:, None, :].astype(x.dtype)], axis=1)
            mask = np.concatenate([mask[:, 1:], np.ones((n, 1), dtype=bool)], axis=1)
        return Prediction(point=np.stack([preds[h] for h in hs], axis=1))
