# ADR-0008: Benchmark findings (Phase 4/5: tuned baselines, iTransformer, PatchTST)

- **Status:** Accepted (results); 2026-11-16
- **Evidence:**
  - MLflow experiments `benchmark` (1 620 runs, parent `1a8befe9e131484aba332450d5206637`) and `benchmark_local` (72 runs); `tuning` (33 studies).
  - Tables: `reports/tables/benchmark{,_local}.{md,csv}`, `benchmark_calibration.csv`, `benchmark_ranks.csv`. Every number below comes from those files.
- **Protocol:** PROTOCOL.md v1.1 plus the logged deviations. Toyota training windows were thinned to every 4th origin (owner decision, option B). NASA and CALCE ran in full. 5 seeds per configuration. Local extrapolators ran 1 seed at start points only.

## Context
This is the first leakage-free, equal-budget comparison of the full model ladder on all three datasets. The source paper claimed a 44.6 % / 29 % RMSE gain for iTransformer over LSTM and the vanilla Transformer on NASA and CALCE. Those numbers were not reproduced and are not trusted; this ADR records what the honest protocol shows instead.

## Findings

### 1. Overall standing: mean rank across 40 (dataset × task × headline metric) conditions
| Rank | Model | Mean rank |
|---|---|---|
| 1 | iTransformer (MC) | 3.08 |
| 2 | iTransformer (SC) | 3.95 |
| 3 | LightGBM | 4.55 |
| 4 | PatchTST | 4.65 |
| 5 | NLinear | 6.15 |
| 6 | LSTM | 6.48 |
| 7 | RLinear | 7.18 |
| 8 | ElasticNet | 7.35 |
| 9 | GRU | 7.73 |
| 10 | DLinear | 9.03 |
| 11 | Transformer | 9.28 |

Level-0 baselines rank last where they apply. **iTransformer is the best model overall, but not uniformly.**

### 2. The answer depends on the dataset (the central finding)
- **Toyota** (in-distribution for tuning; 43 + 40 untouched test cells; real statistics):
  - **Forecast h=50, all origins.** iTransformer is 1st on test1 (0.40 %SOH [0.32, 0.51]); the two iTransformer variants and PatchTST are 1st to 3rd on test2 (0.18–0.20). Every learned model beats persistence (Holm-corrected Wilcoxon p ≈ 1e-8 to 1e-12) except GRU on test2.
  - **SOH estimation.** PatchTST and both iTransformers lead (0.11 %SOH on test1, statistically tied); test2 is easy for every model (0.014–0.05).
  - **RUL from cycle 100.** LightGBM ≈ LSTM on test1 (MAE ≈ 102 cycles); ElasticNet ≈ iTransformer-SC ≈ iTransformer on test2 (264–284). For α-λ accuracy at λ = 0.5, LightGBM leads test1 (0.74) and iTransformer-SC leads test2 (0.84).
- **NASA / CALCE** (LOCO, 4 cells; hyperparameters chosen on Toyota; CIs wide by construction):
  - **Forecast h=50, all origins.** LightGBM is 1st on both (CALCE 2.84, NASA 3.24 %SOH); iTransformer is mid-pack (CALCE 4th, NASA 8th).
  - **SOH estimation.** ElasticNet wins CALCE (0.66 vs ≥ 1.19 for every other model); the iTransformers win NASA (0.70).
  - **RUL.** The Transformer leads CALCE at cycle 200 (68 cycles); iTransformer leads NASA at cycle 30 (16 cycles).
- **Interpretation:**
  - Inverted attention is the strongest architecture **in-distribution** (same chemistry and protocol as tuning).
  - Its advantage does **not transfer** to other chemistries trained on 3 cells, where a well-regularised GBM or a linear model is as good or better.
  - This is the defensible form of the paper's claim, and it directly motivates the transfer experiment (ADR-0012).

### 3. Naive baselines: what the paper's metrics hid
- **Persistence** (SOH_{k+h} = SOH_k) is beaten clearly over a cell's whole life: Toyota 2.50 vs 0.40, NASA 11.2 vs 3.2, CALCE 6.3 vs 2.8 %SOH at h=50.
- **At the CALCE fixed start points, nothing beats persistence:** best 1.49 vs persistence 1.51. Early-life fade there is too flat to forecast.
- **At Toyota's cycle-100 start on test1**, every model is statistically tied with the last-slope baseline (0.06–0.14 %SOH).
- A one-step or early-life metric alone, as used by the paper, cannot separate models. This is why PROTOCOL v1.1 reports multi-horizon, all-origin results.

### 4. Level-stripping normalisation fails at RUL
- RLinear (RevIN) and PatchTST normalise each window by its own location and scale, discarding the absolute SOH level.
- RUL depends on the distance from that level to the EOL threshold, so they are worst at RUL on every dataset: Toyota test1 MAE 602 and 460 cycles, α-λ accuracy 0.00 and 0.26.
- They are among the best at SOH estimation and forecasting.
- iTransformer feeds location and log-scale back into its tokens (a documented deviation), which keeps it competitive at RUL.

### 5. Multi-channel vs single-channel iTransformer
- MC and SC are statistically tied on most conditions: Toyota SOH 0.111 vs 0.111; NASA SOH 0.703 vs 0.699.
- MC is better on Toyota test1 forecasting (0.40 vs 0.53); SC is better on Toyota test2 forecasting and RUL.
- The paper's "multi-channel" premise is **not** confirmed as a general gain. The channel-mixing benefit is dataset-specific.

### 6. Uncertainty calibration (pooled split-conformal CQR, α = 0.1)
- **Forecast h=50 coverage (PICP), all origins:**
  - Calibrated intervals cover 0.89–0.94 on CALCE/NASA and 0.88–0.96 on Toyota, against a 0.90 target.
  - Raw quantiles under-covered: down to 0.46 for iTransformer on NASA and 0.80 for LightGBM on CALCE.
  - Under-covering models get wider intervals (NASA iTransformer MPIW 5.2 → 21.2 %SOH); over-covering ones get narrower (Toyota Transformer 2.96 → 2.37).
- **Best interval score:** iTransformer on Toyota (1.68), iTransformer-SC on CALCE (14.3), PatchTST on NASA (17.6).
- **RUL coverage rose from 0.57–0.72 raw to 0.84–0.87 calibrated**, still short of 0.90 ± 0.05. The likely cause is the small, autocorrelated calibration set (PROTOCOL §3 caveat). This is reported as a limitation, not hidden.

### 7. Classical prognostics baselines
- Parametric fits (linear, double-exponential, power) and GPR are uncompetitive for RUL.
- Their extrapolations frequently plateau and never cross the threshold, so they are scored at the censoring cap (Toyota RUL MAE 1 300 to 3 500 cycles).
- On short-horizon forecasting they are mid-table.
- An unbounded double-exponential fit produced absurd NASA forecasts. It was fixed by clipping to the physical SOH range and re-run.

### 8. Severson reproduction (Toyota, official split, `reports/tables/severson_repro.md`)
- The variance model reproduces the published result (14.8 % / 11.4 % mean error on test1 / test2).
- The full model degrades on test2 (26.8 %). The likely cause is the temperature-integral proxy (Tmax), since cell temperature is not available in the processed tables.

## Limitations (reported, not fixed)
- **Tuning noise.** About 10 of 50 trials survive Hyperband per study, and tuned values moved by up to 0.08 %SOH between passes (iTransformer forecast 0.38 to 0.46). Rankings are claimed from the 5-seed benchmark only.
- **Remaining boundary hits after the stopping rule (ADR-0006 amendment 3), not re-swept:**
  - RLinear SOH lr near the 3e-2 cap; DLinear forecast lr near the 1e-5 floor.
  - LightGBM `num_leaves` and `min_child_samples` high (SOH) and learning rate low (RUL).
  - Transformer SOH weight decay and dropout high.
  - GRU/LSTM depth at its maximum of 2.
- **Toyota training windows thinned to stride 4.** Validation and test windows were never thinned.
- **NASA/CALCE statistics rest on 4 cells:** CIs are wide, and NASA B0018 is the only rig-independent test cell (reported separately in the tables).
- **Hyperparameters were chosen on Toyota only.** NASA/CALCE results therefore include a chemistry-transfer penalty for every tuned model. This is by design (ADR-0004) and is the same for all models.

## Decision
1. **iTransformer (MC) is the base of iTransformer-v2.** It has the best overall rank and the best in-distribution forecasting. LightGBM is kept as the strong tabular reference in every table.
2. **Phase 6 improvements are judged mainly on the cross-chemistry gap:** Toyota transfer (ADR-0012), curve features (ADR-0009) and normalisation/loss (ADR-0013). That gap is where iTransformer currently loses.
3. **CQR calibration is applied to every reported interval.** Raw quantile intervals are reported only as the "before" column.
4. **The README headline will state, in this order:**
   - the dataset-dependent ranking;
   - the persistence/start-point finding;
   - calibrated coverage.

   It will not state a single "% better than LSTM" number.
