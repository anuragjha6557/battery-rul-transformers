# ADR-0004: Evaluation protocol: three tasks, LOCO with cross-fitted inner folds, Toyota-only tuning

- **Status:** Accepted (protocol v1.0 frozen in [`PROTOCOL.md`](../../PROTOCOL.md))
- **Date:** 2026-11-15

## Context
The source paper reported RMSE in normalised units from 3-fold CV over 4 cells. It mixed same-cycle SOH estimation with "forecasting" and never defined a prediction start point or RUL_pred. Phase-1 data inspection added three facts:
1. NASA B0005/06/07 share one rig and rest schedule, so their regeneration jumps co-occur at the same `cycle_idx`.
2. CALCE capacity dips are dominated by an equipment artifact (a skipped CV step).
3. Discharge-phase quantities of cycle k are near-copies of the target `capacity_k`.

## Options considered
| Question | Options | Chosen | Why |
|---|---|---|---|
| Task framing | one "RUL" task / **three tasks (SOH-now, trajectory, RUL)** | three | Separates what the paper measured (Task A) from what it claimed (Tasks B and C). |
| Outer split, NASA/CALCE | 3-fold CV as in the paper / **LOCO** / leave-rig-out | LOCO, plus B0018 reported as the independent fold | Leave-rig-out on NASA trains on a single cell. LOCO plus explicit reporting of the one rig-independent cell is honest and still trainable. |
| Validation and calibration at n = 4 | single held-out cell / **cross-fitted inner LOCO (CV+)** | CV+ | No cell is wasted. The 3 sub-models act as an ensemble, and their held-out residuals give a valid conformal calibration set (Barber et al. 2021). |
| Where to tune | on NASA/CALCE inner folds / **on Toyota** | Toyota | 96 grid configurations picked on one validation cell is winner's curse. Toyota's 41-cell train split supports real model selection, and the configs transfer as architecture choices, not weights. |
| Start points | %-of-life only / **fixed-cycle (headline) + %-of-life** | both | %-of-life leaks life length, so it isn't deployable; it is kept for comparability with the literature and α-λ. |
| Age input | absolute `cycle_idx` / **no absolute index** | no index | It would let models memorise rig-mates' regeneration cycles. An ablation measures the effect. |
| Statistics at n = 4 | p-values / **direction-consistency counts + cluster-bootstrap CIs** | counts + CIs | p-values at n = 4 are theatre. Real tests are kept for Toyota. |

## Decision
Adopt `PROTOCOL.md` v1.0. Its §4 leakage rules become executable tests in `tests/test_leakage.py` (Phase 3), and the benchmark runner refuses to run if they are missing or failing.

## Consequences
- Training cost per NASA/CALCE configuration is ×3 (cross-fitting). It is affordable under ADR-0007 (4 concurrent MPS workers).
- Headline numbers will look worse than the paper's. That is the point, and the README says so with the reasons above.
- Fixed-cycle start values and the EOL rule are filled in by ADR-0005 from `reports/data_quality.md` before any model runs.
