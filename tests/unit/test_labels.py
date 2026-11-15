"""EOL label construction per ADR-0005 (+ Amendment 1)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from battery_rul.data.schema import add_soh, empty_optional_features
from battery_rul.tasks.labels import eol_table


def _cells(dataset: str, ids: list[str], life: list[float | None]) -> pd.DataFrame:
    return pd.DataFrame({"dataset": dataset, "cell_id": ids, "reported_cycle_life": life})


def _cycles(dataset: str, cap_by_cell: dict[str, np.ndarray], cv: dict[str, np.ndarray]):
    rows = []
    for cell, cap in cap_by_cell.items():
        for k, c in enumerate(cap):
            rows.append(
                {
                    "dataset": dataset,
                    "cell_id": cell,
                    "cycle_idx": k + 1,
                    "capacity_ah": c,
                    "cv_time_s": cv[cell][k],
                    "charge_throughput_ah": c,
                }
            )
    return add_soh(empty_optional_features(pd.DataFrame(rows)))


def test_rule_ignores_single_artifact_dip_and_uses_sustained_crossing() -> None:
    n = 100
    cap = np.linspace(1.0, 0.7, n)  # SOH crosses 0.8 around cycle 67
    cap[19] = 0.5  # skipped-CV artifact dip at cycle 20
    cv = np.full(n, 1500.0)
    cv[19] = 10.0
    eol = eol_table(_cycles("calce", {"A": cap}, {"A": cv}), _cells("calce", ["A"], [None]))
    row = eol.iloc[0]
    assert row.label_source == "rule" and not row.censored
    soh = cap / cap[:5].mean()
    below = soh < 0.8
    below[19] = False  # the masked artifact cycle
    expected = int(np.flatnonzero(below)[0]) + 1
    assert expected > 60 and row.eol_cycle == expected  # the dip at cycle 20 is ignored


def test_rule_censors_when_never_sustained() -> None:
    cap = np.linspace(1.0, 0.85, 50)
    eol = eol_table(
        _cycles("nasa", {"B": cap}, {"B": np.full(50, 1500.0)}), _cells("nasa", ["B"], [None])
    )
    assert bool(eol.iloc[0].censored) and np.isnan(eol.iloc[0].eol_cycle)


def test_toyota_uses_provider_cycle_life() -> None:
    cap = np.linspace(1.07, 0.9, 30)
    eol = eol_table(
        _cycles("toyota", {"b1c0": cap}, {"b1c0": np.full(30, 600.0)}),
        _cells("toyota", ["b1c0"], [1852.0]),
    )
    row = eol.iloc[0]
    assert row.label_source == "provider" and row.eol_cycle == 1852.0 and not row.censored
    assert np.isclose(row.theta, 0.88 / cap[:5].mean())
