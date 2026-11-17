# ADR-0012: Cross-chemistry transfer, Toyota (LFP) pre-training → NASA/CALCE (pre-registered)

- **Status:** Accepted: transfer not adopted as the default (registered 2026-11-16; outcome 2026-11-17)

## Hypothesis
Pre-training on 124 LFP cells, then fine-tuning on the 3 LOCO training cells, beats training from scratch on NASA/CALCE for Task B at h=50 and Task C at the fixed starts. Zero-shot transfer will be worse than scratch, given the chemistry and protocol shift (LFP's flat voltage plateau, a different charge protocol).

## Design
- **Arms (PROTOCOL §3):** scratch; zero-shot; fine-tune head-only; fine-tune full; few-shot on the test cell's cycles ≤ T_p.
- **Inputs:** chemistry-agnostic shared inputs only (SOH, normalised charge/discharge durations, IR where present). Curve features are excluded, because the voltage windows differ by chemistry.
- **Seeds:** 5 per arm.
- **Decision rule:** transfer is adopted for iTransformer-v2 only under the PLAN §6.5 rule. A negative result is reported as such.

## Design details fixed during implementation (2026-11-16, before the evaluated run)
- **Shared channels:** `soh, ir_ohm, charge_throughput_ah, charge_time_s, cc_time_s, cv_time_s`, the only ones finite in all three datasets. `charge_throughput_ah` is nearly a copy of SOH.
- **Horizons:** one set for all datasets, (1, 10, 25, 50, 100), because the output head transfers. Toyota's native horizon 200 is dropped for this experiment.
- **Fine-tuning:** cross-fitted like every other model (3 sub-models over the inner folds, averaged). `ft_head` freezes all but the head; `ft_full` and `few_shot` use lr × 0.1.
- **Few-shot:** one model per start point. Training origins are ≤ T_p, and any target with origin + h > T_p is masked (unit-tested). It is evaluated on start points only.
- **Known limitation:** Toyota charge-time channels contain pause-inflated outliers (max 179 653 s vs a median ≈ 1 700 s), which inflate the non-robust scaler. A robust scaler changes every feature set, so it is tested as an arm of ADR-0013 rather than patched here.
- **Pilot** (1 seed, untuned defaults, B0018 / CS2_35, not evidence):
  - zero-shot is worse than scratch (NASA start-point h=50: 8.32 vs 2.53 %SOH);
  - `ft_full` ≈ scratch;
  - `ft_head` is poor on NASA.

## Outcome
- **Evidence:**
  - MLflow experiment `transfer`: 200 runs, 0 failures. Pre-training run in experiment `pretrain` (239 s, 152 epochs, 87 827 Toyota windows).
  - Checkpoint: `artifacts/pretrained/itransformer__forecast.pt`, logged by SHA in every run.
  - Tables: `reports/tables/transfer.{md,csv}` and `transfer_paired_{all,start_points}.{md,csv}`, from `scripts/compare_arms.py`.
- **Comparison method:** runs are paired on (test cell, seed); Δ = arm − scratch in %SOH, so negative is better. Cells are counted out of 4.
- **Scope deviations, logged:**
  - Only Task B (forecasting) was run. Task C (RUL) was not run for transfer, so the RUL half of the hypothesis is untested.
  - The robust-scaler arm announced above was not added to ADR-0013. The pause-inflated Toyota charge-time scaling remains a known limitation of this experiment.

### h = 50 RMSE, all origins
| Arm vs scratch | NASA Δ (cells better) | CALCE Δ (cells better) |
|---|---|---|
| ft_full | **−1.53 [−1.63, −1.41] (4/4, 20/20 pairs)** | +0.29 [+0.09, +0.47] (1/4) |
| ft_head | +1.75 [+0.59, +2.90] (0/4) | +1.09 [+0.98, +1.22] (0/4) |
| zero_shot | +3.58 [+2.08, +5.07] (0/4) | +1.96 [+1.69, +2.24] (0/4) |

### Other conditions
- **Fixed and fraction start points, h = 50:**
  - `ft_full` on NASA: −1.57 [−3.13, −0.02], 3/4 cells.
  - `ft_full` on CALCE: +0.14 [−0.10, +0.35], 1/4 cells.
  - `few_shot` vs `ft_full`: −0.10 on NASA (4/4) and −0.03 on CALCE (1/4).
- **Short horizon (h = 10, all origins):** `ft_full` is slightly worse than scratch on both datasets: NASA +0.11, CALCE +0.06, 0/4 cells each.

### Reading
- **Full fine-tuning helps only where target data are scarce and the horizon is long.**
  - NASA cells have about 130–170 cycles. There, h50 error falls by 28 % (5.41 → 3.88 %SOH) on every cell and seed.
  - That brings iTransformer close to the benchmark leader on NASA (LightGBM 3.24, `mc` features). It does not overtake it.
  - CALCE cells have about 900 cycles. Three of them are enough to train from scratch, and the LFP prior hurts slightly.
- **The Toyota prior acts as a long-horizon fade-shape regulariser, not as transferable short-term dynamics.** h = 10 gets slightly worse everywhere.
- **Zero-shot and head-only transfer are clearly worse than scratch**, as pre-registered. LFP fade dynamics and channel scales do not carry over without updating the encoder.
- **Few-shot adaptation on the test cell's own early cycles adds ≤ 0.1 %SOH.**

### Decision rule (PLAN §6.5): fails
- It requires improvement on both NASA and CALCE, and CALCE gets worse.
- The Toyota leg is not applicable, because Toyota is the source.

## Amendment 1: Task C (RUL) transfer, registered 2026-11-17 before the run
- **Arms:** scratch, zero_shot and ft_full; 5 seeds; NASA and CALCE LOCO; tuned `itransformer__rul` parameters.
  - A separate Toyota RUL checkpoint is pre-trained (`artifacts/pretrained/itransformer__rul.pt`).
  - `ft_head` is dropped to save compute, since it was dominated in Task B.
  - `few_shot` is undefined for RUL: labels on the test cell's own cycles ≤ T_p require its future EOL. The code rejects it.
- **Hypothesis:** ft_full beats scratch on NASA (scarce data, as in Task B), but not on CALCE. Zero-shot is worse than scratch, because Toyota lives (≈ 150–2 300 cycles, LFP) set the RUL scale.
- **Metrics:** RUL MAE (cycles) and α-λ accuracy at the fixed start points, plus all-origin MAE. The comparison method is the same as for Task B.

### Amendment 1 outcome (2026-11-17)
- **Evidence:**
  - MLflow experiment `transfer`, `params.task = rul`: 120 runs, 0 failures. Pre-training: 208 s, 79 epochs.
  - Tables: `reports/tables/transfer_rul_paired_{all,start_points,alpha_lambda}.{md,csv}`.

| Arm vs scratch | NASA Δ MAE, cycles (cells better) | CALCE Δ MAE, cycles (cells better) |
|---|---|---|
| ft_full, all origins | +0.1 [−7.0, +7.1] (2/4) | **+28.4 [+6.1, +56.1]** (1/4) |
| ft_full, start points | +3.0 [−6.3, +12.2] (2/4) | +13.0 [−4.7, +30.8] (2/4) |
| zero_shot, all origins | +23.2 [+9.3, +37.0] (0/4) | +182.8 [+117.2, +226.7] (0/4) |

- **α-λ accuracy at λ = 0.5** (higher is better; there is one start per cell, so each cell-seed scores 0 or 1):
  - ft_full: 0.25 vs 0.10 on NASA and 0.75 vs 0.55 on CALCE. The CIs touch 0, and only 1/4 cells improve.
  - zero_shot scores 0.00 on both datasets.
- **Reading:**
  - The pre-registered NASA gain does **not** appear for RUL. ft_full ties scratch on NASA (scratch already reaches about 17 cycles MAE on 130–170-cycle cells) and is worse on CALCE.
  - Zero-shot is far off. The Toyota RUL scale (lives of 150–2 300 cycles) does not carry over without retraining.
  - The forecasting benefit on NASA (−28 % at h = 50) therefore comes from the long-horizon fade shape. It does not turn into better end-of-life timing.
- **Decision:** unchanged. Transfer is not the default for any task.

## Decision
- **iTransformer-v2 does not use Toyota pre-training by default.**
- **The NASA result is reported as a positive, bounded finding:** transfer from a large LFP corpus helps a data-starved target at long horizons. It is offered as an option (`battery-rul transfer`).
- **Pre-training is not a general cross-chemistry fix.** This answers the paper's stated future-work question honestly: transfer is conditional, and it is not free.

