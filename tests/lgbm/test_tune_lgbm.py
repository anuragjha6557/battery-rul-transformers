"""Tuning a LightGBM model (own pytest process: OpenMP isolation, see models/registry.py)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest
import yaml

from battery_rul.train.tune import tune

pytestmark = pytest.mark.lightgbm

_spec = importlib.util.spec_from_file_location(
    "synthetic_toyota", Path(__file__).parents[1] / "synthetic_toyota.py"
)
assert _spec is not None and _spec.loader is not None
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

LGBM = """name: lgbm
params: {n_estimators: 30, quantile: false, n_lags: 5, lookback: 16, num_leaves: 8}
search:
  learning_rate: {type: float, low: 0.05, high: 0.3, log: true}
  min_child_samples: {type: int, low: 5, high: 50, log: true}
"""


def test_lgbm_study_resumes(tmp_path: Path) -> None:
    processed = tmp_path / "processed"
    _mod.write_toyota(processed)
    cdir = tmp_path / "configs"
    (cdir / "model").mkdir(parents=True)
    (cdir / "model" / "lgbm.yaml").write_text(LGBM)
    kw = {
        "config_dir": cdir,
        "processed_dir": processed,
        "journal": tmp_path / "optuna" / "journal.log",
        "tracking_uri": f"sqlite:///{tmp_path / 'mlflow.db'}",
        "train_stride": 4,
        "n_jobs": 1,
    }
    r1 = tune("lgbm", "forecast", n_trials=2, **kw)  # type: ignore[arg-type]
    r2 = tune("lgbm", "forecast", n_trials=1, **kw)  # type: ignore[arg-type]
    assert (r1.n_trials_total, r2.n_trials_total) == (2, 3) and r1.n_pruned == 0
    out = yaml.safe_load((cdir / "tuned" / "lgbm__forecast.yaml").read_text())
    assert out["tuned_from"] == r2.mlflow_run_id and out["params"]["n_estimators"] == 30
