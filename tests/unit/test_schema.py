"""Tests for the canonical data contract (battery_rul.data.schema)."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pandera.errors as pa_errors
import pytest

from battery_rul.data.schema import (
    CyclesSchema,
    add_soh,
    empty_optional_features,
    validate_tables,
)

# Strict-column violations raise SchemaErrors (plural); value checks raise SchemaError.
SCHEMA_ERRORS = (pa_errors.SchemaError, pa_errors.SchemaErrors)


def _cells() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "dataset": ["nasa", "nasa"],
            "cell_id": ["B0005", "B0006"],
            "chemistry": ["unknown (18650 Li-ion)"] * 2,
            "nominal_capacity_ah": [2.0, 2.0],
            "charge_protocol": ["CC 1.5A to 4.2V, CV to 20mA"] * 2,
            "discharge_protocol": ["CC 2A to 2.7V", "CC 2A to 2.5V"],
            "ambient_temp_c": [24.0, 24.0],
            "v_max": [4.2, 4.2],
            "v_min": [2.7, 2.5],
            "batch": [None, None],
            "split": [None, None],
            "reported_cycle_life": [None, None],
            "source_file": ["B0005.mat", "B0006.mat"],
        }
    )


def _cycles(n: int = 8) -> pd.DataFrame:
    rows = []
    for cell, c0 in (("B0005", 1.86), ("B0006", 2.03)):
        for k in range(1, n + 1):
            rows.append(
                {"dataset": "nasa", "cell_id": cell, "cycle_idx": k, "capacity_ah": c0 - 0.01 * k}
            )
    return empty_optional_features(pd.DataFrame(rows))


def _curves() -> pd.DataFrame:
    rows = []
    for cell in ("B0005", "B0006"):
        for k in (1, 2):
            for phase in ("charge", "discharge"):
                for i in range(3):
                    rows.append(
                        {
                            "dataset": "nasa",
                            "cell_id": cell,
                            "cycle_idx": k,
                            "phase": phase,
                            "sample_idx": i,
                            "t_s": 10.0 * i,
                            "voltage_v": 3.7,
                            "current_a": 1.5 if phase == "charge" else -2.0,
                            "temp_c": 25.0,
                            "charge_ah": 0.1 * i,
                        }
                    )
    return pd.DataFrame(rows)


def test_valid_tables_pass() -> None:
    validate_tables(_cells(), add_soh(_cycles()), _curves())


def test_add_soh_uses_first_five_cycles_only() -> None:
    cyc = add_soh(_cycles(n=8))
    b5 = cyc[cyc.cell_id == "B0005"].reset_index(drop=True)
    ref = np.mean([1.86 - 0.01 * k for k in range(1, 6)])
    np.testing.assert_allclose(b5["soh"], b5["capacity_ah"] / ref)


def test_add_soh_is_invariant_to_future_cycles() -> None:
    """Changing late-life capacity must not change early SOH (no look-ahead)."""
    base = add_soh(_cycles(n=8))
    perturbed = _cycles(n=8)
    perturbed.loc[perturbed.cycle_idx > 5, "capacity_ah"] *= 0.5
    pert = add_soh(perturbed)
    early = base.cycle_idx <= 5
    np.testing.assert_allclose(base.loc[early, "soh"], pert.loc[early, "soh"])


def test_duplicate_cycle_rejected() -> None:
    cyc = _cycles()
    cyc = pd.concat([cyc, cyc.iloc[[0]]], ignore_index=True)
    with pytest.raises(SCHEMA_ERRORS):
        CyclesSchema.validate(cyc)


def test_non_positive_capacity_rejected() -> None:
    cyc = _cycles()
    cyc.loc[0, "capacity_ah"] = 0.0
    with pytest.raises(SCHEMA_ERRORS):
        CyclesSchema.validate(cyc)


def test_unknown_column_rejected() -> None:
    cyc = _cycles()
    cyc["rul"] = 1  # labels must not live in the cycles table
    with pytest.raises(SCHEMA_ERRORS):
        CyclesSchema.validate(cyc)


def test_orphan_curve_rejected() -> None:
    curves = _curves()
    curves.loc[0, "cycle_idx"] = 99
    with pytest.raises(ValueError, match="absent from cycles"):
        validate_tables(_cells(), add_soh(_cycles()), curves)


def test_unknown_cell_rejected() -> None:
    cyc = _cycles()
    cyc.loc[0, "cell_id"] = "B9999"
    with pytest.raises(ValueError, match="missing from cells"):
        validate_tables(_cells(), add_soh(cyc), _curves())
