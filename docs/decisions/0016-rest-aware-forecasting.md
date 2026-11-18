# ADR-0016: Forecasting capacity regeneration with the planned rest schedule (pre-registered)

- **Status:** Accepted: reported as a conditional task variant; H1 and H2 rejected (registered 2026-11-17; outcome 2026-11-17)

## Context
The source paper's motivation for attention models was capturing **capacity regeneration**: the temporary capacity recovery after a cell rests. Measured on the benchmark (`reports/tables/…`, analysis in this ADR's Outcome):

| Dataset | Regeneration | Size |
|---|---|---|
| NASA | Real: 20 events after rests over 6 h | **+3.1 % SOH** mean jump |
| CALCE | Mostly artifact: 109 cycles where the CV charge step was skipped | −10.6 % dips (ADR-0017). Rest recovery is only +0.8 % |
| Toyota | None (no long rests) | – |

- **The benchmark forecasters cannot predict a future regeneration.** At h = 1, every model misses NASA regeneration targets by about −3.3 % SOH, the same as persistence.
- **The reason is missing information, not architecture.** The rest that causes the jump happens *after* the forecast origin, so it is not in the inputs.
- **SOH estimation (Task A) does see the rest before the current cycle.** Pooled over 5 seeds, iTransformer SC/MC are the most accurate models at regeneration cycles: RMSE 1.87 / 2.18 %SOH vs ≥ 3.17 for every other model, with bias −1.20 / −1.52 vs −3.29 for previous-SOH. LSTM has a smaller bias (−0.61) but a much larger spread (RMSE 3.28). Source: `scripts/showcase/regen.py`.

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
- **Evidence:**
  - MLflow `abl_future_rest`: 240 runs, 0 failures.
  - `reports/tables/abl_future_rest_paired.{md,csv}`: paired against `benchmark`, Δ in %SOH.
  - `reports/tables/abl_future_rest_events.csv`: error at regeneration targets, i.e. cycles after a rest of more than 6 h; 5 seeds pooled.

### Regeneration targets, NASA (bias / RMSE in %SOH; the benchmark arm has no schedule)
| Model | h = 1 bias: benchmark → rest-aware | h = 1 RMSE reduction | h = 10 RMSE reduction |
|---|---|---|---|
| Transformer (time-step) | −4.83 → −1.66 | **42 %** | 29 % |
| LSTM | −2.51 → −0.75 | 26 % | 28 % |
| ElasticNet | −3.20 → −2.45 | 17 % | 26 % |
| LightGBM | −3.62 → −2.96 | 15 % | **33 %** |
| iTransformer (MC) | −3.59 → −3.15 | 10 % | 9 % |
| iTransformer (SC) | −3.60 → −3.46 | 4 % | 7 % |

### Overall (paired, all origins)
- **NASA h = 10:** every model improves, with 3–4 of 4 cells better. Δ ranges from −0.08 (iTransformer SC) to −1.12 (Transformer); iTransformer −0.23, LightGBM −0.36.
- **NASA h = 1:** improves for 5 of 6 models on 4/4 cells.
- **CALCE h = 50:** every model improves, by −0.13 to −0.40, mostly on 4/4 cells.
- **CALCE h = 1:** slightly worse for LightGBM (+0.09) and iTransformer (+0.04). Rests there are frequent and only weakly linked to recovery (+0.8 %).

### Verdicts
- **H1 is rejected.** iTransformer's regeneration error falls by only 10 % (h = 1) and 9 % (h = 10), far below the pre-registered 50 %.
- **H2 is rejected, in the opposite direction.** Inverted attention gains the *least* from the schedule. LSTM, the time-step Transformer and LightGBM gain 2–4× more.
  - A plausible mechanism: those models feed the covariates straight into the output head.
  - iTransformer embeds the tabular vector as one extra token among variate tokens, then pools. Its hyperparameters were also tuned without these inputs.
  - Feeding each horizon's covariates to its own head is future work.
- **What the data support:**
  - Regeneration is forecastable only when the rest schedule is known. With it, a recurrent model captures about 70 % of the NASA jump one cycle ahead.
  - The source paper's claim that inverted attention captures regeneration is not supported for *forecasting*.
  - It is partly supported for *estimation* (Task A, where the current rest is observed). There, iTransformer has the lowest RMSE at regeneration cycles.

## Decision
- **Rest-aware forecasting is reported as a conditional task variant (B | schedule).** It is never mixed with unconditional results.
- **The deployed model is unchanged,** because it takes capacity-only input and has no schedule.
- **The dashboard shows the rest-aware benchmark variants** (held-out predictions) next to the standard ones on the NASA and CALCE demo cells, so visitors can see regeneration being anticipated.

