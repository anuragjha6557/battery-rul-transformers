"""Train the deployed iTransformer-v2 models (ADR-0014/0015) and save them for serving.

Recipe = the benchmarked ``itransformer_sc`` (tuned params from ``configs/tuned``), refit on
pooled cells of all three datasets with the single-channel (SOH-only) inputs the public app can
always provide. Cells are split by cell (never by window):

* calibration cells (CQR, never trained on): NASA B0018 (the rig-independent cell), CALCE
  CS2_38, and 20 % of Toyota cells (seeded);
* early-stopping cells: 10 % of the remaining Toyota cells;
* training cells: everything else. Toyota training windows are thinned to stride 4 (as in the
  benchmark, ADR-0006).

Forecast horizons are the transfer set (1, 10, 25, 50, 100) for all datasets. RUL labels are
the benchmark labels (80 % SOH, sustained rule; Toyota = provider cycle life, ADR-0005).

Outputs in ``--out`` (default ``artifacts/deploy``): ``forecast.pt``, ``rul.pt`` (format of
``train.transfer.save_pretrained``) and ``deploy_meta.json`` (CQR corrections, OOD statistics,
cell lists, calibration-set coverage, provenance). Weights are not committed (CLAUDE.md); they
are uploaded to the Hugging Face model repo by ``scripts/push_to_hub.py``.

Usage: uv run python scripts/train_deploy.py [--out artifacts/deploy] [--seed 0]
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path

import numpy as np

from battery_rul.models.base import SampleSet
from battery_rul.tasks.samples import TaskSpec, build_samples, prepare_cycles, thin_origins
from battery_rul.train.runner import dataset_ctx
from battery_rul.train.transfer import (
    SHARED_HORIZONS,
    _make,
    _record_dims,
    concat_samples,
    load_params,
    save_pretrained,
)
from battery_rul.uq.conformal import cqr_correction
from battery_rul.utils import seed_everything

MODEL = "itransformer_sc"
ALPHA = 0.1
THETA = 0.8
CAL_FIXED = {"nasa": ("B0018",), "calce": ("CS2_38",)}
TOYOTA_CAL_FRAC, TOYOTA_VAL_FRAC, TOYOTA_STRIDE = 0.2, 0.1, 4


def split_cells(ctxs: dict, seed: int) -> dict[str, dict[str, tuple[str, ...]]]:
    rng = np.random.default_rng(seed)
    out = {}
    for ds, ctx in ctxs.items():
        cells = sorted(ctx.cells["cell_id"].astype(str))
        if ds == "toyota":
            perm = list(rng.permutation(cells))
            n_cal = round(TOYOTA_CAL_FRAC * len(cells))
            cal, rest = perm[:n_cal], perm[n_cal:]
            n_val = round(TOYOTA_VAL_FRAC * len(rest))
            val, train = rest[:n_val], rest[n_val:]
        else:
            cal = list(CAL_FIXED[ds])
            train, val = [c for c in cells if c not in cal], []
        out[ds] = {
            "train": tuple(sorted(train)),
            "val": tuple(sorted(val)),
            "cal": tuple(sorted(cal)),
        }
    return out


def samples(ctxs, cells, task: str, lookback: int, role: str) -> SampleSet:
    spec = TaskSpec(
        task=task,  # type: ignore[arg-type]
        lookback=lookback,
        horizons=SHARED_HORIZONS,
        feature_set="sc",
    )
    parts = []
    for ds, ctx in ctxs.items():
        cs = cells[ds][role]
        if not cs:
            continue
        prepared = prepare_cycles(ctx.cycles, cs, "sc")
        ss = build_samples(prepared, cs, ctx.eol, spec, "all")
        if role == "train" and ds == "toyota":
            ss = thin_origins(ss, TOYOTA_STRIDE)
        if len(ss.meta):
            parts.append(ss)
    out = parts[0]
    for p in parts[1:]:
        out = concat_samples(out, p)
    return out


def coverage(y, lo, hi, mask) -> float:
    m = mask & np.isfinite(y)
    return float(np.mean((y[m] >= lo[m]) & (y[m] <= hi[m]))) if m.any() else float("nan")


def fit_task(ctxs, cells, task: str, out: Path, seed: int) -> tuple[dict, SampleSet]:
    params, lookback, src = load_params(MODEL, task)
    tr = samples(ctxs, cells, task, lookback, "train")
    va = samples(ctxs, cells, task, lookback, "val")
    ca = samples(ctxs, cells, task, lookback, "cal")
    seed_everything(seed)
    model = _make(MODEL, params, "auto")
    t0 = time.perf_counter()
    info = model.fit(tr, va)
    secs = time.perf_counter() - t0
    _record_dims(model, tr)
    save_pretrained(model, out / f"{task}.pt", params, lookback, {"seed": seed, "task": task})

    pred = model.predict(ca)
    levels = np.asarray(model.quantiles)
    lo_i = int(np.argmin(np.abs(levels - ALPHA / 2)))
    hi_i = int(np.argmin(np.abs(levels - (1 - ALPHA / 2))))
    corr, cov_raw, cov_cal, n_cal = {}, {}, {}, {}
    for j, h in enumerate(ca.horizons):
        m = ca.y_mask[:, j] & np.isfinite(ca.y[:, j])
        y = ca.y[m, j].astype(np.float64)
        lo = pred.quantiles[m, j, lo_i].astype(np.float64)
        hi = pred.quantiles[m, j, hi_i].astype(np.float64)
        c = cqr_correction(y, lo, hi, ALPHA)
        corr[str(h)] = c
        cov_raw[str(h)] = coverage(y, lo, hi, np.ones_like(y, bool))
        cov_cal[str(h)] = coverage(y, lo - c, hi + c, np.ones_like(y, bool))
        n_cal[str(h)] = int(m.sum())
    meta = {
        "lookback": lookback,
        "horizons": [int(h) for h in tr.horizons],
        "params_source": src,
        "params": params,
        "alpha": ALPHA,
        "cqr_correction": corr,
        "cal_coverage_raw": cov_raw,
        "cal_coverage_cqr": cov_cal,
        "n_cal": n_cal,
        "n_train": len(tr.meta),
        "n_val": len(va.meta),
        "epochs": int(info.epochs or 0),
        "fit_seconds": round(secs, 1),
    }
    print(
        task,
        json.dumps({k: meta[k] for k in ("n_train", "epochs", "fit_seconds")}),
        json.dumps({k: meta[k] for k in ("cal_coverage_raw", "cal_coverage_cqr")}),
    )
    return meta, tr


def ood_stats(tr: SampleSet) -> dict:
    x = tr.x_tab.astype(np.float64)
    mu = x.mean(axis=0)
    cov = np.cov(x, rowvar=False)
    prec = np.linalg.pinv(cov)
    d = np.sqrt(np.einsum("ij,jk,ik->i", x - mu, prec, x - mu).clip(min=0))
    fade = -x[:, 3] * 100  # SOH per 100 cycles, from the slope-of-last-50 summary
    return {
        "features": list(tr.feature_names),
        "mean": mu.tolist(),
        "cov": cov.tolist(),
        "threshold": float(np.quantile(d, 0.99)),
        "fade_per_100_range": [float(np.quantile(fade, 0.005)), float(np.quantile(fade, 0.995))],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="artifacts/deploy")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--processed", default="data/processed")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    ctxs = {ds: dataset_ctx(ds, args.processed, THETA) for ds in ("nasa", "calce", "toyota")}
    cells = split_cells(ctxs, args.seed)
    tasks, tr_forecast = {}, None
    for task in ("forecast", "rul"):
        tasks[task], tr = fit_task(ctxs, cells, task, out, args.seed)
        if task == "forecast":
            tr_forecast = tr
    sha = subprocess.run(
        ["git", "rev-parse", "HEAD"], capture_output=True, text=True
    ).stdout.strip()
    meta = {
        "model_version": "itransformer-v2 (itransformer_sc, CQR)",
        "model_name": MODEL,
        "git_sha": sha,
        "seed": args.seed,
        "theta": THETA,
        "cells": {ds: {k: list(v) for k, v in d.items()} for ds, d in cells.items()},
        "tasks": tasks,
        "ood": ood_stats(tr_forecast),
    }
    (out / "deploy_meta.json").write_text(json.dumps(meta, indent=2))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
