# ADR-0017: CALCE CV-skip cycles as invalid measurements (pre-registered)

- **Status:** Proposed (registered 2026-11-17, before any run)

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
_Pending._
