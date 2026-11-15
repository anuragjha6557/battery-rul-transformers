# Project status

_Last updated: 2026-11-15 (Opus 5.5 lead)_

## State
- **Phase 0 complete** (`8020ca4`): uv/Python 3.12 env (torch 2.15 + MPS, lightgbm 4.7, mlflow 3.18, optuna 5.0, gradio 6.32, pandera 0.36), package skeleton, typer CLI, Makefile, pre-commit, GitHub Actions CI, data contract (`data/schema.py`, `data/io.py`), checksummed downloader, ADR-0001..0003. Local gate green.
  - GitHub: public repo `anuragjha6557/battery-rul-transformers` (paper PDF stripped from history before first push; cited by DOI). ADR-0007 done (`8b1d038`): measured MPS-first for neural models.
- **Phase 1 in progress**
  - NASA loader merged (`b574ccc`): 4 cells, 636 cycles, 2.08 M curve rows, build ≈ 5.5 s; 11 unit + 5 real-data tests.
  - CALCE loader merged (`fe825f4`): 4 cells, 3 911 cycles (880/970/1036/1025), 1.07 M curve rows, build ≈ 30 s (python-calamine); 22 unit + 5 real-data tests. Lead review fix: `ir_ohm` restricted to the charge window (leakage).
  - `battery-rul build-data all` builds NASA + CALCE (`44af569`).
  - Toyota loader merged (`dd3b70a`): 124 cells (41/43/40 official split), 100 456 cycles, 10.0 M curve rows; Severson cleaning verified step by step against the raw data.
  - **Phase 1 gate passed:** `battery-rul build-data all` builds all three datasets in 65 s, peak RSS 5.3 GB; 133 unit tests + real-data tests green.
- Data on disk: NASA ✓, CALCE ✓, Toyota ✓ (46/48/46 raw cells).
- **Phase 2 done** (`b0db219`, ADR-0005 `40c95ad` + amendment `a66fe54`): `reports/data_quality.md`; EOL = masked+sustained(5) for NASA/CALCE, provider cycle life for Toyota; fixed starts NASA {30,50}, CALCE {200,400}, Toyota {100}. TODO: add Toyota to the data-quality report; flag 45 pause-inflated Toyota charge_time_s cycles (>4000 s).
- **Phase 3 started early:** PROTOCOL.md v1.0 + ADR-0004/0006 committed (`26d2866`) — **owner review gate**; Model contract + persistence baselines (`eace9b0`); metrics/stats/splits merged (`97b9515`); EOL labels + leakage-safe sample builder + executable leakage tests (`39e7bba`, mutation-checked: 3 injected leaks all caught); shared NeuralModel trainer (`083596b`). Runner + MLflow + report: Sonnet agent running.
- **Phase 4 started (wave 1, 3 Sonnet agents in parallel):** classical extrapolators (PrevSOH, linear/exp2/power fits, GPR); tabular (ElasticNet, LightGBM + quantiles, Severson feature reproduction); neural (NLinear/DLinear/RLinear, LSTM/GRU, time-token Transformer). Search spaces fixed by the lead in `configs/model/*.yaml` before any sweep (ADR-0006).

## Findings to carry forward (Phase 2 data-quality report / Phase 3 protocol)
1. **B0005/06/07 were cycled on one rig with identical timestamps** (same rest schedule). Regeneration jumps co-occur at the same cycles (e.g. 20, 31, 48 after rests > 1e5 s; cycle 90 has no paired charge on all three). → LOCO among these three is **not independent on the time axis**; time/rest-derived features carry shared exogenous information. PROTOCOL.md / ADR-0004 must address this (options: report B0018 as the only fully independent NASA test cell; treat rest schedule as known exogenous input vs unknown future; or group-split). Strong interview point.
2. NASA discharge records stop above the cut-off voltage (median last V ≈ 3.3–3.5 V); `Capacity` is consistent with ∫|I|dt (≤ 1.7 %), but discharge_time/energy are from truncated records.
3. NASA cycle 1 charge is a short top-up (≈ 0.008 Ah); cycle 31 (B0005/6/7) and 56/46 (B0018) are partial charges; first 1–3 charge samples have a current spike (−4 A). Decide flag/exclude rules in ADR-0005.
4. NASA SOH min: B0005 0.699, B0006 0.572, B0007 0.744, B0018 0.729 → at the 70 % threshold B0007 and B0018 are **censored**; at 80 % all four cross.
5. CALCE: file order must come from first `Date_Time` (filenames sort wrong; filename date ≠ session start). No temperature channel; `Internal_Resistance(Ohm)` is logged. Duplicate workbooks (`CS2_35_2_4_11` = `2_10_11`, same for CS2_38) dropped.
6. **CALCE "regeneration" is mostly an equipment artifact.** In ~3 % of cycles (25–31 per cell) the Arbin CV step ends after one sample → discharge delivers 0.13–0.16 Ah less. Flag: `cv_time_s < 300 s`. These dips dominate cycle-to-cycle jumps; real session-boundary recovery is small (+0.006–0.012 Ah mean). Consequence: raw first-crossing of 80 % SOH is cycle 69–311 vs 501–603 with an 11-cycle rolling median → **the EOL rule (ADR-0005) changes CALCE RUL labels by hundreds of cycles.** The paper never mentions this. Strong interview point.
7. CALCE cells were cycled far past EOL (min SOH 0.12–0.22); 80 % SOH ≈ cycles 500–600, 70 % ≈ 650–800 (smoothed).
8. **Feature-availability rule (enforce in `tasks/` + leakage tests):** per-cycle quantities measured during discharge k (`discharge_time_s`, `discharge_energy_wh`, `discharge_temp_max_c`, discharge curves) are ≈ the target `capacity_k` itself. For Task A (estimate SOH_k) only charge-phase features of cycle k (+ history < k) are allowed; for Tasks B/C anything at cycles ≤ T_p. CALCE `ir_ohm` was changed in review to use the charge window only for this reason (NASA `ir_ohm` already uses the latest EIS *before* the charge).

## Next actions
1. ~~Review/merge CALCE loader~~ done.
2. Launch Toyota loader agent when batch 1 is complete; wire `build-data toyota`.
3. Re-run `scripts/bench_cpu_vs_mps.py` on an idle machine → ADR-0007.
4. Phase 1 gate: `make data` builds all three; schema tests pass; counts NASA 4, CALCE 4, Toyota ≈ 124.
5. Phase 2: EDA + `reports/data_quality.md` + ADR-0005 (EOL rule, SOH normalization, anomaly flags).

## Open risks
- HF free tier availability at deploy time (re-check in Phase 8 day 1; fallback Streamlit Community Cloud).

## Phase log
| Phase | Status | Gate evidence |
|---|---|---|
| 0 Bootstrap | done | CI green on GitHub (run 43755416295); ADR-0007 measured |
| 1 Data | in progress (NASA ✓, CALCE ✓, Toyota queued) | NASA 168/168/168/132; CALCE 880/970/1036/1025 cycles |
| 2 EDA | not started | |
| 3 Eval harness | not started | |
| 4 Baselines | not started | |
| 5 iTransformer/PatchTST | not started | |
| 6 Improvements | not started | |
| 7 Final benchmark | not started | |
| 8 Deployment | not started | |
| 9 Docs | not started | |
