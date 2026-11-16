# battery-rul — project instructions for Claude

## What this is
End-to-end ML project rebuilding and significantly improving the owner's IEEE ITEC 2024 paper
(*iTransformer Network Based Approach for Accurate RUL Prediction in Li-ion Batteries*, Jha et al.)
as a rigorous, leakage-free **battery prognostics benchmark + one new method (iTransformer-v2)**,
deployed publicly on Hugging Face Spaces. The owner is the paper's first author.

**The full plan is the contract: `docs/PLAN.md`. Read it completely before doing anything.**
Current state and next action: `docs/STATUS.md`. Decisions: `docs/decisions/` (ADRs).

## Non-negotiables (from the owner)
- Do **not** try to reproduce the paper's reported numbers; the owner says they may be wrong and must not be trusted. The paper supplies the *idea*, not the baseline. Honest negative results are expected and reported.
- Everything runs on this laptop (Apple M4 Pro, 12 cores, 24 GB). No cloud training.
- Keep NASA + CALCE datasets; add Toyota/MIT-Stanford (Severson 2019). No further datasets.
- Every non-trivial choice gets a one-page ADR in `docs/decisions/NNNN-title.md` (Context / Options / Decision / Evidence). The project must be defensible in interviews.
- Final deliverables: public GitHub repo with green CI, installable package, HF Space demo, README with auto-generated results tables, model card.

## Environment
- Python **3.12** via `uv` (`~/.local/bin/uv`). System Homebrew Python is 3.14 — do not use it.
- PyTorch **MPS-first for neural models** (measured, ADR-0007: 4 concurrent MPS worker processes for sweeps; one MPS process for Toyota pre-training); classical models (LightGBM/GPR/sklearn) run on the remaining CPU cores concurrently. CI and the HF Space are CPU-only — never put MPS-specific code in the serving path; use `battery_rul.utils.resolve_device("auto")`.
- MLflow local (`sqlite:///mlflow.db`, `mlruns/` gitignored). Hydra configs under `configs/`.
- `git` present; `gh` CLI is **not installed** — ask the owner to run `! brew install gh && gh auth login` when a GitHub action is needed. No Docker.
- Raw data lives in `data/raw/` (gitignored, checksummed by `src/battery_rul/data/download.py`). Toyota's download page is JS-rendered; if headless download fails, ask the owner to download the three `.mat` batches into `data/raw/toyota/` once.
- Scratch files go in the session scratchpad, not the repo.

## Hard-won rules (do not relearn these)
- **OpenMP isolation (macOS):** torch and LightGBM load different `libomp` copies that cannot share a process in either import order. Never import `lightgbm` or `torch` at module top-level outside their model modules. Model classes load lazily via `models/registry.py`, which records each model's OpenMP family, and the runner isolates mixed experiments in per-unit worker processes. LightGBM tests live in `tests/lgbm/` and run in a separate pytest process (`make test` does both). Linux CI is unaffected, so a green CI does not prove macOS is fine.
- **Gate exit codes:** run gates as `set -o pipefail; make lint test typecheck ...`, or check `$?` before committing. A `| grep` once hid a failing gate and a broken commit was pushed.
- **No merges into `main` while a tuning sweep or benchmark is running.** Each study is a long-lived process that lazily imports modules at the end (MLflow logging), so a mid-run merge mixes old in-memory and new on-disk code (`patchtst__forecast` crashed with an ImportError this way). Commit agent work on its branch and merge after the run. `battery-rul tune --n-trials 0` finalizes a study from its journal without adding trials.
- **Worktrees:** don't `git worktree remove` an agent's worktree until its final hand-back message has arrived; an agent may still be finishing.

## Workflow rules
- Work phase by phase per `docs/PLAN.md §7`; do not start a phase before the previous gate passes. Update `docs/STATUS.md` at every gate and after every merged wave.
- `make lint test` must pass before every commit. Commit messages: conventional (`feat(data): …`, `test(eval): …`, `docs(adr): …`). Branch per phase (`phase-1-data`), squash-merge to `main`. Never commit data, `mlruns/`, weights, or notebooks with outputs.
- Every experiment is a config file; every reported number maps to an MLflow run ID. Results tables in README are generated, never hand-edited.
- Leakage rules (PLAN §6.2) are enforced by unit tests in `tests/test_leakage.py`; any change to features/splits/tasks must keep them green.
- Ask the owner only at gates marked "owner" in the plan, or if a Fixed Decision (PLAN §2) looks wrong. Otherwise decide, record the reasoning in an ADR, and proceed.

## Subagent delegation (lead = Opus 5.5)
Apply the rubric in PLAN §9 to every task:
1. No precise spec yet (interface + acceptance tests + file paths)? → the lead writes the spec first.
2. Correctness hinges on subtle judgment (leakage, labels, statistics, architecture fidelity, interpreting ambiguous results)? → Opus.
3. Otherwise → **Sonnet 5.5** (`model: "sonnet"`), `effort: "lower"` for mechanical work (loaders from a schema, plots, tests, docs, YAML, CI, Gradio UI, running sweeps and tabulating).

Run independent tasks as **parallel waves of 3–4 agents** with `isolation: "worktree"`; the lead merges, runs `make lint test`, commits. Agents never commit. Every delegation prompt includes: goal, exact files to create/modify (and off-limits files), interface contract, acceptance tests, constraints (Python 3.12, no new deps without listing them, no network except dataset URLs), and "return: summary + test output + open questions".
Long benchmark runs are started by the lead with `run_in_background`, not by subagents.

## Code conventions
`src/` layout (`src/battery_rul/…`, see PLAN §4); ruff lint+format; mypy (lenient) on `src/`; pytest with synthetic fixtures only in CI (`@pytest.mark.data` for real-data checks, skipped in CI); every model implements the `Model` protocol in `models/base.py`; one `seed_everything()`; type hints everywhere; docstrings state units (Ah, %SOH, cycles).
