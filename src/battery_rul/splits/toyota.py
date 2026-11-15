"""Toyota/MIT/Stanford splits (PROTOCOL.md §3): official split and grouped k-fold by cell."""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np
import pandas as pd

from battery_rul.data.schema import SPLITS


def official_split(cells: pd.DataFrame) -> dict[str, tuple[str, ...]]:
    """Group cell ids by the published split column.

    Returns ``{"train": ..., "test1": ..., "test2": ...}`` with sorted tuples (a split with no
    cells maps to an empty tuple). Raises if the ``cells`` table lacks ``cell_id`` / ``split``
    or any cell has no split label.
    """
    for col in ("cell_id", "split"):
        if col not in cells.columns:
            raise ValueError(f"cells table lacks column {col!r}")
    if cells.empty:
        raise ValueError("cells table is empty")
    if cells["split"].isna().any():
        raise ValueError("some cells have no split label")
    unknown = set(cells["split"]) - set(SPLITS)
    if unknown:
        raise ValueError(f"unknown split labels: {sorted(unknown)}")
    return {s: tuple(sorted(cells.loc[cells["split"] == s, "cell_id"].astype(str))) for s in SPLITS}


def grouped_kfold(
    cell_ids: Sequence[str], k: int = 5, seed: int = 0
) -> list[tuple[tuple[str, ...], tuple[str, ...]]]:
    """Deterministic k-fold over cells: returns ``[(train, val), ...]``.

    Every cell is in exactly one val fold; fold sizes differ by at most 1. Cells are sorted,
    shuffled with ``default_rng(seed)``, then split.
    """
    ids = sorted(cell_ids)
    if len(set(ids)) != len(ids):
        raise ValueError("cell_ids must be unique")
    if k < 2:
        raise ValueError("k must be >= 2")
    if len(ids) < k:
        raise ValueError(f"need at least k={k} cells, got {len(ids)}")
    perm = np.random.default_rng(seed).permutation(len(ids))
    out: list[tuple[tuple[str, ...], tuple[str, ...]]] = []
    for part in np.array_split(perm, k):
        val_set = {ids[i] for i in part}
        val = tuple(sorted(val_set))
        train = tuple(c for c in ids if c not in val_set)
        out.append((train, val))
    return out
