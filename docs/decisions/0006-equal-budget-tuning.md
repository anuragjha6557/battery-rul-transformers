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

## Amendment 1 (2026-11-15, before the real sweep): wider learning-rate range, gentler pruning
**Trigger.** The boundary-hit check fired on the first real study: NLinear's best lr was 1.15e-4, within 3 % of the lower bound (1e-4) in log space. The same study pruned 88 % of trials on early-epoch validation loss.

**Decision.**
- The lr search range for **every** neural model becomes log-uniform **[1e-5, 1e-2]**, applied to all model configs at once as this ADR requires. The range changes for all models, never for one.
- Hyperband uses `min_resource=20` epochs (the early-stopping patience), so no trial is pruned before early stopping could have acted.
- All studies are re-run from scratch under the new space. The stored search-space hash makes a mixed resume impossible.

**Budget check.** Measured study cost on Toyota: about 22 s for 50 ElasticNet trials and about 52 s for 50 NLinear trials with 4 workers. Tuning all models on all three tasks is therefore affordable, so no task-scoping deviation is needed.

**Clarification (2026-11-15, during the sweep).** The boundary-hit rule applies to *open-ended* scales a search range truncates: learning rate, regularisation strengths, tree counts, widths. It does **not** apply to parameters whose range is their full natural domain:
- `l1_ratio ∈ [0, 1]`
- `dropout ≥ 0`
- `subsample` and `colsample_bytree ≤ 1`

A hit there is a finding, not a truncation. The first instance was ElasticNet forecast, best `l1_ratio = 0.98`, i.e. near-pure lasso; it is reported but triggers no re-sweep.

## Amendment 2 (2026-11-16, mid-sweep): wider weight-decay range
**Trigger.** In the first pass of the forecast studies (under amendment 1), the boundary-hit check fired on `weight_decay` at its lower bound (1e-6) for iTransformer, the time-step Transformer and GRU. Their best values were ≈ 1.27e-6, within 2.6 % of the bound in log space.

**Decision.**
- The weight-decay range for **every** neural model becomes log-uniform **[1e-8, 1e-2]**.
- All neural forecast studies are re-run from scratch. The pre-widening Optuna journal is archived at `optuna/archive/journal_pre_wd_widening.log` for the record.
- ElasticNet and LightGBM are unaffected (they have no weight-decay parameter) and keep their completed studies.

**Not triggered:**
- `n_layers = 1` (PatchTST) and `layers = 1` (GRU) are at the smallest meaningful architecture, the natural lower bound of a depth parameter, so per the clarification above they are reported but don't widen anything.
- The first-pass results (best h=50 RMSE: iTransformer 0.393, GRU 0.421, LightGBM 0.440, iTransformer-SC 0.467, PatchTST 0.481, Transformer 0.545, RLinear 0.678, DLinear 0.742, NLinear 0.746 %SOH) are kept here only as a record. The benchmark uses the re-tuned values.

**Clarification 2 (2026-11-16): depth is bounded by the parameter budget.** For the attention models, `n_layers ≤ 3` is not an arbitrary truncation. The shared ≤ 250 k parameter cap (PROTOCOL §6) already forces the FFN width to shrink at d_model = 128, n_layers = 3, so adding layers only trades width for depth inside the same budget. A best `n_layers = 3` is therefore a budget-bound result: it is reported, and it does not trigger widening. The budget, not the range, is the binding constraint, and it is the same for every model.

**Observed tuning noise (for ADR-0008).** iTransformer forecast scored 0.393 %SOH in the first pass (narrower weight-decay range) and 0.460 in the second (wider range, a superset). With about 10 of 50 trials surviving Hyperband, the tuning outcome varies by an amount comparable to between-model gaps. Two rules follow:
1. Model rankings are only claimed from the 5-seed benchmark with CIs, never from tuning values.
2. Any extra tuning budget is applied to all models equally.

**Clarification 3 (2026-11-16): a weight-decay hit at 1e-8 means "no decay".** After amendment 2, GRU forecast again chose weight_decay at the lower bound: 1.27e-8, at exactly the same log-fraction (0.0259) as the earlier 1.27e-6 hit. That identical fraction means it is the same seeded TPE startup point at the same quantile of a shifted range, not a trend toward ever-smaller values. Decay of 1e-8 is functionally zero for Adam at these learning rates, so 1e-8 is treated as the natural lower bound (no regularisation), and a hit there is reported without widening. No further widening is made for weight decay.
