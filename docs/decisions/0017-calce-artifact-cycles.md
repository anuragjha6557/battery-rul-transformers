# ADR-0017: CALCE CV-skip cycles as invalid measurements (pre-registered)

- **Status:** Accepted: not adopted as the default (forecast gain, RUL loss); artifact-free scoring added (registered 2026-11-17; outcome 2026-11-17)

## Context
- **What the dips are:** in 109 CALCE cycles (≈ 3 %), the charger's constant-voltage step ended after one sample (`cv_time_s < 300 s`). The following discharge delivers about 10.6 % less capacity, and the cell returns to trend on the next cycle (ADR-0005, data-quality report).
- **Current handling:**
  - These cycles are masked when building EOL labels.
  - The causal flag `skipped_cv` is a model input.
  - They are otherwise kept as data, so they appear in the SOH history and in the forecast targets.
- **Effect on forecasting:** no forecaster can predict them (h = 1 error ≈ +10.6 % for every model). They inflate CALCE RMSE and add spikes to every input window.

## Hypothesis
Treating these cycles as invalid measurements, i.e. dropping them before windowing from both inputs and targets, improves CALCE forecasting and RUL:
- Forecast h = 50 RMSE on artifact-free targets.
- RUL MAE at the fixed starts.

Both must improve for most models, with direction consistency on ≥ 3/4 cells.

## Design
- **Runs:** experiment `abl_calce_clean` (`drop_skipped_cv: [calce]`) covers persistence, itransformer, itransformer_sc, lgbm, lstm, nlinear and elasticnet. Tasks: forecast and RUL. 5 seeds; tuned parameters unchanged.
- **Fair comparison:** the benchmark arm is re-scored on the same artifact-free target cycles. Its predictions at dip targets are excluded post hoc, so both arms are judged on identical targets.
- **Causality:** dropping is causal at prediction time, because the flag uses the cycle's own charge (`cv_time_s`), known before its discharge. A user with capacity-only data cannot detect dips; the demo documents this.

## Outcome
- **Evidence:**
  - MLflow `abl_calce_clean`: 260 runs, 0 failures.
  - `reports/tables/abl_calce_clean_paired.csv`: both arms re-scored on identical artifact-free origins and targets; cluster-bootstrap CI over 4 cells × 5 seeds.

| Model | h = 50 RMSE: benchmark → clean (Δ [95 % CI], cells better) | RUL MAE at start points: benchmark → clean (cells better) |
|---|---|---|
| iTransformer (MC) | 2.48 → 2.28 (−0.21 [−0.33, −0.09], 4/4) | 76.6 → 79.7 (2/4) |
| iTransformer (SC) | 2.43 → 2.14 (−0.29 [−0.38, −0.20], 4/4) | 73.0 → 81.8 (0/4) |
| LightGBM | 2.05 → 1.98 (−0.07 [−0.14, +0.04], 3/4) | 82.1 → 85.3 (1/4) |
| LSTM | 2.47 → 2.34 (−0.13, 4/4) | 80.1 → 85.0 (0/4) |
| NLinear | 3.58 → 3.36 (−0.22, 4/4) | 104.0 → 98.4 (3/4) |
| ElasticNet | 3.44 → 3.38 (−0.06, 2/4) | 136.2 → 139.4 (1/4) |

- **Forecasting:** h = 10 also improves on 4/4 cells for every learned model.
- **Scoring effect alone:** re-scoring on artifact-free targets lowers every model's CALCE error by about 0.6 %SOH. iTransformer h = 50 goes from 3.13 (raw targets) to 2.48 before any cleaning.

### Verdict
- **The hypothesis is rejected as pre-registered,** because it required both forecasting and RUL to improve.
  - Forecasting improves consistently.
  - RUL gets slightly worse for most models (+3 to +9 cycles). The CIs exclude 0 only for iTransformer SC and LSTM.
- **A plausible mechanism:** the RUL label still comes from the sustained-crossing rule on the full record. Dips near the threshold are informative about how close a cell is to EOL, and removing them hides that signal.

## Decision
- **The benchmark keeps the raw data.**
- **CALCE forecast results are additionally reported on artifact-free targets.** That is the honest measure of ageing forecasts.
- **Artifact cycles are marked on the dashboard,** so visitors can tell a charger glitch from ageing or regeneration.

