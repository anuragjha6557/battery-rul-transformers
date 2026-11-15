"""Level-0 baselines: persistence and last-slope extrapolation (PLAN §6.4, model 0).

These are the sanity floor. If a learned model cannot beat them at a horizon, it has
learned nothing useful there. Persistence also tests whether one-step metrics are
trivial: on smooth fade, ``SOH_{k+1} ≈ SOH_k`` already scores a very low one-step RMSE.
"""

from __future__ import annotations

from typing import ClassVar

import numpy as np

from battery_rul.models.base import FitInfo, Prediction, SampleSet, TaskName

SOH_CHANNEL = 0


def _last_valid(x: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """Last valid value per row of an (n, L) array, given an (n, L) validity mask."""
    if not mask.any(axis=1).all():
        raise ValueError("every sample needs at least one valid history point")
    last_pos = mask.shape[1] - 1 - np.argmax(mask[:, ::-1], axis=1)
    return x[np.arange(x.shape[0]), last_pos]


class Persistence:
    """SOH_{T_p + h} = SOH_{T_p} for every horizon h (Task B only)."""

    name: ClassVar[str] = "persistence"
    supported_tasks: ClassVar[frozenset[TaskName]] = frozenset({"forecast"})
    probabilistic: ClassVar[bool] = False
    cross_fit: ClassVar[bool] = False  # nothing to fit -> no CV+ sub-models
    tunable: ClassVar[bool] = False  # no free hyperparameters (PROTOCOL §6)

    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        return FitInfo(n_train=len(train), n_val=len(val) if val is not None else 0)

    def predict(self, samples: SampleSet) -> Prediction:
        last = _last_valid(samples.x_hist[:, :, SOH_CHANNEL], samples.hist_mask)
        point = np.repeat(last[:, None], len(samples.horizons), axis=1).astype(np.float64)
        return Prediction(point=point)


class LastSlope:
    """Linear extrapolation of the mean SOH slope over the last ``window`` valid cycles."""

    name: ClassVar[str] = "last_slope"
    supported_tasks: ClassVar[frozenset[TaskName]] = frozenset({"forecast"})
    probabilistic: ClassVar[bool] = False
    cross_fit: ClassVar[bool] = False
    tunable: ClassVar[bool] = False

    def __init__(self, window: int = 10) -> None:
        if window < 2:
            raise ValueError("window must be >= 2")
        self.window = window

    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        return FitInfo(n_train=len(train), n_val=len(val) if val is not None else 0)

    def predict(self, samples: SampleSet) -> Prediction:
        soh = samples.x_hist[:, :, SOH_CHANNEL].astype(np.float64)
        mask = samples.hist_mask
        h = np.asarray(samples.horizons, dtype=np.float64)
        out = np.empty((len(samples), len(h)))
        for i in range(len(samples)):
            vals = soh[i][mask[i]][-self.window :]
            if vals.size >= 2:
                slope = np.polyfit(np.arange(vals.size, dtype=np.float64), vals, 1)[0]
            else:
                slope = 0.0
            out[i] = vals[-1] + slope * h
        return Prediction(point=out)
