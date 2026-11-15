"""Unit tests for the CALCE CS2 loader, on synthetic frames only (no xlsx files)."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from battery_rul.data import calce
from battery_rul.data.calce import (
    INCOMPLETE_DISCHARGE,
    KEPT,
    LOW_CAPACITY,
    NO_CHARGE,
    NO_DISCHARGE,
    cells_row,
    cycles_and_curves,
    order_and_dedupe,
    split_cycles,
)
from battery_rul.data.io import finalize_and_validate

DT = 30.0  # s between samples
N_CC, N_REST1, N_CV, N_REST2, N_DIS, N_REST3 = 20, 4, 10, 2, 120, 2
CAP_EXPECTED = N_DIS * 1.1 * DT / 3600  # Arbin-style (rectangle) discharge counter, Ah


def _cycle_rows(
    *,
    n_dis: int = N_DIS,
    dis_end_v: float = 2.7,
    ir: float = 0.09,
    cv: bool = True,
    discharge: bool = True,
    dis_current: float = -1.1,
) -> list[tuple[float, float, float]]:
    """(current, voltage, internal_resistance) rows of one standard cycle."""
    rows: list[tuple[float, float, float]] = []
    rows += [(0.55, v, 0.0) for v in np.linspace(3.6, 4.2, N_CC)]
    rows += [(0.0, 4.1, 0.0)] * N_REST1
    if cv:
        rows += [(i, 4.2, ir) for i in np.linspace(1.0, 0.05, N_CV)]
    rows += [(0.0, 4.19, ir)] * N_REST2
    if discharge:
        # Discharge-phase IR readings deliberately differ: the loader must ignore them,
        # because discharge k is what measures the target capacity_k (leakage rule).
        rows += [(dis_current, v, 2 * ir) for v in np.linspace(4.0, dis_end_v, n_dis)]
        rows += [(0.0, 3.3, 2 * ir)] * N_REST3
    return rows


def make_session(
    start: str,
    source_file: str,
    cycles: list[list[tuple[float, float, float]]] | None = None,
    n_cycles: int = 2,
    test_time0: float = DT,
) -> pd.DataFrame:
    """A raw-like channel frame: 2 leading rest rows, then the given cycles back to back."""
    cycles = cycles if cycles is not None else [_cycle_rows() for _ in range(n_cycles)]
    rows: list[tuple[float, float, float]] = [(0.0, 3.4, 0.0)] * 2
    for c in cycles:
        rows += c
    cur = np.array([r[0] for r in rows])
    volt = np.array([r[1] for r in rows])
    ir = np.array([r[2] for r in rows])
    out_a = np.clip(-cur, 0, None) * DT / 3600
    dcap = np.cumsum(out_a)
    deng = np.cumsum(out_a * volt)
    t0 = pd.Timestamp(start)
    return pd.DataFrame(
        {
            "Test_Time(s)": test_time0 + DT * np.arange(len(rows)),
            "Date_Time": [t0 + pd.Timedelta(seconds=DT * i) for i in range(len(rows))],
            "Current(A)": cur,
            "Voltage(V)": volt,
            "Discharge_Capacity(Ah)": dcap,
            "Discharge_Energy(Wh)": deng,
            "Internal_Resistance(Ohm)": ir,
            "source_file": source_file,
        }
    )


# --------------------------------------------------------------------------------------
# ordering / dedupe
# --------------------------------------------------------------------------------------
def test_orders_by_date_time_not_filename() -> None:
    # lexical filename order would put '10_15_10' before '1_10_11'; the dates say otherwise.
    late = make_session("2011-01-03 10:00:00", "CS2_35_1_10_11.xlsx")
    early = make_session("2010-10-08 10:00:00", "CS2_35_10_15_10.xlsx")
    out = order_and_dedupe([late, early])
    firsts = out.groupby("session")["source_file"].first().tolist()
    assert firsts == ["CS2_35_10_15_10.xlsx", "CS2_35_1_10_11.xlsx"]
    assert out["global_time_s"].is_monotonic_increasing
    assert sorted(out["session"].unique()) == [0, 1]
    # counters restart per session: the discharge counter is not carried across sessions
    assert out.groupby("session")["Discharge_Capacity(Ah)"].first().max() == 0.0


def test_exact_duplicate_session_dropped_and_reported() -> None:
    a = make_session("2011-01-31 10:00:00", "CS2_35_2_10_11.xlsx")
    b = a.copy()
    b["source_file"] = "CS2_35_2_4_11.xlsx"
    other = make_session("2010-12-01 10:00:00", "CS2_35_12_1_10.xlsx")
    out = order_and_dedupe([a, other, b])
    assert out["session"].nunique() == 2
    assert len(out) == len(a) + len(other)
    report = out.attrs["dedupe_report"]
    assert len(report) == 1 and "duplicate" in report[0]
    # deterministic: ties keep the lexically first file
    assert "CS2_35_2_10_11.xlsx" in set(out["source_file"])


def test_partial_overlap_is_trimmed() -> None:
    a = make_session("2010-10-01 10:00:00", "a.xlsx")
    # starts 100 samples after a starts, so overlaps the tail of a and extends beyond it
    b = make_session("2010-10-01 10:50:00", "b.xlsx")
    assert b["Date_Time"].iloc[0] < a["Date_Time"].iloc[-1] < b["Date_Time"].iloc[-1]
    out = order_and_dedupe([b, a])
    assert out["Date_Time"].is_monotonic_increasing
    assert not out["Date_Time"].duplicated().any()
    assert "trimmed" in out.attrs["dedupe_report"][0]


def test_global_time_continuous_within_session_and_gap_between() -> None:
    a = make_session("2010-10-01 00:00:00", "a.xlsx")
    b = make_session("2010-10-02 00:00:00", "b.xlsx")  # restarts Test_Time(s)
    out = order_and_dedupe([a, b])
    g = out["global_time_s"].to_numpy()
    d = np.diff(g)
    assert np.allclose(np.delete(d, len(a) - 1), DT)
    assert d[len(a) - 1] > 3600  # the idle gap between sessions is visible in global time


# --------------------------------------------------------------------------------------
# cycle splitting
# --------------------------------------------------------------------------------------
def test_full_cycles_kept_and_partial_cycle_at_session_end_dropped() -> None:
    cycles = [_cycle_rows(), _cycle_rows(), _cycle_rows(discharge=False)[:30]]  # ends mid-charge
    df = order_and_dedupe([make_session("2010-10-01 00:00:00", "s.xlsx", cycles=cycles)])
    recs = split_cycles(df)
    assert [r.status for r in recs] == [KEPT, KEPT, NO_DISCHARGE]
    assert recs[2].discharge.empty and not recs[2].charge.empty


def test_discharge_cut_by_session_end_is_partial() -> None:
    cycles = [_cycle_rows(), _cycle_rows(n_dis=40, dis_end_v=3.6)]  # stops at 3.6 V
    df = order_and_dedupe([make_session("2010-10-01 00:00:00", "s.xlsx", cycles=cycles)])
    recs = split_cycles(df)
    assert [r.status for r in recs] == [KEPT, INCOMPLETE_DISCHARGE]


def test_tiny_full_depth_discharge_is_other_and_orphan_discharge_is_other() -> None:
    tiny = _cycle_rows(n_dis=5, dis_end_v=2.7)  # reaches 2.7 V but only ~0.05 Ah
    s = make_session("2010-10-01 00:00:00", "s.xlsx", cycles=[tiny])
    assert [r.status for r in split_cycles(order_and_dedupe([s]))] == [LOW_CAPACITY]
    # a session that starts directly in a discharge has no charge to pair with
    orphan_rows = [r for r in _cycle_rows() if r[0] <= 0]
    s2 = make_session("2010-10-01 00:00:00", "t.xlsx", cycles=[orphan_rows])
    assert [r.status for r in split_cycles(order_and_dedupe([s2]))] == [NO_CHARGE]


def test_charge_is_paired_with_the_discharge_that_follows_it() -> None:
    df = order_and_dedupe([make_session("2010-10-01 00:00:00", "s.xlsx", n_cycles=3)])
    recs = split_cycles(df)
    assert len(recs) == 3
    for k, r in enumerate(recs):
        assert r.charge["global_time_s"].iloc[-1] < r.discharge["global_time_s"].iloc[0]
        assert (r.charge["Current(A)"].max() > 0.5) and (r.discharge["Current(A)"] < 0).all()
        if k > 0:  # charge k starts after discharge k-1 ended
            assert (
                r.charge["global_time_s"].iloc[0] > recs[k - 1].discharge["global_time_s"].iloc[-1]
            )


def test_sandwiched_sign_blip_does_not_break_the_pairing() -> None:
    rows = _cycle_rows()
    # one spurious discharge-sign sample inside the rest between CC and CV
    k = N_CC + 1
    rows[k] = (-0.05, rows[k][1], rows[k][2])
    df = order_and_dedupe([make_session("2010-10-01 00:00:00", "s.xlsx", cycles=[rows])])
    recs = split_cycles(df)
    assert [r.status for r in recs] == [KEPT]
    # ...and the blip-merging did not swallow the real charge: CC part is still there
    assert len(recs[0].charge) >= N_CC


def test_cycles_never_span_sessions() -> None:
    a = make_session(
        "2010-10-01 00:00:00", "a.xlsx", cycles=[_cycle_rows(), _cycle_rows(discharge=False)]
    )
    b = make_session("2010-10-05 00:00:00", "b.xlsx", n_cycles=1)
    recs = split_cycles(order_and_dedupe([a, b]))
    assert [(r.session, r.status) for r in recs] == [(0, KEPT), (0, NO_DISCHARGE), (1, KEPT)]


# --------------------------------------------------------------------------------------
# measurements
# --------------------------------------------------------------------------------------
def test_capacity_counter_matches_integral_and_expected() -> None:
    df = order_and_dedupe([make_session("2010-10-01 00:00:00", "s.xlsx", n_cycles=3)])
    for r in split_cycles(df):
        assert r.capacity_source == "counter"
        assert r.capacity_ah == pytest.approx(CAP_EXPECTED, rel=1e-9)  # per-cycle, not cumulative
        assert r.capacity_counter_ah == pytest.approx(r.capacity_integral_ah, rel=0.01)
        assert r.capacity_integral_ah < r.capacity_counter_ah  # half a sampling interval short


def test_capacity_falls_back_to_integral_when_counter_unusable() -> None:
    s = make_session("2010-10-01 00:00:00", "s.xlsx", n_cycles=1)
    s["Discharge_Capacity(Ah)"] = 0.0  # a broken counter
    (r,) = split_cycles(order_and_dedupe([s]))
    assert r.capacity_source == "integral"
    assert r.capacity_ah == pytest.approx(CAP_EXPECTED, rel=0.01)
    assert r.kept


def test_counter_baseline_is_the_sample_before_the_discharge() -> None:
    # a non-zero counter offset at the start of the discharge must not leak into the capacity
    s = make_session("2010-10-01 00:00:00", "s.xlsx", n_cycles=2)
    (r1, r2) = split_cycles(order_and_dedupe([s]))
    assert r2.discharge["Discharge_Capacity(Ah)"].iloc[-1] > 1.9 * CAP_EXPECTED
    assert r2.capacity_ah == pytest.approx(CAP_EXPECTED, rel=1e-9)
    assert r1.capacity_ah == pytest.approx(CAP_EXPECTED, rel=1e-9)


def test_cc_cv_split_and_charge_features() -> None:
    df = order_and_dedupe([make_session("2010-10-01 00:00:00", "s.xlsx", n_cycles=1)])
    cycles, _, _ = cycles_and_curves(split_cycles(df), "CS2_X")
    row = cycles.iloc[0]
    charge_rows = N_CC + N_REST1 + N_CV
    assert row["charge_time_s"] == pytest.approx((charge_rows - 1) * DT)
    assert row["cc_time_s"] == pytest.approx((N_CC - 1) * DT)  # first V >= 4.19 is the last CC row
    assert row["cv_time_s"] == pytest.approx(row["charge_time_s"] - row["cc_time_s"])
    assert row["cc_time_s"] + row["cv_time_s"] == pytest.approx(row["charge_time_s"])
    assert row["discharge_time_s"] == pytest.approx((N_DIS - 1) * DT)
    assert row["charge_throughput_ah"] > 0
    assert row["discharge_energy_wh"] == pytest.approx(
        CAP_EXPECTED * np.mean(np.linspace(4.0, 2.7, N_DIS)), rel=1e-6
    )


def test_skipped_cv_step_shows_up_as_tiny_cv_time_but_cycle_is_kept() -> None:
    rows = _cycle_rows(cv=False)
    df = order_and_dedupe([make_session("2010-10-01 00:00:00", "s.xlsx", cycles=[rows])])
    cycles, _, stats = cycles_and_curves(split_cycles(df), "CS2_X")
    assert len(cycles) == 1  # faithful parse: no outlier removal
    assert cycles["cv_time_s"].iloc[0] < calce.NO_CV_TIME_S
    assert stats.n_kept_no_cv == 1


def test_ir_is_median_of_positive_charge_window_readings_only() -> None:
    rows = _cycle_rows(ir=0.1)
    # one outlying reading inside the CV (charge) window; CC zeros are ignored
    k = N_CC + N_REST1 + 2
    rows[k] = (rows[k][0], rows[k][1], 0.5)
    df = order_and_dedupe([make_session("2010-10-01 00:00:00", "s.xlsx", cycles=[rows])])
    cycles, _, _ = cycles_and_curves(split_cycles(df), "CS2_X")
    # 0.1, not 0.2 (discharge readings excluded) and not pulled up by the outlier (median)
    assert cycles["ir_ohm"].iloc[0] == pytest.approx(0.1)


def test_ir_nan_when_no_positive_reading() -> None:
    rows = _cycle_rows(ir=0.0)
    df = order_and_dedupe([make_session("2010-10-01 00:00:00", "s.xlsx", cycles=[rows])])
    cycles, _, _ = cycles_and_curves(split_cycles(df), "CS2_X")
    assert np.isnan(cycles["ir_ohm"].iloc[0])


# --------------------------------------------------------------------------------------
# tables
# --------------------------------------------------------------------------------------
def _tables_for(sessions: list[pd.DataFrame]) -> tuple[pd.DataFrame, pd.DataFrame]:
    recs = split_cycles(order_and_dedupe(sessions))
    cycles, curves, _ = cycles_and_curves(recs, "CS2_X")
    return cycles, curves


def test_cycle_idx_is_contiguous_over_kept_cycles_across_sessions() -> None:
    a = make_session(
        "2010-10-01 00:00:00",
        "a.xlsx",
        cycles=[_cycle_rows(), _cycle_rows(), _cycle_rows(discharge=False)],
    )
    b = make_session("2010-10-03 00:00:00", "b.xlsx", n_cycles=2)
    cycles, _ = _tables_for([b, a])
    assert cycles["cycle_idx"].tolist() == [1, 2, 3, 4]


def test_rest_before_s_uses_global_time() -> None:
    a = make_session("2010-10-01 00:00:00", "a.xlsx", n_cycles=2)
    b = make_session("2010-10-03 00:00:00", "b.xlsx", n_cycles=1)
    cycles, _ = _tables_for([a, b])
    rest = cycles["rest_before_s"].to_numpy()
    assert np.isnan(rest[0])
    # within a session: rest after discharge (N_REST3 rows) + rest before charge is zero-length,
    # i.e. charge starts N_REST3 + 1 sampling intervals after the last discharge sample
    assert rest[1] == pytest.approx((N_REST3 + 1) * DT)
    assert rest[2] > 24 * 3600  # across the 2-day session gap


def test_curves_follow_the_contract() -> None:
    cycles, curves = _tables_for([make_session("2010-10-01 00:00:00", "a.xlsx", n_cycles=2)])
    assert set(curves["phase"]) == {"charge", "discharge"}
    assert set(curves["cycle_idx"]) == set(cycles["cycle_idx"])
    for _, g in curves.groupby(["cycle_idx", "phase"]):
        assert g["sample_idx"].tolist() == list(range(len(g)))
        assert g["t_s"].iloc[0] == 0.0 and g["t_s"].is_monotonic_increasing
        assert g["charge_ah"].iloc[0] == 0.0 and g["charge_ah"].is_monotonic_increasing
        assert g["temp_c"].isna().all()
    ch = curves[curves["phase"] == "charge"]
    di = curves[curves["phase"] == "discharge"]
    assert (ch["current_a"] >= 0).all()  # charge positive
    assert (di["current_a"] < 0).all()  # discharge negative
    last = di[di["cycle_idx"] == 1]["charge_ah"].iloc[-1]
    assert last == pytest.approx(CAP_EXPECTED, rel=0.01)


def test_tables_pass_schema_validation() -> None:
    cycles, curves = _tables_for(
        [
            make_session("2010-10-01 00:00:00", "a.xlsx", n_cycles=3),
            make_session("2010-10-09 00:00:00", "b.xlsx", n_cycles=2),
        ]
    )
    cells = pd.DataFrame([cells_row("CS2_X")])
    t = finalize_and_validate(cells, cycles, curves)
    assert len(t.cycles) == 5
    assert t.cycles["soh"].notna().all()
    assert t.cells["ambient_temp_c"].isna().all()
    assert t.cells["batch"].isna().all()
    assert t.cells["source_file"].iloc[0] == "CS2_X.zip"
    assert t.cycles["charge_temp_max_c"].isna().all()


def test_blip_between_charge_and_discharge_is_absorbed_into_the_discharge() -> None:
    # real data: one stray sample with I < -0.01 A right after the charge, before the true discharge
    rows = _cycle_rows()
    k = N_CC + N_REST1 + N_CV  # first rest sample after the CV phase
    rows[k] = (-0.05, rows[k][1], rows[k][2])
    df = order_and_dedupe([make_session("2010-10-01 00:00:00", "s.xlsx", cycles=[rows])])
    recs = split_cycles(df)
    assert [r.status for r in recs] == [KEPT]
    assert len(recs[0].charge) == N_CC + N_REST1 + N_CV
    assert recs[0].capacity_ah == pytest.approx(CAP_EXPECTED, rel=0.01)
