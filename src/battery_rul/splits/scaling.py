"""Train-only feature standardisation (PROTOCOL.md §4 leakage rule 1)."""

from __future__ import annotations

import warnings
from collections.abc import Iterable, Sequence

import numpy as np
import pandas as pd


class FoldScaler:
    """Standardise columns using statistics of the training cells only.

    ``fit`` uses ONLY rows whose ``cell_id`` is in ``train_cells``; every other row is ignored
    (even NaN or extreme values there cannot change the result). NaNs are ignored when fitting
    and preserved when transforming. Attributes after fit: ``mean_`` and ``scale_``
    (``pd.Series`` indexed by column, float64; population std, constant columns get scale 1.0),
    ``fitted_cells_`` (sorted tuple) and ``columns_``.
    """

    def __init__(self) -> None:
        self.mean_: pd.Series | None = None
        self.scale_: pd.Series | None = None
        self.fitted_cells_: tuple[str, ...] = ()
        self.columns_: tuple[str, ...] = ()

    def fit(
        self, df: pd.DataFrame, train_cells: Iterable[str], columns: Sequence[str]
    ) -> FoldScaler:
        cells = tuple(sorted(set(train_cells)))
        cols = tuple(columns)
        if "cell_id" not in df.columns:
            raise ValueError("df lacks a 'cell_id' column")
        if not cells:
            raise ValueError("train_cells is empty")
        if not cols:
            raise ValueError("columns is empty")
        missing_cols = [c for c in cols if c not in df.columns]
        if missing_cols:
            raise ValueError(f"columns not in df: {missing_cols}")
        absent = sorted(set(cells) - set(df["cell_id"].astype(str)))
        if absent:
            raise ValueError(f"train cells absent from df: {absent}")
        sub = df.loc[df["cell_id"].isin(cells), list(cols)].to_numpy(dtype=np.float64)
        if sub.shape[0] == 0:
            raise ValueError("no training rows")
        if np.any(np.all(np.isnan(sub), axis=0)):
            bad = [c for c, a in zip(cols, np.all(np.isnan(sub), axis=0), strict=True) if a]
            raise ValueError(f"columns entirely NaN in training rows: {bad}")
        mean = np.nanmean(sub, axis=0)
        scale = np.nanstd(sub, axis=0)
        const = scale == 0.0
        if const.any():
            names = [c for c, k in zip(cols, const, strict=True) if k]
            warnings.warn(
                f"constant columns in training rows, scale set to 1.0: {names}", stacklevel=2
            )
            scale = np.where(const, 1.0, scale)
        self.mean_ = pd.Series(mean, index=list(cols), dtype=np.float64)
        self.scale_ = pd.Series(scale, index=list(cols), dtype=np.float64)
        self.fitted_cells_ = cells
        self.columns_ = cols
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Return a copy of ``df`` with the fitted columns standardised (NaN preserved)."""
        if self.mean_ is None or self.scale_ is None:
            raise RuntimeError("FoldScaler is not fitted")
        missing = [c for c in self.columns_ if c not in df.columns]
        if missing:
            raise ValueError(f"columns not in df: {missing}")
        out = df.copy()
        for c in self.columns_:
            out[c] = (out[c].astype(np.float64) - self.mean_[c]) / self.scale_[c]
        return out
