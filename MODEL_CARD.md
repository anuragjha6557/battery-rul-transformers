# Model card: iTransformer-v2 for battery SOH forecasting and RUL

Code, benchmark and decisions: https://github.com/anuragjha6557/battery-rul-transformers. Demo: https://huggingface.co/spaces/anurag6557/battery-rul-itransformer-v2. This card covers the lab model and the field models. Every number below comes from the generated tables in `reports/tables/` and the ADRs; none is taken from the source paper.

## Model details

### Lab model (`itransformer_sc`, capacity log required)
- **Architecture:** inverted-attention iTransformer, single-channel variant (SC). Inputs are the SOH history and causal SOH summaries; capacity is divided by the mean of the first 5 cycles. Outputs are direct multi-horizon quantile heads (q = 0.05 ... 0.95, pinball loss) for SOH at h = 1, 10, 25, 50, 100 and for RUL to 80 % SOH ([ADR-0014](docs/decisions/0014-final-model-selection.md)).
- **Intervals:** split-conformal CQR, alpha = 0.1, calibrated on cells the model never trained on ([ADR-0011](docs/decisions/0011-uq-method.md), [ADR-0015](docs/decisions/0015-deployment.md)).
- **Why SC:** public users rarely have consistent per-cycle charge features. SC is statistically tied with the multi-channel variant on most benchmark conditions (ADR-0014, [ADR-0008](docs/decisions/0008-baseline-findings.md)).
- **Size:** weights are about 1 MB; the training recipe caps parameters at 250 k ([ADR-0006](docs/decisions/0006-equal-budget-tuning.md)).
- **Serving:** ONNX graphs run in the browser (ONNX Runtime Web) with the CQR step and the OOD check ported to JavaScript and parity-tested against Python (ADR-0015, amendment 1).

### Field models (no SOH history; [ADR-0022](docs/decisions/0022-field-deployment.md))
<!-- FIELD:START -->
- **One model per protocol** (NASA, CALCE, Toyota), because field signals are protocol-specific: the voltage windows differ (NASA/CALCE 3.85-4.15 V, Toyota 3.50-3.58 V), and a batch shift inside one dataset already breaks the signals (`reports/eda_field.md` section 5).
- **Architecture:** iTransformer, using the exact `field_final` unit recipe at seed 0, with the same tuned parameters, causal cleaning ([ADR-0018](docs/decisions/0018-outlier-policy-and-field-inputs.md)) and training-cell scaler as the benchmark. One model per task (SOH, forecast, RUL).
- **Cross-fit ensemble:** the inner-fold sub-models (3 for NASA, 3 for CALCE, 5 for Toyota) are averaged and exported as one ONNX graph per task.
- **Intervals:** per-horizon CQR (alpha = 0.1) computed from the sub-models' inner-validation predictions, so calibration never sees a demo cell.
- **OOD guard:** distance of the latest cycle's scaled channel vector from the training cycles (threshold: training 99th percentile; diagonal or Ledoit-Wolf covariance, chosen on training cells only), plus flags for missing channels and for histories shorter than the lookback. It is weak: about 6 % of Toyota test2 cycles are flagged, and on NASA it cannot be calibrated with 3 training cells (B0018 is flagged almost always). See `reports/tables/field_ood_check.md`.
- **Configuration:**

  | Protocol | Trained on | Held out (demo) | Feature set | Lookback F-A / F-B / F-C |
  |---|---|---|---|---|
  | NASA | B0005, B0006, B0007 | B0018 | `field_curve` | 64 / 64 / 64 |
  | CALCE | CS2_35, CS2_36, CS2_37 | CS2_38 | `field_curve` | 32 / 32 / 32 |
  | Toyota | official train split | test1 + test2 cells | `field` | 128 / 32 / 32 |

- **Why iTransformer for deployment, given a negative verdict:** the verdict ([ADR-0021](docs/decisions/0021-itransformer-field-verdict.md)) is about rank over all conditions, where LSTM (2.25) is ahead of iTransformer (2.33). The deploy choice weights accuracy under protocol shift, where iTransformer is best on Toyota test2 (SOH 1.55 vs at least 2.19 %SOH; h = 50 forecast 1.90 vs at least 2.20). Its intervals under-cover there (below).
<!-- FIELD:END -->

## Intended use and out of scope
**Intended use:** research and demonstration. Estimate and forecast SOH and RUL for lithium-ion cells whose cycling resembles the training protocols, and see how reliable the estimate is.

**Out of scope:**
- **Protocol-specific.** A model is valid for the protocol it was trained on. Other chemistries, charge protocols or temperatures are unsupported; the OOD guard flags many, not all, mismatches. Zero-shot transfer across chemistries fails ([ADR-0012](docs/decisions/0012-toyota-transfer.md)).
- **Not a safety system.** Do not use it for thermal-runaway detection, charge control, warranty decisions or any go/no-go decision about a battery in service.
- Fleet or pack-level prognostics, and cells with fewer than 10 cycles of history.

## Training data
- **Lab model (pooled):** NASA PCoE, CALCE CS2 and Toyota/MIT-Stanford (Severson 2019, 124 LFP cells). Held out for calibration: NASA B0018, CALCE CS2_38 and 25 of 124 Toyota cells (seeded). Ten more Toyota cells are used only for early stopping (ADR-0015).
- **Field models:** per protocol, as in the table above. Inputs are BMS-measurable only: cycle count, CV time and skip flag, resistance, log rest, charge temperature, relaxation voltage, fixed-window charge features (and 15 Q(V) points for `field_curve`). Capacity, SOH, throughput from empty, total and CC charge time and all discharge quantities are forbidden and leakage-tested (ADR-0018).
- Data and weights are not in git. Weights live on the Hugging Face model repo.

## Evaluation
All numbers are mean over 5 seeds on held-out cells. NASA and CALCE use leave-one-cell-out (4 cells each); Toyota uses the official split (test1, test2). Tables: `reports/tables/benchmark.csv` and `reports/tables/field_final.csv`; the README holds the generated copies with confidence intervals.

**Lab setting (SOH history available), SC variant:**

| | CALCE | NASA | Toyota test1 | Toyota test2 |
|---|---|---|---|---|
| SOH estimation, RMSE (%SOH) | 1.27 | 0.70 | 0.11 | 0.04 |
| Forecast h = 50, RMSE (%SOH) | 3.09 | 4.05 | 0.53 | 0.18 |
| RUL, MAE (cycles) | 73 | 15 | 97 | 140 |

**Field setting (iTransformer; age-only baseline in brackets):**

| | NASA | CALCE | Toyota test1 | Toyota test2 |
|---|---|---|---|---|
| F-A SOH RMSE (%SOH) | 4.59 (5.85) | 3.28 (6.89) | 1.06 (4.01) | 1.55 (3.67) |
| F-B forecast h = 50 RMSE (%SOH) | 5.82 (6.28) | 3.96 (7.08) | 1.26 (4.22) | 1.90 (3.77) |
| F-C RUL MAE (cycles) | 15 (34) | 51 (51) | 56 (236) | 146 (259) |

- Field signals beat age-only on Toyota and CALCE. NASA forecasting does not beat age-only reliably.
- Losing the SOH history costs 4 to 75 times in SOH error against the lab setting ([ADR-0020](docs/decisions/0020-field-benchmark.md)).
- Field verdict for iTransformer: **negative** under the pre-registered rule, with a stated borderline (ADR-0021). It ranks second of six learned models (2.33; LSTM 2.25).

## Uncertainty and calibration
- **Lab model, CQR coverage at h = 50 (target 0.90):** NASA 0.892, CALCE 0.888, Toyota test1 0.901, Toyota test2 0.980. Raw quantile heads under-cover (iTransformer SC: 0.567 on NASA).
- **Field iTransformer, CQR coverage at h = 50 and useful share** (useful = width below 50 % of the distance to 80 % SOH, [ADR-0019](docs/decisions/0019-adaptive-intervals.md)):

  | | Coverage | Width (%SOH) | Useful share |
  |---|---|---|---|
  | NASA | 0.805 | 26.74 | 0.000 |
  | CALCE | 0.905 | 14.26 | 0.007 |
  | Toyota test1 | 0.923 | 4.30 | 0.813 |
  | Toyota test2 | **0.661** | 4.12 | 0.866 |

- **Under distribution shift the intervals fail.** On Toyota test2 (a batch with a different rest, CV time and temperature) field coverage is 0.66, against 0.87 for LightGBM. Conformal coverage assumes exchangeable calibration and test cells; the shift is not in the calibration cells. The demo states this permanently; the OOD guard catches only about 6 % of these cycles.
- **On NASA and CALCE the field intervals are uninformative:** coverage is acceptable but the bands are too wide to act on. The demo marks them. Intervals are informative only on Toyota test1.
- Adaptive calibration did not narrow intervals (ADR-0019); narrowing has to come from better predictions.

## Limitations
- **Four cells** per NASA and CALCE dataset. Confidence intervals are wide by construction, and rankings there are weak evidence.
- **NASA B0005, B0006 and B0007 share one rig and rest schedule**; B0018 is the only independent NASA cell ([ADR-0004](docs/decisions/0004-evaluation-protocol.md)).
- **Regeneration is not forecastable in the field setting.** The known-future rest token and the tabular rest inputs did not reproduce the lab gain (-8.9 % against a pre-registered +26 % bar at NASA regeneration targets; [ADR-0020](docs/decisions/0020-field-benchmark.md)). Regeneration is visible in field signals when it happens.
- **CALCE charger artifact:** about 3 % of CALCE cycles have a skipped CV step that no model can forecast ([ADR-0017](docs/decisions/0017-calce-artifact-cycles.md)). A user with capacity-only data cannot detect them.
- **ElasticNet F-C diverges** on NASA and CALCE in the field benchmark (a few extreme predictions; reported, not removed). It is not the deployed model, so the deployed field models are unaffected.
- Lookbacks are 32 to 128 cycles; a cell lives 150 to 2,200 cycles, so claims about very long context cannot be tested here.
- The deployed field models are refits of benchmarked recipes at seed 0; MPS nondeterminism means they reproduce the benchmark held-out metrics only up to small differences.

## Ethical and safety notes
- A confident-looking RUL for a battery in service can be wrong in ways that matter. Treat output as a research estimate with the stated coverage, not as a guarantee. Where an interval is marked uninformative, do not use it.
- The demo runs in the browser, so uploaded data does not leave the page.
- The datasets are public research data; no personal data is involved.

## How to cite
The idea comes from the source paper; this repository is an independent, leakage-free rebuild and does not reuse its reported numbers.

> A. Jha, P. Dorkar, A. Biswas, A. Emadi, "iTransformer Network Based Approach for Accurate Remaining Useful Life Prediction in Lithium-Ion Batteries," *IEEE ITEC 2024*, doi:10.1109/ITEC60657.2024.10598898.

Datasets: NASA PCoE Battery Data Set; CALCE CS2 (University of Maryland); Severson et al., *Nature Energy* 4, 383-391 (2019).
