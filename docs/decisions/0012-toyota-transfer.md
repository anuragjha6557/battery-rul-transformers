# ADR-0012: Cross-chemistry transfer, Toyota (LFP) pre-training → NASA/CALCE (pre-registered)

- **Status:** Proposed (registered 2026-11-16)

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
_Pending._
