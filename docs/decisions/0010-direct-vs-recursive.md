# ADR-0010: Direct multi-horizon heads vs recursive one-step rollout (pre-registered)

- **Status:** Proposed (registered 2026-11-16)

## Hypothesis
At horizons H ≥ 25, direct multi-horizon heads beat recursive rollout of a one-step model, given the same architecture and tuning. The source paper used recursion. Error compounding should make the gap grow with H.

## Design
- **Models:** the best neural model, iTransformer, and LightGBM.
- **Arms:** (a) direct heads, as implemented; (b) the same model trained for h=1 only and rolled forward on its own predictions, with exogenous channels held at their last value (PROTOCOL §2).
- **Data:** Task B, all three datasets, 5 seeds.
- **Decision rule:** report the gap per horizon with CIs. The direct heads are the default unless recursion wins at H ≥ 25 under the PLAN §6.5 rule.

## Outcome
_Pending._
