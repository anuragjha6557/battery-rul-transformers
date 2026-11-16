# ADR-0012: Cross-chemistry transfer, Toyota (LFP) pre-training → NASA/CALCE (pre-registered)

- **Status:** Proposed (registered 2026-11-16)

## Hypothesis
Pre-training on 124 LFP cells, then fine-tuning on the 3 LOCO training cells, beats training from scratch on NASA/CALCE for Task B at h=50 and Task C at the fixed starts. Zero-shot transfer will be worse than scratch, given the chemistry and protocol shift (LFP's flat voltage plateau, a different charge protocol).

## Design
- **Arms (PROTOCOL §3):** scratch; zero-shot; fine-tune head-only; fine-tune full; few-shot on the test cell's cycles ≤ T_p.
- **Inputs:** chemistry-agnostic shared inputs only (SOH, normalised charge/discharge durations, IR where present). Curve features are excluded, because the voltage windows differ by chemistry.
- **Seeds:** 5 per arm.
- **Decision rule:** transfer is adopted for iTransformer-v2 only under the PLAN §6.5 rule. A negative result is reported as such.

## Outcome
_Pending._
