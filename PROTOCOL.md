# Evaluation protocol

**Status:** v1.1, frozen before any model sweep (2026-11-15). v1.1 fills in the items v1.0 left to ADR-0005; no rule changed. Changes after this point need an ADR and a version bump, and must be called out in the results report.
**Decision record:** [ADR-0004](docs/decisions/0004-evaluation-protocol.md). EOL labelling is [ADR-0005](docs/decisions/0005-eol-definition.md); it was finalised from the Phase-2 data-quality report and its decisions are inlined below.

The source paper's numbers are not reproduced or trusted. This protocol is designed to remove the specific weaknesses identified in `docs/PLAN.md §1`:
- same-cycle features scored as "forecasting"
- RUL never actually evaluated
- scaler leakage
- metrics in normalised units
- n = 4 with no variance
- unequal tuning

---

## 1. Definitions

| Symbol | Meaning |
|---|---|
| `k` | `cycle_idx`: the equivalent full-cycle count of a cell (1-based) |
| `SOH_k` | `capacity_k / mean(capacity of the cell's first 5 cycles)`, computed in `data.schema.add_soh` |
| `θ` | EOL threshold on SOH. **Primary θ = 0.80** for every dataset; **sensitivity θ = 0.70** |
| `EOL` | Cycle at which the cell reaches θ under the labelling rule: `masked` + `sustained(n=5)`, first of 5 consecutive non-artifact cycles below θ; runs cut off by end of record count as censored (ADR-0005). Labels may use the full trajectory in hindsight; **inputs never may**. |
| `RUL_k` | `EOL − k` (cycles). Undefined (censored) if the cell never reaches θ |
| `T_p` | Prediction start ("now"). Everything at cycles ≤ T_p is observable; nothing after it is |

**Censoring:** a cell that never reaches θ has no RUL label at that θ. It is excluded from RUL metrics at that θ and listed in every table footnote. It still counts for Task A and Task B, whose targets are observed capacities. At θ = 0.70, NASA B0007 and B0018 are censored.

## 2. Tasks

Never mix tasks in one table. Every model declares which tasks it supports.

### Task A — SOH estimation (nowcasting)
- **Target:** `SOH_k`.
- **Allowed inputs:**
  - charge-phase features and curves of cycle `k`
  - any data of cycles `< k`
  - static cell metadata
- **Forbidden:** anything measured during discharge `k`. This covers `discharge_time_s`, `discharge_energy_wh`, `discharge_temp_max_c` and discharge curves; each is effectively a re-measurement of the target.
- **Why the task exists:** this is what the paper's "multi-channel" models actually measured. It is useful in deployment because a BMS sees the charge before it can measure capacity.
- **Metrics:** RMSE and MAE in **%SOH**, pooled over all cycles of the test cell(s).

### Task B — capacity-trajectory forecasting
- **Target:** `SOH_{T_p+h}` for h ∈ H.
  - H = {1, 10, 25, 50, 100} for NASA and CALCE.
  - H = {1, 10, 50, 100, 200} for Toyota.
- **Inputs:** anything at cycles ≤ T_p.
- **Forbidden:**
  - any measured quantity after T_p, including the future rest schedule
  - teacher forcing at evaluation
- **Two output modes** (each model declares which it supports):
  - *direct:* one forward pass emits every horizon
  - *recursive:* one-step model rolled forward on its own predictions; every exogenous channel is either forecast jointly or held at its last observed value (declared)
- **Metrics:** RMSE and MAE in %SOH per horizon, computed where the truth exists (horizons past the end of a trajectory are masked, never padded). Each is reported twice:
  - against raw SOH
  - against a centred 5-cycle median of SOH, because at multi-step horizons regeneration spikes are noise relative to the trend

### Task C — RUL
- **Target:** the `RUL_{T_p}` distribution (median plus quantiles).
- **Inputs:** same as Task B.
- **Two estimators** (each model declares which it supports):
  - *trajectory crossing:* first cycle at which the predicted SOH trajectory (median, plus each quantile trajectory for intervals) crosses θ, using the same rule as the labels (sustained, n=5, ADR-0005)
  - *direct head:* a model that regresses `RUL_{T_p}` and its quantiles directly
- If a predicted trajectory never crosses θ within the model's maximum horizon, the prediction is right-censored at that horizon. It is scored as `pred = T_p + H_max` with a censor flag, never silently dropped.

### Prediction start points (Tasks B, C)
Two families, both reported:
1. **Fixed-cycle starts.** The *deployable* setting, and the headline: the cycle count is known in the field, the eventual life is not.
   - The values are dataset-specific constants, each below the earliest EOL in that dataset at θ = 0.8: **NASA {30, 50}**, **CALCE {200, 400}**, **Toyota {100}** (ADR-0005).
   - They are chosen from the data-quality report *before* any model is run and fixed in `configs/task/*.yaml`.
2. **Fraction-of-life starts** λ ∈ {0.3, 0.5, 0.7}, with T_p = round(λ · EOL).
   - These are literature-comparable and match the α-λ metric.
   - Caveat, stated in every table that uses them: they leak the true life length into the protocol, since an earlier-dying cell is evaluated earlier. They are not deployable.

Only uncensored cells take fraction-of-life starts.

## 3. Splits

### NASA and CALCE: leave-one-cell-out (LOCO)
- **Outer loop:** each of the 4 cells is the test cell once; the paper's 3-fold CV is dropped. The other 3 cells train.
- **Inner loop (cross-fitted):** each training cell is held out once, which yields 3 sub-models. Each sub-model early-stops on its held-out cell.
  - Point prediction: the mean of the 3 sub-models (quantiles averaged per level).
  - Conformal calibration (§5) pools the 3 held-out conformity-score sets into one correction per horizon. This is **pooled split conformal**, inspired by CV+ (Barber et al. 2021) but *not* the exact CV+ jackknife: the test prediction averages the sub-models, so the CV+ 1−2α bound does not formally transfer. The finite-sample 1−α guarantee requires exchangeability of pooled and test scores, which holds only approximately (origins within a cell are autocorrelated; the effective calibration size is ~3 cells). **Empirical PICP on held-out cells is therefore the evidence of calibration.**
  - This costs 3× training. In exchange, no data is sacrificed for validation, and an honest calibration set exists even at n = 4.
- **NASA shared-rig caveat.** B0005, B0006 and B0007 were cycled on one rig with identical timestamps and rest schedule, so their regeneration events co-occur at the same `cycle_idx`. Consequences:
  - B0018 is the **only rig-independent NASA test cell**. Every NASA table reports the B0018 fold separately ("independent fold") next to the 4-fold LOCO mean.
  - Absolute `cycle_idx` is **not a model input** for NASA, CALCE or Toyota. Otherwise a model could learn "rig-mates jump at cycle 48". Models see age only through quantities a deployed system also has (window position relative to T_p, cumulative throughput). `tests/test_leakage.py` asserts this. An ablation that adds absolute `cycle_idx` quantifies what memorisation would have bought.
- **CALCE.** No shared-rig caveat: long rests coincide only at start-up (cycles 2–4, 54) and cross-cell ΔSOH correlation is ρ ∈ [−0.08, 0.12] (vs 0.55–0.69 for NASA rig-mates). All four CALCE folds count as independent (ADR-0005).

### Toyota/MIT/Stanford (Severson 2019)
- The **official split** is primary, for literature comparability: train (41 cells), primary test (43), secondary test (batch 3, 40), using the published cleaning.
- **5-fold GroupKFold by cell** over train ∪ primary test gives CIs.
- **Hyperparameters for every tuned model** are selected on Toyota train only, by inner 5-fold grouped CV (§6).

### Transfer (Toyota → NASA/CALCE)
Four conditions, all evaluated on the NASA/CALCE LOCO test cells:
1. *scratch:* LOCO-trained only
2. *zero-shot:* Toyota-trained, no NASA/CALCE data
3. *fine-tune:* Toyota-pretrained, then fine-tuned on the 3 LOCO training cells; head-only and full variants
4. *few-shot:* condition 3 plus fine-tuning on the test cell's own cycles ≤ T_p (legal, since they are before T_p)

## 4. Leakage rules (each is a test in `tests/test_leakage.py`)
1. **Train-only scalers.** Every scaler, imputer, PCA or feature selector is fit on training cells only, inside each fold. Test: perturb test-cell values and assert that every fitted statistic is unchanged.
2. **No future inputs.** A sample with origin T_p only reads rows with `cycle_idx ≤ T_p`. Test: corrupting all rows > T_p does not change the sample's inputs.
3. **Same-cycle discharge exclusion (Task A).** Discharge-phase quantities of cycle k never enter features of sample k. Test: corrupting discharge-k columns does not change Task-A features.
4. **No absolute cycle index** in model inputs (§3). Test on the feature builder's column list.
5. **Hindsight only in labels.** Label functions may read the full trajectory, but feature functions may not. The two are separate modules (`tasks/` vs `features/`), and features never import labels.
6. **Hyperparameters are never selected on a test cell.** Toyota tuning plus inner early stopping only; the runner refuses a config whose provenance lacks a tuning run ID.
7. **Calibration data is disjoint from test data.** Calibration scores come from inner held-out cells only (enforced: `uq.conformal` raises if a test cell appears in the calibration data).

## 5. Uncertainty
- Every Task-B/C entry reports a 90 % interval.
- **Primary method:** conformalised quantile regression (Romano et al. 2019) with pooled inner-fold scores (§3; guarantee stated there).
- **Secondary method:** 5-seed deep ensemble.
- **Reference method:** GPR, which is natively probabilistic.
- **Metrics:**
  - PICP, the empirical coverage, against a target of 0.90 ± 0.05
  - MPIW, the mean interval width
  - pinball loss at q ∈ {0.05, 0.25, 0.5, 0.75, 0.95}
  - CRPS, the sample-based estimator validated against `properscoring`
  - a reliability diagram per dataset

## 6. Tuning budget (equal for every model, ADR-0006)
- Optuna TPE sampler with a Hyperband pruner.
- **Trials:** 50 per (model, task) on Toyota train with inner grouped 5-fold CV.
- **Learning rate:** log-uniform in [1e-5, 1e-2] (widened from [1e-4, 1e-2] by ADR-0006 amendment 1). Other search spaces are declared per model in `configs/model/*.yaml` before the sweep.
- **Model size:** capped by a shared parameter budget (≤ 250 k parameters for NASA/CALCE-transferred configs).
- **Early stopping:** the same rule for every model (patience 20 epochs on inner-validation loss, at most 300 epochs).
- **Untuned models:** those with no free hyperparameters (persistence, parametric fits, GPR with marginal-likelihood kernel fitting) are reported as-is.

## 7. Metrics: exact definitions
- **%SOH errors:** `RMSE = sqrt(mean((ŝ − s)²)) × 100` and `MAE = mean(|ŝ − s|) × 100`, with s and ŝ as SOH fractions.
- **RUL error:** `e = RUL_pred − RUL_true` (cycles). **Positive = late = optimistic**, the dangerous direction. Reported values:
  - MAE (cycles)
  - mean signed error (bias)
  - relative error `|e| / RUL_true`
- **α-λ accuracy** (Saxena et al. 2008), α = 0.2: at fraction-of-life start λ, a prediction is accurate if `|e| ≤ α · RUL_true`. The reported value is the fraction of (cell, seed) predictions that are accurate, for λ ∈ {0.3, 0.5, 0.7}.
- **Prognostic horizon:** the earliest T_p from which all later predictions stay within the α-bounds.
- **Units:** every error is in physical units (%SOH, Ah, cycles). Normalised-unit metrics are not reported.

## 8. Statistics and reporting
- **Seeds and run IDs:** 5 seeds per configuration. Every number in every table carries an MLflow run ID (or a run-group ID).
- **Per-cell reporting:** values are reported per cell, then aggregated.
- **NASA/CALCE aggregate:**
  - mean over (cell × seed)
  - 95 % cluster-bootstrap CI over cells, 10 000 resamples, labelled "n = 4 cells, wide by construction"
  - paired comparisons against the best baseline, reported as "direction consistent in k/4 cells (and k/20 cell-seeds)". No p-values at n = 4.
- **Toyota aggregate:** mean ± 95 % bootstrap CI over test cells, and a paired Wilcoxon signed-rank test vs the best baseline (Holm-corrected across the model ladder).
- **Cross-dataset summary:** the mean rank of each model across (dataset × task × primary metric) (Demšar 2006).
- **Headline metrics, fixed now:**
  - **Task B:** RMSE at H = 50, in %SOH
  - **Task C:** RUL MAE at the first fixed-cycle start, plus α-λ accuracy at λ = 0.5
  - **Calibration:** PICP of the 90 % interval
- **Negative results:** reported in the same tables. Nothing is dropped because it looks bad.

## 9. Deviations log
Any deviation from this protocol is appended here with the date, the reason and the affected tables.

| Date | Section | Deviation | Reason | Tables affected |
|---|---|---|---|---|
| 2026-11-15 (before any sweep) | §1 EOL, §2 Task C | Toyota EOL label = provider `cycle_life` (0.88 Ah = 80 % nominal); θ = 0.70 sensitivity N/A for Toyota | Our sustained rule censors 81/124 cells because tests stopped at EOL by design; where it resolves it matches the provider within 2 cycles (ADR-0005 amendment 1) | all Toyota RUL tables |
| 2026-11-15 (before any sweep) | §6 | lr range [1e-4, 1e-2] → [1e-5, 1e-2] for all neural models; Hyperband min_resource = 20 epochs | Boundary-hit rule fired on the first study (NLinear best lr within 3 % of the lower bound); 88 % early pruning (ADR-0006 amendment 1) | all tuned-model tables |
| 2026-11-16 (mid-sweep, before any benchmark run) | §6 | weight_decay range [1e-6, 1e-2] → [1e-8, 1e-2] for all neural models; neural studies re-run | Boundary-hit rule fired for iTransformer, Transformer, GRU (best ≈ 1.27e-6) (ADR-0006 amendment 2) | all tuned neural-model tables |
| 2026-11-16 (before any benchmark run) | §3, §4.7, §5 | 'CV+' wording replaced by 'pooled split conformal' with its actual (approximate) guarantee | Correction of an over-claim found during implementation; procedure unchanged | calibration tables |
| 2026-11-16 (mid-sweep, before any benchmark run) | §6 | lr upper bound 1e-2 → 3e-2 for all neural models; neural forecast studies re-run; no further range changes before the benchmark | Boundary-hit rule: LSTM best lr at 0.976 of the log range (ADR-0006 amendment 3) | all tuned neural-model tables |
