"""Anomaly-flag tests on synthetic per-cycle tables."""

from __future__ import annotations

import numpy as np
import pandas as pd

from battery_rul.data.quality import FLAG_COLS, NON_CAUSAL_FLAGS, flag_anomalies


def _cycles(n: int = 60, cell: str = "X1") -> pd.DataFrame:
    k = np.arange(1, n + 1)
    return pd.DataFrame(
        {
            "dataset": "calce",
            "cell_id": cell,
            "cycle_idx": k,
            "capacity_ah": 1.1 - 0.002 * k,
            "charge_time_s": 8000.0,
            "cv_time_s": 2500.0,
            "charge_throughput_ah": 1.1 - 0.002 * k,
            "rest_before_s": 215.0,
        }
    )


def test_clean_table_has_no_flags() -> None:
    out = flag_anomalies(_cycles())
    assert list(out.columns[:3]) == ["dataset", "cell_id", "cycle_idx"]
    assert not out[list(FLAG_COLS)].to_numpy().any()
    assert (out["flag_reasons"] == "").all()


def test_each_flag_triggers() -> None:
    df = _cycles()
    df.loc[5, "charge_time_s"] = np.nan  # no paired charge
    df.loc[10, "charge_throughput_ah"] = 0.05  # partial
    df.loc[20, "cv_time_s"] = 50.0  # skipped CV
    df.loc[30, "rest_before_s"] = 1e5  # long rest
    df.loc[40, "capacity_ah"] -= 0.15  # jump (down at 40, back up at 41)
    out = flag_anomalies(df)
    assert out.loc[5, "flag_no_paired_charge"]
    assert out.loc[10, "flag_partial_charge"]
    assert out.loc[20, "flag_skipped_cv"]
    assert out.loc[30, "flag_long_rest"]
    assert out.loc[40, "flag_capacity_jump"]
    assert out.loc[20, "flag_reasons"] == "skipped_cv"
    assert out[list(FLAG_COLS)].to_numpy().sum() >= 5
    clean = out.drop(index=[5, 10, 20, 30, 40, 41])
    assert not clean[list(FLAG_COLS)].to_numpy().any()


def test_partial_charge_uses_local_not_global_reference() -> None:
    # Legit steep fade (1.0 -> 0.2 Ah) must not be flagged as partial charge.
    df = _cycles(100)
    df["capacity_ah"] = np.linspace(1.0, 0.2, 100)
    df["charge_throughput_ah"] = df["capacity_ah"]
    assert not flag_anomalies(df)["flag_partial_charge"].any()


def test_multiple_cells_and_row_order_preserved() -> None:
    a, b = _cycles(cell="A"), _cycles(cell="B")
    b.loc[7, "cv_time_s"] = 10.0
    df = pd.concat([a, b], ignore_index=True).sample(frac=1.0, random_state=0)
    out = flag_anomalies(df)
    assert out.index.equals(df.index)
    hit = out[out["flag_skipped_cv"]]
    assert list(hit["cell_id"]) == ["B"] and list(hit["cycle_idx"]) == [8]


def test_nan_features_do_not_flag() -> None:
    df = _cycles()
    df[["cv_time_s", "rest_before_s", "charge_throughput_ah"]] = np.nan
    out = flag_anomalies(df)
    assert not out[["flag_skipped_cv", "flag_long_rest", "flag_partial_charge"]].to_numpy().any()


def test_charge_pause_flag() -> None:
    df = _cycles()
    df.loc[7, "charge_time_s"] = 3.5 * 8000.0  # paused charge
    df.loc[8, "charge_time_s"] = 2.5 * 8000.0  # long but below 3x
    out = flag_anomalies(df)
    assert out["flag_charge_pause"].to_numpy().nonzero()[0].tolist() == [7]
    assert "charge_pause" in out.loc[7, "flag_reasons"]
    assert "flag_charge_pause" in FLAG_COLS


def test_non_causal_flags_membership() -> None:
    assert set(NON_CAUSAL_FLAGS) == {
        "flag_partial_charge",
        "flag_capacity_jump",
        "flag_charge_pause",  # whole-cell median reads future cycles
    }
    assert set(NON_CAUSAL_FLAGS) <= set(FLAG_COLS)
