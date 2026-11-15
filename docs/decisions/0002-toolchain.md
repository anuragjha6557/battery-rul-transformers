# ADR-0002: Toolchain — uv, Python 3.12, PyTorch, MLflow, ruff/mypy/pytest

- **Status:** Accepted
- **Date:** 2026-11-15

## Context
Everything has to run on one Apple M4 Pro laptop (12 cores, 24 GB), be reproducible from a fresh clone, run in GitHub Actions on Linux, and deploy to a CPU-only Hugging Face Space. The machine's default Python (Homebrew) is 3.14.

## Options considered
| Concern | Options | Chosen | Why |
|---|---|---|---|
| Env/deps | pip+venv, conda, poetry, **uv** | uv | Lockfile (`uv.lock`) for exact reproducibility, per-platform index routing (CPU torch on Linux), and roughly 10–100× faster resolves. `uv` was already installed on the laptop. |
| Python | 3.14 (system), 3.13, **3.12** | 3.12 | 3.14 wheels were still preview-quality for parts of the scientific stack when the plan was made. 3.12 is supported by every dependency and by HF Spaces. |
| DL framework | PyTorch, JAX, MLX | PyTorch | iTransformer/PatchTST reference implementations are in PyTorch, ONNX export is mature, and interviewers expect it. MLX is Apple-only, which breaks CI and Spaces. |
| Tracking | **MLflow (local SQLite)**, W&B, CSV | MLflow | No account needed (the owner's choice). Run IDs give every reported number provenance. |
| Lint/format | flake8+black+isort, **ruff** | ruff | One tool and fast. Rules: E, F, W, I, B, UP, N, SIM, NPY, PD, RUF. |
| Types | none, **mypy (lenient)** | mypy | Catches shape/None bugs in data code; lenient so ML code stays readable. |
| Tests | unittest, **pytest + hypothesis** | pytest | Property tests for windowing and leakage invariants. |

## Decision
`pyproject.toml` with the `uv_build` backend and `src/` layout, `requires-python = ">=3.12,<3.13"`, and `uv.lock` committed. Torch comes from the PyTorch CPU index on Linux only (`[tool.uv.sources]` marker), which keeps CI and Space images small. Runtime extras are under `app` (gradio, huggingface_hub, onnx, onnxruntime) so the core library stays lean. `make lint test typecheck` is the local equivalent of CI.

## Evidence
Initial sync on 2026-11-15 resolved Python 3.12.13, torch 2.15.0 (MPS available), lightgbm 4.7.0, scikit-learn 1.9.1, mlflow 3.18.0, optuna 5.0.0, gradio 6.32.0, pandera 0.36.0, polars 2.1.0 and numpy 2.5.4. All Phase-0 checks passed.

## Consequences
- New dependencies must be added with `uv add` and justified in the PR or commit message.
- mlflow prints an "agent hint" on import; set `MLFLOW_DISABLE_AGENT_HINT=1` in scripts that parse stdout.
