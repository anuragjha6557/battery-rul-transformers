# ADR-0013: Input normalisation and training loss (pre-registered)

- **Status:** Proposed (registered 2026-11-16)

## Hypotheses
- **E (normalisation):** per-instance normalisation with location = last value (RevIN-style, already used in RLinear, PatchTST and iTransformer) beats train-set global scaling alone for the time-step Transformer and LSTM on cross-cell generalisation, which has larger cell-to-cell shifts on NASA and CALCE.
- **F (loss):** a Huber loss (δ chosen on Toyota inner-val) reduces RMSE on NASA, where regeneration jumps act as outliers, compared with MSE. Pinball loss is used whenever quantiles are produced.

## Design
- 5 seeds, Task B, PROTOCOL v1.1.
- **Decision rule:** PLAN §6.5. Changes apply to all neural models or to none (ADR-0006 fairness).

## Outcome
_Pending._
