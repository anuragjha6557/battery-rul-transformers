# ADR-0014: Final model selection, iTransformer-v2

- **Status:** Accepted (2026-11-17)
- **Evidence:**
  - ADR-0008 (benchmark), ADR-0009–0013 (Phase 6 outcomes).
  - Tables in `reports/tables/`, summarised in `reports/results.md` and the README.

## Context
PLAN §6.4 defined iTransformer-v2 as iTransformer plus whichever Phase 6 improvements pass the pre-registered rule (PLAN §6.5): voltage-grid/ICA/ΔQ(V) features, direct quantile heads with CQR, Toyota pre-training, normalisation and loss changes. The rule requires a Toyota gain with a CI excluding zero **and** direction consistency on ≥ 3/4 cells on both NASA and CALCE.

## Options considered (with outcomes)
| Candidate component | Outcome | ADR |
|---|---|---|
| Direct multi-horizon heads vs recursive rollout | **Kept.** Recursive/direct h50 RMSE ratio: 1.15–5.6 | 0010 |
| Quantile (pinball) heads + CQR | **Kept.** CQR puts 30/40 h50 conditions in 0.90 ± 0.05; the quantile median beats a point MSE head on Toyota | 0011, 0013 |
| ICA/ΔQ(V) curve features (`mc_curve`) | Rejected. LightGBM gains on Toyota only | 0009 |
| Toyota pre-training + fine-tuning | Rejected as the default. −28 % h50 on NASA, worse on CALCE | 0012 |
| RevIN; Huber loss | Rejected | 0013 |
| 5-seed deep ensemble on top of CQR | Optional: 32/40 vs 30/40 at 5× cost | 0011 |

## Decision
1. **iTransformer-v2 is the benchmarked iTransformer:** inverted (variate-token) attention, direct multi-horizon quantile heads (q = 0.05…0.95, pinball loss), train-set scaling, and level/scale tokens fed back. Pooled split-conformal CQR (α = 0.1) is applied on held-out inner-validation cells.
   - The **MC** variant is the benchmark entry (mean rank 3.08, first).
   - The **SC** variant is the deployed one (mean rank 3.95, second; ADR-0015).
   - The two are statistically tied on most conditions (ADR-0008 §5).
2. **The final benchmark is the `benchmark` experiment.**
   - No Phase 6 change was adopted, so a separate re-run would repeat identical configurations.
   - `configs/experiment/final.yaml` resolves to the same `ExperimentConfig`; this was checked with `load_experiment('final') == load_experiment('benchmark')`.
   - `make bench` therefore resumes, skipping every finished unit, then recalibrates and regenerates every table, figure and the README block.
3. **The claim, stated honestly:**
   - The improvement over the source paper is in the method around the architecture: a leakage-free protocol, direct heads, calibrated intervals, and a quantified answer on transfer.
   - It is not a new architecture beating strong baselines everywhere.
   - iTransformer leads in-distribution (Toyota, 124 cells). LightGBM/ElasticNet match or beat it on 4-cell NASA/CALCE.

## Consequences
- **The README headline follows ADR-0008 Decision 4:** the dataset-dependent ranking first, then the naive-baseline finding, then calibrated coverage.
- **What this project does not claim:** a single "% better than LSTM" number; any reproduction of the paper's 44.6 % / 29 %.
