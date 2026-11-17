# ADR-0015: Deployment target, served model and input contract

- **Status:** Accepted (2026-11-17)

## Context
The plan's deliverable is a public demo on Hugging Face Spaces, where anyone uploads a cell's cycle log and gets a forecast plus a RUL interval. It must run on CPU Basic (2 vCPU / 16 GB) without MPS code.

## Options considered
| Question | Options | Decision and why |
|---|---|---|
| Which model to serve | MC iTransformer (needs charge-phase channels: CC/CV time, throughput, IR…) vs **SC iTransformer** (SOH history only) | **SC.** Public users rarely have consistent per-cycle charge features, and NASA, CALCE and Toyota log different ones. SC is tied with MC on most benchmark conditions, best on Toyota test2 forecasting (0.18 %SOH h50), and stays calibrated under the test2 shift (CQR PICP 0.98 vs 0.66–0.76 for LSTM/LightGBM). |
| Training data for the served weights | Toyota only; **all three datasets pooled** | **Pooled.** SC inputs (SOH, causal SOH summaries) are chemistry-agnostic, and pooling widens the operating envelope. Evaluation evidence is the benchmark (ADR-0008); the served model is a refit of a benchmarked recipe, which is standard practice. |
| Calibration set | Inner folds; **held-out cells** | **Cells never trained on:** NASA B0018 (the rig-independent cell), CALCE CS2_38, and 25 of 124 Toyota cells (seeded). Ten more Toyota cells are used for early stopping only. Calibration-set coverage is 0.90 by construction, so independent coverage evidence comes from the benchmark. |
| Weights format | ONNX (onnxruntime); TorchScript; **PyTorch state_dict on CPU** | **state_dict + torch CPU wheel.** The window builder and masking run in Python/NumPy (shared with training via `build_samples`), so an ONNX graph would only cover the network and add a second numerics path to keep in sync. Weights are 1 MB and inference takes milliseconds. ONNX remains possible later if cold start matters. |
| Where weights live | In git; **HF model repo** | **HF model repo** `anurag6557/battery-rul-itransformer-v2`. CLAUDE.md forbids weights in git; the Space downloads them at start-up. |
| Out-of-distribution guard | None; **Mahalanobis on causal SOH summaries + range checks** | A banner appears when any of the following is outside the training envelope: the Mahalanobis distance (vs the 99th percentile of training), SOH ∉ [0.3, 1.3], the recent fade rate (0.5–99.5 % of training), or history shorter than the lookback. Conformal coverage assumes exchangeability (ADR-0011's test2 finding), so this is the honest signal. |

## Input contract
- **Columns:** a CSV with `cycle_idx` and `capacity_ah`, one row per cycle, at least 10 cycles; extra columns are ignored.
- **SOH definition:** capacity / mean(first 5 cycles), identical to training.
- **Validation:** errors are reported in plain language (`serve.predictor.InputError`).
- **Outputs:**
  - SOH forecast at h ∈ {1, 10, 25, 50, 100} with a 90 % CQR interval;
  - RUL to 80 % SOH with a 90 % CQR interval and the predicted EOL cycle;
  - the OOD report.

## Reproduction
1. `scripts/train_deploy.py` trains the served weights and writes `artifacts/deploy/` (seeded; under 1 min on MPS).
2. `scripts/push_to_hub.py --weights | --space` publishes the weights and the app.
3. `.github/workflows/deploy-space.yml` republishes the Space on `v*` tags (`HF_TOKEN` repository secret).

## Amendment 1 (2026-11-17): static, in-browser Space
- **What happened:** creating the Gradio Space failed with HTTP 402. Hugging Face now requires a PRO subscription to host Gradio and Docker Spaces on free CPU; only static Spaces are free.
- **Options considered:**
  1. HF PRO ($9/month). Rejected by the owner because of the recurring cost.
  2. Streamlit Community Cloud. The app sleeps when idle, and the UI would need porting.
  3. **A static Space with ONNX Runtime Web.** Chosen by the owner.
- **Change from the original decision:** the "state_dict, no ONNX" row above is reversed **for the public demo only**.
- **How the static Space works:**
  - `scripts/export_onnx.py` folds the model-side transforms into each graph: tab standardisation, the residual-to-SOH step and RUL scaling, and quantile sorting.
  - The browser therefore only builds the SOH window and the five causal summaries (`web/core.mjs`), then applies CQR and the OOD check exactly as `serve/predictor.py` does.
- **Parity, checked by tests:**
  - ONNX vs PyTorch: max |Δ| is 5e-8 SOH (forecast) and 3e-4 cycles (RUL). The export script enforces this.
  - JS vs Python predictor: identical windows, summaries, intervals, RUL and OOD on the three demo cells. `node tests/web/test_core.mjs` runs in CI.
- **Consequences:**
  - Uploaded data never leaves the user's browser, there are no cold starts, and hosting is free.
  - The Gradio app (`app/`) remains for local use (`make app`).
- **Live:**
  - Demo: https://huggingface.co/spaces/anurag6557/battery-rul-itransformer-v2. The `?demo=<cell>` URL runs a demo directly.
  - Weights and ONNX: https://huggingface.co/anurag6557/battery-rul-itransformer-v2.
