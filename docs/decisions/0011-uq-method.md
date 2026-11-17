# ADR-0011: Uncertainty method, CQR vs deep ensemble vs GPR (pre-registered)

- **Status:** Accepted: CQR on single models is primary; ensemble+CQR is optional (registered 2026-11-16; outcome 2026-11-17). Implementation: `uq/conformal.py`, `battery-rul calibrate`.

## Hypothesis
- Pooled split-conformal CQR (PROTOCOL §3, §5) brings 90 % interval coverage (PICP) on held-out cells to 0.90 ± 0.05 for every quantile model, at a mean interval width (MPIW) no more than 1.3× the raw interval's.
- Raw quantile models under-cover; LightGBM's raw coverage on CALCE was 0.74–0.79.
- GPR is the reference. Pilot: raw PICP 0.54 at h=50 on CALCE.

## Design
- **Arms:** raw quantiles; CQR-calibrated; 5-seed deep ensemble (quantiles averaged over seeds).
- **Metrics:** PICP, MPIW, interval score, CRPS, and reliability diagrams per dataset and horizon.
- **Decision rule:** the primary method is the one meeting the PICP target with the lowest interval score. If none meets it, report the shortfall honestly.

## Outcome
- **Evidence:**
  - Single model, raw and CQR: `reports/tables/benchmark_calibration.csv` (`battery-rul calibrate` on all benchmark runs).
  - 5-seed ensemble, raw and CQR: `reports/tables/benchmark_ensemble_calibration.csv`, from `scripts/uq_ensemble.py`.
- **How the ensemble arm was built:**
  - The 5 seed runs of each benchmark unit are averaged per quantile level, for both test and inner-validation predictions.
  - The average is then calibrated with the same pooled CQR. The calibration data are the same and the rule-7 guard is the same.
  - Level-0 baselines have no inner-validation predictions and were skipped.
- **Not computed:** CRPS. Only the 5-quantile grid is stored, and the interval score is the proper scoring rule reported instead.
- **Target band:** PICP within 0.90 ± 0.05.

### Forecast h = 50, all origins: 10 quantile models × 4 dataset-splits = 40 conditions
| Arm | Conditions in the target band | Note |
|---|---|---|
| Raw quantiles | 19/40 | iTransformer on NASA 0.46, DLinear on NASA 0.56 |
| **CQR (single model)** | **30/40** | |
| Ensemble, raw | 17/40 | Averaging quantiles narrows intervals; it does not fix under-coverage |
| Ensemble + CQR | 32/40 | Interval score ≤ single CQR in most conditions (e.g. LSTM NASA 14.6 vs 18.0; Transformer Toyota test1 2.16 vs 2.73). LightGBM is unchanged because its seeds are near-identical. |

### Where coverage still fails after CQR
- **Toyota test2 (secondary test set).** GRU 0.47 (ensemble 0.34), LSTM 0.66 (0.53), LightGBM 0.76.
  - The calibration residuals come from the training distribution, so a shifted test batch breaks the exchangeability CQR relies on.
  - iTransformer (0.95), PatchTST (0.96) and the linear models stay calibrated there.
- **RUL at the start points.** The median calibrated PICP is 0.90–0.94 on NASA, CALCE and Toyota test1, but only 0.72 on Toyota test2. The minima fall to 0.51–0.69.
- **SOH estimation is well calibrated everywhere** (median 0.89–0.97 calibrated), except the 0.72 minimum on Toyota test2.

### Hypothesis check
- **"CQR brings every quantile model to 0.90 ± 0.05": not met in full.** It is met for 30/40 forecast conditions and for every condition except the Toyota test2 shift cases above.
- **The width hypothesis holds where coverage is reached.** Calibrated MPIW is under 1.3× raw except where raw was badly under-covering, e.g. NASA iTransformer 5.2 → 21.2 %SOH. There the wider interval is the honest price of coverage.

## Decision
- **Primary UQ: pooled split-conformal CQR on each model's own quantiles.** It meets the target most often among single-model methods, needs one training run, and is cheap to serve.
- **Ensemble + CQR is reported as the best-scoring option** (32/40, lower interval score). It is not the deployment default, because it costs 5× in training and serving for a modest gain on a 2-vCPU Space.
- **GPR has no inner-validation predictions** (`cross_fit=False`), so it stays raw-only. It is reported as a reference, not as a candidate.
- **The Toyota test2 under-coverage is reported as a limitation:** conformal guarantees do not hold under distribution shift. This motivates the OOD warning in the deployed app (PLAN §7, Phase 8).
- **iTransformer-v2 uses its own quantile head plus CQR.** It is among the models that stay calibrated on test2 (0.95).

