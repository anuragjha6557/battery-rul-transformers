"""Deep-ensemble aggregation over seeds (ADR-0011, arm "5-seed deep ensemble").

K members are K runs of the *same* unit (dataset, fold, task, model, config) that differ only by
seed. The ensemble prediction is:

* ``point``: mean of the member points;
* ``quantiles``: **mean over members, per quantile level** ("Vincentisation" / quantile
  averaging). It keeps the levels non-decreasing (a mean of monotone vectors is monotone), keeps
  the output shape of a single model, and is the same rule the runner already uses to average
  cross-fit sub-models. The alternative is the *mixture* quantile (pool the members' predictive
  distributions and take its quantiles), which is wider when members disagree on the location;
  quantile averaging is narrower and treats disagreement as noise rather than extra uncertainty.
  Not implemented here; CQR (``uq/conformal.py``) can be applied on top of either.

Two entry points: :func:`ensemble_predictions` (``Prediction`` objects) and
:func:`ensemble_frames` / :func:`ensemble_runs` (the ``predictions.parquet`` frames logged by the
runner, which is what the report consumes). No torch/lightgbm imports.
"""

from __future__ import annotations

import re
from collections.abc import Sequence

import numpy as np
import pandas as pd

from battery_rul.models.base import Prediction

_AVG = re.compile(r"^(point|q[0-9.eE+-]+)_h\d+$")


def ensemble_predictions(preds: Sequence[Prediction]) -> Prediction:
    """Mean point and per-level mean quantiles of K >= 1 members (same samples, same levels).

    Quantiles are kept only if every member has them; otherwise the result is point-only.
    """
    if not preds:
        raise ValueError("need at least one member")
    if any(p.point.shape != preds[0].point.shape for p in preds):
        raise ValueError("members disagree on prediction shape")
    point = np.mean([p.point for p in preds], axis=0)
    if any(p.quantiles is None for p in preds):
        return Prediction(point=point)
    levels = preds[0].quantile_levels
    if any(p.quantile_levels != levels for p in preds):
        raise ValueError("members disagree on quantile levels")
    q = np.mean([p.quantiles for p in preds if p.quantiles is not None], axis=0)
    return Prediction(point=point, quantiles=q, quantile_levels=levels)


def ensemble_frames(frames: Sequence[pd.DataFrame]) -> pd.DataFrame:
    """Ensemble ``predictions.parquet``-style frames (one per seed) row by row.

    Columns ``point_h*`` and ``q*_h*`` are averaged; everything else (meta, ``y_h*``,
    ``y_mask_h*``, identifiers) is taken from the first frame after checking that all frames
    describe the same rows and targets.
    """
    if not frames:
        raise ValueError("need at least one member")
    first = frames[0].reset_index(drop=True)
    avg_cols = [c for c in first.columns if _AVG.match(c)]
    for f in frames[1:]:
        f = f.reset_index(drop=True)
        if list(f.columns) != list(first.columns) or len(f) != len(first):
            raise ValueError("members disagree on columns or row count")
        for c in first.columns:
            if c in avg_cols:
                continue
            same = (
                np.array_equal(first[c].to_numpy(), f[c].to_numpy(), equal_nan=True)
                if first[c].dtype.kind in "fiub"
                else first[c].equals(f[c])
            )
            if not same:
                raise ValueError(f"members differ in non-prediction column {c!r}")
    out = first.copy()
    for c in avg_cols:
        out[c] = np.mean([f[c].to_numpy(dtype=float) for f in frames], axis=0)
    # mean of non-decreasing vectors is non-decreasing, but guard against float noise
    for h in sorted({c.rsplit("_h", 1)[1] for c in avg_cols}):
        qcols = sorted(
            (c for c in avg_cols if c.startswith("q") and c.endswith(f"_h{h}")),
            key=lambda c: float(c[1:].rsplit("_h", 1)[0]),
        )
        if qcols:
            out[qcols] = np.sort(out[qcols].to_numpy(), axis=1)
    return out


def ensemble_runs(run_ids: Sequence[str], artifact: str = "predictions.parquet") -> pd.DataFrame:
    """Ensemble the prediction artifact of K MLflow runs (same unit, different seeds)."""
    import mlflow

    frames = [
        pd.read_parquet(mlflow.artifacts.download_artifacts(run_id=r, artifact_path=artifact))
        for r in run_ids
    ]
    return ensemble_frames(frames)
