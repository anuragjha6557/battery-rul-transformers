"""Turn canonical cycle tables into model-ready :class:`SampleSet`s (PROTOCOL.md §2-§4).

Pipeline per fold:
    1. :func:`prepare_cycles` - causal cleaning (per-cell forward fill only), derived causal
       channels, train-cells-only standardisation (FoldScaler, leakage rule 1).
    2. :func:`build_samples` - vectorised windowing. A sample with origin cycle ``k`` reads only
       rows with ``cycle_idx <= k`` (Tasks B/C) or ``< k`` plus the *charge* features of ``k``
       (Task A). Targets come from SOH after the origin or from EOL labels.

Never model inputs: absolute ``cycle_idx``, history length (an age proxy), discharge-phase
quantities of the target cycle, non-causal flags. ``meta`` carries bookkeeping only.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Literal

import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view

from battery_rul.models.base import SampleSet, TaskName
from battery_rul.splits.scaling import FoldScaler

FeatureSet = Literal["sc", "mc", "mc_curve", "shared"]
OriginPolicy = Literal["all", "start_points"]

#: Charge-phase / pre-charge per-cycle quantities. Allowed for the current cycle in Task A
#: (they precede discharge k) and for history in every task.
CHARGE_CHANNELS: Final = (
    "charge_throughput_ah",
    "cc_time_s",
    "cv_time_s",
    "charge_time_s",
    "charge_temp_max_c",
    "charge_temp_mean_c",
    "ir_ohm",
    "log_rest_s",  # derived: log1p(rest_before_s)
    "skipped_cv",  # derived, causal: cv_time_s < 300 s on this cycle
)
#: Discharge-phase quantities: near-copies of capacity_k. History-only (cycles < origin for
#: Task A; <= origin for B/C, where capacity itself is observed anyway).
DISCHARGE_CHANNELS: Final = ("discharge_time_s", "discharge_temp_max_c", "discharge_energy_wh")

#: Curve-feature column prefixes (features/curves.py). ``chg_*`` come from the charge curve of
#: cycle k and join the charge family; ``dis_*`` come from the discharge curve and join the
#: discharge family (history-only for Task A).
CURVE_CHARGE_PREFIX: Final = "chg_"
CURVE_DISCHARGE_PREFIX: Final = "dis_"


def is_charge_channel(name: str) -> bool:
    """True for channels that may be used as the current cycle's inputs in Task A."""
    return name in CHARGE_CHANNELS or name.startswith(CURVE_CHARGE_PREFIX)


def merge_curve_features(cycles: pd.DataFrame, feats: pd.DataFrame) -> pd.DataFrame:
    """Left-join cached curve features (keyed dataset, cell_id, cycle_idx) onto ``cycles``."""
    cols = [c for c in feats.columns if c.startswith((CURVE_CHARGE_PREFIX, CURVE_DISCHARGE_PREFIX))]
    keys = ["dataset", "cell_id", "cycle_idx"]
    base = cycles.drop(columns=[c for c in cols if c in cycles.columns])
    return base.merge(feats[[*keys, *cols]], on=keys, how="left")


#: Chemistry-agnostic channels present (finite) in NASA, CALCE *and* Toyota (ADR-0012), in a fixed
#: order so a transferred model sees identical variates in every dataset. Excluded: temperature
#: (all-NaN charge temperature in CALCE/Toyota), rest time (NaN in Toyota), discharge-phase
#: channels (NaN in Toyota) and ``skipped_cv`` (protocol-specific). Each dataset standardises these
#: with its own training cells (the domain-normalisation step).
SHARED_CHANNELS: Final = (
    "ir_ohm",
    "charge_throughput_ah",
    "charge_time_s",
    "cc_time_s",
    "cv_time_s",
)

FIXED_STARTS: Final[dict[str, tuple[int, ...]]] = {
    "nasa": (30, 50),
    "calce": (200, 400),
    "toyota": (100,),
}  # ADR-0005 §4
FRACTION_STARTS: Final = (0.3, 0.5, 0.7)
SKIPPED_CV_S: Final = 300.0
CLIP_Z: Final = 5.0


@dataclass(frozen=True)
class TaskSpec:
    """What to build. Horizons are cycles ahead (Task B only)."""

    task: TaskName
    lookback: int = 32
    horizons: tuple[int, ...] = (1, 10, 25, 50, 100)
    feature_set: FeatureSet = "mc"
    min_history: int = 5

    def __post_init__(self) -> None:
        if self.lookback < 2 or self.min_history < 1:
            raise ValueError("lookback >= 2 and min_history >= 1 required")
        if self.task == "forecast" and (not self.horizons or min(self.horizons) < 1):
            raise ValueError("forecast horizons must be >= 1")

    @property
    def target_horizons(self) -> tuple[int, ...]:
        return self.horizons if self.task == "forecast" else (0,)


@dataclass
class PreparedCycles:
    """Scaled per-cycle table plus the channel bookkeeping a fold needs."""

    cycles: pd.DataFrame  # sorted by cell, cycle; scaled channel columns; NaN -> 0 after scaling
    channels: tuple[str, ...]  # non-SOH history channels actually available
    scaler: FoldScaler | None


def _derive(cycles: pd.DataFrame) -> pd.DataFrame:
    out = cycles.sort_values(["cell_id", "cycle_idx"]).reset_index(drop=True).copy()
    out["log_rest_s"] = np.log1p(out["rest_before_s"].clip(lower=0.0))
    cv = out["cv_time_s"]
    out["skipped_cv"] = np.where(cv.isna(), np.nan, (cv < SKIPPED_CV_S).astype(float))
    return out


def prepare_cycles(
    cycles: pd.DataFrame, train_cells: tuple[str, ...], feature_set: FeatureSet = "mc"
) -> PreparedCycles:
    """Causal cleaning + train-only scaling for one fold.

    A channel is kept if it has any finite value in the *training* cells (availability is
    decided without looking at test cells). Forward fill runs within each cell only, so a
    value never travels backwards in time.
    """
    df = _derive(cycles)
    if feature_set == "sc":
        return PreparedCycles(cycles=df, channels=(), scaler=None)
    candidates = [*CHARGE_CHANNELS, *DISCHARGE_CHANNELS]
    if feature_set == "shared":
        candidates = list(SHARED_CHANNELS)
        absent = [
            c
            for c in candidates
            if c not in df.columns or not df.loc[df["cell_id"].isin(train_cells), c].notna().any()
        ]
        if absent:  # identical channels across datasets is the point: never silently drop
            raise ValueError(f"feature_set 'shared' needs channels with training data: {absent}")
    if feature_set == "mc_curve":
        curve_cols = [
            c for c in df.columns if c.startswith((CURVE_CHARGE_PREFIX, CURVE_DISCHARGE_PREFIX))
        ]
        if not curve_cols:
            raise ValueError(
                "feature_set 'mc_curve' needs curve features; use merge_curve_features"
            )
        candidates += curve_cols
    train_rows = df["cell_id"].isin(train_cells)
    channels = tuple(c for c in candidates if df.loc[train_rows, c].notna().any())
    df[list(channels)] = df.groupby("cell_id", sort=False)[list(channels)].ffill()
    scaler = FoldScaler().fit(df, train_cells, list(channels))
    scaled = scaler.transform(df)
    scaled[list(channels)] = scaled[list(channels)].clip(-CLIP_Z, CLIP_Z).fillna(0.0)
    return PreparedCycles(cycles=scaled, channels=channels, scaler=scaler)


def _windows(values: np.ndarray, lookback: int) -> tuple[np.ndarray, np.ndarray]:
    """For an (n, C) per-cycle array, return (n, L, C) windows ending at each row and the
    (n, L) validity mask (left-padded with NaN / False)."""
    n, c = values.shape
    padded = np.vstack([np.full((lookback - 1, c), np.nan), values])
    win = sliding_window_view(padded, (lookback, c))[:, 0]  # (n, L, C)
    valid = np.concatenate([np.zeros(lookback - 1, bool), np.ones(n, bool)])
    mask = sliding_window_view(valid, lookback)  # (n, L)
    return win, mask


def _origin_positions(
    ci: np.ndarray, eol: float, dataset: str, policy: OriginPolicy, first_ok: int
) -> list[tuple[int, str]]:
    """(position, start_kind) pairs for one cell."""
    if policy == "all":
        return [(p, "all") for p in range(first_ok, len(ci))]
    out: list[tuple[int, str]] = []
    targets: list[tuple[float, str]] = [(t, f"fixed:{t}") for t in FIXED_STARTS[dataset]]
    if np.isfinite(eol):
        targets += [(round(lam * eol), f"frac:{lam}") for lam in FRACTION_STARTS]
    for t, kind in targets:
        pos = int(np.searchsorted(ci, t, side="right")) - 1  # last cycle <= t
        if pos >= first_ok:
            out.append((pos, kind))
    return out


def build_samples(
    prepared: PreparedCycles,
    cells: tuple[str, ...],
    eol: pd.DataFrame,
    spec: TaskSpec,
    origins: OriginPolicy = "all",
) -> SampleSet:
    """Window the prepared cycles of ``cells`` into a SampleSet for ``spec.task``.

    ``eol`` is :func:`battery_rul.tasks.labels.eol_table` output (targets only).
    """
    df = prepared.cycles
    dataset = str(df["dataset"].iloc[0])
    eol_by_cell = eol.set_index("cell_id")["eol_cycle"]
    theta_by_cell = (
        eol.set_index("cell_id")["theta"] if "theta" in eol.columns else pd.Series(dtype=float)
    )
    hist_channels = ("soh", *prepared.channels)
    task_a_now = tuple(c for c in prepared.channels if is_charge_channel(c))
    L, task = spec.lookback, spec.task
    H = spec.target_horizons

    xs, ms, tabs, ys, ymasks, metas = [], [], [], [], [], []
    for cell in cells:
        g = df[df["cell_id"] == cell]
        if g.empty:
            raise ValueError(f"cell {cell!r} not in prepared cycles")
        ci = g["cycle_idx"].to_numpy()
        soh = g["soh"].to_numpy(dtype=np.float64)
        hist_vals = g[list(hist_channels)].to_numpy(dtype=np.float64)
        win, wmask = _windows(hist_vals, L)
        cell_eol = float(eol_by_cell.get(cell, np.nan))

        # Task A: the window must end at k-1, so it needs min_history rows before k.
        first_ok = spec.min_history if task == "soh" else spec.min_history - 1
        positions = _origin_positions(ci, cell_eol, dataset, origins, first_ok)
        if task == "rul":
            positions = [(p, k) for p, k in positions if np.isfinite(cell_eol) and ci[p] < cell_eol]
        if not positions:
            continue
        pos = np.array([p for p, _ in positions])
        kinds = [k for _, k in positions]

        if task == "soh":
            x, m = win[pos - 1], wmask[pos - 1]  # history ends at k-1
            now = g[list(task_a_now)].to_numpy(dtype=np.float64)[pos]  # charge of cycle k
            last = soh[pos - 1][:, None]
            tab = np.hstack([now, last])
            y = soh[pos][:, None]
            ym = np.ones_like(y, dtype=bool)
        else:
            x, m = win[pos], wmask[pos]
            tab = _summary_features(soh, pos)
            if task == "forecast":
                lookup = {int(c): i for i, c in enumerate(ci)}
                y = np.full((len(pos), len(H)), np.nan)
                for j, h in enumerate(H):
                    tgt = [lookup.get(int(ci[p]) + h) for p in pos]
                    y[:, j] = [soh[t] if t is not None else np.nan for t in tgt]
                ym = np.isfinite(y)
                y = np.nan_to_num(y)
            else:  # rul
                y = (cell_eol - ci[pos].astype(np.float64))[:, None]
                ym = np.ones_like(y, dtype=bool)

        xs.append(x)
        ms.append(m)
        tabs.append(tab)
        ys.append(y)
        ymasks.append(ym)
        metas.append(
            pd.DataFrame(
                {
                    "dataset": dataset,
                    "cell_id": cell,
                    "origin_cycle": ci[pos],
                    "start_kind": kinds,
                    "eol_cycle": cell_eol,
                    # per-cell SOH threshold for trajectory-crossing RUL (Toyota: 0.88 Ah / C_ref)
                    "theta": float(theta_by_cell.get(cell, np.nan)),
                }
            )
        )

    tab_names = (
        (*[f"now_{c}" for c in task_a_now], "last_soh") if task == "soh" else SUMMARY_FEATURES
    )
    if not xs:
        raise ValueError(f"no samples for task {task!r} in cells {cells}")
    return SampleSet(
        task=task,
        x_hist=np.concatenate(xs).astype(np.float32),
        hist_mask=np.concatenate(ms),
        x_tab=np.concatenate(tabs).astype(np.float32),
        y=np.concatenate(ys).astype(np.float32),
        y_mask=np.concatenate(ymasks),
        horizons=H,
        channel_names=hist_channels,
        feature_names=tuple(tab_names),
        meta=pd.concat(metas, ignore_index=True),
    )


SUMMARY_FEATURES: Final = ("last_soh", "mean_soh_5", "slope_10", "slope_50", "curv_50")


def _slope(y: np.ndarray) -> float:
    if y.size < 2:
        return 0.0
    x = np.arange(y.size, dtype=np.float64)
    return float(np.polyfit(x, y, 1)[0])


def _summary_features(soh: np.ndarray, pos: np.ndarray) -> np.ndarray:
    """Causal SOH-trajectory summaries at each origin (only rows <= origin)."""
    out = np.empty((len(pos), len(SUMMARY_FEATURES)))
    for i, p in enumerate(pos):
        h = soh[: p + 1]
        tail50 = h[-50:]
        curv = float(np.polyfit(np.arange(tail50.size), tail50, 2)[0]) if tail50.size >= 3 else 0.0
        out[i] = (h[-1], h[-5:].mean(), _slope(h[-10:]), _slope(tail50), curv)
    return out
