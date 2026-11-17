# ADR-0009: Do physics-informed curve features help? (pre-registered ablation)

- **Status:** Accepted: `mc_curve` not adopted (hypothesis registered 2026-11-16, before any run; outcome 2026-11-17)

## Hypothesis
Voltage-grid ICA and causal ΔQ(V) features (`feature_set=mc_curve`, `features/curves.py`) reduce error versus `mc` for the best tabular model (LightGBM) and for iTransformer:
- **H1 (Task A):** SOH RMSE on NASA/CALCE LOCO falls by ≥ 10 % relative to `mc`.
- **H2 (Task B):** h=50 RMSE falls on Toyota test1.

Motivation: pooled Spearman ρ with SOH is 0.91–0.99 for `dq_min` and 0.86–0.97 for the ICA peak height. A one-fold, untuned pilot showed no Task A gain and seed instability for iTransformer, which is why this needs the full test.

## Design
- **Arms:** `mc` vs `mc_curve`, identical tuned hyperparameters (tuned on `mc`), 5 seeds, PROTOCOL v1.1 splits.
- **Metrics:** Task A RMSE; Task B rmse_h50 and rmse_smooth_h50.
- **Decision rule (PLAN §6.5):** keep `mc_curve` only if the Toyota CI on the improvement excludes zero **and** the gain is direction-consistent on ≥ 3/4 cells in both NASA and CALCE.

## Outcome
- **Evidence:**
  - MLflow experiment `abl_curve` (`mc_curve` arm): 180 runs, 0 failures. The `mc` arm is experiment `benchmark`, run with identical tuned parameters and seeds.
  - Tables: `reports/tables/abl_curve.{md,csv}` and `abl_curve_paired_{soh,forecast}.{md,csv}`, from `scripts/compare_arms.py`.
- **Comparison method:**
  - Runs are paired on (test cell, seed); Δ = `mc_curve` − `mc` in %SOH, so negative is better.
  - Toyota: cluster-bootstrap 95 % CI.
  - NASA/CALCE: number of the 4 cells improved.
- **Not computed:** `rmse_smooth_h50` is logged per run in MLflow but is not part of the per-cell report tables, so it was not used for the decision.

| Model | Task | Toyota test1 Δ | Toyota test2 Δ | NASA Δ (cells better) | CALCE Δ (cells better) |
|---|---|---|---|---|---|
| LightGBM | A: SOH RMSE | +0.000 [−0.000, +0.000] | −0.003 [−0.004, −0.003] | −0.002 (3/4) | +0.019 (0/4) |
| iTransformer | A: SOH RMSE | +0.000 [−0.000, +0.000] | +0.002 [+0.001, +0.002] | +0.046 (0/4) | −0.003 (3/4) |
| LightGBM | B: h50 RMSE | **−0.033 [−0.046, −0.019]** | **−0.021 [−0.031, −0.012]** | +0.094 (2/4) | +0.019 (1/4) |
| iTransformer | B: h50 RMSE | −0.013 [−0.020, −0.006] | +0.026 [+0.018, +0.035] | +0.033 (1/4) | −0.053 (2/4) |

- **H1 (SOH estimation improves by ≥ 10 % on NASA/CALCE): rejected.** Every change is under 0.05 %SOH absolute, under 7 % relative, and in mixed directions. The per-cycle scalars in `mc` (charge time, CC/CV split, throughput) already carry the information. The features correlate strongly with SOH (high ρ) but that correlation is redundant with `mc`, so it adds no new signal.
- **H2 (Toyota test1 h50 improves): supported in-distribution for LightGBM** (−7 % relative, with the improvement significant on test1 and test2 and 34/43 test1 cells better).
  - For iTransformer, test1 improves but test2 gets worse.
  - The gain does not transfer to NASA/CALCE for either model (≤ 2/4 cells).
- **Decision rule (PLAN §6.5): fails for both models.**

## Decision
- **iTransformer-v2 and the benchmark keep `feature_set=mc`.** `mc_curve` stays in the code as a documented optional feature set.
- **The LightGBM Toyota gain is reported as a finding:** ΔQ(V)/ICA summaries help a tree model on the chemistry and protocol it was trained on. This matches Severson 2019, where ΔQ(V) is the key feature.
- **The rule's cross-chemistry requirement is what rejects it.** On 4-cell LCO/NMC sets, the features' gain falls inside run-to-run noise.

