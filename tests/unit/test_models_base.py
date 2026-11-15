"""Model contract (SampleSet / Prediction) and level-0 baselines."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from battery_rul.models.base import Model, Prediction, SampleSet
from battery_rul.models.persistence import LastSlope, Persistence


def make_samples(n: int = 4, L: int = 6, horizons: tuple[int, ...] = (1, 5)) -> SampleSet:
    rng = np.random.default_rng(0)
    soh = 1.0 - 0.01 * np.arange(L)[None, :] - 0.001 * rng.random((n, L))
    x_hist = soh[:, :, None].astype(np.float32)
    mask = np.ones((n, L), bool)
    mask[0, :2] = False  # first sample has a shorter history
    x_hist[0, :2] = np.nan
    return SampleSet(
        task="forecast",
        x_hist=x_hist,
        hist_mask=mask,
        x_tab=np.zeros((n, 0), np.float32),
        y=np.full((n, len(horizons)), 0.9, np.float32),
        y_mask=np.ones((n, len(horizons)), bool),
        horizons=horizons,
        channel_names=("soh",),
        feature_names=(),
        meta=pd.DataFrame(
            {"dataset": "nasa", "cell_id": "B0005", "origin_cycle": np.arange(n) + L}
        ),
    )


def test_sampleset_rejects_cycle_idx_as_input() -> None:
    s = make_samples()
    with pytest.raises(ValueError, match="leakage rule 4"):
        SampleSet(
            task=s.task,
            x_hist=s.x_hist,
            hist_mask=s.hist_mask,
            x_tab=np.zeros((len(s), 1), np.float32),
            y=s.y,
            y_mask=s.y_mask,
            horizons=s.horizons,
            channel_names=s.channel_names,
            feature_names=("cycle_idx",),
            meta=s.meta,
        )


def test_sampleset_shape_checks() -> None:
    s = make_samples()
    with pytest.raises(ValueError, match="y column count"):
        SampleSet(
            task=s.task,
            x_hist=s.x_hist,
            hist_mask=s.hist_mask,
            x_tab=s.x_tab,
            y=s.y[:, :1],
            y_mask=s.y_mask[:, :1],
            horizons=s.horizons,
            channel_names=s.channel_names,
            feature_names=s.feature_names,
            meta=s.meta,
        )


def test_subset_keeps_alignment() -> None:
    s = make_samples(n=5)
    sub = s.subset(np.array([True, False, True, False, True]))
    assert len(sub) == 3
    assert sub.meta["origin_cycle"].tolist() == [6, 8, 10]
    sub2 = s.subset(np.array([4, 0]))
    assert sub2.meta["origin_cycle"].tolist() == [10, 6]


def test_prediction_validates_quantiles() -> None:
    with pytest.raises(ValueError, match="increasing"):
        Prediction(
            point=np.zeros((2, 1)), quantiles=np.zeros((2, 1, 2)), quantile_levels=(0.9, 0.1)
        )


def test_persistence_repeats_last_valid_soh() -> None:
    s = make_samples()
    p = Persistence().predict(s)
    np.testing.assert_allclose(p.point[:, 0], s.x_hist[:, -1, 0], rtol=1e-6)
    np.testing.assert_allclose(p.point[:, 0], p.point[:, 1])
    assert isinstance(Persistence(), Model)


def test_last_slope_extrapolates_linear_fade_exactly() -> None:
    n, L = 3, 12
    soh = (1.0 - 0.002 * np.arange(L))[None, :].repeat(n, 0)
    s = make_samples(n=n, L=L, horizons=(1, 10))
    s = SampleSet(
        task="forecast",
        x_hist=soh[:, :, None].astype(np.float64),
        hist_mask=np.ones((n, L), bool),
        x_tab=s.x_tab[:n],
        y=s.y[:n],
        y_mask=s.y_mask[:n],
        horizons=(1, 10),
        channel_names=("soh",),
        feature_names=(),
        meta=s.meta.iloc[:n],
    )
    p = LastSlope(window=5).predict(s)
    last = soh[0, -1]
    np.testing.assert_allclose(p.point[0], [last - 0.002, last - 0.02], atol=1e-12)
