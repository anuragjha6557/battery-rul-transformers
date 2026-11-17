---
title: Battery RUL Forecaster
emoji: 🔋
colorFrom: blue
colorTo: yellow
sdk: static
app_file: index.html
pinned: false
license: mit
short_description: Battery SOH forecast + RUL with calibrated 90% intervals
---

# Battery RUL Forecaster (iTransformer-v2)

Upload a battery's per-cycle capacity log (`cycle_idx, capacity_ah`), or pick a demo cell the model never trained on. The page returns:
- a state-of-health forecast 1–100 cycles ahead;
- the remaining useful life to 80 % SOH;
- conformal (CQR) 90 % intervals for both;
- a warning when the input is outside the training distribution.

The model runs entirely in your browser (ONNX Runtime Web), so uploaded data never leaves the page.

- Code, benchmark, design decisions and limitations: https://github.com/anuragjha6557/battery-rul-transformers
- Weights: https://huggingface.co/anurag6557/battery-rul-itransformer-v2
- Paper: Jha et al., IEEE ITEC 2024, doi:10.1109/ITEC60657.2024.10598898
