"""Field (BMS-measurable) feature extraction: synthetic profiles with known answers."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from battery_rul.features import field as fld


def _cc(v0: float, v1: float, i: float = 1.5, n: int = 200):
    t = np.linspace(0.0, 3000.0, n)
    v = np.linspace(v0, v1, n)
    return t, v, np.full(n, i)


def test_window_constant_current_dq_is_i_dt() -> None:
    t, v, i = _cc(3.6, 4.2)
    f, valid = fld.window_features(t, v, i)
    assert valid
    dt = (fld.V_HI - fld.V_LO) / 0.6 * 3000.0
    assert f["fld_win_dt_s"] == pytest.approx(dt, rel=1e-3)
    assert f["fld_win_dq_ah"] == pytest.approx(1.5 * dt / 3600.0, rel=1e-3)


def test_q_grid_starts_at_zero_and_is_monotone() -> None:
    t, v, i = _cc(3.5, 4.2)
    v = v + 0.002 * np.sin(np.arange(len(v)))  # small non-monotone voltage noise
    f, valid = fld.window_features(t, v, i)
    q = np.array([f[c] for c in fld.Q_COLS])
    assert valid and q[0] == 0.0 and (np.diff(q) >= 0).all()
    assert q[-1] == pytest.approx(f["fld_win_dq_ah"])


def test_window_not_covered_is_invalid() -> None:
    t, v, i = _cc(3.95, 4.2)  # starts above the window floor
    f, valid = fld.window_features(t, v, i)
    assert not valid and all(np.isnan(x) for x in f.values())
    t, v, i = _cc(3.5, 4.0)  # never reaches the window top
    assert not fld.window_features(t, v, i)[1]


def test_window_ignores_pulse_and_rest_samples() -> None:
    t, v, i = _cc(3.6, 4.2)
    t = np.concatenate([[-6.0, -3.0], t])
    v = np.concatenate([[3.64, 3.4], v])
    i = np.concatenate([[0.0, -4.0], i])
    f, valid = fld.window_features(t, v, i)
    assert valid and f["fld_win_dq_ah"] > 0


def test_pulse_resistance_and_spike() -> None:
    v = np.array([3.60, 3.60 - 4.0 * 0.09, 4.0])
    i = np.array([0.0, -4.0, 1.5])
    assert fld.pulse_resistance(v, i) == pytest.approx(0.09)
    assert np.isnan(fld.pulse_resistance(np.array([8.2, 3.2, 4.0]), i))  # sensor spike
    assert np.isnan(fld.pulse_resistance(np.array([3.6, 2.0, 4.0]), i))  # 0.4 Ohm: too large
    assert np.isnan(fld.pulse_resistance(np.array([3.6, 3.599, 4.0]), i))  # implausibly small


def test_nasa_relaxation_spike_is_nan() -> None:
    t = np.array([0.0, 3.0, 6.0])
    i = np.array([0.0, -4.0, 1.5])
    ok = fld.relaxation_features("nasa", t, np.array([3.64, 3.3, 4.0]), i, 640.0)
    assert ok[0] == ok[1] == pytest.approx(3.64) and np.isnan(ok[2]) and ok[3] == 640.0
    bad = fld.relaxation_features("nasa", t, np.array([8.2, 3.3, 4.0]), i, 640.0)
    assert all(np.isnan(x) for x in bad)


def test_calce_relaxation_dv_sign_and_duration() -> None:
    t = np.arange(0.0, 400.0, 10.0)
    i = np.full(len(t), 0.55)
    v = np.linspace(3.6, 4.19, len(t))
    rest = slice(20, 29)  # 90 s rest, voltage relaxes downward
    i[rest] = 0.0
    v[rest] = np.linspace(4.12, 4.10, 9)
    v0, v1, dv, s = fld.relaxation_features("calce", t, v, i)
    assert (v0, v1) == pytest.approx((4.12, 4.10))
    assert dv < 0 and dv == pytest.approx(v1 - v0)
    assert s == pytest.approx(80.0)


def test_calce_no_rest_is_nan() -> None:
    t = np.arange(0.0, 400.0, 10.0)
    out = fld.relaxation_features("calce", t, np.linspace(3.6, 4.2, len(t)), np.full(len(t), 0.55))
    assert all(np.isnan(x) for x in out)


@pytest.mark.data
def test_real_nasa_b0005() -> None:
    root = Path("/Users/anuragjha/RUL_project/data/processed")
    if not (root / "nasa" / "curves.parquet").exists():
        pytest.skip("processed NASA data not available")
    df = fld.build_field_features("nasa", root)
    b = df[df.cell_id == "B0005"]
    assert b["fld_win_valid"].mean() > 0.9
    assert b["fld_r_dc"].dropna().between(0.05, 0.15).all()
    assert b.loc[b.cycle_idx == 31, "fld_relax_v0"].isna().all()
