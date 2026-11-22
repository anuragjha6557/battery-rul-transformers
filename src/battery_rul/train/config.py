"""Hydra structured configs for benchmark experiments (ADR-0003).

NOTE: no ``from __future__ import annotations`` here — OmegaConf resolves the dataclass field
types at runtime.
"""

import os
from dataclasses import dataclass, field, replace
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
    #: Model registry name. May be left empty when ``tuned`` is set (filled from the tuned file).
    name: str = ""
    params: dict[str, Any] = field(default_factory=dict)
    #: MLflow run ID (or run-group ID) of the tuning run that produced ``params``.
    #: Required for tunable models (PROTOCOL §4 rule 6).
    tuned_from: str | None = None
    #: Reference to ``configs/tuned/<tuned>.yaml`` (written by ``battery-rul tune``), e.g.
    #: ``"lgbm__forecast"``. Resolved by :func:`resolve_tuned_models`: the file supplies
    #: ``name``, ``params`` and ``tuned_from``; explicit ``params`` here override file params.
    tuned: str | None = None
    #: Task the tuned file was tuned for (set by resolution); the runner runs the model only there.
    tuned_task: str | None = None


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
    #: ADR-0016: forecast conditioned on the planned rest schedule (known-future covariates).
    future_rest: bool = False
    #: Task B only (ADR-0020 Stage 3): planned rest of the next K cycles as features (0 = off).
    future_rest_seq: int = 0
    #: ADR-0017: datasets whose CV-skip artifact cycles (cv_time_s < 300 s) are dropped as
    #: invalid capacity measurements before windowing (inputs and targets).
    drop_skipped_cv: list[str] = field(default_factory=list)
    #: ADR-0018 outlier policy (label outliers dropped, causal input masking).
    clean: bool = False
    theta: float = 0.8
    eval_origins: list[str] = field(default_factory=lambda: ["start_points"])
    # Keep every k-th *training* window per cell, per dataset (default 1 = all). Validation
    # (inner held-out) and test windows are never thinned. PROTOCOL deviation log 2026-11-16.
    train_stride: dict[str, int] = field(default_factory=dict)
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


def tuned_path(tuned: str, config_dir: Path | None = None) -> Path:
    return (config_dir or CONFIG_DIR) / "tuned" / f"{tuned}.yaml"


def resolve_tuned_models(cfg: ExperimentConfig, config_dir: Path | None = None) -> ExperimentConfig:
    """Return ``cfg`` with every ``ModelConfig(tuned=...)`` expanded from its tuned file.

    A tuned entry applies only to its own task (``<model>__<task>``; ADR-0006: one study per
    (model, task)): the runner skips it for other tasks. A tunable model that appears *only*
    through tuned entries must have one for every task of the experiment, otherwise this raises.
    Idempotent; models without ``tuned`` pass through unchanged.
    """
    models: list[ModelConfig] = []
    for m in cfg.models:
        if m.tuned is None:
            models.append(m)
            continue
        path = tuned_path(m.tuned, config_dir)
        if not path.exists():
            raise FileNotFoundError(f"tuned config {m.tuned!r} not found at {path}")
        raw = OmegaConf.to_container(OmegaConf.load(path), resolve=True)
        assert isinstance(raw, dict)
        task = str(raw.get("task") or m.tuned.rpartition("__")[2])
        if m.name and m.name != raw["name"]:
            raise ValueError(f"model name {m.name!r} conflicts with tuned file ({raw['name']!r})")
        models.append(
            ModelConfig(
                name=str(raw["name"]),
                params={**dict(raw.get("params") or {}), **m.params},
                tuned_from=m.tuned_from or str(raw["tuned_from"]),
                tuned=m.tuned,
                tuned_task=task,
            )
        )
    _check_tuned_coverage(cfg, models)
    return replace(cfg, models=models)


def _check_tuned_coverage(cfg: ExperimentConfig, models: list[ModelConfig]) -> None:
    from battery_rul.models.registry import MODELS, model_trait

    for name in sorted({m.name for m in models}):
        entries = [m for m in models if m.name == name]
        if not all(m.tuned_task for m in entries) or name not in MODELS:
            continue  # also listed untuned (rule 6 handles it) or unknown
        if not model_trait(MODELS[name], "tunable"):
            continue
        supported = getattr(MODELS[name], "supported_tasks", None)
        covered = {m.tuned_task for m in entries}
        missing = [
            t for t in cfg.tasks if t not in covered and (supported is None or t in supported)
        ]
        if missing:
            raise ValueError(
                f"model {name!r} appears only via tuned entries but has none for task(s) "
                f"{missing}; add `tuned: {name}__<task>` entries or drop those tasks"
            )
