"""Unit tests for battery_rul.eval.metrics (hand-computed vectors + properties)."""

from __future__ import annotations

import math

import numpy as np
import pytest
from hypothesis import given, settings
from hypothesis import strategies as st
from hypothesis.extra.numpy import arrays
from scipy import stats as sps

from battery_rul.eval import metrics as m

_fin = st.floats(min_value=-5, max_value=5, allow_nan=False, allow_infinity=False)


# ---------------------------------------------------------------- SOH errors
def test_rmse_mae_hand() -> None:
    # errors (pred - true) = -0.1, 0.0 ; rmse = sqrt((0.01 + 0)/2) = 0.070711 -> 7.0711 %
    # mae = (0.1 + 0)/2 = 0.05 -> 5 %
    t, p = [1.0, 0.9], [0.9, 0.9]
    assert m.rmse_pct(t, p) == pytest.approx(math.sqrt(0.005) * 100)
    assert m.mae_pct(t, p) == pytest.approx(5.0)


def test_horizon_errors_hand_and_empty_horizon() -> None:
    t = np.array([[1.0, 0.9, 0.8], [0.8, 0.7, 0.6]])
    p = np.array([[0.9, 0.9, 0.0], [0.8, 0.6, 0.0]])
    mask = np.array([[True, True, False], [True, True, False]])
    # h=1: errors -0.1, 0   -> rmse sqrt(0.005)*100, mae 5
    # h=10: errors 0, -0.1  -> same
    # h=50: no valid entries -> NaN
    out = m.horizon_errors(t, p, mask, [1, 10, 50])
    assert out[1]["rmse"] == pytest.approx(math.sqrt(0.005) * 100)
    assert out[1]["mae"] == pytest.approx(5.0)
    assert out[10]["mae"] == pytest.approx(5.0)
    assert math.isnan(out[50]["rmse"]) and math.isnan(out[50]["mae"]) and out[50]["n"] == 0


def test_horizon_errors_masked_nan_allowed_unmasked_nan_raises() -> None:
    t = np.array([[1.0, np.nan]])
    p = np.array([[1.0, np.nan]])
    out = m.horizon_errors(t, p, np.array([[True, False]]), [1, 10])
    assert out[1]["rmse"] == 0.0
    with pytest.raises(ValueError):
        m.horizon_errors(t, p, np.array([[True, True]]), [1, 10])


def test_horizon_errors_validation() -> None:
    a = np.zeros((2, 2))
    ok = np.ones((2, 2), dtype=bool)
    with pytest.raises(ValueError):
        m.horizon_errors(a, a, ok, [1])  # wrong number of horizons
    with pytest.raises(ValueError):
        m.horizon_errors(a, a, ok, [1, 1])  # duplicates
    with pytest.raises(ValueError):
        m.horizon_errors(a, np.zeros((2, 3)), ok, [1, 2])
    with pytest.raises(ValueError):
        m.horizon_errors(a, a, ok.astype(int), [1, 2])
    with pytest.raises(ValueError):
        m.horizon_errors(np.zeros(2), np.zeros(2), np.ones(2, bool), [1, 2])
    with pytest.raises(ValueError):
        m.horizon_errors(np.zeros((0, 2)), np.zeros((0, 2)), np.zeros((0, 2), bool), [1, 2])


def test_point_metric_input_validation() -> None:
    with pytest.raises(ValueError):
        m.rmse_pct([1.0, np.nan], [1.0, 1.0])
    with pytest.raises(ValueError):
        m.mae_pct([1.0, 1.0], [1.0, np.inf])
    with pytest.raises(ValueError):
        m.rmse_pct([1.0], [1.0, 2.0])
    with pytest.raises(ValueError):
        m.rmse_pct([], [])
    with pytest.raises(ValueError):
        m.rmse_pct([[1.0]], [[1.0]])


@settings(max_examples=100)
@given(st.data())
def test_rmse_ge_mae(data: st.DataObject) -> None:
    n = data.draw(st.integers(1, 30))
    t = data.draw(arrays(np.float64, n, elements=_fin))
    p = data.draw(arrays(np.float64, n, elements=_fin))
    assert m.rmse_pct(t, p) >= m.mae_pct(t, p) - 1e-9


# ---------------------------------------------------------------- RUL
def test_rul_errors_hand() -> None:
    # true [100, 50], pred [110, 40] -> e = +10, -10 ; mae 10 ; bias 0 ; rel = (0.1 + 0.2)/2
    r = m.rul_errors([100, 50], [110, 40])
    assert (r.mae, r.bias, r.n) == (pytest.approx(10.0), pytest.approx(0.0), 2)
    assert r.rel_mae == pytest.approx(0.15)
    # late (optimistic) prediction -> positive bias
    assert m.rul_errors([100], [130]).bias == pytest.approx(30.0)


def test_rul_errors_requires_positive_truth() -> None:
    with pytest.raises(ValueError):
        m.rul_errors([0, 10], [1, 10])
    with pytest.raises(ValueError):
        m.rul_errors([10, np.nan], [1, 10])


def test_alpha_lambda_hand() -> None:
    # true [100, 50, 10], pred [120, 40, 13], alpha 0.2:
    # |e| = 20 <= 20 yes (boundary), 10 <= 10 yes (boundary), 3 <= 2 no -> 2/3
    assert m.alpha_lambda_accuracy([100, 50, 10], [120, 40, 13]) == pytest.approx(2 / 3)
    with pytest.raises(ValueError):
        m.alpha_lambda_accuracy([0.0], [1.0])
    with pytest.raises(ValueError):
        m.alpha_lambda_accuracy([1.0], [1.0], alpha=0.0)


@settings(max_examples=100)
@given(st.data())
def test_alpha_lambda_in_unit_interval_and_monotone(data: st.DataObject) -> None:
    n = data.draw(st.integers(1, 20))
    t = data.draw(arrays(np.float64, n, elements=st.floats(1, 1000)))
    p = data.draw(arrays(np.float64, n, elements=st.floats(-1000, 2000)))
    a1 = data.draw(st.floats(0.01, 0.98))
    a2 = data.draw(st.floats(a1, 0.99))
    v1 = m.alpha_lambda_accuracy(t, p, a1)
    v2 = m.alpha_lambda_accuracy(t, p, a2)
    assert 0.0 <= v1 <= v2 <= 1.0


def test_prognostic_horizon_hand() -> None:
    tp = [100, 200, 300, 400]
    true = [400, 300, 200, 100]  # eol = 500
    # bounds 0.2*true = 80, 60, 40, 20
    # pred errors: -100 (bad), +10 (ok), -10 (ok), +5 (ok) -> earliest t_p = 200 -> 500 - 200
    assert m.prognostic_horizon(tp, true, [300, 310, 190, 105], 500) == 300
    # errors: ok, bad (t_p=200), ok, ok -> earliest all-later-ok is 300 -> 200
    assert m.prognostic_horizon(tp, true, [400, 100, 190, 105], 500) == 200
    # all ok -> first t_p -> 400
    assert m.prognostic_horizon(tp, true, true, 500) == 400
    # last fails -> NaN
    assert math.isnan(m.prognostic_horizon(tp, true, [400, 300, 200, 150], 500))
    # unsorted input is sorted internally
    assert m.prognostic_horizon(tp[::-1], true[::-1], [105, 190, 310, 300], 500) == 300


def test_prognostic_horizon_validation() -> None:
    with pytest.raises(ValueError):
        m.prognostic_horizon([1, 2], [5], [5], 10)
    with pytest.raises(ValueError):
        m.prognostic_horizon([1], [-1], [1], 10)
    with pytest.raises(ValueError):
        m.prognostic_horizon([1], [1], [1], float("nan"))


# ---------------------------------------------------------------- uncertainty
def test_picp_mpiw_hand() -> None:
    y = [1, 2, 3, 4]
    lo = [0, 2.5, 2, 4]
    hi = [2, 3, 4, 5]
    # inside: yes, no (2 < 2.5), yes, yes (boundary) -> 0.75 ; widths 2, .5, 2, 1 -> 1.375
    assert m.picp(y, lo, hi) == 0.75
    assert m.mpiw(lo, hi) == pytest.approx(1.375)
    with pytest.raises(ValueError):
        m.picp([1.0], [2.0], [1.0])  # lo > hi
    with pytest.raises(ValueError):
        m.mpiw([1.0, 2.0], [2.0])


def test_pinball_hand() -> None:
    # y=1; q(0.1)=0 -> 0.1*(1-0)=0.1 ; q(0.9)=2 -> d=-1: max(-0.9, 0.1)=0.1 -> mean 0.1
    assert m.pinball_loss([1.0], [[0.0, 2.0]], [0.1, 0.9]) == pytest.approx(0.1)
    with pytest.raises(ValueError):
        m.pinball_loss([1.0], [[0.0, 2.0]], [0.1])
    with pytest.raises(ValueError):
        m.pinball_loss([1.0], [[0.0, 2.0]], [0.0, 1.0])


def test_crps_hand() -> None:
    # y=0, samples {-1, 1}: E|X-y| = 1 ; 0.5*E|X-X'| = 0.5*(0+2+2+0)/4 = 0.5 -> 0.5
    assert m.crps_from_samples([0.0], [[-1.0, 1.0]]) == pytest.approx(0.5)


@pytest.mark.parametrize("s", [1, 2, 50, 200, 201, 500])
def test_crps_matches_properscoring(s: int) -> None:
    ps = pytest.importorskip("properscoring")
    rng = np.random.default_rng(s)
    y = rng.normal(size=17)
    x = rng.normal(loc=0.3, scale=1.4, size=(17, s))
    ref = float(np.mean(ps.crps_ensemble(y, x)))
    assert m.crps_from_samples(y, x) == pytest.approx(ref, abs=1e-10)


def test_crps_exact_and_sorted_agree() -> None:
    rng = np.random.default_rng(1)
    y = rng.normal(size=5)
    x = rng.normal(size=(5, 60))
    assert np.allclose(m._crps_exact_rows(y, x), m._crps_sorted_rows(y, x), atol=1e-12)


def test_crps_validation() -> None:
    with pytest.raises(ValueError):
        m.crps_from_samples([0.0, 1.0], [[0.0, 1.0]])
    with pytest.raises(ValueError):
        m.crps_from_samples([0.0], [[np.nan, 1.0]])


def test_crps_from_quantiles_close_to_gaussian_closed_form() -> None:
    n_q = 999
    tau = (np.arange(n_q) + 0.5) / n_q
    y = 0.3
    q = np.tile(sps.norm.ppf(tau), (1, 1))
    z = y
    closed = z * (2 * sps.norm.cdf(z) - 1) + 2 * sps.norm.pdf(z) - 1 / math.sqrt(math.pi)
    assert m.crps_from_quantiles([y], q, tau) == pytest.approx(closed, abs=5e-3)


def test_rearrange_and_crossing_rate() -> None:
    q = np.array([[1.0, 3.0, 2.0], [1.0, 2.0, 3.0]])
    assert m.quantile_crossing_rate(q) == 0.5
    r = m.rearrange_quantiles(q)
    assert r.tolist() == [[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]
    assert m.quantile_crossing_rate(r) == 0.0
    assert q[0, 1] == 3.0  # input untouched
