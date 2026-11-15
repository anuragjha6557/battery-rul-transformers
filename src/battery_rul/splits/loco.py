"""Leave-one-cell-out splits with cross-fitted inner folds (PROTOCOL.md §3, CV+)."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from battery_rul.data.schema import DATASETS


@dataclass(frozen=True)
class InnerFold:
    """One inner fold: train on ``train``, early-stop / calibrate on the held-out ``val`` cell."""

    train: tuple[str, ...]
    val: str


@dataclass(frozen=True)
class Fold:
    """One outer LOCO fold. ``inner`` has one InnerFold per training cell (CV+)."""

    test: str
    train: tuple[str, ...]
    inner: tuple[InnerFold, ...]


def loco_folds(cell_ids: Sequence[str]) -> list[Fold]:
    """Outer leave-one-cell-out folds, each with inner LOCO over its training cells.

    Deterministic: cell ids are sorted, folds are returned in that order, and all tuples are
    sorted. Requires at least 3 unique cells (so the inner loop trains on >= 1 cell).
    """
    ids = sorted(cell_ids)
    if len(set(ids)) != len(ids):
        raise ValueError("cell_ids must be unique")
    if len(ids) < 3:
        raise ValueError(f"LOCO with inner folds needs >= 3 cells, got {len(ids)}")
    folds: list[Fold] = []
    for test in ids:
        train = tuple(c for c in ids if c != test)
        inner = tuple(InnerFold(train=tuple(c for c in train if c != v), val=v) for v in train)
        folds.append(Fold(test=test, train=train, inner=inner))
    return folds


def independent_fold_cells(dataset: str, cell_ids: Sequence[str] | None = None) -> tuple[str, ...]:
    """Cells whose test fold is rig-independent and reported separately (PROTOCOL §3).

    NASA: ``("B0018",)`` (B0005/6/7 share one rig). Other datasets: every cell, so
    ``cell_ids`` must be supplied. CALCE cells were checked and do not share a schedule
    (cross-cell dSOH rho in [-0.08, 0.12]; ADR-0005).
    """
    if dataset not in DATASETS:
        raise ValueError(f"unknown dataset {dataset!r}; expected one of {DATASETS}")
    if dataset == "nasa":
        return ("B0018",)
    if cell_ids is None:
        raise ValueError(f"cell_ids is required for dataset {dataset!r}")
    return tuple(sorted(cell_ids))
