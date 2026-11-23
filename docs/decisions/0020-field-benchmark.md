# ADR-0020: Field-setting benchmark: SOH estimation, forecasting, RUL without SOH history (pre-registered)

- **Status:** Accepted, all stages complete (2026-11-23). H1 (variates) chemistry-conditional; H2 (lookback) and H3 (regeneration token) not supported. Verdict in ADR-0021.

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

## Outcome: Stage 1 (2026-11-21, 378 runs, 0 failed)
Tables: `reports/tables/field_screen_{field,field_curve}.md`, paired: `reports/tables/field_screen_paired.md`.

**RMSE % SOH, `field` / `field_curve`** (3 seeds; lab reference with SOH history: CALCE 0.66, NASA 0.70, Toyota 0.11 / 0.02):

| Model | CALCE | NASA | Toyota test1 | Toyota test2 |
|---|---|---|---|---|
| age-only | 6.89 | 5.85 | 4.01 | 3.67 |
| iTransformer | 4.71 / **2.71** | 5.54 / 4.73 | 1.03 / 1.19 | **1.55** / 2.27 |
| PatchTST | 6.86 / 7.27 | 7.21 / 5.95 | 1.66 / 1.85 | 2.35 / 3.24 |
| Transformer | 3.02 / 3.07 | 9.70 / 7.54 | 0.93 / **0.91** | 2.58 / 2.03 |
| LSTM | 3.63 / **2.09** | 3.90 / 4.41 | 1.07 / 1.06 | 2.20 / 2.26 |
| LightGBM | 4.41 / 4.15 | 4.08 / 3.94 | 0.95 / 0.92 | 2.55 / 2.58 |
| ElasticNet | 4.59 / 3.60 | **3.24** / 5.42 | 1.18 / 1.18 | 4.16 / 11.90 |

**H1: partially supported, conditional on chemistry.**
- CALCE: iTransformer gains most of all models (Δ −2.00 [−2.53, −1.54], 4/4 cells, 12/12 cell-seeds); LSTM −1.54 (3/4); PatchTST (channel-independent) +0.40 (1/4).
- NASA: iTransformer −0.81 (3/4); Transformer −2.15 and PatchTST −1.25 are larger but with CIs spanning 0.
- Toyota: Q(V) variates hurt iTransformer (test1 +0.15, test2 +0.72, both CI > 0) and PatchTST (+0.20, +0.89); other models ±0.03 except Transformer test2 −0.56 and ElasticNet test2 +7.75.
- Reading: the many-variate advantage appears where the variates carry health information (NMC/LCO top-of-charge curves). On LFP the 3.50–3.58 V window lies on the flat plateau (EDA §3) and its shape shifts with the test2 protocol, so extra variates add mostly noise and shift.

**H0: supported.** Every learned model beats age-only on Toyota test1 in both arms (CI excludes 0; ≥ 41/43 cells). Not general: on NASA the Transformer and PatchTST do not beat age-only, and ElasticNet loses to it on Toyota test2 (protocol shift).

**Other findings.**
- iTransformer with `field` is the most robust model under the Toyota test2 protocol shift (1.55 vs 2.03–4.16).
- PatchTST is the weakest learned model on CALCE and Toyota test1 in both arms; on NASA the time-step Transformer is worse.
- The field-vs-lab gap remains 4–75×.

**Gate decision (feature set per dataset, same for every model; not per model, which would select on test results):**
- NASA, CALCE: `field_curve`. Toyota: `field`.
- No retune: no model failed to train; the age-only gaps are as large as the probe suggested.

**Operational note.** PatchTST folds channels into the batch; on Toyota with 20–35 channels, three parallel workers exhausted memory (swap thrash). Fixed by chunked validation/prediction forward passes (numerically identical) and running the remaining units with one worker. Stage 2 runs PatchTST sequentially.

## Stage 2: long-lookback test (registered 2026-11-21, before any run)
- **Design:**
  - Tasks F-A (SOH at k) and F-B (direct multi-horizon forecast; headline h = 50).
  - Lookback L ∈ {32, 128, 512}; every other parameter is the tuned value (ADR-0006).
  - Models: iTransformer (MC), time-step Transformer, PatchTST, LSTM. Shorter histories are left-padded and masked, so every L is scored on the same samples (paired).
  - CALCE (LOCO, `field_curve`) and Toyota (official split, `field`), per the Stage 1 gate. NASA is excluded: cells of 132–168 cycles.
  - 3 seeds; 360 runs; experiment `field_lookback`. PatchTST runs with one worker (memory, Stage 1 note).
- **Parameter cap (250k):**
  - iTransformer and PatchTST stay under it at every L (iTransformer shrinks its feed-forward width; it now raises instead of exceeding).
  - The time-step Transformer on F-B reaches 274–276k at L = 512, from its learned position table, which grows with L. This is accepted and recorded rather than shrinking d_model, which would confound L with width. The excess favours the competitor, not iTransformer.
- **H2 (iTransformer paper, claim 2: uses long lookbacks):**
  - iTransformer error falls with L: Δ(L512 − L32) < 0, with the Toyota CI excluding 0 and ≥ 3/4 CALCE cells better.
  - Its Δ is more negative than the time-step Transformer's and the LSTM's, which are expected to plateau or degrade.
  - Measured per task (F-A rmse, F-B rmse_h50). Supported if it holds on Toyota for both tasks; CALCE is reported as k/4.
- **Selection for Stage 3 (leakage-free):**
  - Each model's L is the one with the lowest mean inner-validation RMSE (cross-fit predictions on held-out *training* cells, `inner_val_predictions.parquet`), per (model, task, dataset).
  - Test scores are not used for selection.

### Stage 2 amendment (2026-11-21, owner decision; before any CALCE result)
- **L = 512 dropped from the remaining runs.**
  - It is ≈ 91–92 % of the median pre-EOL life on Toyota test1 and CALCE, so the window is full on only 20 % (Toyota test1) and ≈ 8 % (CALCE) of pre-EOL predictions; the rest are mostly padding.
  - It costs most of the compute (Toyota attention models need several GB each; 4 workers thrashed a 24 GB machine).
- The 51 finished Toyota L = 512 runs are kept as a supplementary result and are not part of the H2 test.
- **H2 is tested as L = 128 vs L = 32.** At 128 (≈ 23 % of median life) the window is full on 77–87 % of pre-EOL predictions.
- Selection for Stage 3 is unchanged (lowest inner-validation RMSE), now over L ∈ {32, 128}.
- Context: the iTransformer paper's long-lookback results use L = 96–720 on series tens of thousands of steps long. Here a cell lives 150–2,200 cycles, so claim 2 can only be tested at moderate L.

### Stage 2 outcome (2026-11-21; PatchTST pending, not needed for H2)
Paired Δ RMSE (L128 − L32), % SOH; Toyota 95 % CI, CALCE k/4. Tables: `reports/tables/field_lookback_paired_{soh,forecast}.md`.

| Model | Task | CALCE | Toyota test1 | Toyota test2 |
|---|---|---|---|---|
| iTransformer | F-A | +0.13 (2/4) | −0.03 [−0.09, +0.05] | −0.06 [−0.15, +0.03] |
| iTransformer | F-B h50 | **+0.64 (0/4)** | +0.03 [−0.05, +0.14] | **−0.43** [−0.57, −0.29] |
| Transformer | F-A | −0.40 (3/4) | +0.13 [+0.03, +0.26] | +0.03 [−0.05, +0.12] |
| Transformer | F-B h50 | −0.38 (2/4) | +0.10 [+0.03, +0.18] | **−0.34** [−0.42, −0.26] |
| LSTM | F-A / F-B | −0.05 / −0.07 | ≈ 0 | ≈ 0 |

- **H2: not supported.** iTransformer improves with L only for F-B on Toyota test2. It is flat on F-A and worse on the CALCE forecast (0/4 cells). The time-step Transformer gains at least as much from longer history.
- **Reading:** iTransformer compresses each variate's whole window through one linear map, so a longer window mainly adds parameters. The health signal here is local (slow drift plus regeneration events lasting a few cycles), unlike the long periodic series of the paper's benchmarks.
- **Supplementary (L = 512, Toyota only):** iTransformer is worse than at L = 32 on test1 (F-A +0.38, F-B +0.49, CIs > 0). This is consistent with the padding analysis.
- **Selected lookbacks** (`reports/tables/field_lookback_selection.md`, inner validation):
  - iTransformer: CALCE 32/32, Toyota 128/32 (F-A/F-B).
  - Transformer: CALCE 128/32, Toyota 32/32.
  - LSTM: CALCE 32/128, Toyota 32/128.

### Stage 2 addendum: PatchTST (2026-11-22, 72 runs, 0 failed)
- Selected lookbacks (inner-validation RMSE, same rule): CALCE 32 for F-A (9.17 vs 9.75) and F-B (8.71 vs 8.73); Toyota 128 for F-A (1.99 vs 2.30) and F-B (2.05 vs 2.36). NASA uses 64 as for the other models.
- PatchTST is the only model where L = 128 clearly helps on Toyota, but it stays the least accurate neural model there (≈ 2.0 vs 1.15–1.32 % SOH inner-validation RMSE). H2 (iTransformer) is unaffected.
- Stage 3 runs: `field_final_{nasa,calce,toyota}_patchtst.yaml`, same experiment, one worker.

## Stage 3: final field benchmark (registered 2026-11-21, before any run)
- **Grid:**
  - Tasks F-A, F-B (all horizons), F-C (RUL).
  - Datasets: NASA, CALCE (LOCO, `field_curve`) and Toyota (official split, `field`); ADR-0018 cleaning.
  - 5 seeds (0–4). Experiment `field_final`, configs `field_final_{nasa,calce,toyota}.yaml`.
- **Models:** iTransformer, time-step Transformer, LSTM, LightGBM, ElasticNet, age-only. PatchTST is added with the same rule once its Stage 2 runs finish.
- **Lookbacks:**
  - Stage 2 selection for neural models.
  - F-C uses the F-B lookback (RUL was not screened).
  - NASA (not screened, short cells) and the tabular models use L = 64 (Stage 1).
- **New runs:** every seed is rerun (resume works within an experiment), so all comparisons are within `field_final`.
- **Analysis:**
  - Each model vs age-only, and iTransformer vs each competitor.
  - Toyota: per test split, cluster-bootstrap CI, Wilcoxon with Holm correction over competitors. NASA/CALCE: k/4.
  - Then CQR (per-horizon, ADR-0019) on all runs, with interval informativeness reported.
- **ADR-0021 verdict rule (iTransformer in the field setting):**
  - **Positive** if iTransformer has the best mean rank among learned models over the headline metrics (F-A rmse, F-B rmse_h50, F-C rul_mae; per dataset and Toyota split), and no competitor beats it significantly on Toyota test1 in more than one of the three tasks.
  - **Mixed** if only one condition holds; **negative** otherwise.
  - The Stage 1 (variates: chemistry-conditional) and Stage 2 (lookback: not supported) findings are reported alongside.
- **Regeneration arm:** registered separately before its runs, after the rest-token code is reviewed.

## Stage 3 regeneration arm (registered 2026-11-21, before any run)
- **Question:** can a field model forecast capacity regeneration when the planned rest schedule is known? And does iTransformer use the schedule when it enters the inverted way?
- **Arms** (F-B, NASA + CALCE LOCO, `field_curve`, 5 seeds; experiment `field_regen`; lookbacks equal to `field_final` F-B, so every arm pairs with its `field_final` baseline):
  - **tab:** ADR-0016 covariates (`future_rest`: rest at T+h and rest sum to T+h, per horizon) for iTransformer, the time-step Transformer, LSTM and LightGBM.
  - **token (new):** iTransformer with `rest_token`. The past `log_rest_s` window and the planned rest of each of the next 100 cycles (`future_rest_seq = 100`) form one variate token, `Linear(L + 100 → d)`.
  - Leakage: only `rest_before_s` of future cycles is read (`test_future_rest_seq_reads_only_the_future_rest_schedule`).
- **Regeneration targets:** target cycles preceded by a rest of more than 6 h (ADR-0016 definition). Errors are pooled over cells and seeds and also reported per cell.
- **H3 (primary, h = 1, where both arms hold the same information about the next cycle):**
  - iTransformer-token reduces RMSE at regeneration targets vs its `field_final` baseline by ≥ 26 % (LSTM's gain in ADR-0016).
  - It also reduces it by at least as much as the best tab-arm competitor.
  - Assessed on NASA, which has real, persistent regeneration (EDA §4). CALCE is reported, but its recovery fades within 1–2 cycles.
- **Secondary:**
  - token vs tab for iTransformer at h = 1 and h = 10. At h = 10 the token knows the rest of each intermediate cycle, the tab arm only their sum, so it is a stated information advantage.
  - Overall h = 10 / h = 50 RMSE must not worsen (CI or k/4).
- **Size:** 2 datasets × 4 units × 5 seeds × 5 arms = 200 runs. They run after the main grid, from `main` once the token code is merged (no merge while a sweep runs).

### Stage 3 outcome: main grid (2026-11-22, 810 runs + 180 PatchTST runs, 0 failed)
Tables: `reports/tables/field_final.md`, paired `field_final_paired.md` (`scripts/field_stage3_pairs.py`), intervals `field_final_intervals_summary.csv`.

Headline (RMSE % SOH for F-A and F-B h50, MAE cycles for F-C; best learned model in bold):

| | age-only | iTransformer | LSTM | Transformer | LightGBM | ElasticNet |
|---|---|---|---|---|---|---|
| CALCE F-A | 6.89 | 3.28 | **2.07** | 2.94 | 4.15 | 3.60 |
| CALCE F-B | 7.08 | 3.96 | 2.83 | 3.22 | 4.69 | **2.77** |
| CALCE F-C | 50.7 | **50.6** | 52.5 | 54.0 | 65.7 | 32,547 |
| NASA F-A | 5.85 | 4.59 | 4.22 | 7.77 | **3.94** | 5.42 |
| NASA F-B | 6.28 | 5.82 | **5.62** | 8.47 | 6.47 | 7.74 |
| NASA F-C | 33.8 | **15.1** | 21.3 | 27.2 | 24.3 | 535 |
| Toyota test1 F-A | 4.01 | 1.06 | 1.07 | **0.91** | 0.95 | 1.18 |
| Toyota test1 F-B | 4.22 | 1.26 | 1.00 | 1.03 | **0.93** | 1.42 |
| Toyota test1 F-C | 236 | 55.8 | 54.4 | 58.7 | **51.2** | 79.7 |
| Toyota test2 F-A | 3.67 | **1.55** | 2.19 | 2.53 | 2.55 | 4.16 |
| Toyota test2 F-B | 3.77 | **1.90** | 2.20 | 2.74 | 2.45 | 4.22 |
| Toyota test2 F-C | 259 | 146 | 156 | 162 | 153 | **125** |

- **Field vs age-only:** every learned model beats age-only on Toyota (Holm p < 1e-5), except ElasticNet on test2 F-A/F-B. CALCE F-A/F-B: all models 3–4/4 cells. NASA F-B: no model beats age-only reliably (best LSTM −0.66, 3/4, CI spans 0). ElasticNet F-C diverges on NASA/CALCE (a few extreme predictions; reported, not removed).
- **iTransformer vs competitors:**
  - Toyota test2 (batch shift, EDA §5): best F-A and F-B, significant against every competitor (Holm p ≤ 0.006).
  - NASA F-C: best, 4/4 cells against every competitor.
  - Toyota test1: beaten significantly on F-A by the Transformer (+0.15, p = 0.001) and on F-B by LightGBM, LSTM and Transformer (+0.22 to +0.33, p ≤ 0.004). F-C: no significant difference.
  - CALCE F-A/F-B: behind LSTM (0/4 and 1/4 cells).
- **PatchTST** (added after its Stage 2 selection): Toyota test1 1.64 / 1.70 / 99.5, test2 2.68 / 2.78 / 245; CALCE 8.19 / 8.27 / 98.4 (worse than age-only on all three tasks); NASA 6.26 / 6.16 / 17.8. iTransformer beats it on Toyota test1 in every task (Holm p ≤ 1e-5). This is consistent with (not a test of) channel independence being unable to use the cross-variate structure of the field inputs (Stage 1).
- **Verdict rule (final):** mean rank among the six learned models over the 12 headline conditions: LSTM 2.25, iTransformer 2.33, LightGBM 3.08, Transformer 3.75, ElasticNet 4.50, PatchTST 5.08. Condition 1 fails. Condition 2 and the resulting verdict: see ADR-0021.
- **Intervals (per-horizon CQR, h50, α = 0.1):**
  - Toyota test1: coverage 0.92–0.96, width 2.8–4.8 % SOH, useful share 80–86 %.
  - Toyota test2: neural models under-cover (0.59–0.71; iTransformer 0.66) because the shift is not in the calibration cells; LightGBM keeps 0.87. Accuracy and calibration under shift diverge.
  - CALCE: coverage 0.89–0.94, width 8–31 % SOH, useful share ≤ 10 %. NASA: coverage 0.81–0.90, width 27–34 %, useful share ≈ 0.
  - RUL (log-space CQR vs additive changes little): Toyota test1 coverage 0.94–0.98 at 340–520 cycles width; NASA/CALCE and Toyota test2 under-cover (0.64–0.89).
  - So the field setting does not make NASA/CALCE intervals informative; the 4-cell datasets stay a caveat (ADR-0019).

### Stage 3 outcome: regeneration arm (2026-11-22, 200 runs, 0 failed)
Table: `reports/tables/field_regen_events.md` (`scripts/field_regen_score.py`). Reduction = 1 − RMSE(arm) / RMSE(same model in `field_final`), pooled over cells and seeds at regeneration targets (rest > 6 h); positive = better.

| NASA, h = 1 at regeneration targets (70) | reduction | k/4 | overall h = 1 / h = 50 |
|---|---|---|---|
| iTransformer + token | −8.9 % | 3/4 | −12.1 % / −8.6 % (0/4) |
| iTransformer + tab | +4.3 % | 2/4 | −12.6 % / −9.8 % (0/4) |
| Transformer + tab | +16.6 % | 3/4 | −1.6 % / +18.0 % |
| LightGBM + tab | +12.4 % | 2/4 | −6.1 % / +2.0 % |
| LSTM + tab | −21.1 % | 1/4 | +8.4 % / −16.6 % |

- **H3: not supported.** The token arm does not reduce NASA h = 1 error at regeneration targets (−8.9 %, pre-registered bar +26 %), and is below the best tab competitor (Transformer, +16.6 %).
- **No model reaches the ADR-0016 lab gain (26 %).** Field-setting gains at regeneration targets are small and inconsistent across cells and horizons (e.g. LightGBM +25 % at h = 10 on NASA, 4/4; LSTM −21 % at h = 1 but +17 % at h = 10). With 70 pooled targets (≈ 3–4 events per cell and seed), these estimates are noisy.
- **Interpretation (not tested):** without SOH history the forecast error at a target (4–10 % SOH RMSE on NASA) is larger than the regeneration jump itself (1–4 % SOH, EDA §4), so knowing the rest schedule cannot show through. ADR-0016 found the gain with SOH history, where the level is known and the jump is the main error.
- **Secondary:**
  - token vs tab for iTransformer: worse at NASA h = 1 (4.93 vs 4.33 % SOH), better at h = 10 (5.16 vs 5.57) and better overall on CALCE (h = 1 4.00 vs 4.35).
  - Adding any rest-schedule input worsens iTransformer's overall forecast on both datasets (NASA 0/4 cells, CALCE 0–2/4); it fails the "must not worsen" condition. LSTM + tab improves CALCE at every horizon (h = 50 +17 %, 4/4).
- **Consequence:** the field forecaster does not predict regeneration. The demo and README state that regeneration is visible in field signals when it happens (EDA §4) but is not forecastable at this error level.
