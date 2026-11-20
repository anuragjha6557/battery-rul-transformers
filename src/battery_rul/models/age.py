"""Age-only baseline for the field setting (PLAN_PHASE2 §6).

Uses nothing but the cell's age (cycle count, which any BMS knows): the pooled, monotone
(non-increasing) relation SOH = f(cycle) fitted on the training cells by isotonic regression.

* soh: f(k)
* forecast: f(k + h)
* rul: the median over training cells of (EOL - k), i.e. RUL = max(median EOL - k, 0) with the
  training cells' EOL cycles; that is the best age-only guess of remaining life.

If field models cannot beat this, their signals add nothing beyond age. The age is read from the
``log_age`` tabular feature (field feature sets), never from ``meta``.
"""

from __future__ import annotations

from typing import ClassVar

import numpy as np
from sklearn.isotonic import IsotonicRegression

from battery_rul.models.base import FitInfo, Prediction, SampleSet, TaskName


def _age(s: SampleSet) -> np.ndarray:
    if "log_age" not in s.feature_names:
        raise ValueError("age_only needs the 'log_age' feature (field feature sets)")
    return np.expm1(s.x_tab[:, s.feature_names.index("log_age")].astype(np.float64))


class AgeOnly:
    name = "age_only"
    supported_tasks: ClassVar[frozenset[TaskName]] = frozenset({"soh", "forecast", "rul"})
    probabilistic: ClassVar[bool] = False
    cross_fit: ClassVar[bool] = False
    tunable: ClassVar[bool] = False

    def __init__(self) -> None:
        self._iso: IsotonicRegression | None = None
        self._eol: float = float("nan")

    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        age = _age(train)
        if train.task == "rul":
            eol = age + train.y[:, 0].astype(np.float64)  # every row of a cell gives its EOL
            self._eol = float(np.median(eol[train.y_mask[:, 0]]))
        else:
            # pool (age + h, target) over horizons: SOH as a function of the target cycle
            xs, ys = [], []
            for j, h in enumerate(train.horizons):
                m = train.y_mask[:, j]
                xs.append(age[m] + h)
                ys.append(train.y[m, j].astype(np.float64))
            self._iso = IsotonicRegression(increasing=False, out_of_bounds="clip")
            self._iso.fit(np.concatenate(xs), np.concatenate(ys))
        return FitInfo(n_train=len(train), n_val=0 if val is None else len(val))

    def predict(self, samples: SampleSet) -> Prediction:
        age = _age(samples)
        if samples.task == "rul":
            return Prediction(point=np.maximum(self._eol - age, 0.0)[:, None])
        assert self._iso is not None, "fit() first"
        cols = [self._iso.predict(age + h) for h in samples.horizons]
        return Prediction(point=np.stack(cols, axis=1))
