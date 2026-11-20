"""Executable leakage rules (PROTOCOL.md §4). Each test corrupts data a model must not see and
asserts that every model input is bit-identical. Rules 6 (tuning provenance) and 7 (calibration
disjointness) are enforced in the runner / UQ modules and tested there."""

from __future__ import annotations

import ast
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from battery_rul.data.schema import add_soh, empty_optional_features
from battery_rul.tasks.samples import (
    CHARGE_CHANNELS,
    TaskSpec,
    build_samples,
    is_charge_channel,
    prepare_cycles,
)

CELLS = ("C1", "C2", "C3")
N = 60
NAN_AT = {10, 25, 39}


def _cycles(seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    for j, cell in enumerate(CELLS):
        cap = 1.1 - 0.004 * np.arange(N) * (1 + 0.2 * j) + 0.003 * rng.standard_normal(N)
        for k in range(N):
            rows.append(
                {
                    "dataset": "calce",
                    "cell_id": cell,
                    "cycle_idx": k + 1,
                    "capacity_ah": cap[k],
                    "charge_time_s": 3000 + 10 * k + rng.normal(0, 5),
                    "cc_time_s": 2000 - 5 * k + rng.normal(0, 5),
                    "cv_time_s": 1000 + 15 * k,
                    "charge_throughput_ah": cap[k] * 1.01,
                    # NaN gaps exactly at the rule-2 cut-offs: a backward fill would pull the
                    # (corrupted) future value into the past, a forward fill never does.
                    "ir_ohm": np.nan if k + 1 in NAN_AT else 0.09 + 0.0002 * k,
                    "rest_before_s": 200.0 if k else np.nan,
                    "discharge_time_s": cap[k] / 1.1 * 3600,
                    "discharge_energy_wh": cap[k] * 3.7,
                }
            )
    return add_soh(empty_optional_features(pd.DataFrame(rows)))


EOL = pd.DataFrame({"cell_id": list(CELLS), "eol_cycle": [50.0, 45.0, 40.0]})
TRAIN, TEST = ("C1", "C2"), ("C3",)


def _inputs(cycles: pd.DataFrame, task: str, cells: tuple[str, ...] = TEST, fs: str = "mc"):
    prep = prepare_cycles(cycles, TRAIN, fs)  # type: ignore[arg-type]
    spec = TaskSpec(task=task, lookback=8, horizons=(1, 5))  # type: ignore[arg-type]
    return build_samples(prep, cells, EOL, spec)


# Rule 1 -------------------------------------------------------------------------------------
def test_rule1_scaler_ignores_test_cells() -> None:
    base = prepare_cycles(_cycles(), TRAIN, "mc").scaler
    bad = _cycles()
    test_rows = bad["cell_id"].isin(TEST)
    bad.loc[test_rows, list(CHARGE_CHANNELS[:4])] *= 1000.0
    pert = prepare_cycles(bad, TRAIN, "mc").scaler
    assert base is not None and pert is not None
    pd.testing.assert_series_equal(base.mean_, pert.mean_)
    pd.testing.assert_series_equal(base.scale_, pert.scale_)


# Rule 2 -------------------------------------------------------------------------------------
@pytest.mark.parametrize("task", ["soh", "forecast", "rul"])
@pytest.mark.parametrize("k", [10, 25, 39])
def test_rule2_no_future_inputs(task: str, k: int) -> None:
    clean = _inputs(_cycles(), task)
    bad = _cycles()
    future = (bad["cell_id"] == "C3") & (bad["cycle_idx"] > k)
    num = bad.select_dtypes("number").columns.drop("cycle_idx")
    bad.loc[future, num] = bad.loc[future, num] * -7.0 + 3.0
    pert = _inputs(bad, task)
    sel_c = (clean.meta["origin_cycle"] <= k).to_numpy()
    sel_p = (pert.meta["origin_cycle"] <= k).to_numpy()
    assert sel_c.sum() > 0 and sel_c.sum() == sel_p.sum()
    np.testing.assert_array_equal(clean.x_hist[sel_c], pert.x_hist[sel_p])
    np.testing.assert_array_equal(clean.x_tab[sel_c], pert.x_tab[sel_p])


@pytest.mark.parametrize("task", ["soh", "forecast", "rul"])
@pytest.mark.parametrize("k", [10, 25, 39])
def test_shared_rule2_no_future_inputs(task: str, k: int) -> None:
    clean = _inputs(_cycles(), task, fs="shared")
    bad = _cycles()
    future = (bad["cell_id"] == "C3") & (bad["cycle_idx"] > k)
    num = bad.select_dtypes("number").columns.drop("cycle_idx")
    bad.loc[future, num] = bad.loc[future, num] * -7.0 + 3.0
    pert = _inputs(bad, task, fs="shared")
    sel_c = (clean.meta["origin_cycle"] <= k).to_numpy()
    sel_p = (pert.meta["origin_cycle"] <= k).to_numpy()
    assert sel_c.sum() > 0 and sel_c.sum() == sel_p.sum()
    np.testing.assert_array_equal(clean.x_hist[sel_c], pert.x_hist[sel_p])
    np.testing.assert_array_equal(clean.x_tab[sel_c], pert.x_tab[sel_p])


def test_shared_task_a_current_cycle_features_are_charge_only() -> None:
    s = _inputs(_cycles(), "soh", fs="shared")
    now = [f.removeprefix("now_") for f in s.feature_names if f.startswith("now_")]
    assert now and set(now) <= set(CHARGE_CHANNELS)
    assert not set(s.channel_names) & {"discharge_time_s", "discharge_energy_wh"}


# Rule 3 -------------------------------------------------------------------------------------
@pytest.mark.parametrize("k", [10, 30])
def test_rule3_task_a_ignores_target_cycle_capacity_and_discharge(k: int) -> None:
    clean = _inputs(_cycles(), "soh")
    bad = _cycles()
    row = (bad["cell_id"] == "C3") & (bad["cycle_idx"] == k)
    for col in ("capacity_ah", "soh", "discharge_time_s", "discharge_energy_wh"):
        bad.loc[row, col] = bad.loc[row, col] * 0.5
    pert = _inputs(bad, "soh")
    i = int(np.flatnonzero(clean.meta["origin_cycle"].to_numpy() == k)[0])
    np.testing.assert_array_equal(clean.x_hist[i], pert.x_hist[i])
    np.testing.assert_array_equal(clean.x_tab[i], pert.x_tab[i])
    assert clean.y[i, 0] != pert.y[i, 0]  # the target itself did change


def test_rule3_task_a_current_cycle_features_are_charge_only() -> None:
    s = _inputs(_cycles(), "soh")
    now = [f.removeprefix("now_") for f in s.feature_names if f.startswith("now_")]
    assert now and set(now) <= set(CHARGE_CHANNELS)


# Rule 4 -------------------------------------------------------------------------------------
@pytest.mark.parametrize("task", ["soh", "forecast", "rul"])
def test_rule4_no_absolute_age_inputs(task: str) -> None:
    s = _inputs(_cycles(), task)
    names = {*s.channel_names, *s.feature_names}
    assert not {n for n in names if "cycle" in n or "cell" in n or "origin" in n or "age" in n}


def test_rule4_shifting_cycle_index_changes_nothing() -> None:
    """Relabelling cycle_idx (age) must not change inputs: models never see it."""
    clean = _inputs(_cycles(), "forecast")
    shifted = _cycles()
    shifted["cycle_idx"] += 1000
    eol_shift = EOL.assign(eol_cycle=EOL["eol_cycle"] + 1000)
    prep = prepare_cycles(shifted, TRAIN, "mc")
    pert = build_samples(
        prep, TEST, eol_shift, TaskSpec(task="forecast", lookback=8, horizons=(1, 5))
    )
    np.testing.assert_array_equal(clean.x_hist, pert.x_hist)
    np.testing.assert_array_equal(clean.x_tab, pert.x_tab)


# Rule 5 -------------------------------------------------------------------------------------
SRC = Path(__file__).resolve().parents[2] / "src" / "battery_rul"


def _imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text())
    mods: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            mods.add(node.module)
        elif isinstance(node, ast.Import):
            mods |= {a.name for a in node.names}
    return mods


@pytest.mark.parametrize(
    "path", [*sorted((SRC / "features").glob("*.py")), SRC / "tasks" / "samples.py"]
)
def test_rule5_feature_code_never_imports_label_code(path: Path) -> None:
    banned = {"battery_rul.tasks.labels", "battery_rul.tasks.eol", "battery_rul.data.quality"}
    assert not (_imports(path) & banned), f"{path.name} imports hindsight label/flag code"


# mc_curve (physics-informed curve features) ---------------------------------------------------
def _curve_cycles(seed: int = 0) -> pd.DataFrame:
    """Cycles plus synthetic chg_* (charge-curve) and dis_* (discharge-curve) columns."""
    df = _cycles(seed)
    rng = np.random.default_rng(seed + 1)
    k = df["cycle_idx"].to_numpy(dtype=float)
    df["chg_ica_peak_v"] = 4.0 - 0.0005 * k + 0.001 * rng.standard_normal(len(df))
    df["chg_dq_var"] = 0.001 * k + 0.0001 * rng.standard_normal(len(df))
    df.loc[df["cycle_idx"].isin(NAN_AT), "chg_dq_var"] = np.nan
    df["dis_ica_peak_v"] = 3.2 - 0.0004 * k + 0.001 * rng.standard_normal(len(df))
    df["dis_dq_var"] = 0.002 * k + 0.0001 * rng.standard_normal(len(df))
    return df


def _curve_inputs(cycles: pd.DataFrame, task: str):
    prep = prepare_cycles(cycles, TRAIN, "mc_curve")
    spec = TaskSpec(task=task, lookback=8, horizons=(1, 5), feature_set="mc_curve")  # type: ignore[arg-type]
    return build_samples(prep, TEST, EOL, spec)


def test_mc_curve_task_a_now_has_chg_but_never_dis() -> None:
    s = _curve_inputs(_curve_cycles(), "soh")
    now = [f.removeprefix("now_") for f in s.feature_names if f.startswith("now_")]
    assert {"chg_ica_peak_v", "chg_dq_var"} <= set(now)
    assert not [c for c in now if c.startswith("dis_")]
    assert all(is_charge_channel(c) for c in now)
    assert {"dis_ica_peak_v", "dis_dq_var"} <= set(s.channel_names)  # history only


@pytest.mark.parametrize("k", [10, 30])
def test_mc_curve_task_a_ignores_target_cycle_discharge_curve(k: int) -> None:
    clean = _curve_inputs(_curve_cycles(), "soh")
    bad = _curve_cycles()
    row = (bad["cell_id"] == "C3") & (bad["cycle_idx"] == k)
    for col in ("dis_ica_peak_v", "dis_dq_var", "capacity_ah", "soh"):
        bad.loc[row, col] = bad.loc[row, col] * 0.5 + 1.0
    pert = _curve_inputs(bad, "soh")
    i = int(np.flatnonzero(clean.meta["origin_cycle"].to_numpy() == k)[0])
    np.testing.assert_array_equal(clean.x_hist[i], pert.x_hist[i])
    np.testing.assert_array_equal(clean.x_tab[i], pert.x_tab[i])


def test_mc_curve_task_a_uses_current_cycle_charge_curve() -> None:
    """Positive control: the chg_* value of cycle k IS an input (so the test above can bite)."""
    clean = _curve_inputs(_curve_cycles(), "soh")
    bad = _curve_cycles()
    row = (bad["cell_id"] == "C3") & (bad["cycle_idx"] == 30)
    bad.loc[row, "chg_ica_peak_v"] += 0.5
    pert = _curve_inputs(bad, "soh")
    i = int(np.flatnonzero(clean.meta["origin_cycle"].to_numpy() == 30)[0])
    assert not np.array_equal(clean.x_tab[i], pert.x_tab[i])


@pytest.mark.parametrize("task", ["soh", "forecast", "rul"])
@pytest.mark.parametrize("k", [10, 25, 39])
def test_mc_curve_rule2_no_future_inputs(task: str, k: int) -> None:
    clean = _curve_inputs(_curve_cycles(), task)
    bad = _curve_cycles()
    future = (bad["cell_id"] == "C3") & (bad["cycle_idx"] > k)
    num = bad.select_dtypes("number").columns.drop("cycle_idx")
    bad.loc[future, num] = bad.loc[future, num] * -7.0 + 3.0
    pert = _curve_inputs(bad, task)
    sel_c = (clean.meta["origin_cycle"] <= k).to_numpy()
    sel_p = (pert.meta["origin_cycle"] <= k).to_numpy()
    assert sel_c.sum() > 0 and sel_c.sum() == sel_p.sum()
    np.testing.assert_array_equal(clean.x_hist[sel_c], pert.x_hist[sel_p])
    np.testing.assert_array_equal(clean.x_tab[sel_c], pert.x_tab[sel_p])


def test_mc_curve_requires_curve_columns_and_mc_ignores_them() -> None:
    with pytest.raises(ValueError, match="curve features"):
        prepare_cycles(_cycles(), TRAIN, "mc_curve")
    a = prepare_cycles(_curve_cycles(), TRAIN, "mc")
    assert not [c for c in a.channels if c.startswith(("chg_", "dis_"))]


# ADR-0016: known-future rest covariates ------------------------------------------------------
def _fr_inputs(cycles: pd.DataFrame, future_rest: bool = True):
    prep = prepare_cycles(cycles, TRAIN, "mc")
    spec = TaskSpec(task="forecast", lookback=8, horizons=(1, 5), future_rest=future_rest)
    return build_samples(prep, TEST, EOL, spec)


@pytest.mark.parametrize("k", [10, 25, 39])
def test_future_rest_reads_only_the_future_rest_schedule(k: int) -> None:
    """Corrupting every future measurement except rest_before_s leaves all inputs identical."""
    clean = _fr_inputs(_cycles())
    bad = _cycles()
    future = (bad["cell_id"] == "C3") & (bad["cycle_idx"] > k)
    num = bad.select_dtypes("number").columns.drop(["cycle_idx", "rest_before_s"])
    bad.loc[future, num] = bad.loc[future, num] * -7.0 + 3.0
    pert = _fr_inputs(bad)
    sel = (clean.meta["origin_cycle"] <= k).to_numpy()
    np.testing.assert_array_equal(clean.x_hist[sel], pert.x_hist[sel])
    np.testing.assert_array_equal(clean.x_tab[sel], pert.x_tab[sel])


def test_future_rest_values_and_flag() -> None:
    cyc = _cycles()
    c3 = cyc["cell_id"] == "C3"
    cyc.loc[c3 & (cyc["cycle_idx"] == 21), "rest_before_s"] = 86400.0  # a planned 1-day rest
    on, off = _fr_inputs(cyc), _fr_inputs(cyc, future_rest=False)
    assert off.x_tab.shape[1] == 5 and on.x_tab.shape[1] == 5 + 4
    assert on.feature_names[5:] == ("rest_at_h1", "rest_at_h5", "rest_sum_h1", "rest_sum_h5")
    row = int(np.flatnonzero(on.meta["origin_cycle"].to_numpy() == 20)[0])
    rest_at_h1, rest_at_h5, sum_h1, sum_h5 = on.x_tab[row, 5:]
    assert np.isclose(rest_at_h1, np.log1p(86400.0))  # rest before cycle 21
    assert np.isclose(rest_at_h5, np.log1p(200.0))  # rest before cycle 25
    assert np.isclose(sum_h1, np.log1p(86400.0))
    assert np.isclose(sum_h5, np.log1p(86400.0 + 4 * 200.0))
    with pytest.raises(ValueError, match="forecast task only"):
        TaskSpec(task="rul", future_rest=True)


# Field setting (PLAN_PHASE2): no capacity-derived input, ever --------------------------------
def _field_cycles(seed: int = 0) -> pd.DataFrame:
    cyc = _cycles(seed)
    rng = np.random.default_rng(seed + 1)
    cyc["fld_relax_v0"] = 3.6 + 0.001 * cyc["cycle_idx"] + 0.002 * rng.standard_normal(len(cyc))
    cyc["fld_win_dq_ah"] = cyc["capacity_ah"] * 0.6 + 0.01 * rng.standard_normal(len(cyc))
    for k in range(1, 16):
        cyc[f"fld_q_v{k:02d}"] = cyc["fld_win_dq_ah"] * k / 15
    return cyc


def _field_inputs(cycles: pd.DataFrame, task: str, fs: str = "field_curve"):
    prep = prepare_cycles(cycles, TRAIN, fs)  # type: ignore[arg-type]
    spec = TaskSpec(task=task, lookback=8, horizons=(1, 5), feature_set=fs)  # type: ignore[arg-type]
    return build_samples(prep, TEST, EOL, spec)


@pytest.mark.parametrize("task", ["soh", "forecast", "rul"])
def test_field_inputs_never_read_capacity_derived_columns(task: str) -> None:
    from battery_rul.tasks.samples import FIELD_FORBIDDEN

    clean = _field_inputs(_field_cycles(), task)
    bad = _field_cycles()
    for c in FIELD_FORBIDDEN:
        if c in bad:
            bad[c] = bad[c] * -3.0 + 7.0  # corrupt every cycle of every cell
    pert = _field_inputs(bad, task)
    assert "soh" not in clean.channel_names
    assert not set(clean.channel_names) & set(FIELD_FORBIDDEN)
    np.testing.assert_array_equal(clean.x_hist, pert.x_hist)
    np.testing.assert_array_equal(clean.x_tab, pert.x_tab)


@pytest.mark.parametrize("task", ["soh", "forecast", "rul"])
@pytest.mark.parametrize("k", [10, 25, 39])
def test_field_rule2_no_future_inputs(task: str, k: int) -> None:
    clean = _field_inputs(_field_cycles(), task)
    bad = _field_cycles()
    future = (bad["cell_id"] == "C3") & (bad["cycle_idx"] > k)
    num = bad.select_dtypes("number").columns.drop("cycle_idx")
    bad.loc[future, num] = bad.loc[future, num] * -7.0 + 3.0
    pert = _field_inputs(bad, task)
    sel_c = (clean.meta["origin_cycle"] <= k).to_numpy()
    sel_p = (pert.meta["origin_cycle"] <= k).to_numpy()
    np.testing.assert_array_equal(clean.x_hist[sel_c], pert.x_hist[sel_p])
    np.testing.assert_array_equal(clean.x_tab[sel_c], pert.x_tab[sel_p])


def test_field_soh_window_ends_at_the_target_cycle() -> None:
    """Field Task A may use cycle k's charge-side signals (they precede discharge k)."""
    ss = _field_inputs(_field_cycles(), "soh", "field")
    cyc = _field_cycles()
    i = 20
    k = int(ss.meta["origin_cycle"].iloc[i])
    c = ss.channel_names.index("fld_relax_v0")
    raw = cyc[(cyc.cell_id == "C3") & (cyc.cycle_idx <= k)]["fld_relax_v0"]
    # last window step is cycle k itself (after train-only scaling: compare ranks of change)
    assert ss.hist_mask[i, -1]
    assert np.sign(ss.x_hist[i, -1, c] - ss.x_hist[i, -2, c]) == np.sign(
        raw.iloc[-1] - raw.iloc[-2]
    )
