"""Real-data checks for the CALCE CS2 loader (skipped when the raw files are absent / in CI)."""

from __future__ import annotations

from pathlib import Path

import pytest

from battery_rul.data import calce
from battery_rul.data.io import DatasetTables, read_tables
from battery_rul.utils import RAW_DIR

pytestmark = pytest.mark.data

RAW = RAW_DIR / "calce"


def _have_raw() -> bool:
    return all(
        ((RAW / c).is_dir() and any((RAW / c).glob("*.xlsx"))) or (RAW / f"{c}.zip").exists()
        for c in calce.CELL_IDS
    )


@pytest.fixture(scope="module")
def built(tmp_path_factory: pytest.TempPathFactory) -> tuple[DatasetTables, Path]:
    if not _have_raw():
        pytest.skip("CALCE raw data not present")
    root = tmp_path_factory.mktemp("processed")
    return calce.build(RAW, root), root


def test_four_cells_with_many_cycles(built: tuple[DatasetTables, Path]) -> None:
    tables, _ = built
    assert sorted(tables.cells["cell_id"]) == list(calce.CELL_IDS)
    counts = tables.cycles.groupby("cell_id").size()
    assert (counts > 500).all(), counts.to_dict()


def test_first_capacity_and_soh_range(built: tuple[DatasetTables, Path]) -> None:
    cyc = built[0].cycles
    for cell, g in cyc.groupby("cell_id"):
        g = g.sort_values("cycle_idx")
        assert 1.0 <= g["capacity_ah"].iloc[0] <= 1.2, cell
        # the cells were cycled far past 80 % SOH (down to ~15-30 %)
        assert g["soh"].between(0.05, 1.15).all(), cell
        assert g["soh"].min() < 0.8, cell
        assert g["cycle_idx"].is_monotonic_increasing and g["cycle_idx"].is_unique
        assert g["cycle_idx"].iloc[0] == 1 and g["cycle_idx"].iloc[-1] == len(g)


def test_cycle_features_are_physical(built: tuple[DatasetTables, Path]) -> None:
    cyc = built[0].cycles
    assert cyc["charge_temp_max_c"].isna().all()  # no temperature channel
    # IR comes from the charge window only (leakage rule); ~3 % of cycles have no reading there
    ir = cyc["ir_ohm"]
    assert ir.dropna().between(0.05, 0.25).all()
    assert ir.isna().mean() < 0.05
    assert cyc["rest_before_s"].dropna().gt(0).all()
    assert cyc.groupby("cell_id")["rest_before_s"].apply(lambda s: s.isna().sum()).eq(1).all()
    first = cyc.groupby("cell_id")["cycle_idx"].idxmin()
    assert cyc.loc[first, "rest_before_s"].isna().all()
    # charge time ~ CC (0.5C) + CV; discharge at 1C is at most ~1 h
    assert cyc["discharge_time_s"].between(300, 4200).all()
    assert cyc["charge_time_s"].between(300, 10000).all()


def test_every_cycle_has_both_curve_phases_and_written_tables_roundtrip(
    built: tuple[DatasetTables, Path],
) -> None:
    tables, root = built
    n = tables.cycles.shape[0]
    per = tables.curves.groupby(["cell_id", "cycle_idx", "phase"]).size()
    assert len(per) == 2 * n
    on_disk = read_tables("calce", root)
    assert len(on_disk.cycles) == n and len(on_disk.curves) == len(tables.curves)
    di = tables.curves[tables.curves["phase"] == "discharge"]
    # a discharge window may contain a handful of ~0 A rest samples (stray sign glitch merged)
    assert (di["current_a"] < 0).mean() > 0.9999
    assert (di["voltage_v"] < 4.3).all() and (di["voltage_v"] > 2.6).all()


def test_dedupe_drops_the_duplicate_workbooks() -> None:
    if not _have_raw():
        pytest.skip("CALCE raw data not present")
    load = calce.load_cell_detailed(RAW / "CS2_35", "CS2_35")
    assert load.stats.n_files - load.stats.n_sessions_used == len(load.stats.dedupe_report) == 1
