"""ADR-0018 outlier policy: label rules (hindsight) and causal input rules."""

from __future__ import annotations

import numpy as np
import pandas as pd

from battery_rul.data.cleaning import (
    clean_cycles,
    input_outliers,
    isolated_glitch,
    label_outliers,
)


def _cell(n: int = 80, dataset: str = "calce", seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    k = np.arange(n)
    cap = 1.1 - 0.002 * k + 0.0005 * rng.standard_normal(n)
    return pd.DataFrame(
        {
            "dataset": dataset,
            "cell_id": "c1",
            "cycle_idx": k + 1,
            "capacity_ah": cap,
            "charge_throughput_ah": cap * 1.01,
            "charge_time_s": 3000.0 + rng.normal(0, 5, n),
            "cc_time_s": 2000.0 + rng.normal(0, 5, n),
            "cv_time_s": 1000.0 + rng.normal(0, 5, n),
            "rest_before_s": 200.0,
            "ir_ohm": 0.09 + 0.0001 * k + 0.0002 * rng.standard_normal(n),
        }
    )


def test_glitch_both_directions_but_not_regeneration() -> None:
    c = 1.0 - 0.002 * np.arange(60)
    c[20] -= 0.05  # one-cycle dip
    c[35] += 0.05  # one-cycle spike
    reg = c.copy()
    reg[45:52] += 0.04 * np.exp(-np.arange(7) / 2.0)  # regeneration: jump that decays
    g = isolated_glitch(reg)
    assert g[20] and g[35]
    assert not g[45:52].any()


def test_cv_skip_and_partial_charge_dropped() -> None:
    df = _cell()
    df.loc[10, "cv_time_s"] = 30.0
    df.loc[10, "capacity_ah"] -= 0.11
    df.loc[30, "charge_throughput_ah"] *= 0.3
    lab = label_outliers(df)
    assert lab.loc[10, "cv_skip"] and lab.loc[30, "partial_charge"]
    out, rep = clean_cycles(df)
    assert 11 not in set(out["cycle_idx"]) and 31 not in set(out["cycle_idx"])
    assert rep.n_rows_in - rep.n_rows_out == rep.label_counts["any"] >= 2


def test_cv_skip_rule_is_calce_only() -> None:
    df = _cell(dataset="toyota")
    df.loc[10, "cv_time_s"] = 0.0  # Toyota batch-3 protocol: no CV step, not an artifact
    assert not label_outliers(df).loc[10, "cv_skip"]


def test_charge_pause_masks_duration_inputs_only() -> None:
    df = _cell()
    df["fld_win_dq_ah"] = 0.5
    df["fld_win_valid"] = True  # bool flag column: must be left alone
    df.loc[40, "charge_time_s"] = 50_000.0
    out, rep = clean_cycles(df)
    row = out[out["cycle_idx"] == 41].iloc[0]
    assert rep.input_counts["charge_pause"] == 1
    assert np.isnan(row["cv_time_s"]) and np.isnan(row["fld_win_dq_ah"])
    assert np.isfinite(row["ir_ohm"]) and np.isfinite(row["capacity_ah"])


def test_robust_rule_and_physical_range() -> None:
    df = _cell()
    df.loc[50, "ir_ohm"] = 0.5  # 5x jump in a smooth physical signal
    df.loc[60, "ir_ohm"] = -1.0  # impossible value
    out, rep = clean_cycles(df)
    assert rep.input_counts["ir_ohm"] >= 1 and rep.input_counts["range:ir_ohm"] == 1
    assert out.loc[out["cycle_idx"] == 51, "ir_ohm"].isna().all()


def test_long_rest_exempts_robust_rule() -> None:
    df = _cell()
    df.loc[50, "ir_ohm"] = 0.5
    df.loc[50, "rest_before_s"] = 2 * 86400.0  # regeneration cycle: shift is expected
    assert not input_outliers(df, ["ir_ohm"])["ir_ohm"].loc[50]


def test_input_rules_are_causal() -> None:
    """Corrupting future cycles never changes the input masks of earlier cycles."""
    df = _cell()
    df.loc[40, "ir_ohm"] = 0.4
    base = input_outliers(df, ["ir_ohm"])
    bad = df.copy()
    bad.loc[bad["cycle_idx"] > 45, ["ir_ohm", "charge_time_s"]] *= 50.0
    pert = input_outliers(bad, ["ir_ohm"])
    early = df["cycle_idx"] <= 45
    for k in base:
        pd.testing.assert_series_equal(base[k][early], pert[k][early])
