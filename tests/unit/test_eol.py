"""EOL labelling rules on synthetic SOH trajectories."""

from __future__ import annotations

import numpy as np
import pytest
from hypothesis import given
from hypothesis import strategies as st

from battery_rul.tasks.eol import (
    RULES,
    eol_masked,
    eol_raw,
    eol_rolling_median,
    eol_sustained,
)

THR = 0.8


def _fade(n: int = 100, start: float = 1.0, slope: float = 0.004) -> tuple[np.ndarray, np.ndarray]:
    cyc = np.arange(1, n + 1)
    return cyc, start - slope * (cyc - 1)


def test_monotone_fade_known_crossing() -> None:
    cyc, soh = _fade()  # soh = 1 - 0.004 (c-1); first < 0.8 at c-1 > 50 -> c = 52
    assert eol_raw(cyc, soh, THR).eol_cycle == 52
    assert eol_sustained(cyc, soh, THR).eol_cycle == 52
    res = eol_rolling_median(cyc, soh, THR)
    assert 52 <= res.eol_cycle <= 54  # type: ignore[operator]
    assert not res.censored
    assert res.rule == "rolling_median" and res.threshold == THR


def test_eol_cycle_is_cycle_idx_not_position() -> None:
    cyc, soh = _fade()
    cyc = cyc * 2 + 10  # gaps, offset
    assert eol_raw(cyc, soh, THR).eol_cycle == 52 * 2 + 10


def test_single_dip_caught_by_raw_only() -> None:
    cyc, soh = _fade()
    soh = soh.copy()
    soh[10] = 0.5  # one-cycle dip (cycle 11)
    assert eol_raw(cyc, soh, THR).eol_cycle == 11
    assert eol_sustained(cyc, soh, THR).eol_cycle == 52
    assert eol_rolling_median(cyc, soh, THR).eol_cycle != 11


def test_regeneration_spike_after_crossing() -> None:
    cyc, soh = _fade()
    soh = soh.copy()
    soh[55] = 0.9  # spike back above threshold after the crossing at cycle 52
    assert eol_raw(cyc, soh, THR).eol_cycle == 52
    # sustained requires 5 in a row, so the run starting at 52 is broken but a later one counts
    res = eol_sustained(cyc, soh, THR)
    assert res.eol_cycle == 57
    assert not res.censored


def test_censored() -> None:
    cyc, soh = _fade(n=50)
    for fn in (eol_raw, eol_rolling_median, eol_sustained):
        res = fn(cyc, soh, THR)
        assert res.eol_cycle is None and res.censored
    res = eol_masked(cyc, soh, THR, np.zeros(50, dtype=bool))
    assert res.eol_cycle is None and res.censored


def test_sustained_ignores_run_cut_by_end_of_record() -> None:
    cyc = np.arange(1, 11)
    soh = np.array([1.0] * 7 + [0.7] * 3)
    assert eol_sustained(cyc, soh, THR, n=5).censored
    assert eol_raw(cyc, soh, THR).eol_cycle == 8


def test_masked_ignores_flagged_dip() -> None:
    cyc, soh = _fade()
    soh = soh.copy()
    mask = np.zeros(len(soh), dtype=bool)
    soh[10:15] = 0.5  # 5-cycle artifact: even `sustained` is fooled
    mask[10:15] = True
    assert eol_sustained(cyc, soh, THR).eol_cycle == 11
    res = eol_masked(cyc, soh, THR, mask)
    assert res.eol_cycle == 52 and res.rule == "masked_sustained"
    assert eol_masked(cyc, soh, THR, mask, base=eol_raw).eol_cycle == 52


@pytest.mark.parametrize("fn", [eol_raw, eol_rolling_median, eol_sustained])
def test_unsorted_input_raises(fn) -> None:  # type: ignore[no-untyped-def]
    cyc, soh = _fade(n=20)
    cyc = cyc.copy()
    cyc[[3, 4]] = cyc[[4, 3]]
    with pytest.raises(ValueError):
        fn(cyc, soh, THR)
    with pytest.raises(ValueError):
        eol_masked(cyc, soh, THR, np.zeros(20, dtype=bool))


def test_rules_registry() -> None:
    assert set(RULES) == {"raw", "rolling_median", "sustained", "masked"}


@st.composite
def _trajectories(draw: st.DrawFn) -> tuple[np.ndarray, np.ndarray, float]:
    n = draw(st.integers(1, 80))
    steps = draw(st.lists(st.integers(1, 5), min_size=n, max_size=n))
    cyc = np.cumsum(steps)
    soh = np.array(
        draw(st.lists(st.floats(0.3, 1.1, allow_nan=False), min_size=n, max_size=n)), dtype=float
    )
    thr = draw(st.sampled_from([0.7, 0.8]))
    return cyc, soh, thr


@given(_trajectories())
def test_property_sustained_not_before_raw_and_in_cycle_idx(
    traj: tuple[np.ndarray, np.ndarray, float],
) -> None:
    cyc, soh, thr = traj
    raw = eol_raw(cyc, soh, thr)
    sus = eol_sustained(cyc, soh, thr)
    if raw.eol_cycle is None:
        assert sus.eol_cycle is None
    if raw.eol_cycle is not None and sus.eol_cycle is not None:
        assert sus.eol_cycle >= raw.eol_cycle
    mask = soh < 0.4
    for res in (raw, sus, eol_rolling_median(cyc, soh, thr), eol_masked(cyc, soh, thr, mask)):
        assert res.censored == (res.eol_cycle is None)
        if res.eol_cycle is not None:
            assert res.eol_cycle in set(cyc.tolist())
