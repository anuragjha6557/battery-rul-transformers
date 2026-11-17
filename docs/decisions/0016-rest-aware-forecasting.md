# ADR-0016: Forecasting capacity regeneration with the planned rest schedule (pre-registered)

- **Status:** Proposed (registered 2026-11-17, before any run)

## Context
The source paper's motivation for attention models was capturing **capacity regeneration**: the temporary capacity recovery after a cell rests. Measured on the benchmark (`reports/tables/…`, analysis in this ADR's Outcome):

| Dataset | Regeneration | Size |
|---|---|---|
| NASA | Real: 20 events after rests over 6 h | **+3.1 % SOH** mean jump |
| CALCE | Mostly artifact: 109 cycles where the CV charge step was skipped | −10.6 % dips (ADR-0017). Rest recovery is only +0.8 % |
| Toyota | None (no long rests) | – |

- **The benchmark forecasters cannot predict a future regeneration.** At h = 1, every model misses NASA regeneration targets by about −3.3 % SOH, the same as persistence.
- **The reason is missing information, not architecture.** The rest that causes the jump happens *after* the forecast origin, so it is not in the inputs.
- **SOH estimation (Task A) does see the rest before the current cycle.** There, iTransformer SC/MC capture about 55–60 % of each jump (bias −1.4 / −1.8 % vs −3.3 %), which is the best of all models.

## Hypothesis
Giving forecasters the **planned rest schedule** of the forecast window as known-future covariates lets them forecast regeneration:
- **Covariates:** for each horizon h, `log1p(rest before cycle T_p+h)` and `log1p(total rest over T_p+1…T_p+h)`. Rests are scheduled by the operator or test plan; this is the TFT-style "known future inputs" setting.
- **H1:** on NASA, h = 1 RMSE at regeneration targets falls by ≥ 50 % for iTransformer, and overall h = 10 RMSE improves (CI excludes 0, direction consistent on ≥ 3/4 cells).
- **H2 (the paper's thesis, tested honestly):** attention models gain more from the covariates than LightGBM and LSTM.

## Design
- **Task variant:** "B | schedule". It is reported separately and never mixed with unconditional Task B, because it uses exogenous future information.
- **Leakage rule:** only `rest_before_s` of future cycles is read. Enforced by `test_future_rest_reads_only_the_future_rest_schedule`.
- **Runs:** experiment `abl_future_rest` covers itransformer, itransformer_sc, lgbm, lstm, transformer and elasticnet (the models that consume tabular inputs). Tuned parameters are unchanged; NASA and CALCE LOCO; 5 seeds.
- **Comparison:** paired against the same model in `benchmark`.
- **Metrics:** RMSE at h = 1/10/50, plus RMSE and bias on regeneration target cycles.
- **Deployment:** adopted for the demo only if H1 holds. The demo would then need a planned-rest input.

## Outcome
_Pending._
