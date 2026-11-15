"""Unit tests for battery_rul.eval.stats."""

from __future__ import annotations

import logging

import numpy as np
import pandas as pd
import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from battery_rul.eval import stats as s


@settings(max_examples=30, deadline=None)
@given(
    st.lists(st.floats(-100, 100), min_size=1, max_size=6),
    st.integers(1, 5),
)
def test_bootstrap_ci_contains_estimate_for_constant_per_cell(
    vals: list[float], n_seeds: int
) -> None:
    data = {f"c{i}": np.full(n_seeds, v) for i, v in enumerate(vals)}
    ci = s.cluster_bootstrap_ci(data, n_boot=500, seed=1)
    assert ci.lo - 1e-9 <= ci.estimate <= ci.hi + 1e-9
    assert ci.n_clusters == len(vals)


def test_bootstrap_deterministic_and_hand_case() -> None:
    data = {"a": np.array([1.0, 1.0]), "b": np.array([3.0, 3.0])}
    c1 = s.cluster_bootstrap_ci(data, n_boot=2000, seed=7)
    c2 = s.cluster_bootstrap_ci(data, n_boot=2000, seed=7)
    assert c1 == c2
    # means over resampled cells in {1, 2, 3}; estimate 2; 95 % percentile CI spans [1, 3]
    assert (c1.estimate, c1.lo, c1.hi) == (2.0, 1.0, 3.0)
    med = s.cluster_bootstrap_ci(data, stat=np.median, n_boot=100)
    assert med.estimate == 2.0


def test_bootstrap_validation() -> None:
    with pytest.raises(ValueError):
        s.cluster_bootstrap_ci({})
    with pytest.raises(ValueError):
        s.cluster_bootstrap_ci({"a": np.array([np.nan])})
    with pytest.raises(ValueError):
        s.cluster_bootstrap_ci({"a": np.array([])})
    with pytest.raises(ValueError):
        s.cluster_bootstrap_ci({"a": [1.0]}, n_boot=0)
    with pytest.raises(ValueError):
        s.cluster_bootstrap_ci({"a": [1.0]}, level=1.0)


def test_direction_consistency_hand() -> None:
    model = {"a": [1.0, 1.0], "b": [2.0, 4.0], "c": [5.0, 5.0]}
    base = {"a": [2.0, 2.0], "b": [3.0, 3.0], "c": [5.0, 5.0]}
    # cell means: a 1<2 yes; b 3 vs 3 tie no; c tie no -> k_cells 1
    # pairs: a 2/2 ; b (2<3 yes, 4<3 no) 1 ; c 0 -> k_pairs 3 of 6
    r = s.direction_consistency(model, base)
    assert (r.k_cells, r.n_cells, r.k_pairs, r.n_pairs) == (1, 3, 3, 6)
    r2 = s.direction_consistency(model, base, lower_is_better=False)
    # higher is better: a no, b tie, c tie -> 0 cells; pairs: b (4>3) -> 1
    assert (r2.k_cells, r2.k_pairs) == (0, 1)


def test_direction_consistency_validation() -> None:
    with pytest.raises(ValueError):
        s.direction_consistency({"a": [1.0]}, {"b": [1.0]})
    with pytest.raises(ValueError):
        s.direction_consistency({"a": [1.0, 2.0]}, {"a": [1.0]})


def test_holm_hand() -> None:
    # raw [0.01, 0.04, 0.03], m=3: sorted .01,.03,.04 -> 0.03, 0.06, 0.04 -> cummax 0.03, .06, .06
    assert s.holm_adjust([0.01, 0.04, 0.03]).tolist() == pytest.approx([0.03, 0.06, 0.06])
    assert s.holm_adjust([0.9, 0.8]).tolist() == [1.0, 1.0]
    with pytest.raises(ValueError):
        s.holm_adjust([1.5])
    with pytest.raises(ValueError):
        s.holm_adjust([])


@settings(max_examples=100)
@given(st.lists(st.floats(0, 1), min_size=1, max_size=15))
def test_holm_properties(p: list[float]) -> None:
    raw = np.array(p)
    adj = s.holm_adjust(raw)
    assert np.all(adj >= raw - 1e-15) and np.all(adj <= 1.0)
    order = np.argsort(raw, kind="stable")
    assert np.all(np.diff(adj[order]) >= -1e-15)


def test_wilcoxon_vs_baseline() -> None:
    base = np.zeros(8)
    better = base + np.arange(1, 9) * 0.1  # all diffs positive, exact p = 2/2^8
    same = base.copy()  # all diffs zero -> raw p = 1
    out = s.wilcoxon_vs_baseline(base, {"x": better, "same": same})
    # Holm with m=2: smallest raw 2/256 * 2 = 1/64 ; the other raw 1.0
    assert out["x"] == pytest.approx(1 / 64)
    assert out["same"] == 1.0
    assert list(out) == ["x", "same"]


def test_wilcoxon_validation() -> None:
    with pytest.raises(ValueError):
        s.wilcoxon_vs_baseline(np.zeros(3), {"x": np.zeros(4)})
    with pytest.raises(ValueError):
        s.wilcoxon_vs_baseline(np.zeros(3), {})
    with pytest.raises(ValueError):
        s.wilcoxon_vs_baseline(np.array([np.nan, 1.0]), {"x": np.zeros(2)})
    with pytest.raises(ValueError):
        s.wilcoxon_vs_baseline(np.zeros(2), {"x": np.array([np.nan, 1.0])})
    with pytest.raises(ValueError):
        s.wilcoxon_vs_baseline(np.array([]), {"x": np.array([])})


def test_mean_rank_hand_ties_and_direction() -> None:
    df = pd.DataFrame({"c1": [1.0, 2.0, 3.0], "c2": [2.0, 2.0, 1.0]}, index=["A", "B", "C"])
    # c1 ranks A1 B2 C3 ; c2: C=1, A/B tie -> 2.5 each. mean: A 1.75, B 2.25, C 2.0
    r = s.mean_rank(df)
    assert r.to_dict() == pytest.approx({"A": 1.75, "B": 2.25, "C": 2.0})
    # higher is better: c1 A3 B2 C1 ; c2: A/B tie for rank 1.5, C 3 -> A 2.25, B 1.75, C 2.0
    r2 = s.mean_rank(df, lower_is_better=False)
    assert r2.to_dict() == pytest.approx({"A": 2.25, "B": 1.75, "C": 2.0})


def test_mean_rank_nan_skipped_and_logged(caplog: pytest.LogCaptureFixture) -> None:
    df = pd.DataFrame({"c1": [1.0, 2.0, 3.0], "c2": [2.0, np.nan, 1.0]}, index=["A", "B", "C"])
    with caplog.at_level(logging.WARNING):
        r = s.mean_rank(df)
    # c2 ranks only A, C: C=1, A=2 -> B mean is just its c1 rank 2
    assert r.to_dict() == pytest.approx({"A": 1.5, "B": 2.0, "C": 2.0})
    assert r.attrs["n_missing"] == {"A": 0, "B": 1, "C": 0}
    assert "skipped" in caplog.text
    with pytest.raises(ValueError):
        s.mean_rank(pd.DataFrame())
