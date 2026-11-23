"""Serving path for the field-mode models (ADR-0022). CPU only, no MPS code.

A field model estimates and forecasts SOH **without any capacity or SOH input**: only the
BMS-measurable signals of one charging protocol plus the cycle count (ADR-0018). There is one
model per protocol (``nasa``, ``calce``, ``toyota``); each is the benchmarked ``field_final``
iTransformer recipe (cross-fit sub-models averaged) trained on that protocol's cells.

Input contract (:func:`validate_field`): one row per cycle with ``cycle_idx`` and the raw
columns listed in ``field_meta.json["inputs"]`` (missing values allowed; a column that is
absent or entirely empty is reported as an OOD flag). ``charge_time_s`` is optional and only
feeds the charge-pause cleaning rule; it is never a model input. Processing is the training
code path: ADR-0018 causal input rules (:func:`battery_rul.data.cleaning.clean_inputs`), then
:func:`battery_rul.tasks.samples.apply_prepared` with the training cells' scaler, then
:func:`battery_rul.tasks.samples.build_samples`.

Outputs (:meth:`FieldPredictor.predict`): the current SOH estimate (task F-A), a multi-horizon
SOH forecast (F-B) and a RUL estimate (F-C, cycles to 80 % SOH), each with a CQR-calibrated
90 % interval, the informativeness of every interval (ADR-0019) and an OOD report.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Final

import numpy as np
import pandas as pd

from battery_rul.data.cleaning import clean_inputs
from battery_rul.models.base import Prediction, SampleSet
from battery_rul.splits.scaling import FoldScaler
from battery_rul.tasks.samples import TaskSpec, apply_prepared, build_samples

PROTOCOLS: Final = ("nasa", "calce", "toyota")
TASKS: Final = ("soh", "forecast", "rul")
MIN_CYCLES: Final = 5  #: TaskSpec.min_history: the first window needs 5 cycles
MAX_CYCLES: Final = 20_000
THETA: Final = 0.8
USEFUL_FRAC: Final = 0.5  #: ADR-0019: useful if width < 50 % of the distance to 80 % SOH
#: derived model channel -> raw input column (samples._derive)
DERIVED_FROM: Final = {
    "cycle_count": "cycle_idx",
    "log_rest_s": "rest_before_s",
    "skipped_cv": "cv_time_s",
}
OPTIONAL_INPUTS: Final = ("charge_time_s",)


class InputError(ValueError):
    """User-facing validation error (message is shown verbatim in the app)."""


def raw_inputs(channels: tuple[str, ...] | list[str]) -> list[str]:
    """Raw CSV columns needed to compute ``channels`` (``cycle_idx`` first, no duplicates)."""
    out = ["cycle_idx"]
    for c in channels:
        r = DERIVED_FROM.get(c, c)
        if r not in out:
            out.append(r)
    return out


def validate_field(df: pd.DataFrame, inputs: list[str], protocol: str) -> pd.DataFrame:
    """Check the contract; return a canonical cycles frame for one uploaded cell.

    Required: ``cycle_idx`` (numeric, unique). Signal columns are coerced to numbers (blank
    or non-numeric -> missing); absent signal columns are added as missing.
    """
    cols = {str(c).strip().lower(): c for c in df.columns}
    if "cycle_idx" not in cols:
        raise InputError(f"missing column 'cycle_idx' (got {list(df.columns)})")
    ci = pd.to_numeric(df[cols["cycle_idx"]], errors="coerce")
    if ci.isna().any():
        raise InputError(f"{int(ci.isna().sum())} row(s) have a non-numeric cycle_idx")
    if ci.duplicated().any():
        raise InputError("cycle_idx has duplicates; give one row per cycle")
    if len(ci) < MIN_CYCLES:
        raise InputError(f"need at least {MIN_CYCLES} cycles, got {len(ci)}")
    if len(ci) > MAX_CYCLES:
        raise InputError(f"at most {MAX_CYCLES} cycles are supported, got {len(ci)}")
    out = pd.DataFrame({"cycle_idx": ci.round().astype(int)})
    derive_src = [r for r in DERIVED_FROM.values() if r != "cycle_idx"]
    for c in dict.fromkeys([*inputs[1:], *OPTIONAL_INPUTS, *derive_src]):
        src = cols.get(c.lower())
        out[c] = pd.to_numeric(df[src], errors="coerce") if src is not None else np.nan
    out = out.sort_values("cycle_idx").reset_index(drop=True)
    out.insert(0, "cell_id", "uploaded")
    out.insert(0, "dataset", protocol)
    out["soh"] = np.nan  # never observed in the field; build_samples needs the column
    return out


def latest_sample(
    prepared: Any, task: str, lookback: int, horizons: tuple[int, ...], feature_set: str
) -> SampleSet:
    """The window ending at the last uploaded cycle, built by the training code path."""
    cell = str(prepared.cycles["cell_id"].iloc[0])
    build_task = "soh" if task == "soh" else "forecast"
    h = horizons if task == "forecast" else (1,)
    spec = TaskSpec(
        task=build_task,  # type: ignore[arg-type]
        lookback=lookback,
        horizons=h,
        feature_set=feature_set,  # type: ignore[arg-type]
    )
    eol = pd.DataFrame({"cell_id": [cell], "eol_cycle": [np.nan]})
    ss = build_samples(prepared, (cell,), eol, spec, "all")
    last = ss.subset(np.arange(len(ss.meta)) == len(ss.meta) - 1)
    if task == "rul":  # same inputs as the forecast windows; targets are placeholders
        last = replace(
            last,
            task="rul",
            y=np.zeros((1, 1), np.float32),
            y_mask=np.ones((1, 1), bool),
            horizons=(0,),
        )
    return last


def mean_prediction(preds: list[Prediction]) -> Prediction:
    """Mean of sub-model points and quantiles (``runner.average_predictions``)."""
    q = [p.quantiles for p in preds if p.quantiles is not None]
    if len(q) != len(preds):
        raise ValueError("field models must be quantile models")
    return Prediction(
        point=np.mean([p.point for p in preds], axis=0),
        quantiles=np.mean(q, axis=0),
        quantile_levels=preds[0].quantile_levels,
    )


def interval_index(levels: tuple[float, ...] | None, alpha: float) -> tuple[int, int]:
    if not levels:
        raise ValueError("field models must be quantile models")
    lv = np.asarray(levels)
    lo, hi = int(np.argmin(np.abs(lv - alpha / 2))), int(np.argmin(np.abs(lv - (1 - alpha / 2))))
    if not (np.isclose(lv[lo], alpha / 2) and np.isclose(lv[hi], 1 - alpha / 2)):
        raise ValueError(f"quantile levels {levels} lack {alpha / 2} / {1 - alpha / 2}")
    return lo, hi


def useful(lo: float, hi: float, point: float) -> bool:
    """ADR-0019 informativeness of an SOH interval."""
    return bool(hi - lo < USEFUL_FRAC * max(point - THETA, 0.005))


@dataclass
class FieldTask:
    members: list[Any]
    lookback: int
    horizons: tuple[int, ...]
    correction: dict[str, float]
    alpha: float


class FieldPredictor:
    """Loads ``<dir>/field_meta.json`` and its member checkpoints (``train_deploy_field.py``)."""

    def __init__(self, protocol_dir: str | Path) -> None:
        from battery_rul.train.transfer import load_pretrained

        d = Path(protocol_dir)
        self.meta: dict[str, Any] = json.loads((d / "field_meta.json").read_text())
        self.protocol = str(self.meta["protocol"])
        self.feature_set = str(self.meta["feature_set"])
        self.channels = tuple(self.meta["channels"])
        self.inputs = list(self.meta["inputs"])
        self.scaler = FoldScaler.from_stats(
            self.meta["scaler"]["mean"], self.meta["scaler"]["scale"]
        )
        self.tasks: dict[str, FieldTask] = {}
        for task in TASKS:
            m = self.meta["tasks"][task]
            self.tasks[task] = FieldTask(
                members=[load_pretrained(d / f, device="cpu") for f in m["members"]],
                lookback=int(m["lookback"]),
                horizons=tuple(int(h) for h in m["horizons"]),
                correction={str(k): float(v) for k, v in m["cqr_correction"].items()},
                alpha=float(m["alpha"]),
            )
        o = self.meta["ood"]
        self._ood_mu = np.asarray(o["mean"], dtype=np.float64)
        self._ood_prec = np.linalg.pinv(np.asarray(o["cov"], dtype=np.float64))
        self._ood_thr = float(o["threshold"])

    def prepare(self, df: pd.DataFrame) -> tuple[Any, pd.DataFrame, dict[str, int]]:
        cyc = validate_field(df, self.inputs, self.protocol)
        cleaned, counts = clean_inputs(cyc)
        return apply_prepared(cleaned, self.channels, self.scaler), cyc, counts

    def _predict(self, task: str, prepared: Any) -> tuple[SampleSet, Prediction]:
        t = self.tasks[task]
        ss = latest_sample(prepared, task, t.lookback, t.horizons, self.feature_set)
        return ss, mean_prediction([m.predict(ss) for m in t.members])

    def _interval(
        self, task: str, pred: Prediction, j: int, key: str
    ) -> tuple[float, float, float]:
        t = self.tasks[task]
        lo_i, hi_i = interval_index(pred.quantile_levels, t.alpha)
        assert pred.quantiles is not None
        c = t.correction[key]
        lo = float(pred.quantiles[0, j, lo_i]) - c
        hi = float(pred.quantiles[0, j, hi_i]) + c
        lo, hi = min(lo, hi), max(lo, hi)
        return float(pred.point[0, j]), lo, hi

    def ood(self, prepared: Any, raw: pd.DataFrame) -> dict[str, Any]:
        x = prepared.cycles[list(self.channels)].to_numpy(dtype=np.float64)[-1]
        diff = x - self._ood_mu
        dist = float(np.sqrt(max(diff @ self._ood_prec @ diff, 0.0)))
        flags: list[str] = []
        if dist > self._ood_thr:
            flags.append(
                f"latest cycle's signals are far from the training cycles (Mahalanobis "
                f"{dist:.1f} > {self._ood_thr:.1f}, the training 99th percentile); the "
                f"intervals assume a cell like the {self.protocol} training cells"
            )
        empty = [c for c in self.inputs[1:] if raw[c].isna().all()]
        if empty:
            flags.append(f"missing or empty signal column(s) {empty}; treated as unobserved")
        lb = max(t.lookback for t in self.tasks.values())
        if len(raw) < lb:
            flags.append(f"short history ({len(raw)} cycles < lookback {lb}); the window is padded")
        return {"is_ood": bool(flags), "distance": dist, "threshold": self._ood_thr, "flags": flags}

    def predict(self, df: pd.DataFrame) -> dict[str, Any]:
        """Validate, clean, then return SOH now, forecast, RUL and the OOD report (JSON-safe)."""
        prepared, raw, counts = self.prepare(df)
        last_cycle = int(raw["cycle_idx"].iloc[-1])

        _, sp = self._predict("soh", prepared)
        pt, lo, hi = self._interval("soh", sp, 0, "0")
        soh_now = {"soh": pt, "lo": max(lo, 0.0), "hi": hi, "useful": useful(lo, hi, pt)}

        _, fp = self._predict("forecast", prepared)
        forecast = []
        for j, h in enumerate(self.tasks["forecast"].horizons):
            pt, lo, hi = self._interval("forecast", fp, j, str(h))
            forecast.append(
                {
                    "horizon": int(h),
                    "cycle": last_cycle + int(h),
                    "soh": pt,
                    "lo": max(lo, 0.0),
                    "hi": hi,
                    "useful": useful(lo, hi, pt),
                }
            )

        _, rp = self._predict("rul", prepared)
        r_pt, r_lo, r_hi = self._interval("rul", rp, 0, "0")
        r_lo = max(r_lo, 0.0)
        r_hi = max(r_hi, r_lo)
        r_pt = float(np.clip(r_pt, r_lo, r_hi))
        rul = {
            "cycles": r_pt,
            "lo": r_lo,
            "hi": r_hi,
            "eol_cycle": last_cycle + r_pt,
            "threshold_soh": THETA,
            # RUL is trained on origins before EOL only; an estimate below 80 % is past it
            "already_below_threshold": bool(soh_now["soh"] < THETA),
        }

        return {
            "protocol": self.protocol,
            "n_cycles": len(raw),
            "last_cycle": last_cycle,
            "soh_now": soh_now,
            "forecast": forecast,
            "rul": rul,
            "coverage": 1 - self.tasks["forecast"].alpha,
            "cleaning": {k: v for k, v in counts.items() if v},
            "ood": self.ood(prepared, raw),
            "heldout": self.meta.get("heldout", {}),
            "model": self.meta.get("model_version", "itransformer field"),
        }
