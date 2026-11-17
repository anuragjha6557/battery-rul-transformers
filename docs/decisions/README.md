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
| [0008](0008-baseline-findings.md) | Benchmark findings: dataset-dependent ranking, calibration, limitations | Accepted |
| [0009](0009-curve-features.md) | Curve features ablation (ICA, ΔQ(V)) | Accepted: mc_curve not adopted |
| [0010](0010-direct-vs-recursive.md) | Direct multi-horizon vs recursive rollout | Accepted: direct wins at h ≥ 25 |
| [0011](0011-uq-method.md) | Uncertainty: CQR vs deep ensemble vs GPR | Accepted: CQR primary |
| [0012](0012-toyota-transfer.md) | Toyota (LFP) pre-training → NASA/CALCE transfer | Accepted: not default (NASA-only gain) |
| [0013](0013-normalisation-and-loss.md) | Instance normalisation; Huber vs MSE | Accepted: neither adopted |

Planned (docs/PLAN.md §12): 0014 final model selection · 0015 deployment target & input contract.
