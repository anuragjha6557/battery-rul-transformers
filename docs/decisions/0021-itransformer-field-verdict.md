# ADR-0021: Is iTransformer justified in the field setting? (verdict)

- **Status:** Accepted: **negative** under the pre-registered rule, with a stated borderline reading (2026-11-23)
- **Evidence:**
  - Experiment `field_final` (990 runs, 5 seeds, 0 failed): `reports/tables/field_final.md`, paired `field_final_paired.md` (`scripts/field_stage3_pairs.py`), intervals `field_final_intervals_summary.csv`.
  - Claim tests: ADR-0020 Stage 1 (variates), Stage 2 (lookback), Stage 3 regeneration arm (known-future token).

## Question
PLAN_PHASE2 asked whether iTransformer earns its place through the strengths its paper (Liu et al., ICLR 2024) claims, in the setting a real BMS faces: field-measurable inputs only, no SOH or capacity history.

## Pre-registered rule (ADR-0020, Stage 3)
- **Positive** if iTransformer has the best mean rank among learned models over the headline metrics (F-A rmse, F-B rmse_h50, F-C rul_mae; per dataset and Toyota split), **and** no competitor beats it significantly on Toyota test1 in more than one of the three tasks.
- **Mixed** if only one condition holds; **negative** otherwise.

## Result
**Condition 1 fails.** Mean rank over 12 conditions: LSTM 2.25, iTransformer 2.33, LightGBM 3.08, Transformer 3.75, ElasticNet 4.50, PatchTST 5.08.

**Condition 2 depends on what "significantly" means; the rule did not say.** Toyota test1, competitor minus iTransformer (positive = competitor better):

| task | competitor | Δ [95 % cluster-bootstrap CI] | Holm p | CI excludes 0 | Holm p < 0.05 |
|---|---|---|---|---|---|
| F-A | LightGBM | 0.11 [0.02, 0.21] | 0.13 | yes | no |
| F-A | Transformer | 0.15 [−0.09, 0.37] | 0.001 | no | yes |
| F-B | LightGBM | 0.33 [0.21, 0.47] | 3e-6 | yes | yes |
| F-B | LSTM | 0.26 [0.12, 0.40] | 4e-4 | yes | yes |
| F-B | Transformer | 0.22 [0.10, 0.36] | 0.004 | yes | yes |
| F-C | none | | | | |

- With either criterion alone, the project's CI rule (PLAN §6.5) or the Holm-Wilcoxon test, competitors win 2 of 3 tasks: condition 2 fails and the verdict is **negative**.
- Only if both criteria must hold for the same competitor does F-A drop out (1 of 3 tasks), and the verdict would be **mixed**.
- We report **negative**, since it holds under each criterion the project has used. We do not pick the reading after seeing the result. The borderline is stated wherever the verdict is cited.

## What iTransformer does well (reported alongside, not part of the rule)
- **Under distribution shift** (Toyota test2, a batch with a different rest, CV time and temperature; EDA §5), it is the most accurate model for F-A (1.55 % SOH vs 2.19 for the next best) and F-B (1.90 vs 2.20). It is significantly better than every competitor (Holm p ≤ 0.006).
- **RUL on the small datasets:** best on NASA (15.1 cycles MAE vs 21.3 for LSTM; 4/4 cells against every competitor), and level-best on CALCE.
- **Its calibration does not follow its accuracy under shift.** On Toyota test2, h50 CQR coverage is 0.66, against 0.87 for LightGBM.

## The paper's claims, tested
| Claim | Test | Outcome |
|---|---|---|
| Variate tokens exploit many correlated variates | Stage 1, `field` → `field_curve` (+15 Q(V) points) | Chemistry-conditional. Largest gain of any model on CALCE (−2.00 % SOH, 4/4); it hurts on Toyota (LFP flat plateau). |
| Benefits from long lookbacks | Stage 2, L 32 → 128 (512 dropped, owner decision) | Not supported. No monotone gain. L = 128 is worse on CALCE F-B (0/4) and mixed on Toyota. |
| Takes known-future covariates as a variate | Stage 3 rest-schedule token (H3) | Not supported. −8.9 % at NASA regeneration targets (bar +26 %). Any rest input worsens its overall forecast. |
| Channel mixing beats channel independence | iTransformer vs PatchTST | Supported here. iTransformer has lower error than PatchTST in all 12 conditions (significant on every Toyota split and task, Holm p ≤ 1e-5). On CALCE, PatchTST is worse than age-only. |

## Consequences
- The field-setting write-up (README, showcase, model card) states the verdict as negative. iTransformer is presented as the most shift-robust field estimator, not as the best overall. LSTM and LightGBM are equally strong in-distribution.
- **Deployment choice (Stage 4)** is made separately on the deploy use case: accuracy under protocol shift and interval reliability, with OOD guarding (EDA §5). It is not justified by this verdict.
- The lab-setting result (iTransformer best mean rank, ADR-0014) stands, and is reported as a different setting.
