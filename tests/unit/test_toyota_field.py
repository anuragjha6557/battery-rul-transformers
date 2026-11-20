"""Toyota charge-side field features on a synthetic protocol with known answers."""

from __future__ import annotations

import numpy as np

from battery_rul.data.toyota_field import (
    relaxation_features,
    segment_charge,
    window_features,
)

AH_PER_C = 1.1  # 1C = 1.1 A


def _profile(with_rest: bool = True, cc_start_v: float = 3.40) -> tuple[np.ndarray, ...]:
    """fast 4C step (10 min) -> 1 min rest -> 1C CC to 3.6 V (20 min) -> CV -> discharge."""
    dt = 1 / 60  # 1 s in minutes
    seg_t, seg_v, seg_i = [], [], []

    def add(minutes: float, v0: float, v1: float, i: float | np.ndarray) -> None:
        n = round(minutes / dt)
        seg_v.append(np.linspace(v0, v1, n))
        seg_i.append(np.full(n, i) if np.isscalar(i) else np.asarray(i))
        seg_t.append(np.full(n, dt))

    add(1, 2.5, 2.5, 0.0)  # idle before charge
    add(10, 3.30, 3.45, 4.0)
    if with_rest:
        add(1, 3.45, cc_start_v, 0.0)
    add(20, cc_start_v, 3.60, 1.0)
    n_cv = 600
    add(10, 3.60, 3.60, np.linspace(1.0, 0.05, n_cv))
    add(5, 3.2, 2.0, -4.0)
    t = np.cumsum(np.concatenate(seg_t)) - dt
    v, i = np.concatenate(seg_v), np.concatenate(seg_i)
    qc = np.concatenate([[0.0], np.cumsum(np.clip(i[1:], 0, None) * AH_PER_C * dt / 60.0)])
    return t, v, i, qc


def test_segments_found_in_protocol_order() -> None:
    t, v, i, _ = _profile()
    seg = segment_charge(t, v, i)
    assert seg is not None and seg.rest0 is not None and seg.cc0 is not None and seg.cv0 is not None
    assert seg.start < seg.rest0 <= seg.rest1 < seg.cc0 < seg.cv0 <= seg.end
    assert abs(v[seg.cv0] - 3.60) < 0.01


def test_relaxation_values() -> None:
    t, v, i, _ = _profile()
    r = relaxation_features(t, v, segment_charge(t, v, i))
    assert r["fld_relax_v0"] > r["fld_relax_v1"] and r["fld_relax_dv"] < 0
    # read at 8 s of a linear 60 s relaxation from 3.45 to 3.40 V
    assert abs(r["fld_relax_dv"] - (-0.05 * 8 / 60)) < 0.003
    assert 50 <= r["fld_relax_s"] <= 70


def test_no_rest_gives_nan_relaxation() -> None:
    t, v, i, _ = _profile(with_rest=False)
    seg = segment_charge(t, v, i)
    assert seg is not None
    assert np.isnan(relaxation_features(t, v, seg)["fld_relax_v0"])


def test_window_charge_matches_constant_current() -> None:
    t, v, i, qc = _profile()
    seg = segment_charge(t, v, i)
    w = window_features(t, v, qc, seg.cc0, seg.cv0)
    # 1C CC from 3.40 to 3.60 V over 20 min: the 3.50-3.58 V window spans 8 min at 1.1 A
    assert w["fld_win_valid"]
    assert abs(w["fld_win_dq_ah"] - AH_PER_C * 8 / 60) < 0.005
    assert abs(w["fld_win_dt_s"] - 8 * 60) < 5
    q = np.array([w[f"fld_q_v{k:02d}"] for k in range(16)])
    assert q[0] == 0 and np.all(np.diff(q) >= 0)


def test_window_not_covered_is_invalid() -> None:
    t, v, i, qc = _profile(cc_start_v=3.55)  # CC starts above the window floor
    seg = segment_charge(t, v, i)
    w = window_features(t, v, qc, seg.cc0, seg.cv0)
    assert not w["fld_win_valid"] and np.isnan(w["fld_win_dq_ah"])
