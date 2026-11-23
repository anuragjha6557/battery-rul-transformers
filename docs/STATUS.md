# Project status

_Last updated: 2026-11-23 (Opus 5.5 lead)_

## State
- **Phase 2 (field setting, `docs/PLAN_PHASE2.md`): complete (2026-11-23).** Stage 4 delivered: field-mode demo live on the Space (ADR-0022; per-protocol iTransformer, reproduces `field_final` held-out metrics, JS port parity-tested), showcase field section, trajectories field mode with informativeness badges, README field results, MODEL_CARD.md, interview notes, CONTRIBUTING, architecture. Weights (lab + `field/`) on the HF model repo.
  - Stage 0: ADR-0018 (outliers, field inputs), ADR-0019 (intervals), `reports/eda_field.md`.
  - Stage 1–3: ADR-0020. `field_screen` 378 runs, `field_lookback` 360, `field_final` 990, `field_regen` 200; 0 failures.
  - Field signals beat age-only on Toyota and CALCE; on NASA forecasting no model does reliably.
  - Many variates help iTransformer on CALCE only (H1 chemistry-conditional); long lookbacks do not help (H2 not supported); the rest-schedule token does not forecast regeneration (H3 not supported, −8.9 % vs bar +26 %).
  - **ADR-0021 verdict: negative** (borderline: mixed if CI and Holm p must both hold). Mean rank LSTM 2.25, iTransformer 2.33, LightGBM 3.08. iTransformer is the most accurate under the Toyota test2 batch shift and the best NASA RUL model, but its intervals under-cover under shift (0.66).
  - Intervals: informative on Toyota test1 (80–86 % useful at h50); not on NASA/CALCE (≤ 10 %).
- **Phases 0–8 complete.** Live demo: https://huggingface.co/spaces/anurag6557/battery-rul-itransformer-v2. It is a static in-browser Space (ADR-0015 amendment 1) because Gradio hosting needs HF PRO.
- **Phase 4/5 (ADR-0008):**
  - Benchmark: 1 620 runs, 0 failures, plus `benchmark_local` (72 runs). Tuned with 50 Optuna trials per (model, task) on Toyota (ADR-0006, amendments 1–3).
  - Mean rank: iTransformer 3.08, iTransformer-SC 3.95, LightGBM 4.55, PatchTST 4.65.
  - The ranking depends on the dataset: iTransformer leads in-distribution (Toyota); LightGBM/ElasticNet lead on NASA/CALCE.
- **Phase 6 ablations:** all outcomes recorded, and every proposed change was rejected under PLAN §6.5.
  - ADR-0010: direct heads beat recursive rollout.
  - ADR-0013: RevIN and Huber not adopted; the quantile head beats a point MSE head on Toyota.
  - ADR-0009: `mc_curve` features not adopted; LightGBM gains only on Toyota.
  - ADR-0012: Toyota pre-training plus full fine-tuning gives −28 % h50 on NASA but is worse on CALCE, so it is not the default.
  - ADR-0011: CQR is the primary UQ method (30/40 h50 conditions in the target band; ensemble+CQR 32/40). Toyota test2 under-covers under shift.
- **iTransformer-v2 (Phase 6 gate):** iTransformer MC with `mc` features, direct multi-horizon quantile heads (pinball loss), train-set scaling and CQR calibration, with no pre-training. The contribution is the protocol, calibrated UQ and honest transfer analysis, not a new architecture.
- **Tools added:**
  - `scripts/compare_arms.py`: paired arm comparison.
  - `scripts/uq_ensemble.py`: ensemble UQ arm.
  - The report now splits ablation arms (`with_arm_labels`).

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
1. Add the `HF_TOKEN` repository secret on GitHub so `deploy-space.yml` can republish on `v*` tags (optional).
2. Push `main` to GitHub and check CI (the field node test was added to CI).
3. Optional: live field model in the trajectories page (`LIVE_FIELD` hook in `web/traj.mjs`; needs signal columns in `traj_field`).
4. **Owner reminder:** re-enable sleep with `sudo pmset -a disablesleep 0`.

## Open risks
- HF free tier availability at deploy time (re-check in Phase 8 day 1; fallback Streamlit Community Cloud).

## Phase log
| Phase | Status | Gate evidence |
|---|---|---|
| 0 Bootstrap | done | CI green on GitHub (run 43755416295); ADR-0007 measured |
| 1 Data | done |  NASA 168/168/168/132; CALCE 880/970/1036/1025 cycles |
| 2 EDA | not started | |
| 3 Eval harness | not started | |
| 4 Baselines | not started | |
| 5 iTransformer/PatchTST | not started | |
| 6 Improvements | not started | |
| 7 Final benchmark | not started | |
| 8 Deployment | not started | |
| 9 Docs | not started | |
| 2–3 EDA, protocol, harness | done | `reports/data_quality.md`; PROTOCOL v1.1; leakage tests mutation-checked |
| 4–5 Baselines, iTransformer, PatchTST | done | ADR-0008; `reports/tables/benchmark*` |
| 6 Improvements | done | ADR-0009–0013 outcomes (incl. RUL transfer, ADR-0012 amendment 1); v2 config frozen |
| 7 Final benchmark and report | done | ADR-0014; `configs/experiment/final.yaml` ≡ benchmark; README results generated |
| 8 Deployment | done: live static Space + HF model repo | ADR-0015; `app/`, `serve/predictor.py`, 430 + 13 tests green |
