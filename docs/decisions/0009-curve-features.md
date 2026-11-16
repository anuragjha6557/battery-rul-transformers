# ADR-0009: Do physics-informed curve features help? (pre-registered ablation)

- **Status:** Proposed (hypothesis registered 2026-11-16, before any run; outcome appended below)

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
_Pending: MLflow experiment `abl_curve_features`._
