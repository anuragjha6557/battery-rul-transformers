# Project status

_Last updated: 2026-11-15 (Opus 5.5 lead)_

## State
- **Phase 0 complete** (`8020ca4`): uv/Python 3.12 env (torch 2.15 + MPS, lightgbm 4.7, mlflow 3.18, optuna 5.0, gradio 6.32, pandera 0.36), package skeleton, typer CLI, Makefile, pre-commit, GitHub Actions CI, data contract (`data/schema.py`, `data/io.py`), checksummed downloader, ADR-0001..0003. Local gate green.
  - Outstanding for the gate: **CI not yet run on GitHub** — needs the owner to run `! brew install gh && gh auth login`, then the lead creates `anuragjha/battery-rul` and pushes. **ADR-0007 pending** — `scripts/bench_cpu_vs_mps.py` must be re-run on an idle machine (first run overlapped with loader agents).
- **Phase 1 in progress**
  - NASA loader merged (`b574ccc`): 4 cells, 636 cycles, 2.08 M curve rows, build ≈ 5.5 s; 11 unit + 5 real-data tests.
  - CALCE loader: Sonnet agent running in a worktree (data extracted at `data/raw/calce/CS2_3x/`, checksums pinned).
  - Toyota loader: waiting for batch 1 `.mat` to finish downloading (headless download works — no manual step needed); agent launches when it lands.
- Data on disk: NASA ✓, CALCE ✓, Toyota downloading (~1–1.5 MB/s, 3 files).

## Findings to carry forward (Phase 2 data-quality report / Phase 3 protocol)
1. **B0005/06/07 were cycled on one rig with identical timestamps** (same rest schedule). Regeneration jumps co-occur at the same cycles (e.g. 20, 31, 48 after rests > 1e5 s; cycle 90 has no paired charge on all three). → LOCO among these three is **not independent on the time axis**; time/rest-derived features carry shared exogenous information. PROTOCOL.md / ADR-0004 must address this (options: report B0018 as the only fully independent NASA test cell; treat rest schedule as known exogenous input vs unknown future; or group-split). Strong interview point.
2. NASA discharge records stop above the cut-off voltage (median last V ≈ 3.3–3.5 V); `Capacity` is consistent with ∫|I|dt (≤ 1.7 %), but discharge_time/energy are from truncated records.
3. NASA cycle 1 charge is a short top-up (≈ 0.008 Ah); cycle 31 (B0005/6/7) and 56/46 (B0018) are partial charges; first 1–3 charge samples have a current spike (−4 A). Decide flag/exclude rules in ADR-0005.
4. NASA SOH min: B0005 0.699, B0006 0.572, B0007 0.744, B0018 0.729 → at the 70 % threshold B0007 and B0018 are **censored**; at 80 % all four cross.
5. CALCE: file order must come from first `Date_Time` (filenames sort wrong; filename date ≠ session start). No temperature channel; `Internal_Resistance(Ohm)` is logged.

## Next actions
1. Review/merge CALCE loader; wire `build-data calce` in `cli.py`.
2. Launch Toyota loader agent when batch 1 is complete; wire `build-data toyota`.
3. Re-run `scripts/bench_cpu_vs_mps.py` on an idle machine → ADR-0007.
4. Phase 1 gate: `make data` builds all three; schema tests pass; counts NASA 4, CALCE 4, Toyota ≈ 124.
5. Phase 2: EDA + `reports/data_quality.md` + ADR-0005 (EOL rule, SOH normalization, anomaly flags).

## Open risks
- HF free tier availability at deploy time (re-check in Phase 8 day 1; fallback Streamlit Community Cloud).

## Phase log
| Phase | Status | Gate evidence |
|---|---|---|
| 0 Bootstrap | done locally; CI-on-GitHub + ADR-0007 pending | `make lint test typecheck` green (`8020ca4`) |
| 1 Data | in progress (NASA ✓, CALCE running, Toyota queued) | NASA: 168/168/168/132 cycles |
| 2 EDA | not started | |
| 3 Eval harness | not started | |
| 4 Baselines | not started | |
| 5 iTransformer/PatchTST | not started | |
| 6 Improvements | not started | |
| 7 Final benchmark | not started | |
| 8 Deployment | not started | |
| 9 Docs | not started | |
