UV ?= $(HOME)/.local/bin/uv
export OMP_NUM_THREADS ?= 2
export PYTORCH_ENABLE_MPS_FALLBACK = 1

.PHONY: help env lint format typecheck test test-all cov data bench mlflow app clean

help:  ## Show targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

env:  ## Create/refresh the Python 3.12 environment (all extras + dev)
	$(UV) sync --all-extras
	$(UV) run pre-commit install

lint:  ## Ruff lint + format check
	$(UV) run ruff check .
	$(UV) run ruff format --check .

format:  ## Auto-fix lint and formatting
	$(UV) run ruff check --fix .
	$(UV) run ruff format .

typecheck:  ## mypy on src/
	$(UV) run mypy

test:  ## Fast unit tests (CI-identical). LightGBM tests run in a second process (OpenMP isolation)
	$(UV) run pytest
	$(UV) run pytest -o addopts="-ra --strict-markers -m 'not data and not slow'" tests/lgbm

test-all:  ## All tests incl. real-data and slow (needs data/raw)
	$(UV) run pytest -m ""
	$(UV) run pytest -o addopts="-ra --strict-markers" tests/lgbm

cov:  ## Unit tests with coverage report
	$(UV) run pytest --cov --cov-report=term-missing

data:  ## Download + build canonical parquet for all datasets
	$(UV) run battery-rul download all
	$(UV) run battery-rul build-data all

bench:  ## Full frozen benchmark (long; resumable) + CQR + reports + README tables
	$(UV) run battery-rul benchmark --config final
	bash scripts/post_benchmark.sh
	$(UV) run python scripts/make_figures.py
	$(UV) run python scripts/make_readme_tables.py

mlflow:  ## Launch the MLflow UI on the local store
	$(UV) run mlflow ui --backend-store-uri sqlite:///mlflow.db

app:  ## Run the Gradio demo locally
	BATTERY_RUL_WEIGHTS=artifacts/deploy $(UV) run python app/app.py

clean:  ## Remove caches (keeps data and mlruns)
	rm -rf .pytest_cache .ruff_cache .mypy_cache .hypothesis htmlcov .coverage
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
