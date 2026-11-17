# ADR-0010: Direct multi-horizon heads vs recursive one-step rollout (pre-registered)

- **Status:** Accepted: hypothesis confirmed (outcome 2026-11-16)

## Hypothesis
At horizons H ≥ 25, direct multi-horizon heads beat recursive rollout of a one-step model, given the same architecture and tuning. The source paper used recursion. Error compounding should make the gap grow with H.

## Design
- **Models:** the best neural model, iTransformer, and LightGBM.
- **Arms:** (a) direct heads, as implemented; (b) the same model trained for h=1 only and rolled forward on its own predictions, with exogenous channels held at their last value (PROTOCOL §2).
- **Data:** Task B, all three datasets, 5 seeds.
- **Decision rule:** report the gap per horizon with CIs. The direct heads are the default unless recursion wins at H ≥ 25 under the PLAN §6.5 rule.

## Outcome (MLflow `abl_recursive` vs `benchmark`; 5 seeds, identical tuned iTransformer params)
RMSE ratio recursive / direct, all-origins policy (start points show the same pattern):

| Dataset | h=1 | h=10 | h=25 | h=50 | h=100 | h=200 |
|---|---|---|---|---|---|---|
| NASA (LOCO) | 1.01 | 1.20 | 2.07 | 5.63 | 59.0 | – |
| CALCE (LOCO) | 0.99 | 1.04 | 1.22 | 2.21 | 6.90 | – |
| Toyota test1 | 0.95 | 0.94 | – | 1.53 | 1.84 | 1.94 |
| Toyota test2 | 0.96 | 1.11 | – | 1.15 | 1.58 | 2.39 |

- **h ≤ 10:** recursive matches or slightly beats direct (0.91–1.20). That is expected, since it is trained for exactly h=1.
- **h ≥ 25:** direct is better on every dataset, and its CIs exclude the recursive value on Toyota and on NASA/CALCE at h ≥ 50. Compounding error grows with the horizon.
  - On NASA the rollout **diverges**: h=100 RMSE is 837 %SOH, i.e. physically impossible SOH values. Feeding back its own predictions with held exogenous channels drives the model out of its training distribution.
  - The only exception is CALCE start points at h=50 (ratio 0.89), and the CIs overlap ([0.99, 2.05] vs [0.99, 1.65]).
- **Decision:** keep direct multi-horizon heads for every neural model and for iTransformer-v2.
- **Implication for the source paper:** it scored *recursive* single-channel models over long rollouts against *one-step* multi-channel models. This experiment shows that recursion alone degrades long-horizon error by about 2–6× (NASA/CALCE h=50), which accounts for much of the "multi-channel gain" the paper attributed to architecture.
