# ADR-0019: Adaptive conformal intervals (post-hoc test on existing runs)

- **Status:** Accepted: hypothesis rejected; current CQR kept, plus informativeness reporting (2026-11-20)
- **Evidence:**
  - `scripts/interval_rescoring.py` → `reports/tables/interval_rescoring{,_summary}.csv`.
  - Data: all benchmark runs of iTransformer, iTransformer SC, LightGBM, LSTM and PatchTST (forecast + RUL, 5 seeds), using stored test and inner-validation predictions. There was no retraining.

## Hypothesis (PLAN_PHASE2 §4.1)
Locally adaptive calibration can keep marginal coverage at 0.90 ± 0.05 and ≥ 0.85 in every life-stage bin, while making intervals ≥ 20 % narrower than one additive CQR correction per horizon.

The candidates:
- Mondrian bins on the model's own predicted SOH (causal);
- scaled, multiplicative CQR;
- both combined;
- for RUL, calibration in log space.

## Result (h = 50 forecast; RUL at all origins; mean over models and seeds)
| | Method | PICP | Worst life-stage PICP | Width | Useful share |
|---|---|---|---|---|---|
| NASA | cqr | 0.91 | 0.68 | 15.8 %SOH | 0.3 % |
| | mondrian | 0.87 | 0.64 | 13.9 | 0 % |
| | scaled | 0.91 | 0.69 | 26.0 | 1 % |
| CALCE | cqr | 0.90 | 0.83 | 9.7 | 4 % |
| | mondrian | 0.89 | 0.80 | 9.7 | 10 % |
| Toyota test1 | cqr | 0.91 | 0.87 | 1.07 | 94 % |
| Toyota test2 | cqr | 0.86 | 0.76 | 0.73 | 98 % |
| RUL NASA | cqr / log / scaled | 0.91 / 0.90 / 0.92 | 0.72 / 0.70 / 0.78 | 106 / 134 / 211 cycles | |
| RUL Toyota test1 | cqr / log | 0.91 / 0.94 | 0.79 / 0.87 | 680 / 755 cycles | |

"Useful share" means width < 50 % of the predicted distance to 80 % SOH.

**Findings:**
- **No method narrows intervals by ≥ 20 % while holding coverage.** Mondrian narrows NASA by 12 % but loses coverage (0.87; early-life bin 0.64). Scaled CQR widens.
- **Width is driven by the size of the errors, not by the calibration rule.** Conditioning on the predicted SOH level does not separate easy cases from hard ones.
- **Early-life coverage is the weak spot on NASA:** short histories, the same failure ADR-0008 and the showcase history-length chart identify.
- Log-space RUL calibration improves worst-bin coverage on Toyota test1 (0.79 → 0.87), at +11 % width.

## Decision
1. **Keep per-horizon CQR as the default.**
2. **Narrow intervals at the source** (cleaning, field signals, long lookback; PLAN_PHASE2 Stages 1–3). Re-run this rescoring on the field runs.
3. **Report informativeness everywhere.** Every interval table gets a "useful share" column, and dashboards mark uninformative bands rather than presenting them as meaningful.
   - Today's state: NASA forecasts ≈ 0 % useful, CALCE ≈ 4 %, Toyota ≈ 94–98 %.
4. **Offer log-space RUL calibration** as an option for long-lived cells.
