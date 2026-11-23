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

## Field mode (no capacity log)

A **Field: BMS signals** switch (shown only when the Space ships `field/<protocol>/*`) runs the
ADR-0022 field models: SOH estimate now, SOH forecast (hatched where the 90 % interval is
uninformative) and RUL, from charge-side BMS signals only. One model per protocol, chosen by the
user: `nasa`, `calce`, `toyota` (they are **not interchangeable**).

Input contract: a CSV with one row per cycle, a required `cycle_idx` and the protocol's raw signal
columns (listed on the page; blank values are allowed, a missing column is treated as unobserved
and flagged). Optional `charge_time_s` only feeds the charge-pause cleaning rule. Other columns
(e.g. the demo files' `soh_measured`, drawn for comparison only) are ignored. At least 5 cycles; the
ADR-0018 causal input cleaning runs in the browser exactly as in training, and its counts are shown.

Caveats shown permanently on the page: protocol specificity; Toyota test 2 batch shift (held-out
coverage 0.66, OOD guard flags only ~6 % of those cycles); NASA/CALCE intervals are usually
uninformative (4 training cells).

Files: `field.mjs` (pure port of `serve/field.py` + `data/cleaning.py`), `field_app.mjs` (UI),
`field/<protocol>/{soh,forecast,rul}.onnx` + `field_serve_meta.json`
(`scripts/export_onnx_field.py`, each graph averages all cross-fit members). Demo uploads:
`examples/field/*.csv` + `demos.json` (`scripts/make_field_examples.py`, held-out cells only).
Tests: `node tests/web/test_field.mjs` (hist/tab within 1e-5 and final outputs within 1e-6 of the
Python `FieldPredictor`, from `tests/web/field_vectors.json`).
