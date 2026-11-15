# Project status

_Last updated: 2026-11-15 (planning session, Fable 5.1)_

## State
- Plan approved by the owner: `docs/PLAN.md` (sections 1–3 are fixed decisions).
- Repo initialized (`git init`, branch `main`), nothing implemented yet. No `pyproject.toml`, no code, no data.
- Paper + extracted text in `docs/paper/`. Swift PDF text extractor in `scripts/pdftext.swift` (no PDF Python libs are installed system-wide).
- Verified 2026-11-15: HF Spaces free CPU Basic (2 vCPU / 16 GB) is listed on huggingface.co/pricing; NASA zip URL `https://phm-datasets.s3.amazonaws.com/NASA/5.+Battery+Data+Set.zip`; CALCE at `https://web.calce.umd.edu/batteries/data/`; Toyota at `https://data.matr.io/1/projects/5c48dd2bc625d700019f3204` (JS page).
- Laptop: Apple M4 Pro, 12 cores, 24 GB, macOS 26.6, 272 GB free. `uv` installed; Homebrew Python 3.14 (do not use); `mlx` present; no torch, no `gh`, no Docker.

## Next action → Phase 0 (Bootstrap), PLAN §7
1. Ask the owner to run `! brew install gh && gh auth login` (needed to create the public GitHub repo `anuragjha/battery-rul`).
2. `uv init` (Python 3.12, src layout, package name `battery_rul`), add dependencies listed in PLAN §7 Phase 0, Makefile, pre-commit, CI workflow, repo skeleton from PLAN §4.
3. `scripts/bench_cpu_vs_mps.py` → ADR-0007.
4. ADR-0001 (record decisions), ADR-0002 (toolchain), ADR-0003 (Hydra config system).
5. Gate: CI green; `uv run battery-rul --help` works. Then update this file and move to Phase 1.

## Open risks
- Toyota download may need a manual browser step.
- HF free tier availability at deploy time (re-check in Phase 8 day 1; fallback Streamlit Community Cloud).

## Phase log
| Phase | Status | Gate evidence |
|---|---|---|
| 0 Bootstrap | not started | |
| 1 Data | not started | |
| 2 EDA | not started | |
| 3 Eval harness | not started | |
| 4 Baselines | not started | |
| 5 iTransformer/PatchTST | not started | |
| 6 Improvements | not started | |
| 7 Final benchmark | not started | |
| 8 Deployment | not started | |
| 9 Docs | not started | |
