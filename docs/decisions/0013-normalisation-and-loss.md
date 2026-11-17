# ADR-0013: Input normalisation and training loss (pre-registered)

- **Status:** Accepted: neither change adopted (registered 2026-11-16; outcome 2026-11-16)

## Hypotheses
- **E (normalisation):** per-instance normalisation with location = last value (RevIN-style, already used in RLinear, PatchTST and iTransformer) beats train-set global scaling alone for the time-step Transformer and LSTM on cross-cell generalisation, which has larger cell-to-cell shifts on NASA and CALCE.
- **F (loss):** a Huber loss (δ chosen on Toyota inner-val) reduces RMSE on NASA, where regeneration jumps act as outliers, compared with MSE. Pinball loss is used whenever quantiles are produced.

## Design
- 5 seeds, Task B, PROTOCOL v1.1.
- **Decision rule:** PLAN §6.5. Changes apply to all neural models or to none (ADR-0006 fairness).

## Outcome
- **Evidence:**
  - MLflow experiment `abl_norm_loss`: 270 runs, 0 failures.
  - Tables: `reports/tables/abl_norm_loss.{md,csv}` (per arm) and `reports/tables/abl_norm_loss_paired.{md,csv}`, from `scripts/compare_arms.py`.
- **Comparison method:**
  - Runs are paired on (test cell, seed); Δ = candidate − reference, so negative is better.
  - Toyota: cluster-bootstrap 95 % CI plus Wilcoxon on per-cell means.
  - NASA/CALCE: number of the 4 cells where the candidate is better.
- **Metric:** RMSE in %SOH over all origins, at h = 50 (primary) and h = 10.
- **Scope:** this ablation is forecast-only, so the RUL half of the §6.5 rule was not evaluated. Neither change passed the forecast half, so RUL runs would not alter the decision.

### E: RevIN on the time-step Transformer and the LSTM, vs the benchmark (no RevIN)
| Arm | Toyota test1 Δh50 | Toyota test2 Δh50 | NASA Δh50 (cells better) | CALCE Δh50 (cells better) |
|---|---|---|---|---|
| Transformer + RevIN | +1.25 [+1.07, +1.45] | +0.59 [+0.53, +0.63] | −1.76 [−2.95, −0.56] (4/4) | +0.20 [−0.88, +1.00] (1/4) |
| LSTM + RevIN | +0.41 [+0.30, +0.53] | +0.10 [+0.05, +0.15] | +0.78 [+0.44, +1.01] (0/4) | +0.57 [+0.06, +1.02] (1/4) |

- **Result: rejected.** RevIN makes both models significantly worse on Toyota; the Transformer's h50 error is about 3.4× higher on test1 (p < 1e-12).
- **The one gain is the Transformer on NASA** (4/4 cells at h50; 4/4 on both NASA and CALCE at h10). This is the cross-rig shift the hypothesis predicted, but the same change hurts in-distribution.
- **Mechanism:** the same as ADR-0008 §4. Per-window location/scale removal discards the absolute SOH level and the long-run fade rate the horizon-50 head needs. iTransformer keeps both by feeding location and log-scale back as tokens.

### F: Huber vs MSE, both point-forecast heads with otherwise identical tuned parameters
| Arm | Toyota test1 Δh50 | Toyota test2 Δh50 | NASA Δh50 (cells better) | CALCE Δh50 (cells better) |
|---|---|---|---|---|
| iTransformer: Huber − MSE | −0.006 [−0.019, +0.006] | +0.013 [+0.004, +0.022] | −0.089 [−0.149, −0.029] (4/4) | −0.031 [−0.060, +0.016] (3/4) |
| LSTM: Huber − MSE | +0.13 [+0.06, +0.21] | −0.095 [−0.108, −0.083] | −1.47 [−2.19, −0.76] (4/4) | +0.06 [−0.74, +0.55] (1/4) |

- **Result: rejected.** For iTransformer the effect is negligible: under 0.1 %SOH on NASA, and Toyota is tied on test1 and slightly worse on test2.
- **For the LSTM the sign flips** between Toyota test1 and test2 and between NASA and CALCE. Huber mainly stabilises the LSTM's bad NASA seeds (its MSE arm has a 5.05 mean with a wide CI); it is not a consistent gain.
- **The NASA-regeneration hypothesis is directionally supported** (NASA 4/4 for both models), but the effect is too small, or too inconsistent, to change a model-wide default.

### Side result: quantile (pinball) head vs a point MSE head (iTransformer, benchmark vs the F arm)
- The quantile head's median is **better** on Toyota: test1 Δh50 = −0.052 [−0.068, −0.036], with the point head better on only 3/43 cells. It is also better on test2 (−0.014) and on CALCE (4/4 cells).
- The point head is better on NASA (−0.58, 4/4 cells).
- Training with pinball loss therefore costs nothing in point accuracy where data are adequate, and it produces the intervals CQR needs.

## Decision
- **No change for any neural model** (ADR-0006: a change applies to all models or to none).
- Train-set scaling stays. Pinball loss stays for quantile models and MSE for point models. RevIN remains specific to the architectures that define it (RLinear, PatchTST).
- **iTransformer-v2 keeps the quantile head** (ADR-0011/0014).

