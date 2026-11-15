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


def _inputs(cycles: pd.DataFrame, task: str, cells: tuple[str, ...] = TEST):
    prep = prepare_cycles(cycles, TRAIN, "mc")
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
