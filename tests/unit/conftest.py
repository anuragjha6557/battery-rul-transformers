"""Shared fixtures: a tiny deployable weights dir built from synthetic cells (CPU, seconds)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pytest

LOOKBACK = 8
HORIZONS = (1, 10, 25, 50, 100)
ALPHA = 0.1
PARAMS: dict[str, Any] = {
    "d_model": 16,
    "n_heads": 2,
    "n_layers": 1,
    "max_epochs": 2,
    "patience": 2,
    "batch_size": 128,
}


def synthetic_cell(n: int = 160, rate: float = 0.003, noise: float = 0.002, seed: int = 0):
    """One cell's raw (cycle_idx, capacity_ah) frame: linear fade from ~1.1 Ah."""
    rng = np.random.default_rng(seed)
    cap = 1.1 - rate * np.arange(n) + noise * rng.standard_normal(n)
    return pd.DataFrame({"cycle_idx": np.arange(1, n + 1), "capacity_ah": cap})


def _build_weights(out: Path) -> Path:
    from battery_rul.data.schema import add_soh, empty_optional_features
    from battery_rul.models.registry import make_model
    from battery_rul.tasks.samples import TaskSpec, build_samples, prepare_cycles
    from battery_rul.train.transfer import _record_dims, save_pretrained
    from battery_rul.uq.conformal import cqr_correction

    frames = []
    for j in range(6):
        d = synthetic_cell(rate=0.0025 + 0.0004 * j, seed=j).assign(dataset="user", cell_id=f"c{j}")
        frames.append(d)
    cyc = add_soh(empty_optional_features(pd.concat(frames, ignore_index=True)))
    cells = tuple(sorted(cyc["cell_id"].unique()))
    train, cal = cells[:4], cells[4:]
    eol = pd.DataFrame({"cell_id": list(cells), "eol_cycle": 80.0})
    prepared = prepare_cycles(cyc, cells, "sc")

    out.mkdir(parents=True, exist_ok=True)
    meta: dict[str, Any] = {
        "model_version": "itransformer-v2 (tiny test)",
        "cells": {"user": {"train": list(train), "val": [], "cal": list(cal)}},
        "tasks": {},
    }
    x_tab = None
    for task in ("forecast", "rul"):
        spec = TaskSpec(task=task, lookback=LOOKBACK, horizons=HORIZONS, feature_set="sc")  # type: ignore[arg-type]
        tr = build_samples(prepared, train, eol, spec, "all")
        ca = build_samples(prepared, cal, eol, spec, "all")
        model = make_model("itransformer_sc", **{**PARAMS, "device": "cpu"})
        model.fit(tr, ca)  # type: ignore[attr-defined]
        _record_dims(model, tr)  # type: ignore[arg-type]
        save_pretrained(model, out / f"{task}.pt", PARAMS, LOOKBACK, {"task": task})  # type: ignore[arg-type]
        pred = model.predict(ca)
        lv = np.asarray(model.quantiles)  # type: ignore[attr-defined]
        lo_i, hi_i = int(np.argmin(abs(lv - ALPHA / 2))), int(np.argmin(abs(lv - (1 - ALPHA / 2))))
        corr = {}
        for j, h in enumerate(ca.horizons):
            m = ca.y_mask[:, j] & np.isfinite(ca.y[:, j])
            corr[str(h)] = float(
                cqr_correction(
                    ca.y[m, j].astype(float),
                    pred.quantiles[m, j, lo_i].astype(float),
                    pred.quantiles[m, j, hi_i].astype(float),
                    ALPHA,
                )
            )
        meta["tasks"][task] = {
            "lookback": LOOKBACK,
            "horizons": [int(h) for h in tr.horizons],
            "alpha": ALPHA,
            "cqr_correction": corr,
        }
        if task == "forecast":
            x_tab = tr.x_tab.astype(np.float64)
    assert x_tab is not None
    mu = x_tab.mean(axis=0)
    cov = np.cov(x_tab, rowvar=False)
    d = np.sqrt(np.einsum("ij,jk,ik->i", x_tab - mu, np.linalg.pinv(cov), x_tab - mu).clip(0))
    fade = -x_tab[:, 3] * 100
    meta["ood"] = {
        "mean": mu.tolist(),
        "cov": cov.tolist(),
        "threshold": float(np.quantile(d, 0.99)),
        "fade_per_100_range": [float(np.quantile(fade, 0.005)), float(np.quantile(fade, 0.995))],
    }
    (out / "deploy_meta.json").write_text(json.dumps(meta))
    return out


@pytest.fixture(scope="session")
def tiny_weights(tmp_path_factory: pytest.TempPathFactory) -> Path:
    return _build_weights(tmp_path_factory.mktemp("tiny_weights"))
