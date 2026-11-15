"""Real-data checks for the NASA loader (skipped when raw files are absent)."""

from __future__ import annotations

import numpy as np
import pytest

from battery_rul.data import nasa
from battery_rul.utils import RAW_DIR

pytestmark = pytest.mark.data

EXPECTED = {"B0005": 168, "B0006": 168, "B0007": 168, "B0018": 132}


@pytest.fixture(scope="module")
def tables(tmp_path_factory: pytest.TempPathFactory):  # type: ignore[no-untyped-def]
    raw = RAW_DIR / "nasa"
    if not all((raw / f"{c}.mat").exists() for c in EXPECTED):
        pytest.skip("NASA raw files not present")
    return nasa.build(raw, tmp_path_factory.mktemp("processed"))


def test_cycle_counts(tables) -> None:  # type: ignore[no-untyped-def]
    counts = tables.cycles.groupby("cell_id").size().to_dict()
    assert counts == EXPECTED


def test_first_capacity_b0005(tables) -> None:  # type: ignore[no-untyped-def]
    c = tables.cycles
    first = c[(c.cell_id == "B0005") & (c.cycle_idx == 1)]["capacity_ah"].iloc[0]
    assert first == pytest.approx(1.8565, abs=1e-3)


def test_soh_range(tables) -> None:  # type: ignore[no-untyped-def]
    assert tables.cycles["soh"].between(0.5, 1.15, inclusive="neither").all()


def test_cc_plus_cv_equals_charge_time(tables) -> None:  # type: ignore[no-untyped-def]
    c = tables.cycles.dropna(subset=["charge_time_s"])
    assert len(c) > 0
    assert np.allclose(c["cc_time_s"] + c["cv_time_s"], c["charge_time_s"], atol=1e-6)


def test_curves_charge_ah_monotone(tables) -> None:  # type: ignore[no-untyped-def]
    d = tables.curves.groupby(["cell_id", "cycle_idx", "phase"], sort=False)["charge_ah"].diff()
    assert (d.dropna() >= 0).all()
