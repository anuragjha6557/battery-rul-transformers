"""Train the field-mode models (ADR-0022): one per protocol, the exact ``field_final`` recipe.

For each protocol the iTransformer entries of ``configs/experiment/field_final_<protocol>.yaml``
(tuned params, per-task lookback, feature set, ADR-0018 cleaning) are trained on the fold whose
held-out cells are the demo cells (NASA B0018, CALCE CS2_38, Toyota the official test cells),
seed 0, with the runner's own data path (``runner.fold_data``) and cross-fit sub-models.

Calibration: per-horizon CQR on the sub-models' inner-validation predictions (the rule of
``battery-rul calibrate``), so no held-out cell is ever used for training or calibration.
Held-out check: the averaged model is scored on the held-out cells with the runner's metrics;
``heldout`` in the meta records them next to the matching ``field_final`` MLflow run (same unit
key), which they should reproduce up to MPS nondeterminism.

Outputs in ``--out/<protocol>/``: ``<task>_<k>.pt`` (``train.transfer.save_pretrained``) and
``field_meta.json``. Weights are not committed (CLAUDE.md).

Usage: uv run python scripts/train_deploy_field.py [--protocols nasa calce toyota]
    [--out artifacts/deploy_field]
"""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path
from typing import Any

import numpy as np

from battery_rul.serve.field import PROTOCOLS, TASKS, raw_inputs, useful
from battery_rul.tasks.samples import thin_origins
from battery_rul.train.config import (
    default_tracking_uri,
    horizons_for,
    load_experiment,
    resolve_tuned_models,
)
from battery_rul.train.runner import (
    UnitSpec,
    _make,
    average_predictions,
    compute_metrics,
    dataset_ctx,
    effective_lookback,
    fold_data,
    model_ctor_params,
    plan_folds,
    unit_config,
)
from battery_rul.train.transfer import _record_dims, save_pretrained
from battery_rul.uq.conformal import cqr_correction
from battery_rul.utils import config_hash, seed_everything

MODEL = "itransformer"
SEED = 0
ALPHA = 0.1
FOLD = {"nasa": "B0018", "calce": "CS2_38", "toyota": "official"}


def _q_index(levels: tuple[float, ...]) -> tuple[int, int]:
    lv = np.asarray(levels)
    return int(np.argmin(np.abs(lv - ALPHA / 2))), int(np.argmin(np.abs(lv - (1 - ALPHA / 2))))


def _mlflow_metrics(key: str) -> dict[str, float]:
    import mlflow

    mlflow.set_tracking_uri(default_tracking_uri())
    r = mlflow.search_runs(
        experiment_names=["field_final"], filter_string=f"tags.unit_key = '{key}'"
    )
    if r.empty:
        return {}
    row = r.iloc[0]
    return {
        c[len("metrics.") :]: float(row[c])
        for c in r.columns
        if c.startswith("metrics.")
        if np.isfinite(row[c])
    }


def train_task(cfg, ctx, plan, ds, task, out: Path, processed: str) -> tuple[dict, Any]:
    m = next(x for x in cfg.models if x.name == MODEL and x.tuned_task == task)
    lb = effective_lookback(cfg, m)
    ucfg = unit_config(cfg, ds, task, m, plan.name, SEED, lb)
    key = config_hash(ucfg)
    unit = UnitSpec(ds, task, m, plan.name, SEED, lb, key, ucfg)
    fd = fold_data(ctx, plan, cfg, ds, task, lb, processed)
    stride = int(cfg.train_stride.get(ds, 1))
    cells = fd.train.meta["cell_id"].to_numpy()
    members, inner_parts, epochs = [], [], []
    t0 = time.perf_counter()
    for i, (tr, va) in enumerate(plan.inner):
        seed_everything(SEED)
        model = _make(unit, cfg)
        va_ss = fd.train.subset(np.isin(cells, list(va)))
        tr_ss = thin_origins(fd.train.subset(np.isin(cells, list(tr))), stride)
        info = model.fit(tr_ss, va_ss)
        epochs.append(int(info.epochs or 0))
        _record_dims(model, tr_ss)
        fname = f"{task}_{i}.pt"
        save_pretrained(
            model,
            out / fname,
            model_ctor_params(m),
            lb,
            {"seed": SEED, "task": task, "inner_val": list(va), "unit_key": key},
        )
        members.append((fname, model))
        inner_parts.append((va_ss, model.predict(va_ss)))
    secs = time.perf_counter() - t0

    # CQR from the pooled inner-validation predictions (battery-rul calibrate rule)
    levels = inner_parts[0][1].quantile_levels
    lo_i, hi_i = _q_index(levels)
    corr, n_cal = {}, {}
    hz = fd.train.horizons
    for j, h in enumerate(hz):
        ys, los, his = [], [], []
        for ss, p in inner_parts:
            mk = ss.y_mask[:, j] & np.isfinite(ss.y[:, j])
            ys.append(ss.y[mk, j])
            los.append(p.quantiles[mk, j, lo_i])
            his.append(p.quantiles[mk, j, hi_i])
        y, lo, hi = (np.concatenate(a).astype(np.float64) for a in (ys, los, his))
        corr[str(h)] = float(cqr_correction(y, lo, hi, ALPHA))
        n_cal[str(h)] = len(y)

    # held-out check: averaged model on the fold's test cells, runner metrics + calibrated
    heldout: dict[str, dict] = {}
    for (tag, policy), ss in fd.tests.items():
        if policy != "all":
            continue
        pred = average_predictions([mm.predict(ss) for _, mm in members])
        met = compute_metrics(ss, pred, fd.y_smooth.get((tag, policy)))
        hd: dict[str, float] = {
            f"{k}/{n}": float(v) for k, mm in met.items() for n, v in mm.items() if k == "overall"
        }
        for j, h in enumerate(ss.horizons):
            mk = ss.y_mask[:, j] & np.isfinite(ss.y[:, j])
            if not mk.any():
                continue
            c = corr[str(h)]
            lo = pred.quantiles[mk, j, lo_i] - c
            hi = pred.quantiles[mk, j, hi_i] + c
            y = ss.y[mk, j]
            hd[f"picp_h{h}"] = float(np.mean((y >= lo) & (y <= hi)))
            hd[f"width_h{h}"] = float(np.mean(hi - lo))
            if task != "rul":
                pt = pred.point[mk, j]
                hd[f"useful_h{h}"] = float(
                    np.mean([useful(a, b, p) for a, b, p in zip(lo, hi, pt, strict=True)])
                )
        heldout[tag] = hd
    ref = _mlflow_metrics(key)
    ref_keep = {k: v for k, v in ref.items() if k.split("/")[1:2] == ["all"] and "/overall/" in k}
    print(
        ds,
        task,
        f"L={lb}",
        f"{len(members)} members",
        f"epochs={epochs}",
        f"{secs:.0f}s",
        json.dumps(
            {
                t: {k: round(v, 4) for k, v in d.items() if k.startswith("overall/")}
                for t, d in heldout.items()
            }
        ),
    )
    print("  field_final run:", json.dumps({k: round(v, 4) for k, v in ref_keep.items()}))
    return {
        "members": [f for f, _ in members],
        "lookback": lb,
        "horizons": [int(h) for h in hz],
        "alpha": ALPHA,
        "cqr_correction": corr,
        "n_cal": n_cal,
        "params": model_ctor_params(m),
        "tuned_from": m.tuned_from,
        "unit_key": key,
        "epochs": epochs,
        "fit_seconds": round(secs, 1),
        "n_train": len(fd.train),
        "heldout": heldout,
        "field_final_reference": ref_keep,
    }, fd


def ood_stats(prepared, train_cells: tuple[str, ...], channels: tuple[str, ...]) -> dict:
    x = prepared.cycles.loc[prepared.cycles["cell_id"].isin(train_cells), list(channels)]
    x = x.to_numpy(dtype=np.float64)
    mu = x.mean(axis=0)
    cov = np.cov(x, rowvar=False)
    d = np.sqrt(np.einsum("ij,jk,ik->i", x - mu, np.linalg.pinv(cov), x - mu).clip(min=0))
    return {"mean": mu.tolist(), "cov": cov.tolist(), "threshold": float(np.quantile(d, 0.99))}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--protocols", nargs="*", default=list(PROTOCOLS))
    ap.add_argument("--out", default="artifacts/deploy_field")
    ap.add_argument("--processed", default="data/processed")
    args = ap.parse_args()
    sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout
    for ds in args.protocols:
        out = Path(args.out) / ds
        out.mkdir(parents=True, exist_ok=True)
        cfg = resolve_tuned_models(load_experiment(f"field_final_{ds}"))
        ctx = dataset_ctx(ds, args.processed, cfg.theta)
        plan = next(p for p in plan_folds(ds, ctx.cells) if p.name == FOLD[ds])
        tasks, prepared = {}, None
        for task in TASKS:
            tasks[task], fd = train_task(cfg, ctx, plan, ds, task, out, args.processed)
            prepared = fd.prepared
        assert prepared is not None and prepared.scaler is not None
        ch = tuple(prepared.channels)
        sc = prepared.scaler
        meta = {
            "model_version": f"itransformer field ({ds}, field_final recipe, CQR)",
            "protocol": ds,
            "feature_set": cfg.feature_set,
            "clean": bool(cfg.clean),
            "theta": cfg.theta,
            "channels": list(ch),
            "inputs": raw_inputs(ch),
            "scaler": {
                "mean": {c: float(sc.mean_[c]) for c in ch},
                "scale": {c: float(sc.scale_[c]) for c in ch},
            },
            "horizons": list(horizons_for(cfg, ds)),
            "cells": {
                "train": list(plan.train),
                "heldout": {t: list(c) for t, c in plan.tests},
                "inner": [[list(a), list(b)] for a, b in plan.inner],
            },
            "tasks": tasks,
            "heldout": {
                t: {
                    "soh": tasks["soh"]["heldout"].get(t, {}),
                    "forecast": tasks["forecast"]["heldout"].get(t, {}),
                    "rul": tasks["rul"]["heldout"].get(t, {}),
                }
                for t, _ in plan.tests
            },
            "ood": ood_stats(prepared, plan.train, ch),
            "git_sha": sha.strip(),
            "seed": SEED,
        }
        (out / "field_meta.json").write_text(json.dumps(meta, indent=2))
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
