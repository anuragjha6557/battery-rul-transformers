"""Serving path for the deployed iTransformer-v2 (ADR-0014/0015). CPU only, no MPS code.

Input contract (``validate_cycles``): a table with one row per cycle and columns
``cycle_idx`` (int, increasing) and ``capacity_ah`` (discharge capacity, Ah). Extra columns are
ignored. SOH is computed exactly as in training: ``capacity / mean(first 5 cycles)``.

The deployed models use the **single-channel** inputs (SOH history + causal SOH summaries) so
any cycler's capacity log works; see ADR-0015 for why the multi-channel variant is not served.
Windows are built with the same ``tasks.samples.build_samples`` code as training, so serving
cannot drift from the benchmarked feature pipeline.

Outputs (``Predictor.predict``): SOH history, a multi-horizon SOH forecast with CQR-calibrated
90 % intervals, a RUL estimate (cycles to 80 % SOH) with a calibrated 90 % interval, and an
out-of-distribution report. Intervals are distribution-free *only* when the cell resembles the
training cells (exchangeability); the OOD report says when that is doubtful.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from battery_rul.data.schema import add_soh, empty_optional_features
from battery_rul.models.base import SampleSet
from battery_rul.tasks.samples import TaskSpec, build_samples, prepare_cycles

DEPLOY_DATASET = "user"
MIN_CYCLES = 10  #: shortest history accepted (5 cycles define SOH = 1, then >= 5 more)
MAX_CYCLES = 20_000
SOH_RANGE = (0.3, 1.3)


class InputError(ValueError):
    """User-facing validation error (message is shown verbatim in the app)."""


def validate_cycles(df: pd.DataFrame) -> pd.DataFrame:
    """Check the input contract and return a clean (cycle_idx, capacity_ah) frame."""
    cols = {c.strip().lower(): c for c in df.columns}
    missing = [c for c in ("cycle_idx", "capacity_ah") if c not in cols]
    if missing:
        raise InputError(
            f"missing column(s) {missing}; expected 'cycle_idx' and 'capacity_ah' "
            f"(got {list(df.columns)})"
        )
    out = pd.DataFrame(
        {
            "cycle_idx": pd.to_numeric(df[cols["cycle_idx"]], errors="coerce"),
            "capacity_ah": pd.to_numeric(df[cols["capacity_ah"]], errors="coerce"),
        }
    )
    bad = out.isna().any(axis=1)
    if bad.any():
        raise InputError(f"{int(bad.sum())} row(s) have non-numeric cycle_idx/capacity_ah")
    if (out["capacity_ah"] <= 0).any():
        raise InputError("capacity_ah must be positive")
    if out["cycle_idx"].duplicated().any():
        raise InputError("cycle_idx has duplicates; give one row per cycle")
    out = out.sort_values("cycle_idx").reset_index(drop=True)
    if len(out) < MIN_CYCLES:
        raise InputError(f"need at least {MIN_CYCLES} cycles, got {len(out)}")
    if len(out) > MAX_CYCLES:
        raise InputError(f"at most {MAX_CYCLES} cycles are supported, got {len(out)}")
    out["cycle_idx"] = out["cycle_idx"].round().astype(int)
    return out


def to_cycles(clean: pd.DataFrame, cell_id: str = "uploaded") -> pd.DataFrame:
    """Canonical cycles table (schema of ``data/schema.py``) for one user cell."""
    df = clean.assign(dataset=DEPLOY_DATASET, cell_id=cell_id)
    return add_soh(empty_optional_features(df))


def latest_sample(
    cycles: pd.DataFrame, task: str, lookback: int, horizons: tuple[int, ...]
) -> SampleSet:
    """The window ending at the last observed cycle, built by the training code path."""
    cell = str(cycles["cell_id"].iloc[0])
    prepared = prepare_cycles(cycles, (cell,), "sc")
    h = horizons if task == "forecast" else (1,)  # rul reuses the forecast windows
    spec = TaskSpec(task="forecast", lookback=lookback, horizons=h, feature_set="sc")
    eol = pd.DataFrame({"cell_id": [cell], "eol_cycle": [np.nan]})
    ss = build_samples(prepared, (cell,), eol, spec, "all")
    if len(ss.meta) == 0:
        raise InputError("history too short to build an input window")
    last = ss.subset(np.arange(len(ss.meta)) == len(ss.meta) - 1)
    if task == "rul":  # same inputs; targets are placeholders (never used at inference)
        n = len(last.meta)
        last = replace(
            last,
            task="rul",
            y=np.zeros((n, 1), np.float32),
            y_mask=np.ones((n, 1), bool),
            horizons=(0,),
        )
    return last


@dataclass
class OODReport:
    distance: float
    threshold: float
    flags: list[str] = field(default_factory=list)

    @property
    def is_ood(self) -> bool:
        return bool(self.flags)


@dataclass
class TaskBundle:
    model: Any
    lookback: int
    horizons: tuple[int, ...]
    correction: dict[str, float]  #: CQR correction per horizon (str key), target units
    alpha: float


class Predictor:
    """Loads ``<weights_dir>/{forecast,rul}.pt`` and ``deploy_meta.json``.

    Both are written by ``scripts/train_deploy.py``.
    """

    def __init__(self, weights_dir: str | Path) -> None:
        from battery_rul.train.transfer import load_pretrained

        d = Path(weights_dir)
        self.meta: dict[str, Any] = json.loads((d / "deploy_meta.json").read_text())
        self.tasks: dict[str, TaskBundle] = {}
        for task in ("forecast", "rul"):
            m = self.meta["tasks"][task]
            model = load_pretrained(d / f"{task}.pt", device="cpu")
            self.tasks[task] = TaskBundle(
                model=model,
                lookback=int(m["lookback"]),
                horizons=tuple(int(h) for h in m["horizons"]),
                correction={str(k): float(v) for k, v in m["cqr_correction"].items()},
                alpha=float(m["alpha"]),
            )
        o = self.meta["ood"]
        self._ood_mu = np.asarray(o["mean"])
        self._ood_prec = np.linalg.pinv(np.asarray(o["cov"]))
        self._ood_thr = float(o["threshold"])
        self._fade = tuple(o["fade_per_100_range"])

    # ------------------------------------------------------------------------------------
    def ood(self, cycles: pd.DataFrame, sample: SampleSet) -> OODReport:
        x = sample.x_tab[0].astype(np.float64)
        diff = x - self._ood_mu
        dist = float(np.sqrt(max(diff @ self._ood_prec @ diff, 0.0)))
        flags: list[str] = []
        if dist > self._ood_thr:
            flags.append(
                f"SOH-trajectory summary is far from the training cells "
                f"(Mahalanobis {dist:.1f} > {self._ood_thr:.1f}, the 99th percentile of training)"
            )
        soh = cycles["soh"].to_numpy()
        if soh.min() < SOH_RANGE[0] or soh.max() > SOH_RANGE[1]:
            flags.append(
                f"SOH outside [{SOH_RANGE[0]}, {SOH_RANGE[1]}] (check units or the first cycles)"
            )
        if len(soh) >= 10:
            fade = -float(sample.x_tab[0, 3]) * 100  # summary #3 = slope of last 50 cycles
            lo, hi = self._fade
            if not lo <= fade <= hi:
                flags.append(
                    f"recent fade rate {fade:.2%} SOH/100 cycles is outside the training range "
                    f"[{lo:.2%}, {hi:.2%}]"
                )
        if len(cycles) < self.tasks["forecast"].lookback:
            flags.append(
                f"short history ({len(cycles)} cycles < lookback "
                f"{self.tasks['forecast'].lookback}); the model pads the window"
            )
        return OODReport(distance=dist, threshold=self._ood_thr, flags=flags)

    def predict(self, df: pd.DataFrame) -> dict[str, Any]:
        """Validate, then return SOH history, forecast, RUL and the OOD report (JSON-safe)."""
        cycles = to_cycles(validate_cycles(df))
        last_cycle = int(cycles["cycle_idx"].iloc[-1])

        fb = self.tasks["forecast"]
        fs = latest_sample(cycles, "forecast", fb.lookback, fb.horizons)
        fp = fb.model.predict(fs)
        lo_i, hi_i = _interval_index(fb.model.quantiles, fb.alpha)
        forecast = []
        for j, h in enumerate(fb.horizons):
            c = fb.correction[str(h)]
            lo = float(fp.quantiles[0, j, lo_i]) - c
            hi = float(fp.quantiles[0, j, hi_i]) + c
            lo, hi = min(lo, hi), max(lo, hi)
            forecast.append(
                {
                    "horizon": int(h),
                    "cycle": last_cycle + int(h),
                    "soh": float(fp.point[0, j]),
                    "lo": max(lo, 0.0),
                    "hi": hi,
                }
            )

        rb = self.tasks["rul"]
        rs = latest_sample(cycles, "rul", rb.lookback, (0,))
        rp = rb.model.predict(rs)
        lo_i, hi_i = _interval_index(rb.model.quantiles, rb.alpha)
        c = rb.correction["0"]
        r_lo = max(float(rp.quantiles[0, 0, lo_i]) - c, 0.0)
        r_hi = max(float(rp.quantiles[0, 0, hi_i]) + c, r_lo)
        r_pt = float(np.clip(rp.point[0, 0], r_lo, r_hi))
        rul = {
            "cycles": r_pt,
            "lo": r_lo,
            "hi": r_hi,
            "eol_cycle": last_cycle + r_pt,
            "threshold_soh": 0.8,
            "already_below_threshold": bool(cycles["soh"].iloc[-1] < 0.8),
        }

        rep = self.ood(cycles, fs)
        return {
            "n_cycles": len(cycles),
            "last_cycle": last_cycle,
            "history": {
                "cycle": cycles["cycle_idx"].astype(int).tolist(),
                "soh": cycles["soh"].astype(float).round(6).tolist(),
            },
            "forecast": forecast,
            "rul": rul,
            "coverage": 1 - fb.alpha,
            "ood": {
                "is_ood": rep.is_ood,
                "distance": rep.distance,
                "threshold": rep.threshold,
                "flags": rep.flags,
            },
            "model": self.meta.get("model_version", "itransformer-v2"),
        }


def _interval_index(levels: tuple[float, ...] | None, alpha: float) -> tuple[int, int]:
    if not levels:
        raise ValueError("deployed models must be quantile models")
    lv = np.asarray(levels)
    lo, hi = int(np.argmin(np.abs(lv - alpha / 2))), int(np.argmin(np.abs(lv - (1 - alpha / 2))))
    if not (np.isclose(lv[lo], alpha / 2) and np.isclose(lv[hi], 1 - alpha / 2)):
        raise ValueError(f"quantile levels {levels} lack {alpha / 2} / {1 - alpha / 2}")
    return lo, hi
