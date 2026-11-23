# ADR-0022: Field-mode deployment (no SOH history)

- **Status:** Accepted (2026-11-23)
- **Context:** PLAN_PHASE2 Stage 4. The public demo (ADR-0015) serves the lab-setting model, which needs a measured capacity log. A real BMS has field signals instead: charge-side quantities, rest, resistance, temperature and cycle count (ADR-0018). ADR-0020/0021 show what those signals support. Field SOH estimation beats age-only on Toyota and CALCE. Forecasting is useful in-distribution on Toyota only. Intervals are informative on Toyota test1, not on NASA/CALCE.

## Options
1. **Keep only the lab demo.** Simple, but it would not show the field result, which is the point of Phase 2.
2. **One pooled field model for all three datasets.** Rejected. Field signals are protocol-specific: the voltage windows differ (NASA/CALCE 3.85–4.15 V, Toyota 3.50–3.58 V), and a batch shift inside one dataset already breaks the signals (EDA §5). A pooled model would hide that.
3. **One field model per protocol (NASA, CALCE, Toyota), chosen.** The user picks the protocol their data follows.

**Model family:** iTransformer (chosen) vs LightGBM vs LSTM.
- iTransformer is the most accurate model under the Toyota batch shift: F-A 1.55 vs ≥ 2.19 % SOH, F-B 1.90 vs ≥ 2.20, significant against every competitor. A deployed model meets unseen protocols and conditions, so this is the property that matters most.
- It is also the best NASA RUL model, and the ONNX/browser path already exists for it.
- LightGBM keeps better coverage under shift (0.87 vs 0.66). However, its intervals are wider, and a browser port would need a new ONNX converter dependency.
- LSTM has the best in-distribution mean rank (ADR-0021), by 0.08 over iTransformer, a gap inside the noise.
- This is a deployment criterion, not a reversal of ADR-0021. The verdict concerns rank over all conditions; the deploy choice weights robustness to shift.

## Decision
- **Lab mode** (capacity log, `itransformer_sc`, ADR-0015) stays unchanged.
- **Field mode:** for each protocol, the exact `field_final` iTransformer unit recipe, seed 0, on the fold whose held-out cells are the demo cells.

  | Protocol | Trained on | Held out (demo) | Feature set | Lookback F-A / F-B / F-C |
  |---|---|---|---|---|
  | NASA | B0005, B0006, B0007 | B0018 | `field_curve` | 64 / 64 / 64 |
  | CALCE | CS2_35, CS2_36, CS2_37 | CS2_38 | `field_curve` | 32 / 32 / 32 |
  | Toyota | official train split | test1 + test2 cells | `field` | 128 / 32 / 32 |

  - Same tuned parameters, ADR-0018 cleaning and training-cell scaler as the benchmark.
  - The cross-fit sub-models (3 / 3 / 5) are averaged, as in the benchmark, and exported as one ONNX graph per task.
- **Intervals:** per-horizon CQR (α = 0.1) from the sub-models' inner-validation predictions, the same rule as `battery-rul calibrate`. Calibration therefore never sees a demo cell.
- **Input contract:** CSV with `cycle_idx` plus the protocol's raw field signals. The required columns are the model's channels before derivation. Optional `charge_time_s` is used only by the charge-pause rule; it is never a model input. The ADR-0018 causal input rules (physical ranges, charge pause, robust z) run on the upload exactly as in training. Label rules cannot run, because there is no capacity.
- **OOD guard:**
  - Mahalanobis distance of the latest cycle's scaled channel vector against the training cycles (threshold: training 99th percentile).
  - A flag for missing or all-empty channels and for histories shorter than the lookback.
  - The page states the measured coverage under batch shift (Toyota test2 0.66) and the informativeness of each interval (useful = width < 50 % of the distance to 80 % SOH; ADR-0019).
- **Artifacts:**
  - `scripts/train_deploy_field.py` writes `artifacts/deploy_field/<protocol>/`: `{soh,forecast,rul}.pt` and `field_meta.json` (channels, scaler, lookbacks, horizons, CQR corrections, OOD statistics, cells, provenance).
  - Python serving: `battery_rul.serve.field.FieldPredictor`. Browser: `web/field.mjs`, parity-tested against Python vectors.
  - Weights are uploaded to the existing HF model repo under `field/` and are never committed.

## Evidence
- ADR-0020 Stage 3 outcome and ADR-0021: the accuracy and interval tables cited above.
- The deployed field models reproduce the `field_final` seed-0 held-out metrics for their demo cells, up to MPS nondeterminism. This check is reported by `train_deploy_field.py`.

## Consequences
- Each field model is valid only for its protocol. The UI says so, and the OOD guard flags mismatches.
- NASA and CALCE field forecasts are shown with "uninformative interval" marks. This is the honest state of the field setting at 4 cells per dataset.
