# ADR-0006: Equal tuning budget for every model, selected on Toyota

- **Status:** Accepted
- **Date:** 2026-11-15

## Context
The paper tuned iTransformer over a 96-point grid. It did not report the baselines' search spaces, and it used a learning-rate grid up to 0.5 for Adam, a regime where a time-token Transformer is known to diverge. "Model X beats Y" is only meaningful if X and Y get the same search effort under the same selection rule.

## Options considered
1. **Per-model grids** (as in the paper). Budgets differ implicitly, which invites the "under-tuned baseline" critique.
2. **Fixed defaults for every model.** Fair, but leaves performance on the table and penalises the models most sensitive to hyperparameters.
3. **Equal-budget Bayesian search.**
   - The same number of Optuna trials for each model.
   - The same sampler and pruner, data split, early-stopping rule and seeds.
   - A shared learning-rate range and a shared parameter-count cap.

## Decision
Option 3, as specified in `PROTOCOL.md §6`:
- 50 TPE trials per (model, task) with Hyperband pruning
- inner grouped 5-fold CV on Toyota train
- LR log-uniform in [1e-4, 1e-2]
- ≤ 250 k parameters
- patience 20, at most 300 epochs

Each model's search space is committed in `configs/model/<name>.yaml` before its sweep starts; the commit timestamp is the evidence. Models without free hyperparameters are not tuned.

## Consequences
- Every results table can state "equal budget: 50 trials each".
- A model whose best trial sits on a search-space boundary gets flagged in the report (boundary-hit check in `train/tune.py`). In that case the space is widened for **all** models, not just that one.
- Toyota-chosen configs may be sub-optimal for NASA/CALCE. That is the accepted price of not selecting on 4 cells, and the nested-LOCO sanity check (`PROTOCOL.md §3`) shows how large it is.
