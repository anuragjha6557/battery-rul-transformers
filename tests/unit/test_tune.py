"""Tuning tests on a synthetic Toyota-like dataset (tiny budgets; no real data, tmp stores)."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any

import numpy as np
import optuna
import pandas as pd
import pytest
import yaml

from battery_rul.models.linear import NLinear
from battery_rul.train import config as config_mod
from battery_rul.train.config import ExperimentConfig, ModelConfig, resolve_tuned_models
from battery_rul.train.runner import run_experiment
from battery_rul.train.tune import (
    TuneSpec,
    TuningError,
    boundary_hits,
    make_objective,
    make_pruner,
    primary_horizon,
    thin_origins,
    tune,
)

_spec = importlib.util.spec_from_file_location(
    "synthetic_toyota", Path(__file__).parents[1] / "synthetic_toyota.py"
)
assert _spec is not None and _spec.loader is not None
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
write_toyota = _mod.write_toyota

ELASTICNET = """name: elasticnet
params: {alpha: 1.0e-3, l1_ratio: 0.5, n_lags: 10, lookback: 16}
search:
  alpha: {type: float, low: 1.0e-5, high: 1.0, log: true}
  l1_ratio: {type: float, low: 0.0, high: 1.0}
  n_lags: {type: categorical, choices: [5, 10]}
"""
NLINEAR = """name: nlinear
params: {lookback: 16, max_epochs: 6, patience: 3, quantiles: null, device: cpu}
search:
  lr: {type: float, low: 1.0e-4, high: 1.0e-2, log: true}
  weight_decay: {type: float, low: 1.0e-6, high: 1.0e-2, log: true}
"""
PERSISTENCE = "name: persistence\nparams: {}\n"


@pytest.fixture
def env(tmp_path: Path) -> dict[str, Any]:
    processed = tmp_path / "processed"
    write_toyota(processed)
    cdir = tmp_path / "configs"
    (cdir / "model").mkdir(parents=True)
    for name, text in (
        ("elasticnet", ELASTICNET),
        ("nlinear", NLINEAR),
        ("persistence", PERSISTENCE),
    ):
        (cdir / "model" / f"{name}.yaml").write_text(text)
    return {
        "config_dir": cdir,
        "processed_dir": processed,
        "journal": tmp_path / "optuna" / "journal.log",
        "tracking_uri": f"sqlite:///{tmp_path / 'mlflow.db'}",
    }


def test_resume_and_tuned_yaml(env: dict[str, Any]) -> None:
    r1 = tune("elasticnet", "forecast", n_trials=3, n_jobs=1, train_stride=4, **env)
    assert r1.n_trials_total == 3 and r1.n_complete == 3
    r2 = tune("elasticnet", "forecast", n_trials=2, n_jobs=1, train_stride=4, **env)
    assert r2.n_trials_total == 5  # resumed, not restarted
    assert r2.mlflow_run_id != r1.mlflow_run_id

    out = yaml.safe_load((env["config_dir"] / "tuned" / "elasticnet__forecast.yaml").read_text())
    assert out["name"] == "elasticnet" and out["tuned_from"] == r2.mlflow_run_id
    assert out["search_hash"] == r2.search_hash
    assert set(out["params"]) >= {"alpha", "l1_ratio", "n_lags", "lookback"}  # defaults + best
    assert out["params"]["alpha"] == r2.best_params["alpha"]

    import mlflow

    mlflow.set_tracking_uri(env["tracking_uri"])
    run = mlflow.get_run(r2.mlflow_run_id)
    assert run.data.params["model"] == "elasticnet" and run.data.params["train_stride"] == "4"
    assert run.data.metrics["n_complete"] == 5
    assert mlflow.get_experiment(run.info.experiment_id).name == "tuning"


def test_parallel_workers_share_study(env: dict[str, Any]) -> None:
    r = tune("elasticnet", "forecast", n_trials=4, n_jobs=2, train_stride=4, **env)
    assert r.n_trials_total == 4 and r.n_complete == 4


def test_refuses_untunable(env: dict[str, Any]) -> None:
    with pytest.raises(TuningError, match="not tunable"):
        tune("persistence", "forecast", n_trials=1, n_jobs=1, **env)
    with pytest.raises(TuningError, match="does not support"):
        tune("elasticnet", "bogus", n_trials=1, n_jobs=1, **env)


def test_boundary_hits() -> None:
    search = {
        "lr": {"type": "float", "low": 1e-4, "high": 1e-2, "log": True},
        "x": {"type": "float", "low": 0.0, "high": 1.0},
        "n": {"type": "int", "low": 8, "high": 64, "log": True},
        "c": {"type": "categorical", "choices": [1, 2]},
    }
    # lr 1.05e-4 is 2.5 % up the log range; x mid-range; n=63 is near the top; c ignored
    hits = boundary_hits(search, {"lr": 1.05e-4, "x": 0.5, "n": 63, "c": 1})
    assert {(h["param"], h["side"]) for h in hits} == {("lr", "low"), ("n", "high")}
    # log params are measured in log space: 1e-3 is mid-range
    assert [h["param"] for h in boundary_hits(search, {"lr": 1e-3, "x": 0.97, "n": 20})] == ["x"]


def test_boundary_flag_fires_in_study(env: dict[str, Any]) -> None:
    # contrived: a 2-value int range, so the best value is necessarily on a bound
    (env["config_dir"] / "model" / "elasticnet.yaml").write_text(
        ELASTICNET + "  max_iter: {type: int, low: 20000, high: 20001}\n"
    )
    r = tune("elasticnet", "forecast", n_trials=2, n_jobs=1, **env)
    assert [h["param"] for h in r.boundary if h["param"] == "max_iter"] == ["max_iter"]


def test_changed_search_space_is_refused(env: dict[str, Any]) -> None:
    tune("elasticnet", "forecast", n_trials=1, n_jobs=1, **env)
    (env["config_dir"] / "model" / "elasticnet.yaml").write_text(
        ELASTICNET.replace("[5, 10]", "[5, 10, 20]")
    )
    with pytest.raises(TuningError, match="search space"):
        tune("elasticnet", "forecast", n_trials=1, n_jobs=1, **env)


def test_neural_tuning_runs(env: dict[str, Any]) -> None:
    r = tune("nlinear", "forecast", n_trials=2, n_jobs=1, train_stride=8, **env)
    assert r.n_complete + r.n_pruned == 2 and np.isfinite(r.best_value)


def test_epoch_callback_exception_propagates() -> None:
    from battery_rul.models.base import SampleSet

    rng = np.random.default_rng(0)
    n, L = 40, 8
    soh = 1 - 0.002 * np.arange(L)[None, :] - rng.uniform(0, 0.1, (n, 1))
    y = (soh[:, -1:] - 0.01 * np.array([[1, 10]])).astype(np.float32)
    ss = SampleSet(
        task="forecast",
        x_hist=soh[..., None].astype(np.float32),
        hist_mask=np.ones((n, L), bool),
        x_tab=np.zeros((n, 1), np.float32),
        y=y,
        y_mask=np.ones_like(y, bool),
        horizons=(1, 10),
        channel_names=("soh",),
        feature_names=("f",),
        meta=pd.DataFrame({"dataset": "x", "cell_id": "c", "origin_cycle": np.arange(n)}),
    )
    seen: list[tuple[int, float]] = []

    def cb(epoch: int, v: float) -> None:
        seen.append((epoch, v))
        if epoch == 3:
            raise optuna.TrialPruned()

    m = NLinear(max_epochs=10, quantiles=None, device="cpu", epoch_callback=cb)
    with pytest.raises(optuna.TrialPruned):
        m.fit(ss, ss)
    assert [e for e, _ in seen] == [1, 2, 3]


def test_objective_prunes_through_callback(env: dict[str, Any]) -> None:
    class PruneNow(optuna.trial.FixedTrial):
        def should_prune(self) -> bool:
            return True

    spec = TuneSpec(
        name="nlinear",
        task="forecast",
        defaults={"lookback": 16, "max_epochs": 5, "quantiles": None, "device": "cpu"},
        search={"lr": {"type": "float", "low": 1e-4, "high": 1e-2, "log": True}},
        train_stride=8,
        processed_dir=str(env["processed_dir"]),
        journal=str(env["journal"]),
    )
    with pytest.raises(optuna.TrialPruned):
        make_objective(spec)(PruneNow({"lr": 1e-3}))


def test_runner_accepts_tuned_reference(
    env: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    r = tune("elasticnet", "forecast", n_trials=2, n_jobs=1, **env)
    monkeypatch.setattr(config_mod, "CONFIG_DIR", env["config_dir"])
    cfg = ExperimentConfig(
        name="tuned_ref",
        datasets=["toyota"],
        tasks=["forecast"],
        models=[ModelConfig(tuned="elasticnet__forecast")],
        lookback=16,
        eval_origins=["all"],
        tracking_uri=env["tracking_uri"],
    )
    res = resolve_tuned_models(cfg)
    m = res.models[0]
    assert m.name == "elasticnet" and m.tuned_from == r.mlflow_run_id
    assert m.params["alpha"] == r.best_params["alpha"]
    # rule 6 satisfied via tuned_from (allow_untuned is False)
    s = run_experiment(cfg, env["processed_dir"])
    assert s.n_run == 1
    import mlflow

    mlflow.set_tracking_uri(env["tracking_uri"])
    runs = mlflow.search_runs(experiment_names=["tuned_ref"])
    assert (runs["params.tuned_from"].dropna() == r.mlflow_run_id).sum() == 1

    bad = ExperimentConfig(
        name="x", tasks=["rul"], models=[ModelConfig(tuned="elasticnet__forecast")]
    )
    with pytest.raises(ValueError, match="none for task"):
        resolve_tuned_models(bad)
    with pytest.raises(FileNotFoundError):
        resolve_tuned_models(
            ExperimentConfig(
                name="x", tasks=["forecast"], models=[ModelConfig(tuned="nope__forecast")]
            )
        )


def test_thin_origins_and_primary_horizon() -> None:
    assert primary_horizon((1, 10, 50, 100, 200)) == 50
    assert primary_horizon((1, 10, 25)) == 25
    with pytest.raises(TuningError):
        primary_horizon((100,))

    class S:  # minimal stand-in: thin_origins only needs meta and subset
        meta = pd.DataFrame({"cell_id": ["a"] * 5 + ["b"] * 4})

        def subset(self, idx: np.ndarray) -> np.ndarray:
            return idx

    kept = thin_origins(S(), 3)  # type: ignore[arg-type]
    assert kept.tolist() == [True, False, False, True, False, True, False, False, True]


def test_pruner_never_prunes_before_patience() -> None:
    study = optuna.create_study(pruner=make_pruner())
    for i in range(30):
        t = study.ask()
        for step in range(1, 20):  # epochs 1..19 of fold 0: before early stopping can act
            t.report(1e3 * (i + 1), step)  # increasingly terrible values
            assert not t.should_prune()
        study.tell(t, 1e3 * (i + 1))


def test_tuned_entries_are_task_scoped(
    env: dict[str, Any], monkeypatch: pytest.MonkeyPatch
) -> None:
    tune("elasticnet", "forecast", n_trials=1, n_jobs=1, **env)
    tune("elasticnet", "soh", n_trials=1, n_jobs=1, **env)
    monkeypatch.setattr(config_mod, "CONFIG_DIR", env["config_dir"])
    both = ExperimentConfig(
        name="scoped",
        datasets=["toyota"],
        tasks=["forecast", "soh"],
        models=[ModelConfig(tuned="elasticnet__forecast"), ModelConfig(tuned="elasticnet__soh")],
        lookback=16,
        eval_origins=["all"],
        tracking_uri=env["tracking_uri"],
    )
    s = run_experiment(both, env["processed_dir"])
    # each tuned entry runs only for its own task: 1 unit per task, 2 skipped pairings
    assert s.n_run == 2
    only_forecast = ExperimentConfig(
        name="x", tasks=["forecast", "soh"], models=[ModelConfig(tuned="elasticnet__forecast")]
    )
    with pytest.raises(ValueError, match=r"none for task\(s\) \['soh'\]"):
        resolve_tuned_models(only_forecast)


def test_finalize_only_requires_existing_study(tmp_path) -> None:  # type: ignore[no-untyped-def]
    import pytest

    from battery_rul.train.tune import TuningError, tune

    with pytest.raises(TuningError, match="finalize-only"):
        tune("elasticnet", "forecast", n_trials=0, journal=tmp_path / "j.log")
