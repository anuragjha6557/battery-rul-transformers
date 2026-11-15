"""End-to-end runner tests on a tiny synthetic dataset and a tmp MLflow store."""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path
from typing import Any, ClassVar

import numpy as np
import pandas as pd
import pytest

from battery_rul.data.io import DatasetTables, finalize_and_validate, write_tables
from battery_rul.eval.report import make_tables, write_report
from battery_rul.models.base import FitInfo, Prediction, SampleSet, TaskName
from battery_rul.models.registry import MODELS
from battery_rul.train.config import ExperimentConfig, ModelConfig
from battery_rul.train.runner import UntunedModelError, average_predictions, run_experiment

N_CYC = 70
NASA = ["B0005", "B0006", "B0007", "B0018"]
CALCE = ["CS2_35", "CS2_36", "CS2_37", "CS2_38"]
TOYOTA_TRAIN = [f"t{i}" for i in range(6)]


class ConstModel:
    """Tunable, cross-fitted toy model: predicts the mean training target per column."""

    name: ClassVar[str] = "const"
    supported_tasks: ClassVar[frozenset[TaskName]] = frozenset({"forecast", "soh"})
    probabilistic: ClassVar[bool] = False
    fits: ClassVar[list[np.ndarray]] = []

    def __init__(self, device: str = "cpu") -> None:
        self.c: np.ndarray | None = None

    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        assert val is not None
        assert not set(val.meta["cell_id"]) & set(train.meta["cell_id"])
        self.c = np.array([train.y[train.y_mask[:, j], j].mean() for j in range(train.y.shape[1])])
        ConstModel.fits.append(self.c)
        return FitInfo(n_train=len(train), n_val=len(val), best_val_loss=0.5)

    def predict(self, samples: SampleSet) -> Prediction:
        assert self.c is not None
        return Prediction(point=np.tile(self.c, (len(samples), 1)))


def _write(root: Path, dataset: str, ids: list[str], splits: list[str | None], n: int) -> None:
    rng = np.random.default_rng(len(ids) + n)
    rows = []
    for i, c in enumerate(ids):
        cap = 1.1 * (1 - (0.25 + 0.03 * i) * np.arange(n) / n) + rng.normal(0, 0.002, n)
        rows.append(
            pd.DataFrame(
                {
                    "dataset": dataset,
                    "cell_id": c,
                    "cycle_idx": np.arange(1, n + 1),
                    "capacity_ah": cap,
                    "charge_throughput_ah": cap * 1.02,
                    "cc_time_s": 1000.0 + rng.normal(0, 5, n),
                    "cv_time_s": 900.0 + rng.normal(0, 5, n),
                    "discharge_time_s": cap * 3000,
                }
            )
        )
    cells = pd.DataFrame(
        {
            "dataset": dataset,
            "cell_id": ids,
            "chemistry": "x",
            "nominal_capacity_ah": 1.1,
            "charge_protocol": "cc",
            "discharge_protocol": "cc",
            "ambient_temp_c": 25.0,
            "v_max": 4.2,
            "v_min": 2.7,
            "batch": None,
            "split": splits,
            "reported_cycle_life": 60.0 if dataset == "toyota" else None,
            "source_file": "synthetic",
        }
    )
    curves = pd.DataFrame(
        {
            "dataset": dataset,
            "cell_id": ids[0],
            "cycle_idx": [1],
            "phase": ["charge"],
            "sample_idx": [0],
            "t_s": [0.0],
            "voltage_v": [3.7],
            "current_a": [1.0],
            "temp_c": [25.0],
            "charge_ah": [0.0],
        }
    )
    t = finalize_and_validate(cells, pd.concat(rows, ignore_index=True), curves)
    write_tables(dataset, DatasetTables(t.cells, t.cycles, t.curves), root)


@pytest.fixture
def processed(tmp_path: Path) -> Path:
    root = tmp_path / "processed"
    _write(root, "nasa", NASA, [None] * 4, N_CYC)
    _write(root, "calce", CALCE, [None] * 4, N_CYC)
    _write(root, "toyota", [*TOYOTA_TRAIN, "a1", "b1"], ["train"] * 6 + ["test1", "test2"], N_CYC)
    return root


@pytest.fixture
def const_registered() -> Iterator[None]:
    MODELS["const"] = ConstModel
    ConstModel.fits.clear()
    yield
    MODELS.pop("const", None)


def _cfg(tmp_path: Path, **kw: Any) -> ExperimentConfig:
    base: dict[str, Any] = {
        "name": "t",
        "datasets": ["nasa", "calce", "toyota"],
        "tasks": ["forecast"],
        "models": [ModelConfig("persistence"), ModelConfig("last_slope", {"window": 5})],
        "seeds": [0],
        "lookback": 16,
        "eval_origins": ["start_points", "all"],
        "allow_untuned": True,
        "tracking_uri": f"sqlite:///{tmp_path / 'mlflow.db'}",
        "horizons": {"nasa": [1, 10], "calce": [1, 10], "toyota": [1, 10]},
    }
    base.update(kw)
    return ExperimentConfig(**base)


def _unit_runs(cfg: ExperimentConfig) -> pd.DataFrame:
    import mlflow

    mlflow.set_tracking_uri(cfg.tracking_uri)
    df = mlflow.search_runs(experiment_names=[cfg.name])
    return df[df["tags.unit_key"].notna()]


def _artifact(run_id: str, name: str) -> pd.DataFrame:
    import mlflow

    return pd.read_parquet(mlflow.artifacts.download_artifacts(run_id=run_id, artifact_path=name))


def test_smoke_resume_artifacts_and_report(tmp_path: Path, processed: Path) -> None:
    cfg = _cfg(tmp_path)
    s = run_experiment(cfg, processed)
    # (4 nasa + 4 calce + 1 toyota folds) x 2 models; every unit has "all" samples
    assert s.n_run == 18 and s.n_resumed == 0
    runs = _unit_runs(cfg)
    assert len(runs) == 18
    assert set(runs["params.protocol_version"]) == {"1.1"}
    assert (runs["params.tuned_from"] == "none").all()

    s2 = run_experiment(cfg, processed)
    assert s2.n_run == 0 and s2.n_resumed == 18
    assert len(_unit_runs(cfg)) == 18

    r = runs[(runs["params.dataset"] == "nasa") & (runs["params.fold"] == "B0018")].iloc[0]
    assert r["params.independent_fold"] == "True"
    p = _artifact(r["run_id"], "predictions.parquet")
    for col in (
        "cell_id",
        "origin_cycle",
        "start_kind",
        "y_h1",
        "y_mask_h10",
        "point_h10",
        "split",
    ):
        assert col in p.columns
    assert set(p["origin_policy"]) == {"start_points", "all"}

    tables = make_tables(cfg.name, cfg.tracking_uri)
    t = tables["nasa_forecast"]
    sel = (t.metric == "rmse_h10") & (t.model == "persistence") & (t.policy == "all")
    row = t[sel].iloc[0]
    assert row.n_cells == 4 and row.ci_lo <= row["mean"] <= row.ci_hi
    assert not np.isnan(row.independent)
    assert set(tables["toyota_forecast"]["split"]) == {"test1", "test2"}
    md, csv = write_report(cfg.name, cfg.tracking_uri, tmp_path / "out")
    assert "wide by construction" in md.read_text() and "1.1" in md.read_text()
    assert "run_ids" in csv.read_text().splitlines()[0]


def test_rule6_refuses_untuned_tunable_model(
    tmp_path: Path, processed: Path, const_registered: None
) -> None:
    cfg = _cfg(tmp_path, models=[ModelConfig("const")], allow_untuned=False)
    with pytest.raises(UntunedModelError):
        run_experiment(cfg, processed)
    ok = _cfg(
        tmp_path,
        models=[ModelConfig("const", tuned_from="abc123")],
        datasets=["nasa"],
        allow_untuned=False,
    )
    run_experiment(ok, processed)
    assert set(_unit_runs(ok)["params.tuned_from"]) == {"abc123"}


def test_cross_fit_averages_sub_models(
    tmp_path: Path, processed: Path, const_registered: None
) -> None:
    cfg = _cfg(
        tmp_path,
        datasets=["nasa"],
        models=[ModelConfig("const", {"lookback": 8})],
        eval_origins=["all"],
    )
    run_experiment(cfg, processed)
    assert len(ConstModel.fits) == 4 * 3  # 4 outer folds x 3 inner sub-models
    runs = _unit_runs(cfg).sort_values("params.fold")
    assert (runs["params.lookback"] == "8").all()
    for i, (_, r) in enumerate(runs.iterrows()):
        subs = ConstModel.fits[3 * i : 3 * i + 3]
        p = _artifact(r["run_id"], "predictions.parquet")
        np.testing.assert_allclose(p["point_h1"], np.mean([c[0] for c in subs]), rtol=1e-5)
        iv = _artifact(r["run_id"], "inner_val_predictions.parquet")
        assert iv["inner_fold"].nunique() == 3
        assert r["metrics.n_sub_models"] == 3


def test_unsupported_task_is_skipped(tmp_path: Path, processed: Path) -> None:
    cfg = _cfg(
        tmp_path, datasets=["nasa"], tasks=["soh", "forecast"], models=[ModelConfig("persistence")]
    )
    s = run_experiment(cfg, processed)
    assert s.n_unsupported == 1 and s.n_run == 4


def test_average_predictions_quantiles() -> None:
    a = Prediction(np.zeros((2, 1)), np.zeros((2, 1, 2)), (0.1, 0.9))
    b = Prediction(np.full((2, 1), 2.0), np.full((2, 1, 2), 4.0), (0.1, 0.9))
    m = average_predictions([a, b])
    assert m.point[0, 0] == 1.0 and m.quantiles is not None and m.quantiles[0, 0, 1] == 2.0


def test_hydra_smoke_config_composes() -> None:
    from battery_rul.train.config import load_experiment

    c = load_experiment("smoke", ["seeds=[0,1]"])
    assert c.seeds == [0, 1] and c.allow_untuned and c.eval_origins == ["start_points", "all"]
    assert [m.name for m in c.models] == ["persistence", "last_slope"]
    assert c.horizons["toyota"] == [1, 10, 50, 100, 200]
