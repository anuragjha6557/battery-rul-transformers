"""Real-data checks for the Toyota loader (skipped when raw files are absent)."""

from __future__ import annotations

import numpy as np
import pytest

from battery_rul.data import toyota
from battery_rul.utils import RAW_DIR

pytestmark = pytest.mark.data


@pytest.fixture(scope="module")
def tables(tmp_path_factory: pytest.TempPathFactory):  # type: ignore[no-untyped-def]
    raw = RAW_DIR / "toyota"
    if not all(next(raw.glob(f"{d}_*.mat"), None) for d in toyota.BATCH_DATES.values()):
        pytest.skip("Toyota raw files not present")
    return toyota.build(raw, tmp_path_factory.mktemp("processed"))


def test_cell_counts_and_split(tables) -> None:  # type: ignore[no-untyped-def]
    c = tables.cells
    assert len(c) == 124
    assert c["batch"].value_counts().sort_index().tolist() == [41, 43, 40]
    assert c["split"].value_counts().to_dict() == {"test1": 43, "train": 41, "test2": 40}
    assert (c[c.cell_id.str.startswith("b3")]["split"] == "test2").all()


def test_merged_cell_cycle_life(tables) -> None:  # type: ignore[no-untyped-def]
    c = tables.cells.set_index("cell_id")
    assert c.loc["b1c0", "reported_cycle_life"] == 1852
    assert c.loc["b1c1", "reported_cycle_life"] == 1179 + 981
    assert "b2c7" not in c.index and "b1c8" not in c.index and "b3c37" not in c.index


def test_published_cycle_lives_match_file(tables) -> None:  # type: ignore[no-untyped-def]
    c = tables.cells.set_index("cell_id")
    assert c.loc["b1c5", "reported_cycle_life"] == 1074
    assert c.loc["b2c0", "reported_cycle_life"] == 300
    assert c.loc["b3c7", "reported_cycle_life"] == 1836


def test_cycle_idx_strictly_increasing(tables) -> None:  # type: ignore[no-untyped-def]
    for _, s in tables.cycles.groupby("cell_id")["cycle_idx"]:
        assert s.is_monotonic_increasing and s.is_unique


def test_soh_range(tables) -> None:  # type: ignore[no-untyped-def]
    assert tables.cycles["soh"].between(0.6, 1.2).all()


def test_charge_features(tables) -> None:  # type: ignore[no-untyped-def]
    c = tables.cycles
    assert c["charge_time_s"].notna().mean() > 0.99
    assert np.allclose(
        c["cc_time_s"] + c["cv_time_s"], c["charge_time_s"], atol=1e-6, equal_nan=True
    )


def test_curves(tables) -> None:  # type: ignore[no-untyped-def]
    cv = tables.curves
    assert len(cv) == 100 * len(tables.cycles)
    assert set(cv["phase"]) == {"discharge"}
    assert cv["charge_ah"].min() >= 0
