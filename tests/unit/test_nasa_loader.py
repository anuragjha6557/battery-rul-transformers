"""NASA loader tests on a small synthetic .mat that mimics the real file structure."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pytest
from scipy.io import loadmat, savemat

from battery_rul.data import nasa
from battery_rul.data.io import finalize_and_validate, read_tables

ENTRY_DTYPE = [("type", "O"), ("ambient_temperature", "O"), ("time", "O"), ("data", "O")]


def _datevec(h: int, m: int, s: float = 0.0) -> np.ndarray:
    return np.array([2008, 4, 2, h, m, s], dtype=float)


def _charge(dt: float, start: tuple[int, int]) -> dict[str, Any]:
    """11-sample charge: CC 1.5 A, V hits 4.19 at sample 6, then CV taper; sample 0 is a spike."""
    volt = np.array([3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.19, 4.2, 4.2, 4.2, 4.2])
    cur = np.array([-0.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.0, 0.6, 0.3, 0.1])
    return {
        "type": "charge",
        "ambient_temperature": 24.0,
        "time": _datevec(*start),
        "data": {
            "Voltage_measured": volt,
            "Current_measured": cur,
            "Temperature_measured": 25.0 + 0.1 * np.arange(11),
            "Time": dt * np.arange(11),
        },
    }


def _discharge(dt: float, start: tuple[int, int], cap: float) -> dict[str, Any]:
    """7-sample constant-current 2 A discharge, V falling linearly 4.0 -> 3.0 V."""
    return {
        "type": "discharge",
        "ambient_temperature": 24.0,
        "time": _datevec(*start),
        "data": {
            "Voltage_measured": 4.0 - np.arange(7) / 6.0,
            "Current_measured": np.full(7, -2.0),
            "Temperature_measured": 30.0 + np.arange(7),
            "Time": dt * np.arange(7),
            "Capacity": np.array(cap),
        },
    }


def _impedance(start: tuple[int, int], re: float, rct: float) -> dict[str, Any]:
    return {
        "type": "impedance",
        "ambient_temperature": 24.0,
        "time": _datevec(*start),
        "data": {
            "Sense_current": np.ones(4, dtype=complex),
            "Re": np.array(re),
            "Rct": np.array(rct),
        },
    }


def _entries() -> list[dict[str, Any]]:
    return [
        _impedance((10, 0), 0.05, 0.07),  # EIS #1 -> ir 0.12
        _charge(10.0, (10, 10)),  # charge A -> cycle 1
        _discharge(100.0, (11, 0), 1.5),  # cycle 1, ends 11:10:00
        _charge(5.0, (12, 0)),  # charge B: decoy, superseded by C
        _charge(12.0, (12, 30)),  # charge C -> cycle 2 (rest 4800 s)
        _discharge(200.0, (13, 30), 1.4),  # cycle 2, ends 13:50:00
        _impedance((14, 30), 0.06, 0.08),  # EIS #2 -> ir 0.14, only visible from cycle 3
        _charge(20.0, (15, 0)),  # charge D -> cycle 3 (rest 4200 s)
        _discharge(200.0, (16, 0), 1.3),  # cycle 3
    ]


def write_mat(path: Path, cell_id: str, entries: list[dict[str, Any]]) -> None:
    arr = np.empty((1, len(entries)), dtype=ENTRY_DTYPE)
    for j, e in enumerate(entries):
        arr[0, j] = (e["type"], e["ambient_temperature"], e["time"], e["data"])
    savemat(path, {cell_id: {"cycle": arr}})


@pytest.fixture
def mat_path(tmp_path: Path) -> Path:
    p = tmp_path / "B0005.mat"
    write_mat(p, "B0005", _entries())
    return p


def test_fixture_roundtrips_like_nasa(mat_path: Path) -> None:
    cyc = loadmat(str(mat_path), simplify_cells=True)["B0005"]["cycle"]
    assert len(cyc) == 9
    assert [e["type"] for e in cyc][:3] == ["impedance", "charge", "discharge"]
    assert set(cyc[1]) == {"type", "ambient_temperature", "time", "data"}
    assert cyc[1]["data"]["Time"].shape == (11,)
    assert cyc[2]["data"]["Capacity"] == pytest.approx(1.5)
    assert cyc[0]["data"]["Re"] == pytest.approx(0.05)


def test_cycle_pairing_and_idx(mat_path: Path) -> None:
    cycles, curves = nasa.load_cell(mat_path, "B0005")
    assert cycles["cycle_idx"].tolist() == [1, 2, 3]
    assert cycles["capacity_ah"].tolist() == pytest.approx([1.5, 1.4, 1.3])
    # charge durations 100, 120 (charge C, NOT decoy B = 50), 200
    assert cycles["charge_time_s"].tolist() == pytest.approx([100.0, 120.0, 200.0])
    ch2 = curves[(curves.cycle_idx == 2) & (curves.phase == "charge")]
    assert ch2["t_s"].max() == pytest.approx(120.0)
    assert set(curves["phase"]) == {"charge", "discharge"}


def test_ir_is_forward_filled_only(mat_path: Path) -> None:
    cycles, _ = nasa.load_cell(mat_path, "B0005")
    assert cycles["ir_ohm"].tolist() == pytest.approx([0.12, 0.12, 0.14])


def test_rest_before(mat_path: Path) -> None:
    cycles, _ = nasa.load_cell(mat_path, "B0005")
    rest = cycles["rest_before_s"].to_numpy()
    assert np.isnan(rest[0])
    # cycle 2: charge C 12:30:00 - (11:00:00 + 600 s) = 4800 s; cycle 3: 15:00 - (13:30 + 1200 s)
    assert rest[1:] == pytest.approx([4800.0, 4200.0])


def test_cc_cv_split(mat_path: Path) -> None:
    cycles, _ = nasa.load_cell(mat_path, "B0005")
    # V reaches 4.19 at sample index 6 -> cc = 6*dt
    assert cycles["cc_time_s"].tolist() == pytest.approx([60.0, 72.0, 120.0])
    assert cycles["cv_time_s"].tolist() == pytest.approx([40.0, 48.0, 80.0])
    total = cycles["cc_time_s"] + cycles["cv_time_s"]
    assert total.tolist() == pytest.approx(cycles["charge_time_s"].tolist())


def test_integrals_and_temperatures(mat_path: Path) -> None:
    cycles, curves = nasa.load_cell(mat_path, "B0005")
    # trapezoid of max(I,0): spike sample counts as 0 -> 10.95 A*dt units, dt=10 -> 109.5 A*s
    expected_tp = np.array([10.0, 12.0, 20.0]) * 10.95 / 3600.0
    assert cycles["charge_throughput_ah"].tolist() == pytest.approx(expected_tp.tolist())
    assert cycles["charge_temp_max_c"].tolist() == pytest.approx([26.0] * 3)
    assert cycles["charge_temp_mean_c"].tolist() == pytest.approx([25.5] * 3)  # linear ramp
    # discharge: 2 A * (mean V = 3.5) * duration / 3600
    dur = np.array([600.0, 1200.0, 1200.0])
    assert cycles["discharge_time_s"].tolist() == pytest.approx(dur.tolist())
    assert cycles["discharge_energy_wh"].tolist() == pytest.approx((2 * 3.5 * dur / 3600).tolist())
    assert cycles["discharge_temp_max_c"].tolist() == pytest.approx([36.0] * 3)
    # curve charge_ah uses |I| (spike included): dt*(sum|I| - (|I0|+|In|)/2)/3600, sum|I|=11.5
    ch1 = curves[(curves.cycle_idx == 1) & (curves.phase == "charge")]
    assert ch1["charge_ah"].iloc[-1] == pytest.approx(10.0 * (11.5 - 0.3) / 3600.0)
    dis1 = curves[(curves.cycle_idx == 1) & (curves.phase == "discharge")]
    assert dis1["charge_ah"].iloc[-1] == pytest.approx(2.0 * 600.0 / 3600.0)


def test_curve_conventions(mat_path: Path) -> None:
    _, curves = nasa.load_cell(mat_path, "B0005")
    ch = curves[(curves.cycle_idx == 3) & (curves.phase == "charge")]
    dis = curves[(curves.cycle_idx == 3) & (curves.phase == "discharge")]
    assert ch["current_a"].iloc[3] > 0 and (dis["current_a"] < 0).all()  # charge +, discharge -
    for grp in (ch, dis):
        assert grp["sample_idx"].tolist() == list(range(len(grp)))
        assert grp["t_s"].iloc[0] == 0.0
        assert grp["charge_ah"].iloc[0] == 0.0
        assert (grp["charge_ah"].diff().dropna() >= 0).all()
    assert len(ch) == 11 and len(dis) == 7


def test_tables_pass_validation_and_soh(mat_path: Path) -> None:
    cycles, curves = nasa.load_cell(mat_path, "B0005")
    cells = pd.DataFrame([nasa._cell_row("B0005", "B0005.mat", 24.0)])
    t = finalize_and_validate(cells, cycles, curves)
    assert t.cycles["soh"].iloc[0] == pytest.approx(1.5 / 1.4)  # ref = mean of first 3 caps
    assert t.cells["v_min"].iloc[0] == 2.7


def test_charge_without_pair_and_invalid_capacity(tmp_path: Path) -> None:
    entries = [
        _discharge(100.0, (9, 0), 1.5),  # cycle 1: no charge before it
        _charge(10.0, (10, 0)),
        _discharge(100.0, (11, 0), float("nan")),  # invalid capacity: not a cycle
        _charge(10.0, (12, 0)),
        _discharge(100.0, (13, 0), 1.4),  # cycle 2, pairs with the 12:00 charge
    ]
    p = tmp_path / "B0018.mat"
    write_mat(p, "B0018", entries)
    cycles, curves = nasa.load_cell(p, "B0018")
    assert cycles["cycle_idx"].tolist() == [1, 2]
    assert np.isnan(cycles.loc[0, ["charge_time_s", "cc_time_s", "rest_before_s", "ir_ohm"]]).all()
    assert cycles.loc[1, "charge_time_s"] == pytest.approx(100.0)
    assert not ((curves.cycle_idx == 1) & (curves.phase == "charge")).any()
    # rest: 12:00:00 - (9:00:00 + 600 s)? No: previous *cycle* discharge is cycle 1
    assert cycles.loc[1, "rest_before_s"] == pytest.approx(3 * 3600 - 600.0)


def test_bad_time_samples_are_dropped(tmp_path: Path) -> None:
    ch = _charge(10.0, (10, 0))
    t = ch["data"]["Time"].copy()
    t[4] = t[3]  # duplicate
    t[7] = 5.0  # backward
    t[9] = np.nan
    ch["data"]["Time"] = t
    p = tmp_path / "B0006.mat"
    write_mat(p, "B0006", [ch, _discharge(100.0, (11, 0), 1.5)])
    cycles, curves = nasa.load_cell(p, "B0006")
    c = curves[(curves.phase == "charge")]
    assert len(c) == 8
    assert c["t_s"].is_monotonic_increasing and c["t_s"].is_unique
    assert c["sample_idx"].tolist() == list(range(8))
    assert cycles.loc[0, "charge_time_s"] == pytest.approx(100.0)


def test_build_writes_validated_tables(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    raw.mkdir()
    for cid in nasa.CELLS:
        write_mat(raw / f"{cid}.mat", cid, _entries())
    out = tmp_path / "processed"
    tables = nasa.build(raw, out)
    assert sorted(tables.cells["cell_id"]) == sorted(nasa.CELLS)
    assert len(tables.cycles) == 12
    assert tables.cells.set_index("cell_id").loc["B0007", "v_min"] == 2.2
    assert tables.cells["ambient_temp_c"].eq(24.0).all()
    back = read_tables("nasa", out)
    assert len(back.curves) == len(tables.curves)
