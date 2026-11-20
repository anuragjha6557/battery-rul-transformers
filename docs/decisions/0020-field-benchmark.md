# ADR-0020: Field-setting benchmark: SOH estimation, forecasting, RUL without SOH history (pre-registered)

- **Status:** Proposed (Stage 1 registered 2026-11-20, before any run)

## Stage 1: field SOH estimation screen
- **Design:**
  - Task F-A: SOH at cycle k from BMS-measurable inputs of cycles ≤ k (ADR-0018).
  - Models: iTransformer (MC, token-pooled readout), PatchTST (channel-mixing head), time-step Transformer, LSTM, LightGBM, ElasticNet, and the age-only baseline.
  - Tuned hyperparameters reused; lookback 64; 3 seeds; ADR-0018 cleaning.
  - NASA/CALCE leave-one-cell-out, Toyota official split (train stride 4).
- **Arms:** feature set `field` (scalars) vs `field_curve` (+15 Q(V) variates).
- **H1 (iTransformer paper, claim 1: many correlated variates):** going from `field` to `field_curve` helps iTransformer more than it helps PatchTST, LSTM, Transformer and LightGBM.
  - Measure: paired Δ RMSE (field_curve − field), per model, on Toyota test1/test2 (CI) and NASA/CALCE (k/4 cells).
- **H0 (sanity):** every learned model beats age-only on Toyota test1 (CI excludes 0).
- **Gate:** each model's feature set for Stage 2.

## Outcome
_Pending._
