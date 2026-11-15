"""Canonical data contract shared by every loader, the feature builder and the serving layer.

Every dataset loader (``nasa.py``, ``calce.py``, ``toyota.py``) must emit exactly three
tables, validated by the pandera models below, written to
``data/processed/<dataset>/{cells,cycles,curves}.parquet``:

``cells``   one row per physical cell — static metadata.
``cycles``  one row per *aging cycle* that has a capacity measurement — scalar
            per-cycle quantities. Loaders fill the raw columns; ``soh`` is added
            centrally by :func:`add_soh` so the normalization rule lives in one place.
``curves``  long-format raw time series per cycle and phase (charge / discharge),
            lightly decimated. Voltage-grid resampling, ICA and ΔQ(V) are *feature*
            concerns (``battery_rul.features``), not loader concerns.

Conventions (units are part of the contract):
- ``cycle_idx`` is the cell's equivalent full-cycle count, 1-based and strictly
  increasing. Gaps are allowed (dropped junk cycles keep their place in the count,
  so RUL in cycles stays physically meaningful).
- Currents in A with **charge positive, discharge negative**; voltage in V;
  temperature in °C; time in s from the start of the phase; charge in Ah,
  cumulative within the phase, always non-negative.
- Cycle ``k`` pairs the charge that *precedes* discharge ``k`` with discharge ``k``
  (the discharge is what measures ``capacity_ah``).
- No label columns (EOL, RUL) here: labels are task-dependent and are built in
  ``battery_rul.tasks`` so the leakage rules can be enforced in one place.
"""

from __future__ import annotations

from typing import Final

import pandas as pd
import pandera.pandas as pa
from pandera.typing.pandas import Series

DATASETS: Final = ("nasa", "calce", "toyota")
PHASES: Final = ("charge", "discharge")
SPLITS: Final = ("train", "test1", "test2")  # Severson official split (Toyota only)

#: Number of earliest cycles whose mean capacity defines SOH = 1 for a cell.
SOH_REFERENCE_CYCLES: Final = 5

#: Optional per-cycle scalar features a loader *may* fill (NaN when unavailable).
OPTIONAL_CYCLE_FEATURES: Final = (
    "charge_time_s",  # total charge-phase duration
    "cc_time_s",  # duration of the constant-current part of the charge
    "cv_time_s",  # duration of the constant-voltage part of the charge
    "charge_throughput_ah",  # Ah delivered during the charge phase
    "charge_temp_max_c",
    "charge_temp_mean_c",
    "discharge_time_s",
    "discharge_temp_max_c",
    "discharge_energy_wh",
    "ir_ohm",  # internal resistance; NASA: Re+Rct of the latest EIS *before* this cycle's charge
    "rest_before_s",  # idle time between previous discharge end and this charge start
)


class CellsSchema(pa.DataFrameModel):
    """Static per-cell metadata."""

    dataset: Series[str] = pa.Field(isin=DATASETS)
    cell_id: Series[str] = pa.Field(unique=True)
    chemistry: Series[str]  # e.g. "LCO/graphite", "LFP/graphite", "NCA? (unknown)" — say unknown
    nominal_capacity_ah: Series[float] = pa.Field(gt=0)
    charge_protocol: Series[str]  # human-readable, e.g. "CC 1.5A to 4.2V, CV to 20mA"
    discharge_protocol: Series[str]
    ambient_temp_c: Series[float] = pa.Field(nullable=True)
    v_max: Series[float] = pa.Field(gt=0)  # charge cut-off voltage
    v_min: Series[float] = pa.Field(gt=0)  # discharge cut-off voltage
    batch: Series[str] = pa.Field(nullable=True)  # Toyota batch date; NaN elsewhere
    split: Series[str] = pa.Field(nullable=True, isin=SPLITS)  # Toyota only
    # Cycle life as reported by the data provider (Toyota: cycles to 0.88 Ah). Kept only for
    # literature comparability; our own EOL labels are computed in battery_rul.tasks.
    reported_cycle_life: Series[float] = pa.Field(nullable=True, gt=0)
    source_file: Series[str]

    class Config:
        coerce = True
        strict = True


class CyclesSchema(pa.DataFrameModel):
    """One row per aging cycle with a capacity measurement."""

    dataset: Series[str] = pa.Field(isin=DATASETS)
    cell_id: Series[str]
    cycle_idx: Series[int] = pa.Field(ge=1)
    capacity_ah: Series[float] = pa.Field(gt=0)
    soh: Series[float] = pa.Field(nullable=True, gt=0)  # filled by add_soh()

    charge_time_s: Series[float] = pa.Field(nullable=True, ge=0)
    cc_time_s: Series[float] = pa.Field(nullable=True, ge=0)
    cv_time_s: Series[float] = pa.Field(nullable=True, ge=0)
    charge_throughput_ah: Series[float] = pa.Field(nullable=True, ge=0)
    charge_temp_max_c: Series[float] = pa.Field(nullable=True)
    charge_temp_mean_c: Series[float] = pa.Field(nullable=True)
    discharge_time_s: Series[float] = pa.Field(nullable=True, ge=0)
    discharge_temp_max_c: Series[float] = pa.Field(nullable=True)
    discharge_energy_wh: Series[float] = pa.Field(nullable=True, ge=0)
    ir_ohm: Series[float] = pa.Field(nullable=True, ge=0)
    rest_before_s: Series[float] = pa.Field(nullable=True, ge=0)

    class Config:
        coerce = True
        strict = True

    @pa.dataframe_check
    @classmethod
    def unique_cycle_per_cell(cls, df: pd.DataFrame) -> bool:
        return not df.duplicated(["dataset", "cell_id", "cycle_idx"]).any()

    @pa.dataframe_check
    @classmethod
    def cycle_idx_strictly_increasing(cls, df: pd.DataFrame) -> bool:
        return bool(
            df.groupby(["dataset", "cell_id"], sort=False)["cycle_idx"]
            .apply(lambda s: s.is_monotonic_increasing and s.is_unique)
            .all()
        )


class CurvesSchema(pa.DataFrameModel):
    """Long-format raw curves: one row per (cell, cycle, phase, sample)."""

    dataset: Series[str] = pa.Field(isin=DATASETS)
    cell_id: Series[str]
    cycle_idx: Series[int] = pa.Field(ge=1)
    phase: Series[str] = pa.Field(isin=PHASES)
    sample_idx: Series[int] = pa.Field(ge=0)
    t_s: Series[float] = pa.Field(nullable=True, ge=0)  # NaN when only V-grid data exist (Toyota)
    voltage_v: Series[float] = pa.Field(nullable=True)
    current_a: Series[float] = pa.Field(nullable=True)
    temp_c: Series[float] = pa.Field(nullable=True)
    charge_ah: Series[float] = pa.Field(nullable=True, ge=0)

    class Config:
        coerce = True
        strict = True

    @pa.dataframe_check
    @classmethod
    def unique_sample(cls, df: pd.DataFrame) -> bool:
        key = ["dataset", "cell_id", "cycle_idx", "phase", "sample_idx"]
        return not df.duplicated(key).any()


def empty_optional_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add any missing optional feature column as NaN (loaders call this before validation)."""
    out = df.copy()
    for col in OPTIONAL_CYCLE_FEATURES:
        if col not in out.columns:
            out[col] = float("nan")
    if "soh" not in out.columns:
        out["soh"] = float("nan")
    return out


def add_soh(cycles: pd.DataFrame, n_ref: int = SOH_REFERENCE_CYCLES) -> pd.DataFrame:
    """Return a copy with ``soh = capacity_ah / mean(capacity of the cell's first n_ref cycles)``.

    Uses only each cell's own earliest cycles, so it never looks into the future
    relative to any prediction point after cycle ``n_ref``. See ADR-0005.
    """
    out = cycles.sort_values(["dataset", "cell_id", "cycle_idx"]).copy()
    ref = out.groupby(["dataset", "cell_id"], sort=False)["capacity_ah"].transform(
        lambda s: s.iloc[:n_ref].mean()
    )
    out["soh"] = out["capacity_ah"] / ref
    return out


def validate_tables(
    cells: pd.DataFrame, cycles: pd.DataFrame, curves: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Validate all three tables plus cross-table referential integrity."""
    cells_v = CellsSchema.validate(cells)
    cycles_v = CyclesSchema.validate(cycles)
    curves_v = CurvesSchema.validate(curves)

    known = set(cells_v["cell_id"])
    for name, tbl in (("cycles", cycles_v), ("curves", curves_v)):
        unknown = set(tbl["cell_id"]) - known
        if unknown:
            raise ValueError(f"{name} references cells missing from cells table: {sorted(unknown)}")

    cyc_keys = set(map(tuple, cycles_v[["cell_id", "cycle_idx"]].to_numpy().tolist()))
    curve_keys = set(
        map(tuple, curves_v[["cell_id", "cycle_idx"]].drop_duplicates().to_numpy().tolist())
    )
    orphan = curve_keys - cyc_keys
    if orphan:
        raise ValueError(f"curves contain {len(orphan)} (cell, cycle) pairs absent from cycles")
    return cells_v, cycles_v, curves_v
