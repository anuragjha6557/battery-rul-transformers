"""The contract every model in the benchmark implements.

A model never sees raw tables. It receives a :class:`SampleSet` built by
``battery_rul.tasks`` + ``battery_rul.features``, which have already enforced the
leakage rules of PROTOCOL.md §4. Absolute ``cycle_idx`` and ``cell_id`` live in
``SampleSet.meta`` and are never model inputs.

Shapes: n = samples, L = history length, C = history channels, F = tabular features,
H = horizons (Task A: H = 1; Task B: len(horizons); Task C: H = 1, target = RUL),
Q = quantile levels.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar, Literal, Protocol, runtime_checkable

import numpy as np
import pandas as pd

TaskName = Literal["soh", "forecast", "rul"]
TASKS: tuple[TaskName, ...] = ("soh", "forecast", "rul")
DEFAULT_QUANTILES: tuple[float, ...] = (0.05, 0.25, 0.5, 0.75, 0.95)


@dataclass(frozen=True)
class SampleSet:
    """Model-ready samples for one task and one set of cells.

    Attributes:
        task: Which PROTOCOL task the targets belong to.
        x_hist: (n, L, C) float32 history up to and including the origin cycle; NaN where
            the cell has fewer than L past cycles (see ``hist_mask``). Channel 0 is SOH.
        hist_mask: (n, L) bool, True where ``x_hist`` holds real data.
        x_tab: (n, F) float32 tabular features at the origin (Task A: charge-phase features of
            the current cycle + history summaries; Tasks B/C: summaries of cycles <= T_p).
        y: (n, H) float32 targets. SOH fraction for "soh"/"forecast", cycles for "rul".
        y_mask: (n, H) bool, True where the target exists (horizons past end of life are False).
        horizons: Horizon (cycles ahead) of each target column; (0,) for Task A, (0,) for RUL.
        channel_names: Names of the C history channels.
        feature_names: Names of the F tabular features.
        meta: One row per sample with at least ``dataset``, ``cell_id``, ``origin_cycle``.
            Bookkeeping only — never a model input (leakage rule 4).
    """

    task: TaskName
    x_hist: np.ndarray
    hist_mask: np.ndarray
    x_tab: np.ndarray
    y: np.ndarray
    y_mask: np.ndarray
    horizons: tuple[int, ...]
    channel_names: tuple[str, ...]
    feature_names: tuple[str, ...]
    meta: pd.DataFrame = field(repr=False)

    def __post_init__(self) -> None:
        n = self.y.shape[0]
        if self.task not in TASKS:
            raise ValueError(f"unknown task {self.task!r}")
        if self.x_hist.ndim != 3 or self.x_hist.shape[0] != n:
            raise ValueError(f"x_hist must be (n, L, C) with n={n}, got {self.x_hist.shape}")
        if self.hist_mask.shape != self.x_hist.shape[:2]:
            raise ValueError("hist_mask must be (n, L)")
        if self.x_hist.shape[2] != len(self.channel_names):
            raise ValueError("x_hist channel count != len(channel_names)")
        if self.x_tab.ndim != 2 or self.x_tab.shape[0] != n:
            raise ValueError(f"x_tab must be (n, F) with n={n}, got {self.x_tab.shape}")
        if self.x_tab.shape[1] != len(self.feature_names):
            raise ValueError("x_tab feature count != len(feature_names)")
        if self.y.ndim != 2 or self.y_mask.shape != self.y.shape:
            raise ValueError("y and y_mask must both be (n, H)")
        if self.y.shape[1] != len(self.horizons):
            raise ValueError("y column count != len(horizons)")
        if len(self.meta) != n:
            raise ValueError("meta must have one row per sample")
        missing = {"dataset", "cell_id", "origin_cycle"} - set(self.meta.columns)
        if missing:
            raise ValueError(f"meta is missing columns {sorted(missing)}")
        forbidden = {"cycle_idx", "origin_cycle", "cell_id"} & {
            *self.channel_names,
            *self.feature_names,
        }
        if forbidden:
            raise ValueError(f"leakage rule 4: {sorted(forbidden)} must not be model inputs")

    def __len__(self) -> int:
        return int(self.y.shape[0])

    def subset(self, idx: np.ndarray) -> SampleSet:
        """Row subset (boolean mask or integer index)."""
        return SampleSet(
            task=self.task,
            x_hist=self.x_hist[idx],
            hist_mask=self.hist_mask[idx],
            x_tab=self.x_tab[idx],
            y=self.y[idx],
            y_mask=self.y_mask[idx],
            horizons=self.horizons,
            channel_names=self.channel_names,
            feature_names=self.feature_names,
            meta=self.meta.iloc[np.asarray(idx)].reset_index(drop=True)
            if np.asarray(idx).dtype != bool
            else self.meta.loc[np.asarray(idx)].reset_index(drop=True),
        )


@dataclass(frozen=True)
class Prediction:
    """Model output aligned with a SampleSet's targets.

    Attributes:
        point: (n, H) point prediction (median for probabilistic models).
        quantiles: (n, H, Q) or None for point-only models; non-decreasing along Q.
        quantile_levels: The Q levels, e.g. DEFAULT_QUANTILES.
    """

    point: np.ndarray
    quantiles: np.ndarray | None = None
    quantile_levels: tuple[float, ...] = ()

    def __post_init__(self) -> None:
        if self.point.ndim != 2:
            raise ValueError("point must be (n, H)")
        if self.quantiles is not None:
            if self.quantiles.shape[:2] != self.point.shape:
                raise ValueError("quantiles must be (n, H, Q) matching point")
            if self.quantiles.shape[2] != len(self.quantile_levels):
                raise ValueError("quantile_levels length != Q")
            if list(self.quantile_levels) != sorted(self.quantile_levels):
                raise ValueError("quantile_levels must be increasing")


@dataclass
class FitInfo:
    """What a fit reports back to the runner (logged to MLflow)."""

    n_train: int
    n_val: int = 0
    epochs: int | None = None
    best_val_loss: float | None = None
    extra: dict[str, Any] = field(default_factory=dict)


@runtime_checkable
class Model(Protocol):
    """Every benchmark entry implements this; the runner is model-agnostic."""

    name: ClassVar[str]
    supported_tasks: ClassVar[frozenset[TaskName]]
    probabilistic: ClassVar[bool]

    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        """Fit on ``train``; ``val`` (inner held-out cell) is for early stopping only."""
        ...

    def predict(self, samples: SampleSet) -> Prediction:
        """Predict targets for ``samples``; must not read ``samples.y``."""
        ...


def check_supports(model: Model, task: TaskName) -> None:
    if task not in model.supported_tasks:
        raise ValueError(f"{model.name} does not support task {task!r}")
