"""Read/write the canonical processed tables (contract: battery_rul.data.schema)."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from battery_rul.data.schema import add_soh, empty_optional_features, validate_tables
from battery_rul.utils import PROCESSED_DIR

TABLES = ("cells", "cycles", "curves")


@dataclass(frozen=True)
class DatasetTables:
    cells: pd.DataFrame
    cycles: pd.DataFrame
    curves: pd.DataFrame


def finalize_and_validate(
    cells: pd.DataFrame, cycles: pd.DataFrame, curves: pd.DataFrame
) -> DatasetTables:
    """Fill optional columns, compute SOH centrally, sort, validate everything."""
    cycles = add_soh(empty_optional_features(cycles))
    cycles = cycles.sort_values(["dataset", "cell_id", "cycle_idx"]).reset_index(drop=True)
    curves = curves.sort_values(
        ["dataset", "cell_id", "cycle_idx", "phase", "sample_idx"]
    ).reset_index(drop=True)
    cells = cells.sort_values(["dataset", "cell_id"]).reset_index(drop=True)
    c, y, v = validate_tables(cells, cycles, curves)
    return DatasetTables(cells=c, cycles=y, curves=v)


def write_tables(dataset: str, tables: DatasetTables, root: Path = PROCESSED_DIR) -> Path:
    """Write validated tables to ``<root>/<dataset>/{cells,cycles,curves}.parquet``."""
    out = root / dataset
    out.mkdir(parents=True, exist_ok=True)
    for name in TABLES:
        getattr(tables, name).to_parquet(out / f"{name}.parquet", index=False)
    return out


def read_tables(dataset: str, root: Path = PROCESSED_DIR, curves: bool = True) -> DatasetTables:
    """Load processed tables (curves optional — they are the large one)."""
    d = root / dataset
    if not (d / "cycles.parquet").exists():
        raise FileNotFoundError(
            f"{d} has no processed tables; run `battery-rul build-data {dataset}`"
        )
    return DatasetTables(
        cells=pd.read_parquet(d / "cells.parquet"),
        cycles=pd.read_parquet(d / "cycles.parquet"),
        curves=pd.read_parquet(d / "curves.parquet") if curves else pd.DataFrame(),
    )
