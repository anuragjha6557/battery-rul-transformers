# ADR-0003: Configuration with Hydra + structured configs

- **Status:** Accepted
- **Date:** 2026-11-15

## Context
The benchmark is a product of axes: 3 datasets × 3 tasks × ~11 models × feature sets × start points × seeds, plus ablations. Each run must be fully specified by a file, reproducible, and traceable from an MLflow run back to its exact configuration. CLI-flag soup and ad-hoc dicts don't meet that bar.

## Options considered
1. **argparse/typer flags.** Not composable, and history lives in shell scripts.
2. **Plain YAML + pydantic-settings.** Typed, but no composition or multirun; we would rebuild Hydra badly.
3. **gin-config.** Powerful, but magical and less familiar to interviewers.
4. **Hydra + OmegaConf with structured (dataclass) schemas.** Config groups (`data/`, `model/`, `task/`, `experiment/`) compose cleanly. Overrides and multirun (`-m model=a,b seed=0,1,2`) are built in, and dataclass schemas give type checking.

## Decision
Option 4. Config groups live under `configs/`. Each experiment file in `configs/experiment/` declares its defaults list and is the single source for a results table. The training entry point resolves the config, computes `battery_rul.utils.config_hash()` on it, and logs both the resolved YAML and the hash to MLflow. The hash also keys the feature/tensor cache and lets reruns skip already-completed runs. Hydra's per-run output dirs (`outputs/`, `multirun/`) are gitignored; MLflow is the record of truth.

## Consequences
- The CLI (`typer`) is a thin wrapper that hands config names to Hydra's compose API; there is no business logic in flags.
- Every reported number is reproducible with `battery-rul benchmark --config <experiment>`.
