"""CQR / CV+-pooled calibration on synthetic data, plus the calibrate CLI end to end."""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path
from typing import ClassVar

import numpy as np
import pandas as pd
import pytest
from scipy.stats import norm
from test_runner import _artifact, _cfg, _unit_runs, processed  # noqa: F401
from typer.testing import CliRunner

from battery_rul.cli import app
from battery_rul.models.base import FitInfo, Prediction, SampleSet, TaskName
from battery_rul.models.registry import MODELS
from battery_rul.train.config import ModelConfig
from battery_rul.train.runner import run_experiment
from battery_rul.uq.conformal import calibrate_cv_plus, cqr_correction
from battery_rul.uq.metrics_uq import interval_score, wide_to_long


def _long(
    cells: list[str], n: int, sigma: float, q_scale: float, rng: np.random.Generator, horizons=(1,)
) -> pd.DataFrame:
    """y ~ N(0, sigma); the raw 90 % interval is +/- 1.645 * sigma * q_scale around 0."""
    parts = []
    z = norm.ppf(0.95)
    for h in horizons:
        for c in cells:
            y = rng.normal(0, sigma, n)
            parts.append(
                pd.DataFrame(
                    {
                        "cell_id": c,
                        "horizon": h,
                        "y": y,
                        "mask": True,
                        "point": 0.0,
                        "lo": -z * sigma * q_scale,
                        "hi": z * sigma * q_scale,
                        "split": "test",
                        "origin_policy": "all",
                        "start_kind": "all",
                    }
                )
            )
    return pd.concat(parts, ignore_index=True)


def test_correction_finite_sample_index_and_small_n() -> None:
    y = np.arange(10, dtype=float)  # scores = |y - 0| with lo=hi=0 -> 0..9
    z = np.zeros(10)
    # n=10, alpha=0.1 -> k = ceil(11*0.9) = 10 -> the maximum
    assert cqr_correction(y, z, z, 0.1) == 9.0
    # n=8 -> k = ceil(9*0.9) = 9 > 8 -> +inf
    assert cqr_correction(y[:8], z[:8], z[:8], 0.1) == np.inf
    assert cqr_correction(np.array([]), np.array([]), np.array([]), 0.1) == np.inf
    with pytest.raises(ValueError):
        cqr_correction(y, z, z, 1.5)


def test_coverage_within_tolerance_over_many_draws() -> None:
    cov = []
    for seed in range(200):
        rng = np.random.default_rng(seed)
        inner = _long(["a", "b", "c"], 40, 1.0, 0.5, rng)  # raw under-covers badly
        test = _long(["t"], 40, 1.0, 0.5, rng)
        out = calibrate_cv_plus(inner, test, alpha=0.1)
        cov.append(np.mean((out["y"] >= out["lo_cal"]) & (out["y"] <= out["hi_cal"])))
    assert abs(np.mean(cov) - 0.90) < 0.03


def test_under_covering_widens_over_covering_narrows() -> None:
    rng = np.random.default_rng(0)
    inner = _long(["a", "b"], 400, 1.0, 0.4, rng)
    test = _long(["t"], 10, 1.0, 0.4, rng)
    out = calibrate_cv_plus(inner, test)
    assert (out["correction"] > 0).all()
    assert (out["hi_cal"] - out["lo_cal"] > out["hi"] - out["lo"]).all()

    inner = _long(["a", "b"], 400, 1.0, 3.0, rng)  # raw interval far too wide
    out = calibrate_cv_plus(inner, _long(["t"], 10, 1.0, 3.0, rng))
    assert (out["correction"] < 0).all()  # CQR allows negative corrections
    assert (out["hi_cal"] - out["lo_cal"] < out["hi"] - out["lo"]).all()
    assert (out["lo_cal"] <= out["hi_cal"]).all()


def test_rule7_guard() -> None:
    rng = np.random.default_rng(0)
    inner = _long(["a", "b"], 30, 1.0, 1.0, rng)
    with pytest.raises(ValueError, match="rule 7"):
        calibrate_cv_plus(inner, _long(["b"], 30, 1.0, 1.0, rng))


def test_point_only_symmetric_split_conformal() -> None:
    rng = np.random.default_rng(1)
    inner = _long(["a", "b", "c"], 100, 1.0, 1.0, rng).assign(lo=np.nan, hi=np.nan)
    test = _long(["t"], 2000, 1.0, 1.0, rng).assign(lo=np.nan, hi=np.nan)
    out = calibrate_cv_plus(inner, test, alpha=0.1)
    assert (out["correction"] > 0).all()
    assert np.allclose(out["hi_cal"] + out["lo_cal"], 2 * out["point"])
    cov = np.mean((out["y"] >= out["lo_cal"]) & (out["y"] <= out["hi_cal"]))
    assert abs(cov - 0.9) < 0.03
    with pytest.raises(ValueError, match="both"):
        calibrate_cv_plus(inner, _long(["t"], 5, 1.0, 1.0, rng))


def test_per_horizon_grouping_and_mask() -> None:
    rng = np.random.default_rng(2)
    h1 = _long(["a", "b"], 300, 1.0, 1.0, rng, horizons=(1,))
    h9 = _long(["a", "b"], 300, 5.0, 0.2, rng, horizons=(9,))  # 5x noisier, same raw width
    inner = pd.concat([h1, h9], ignore_index=True)
    inner.loc[(inner["horizon"] == 9) & (inner.index % 7 == 0), "mask"] = False
    test = pd.concat([_long(["t"], 5, 1.0, 1.0, rng, (1,)), _long(["t"], 5, 5.0, 0.2, rng, (9,))])
    out = calibrate_cv_plus(inner, test)
    c = out.groupby("horizon")["correction"].first()
    assert c[9] > c[1] + 3.0  # the noisy horizon gets a much larger correction
    assert out.groupby("horizon")["n_cal"].first()[9] < 600  # masked rows excluded
    # a group without calibration data -> infinite interval, not a silent pass
    only1 = calibrate_cv_plus(h1, test[test["horizon"] == 9])
    assert np.isinf(only1["hi_cal"]).all()


def test_interval_score_matches_formula() -> None:
    s = interval_score(np.array([0.0, 3.0]), np.array([-1.0, -1.0]), np.array([1.0, 1.0]), 0.1)
    assert s == pytest.approx((2.0 + (2.0 + 20.0 * 2.0)) / 2)


# ---- CLI end to end ---------------------------------------------------------------------
class QuantToy:
    """Cross-fitted probabilistic toy: mean +/- a (deliberately too narrow) band."""

    name: ClassVar[str] = "quanttoy"
    supported_tasks: ClassVar[frozenset[TaskName]] = frozenset({"forecast"})
    probabilistic: ClassVar[bool] = True
    cross_fit: ClassVar[bool] = True

    def __init__(self, device: str = "cpu") -> None:
        self.c: np.ndarray | None = None

    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        self.c = np.array([train.y[train.y_mask[:, j], j].mean() for j in range(train.y.shape[1])])
        return FitInfo(n_train=len(train))

    def predict(self, samples: SampleSet) -> Prediction:
        assert self.c is not None
        pt = np.tile(self.c, (len(samples), 1))
        q = np.stack([pt - 0.002, pt - 0.001, pt, pt + 0.001, pt + 0.002], axis=2)
        return Prediction(pt, q, (0.05, 0.25, 0.5, 0.75, 0.95))


@pytest.fixture
def toy_registered() -> Iterator[None]:
    MODELS["quanttoy"] = QuantToy
    yield
    MODELS.pop("quanttoy", None)


def test_calibrate_cli_end_to_end(tmp_path: Path, processed: Path, toy_registered: None) -> None:  # noqa: F811
    import mlflow

    cfg = _cfg(
        tmp_path,
        name="cal",
        datasets=["calce"],
        models=[ModelConfig("quanttoy"), ModelConfig("persistence")],
    )
    run_experiment(cfg, processed)
    cli = CliRunner()
    args = ["calibrate", "--experiment", "cal", "--tracking-uri", cfg.tracking_uri]
    r = cli.invoke(app, args)
    assert r.exit_code == 0, r.output
    assert "4 calibrated" in r.output
    runs = _unit_runs(cfg)
    q = runs[runs["params.model"] == "quanttoy"]
    assert (q["tags.calibrated_alpha"] == "0.1").all()
    row = q.iloc[0]
    run = mlflow.get_run(row["run_id"])
    m = run.data.metrics
    key_cal = "cal/test/all/overall/picp_h10"
    assert key_cal in m and "raw/test/all/overall/picp_h10" in m
    assert m["cal/test/all/overall/mpiw_h10"] > m["raw/test/all/overall/mpiw_h10"]
    cp = _artifact(row["run_id"], "calibrated_predictions.parquet")
    assert {"lo_cal", "hi_cal", "lo", "hi", "horizon"} <= set(cp.columns)
    # persistence is point-only with no inner-val: untouched
    assert runs[runs["params.model"] == "persistence"]["tags.calibrated_alpha"].isna().all()

    # idempotent: nothing new on a second call
    r2 = cli.invoke(app, args)
    assert "0 calibrated" in r2.output and "4 already done" in r2.output
    # a different alpha recalibrates
    r3 = cli.invoke(app, [*args, "--alpha", "0.5"])
    assert "4 calibrated" in r3.output

    from battery_rul.eval.report import write_report

    md, _ = write_report("cal", cfg.tracking_uri, tmp_path / "tables")
    text = md.read_text()
    assert "## Calibration" in text and "quanttoy" in text
    assert list((tmp_path / "figures").glob("cal_reliability_calce.png"))


def test_wide_to_long_requires_alpha_pair() -> None:
    f = pd.DataFrame(
        {
            "cell_id": ["a"],
            "y_h1": [1.0],
            "y_mask_h1": [True],
            "point_h1": [1.0],
            "q0.25_h1": [0.9],
            "q0.75_h1": [1.1],
        }
    )
    assert wide_to_long(f, 0.5)["hi"].iloc[0] == pytest.approx(1.1)
    with pytest.raises(ValueError, match="lacks"):
        wide_to_long(f, 0.1)
