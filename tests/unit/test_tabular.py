"""Tabular baselines (ElasticNet / LightGBM) and Severson features, synthetic data only."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from battery_rul.features.severson import delta_q_features, severson_features
from battery_rul.models.base import DEFAULT_QUANTILES, Model, SampleSet
from battery_rul.models.tabular import (
    ElasticNetModel,
    LGBMModel,
    TabularModel,
    design_matrix,
    last_soh,
)

L, H = 12, (1, 5)


def _samples(n: int = 120, task: str = "forecast", seed: int = 0, nan_lags: bool = False):
    rng = np.random.default_rng(seed)
    slope = rng.uniform(0.001, 0.004, n)
    base = rng.uniform(0.85, 1.0, n)
    hist = base[:, None] - slope[:, None] * np.arange(L)[None, :]
    mask = np.ones((n, L), bool)
    if nan_lags:
        mask[: n // 2, :6] = False
        hist = np.where(mask, hist, np.nan)
    extra = rng.normal(size=(n, L, 1))
    x_hist = np.concatenate([hist[:, :, None], extra], axis=2).astype(np.float32)
    if task == "forecast":
        y = np.stack([hist[:, -1] - slope * h for h in H], axis=1)
        hz = H
    else:
        y = ((hist[:, -1] - 0.8) / slope)[:, None]
        hz = (0,)
    return SampleSet(
        task=task,  # type: ignore[arg-type]
        x_hist=x_hist,
        hist_mask=mask,
        x_tab=(slope[:, None] * 100).astype(np.float32),
        y=y.astype(np.float32),
        y_mask=np.ones_like(y, dtype=bool),
        horizons=hz,
        channel_names=("soh", "aux"),
        feature_names=("slope100",),
        meta=pd.DataFrame({"dataset": "x", "cell_id": "c", "origin_cycle": np.arange(n)}),
    )


@pytest.mark.parametrize("model", [ElasticNetModel(n_lags=5), LGBMModel(n_lags=5, n_estimators=20)])
def test_conformance(model) -> None:
    assert isinstance(model, Model)
    assert model.cross_fit and model.tunable
    s = _samples()
    info = model.fit(s)
    assert info.n_train == len(s)
    p = model.predict(s)
    assert p.point.shape == s.y.shape and np.isfinite(p.point).all()


def test_elasticnet_recovers_linear_residual() -> None:
    train, test = _samples(300, seed=1), _samples(100, seed=2)
    m = ElasticNetModel(alpha=1e-6, l1_ratio=0.5, n_lags=5)
    m.fit(train)
    err = np.abs(m.predict(test).point - test.y)
    assert err.max() < 5e-3
    # persistence error is much larger at h=5
    assert err[:, 1].mean() < 0.2 * np.abs(last_soh(test)[:, None] - test.y)[:, 1].mean()


def test_per_horizon_masking() -> None:
    s = _samples()
    mask = s.y_mask.copy()
    mask[:, 1] = False
    mask[:10, 1] = True
    y = s.y.copy()
    y[~mask] = 1e6  # garbage in masked cells must never be learned
    s2 = SampleSet(**{**s.__dict__, "y": y, "y_mask": mask})
    m = ElasticNetModel(n_lags=5, alpha=1e-6)
    m.fit(s2)
    assert np.abs(m.predict(s).point[:, 0] - s.y[:, 0]).max() < 5e-3
    assert np.abs(m.predict(s).point[:, 1]).max() < 1.0  # not pulled toward 1e6
    # fully masked horizon falls back to persistence (zero residual)
    mask[:, 1] = False
    s3 = SampleSet(**{**s.__dict__, "y": y, "y_mask": mask})
    m3 = LGBMModel(n_lags=5, n_estimators=10)
    m3.fit(s3)
    np.testing.assert_allclose(m3.predict(s).point[:, 1], last_soh(s))


def test_quantile_monotonicity_and_median_point() -> None:
    s = _samples(200)
    m = LGBMModel(n_lags=5, n_estimators=30, num_leaves=8, min_child_samples=5)
    m.fit(s)
    p = m.predict(s)
    assert p.quantiles is not None and p.quantiles.shape == (200, 2, 5)
    assert p.quantile_levels == DEFAULT_QUANTILES
    assert (np.diff(p.quantiles, axis=2) >= 0).all()
    np.testing.assert_array_equal(p.point, p.quantiles[..., 2])
    assert LGBMModel(quantile=False, n_estimators=5).fit(s).n_train == len(s)


def test_early_stopping_uses_val() -> None:
    train, val = _samples(150, seed=3), _samples(60, seed=4)
    m = LGBMModel(n_lags=5, n_estimators=1000, learning_rate=0.2, quantile=False)
    info = m.fit(train, val)
    best = [e["best_iteration"] for e in info.extra["per_horizon"]]
    assert all(b < 1000 for b in best)
    assert info.best_val_loss is not None and info.n_val == 60
    no_val = LGBMModel(n_lags=5, n_estimators=40, quantile=False).fit(train)
    assert [e["best_iteration"] for e in no_val.extra["per_horizon"]] == [40, 40]


def test_rul_log1p_round_trip_and_fit() -> None:
    s = _samples(task="rul")
    t = TabularModel.to_target(s)
    np.testing.assert_allclose(t, np.log1p(s.y.astype(np.float64)))
    np.testing.assert_allclose(TabularModel.from_target(s, t[..., None])[..., 0], s.y, rtol=1e-5)
    m = ElasticNetModel(alpha=1e-4, n_lags=5)
    m.fit(s)
    p = m.predict(s).point
    assert (p >= 0).all()
    assert np.median(np.abs(p - s.y) / s.y) < 0.3


def test_determinism() -> None:
    s = _samples(150)
    p1 = LGBMModel(n_lags=5, n_estimators=30, seed=7)
    p2 = LGBMModel(n_lags=5, n_estimators=30, seed=7)
    p1.fit(s)
    p2.fit(s)
    np.testing.assert_array_equal(p1.predict(s).quantiles, p2.predict(s).quantiles)


def test_elasticnet_imputes_with_training_medians_only() -> None:
    train = _samples(100, seed=5, nan_lags=True)
    m1 = ElasticNetModel(n_lags=8)
    m1.fit(train)
    test = _samples(40, seed=6, nan_lags=True)
    wild = SampleSet(**{**test.__dict__, "x_hist": test.x_hist * 100, "x_tab": test.x_tab + 50})
    m1.predict(test)
    m1.predict(wild)  # predicting never refits
    m2 = ElasticNetModel(n_lags=8)
    m2.fit(train)
    for h in (0, 1):
        a, b = m1.pipelines_[h], m2.pipelines_[h]
        np.testing.assert_array_equal(a.named_steps["enet"].coef_, b.named_steps["enet"].coef_)
        np.testing.assert_array_equal(
            a.named_steps["impute"].statistics_, b.named_steps["impute"].statistics_
        )
    x, _ = design_matrix(train, 8)
    np.testing.assert_allclose(
        m1.pipelines_[0].named_steps["impute"].statistics_, np.nanmedian(x, axis=0)
    )


def test_feature_importances_tables() -> None:
    s = _samples()
    for m in (ElasticNetModel(n_lags=5), LGBMModel(n_lags=5, n_estimators=10)):
        m.fit(s)
        fi = m.feature_importances()
        assert set(fi.columns) == {"horizon_idx", "feature", "importance"}
        assert {"slope100", "soh_lag0", "last_aux"} <= set(fi["feature"])


# -- Severson ------------------------------------------------------------------------------------
def test_delta_q_known_variance() -> None:
    v = np.linspace(0, 1, 101)
    q10 = 1.0 - 0.2 * v
    q100 = q10 + 0.05 * v  # dQ = 0.05 * v -> var = 0.05^2 * var(v)
    f = delta_q_features(q100, q10)
    assert f["dq_var"] == pytest.approx(np.log10(0.05**2 * np.var(v, ddof=1)))
    assert f["dq_min"] == pytest.approx(np.log10(1e-12))  # min dQ = 0 -> eps floor
    assert f["dq_skew"] == pytest.approx(np.log10(1e-12), abs=1.0)  # uniform -> ~0 skew


def test_severson_features_synthetic_cell() -> None:
    cyc = np.arange(2, 101)
    cycles = pd.DataFrame(
        {
            "cycle_idx": cyc,
            "capacity_ah": 1.1 - 1e-4 * cyc,
            "charge_time_s": 1000.0,
            "ir_ohm": 0.016 + 1e-5 * cyc,
            "discharge_temp_max_c": 30.0,
        }
    )
    grid = np.linspace(0, 1, 50)
    curves = pd.concat(
        [
            pd.DataFrame(
                {
                    "cycle_idx": c,
                    "phase": "discharge",
                    "sample_idx": np.arange(50),
                    "charge_ah": 1.0 - 0.1 * (c / 100) * grid,
                }
            )
            for c in (10, 100)
        ]
    )
    f = severson_features(cycles, curves)
    dq = -0.1 * (1 - 0.1) * grid
    assert f["dq_var"] == pytest.approx(np.log10(np.var(dq, ddof=1)))
    assert f["q2"] == pytest.approx(1.1 - 2e-4)
    assert f["qmax_minus_q2"] == pytest.approx(0.0)
    assert f["fade_slope"] == pytest.approx(-1e-4, rel=1e-6)
    assert f["charge_time_mean_2_6"] == 1000.0
    assert f["ir_delta"] == pytest.approx(1e-5 * 98)
    assert f["temp_integral"] == pytest.approx(30.0 * 98)
