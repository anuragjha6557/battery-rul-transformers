"""Statistics and aggregation (PROTOCOL.md §8): cluster bootstrap, consistency, Wilcoxon, ranks.

Per-cell arrays hold one value per seed (e.g. the 5 seeds' RMSE for that cell). All inputs are
validated; NaN raises ``ValueError``.
"""

from __future__ import annotations

import logging
from collections.abc import Callable, Mapping
from dataclasses import dataclass

import numpy as np
import pandas as pd
from numpy.typing import ArrayLike, NDArray
from scipy import stats as sps

logger = logging.getLogger(__name__)

FloatArray = NDArray[np.float64]


def _cell_arrays(name: str, by_cell: Mapping[str, ArrayLike]) -> dict[str, FloatArray]:
    if len(by_cell) == 0:
        raise ValueError(f"{name} is empty")
    out: dict[str, FloatArray] = {}
    for cell, v in by_cell.items():
        a = np.atleast_1d(np.asarray(v, dtype=np.float64))
        if a.ndim != 1 or a.size == 0:
            raise ValueError(f"{name}[{cell!r}] must be a non-empty 1-D array, got {a.shape}")
        if not np.all(np.isfinite(a)):
            raise ValueError(f"{name}[{cell!r}] contains NaN or inf")
        out[cell] = a
    return out


@dataclass(frozen=True)
class CI:
    """Point estimate with a percentile interval (same units as the statistic)."""

    estimate: float
    lo: float
    hi: float
    n_clusters: int


def cluster_bootstrap_ci(
    values_by_cell: Mapping[str, ArrayLike],
    stat: Callable[[FloatArray], float] = np.mean,
    n_boot: int = 10_000,
    level: float = 0.95,
    seed: int = 0,
) -> CI:
    """Cluster (cell-level) bootstrap percentile CI.

    Resamples *cells* with replacement, pools all their seed-values, applies ``stat``.
    ``estimate`` is ``stat`` on all data. Deterministic given ``seed``. With few cells the
    interval is wide by construction (e.g. n = 4).
    """
    cells = _cell_arrays("values_by_cell", values_by_cell)
    if n_boot < 1:
        raise ValueError("n_boot must be >= 1")
    if not 0.0 < level < 1.0:
        raise ValueError("level must lie in (0, 1)")
    arrays = list(cells.values())
    k = len(arrays)
    estimate = float(stat(np.concatenate(arrays)))
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, k, size=(n_boot, k))
    boots = np.empty(n_boot, dtype=np.float64)
    for b in range(n_boot):
        boots[b] = stat(np.concatenate([arrays[i] for i in idx[b]]))
    alpha = (1.0 - level) / 2.0
    lo, hi = np.quantile(boots, [alpha, 1.0 - alpha])
    return CI(estimate=estimate, lo=float(lo), hi=float(hi), n_clusters=k)


@dataclass(frozen=True)
class Consistency:
    """Direction consistency of a model vs a baseline ("k/4 cells, k/20 cell-seeds")."""

    k_cells: int  #: cells where the model's mean beats the baseline's mean
    n_cells: int
    k_pairs: int  #: (cell, seed) pairs where the model beats the baseline
    n_pairs: int


def direction_consistency(
    model_by_cell: Mapping[str, ArrayLike],
    base_by_cell: Mapping[str, ArrayLike],
    lower_is_better: bool = True,
) -> Consistency:
    """Count cells (by mean) and (cell, seed) pairs where the model strictly beats the baseline.

    Per-cell arrays must have the same length and be aligned by seed. Ties do not count.
    """
    m = _cell_arrays("model_by_cell", model_by_cell)
    b = _cell_arrays("base_by_cell", base_by_cell)
    if set(m) != set(b):
        raise ValueError(f"cell sets differ: {sorted(set(m) ^ set(b))}")
    sign = 1.0 if lower_is_better else -1.0
    k_cells = k_pairs = n_pairs = 0
    for cell, mv in m.items():
        bv = b[cell]
        if mv.shape != bv.shape:
            raise ValueError(f"cell {cell!r}: model {mv.shape} vs baseline {bv.shape} seeds")
        k_cells += int(sign * (mv.mean() - bv.mean()) < 0.0)
        k_pairs += int(np.sum(sign * (mv - bv) < 0.0))
        n_pairs += mv.size
    return Consistency(k_cells=k_cells, n_cells=len(m), k_pairs=k_pairs, n_pairs=n_pairs)


def holm_adjust(pvals: ArrayLike) -> FloatArray:
    """Holm-Bonferroni adjusted p-values (same order as input), clipped to [0, 1].

    Adjusted p is always >= raw p and monotone non-decreasing in raw p.
    """
    p = np.asarray(pvals, dtype=np.float64)
    if p.ndim != 1 or p.size == 0:
        raise ValueError("pvals must be a non-empty 1-D array")
    if np.any(np.isnan(p)) or np.any(p < 0.0) or np.any(p > 1.0):
        raise ValueError("pvals must lie in [0, 1]")
    m = p.size
    order = np.argsort(p, kind="stable")
    scaled = (m - np.arange(m)) * p[order]
    adj_sorted = np.minimum(np.maximum.accumulate(scaled), 1.0)
    out = np.empty(m, dtype=np.float64)
    out[order] = adj_sorted
    return out


def wilcoxon_vs_baseline(baseline: ArrayLike, others: Mapping[str, ArrayLike]) -> dict[str, float]:
    """Paired two-sided Wilcoxon signed-rank test of each model vs the baseline, Holm-adjusted.

    ``baseline`` and every entry of ``others`` are paired per-cell scores (same cell order).
    Returns ``{model: holm_adjusted_p}`` in the order of ``others``. If a model's scores equal
    the baseline's everywhere the raw p is 1.0. Zero differences are dropped (scipy 'wilcox').
    """
    base = np.asarray(baseline, dtype=np.float64)
    if base.ndim != 1 or base.size == 0:
        raise ValueError("baseline must be a non-empty 1-D array")
    if not np.all(np.isfinite(base)):
        raise ValueError("baseline contains NaN or inf")
    if len(others) == 0:
        raise ValueError("others is empty")
    raw: list[float] = []
    for name, v in others.items():
        x = np.asarray(v, dtype=np.float64)
        if x.shape != base.shape:
            raise ValueError(f"{name!r}: shape {x.shape} vs baseline {base.shape}")
        if not np.all(np.isfinite(x)):
            raise ValueError(f"{name!r} contains NaN or inf")
        if np.all(x - base == 0.0):
            raw.append(1.0)
        else:
            raw.append(float(sps.wilcoxon(x, base, alternative="two-sided").pvalue))
    adj = holm_adjust(np.array(raw))
    return {name: float(a) for name, a in zip(others, adj, strict=True)}


def mean_rank(scores: pd.DataFrame, lower_is_better: bool = True) -> pd.Series:
    """Mean rank of each model across conditions (Demsar 2006).

    ``scores``: rows = models, columns = conditions (dataset x task x metric). Within each
    condition models are ranked 1..M (ties get the average rank); a NaN score is skipped, so
    that model is simply absent from that condition's ranking and from its mean. Mean ranks of
    models with different numbers of valid conditions are not strictly comparable, so a warning
    is logged and the per-model count of skipped conditions is attached as
    ``result.attrs["n_missing"]``.
    """
    if scores.empty:
        raise ValueError("scores is empty")
    ranks = scores.astype(np.float64).rank(axis=0, method="average", ascending=lower_is_better)
    result = ranks.mean(axis=1, skipna=True)
    result.name = "mean_rank"
    n_missing = {str(k): int(v) for k, v in scores.isna().sum(axis=1).items()}
    result.attrs["n_missing"] = n_missing
    skipped = {k: v for k, v in n_missing.items() if v}
    if skipped:
        logger.warning("mean_rank skipped NaN conditions per model: %s", skipped)
    return result
