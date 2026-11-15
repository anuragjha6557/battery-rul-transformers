"""Hydra structured configs for benchmark experiments (ADR-0003).

NOTE: no ``from __future__ import annotations`` here — OmegaConf resolves the dataclass field
types at runtime.
"""

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from omegaconf import MISSING, OmegaConf

from battery_rul.utils import PROJECT_ROOT

CONFIG_DIR = Path(os.environ.get("BATTERY_RUL_CONFIG_DIR", PROJECT_ROOT / "configs"))
PROTOCOL_VERSION = "1.1"


def default_tracking_uri() -> str:
    return os.environ.get("MLFLOW_TRACKING_URI", "sqlite:///mlflow.db")


def default_horizons() -> dict[str, list[int]]:
    """PROTOCOL §2 Task B horizons per dataset."""
    return {
        "nasa": [1, 10, 25, 50, 100],
        "calce": [1, 10, 25, 50, 100],
        "toyota": [1, 10, 50, 100, 200],
    }


@dataclass
class ModelConfig:
    name: str = MISSING
    params: dict[str, Any] = field(default_factory=dict)
    #: MLflow run ID (or run-group ID) of the tuning run that produced ``params``.
    #: Required for tunable models (PROTOCOL §4 rule 6).
    tuned_from: str | None = None


@dataclass
class ExperimentConfig:
    name: str = MISSING
    datasets: list[str] = field(default_factory=lambda: ["nasa", "calce", "toyota"])
    tasks: list[str] = field(default_factory=lambda: ["forecast"])
    models: list[ModelConfig] = field(default_factory=list)
    seeds: list[int] = field(default_factory=lambda: [0])
    lookback: int = 32
    horizons: dict[str, list[int]] = field(default_factory=default_horizons)
    feature_set: str = "mc"
    theta: float = 0.8
    eval_origins: list[str] = field(default_factory=lambda: ["start_points"])
    n_jobs: int = 1
    device: str = "auto"
    allow_untuned: bool = False
    tracking_uri: str = field(default_factory=default_tracking_uri)
    protocol_version: str = PROTOCOL_VERSION


def register_configs() -> None:
    """Register the schema with Hydra's ConfigStore (idempotent)."""
    from hydra.core.config_store import ConfigStore

    ConfigStore.instance().store(name="experiment_schema", node=ExperimentConfig)


def load_experiment(
    name: str, overrides: list[str] | None = None, config_dir: Path | None = None
) -> ExperimentConfig:
    """Compose ``configs/experiment/<name>.yaml`` (+ overrides) into a typed config."""
    from hydra import compose, initialize_config_dir
    from hydra.core.global_hydra import GlobalHydra

    register_configs()
    GlobalHydra.instance().clear()
    cdir = (config_dir or CONFIG_DIR).resolve()
    with initialize_config_dir(config_dir=str(cdir), version_base="1.3"):
        cfg = compose(config_name=f"experiment/{name}", overrides=overrides or [])
    obj = OmegaConf.to_object(cfg)
    assert isinstance(obj, ExperimentConfig)
    return obj


def horizons_for(cfg: ExperimentConfig, dataset: str) -> tuple[int, ...]:
    return tuple(int(h) for h in cfg.horizons[dataset])
