"""Field-mode serving (ADR-0022): the serving path equals the training path."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from test_cleaning import _cell
from test_leakage import EOL, TEST, TRAIN, _field_cycles

from battery_rul.data.cleaning import clean_cycles, clean_inputs, label_outliers
from battery_rul.models.registry import make_model
from battery_rul.serve.field import (
    FieldPredictor,
    InputError,
    latest_sample,
    raw_inputs,
    useful,
    validate_field,
)
from battery_rul.splits.scaling import FoldScaler
from battery_rul.tasks.samples import TaskSpec, apply_prepared, build_samples, prepare_cycles
from battery_rul.train.transfer import _record_dims, load_pretrained, save_pretrained

FS = "field_curve"
TINY = {
    "d_model": 16,
    "n_heads": 2,
    "n_layers": 1,
    "channels": "all",
    "max_epochs": 2,
    "patience": 1,
    "device": "cpu",
    "batch_size": 64,
}
L, HZ = 8, (1, 5)


def _stats(prep) -> FoldScaler:
    return FoldScaler.from_stats(dict(prep.scaler.mean_), dict(prep.scaler.scale_))


def test_from_stats_roundtrip() -> None:
    prep = prepare_cycles(_field_cycles(), TRAIN, FS)
    sc = _stats(prep)
    df = prep.cycles
    pd.testing.assert_frame_equal(sc.transform(df), prep.scaler.transform(df))
    with pytest.raises(ValueError):
        FoldScaler.from_stats({"a": 0.0}, {"a": 0.0})


def test_apply_prepared_equals_prepare_cycles_on_a_new_cell() -> None:
    cyc = _field_cycles()
    prep = prepare_cycles(cyc, TRAIN, FS)
    one = cyc[cyc["cell_id"] == TEST[0]]
    served = apply_prepared(one, prep.channels, _stats(prep)).cycles
    ref = prep.cycles[prep.cycles["cell_id"] == TEST[0]]
    np.testing.assert_allclose(
        served[list(prep.channels)].to_numpy(), ref[list(prep.channels)].to_numpy()
    )


def test_clean_inputs_is_clean_cycles_without_label_drop() -> None:
    df = _cell()
    df.loc[10, "cv_time_s"] = 30.0
    df.loc[10, "capacity_ah"] -= 0.11
    df.loc[50, "ir_ohm"] = 0.5
    df.loc[60, "ir_ohm"] = -1.0
    full, rep = clean_cycles(df)
    inp, counts = clean_inputs(df)
    assert counts == rep.input_counts and len(inp) == len(df)
    keep = ~label_outliers(df)["any"].to_numpy()
    pd.testing.assert_frame_equal(inp[keep].reset_index(drop=True), full)


def _fit(task: str, prep) -> object:
    spec = TaskSpec(task=task, lookback=L, horizons=HZ, feature_set=FS)  # type: ignore[arg-type]
    tr = build_samples(prep, TRAIN, EOL, spec)
    m = make_model("itransformer", **TINY)
    m.fit(tr, None)
    _record_dims(m, tr)  # type: ignore[arg-type]
    return m


def test_checkpoint_keeps_the_field_target_offset(tmp_path: Path) -> None:
    prep = prepare_cycles(_field_cycles(), TRAIN, FS)
    m = _fit("forecast", prep)
    params = {k: v for k, v in TINY.items() if k != "device"}
    save_pretrained(m, tmp_path / "f.pt", params, L, {})  # type: ignore[arg-type]
    back = load_pretrained(tmp_path / "f.pt", device="cpu")
    spec = TaskSpec(task="forecast", lookback=L, horizons=HZ, feature_set=FS)
    te = build_samples(prep, TEST, EOL, spec)
    assert np.abs(back._y_offset).sum() > 0  # the field offset is non-zero and restored
    np.testing.assert_allclose(back.predict(te).point, m.predict(te).point, rtol=1e-5)


def _deploy_dir(tmp_path: Path) -> tuple[Path, object, dict]:
    cyc, _ = clean_inputs(_field_cycles())
    prep = prepare_cycles(cyc, TRAIN, FS)
    params = {k: v for k, v in TINY.items() if k != "device"}
    tasks, models = {}, {}
    for task in ("soh", "forecast", "rul"):
        m = _fit(task, prep)
        save_pretrained(m, tmp_path / f"{task}_0.pt", params, L, {})  # type: ignore[arg-type]
        hz = list(HZ) if task == "forecast" else [0]
        tasks[task] = {
            "members": [f"{task}_0.pt"],
            "lookback": L,
            "horizons": hz,
            "alpha": 0.1,
            "cqr_correction": {str(h): 0.0 for h in hz},
        }
        models[task] = m
    ch = list(prep.channels)
    meta = {
        "protocol": "nasa",
        "feature_set": FS,
        "channels": ch,
        "inputs": raw_inputs(ch),
        "scaler": {"mean": dict(prep.scaler.mean_), "scale": dict(prep.scaler.scale_)},
        "tasks": tasks,
        "ood": {"mean": [0.0] * len(ch), "cov": np.eye(len(ch)).tolist(), "threshold": 1e9},
    }
    (tmp_path / "field_meta.json").write_text(json.dumps(meta))
    return tmp_path, prep, models


def test_field_predictor_matches_the_training_path(tmp_path: Path) -> None:
    d, prep, models = _deploy_dir(tmp_path)
    fp = FieldPredictor(d)
    one = _field_cycles()
    one = one[one["cell_id"] == TEST[0]]
    upload = one[[c for c in fp.inputs if c in one.columns]]
    out = fp.predict(upload)
    # training path: last origin of the test cell
    for task in ("soh", "forecast"):
        bt = "soh" if task == "soh" else "forecast"
        spec = TaskSpec(task=bt, lookback=L, horizons=HZ, feature_set=FS)  # type: ignore[arg-type]
        ss = build_samples(prep, TEST, EOL, spec)
        last = ss.subset(np.arange(len(ss.meta)) == len(ss.meta) - 1)
        ref = models[task].predict(last).point[0]
        got = [out["soh_now"]["soh"]] if task == "soh" else [f["soh"] for f in out["forecast"]]
        np.testing.assert_allclose(got, ref, rtol=1e-5)
    assert set(out) >= {"soh_now", "forecast", "rul", "ood", "heldout"}
    assert out["rul"]["lo"] <= out["rul"]["cycles"] <= out["rul"]["hi"]
    assert not out["ood"]["is_ood"]


def test_latest_sample_rul_reuses_forecast_windows(tmp_path: Path) -> None:
    prep = prepare_cycles(_field_cycles(), TRAIN, FS)
    one = apply_prepared(_field_cycles().query("cell_id == 'C3'"), prep.channels, _stats(prep))
    f = latest_sample(one, "forecast", L, HZ, FS)
    r = latest_sample(one, "rul", L, HZ, FS)
    np.testing.assert_array_equal(f.x_hist, r.x_hist)
    assert r.task == "rul" and r.horizons == (0,)


def test_validate_field_contract() -> None:
    inputs = ["cycle_idx", "cv_time_s", "fld_win_dq_ah"]
    ok = pd.DataFrame({"Cycle_Idx": [3, 1, 2, 4, 5], "cv_time_s": ["1", "", "x", "4", "5"]})
    out = validate_field(ok, inputs, "toyota")
    assert out["cycle_idx"].tolist() == [1, 2, 3, 4, 5]
    assert out["fld_win_dq_ah"].isna().all() and out["cv_time_s"].isna().sum() == 2
    assert out["soh"].isna().all() and (out["dataset"] == "toyota").all()
    with pytest.raises(InputError, match="cycle_idx"):
        validate_field(pd.DataFrame({"a": [1]}), inputs, "toyota")
    with pytest.raises(InputError, match="duplicates"):
        validate_field(pd.DataFrame({"cycle_idx": [1, 1, 2, 3, 4]}), inputs, "toyota")
    with pytest.raises(InputError, match="at least"):
        validate_field(pd.DataFrame({"cycle_idx": [1, 2]}), inputs, "toyota")


def test_raw_inputs_and_useful() -> None:
    assert raw_inputs(("cycle_count", "log_rest_s", "skipped_cv", "cv_time_s", "x")) == [
        "cycle_idx",
        "rest_before_s",
        "cv_time_s",
        "x",
    ]
    assert useful(0.90, 0.92, 0.95) and not useful(0.80, 0.95, 0.90)
