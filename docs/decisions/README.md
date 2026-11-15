# Architecture Decision Records

Format and rules: [ADR-0001](0001-record-architecture-decisions.md). Experiment-driven ADRs pre-register their hypothesis before the run and cite MLflow run IDs afterwards.

| # | Title | Status |
|---|---|---|
| [0001](0001-record-architecture-decisions.md) | Record decisions as ADRs | Accepted |
| [0002](0002-toolchain.md) | Toolchain: uv, Python 3.12, PyTorch, MLflow, ruff/mypy/pytest | Accepted |
| [0003](0003-config-system.md) | Configuration with Hydra + structured configs | Accepted |
| [0004](0004-evaluation-protocol.md) | Evaluation protocol: 3 tasks, LOCO + cross-fitted CV+, Toyota-only tuning | Accepted |
| [0005](0005-eol-definition.md) | EOL rule (masked+sustained), thresholds, fixed starts, fold independence | Accepted |
| [0006](0006-equal-budget-tuning.md) | Equal tuning budget for every model, selected on Toyota | Accepted |
| [0007](0007-compute-strategy.md) | Compute strategy: MPS for neural, CPU for classical (measured) | Accepted |

Planned (docs/PLAN.md §12): 0008 baseline findings · 0009 feature set · 0010 direct vs recursive · 0011 UQ method · 0012 Toyota transfer · 0013 normalization · 0014 final model selection · 0015 deployment target & input contract.
