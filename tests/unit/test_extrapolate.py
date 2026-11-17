"""Local extrapolation baselines on synthetic fade curves."""

from __future__ import annotations

import numpy as np
import pandas as pd

from battery_rul.models.base import Model, SampleSet, TaskName
from battery_rul.models.extrapolate import GPRExtrap, ParamFit, PrevSOH

THETA = 0.8


def make(
    curves: list[np.ndarray],
    task: TaskName,
    horizons: tuple[int, ...] = (0,),
    pad: int = 0,
) -> SampleSet:
    """Each curve is the valid history; left-padded with NaN to a common length."""
    L = max(len(c) for c in curves) + pad
    n = len(curves)
    x = np.full((n, L, 1), np.nan, np.float32)
    m = np.zeros((n, L), bool)
    for i, c in enumerate(curves):
        x[i, L - len(c) :, 0] = c
        m[i, L - len(c) :] = True
    return SampleSet(
        task=task,
        x_hist=x,
        hist_mask=m,
        x_tab=np.zeros((n, 0), np.float32),
        y=np.zeros((n, len(horizons)), np.float32),
        y_mask=np.ones((n, len(horizons)), bool),
        horizons=horizons,
        channel_names=("soh",),
        feature_names=(),
        meta=pd.DataFrame(
            {"dataset": "nasa", "cell_id": "c", "origin_cycle": 0, "theta": THETA}, index=range(n)
        ),
    )


def linear_curve(n: int, slope: float = 5e-4) -> np.ndarray:
    return 1.0 - slope * np.arange(n)


def test_linear_exact_forecast_and_rul() -> None:
    n, slope = 200, 5e-4
    y = linear_curve(n, slope)
    f = ParamFit("linear").predict(make([y], "forecast", (1, 50)))
    t_last = n - 1
    assert np.allclose(f.point[0], 1 - slope * (t_last + np.array([1, 50])), atol=1e-6)
    m = ParamFit("linear")
    r = m.predict(make([y], "rul"))
    true = (1 - THETA) / slope - t_last  # step at which SOH reaches theta
    assert abs(r.point[0, 0] - true) <= 1.0 + 1e-6
    assert not m.last_censored_[0]


def test_exp2_recovers_two_exponentials() -> None:
    t = np.arange(300, dtype=float)
    f = lambda tt: 0.4 * np.exp(-0.0004 * tt) + 0.6 * np.exp(-0.0008 * tt)  # noqa: E731
    m = ParamFit("exp2")
    p = m.predict(make([f(t)], "forecast", (50,)))
    assert abs(p.point[0, 0] - f(299.0 + 50)) < 1e-3
    assert m.n_fallback_ == 0


def test_power_recovers_power_law() -> None:
    t = np.arange(300, dtype=float)
    f = lambda tt: 1.0 - 2e-4 * tt**1.3  # noqa: E731
    m = ParamFit("power")
    p = m.predict(make([f(t)], "forecast", (50,)))
    assert abs(p.point[0, 0] - f(299.0 + 50)) < 1e-3
    assert m.n_fallback_ == 0


def test_censoring_when_never_crossing() -> None:
    y = linear_curve(100, 1e-6)
    m = ParamFit("linear", max_horizon=500)
    p = m.predict(make([y], "rul"))
    assert p.point[0, 0] == 500
    assert m.last_censored_.tolist() == [True]


def test_short_history_fallbacks() -> None:
    short = np.array([0.99, 0.98])
    long = linear_curve(50)
    sf = make([short, long], "forecast", (5,))
    m = ParamFit("linear")
    p = m.predict(sf)
    assert p.point[0, 0] == np.float32(0.98)  # persistence
    assert m.n_short_ == 1
    mr = ParamFit("linear", max_horizon=100)
    r = mr.predict(make([short, long], "rul", pad=5))
    assert r.point[0, 0] == 100 and mr.last_censored_[0]


def test_prev_soh_equals_last_valid() -> None:
    s = make([linear_curve(10), linear_curve(7)], "soh")
    p = PrevSOH().predict(s)
    assert p.point.shape == (2, 1)
    assert np.allclose(p.point[:, 0], [linear_curve(10)[-1], linear_curve(7)[-1]], atol=1e-6)


def test_conformance() -> None:
    for m in (PrevSOH(), ParamFit("exp2"), GPRExtrap()):
        assert isinstance(m, Model)
        assert m.cross_fit is False and m.tunable is False
    assert GPRExtrap.probabilistic and not ParamFit.probabilistic


def _smooth(n: int, extra: int = 0) -> np.ndarray:
    t = np.arange(n + extra, dtype=float)
    return 1.0 - 4e-4 * t - 1e-7 * t**2


def test_gpr_forecast_quantiles() -> None:
    n = 150
    full = _smooth(n, 30)
    rng = np.random.default_rng(0)
    y = full[:n] + 5e-4 * rng.standard_normal(n)
    m = GPRExtrap(fit_window=100)
    p = m.predict(make([y], "forecast", (10, 30)))
    assert p.quantiles is not None
    assert np.all(np.diff(p.quantiles[0], axis=-1) >= 0)
    lo, hi = p.quantiles[0, :, 0], p.quantiles[0, :, -1]
    truth = full[[n - 1 + 10, n - 1 + 30]]
    assert np.all((lo <= truth) & (truth <= hi))


def test_gpr_rul_quantiles_bracket_truth() -> None:
    n = 250
    full = _smooth(n + 400)
    rng = np.random.default_rng(1)
    y = full[:n] + 5e-4 * rng.standard_normal(n)
    true_step = int(np.argmax(full[n:] < THETA)) + 1
    m = GPRExtrap(fit_window=120, max_horizon=800, n_paths=100)
    p = m.predict(make([y], "rul"))
    assert p.quantiles is not None
    q = p.quantiles[0, 0]
    assert np.all(np.diff(q) >= 0)
    assert q[0] <= true_step <= q[-1]


def test_gpr_rul_point_within_quantiles() -> None:
    n = 250
    full = _smooth(n + 400)
    rng = np.random.default_rng(2)
    y = full[:n] + 5e-4 * rng.standard_normal(n)
    p = GPRExtrap(fit_window=120, max_horizon=800, n_paths=100).predict(make([y], "rul"))
    assert p.quantiles is not None
    assert p.quantiles[0, 0, 0] <= p.point[0, 0] <= p.quantiles[0, 0, -1]


def test_max_horizon_set_from_training_labels() -> None:
    train = make([linear_curve(50), linear_curve(60)], "rul")
    meta = train.meta.assign(eol_cycle=[300.0, 400.0], origin_cycle=[50, 60])
    train = SampleSet(**{**train.__dict__, "meta": meta})
    for m in (ParamFit("linear"), GPRExtrap()):
        info = m.fit(train)
        assert m.max_horizon_ == 2 * 340 == info.extra["max_horizon"]
    # no labels -> constructor fallback
    m2 = ParamFit("linear", max_horizon=777)
    m2.fit(make([linear_curve(50)], "forecast", (5,)))
    assert m2.max_horizon_ == 777
    # the censor value follows max_horizon_
    m3 = ParamFit("linear")
    m3.fit(train)
    p = m3.predict(make([linear_curve(100, 1e-7)], "rul"))
    assert p.point[0, 0] == 680


def test_gpr_short_history() -> None:
    m = GPRExtrap()
    p = m.predict(make([np.array([0.99, 0.98])], "rul"))
    assert p.point[0, 0] == m.max_horizon and m.last_censored_[0]


def test_paramfit_forecast_is_clipped_to_physical_range() -> None:
    """An exploding exp2 extrapolation must not produce absurd SOH values (NASA bug: ~1e8)."""
    from battery_rul.models.extrapolate import SOH_MAX, SOH_MIN, ParamFit

    m = ParamFit(kind="exp2")
    m._fit_one = lambda y: ((lambda t: np.exp(np.asarray(t, float))), False)  # type: ignore[method-assign]
    s = make([np.linspace(1.0, 0.9, 30)], "forecast", horizons=(1, 50, 100))
    p = m.predict(s).point
    assert np.all((p >= SOH_MIN) & (p <= SOH_MAX)) and p.max() == SOH_MAX
