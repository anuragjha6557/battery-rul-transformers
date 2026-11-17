"""Equal-budget hyperparameter tuning on Toyota train (PROTOCOL §3/§6, ADR-0006).

One Optuna study per (model config, task), named ``"{name}__{task}"``, stored in a shared
``JournalStorage`` file so that ``n_jobs`` spawned worker processes (and later invocations)
cooperate on the same study.

Objective (lower is better): mean over the **inner grouped 5-fold CV on Toyota train cells
only** (``official_split`` train, ``grouped_kfold(k=5, seed=0)``) of the fold's validation
metric:

* ``forecast``: RMSE in %SOH at the largest horizon <= 50 present (Toyota: h = 50)
* ``soh``: RMSE in %SOH
* ``rul``: MAE in cycles

Per fold: scalers are fit on the fold's training cells only (``prepare_cycles``); training
samples use origins ``"all"`` thinned by ``train_stride`` (**keep every k-th origin per cell,
starting with the first one; the same rule for every model**, so the compute budget per trial is
comparable and no model sees more training data than another); validation samples use origins
``"all"`` at stride 1. The model is fit with ``val`` for early stopping (as in the runner).

Pruning: neural models report their validation loss to Optuna after every epoch
(``NeuralModel(epoch_callback=...)``) at step ``fold_idx * max_epochs + epoch``; Hyperband
decides. Non-neural models are never pruned. A trial whose metric is non-finite is pruned.

OpenMP isolation (CLAUDE.md): this module imports neither torch nor lightgbm at module level.
A study is one model, hence one OpenMP family, so the process that fits it may import that
family's library; the parent only imports it when it needs the model class's traits.
"""

from __future__ import annotations

import hashlib
import json
import logging
import math
import multiprocessing as mp
import os
import tempfile
import time
from collections.abc import Callable, Iterator, Mapping
from concurrent.futures import ProcessPoolExecutor
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import numpy as np
import yaml

from battery_rul.eval.metrics import horizon_errors, rmse_pct, rul_errors
from battery_rul.models.base import SampleSet
from battery_rul.models.registry import (
    MODELS,
    accepts_kwarg,
    make_model,
    model_trait,
    omp_family,
)
from battery_rul.splits.toyota import grouped_kfold, official_split
from battery_rul.tasks.samples import TaskSpec, build_samples, prepare_cycles, thin_origins
from battery_rul.train.config import CONFIG_DIR, default_horizons, default_tracking_uri
from battery_rul.utils import PROCESSED_DIR, PROJECT_ROOT, resolve_device, seed_everything

log = logging.getLogger("battery_rul.tune")

DATASET = "toyota"
THETA = 0.8
FEATURE_SET: Literal["sc", "mc"] = "mc"
N_FOLDS = 5
MAX_PRIMARY_HORIZON = 50
BOUNDARY_TOL = 0.05
TUNING_EXPERIMENT = "tuning"
DEFAULT_JOURNAL = PROJECT_ROOT / "optuna" / "journal.log"
PATIENCE = 20  # early-stopping patience (PROTOCOL §6)
DEFAULT_MAX_EPOCHS = 300  # NeuralModel default; used to space pruning steps across folds
THREAD_VARS = (
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "OPENBLAS_NUM_THREADS",
)


class TuningError(ValueError):
    """The model/task cannot be tuned (no search space, untunable, unsupported task)."""


# --------------------------------------------------------------------------------------
# Config, search space
# --------------------------------------------------------------------------------------
@dataclass(frozen=True)
class TuneSpec:
    """Everything a worker process needs (picklable)."""

    name: str
    task: str
    defaults: dict[str, Any]
    search: dict[str, dict[str, Any]]
    train_stride: int
    processed_dir: str
    journal: str
    seed: int = 0


def load_model_config(name: str, config_dir: Path | None = None) -> dict[str, Any]:
    path = (config_dir or CONFIG_DIR) / "model" / f"{name}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"model config {name!r} not found at {path}")
    raw = yaml.safe_load(path.read_text())
    if raw.get("name") != name:
        raise ValueError(f"{path}: `name` is {raw.get('name')!r}, expected {name!r}")
    return {
        "name": name,
        "params": dict(raw.get("params") or {}),
        "search": raw.get("search") or {},
    }


def search_hash(search: Mapping[str, Any]) -> str:
    return hashlib.sha256(json.dumps(search, sort_keys=True, default=str).encode()).hexdigest()[:12]


def suggest(trial: Any, search: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    """Draw one parameter set from the search space (float / int / categorical)."""
    out: dict[str, Any] = {}
    for key, spec in search.items():
        kind = spec["type"]
        if kind == "float":
            out[key] = trial.suggest_float(
                key, float(spec["low"]), float(spec["high"]), log=bool(spec.get("log", False))
            )
        elif kind == "int":
            out[key] = trial.suggest_int(
                key, int(spec["low"]), int(spec["high"]), log=bool(spec.get("log", False))
            )
        elif kind == "categorical":
            out[key] = trial.suggest_categorical(key, list(spec["choices"]))
        else:
            raise TuningError(f"search param {key!r}: unknown type {kind!r}")
    return out


def boundary_hits(
    search: Mapping[str, Mapping[str, Any]],
    best: Mapping[str, Any],
    tol: float = BOUNDARY_TOL,
) -> list[dict[str, Any]]:
    """Numeric params whose best value lies within ``tol`` (fraction of the range) of a bound.

    The range is measured in log space for ``log: true`` params. Categorical params are skipped.
    """
    hits: list[dict[str, Any]] = []
    for key, spec in search.items():
        if spec["type"] not in ("float", "int") or key not in best:
            continue
        lo, hi, v = float(spec["low"]), float(spec["high"]), float(best[key])
        if bool(spec.get("log", False)):
            lo, hi, v = math.log(lo), math.log(hi), math.log(v)
        if hi <= lo:
            continue
        frac = (v - lo) / (hi - lo)
        if frac <= tol:
            hits.append({"param": key, "side": "low", "value": best[key], "frac": frac})
        elif frac >= 1.0 - tol:
            hits.append({"param": key, "side": "high", "value": best[key], "frac": frac})
    return hits


# --------------------------------------------------------------------------------------
# Objective
# --------------------------------------------------------------------------------------
def primary_horizon(horizons: tuple[int, ...]) -> int:
    ok = [h for h in horizons if h <= MAX_PRIMARY_HORIZON]
    if not ok:
        raise TuningError(f"no horizon <= {MAX_PRIMARY_HORIZON} in {horizons}")
    return max(ok)


def primary_metric(task: str, ss: SampleSet, point: np.ndarray) -> float:
    """The task's tuning metric on validation samples (nan if there is nothing to score)."""
    y, m = ss.y, ss.y_mask
    if task == "forecast":
        h = primary_horizon(ss.horizons)
        return float(horizon_errors(y, point, m, ss.horizons)[h]["rmse"])
    if task == "soh":
        sel = m[:, 0]
        return rmse_pct(y[sel, 0], point[sel, 0]) if sel.any() else float("nan")
    sel = m[:, 0] & (y[:, 0] > 0)
    return rul_errors(y[sel, 0], point[sel, 0]).mae if sel.any() else float("nan")


class _FoldCache:
    """Per-process cache of (train, val) SampleSets per (lookback, fold)."""

    def __init__(self, spec: TuneSpec) -> None:
        from battery_rul.train.runner import dataset_ctx

        self.spec = spec
        self.ctx = dataset_ctx(DATASET, spec.processed_dir, THETA)
        train_cells = official_split(self.ctx.cells)["train"]
        self.folds = grouped_kfold(train_cells, k=N_FOLDS, seed=0)
        self.horizons = tuple(default_horizons()[DATASET])
        self._prepared: dict[int, Any] = {}
        self._samples: dict[tuple[int, int], tuple[SampleSet, SampleSet] | None] = {}

    def get(self, fold: int, lookback: int) -> tuple[SampleSet, SampleSet] | None:
        key = (lookback, fold)
        if key not in self._samples:
            tr_cells, va_cells = self.folds[fold]
            if fold not in self._prepared:
                self._prepared[fold] = prepare_cycles(self.ctx.cycles, tr_cells, FEATURE_SET)
            prep = self._prepared[fold]
            ts = TaskSpec(
                task=self.spec.task,  # type: ignore[arg-type]
                lookback=lookback,
                horizons=self.horizons,
                feature_set=FEATURE_SET,
            )
            try:
                tr = thin_origins(
                    build_samples(prep, tr_cells, self.ctx.eol, ts, "all"), self.spec.train_stride
                )
                va = build_samples(prep, va_cells, self.ctx.eol, ts, "all")
                self._samples[key] = (tr, va)
            except ValueError as e:
                if "no samples" not in str(e):
                    raise
                self._samples[key] = None
        return self._samples[key]


def make_objective(spec: TuneSpec, cache: _FoldCache | None = None) -> Callable[[Any], float]:
    """Optuna objective closure. Imports optuna lazily."""
    import optuna

    cache = cache or _FoldCache(spec)
    factory = MODELS[spec.name]
    neural = omp_family(spec.name) == "torch"
    wants_device = accepts_kwarg(factory, "device")

    def objective(trial: optuna.Trial) -> float:
        params = {**spec.defaults, **suggest(trial, spec.search)}
        lookback = int(params.get("lookback", 32))
        ctor = {k: v for k, v in params.items() if k != "lookback"}
        if wants_device and "device" not in ctor:
            ctor["device"] = resolve_device("auto")
        max_epochs = int(ctor.get("max_epochs", DEFAULT_MAX_EPOCHS))
        scores: list[float] = []
        for fold in range(N_FOLDS):
            data = cache.get(fold, lookback)
            if data is None:
                continue
            tr, va = data
            kw = dict(ctor)
            if neural:

                def cb(epoch: int, val_loss: float, fold: int = fold) -> None:
                    step = fold * max_epochs + epoch
                    trial.report(val_loss, step)
                    if trial.should_prune():
                        raise optuna.TrialPruned()

                kw["epoch_callback"] = cb
            seed_everything(spec.seed)
            model = make_model(spec.name, **kw)
            model.fit(tr, va)
            v = primary_metric(spec.task, va, model.predict(va).point)
            if not np.isfinite(v):
                raise optuna.TrialPruned(f"non-finite metric in fold {fold}")
            scores.append(v)
        if not scores:
            raise TuningError("no fold produced validation samples")
        return float(np.mean(scores))

    return objective


# --------------------------------------------------------------------------------------
# Study plumbing
# --------------------------------------------------------------------------------------
def make_pruner() -> Any:
    """Hyperband with ``min_resource=20``: the early-stopping patience.

    Pruning steps are ``fold * max_epochs + epoch``, so no trial can be pruned before epoch 20 of
    fold 0, i.e. before early stopping itself could have acted. With the default
    ``min_resource=1``, 88 % of NLinear trials were pruned on early-epoch loss, which favours
    fast-starting (high-lr) configs. ``reduction_factor=3`` is Optuna's usual setting.
    """
    import optuna

    return optuna.pruners.HyperbandPruner(min_resource=PATIENCE, reduction_factor=3)


def study_name(name: str, task: str) -> str:
    return f"{name}__{task}"


def _storage(journal: str) -> Any:
    from optuna.storages import JournalStorage
    from optuna.storages.journal import JournalFileBackend

    return JournalStorage(JournalFileBackend(journal))


def _worker(spec: TuneSpec, n_trials: int, sampler_seed: int, constant_liar: bool) -> int:
    """Run ``n_trials`` trials of the shared study; returns the number requested."""
    import optuna

    optuna.logging.set_verbosity(optuna.logging.WARNING)
    study = optuna.load_study(
        study_name=study_name(spec.name, spec.task),
        storage=_storage(spec.journal),
        sampler=optuna.samplers.TPESampler(seed=sampler_seed, constant_liar=constant_liar),
        pruner=make_pruner(),
    )
    study.optimize(make_objective(spec), n_trials=n_trials, catch=(TuningError,))
    return n_trials


def _worker_init() -> None:
    import sys

    torch = sys.modules.get("torch")
    if torch is not None:
        torch.set_num_threads(1)


@contextmanager
def _single_thread_env() -> Iterator[None]:
    """Set thread-count env vars before spawning so children read them at first import."""
    old = {v: os.environ.get(v) for v in THREAD_VARS}
    os.environ.update({v: "1" for v in THREAD_VARS})
    try:
        yield
    finally:
        for v, o in old.items():
            if o is None:
                os.environ.pop(v, None)
            else:
                os.environ[v] = o


def _check_tunable(cfg: Mapping[str, Any], task: str) -> None:
    name = cfg["name"]
    if name not in MODELS:
        raise KeyError(f"unknown model {name!r}; registered: {sorted(MODELS)}")
    cls = MODELS[name]
    if not model_trait(cls, "tunable") or not cfg["search"]:
        raise TuningError(
            f"model {name!r} is not tunable (tunable={model_trait(cls, 'tunable')}, "
            f"search space has {len(cfg['search'])} params); nothing to tune"
        )
    supported = getattr(cls, "supported_tasks", None)
    if supported is not None and task not in supported:
        raise TuningError(f"model {name!r} does not support task {task!r}")
    if task not in ("soh", "forecast", "rul"):
        raise TuningError(f"unknown task {task!r}")


@dataclass
class TuneResult:
    study_name: str
    best_value: float
    best_params: dict[str, Any]
    params: dict[str, Any]  # defaults + best
    n_complete: int
    n_pruned: int
    n_fail: int
    n_trials_total: int
    boundary: list[dict[str, Any]]
    mlflow_run_id: str
    tuned_path: Path
    wall_seconds: float
    search_hash: str


def tune(
    model: str,
    task: str,
    n_trials: int = 50,
    n_jobs: int = 4,
    train_stride: int = 4,
    *,
    config_dir: Path | None = None,
    processed_dir: Path | None = None,
    journal: Path | None = None,
    tracking_uri: str | None = None,
    seed: int = 0,
) -> TuneResult:
    """Run (or resume) the study for ``(model, task)``; ``n_trials`` *more* trials are added.

    ``n_jobs > 1`` spawns that many worker processes sharing the journal storage; with
    ``n_jobs == 1`` trials run in this process.
    """
    import optuna

    optuna.logging.set_verbosity(optuna.logging.WARNING)
    # n_trials == 0 = finalize only: re-run the post-processing (tuned YAML, boundary check,
    # MLflow run) for an existing study without adding trials (e.g. after a crash in logging).
    if n_trials < 0 or n_jobs < 1 or train_stride < 1:
        raise ValueError("n_trials must be >= 0; n_jobs and train_stride must be >= 1")
    cdir = config_dir or CONFIG_DIR
    cfg = load_model_config(model, cdir)
    _check_tunable(cfg, task)
    shash = search_hash(cfg["search"])
    jpath = Path(journal or DEFAULT_JOURNAL).resolve()
    jpath.parent.mkdir(parents=True, exist_ok=True)
    journal_s = str(jpath)
    spec = TuneSpec(
        name=model,
        task=task,
        defaults=cfg["params"],
        search=cfg["search"],
        train_stride=train_stride,
        processed_dir=str(processed_dir or PROCESSED_DIR),
        journal=journal_s,
        seed=seed,
    )
    sname = study_name(model, task)
    study = optuna.create_study(
        study_name=sname,
        storage=_storage(journal_s),
        sampler=optuna.samplers.TPESampler(seed=seed),
        pruner=make_pruner(),
        load_if_exists=True,
    )
    prev = study.user_attrs.get("search_hash")
    if prev is not None and prev != shash:
        raise TuningError(
            f"study {sname!r} was created with search space {prev}, but the config now hashes "
            f"to {shash}; use a new journal or revert the search space"
        )
    study.set_user_attr("search_hash", shash)
    study.set_user_attr("train_stride", train_stride)
    n_existing = len(study.trials)

    t0 = time.perf_counter()
    if n_trials == 0 and n_existing == 0:
        raise TuningError(f"finalize-only (n_trials=0) needs an existing study {sname!r}")
    jobs = max(1, min(n_jobs, n_trials))
    shares = [n_trials // jobs + (1 if i < n_trials % jobs else 0) for i in range(jobs)]
    # Distinct, deterministic sampler seeds per worker and per resume (identical seeds would
    # make parallel workers propose identical startup trials).
    seeds = [seed + n_existing + i for i in range(jobs)]
    if n_trials == 0:
        pass  # finalize only
    elif jobs == 1:
        _worker(spec, shares[0], seeds[0], False)
    else:
        with (
            _single_thread_env(),
            ProcessPoolExecutor(
                max_workers=jobs, mp_context=mp.get_context("spawn"), initializer=_worker_init
            ) as ex,
        ):
            futs = [
                ex.submit(_worker, spec, s, sd, True) for s, sd in zip(shares, seeds, strict=True)
            ]
            for f in futs:
                f.result()
    wall = time.perf_counter() - t0

    study = optuna.load_study(study_name=sname, storage=_storage(journal_s))
    from optuna.trial import TrialState

    states = [t.state for t in study.trials]
    n_complete = states.count(TrialState.COMPLETE)
    n_pruned = states.count(TrialState.PRUNED)
    n_fail = states.count(TrialState.FAIL)
    if n_complete == 0:
        raise RuntimeError(f"study {sname!r} has no completed trials ({n_fail} failed)")
    best_params = dict(study.best_params)
    merged = {**cfg["params"], **best_params}
    hits = boundary_hits(cfg["search"], best_params)
    for h in hits:
        log.warning("boundary hit: %s", h)
    out_path = (cdir / "tuned") / f"{sname}.yaml"

    run_id = _log_mlflow(
        spec, study, n_trials, shash, merged, best_params, hits, tracking_uri, n_complete, n_pruned
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        yaml.safe_dump(
            {
                "name": model,
                "task": task,
                "params": merged,
                "tuned_from": run_id,
                "search_hash": shash,
                "best_value": float(study.best_value),
            },
            sort_keys=False,
        )
    )
    return TuneResult(
        study_name=sname,
        best_value=float(study.best_value),
        best_params=best_params,
        params=merged,
        n_complete=n_complete,
        n_pruned=n_pruned,
        n_fail=n_fail,
        n_trials_total=len(states),
        boundary=hits,
        mlflow_run_id=run_id,
        tuned_path=out_path,
        wall_seconds=wall,
        search_hash=shash,
    )


def _log_mlflow(
    spec: TuneSpec,
    study: Any,
    n_trials: int,
    shash: str,
    merged: dict[str, Any],
    best_params: dict[str, Any],
    hits: list[dict[str, Any]],
    tracking_uri: str | None,
    n_complete: int,
    n_pruned: int,
) -> str:
    import mlflow

    from battery_rul.train.runner import get_experiment_id, git_info

    uri = tracking_uri or default_tracking_uri()
    exp_id = get_experiment_id(TUNING_EXPERIMENT, uri)
    sha, dirty = git_info()
    with mlflow.start_run(experiment_id=exp_id, run_name=study.study_name) as run:
        mlflow.log_params(
            {
                "model": spec.name,
                "task": spec.task,
                "n_trials": n_trials,
                "train_stride": spec.train_stride,
                "search_hash": shash,
                "git_sha": sha,
                "git_dirty": dirty,
                "n_trials_total": len(study.trials),
            }
        )
        mlflow.log_metrics(
            {
                "best_value": float(study.best_value),
                "n_complete": n_complete,
                "n_pruned": n_pruned,
            }
        )
        mlflow.set_tags(
            {
                "kind": "tuning",
                "boundary_hits": ",".join(f"{h['param']}:{h['side']}" for h in hits) or "none",
            }
        )
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            study.trials_dataframe().to_csv(d / "trials.csv", index=False)
            (d / "best_params.yaml").write_text(
                yaml.safe_dump({"params": merged, "searched": best_params, "boundary": hits})
            )
            mlflow.log_artifact(str(d / "trials.csv"))
            mlflow.log_artifact(str(d / "best_params.yaml"))
        return str(run.info.run_id)


def format_result(r: TuneResult) -> str:
    lines = [
        f"study {r.study_name}: best value {r.best_value:.4f} "
        f"({r.n_complete} complete, {r.n_pruned} pruned, {r.n_fail} failed of "
        f"{r.n_trials_total} trials; {r.wall_seconds:.0f} s this call)",
        f"best params: {json.dumps(r.best_params, default=str)}",
    ]
    if r.boundary:
        lines.append(
            "BOUNDARY HIT (ADR-0006: widen the space for ALL models): "
            + "; ".join(f"{h['param']} at {h['side']} bound ({h['value']})" for h in r.boundary)
        )
    else:
        lines.append("boundary check: no numeric param within 5 % of a bound")
    lines.append(f"tuned config: {r.tuned_path} (tuned_from={r.mlflow_run_id})")
    return "\n".join(lines)
