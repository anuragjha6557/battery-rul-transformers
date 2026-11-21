# ADR-0020: Field-setting benchmark: SOH estimation, forecasting, RUL without SOH history (pre-registered)

- **Status:** Stage 1 decided 2026-11-21 (Stages 2–3 to be registered before their runs)

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
