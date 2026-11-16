"""Interval metrics on long calibrated frames, and the wide<->long glue for runner artifacts.

Lives in ``uq/`` (not ``eval/metrics.py``) because it operates on the long-format frames produced
by :func:`battery_rul.uq.conformal.calibrate_cv_plus`; the array-level primitives (``picp``,
``mpiw``) are reused from ``eval.metrics``. Width / interval-score units: %SOH for the ``soh``
and ``forecast`` tasks (``scale = 100`` on SOH fractions), cycles for ``rul``.
"""

from __future__ import annotations

import re
from collections.abc import Sequence

import numpy as np
import pandas as pd

from battery_rul.eval.metrics import mpiw, picp
from battery_rul.uq.conformal import calibrate_cv_plus

#: Nominal miscoverage levels of the reliability diagram (PROTOCOL §5).
RELIABILITY_ALPHAS: tuple[float, ...] = (0.5, 0.2, 0.1, 0.05)
_PRED = re.compile(r"^(y|y_mask|point)_h(-?\d+)$|^q([0-9.]+)_h(-?\d+)$")


def scale_for(task: str) -> float:
    """Multiplier to report widths in %SOH (soh, forecast) or cycles (rul)."""
    return 1.0 if task == "rul" else 100.0


def interval_levels(
    levels: Sequence[float], alpha: float, tol: float = 1e-9
) -> tuple[float, float] | None:
    """The stored quantile levels ``(alpha/2, 1 - alpha/2)`` or None if not both present."""
    lo, hi = alpha / 2.0, 1.0 - alpha / 2.0
    has = lambda t: any(abs(t - lv) < tol for lv in levels)  # noqa: E731
    return (lo, hi) if has(lo) and has(hi) else None


def wide_to_long(frame: pd.DataFrame, alpha: float | None) -> pd.DataFrame:
    """Runner prediction frame (wide, ``*_h{H}`` columns) -> long ``(row, horizon)`` frame.

    Columns ``horizon, y, mask, point, lo, hi`` are added to the metadata columns. ``lo``/``hi``
    are the stored quantiles at ``(alpha/2, 1 - alpha/2)``; NaN if the model is point-only or
    ``alpha`` is None. Raises ValueError if the frame holds quantiles but not that pair.
    """
    horizons = sorted(
        int(m.group(2)) for c in frame.columns if (m := re.match(r"^(y)_h(-?\d+)$", c))
    )
    meta_cols = [c for c in frame.columns if not _PRED.match(c)]
    levels = sorted(
        {float(m.group(3)) for c in frame.columns if (m := _PRED.match(c)) and m.group(3)}
    )
    pair = None
    if alpha is not None and levels:
        pair = interval_levels(levels, alpha)
        if pair is None:
            raise ValueError(f"alpha={alpha} needs quantile levels it lacks (have {levels})")
    parts = []
    for h in horizons:
        d = frame[meta_cols].copy()
        d["horizon"] = h
        d["y"] = frame[f"y_h{h}"].to_numpy(dtype=np.float64)
        d["mask"] = frame[f"y_mask_h{h}"].to_numpy(dtype=bool)
        d["point"] = frame[f"point_h{h}"].to_numpy(dtype=np.float64)
        if pair is not None:
            d["lo"] = frame[f"q{pair[0]:g}_h{h}"].to_numpy(dtype=np.float64)
            d["hi"] = frame[f"q{pair[1]:g}_h{h}"].to_numpy(dtype=np.float64)
        else:
            d["lo"] = d["hi"] = np.nan
        parts.append(d)
    return pd.concat(parts, ignore_index=True)


def interval_score(y: np.ndarray, lo: np.ndarray, hi: np.ndarray, alpha: float) -> float:
    """Mean Winkler / interval score (Gneiting & Raftery 2007): width + 2/alpha * miss distance."""
    y, lo, hi = (np.asarray(a, dtype=np.float64) for a in (y, lo, hi))
    s = (hi - lo) + (2.0 / alpha) * (np.maximum(lo - y, 0.0) + np.maximum(y - hi, 0.0))
    return float(np.mean(s))


def interval_table(
    long: pd.DataFrame,
    lo_col: str,
    hi_col: str,
    alpha: float,
    scale: float = 100.0,
    per_cell: bool = True,
) -> pd.DataFrame:
    """PICP / MPIW / interval score per ``(split, policy, kind, [cell,] horizon)``.

    ``kind`` is ``overall`` plus each start kind (as the runner's metrics). Rows with
    ``mask`` False, non-finite targets or non-finite interval ends are dropped; groups with an
    infinite interval report ``picp`` normally and ``mpiw = iscore = inf``. MPIW and interval
    score are multiplied by ``scale``.
    """
    d = long[long["mask"].astype(bool)]
    d = d[np.isfinite(d["y"]) & d[lo_col].notna() & d[hi_col].notna()]
    rows: list[dict[str, object]] = []
    keys = ["split", "origin_policy", "horizon"] + (["cell_id"] if per_cell else [])
    for key, g in d.groupby(keys, sort=True):
        k = dict(zip(keys, key, strict=True))
        kinds = g["start_kind"].astype(str).to_numpy()
        groups = {"overall": g}
        for kk in sorted(set(kinds) - {"all"}):
            groups[kk] = g[kinds == kk]
        for kind, gk in groups.items():
            y, lo, hi = (gk[c].to_numpy(dtype=np.float64) for c in ("y", lo_col, hi_col))
            rows.append(
                {
                    "split": "loco" if k["split"] == "test" else k["split"],
                    "split_tag": k["split"],
                    "policy": k["origin_policy"],
                    "kind": kind,
                    "cell": str(k.get("cell_id", "pooled")),
                    "horizon": int(k["horizon"]),
                    "picp": picp(y, lo, hi),
                    "mpiw": mpiw(lo, hi) * scale,
                    "iscore": interval_score(y, lo, hi, alpha) * scale,
                    "n": len(gk),
                }
            )
    return pd.DataFrame(
        rows,
        columns=[
            "split",
            "split_tag",
            "policy",
            "kind",
            "cell",
            "horizon",
            "picp",
            "mpiw",
            "iscore",
            "n",
        ],
    )


def metric_name(base: str, task: str, horizon: int) -> str:
    return f"{base}_h{horizon}" if task == "forecast" else base


def mlflow_metrics(table: pd.DataFrame, task: str, prefix: str) -> dict[str, float]:
    """Flatten a pooled :func:`interval_table` into ``{prefix}/{split_tag}/{policy}/{kind}/{m}``."""
    out: dict[str, float] = {}
    for r in table.to_dict("records"):
        for base in ("picp", "mpiw", "iscore"):
            v = float(r[base])
            if np.isfinite(v):
                name = metric_name(base, task, int(r["horizon"]))
                out[f"{prefix}/{r['split_tag']}/{r['policy']}/{r['kind']}/{name}"] = v
    return out


def reliability_table(
    inner_wide: pd.DataFrame | None,
    test_wide: pd.DataFrame,
    alphas: Sequence[float] = RELIABILITY_ALPHAS,
    scale: float = 100.0,
) -> pd.DataFrame:
    """Per-cell empirical coverage at each nominal level, raw vs calibrated.

    One row per ``(split, policy, cell, horizon, alpha)`` over ``kind == overall``. ``raw_picp``
    is NaN for point-only models and for ``alpha`` whose symmetric quantile pair the model does
    not store (default levels give 0.5 and 0.1 only); ``cal_picp`` is always defined (the
    point-only path calibrates any alpha). Levels that need a missing pair on a probabilistic
    model are skipped entirely (no silent switch of method).
    """
    parts = []
    keys = ["split", "policy", "cell", "horizon"]
    for a in alphas:
        try:
            test = wide_to_long(test_wide, a)
            inner = wide_to_long(inner_wide, a) if inner_wide is not None else None
        except ValueError:
            continue
        probabilistic = bool(test["lo"].notna().any())
        if inner is None and not probabilistic:
            continue
        t: pd.DataFrame | None = None
        if inner is not None:
            cal = calibrate_cv_plus(inner, test, alpha=a)
            ct = interval_table(cal, "lo_cal", "hi_cal", a, scale)
            ct = ct[ct["kind"] == "overall"]
            t = ct[[*keys, "picp", "mpiw"]].rename(columns={"picp": "cal_picp", "mpiw": "cal_mpiw"})
        else:
            cal = test
        if probabilistic:
            rt = interval_table(cal, "lo", "hi", a, scale)
            rt = rt[rt["kind"] == "overall"][[*keys, "picp", "mpiw"]].rename(
                columns={"picp": "raw_picp", "mpiw": "raw_mpiw"}
            )
            t = rt if t is None else t.merge(rt, on=keys, how="left")
        assert t is not None
        for c in ("raw_picp", "raw_mpiw", "cal_picp", "cal_mpiw"):
            if c not in t:
                t[c] = np.nan
        parts.append(t.assign(alpha=a))
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()
