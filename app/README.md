---
title: Battery RUL — iTransformer-v2
emoji: 🔋
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 6.32.0
app_file: app.py
pinned: false
license: mit
short_description: Li-ion SOH forecast and RUL with calibrated 90% intervals
---

# Battery RUL — iTransformer-v2

Upload a cell's per-cycle discharge capacity (`cycle_idx`, `capacity_ah`) and get a
multi-horizon state-of-health forecast and a remaining-useful-life (to 80% SOH) estimate,
both with conformalized 90% intervals, plus a warning when the input looks unlike the
training cells. Or pick a demo cell that the model never trained on.

- Code, benchmark and model card: https://github.com/anuragjha6557/battery-rul-transformers
- Weights: https://huggingface.co/anurag6557/battery-rul-itransformer-v2
- Paper: Jha et al., ITEC 2024, https://doi.org/10.1109/ITEC60657.2024.10598898

Research demo; intervals are only calibrated for cells resembling the training data
(NASA, CALCE, Toyota/MIT-Stanford).

## Field mode (static Space only)

The static Space (`web/`) also has a **Field** mode that needs no capacity log: upload per-cycle
BMS signals (`cycle_idx` plus the columns of one protocol: NASA, CALCE or Toyota/MIT) and get a
SOH estimate, a forecast and RUL with 90 % intervals, computed in your browser. Field models are
protocol-specific; under batch shift (Toyota test 2) interval coverage fell to 0.66 and the
out-of-distribution guard flags only ~6 % of those cycles. NASA/CALCE intervals are usually
uninformative. See ADR-0022 in the GitHub repository. This Gradio app is unchanged (lab mode).
