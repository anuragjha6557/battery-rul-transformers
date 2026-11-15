"""Toyota loader tests on synthetic RawCells (no HDF5 files)."""

from __future__ import annotations

from collections import Counter

import numpy as np
import pandas as pd
import pytest

from battery_rul.data import toyota
from battery_rul.data.io import finalize_and_validate
from battery_rul.data.toyota import RawCell, RawCycle

NGRID = 1000


def _raw_cycle(scale: float = 1.0, neg: bool = False) -> RawCycle:
    """Charge: 1 C for 6 samples, V hits 3.6 at sample 4, I tapers; then 4 C discharge."""
    t = np.arange(14) * 0.5  # minutes
    i = np.array([0, 3, 3, 3, 3, 1, 0.5, -4, -4, -4, -4, -4, -4, 0.0])
    v = np.array([2.0, 3.0, 3.3, 3.5, 3.6, 3.6, 3.6, 3.4, 3.2, 3.0, 2.8, 2.4, 2.0, 2.0])
    q = np.linspace(0.0, 1.0 * scale, NGRID)
    if neg:
        q[0] = -0.01
    return RawCycle(t, v, i, q, np.full(NGRID, 31.0))


def _cell(
    cid: str,
    caps: list[float],
    cycles: list[float] | None = None,
    life: float = 100.0,
    ir: float = 0.016,
    tag: float = 1.0,
) -> RawCell:
    n = len(caps)
    summary = {
        "cycle": np.array(cycles if cycles is not None else np.arange(1, n + 1), dtype=float),
        "QDischarge": np.array(caps, dtype=float),
        "QCharge": np.array(caps, dtype=float) + 0.001,
        "IR": np.full(n, ir),
        "Tmax": np.full(n, 35.0),
        "Tavg": np.full(n, 32.0),
        "Tmin": np.full(n, 30.0),
        "chargetime": np.full(n, 13.0),
    }
    return RawCell(
        cell_id=cid,
        batch="2017-05-12",
        source_file=f"{cid}.mat",
        policy="3.6C(80%)-3.6C",
        cycle_life=life,
        summary=summary,
        vdlin=np.linspace(3.5, 2.0, NGRID),
        loaders=[(lambda tag=tag: _raw_cycle(tag)) for _ in range(n)],
    )


def test_charge_times() -> None:
    rc = _raw_cycle()
    total, cc, cv = toyota.charge_times(rc.t, rc.v, rc.i)
    # charge samples 1..6 -> 2.5 min = 150 s; V >= 3.595 at sample 4 -> (4-1)*0.5 min = 90 s
    assert total == pytest.approx(150.0)
    assert cc == pytest.approx(90.0)
    assert cv == pytest.approx(60.0)


def test_charge_times_without_discharge_is_nan() -> None:
    rc = _raw_cycle()
    out = toyota.charge_times(rc.t[:7], rc.v[:7], rc.i[:7])
    assert all(np.isnan(x) for x in out)


def test_cycle_filter_and_units() -> None:
    caps = [0.0, 1.07, 1.5, 1.06, 0.05, float("nan"), 1.05]
    cell = _cell("b1c0", caps)
    st: Counter[str] = Counter()
    cycles, _ = toyota.cell_tables(cell, st)
    assert cycles["cycle_idx"].tolist() == [2, 4, 7]  # gaps keep their place
    assert st["kept"] == 3
    assert st["dropped_low"] == 3  # 0.0, 0.05, nan
    assert st["dropped_high"] == 1
    assert cycles["capacity_ah"].tolist() == pytest.approx([1.07, 1.06, 1.05])
    assert cycles["charge_time_s"].tolist() == pytest.approx([150.0] * 3)
    assert (cycles["cc_time_s"] + cycles["cv_time_s"]).tolist() == pytest.approx([150.0] * 3)
    assert cycles["discharge_temp_max_c"].tolist() == [35.0] * 3
    assert cycles["charge_throughput_ah"].tolist() == pytest.approx([1.071, 1.061, 1.051])


def test_ir_zero_becomes_nan() -> None:
    cycles, _ = toyota.cell_tables(_cell("b1c0", [1.0, 1.0], ir=0.0))
    assert cycles["ir_ohm"].isna().all()


def test_curve_decimation_and_clipping() -> None:
    cell = _cell("b1c0", [1.0, 1.0])
    cell2 = RawCell(**{**cell.__dict__, "loaders": [lambda: _raw_cycle(1.0, neg=True)] * 2})
    st: Counter[str] = Counter()
    _, curves = toyota.cell_tables(cell2, st)
    assert len(curves) == 2 * 100
    assert st["qdlin_clipped"] == 2
    one = curves[curves.cycle_idx == 1]
    assert one["sample_idx"].tolist() == list(range(100))
    assert one["voltage_v"].iloc[0] == pytest.approx(3.5)
    assert one["voltage_v"].iloc[1] == pytest.approx(cell.vdlin[10])
    assert (one["charge_ah"] >= 0).all()
    assert set(curves["phase"]) == {"discharge"}
    assert curves["t_s"].isna().all()
    assert curves["current_a"].isna().all()


def test_merge_continuations_offsets() -> None:
    a = _cell("b1c0", [1.0] * 5, life=10.0, tag=1.0)
    b = _cell("b2c7", [0.9] * 3, life=4.0, tag=2.0)
    merged = toyota.merge_continuations({"b1c0": a}, {"b2c7": b}, {"b1c0": ("b2c7", 3)})
    m = merged["b1c0"]
    assert m.cycle_life == 13.0
    assert m.summary["cycle"].tolist() == [1, 2, 3, 4, 5, 6, 7, 8]
    assert m.summary["QDischarge"].tolist() == [1.0] * 5 + [0.9] * 3
    assert len(m.loaders) == 8
    assert m.loaders[7]().qdlin[-1] == pytest.approx(2.0)  # came from batch 2 cell
    assert a.cycle_life == 10.0  # inputs untouched


def test_merge_length_mismatch_raises() -> None:
    a = _cell("b1c0", [1.0] * 5)
    b = _cell("b2c7", [0.9] * 3)
    with pytest.raises(ValueError, match="continuation"):
        toyota.merge_continuations({"b1c0": a}, {"b2c7": b}, {"b1c0": ("b2c7", 4)})


def test_drop_cells() -> None:
    cells = {"b1c0": _cell("b1c0", [1.0]), "b1c1": _cell("b1c1", [1.0])}
    assert list(toyota.drop_cells(cells, ["b1c1"])) == ["b1c0"]
    with pytest.raises(KeyError):
        toyota.drop_cells(cells, ["b1c9"])


def test_official_continuation_constants() -> None:
    assert len(toyota.CONTINUATIONS) == 5
    assert [v[1] for v in toyota.CONTINUATIONS.values()] == [662, 981, 1060, 208, 482]
    assert len(toyota.DROP_B1) == 5 and len(toyota.DROP_B3) == 6


def test_split_41_43_40() -> None:
    ids = [f"b1c{k}" for k in range(41)] + [f"b2c{k}" for k in range(43)]
    ids += [f"b3c{k}" for k in range(40)]
    split = toyota.assign_split(ids)
    counts = Counter(split.values())
    assert counts == {"train": 41, "test1": 43, "test2": 40}
    assert [i for i, c in enumerate(ids) if split[c] == "train"] == list(range(1, 82, 2))
    assert split[ids[83]] == "test1"
    assert split[ids[82]] == "test1"
    assert all(split[c] == "test2" for c in ids[84:])


def test_tables_pass_validation() -> None:
    cells = [_cell("b1c0", [0.0, 1.07, 1.06]), _cell("b1c1", [1.08, 1.07])]
    split = toyota.assign_split([c.cell_id for c in cells], n_batch12=2)
    parts = [toyota.cell_tables(c) for c in cells]
    t = finalize_and_validate(
        pd.DataFrame([toyota.cell_row(c, split[c.cell_id]) for c in cells]),
        pd.concat([p[0] for p in parts], ignore_index=True),
        pd.concat([p[1] for p in parts], ignore_index=True),
    )
    assert len(t.cycles) == 4
    assert len(t.curves) == 400
    assert t.cells["split"].tolist() == ["test1", "test1"]
    assert t.cells["reported_cycle_life"].tolist() == [100.0, 100.0]
    assert t.cells["charge_protocol"].iloc[0].startswith("fast-charge 3.6C(80%)-3.6C")
