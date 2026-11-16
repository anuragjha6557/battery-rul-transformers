"""Synthetic checks for features/curves.py: known ICA peak shift and known dQ(V) variance."""

from __future__ import annotations

import numpy as np
import pandas as pd

from battery_rul.features.curves import SPECS, curve_features, ica_features, resample_curve

SPEC = SPECS["calce"]
DV = 0.002


def _q_of_v(v: np.ndarray, centre: float, scale: float = 1.0) -> np.ndarray:
    """Q(V) whose dQ/dV is a Gaussian bump at ``centre`` plus a small linear background."""
    from scipy.special import erf

    sig = 0.03
    return scale * 0.5 * (1 + erf((v - centre) / (sig * np.sqrt(2)))) + 0.05 * (v - 3.7)


def _curve_rows(cell: str, cycle: int, centre: float, scale: float = 1.0) -> pd.DataFrame:
    v = np.arange(3.6, 4.2 + 1e-9, DV)
    q = _q_of_v(v, centre, scale)
    q = q - q[0]
    # CV tail: voltage flat, charge keeps growing (must be ignored)
    v = np.concatenate([v, np.full(20, 4.2)])
    q = np.concatenate([q, q[-1] + np.linspace(0.01, 0.2, 20)])
    return pd.DataFrame(
        {
            "cell_id": cell,
            "cycle_idx": cycle,
            "phase": "charge",
            "sample_idx": np.arange(len(v)),
            "voltage_v": v,
            "charge_ah": q,
        }
    )


def _family(centres: list[float], scales: list[float] | None = None) -> pd.DataFrame:
    scales = scales or [1.0] * len(centres)
    return pd.concat(
        [
            _curve_rows("A", i + 1, c, s)
            for i, (c, s) in enumerate(zip(centres, scales, strict=True))
        ],
        ignore_index=True,
    )


def test_resample_covers_grid_and_ignores_cv() -> None:
    rows = _curve_rows("A", 1, 4.0)
    q = resample_curve(rows["voltage_v"].to_numpy(), rows["charge_ah"].to_numpy(), SPEC)
    assert q is not None and len(q) == len(SPEC.grid) and q[0] == 0.0
    assert q[-1] < 1.3  # CV charge (up to +0.2 Ah) not added on top of the CC curve
    assert np.all(np.diff(q) > -1e-9)


def test_short_or_partial_curves_give_none() -> None:
    v = np.linspace(3.6, 3.95, 50)  # never reaches the top of the grid
    assert resample_curve(v, np.linspace(0, 1, 50), SPEC) is None
    assert resample_curve(v[:3], np.zeros(3), SPEC) is None
    assert resample_curve(np.full(40, np.nan), np.zeros(40), SPEC) is None


def test_ica_peak_tracks_known_shift() -> None:
    centres = [4.00, 3.98, 3.96, 3.94, 3.92, 3.90, 3.95]
    feats = curve_features(_family(centres), "calce")
    np.testing.assert_allclose(feats["chg_ica_peak_v"].to_numpy(), centres, atol=0.004)
    peak_h = feats["chg_ica_peak_h"].to_numpy()
    assert np.allclose(peak_h, 1.0 / (0.03 * np.sqrt(2 * np.pi)) + 0.05, rtol=0.05)
    assert np.all(feats["chg_ica_area"] > 0.8)


def test_dq_var_matches_known_value_and_is_causal() -> None:
    n_ref = 5
    scales = [1.0] * n_ref + [1.0, 0.9, 0.8]  # cycles 6..8 lose 0%, 10%, 20% of the bump
    centres = [3.97] * len(scales)
    feats = curve_features(_family(centres, scales), "calce")
    # no complete reference before the 5th valid cycle
    assert feats["chg_dq_var"].iloc[: n_ref - 1].isna().all()
    assert feats["chg_dq_var"].iloc[n_ref - 1] < 1e-12  # identical reference cycles
    # expected variance from the analytic grid curves
    grid = SPEC.grid
    q_ref = _q_of_v(grid, 3.97) - _q_of_v(grid, 3.97)[0]
    q_k = _q_of_v(grid, 3.97, 0.8)
    q_k = q_k - q_k[0]
    dq = q_k - q_ref
    row = feats.iloc[7]
    np.testing.assert_allclose(row["chg_dq_var"], dq.var(), rtol=0.05, atol=1e-5)
    assert row["chg_dq_min"] < 0 and np.isclose(row["chg_dq_mean"], dq.mean(), rtol=0.05, atol=1e-4)
    assert feats["chg_dq_var"].iloc[5] < feats["chg_dq_var"].iloc[6] < row["chg_dq_var"]


def test_future_cycles_do_not_change_earlier_features() -> None:
    a = _family([3.97] * 8, [1, 1, 1, 1, 1, 0.95, 0.9, 0.85])
    b = _family([3.97] * 8, [1, 1, 1, 1, 1, 0.95, 0.5, 0.2])
    fa, fb = curve_features(a, "calce"), curve_features(b, "calce")
    cols = [c for c in fa.columns if c.startswith("chg_")]
    pd.testing.assert_frame_equal(fa.loc[:5, cols], fb.loc[:5, cols])


def test_ica_all_nan_rows_stay_nan() -> None:
    out = ica_features(np.full((2, len(SPEC.grid)), np.nan), SPEC)
    assert np.isnan(out).all()


def test_toyota_discharge_prefix_and_positive_ica() -> None:
    v = np.linspace(3.5, 2.0135, 100)
    rows = []
    for cyc in range(1, 8):
        q = 1.0 / (1 + np.exp((v - 3.2) / 0.05)) * (1.1 - 0.01 * cyc)
        rows.append(
            pd.DataFrame(
                {
                    "cell_id": "T",
                    "cycle_idx": cyc,
                    "phase": "discharge",
                    "sample_idx": np.arange(100),
                    "voltage_v": v,
                    "charge_ah": q - q[0],
                }
            )
        )
    feats = curve_features(pd.concat(rows, ignore_index=True), "toyota")
    assert {"dis_ica_peak_v", "dis_dq_var"} <= set(feats.columns)
    assert not [c for c in feats.columns if c.startswith("chg_")]
    np.testing.assert_allclose(feats["dis_ica_peak_v"], 3.2, atol=0.02)
    assert (feats["dis_ica_peak_h"] > 0).all()
