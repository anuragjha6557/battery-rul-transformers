"""Serving predictor on a tiny synthetic model (CPU, no network, no real weights)."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from conftest import HORIZONS, synthetic_cell

from battery_rul.serve.predictor import InputError, Predictor


@pytest.fixture(scope="module")
def predictor(tiny_weights: Path) -> Predictor:
    return Predictor(tiny_weights)


@pytest.fixture(scope="module")
def cell() -> pd.DataFrame:
    return synthetic_cell(n=60, seed=42)


def test_output_schema_and_json_safe(predictor: Predictor, cell: pd.DataFrame) -> None:
    res = predictor.predict(cell)
    json.dumps(res)  # JSON-safe
    assert {"history", "forecast", "rul", "ood", "coverage", "model", "n_cycles", "last_cycle"} <= (
        res.keys()
    )
    assert res["n_cycles"] == 60 and res["last_cycle"] == 60
    assert set(res["history"]) == {"cycle", "soh"} and len(res["history"]["soh"]) == 60
    assert set(res["rul"]) >= {"cycles", "lo", "hi", "eol_cycle", "threshold_soh"}
    assert set(res["ood"]) == {"is_ood", "distance", "threshold", "flags"}
    assert res["coverage"] == pytest.approx(0.9)


def test_forecast_and_rul_invariants(predictor: Predictor, cell: pd.DataFrame) -> None:
    res = predictor.predict(cell)
    assert [f["horizon"] for f in res["forecast"]] == list(HORIZONS)
    for f in res["forecast"]:
        assert f["cycle"] == res["last_cycle"] + f["horizon"]
        assert f["lo"] <= f["soh"] <= f["hi"]
    r = res["rul"]
    assert 0 <= r["lo"] <= r["cycles"] <= r["hi"]
    assert r["eol_cycle"] == pytest.approx(res["last_cycle"] + r["cycles"])


@pytest.mark.parametrize(
    ("mutate", "match"),
    [
        (lambda d: d.rename(columns={"capacity_ah": "cap"}), "missing column"),
        (lambda d: d.head(9), "at least 10"),
        (lambda d: d.assign(cycle_idx=[1, *d["cycle_idx"].iloc[1:].tolist()[:-1], 1]), "duplicate"),
        (lambda d: d.assign(capacity_ah=[0.0, *d["capacity_ah"].iloc[1:]]), "positive"),
    ],
)
def test_input_errors(predictor: Predictor, cell: pd.DataFrame, mutate, match: str) -> None:
    with pytest.raises(InputError, match=match):
        predictor.predict(mutate(cell.copy()))


def test_unsorted_input_equals_sorted(predictor: Predictor, cell: pd.DataFrame) -> None:
    shuffled = cell.sample(frac=1.0, random_state=3)
    assert predictor.predict(shuffled) == predictor.predict(cell)


def test_extreme_drop_is_ood(predictor: Predictor) -> None:
    n = 60
    cap = np.concatenate([np.full(40, 1.1), np.linspace(1.1, 0.55, 20)])  # -50 % in 20 cycles
    res = predictor.predict(pd.DataFrame({"cycle_idx": np.arange(1, n + 1), "capacity_ah": cap}))
    assert res["ood"]["is_ood"] and res["ood"]["flags"]
