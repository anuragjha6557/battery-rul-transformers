"""Benchmark runner: work units -> (cross-fitted) fits -> metrics -> MLflow.

Work unit = (dataset, task, model, outer_fold, seed). See PROTOCOL.md §3 (splits, CV+),
§4 rule 6 (no untuned tunable models), §7 (metrics).

Design choices
--------------
* **MLflow is only ever written from the main process.** Workers (``ProcessPoolExecutor``,
  spawn) are pure compute and return picklable results (metrics + prediction frames); the main
  process logs one nested run per unit under a single parent run. This avoids sqlite write
  contention and half-written runs when a worker dies, at the cost of shipping prediction
  DataFrames over a pipe (small next to model fit time).
* Per-process caches: prepared cycles per (dataset, fold) and SampleSets per
  (dataset, fold, task, lookback), so models sharing a lookback never rebuild them.
* ``lookback`` in ``ModelConfig.params`` overrides the experiment lookback for that model and is
  not passed to the model constructor.
"""

from __future__ import annotations

import logging
import multiprocessing as mp
import os
import subprocess
import sys
import tempfile
import time
import traceback
from collections import OrderedDict
from collections.abc import Callable
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

from battery_rul.data.io import read_tables
from battery_rul.eval.metrics import (
    alpha_lambda_accuracy,
    horizon_errors,
    mae_pct,
    rmse_pct,
    rul_errors,
)
from battery_rul.features.curves import load_curve_features
from battery_rul.models.base import FitInfo, Model, Prediction, SampleSet
from battery_rul.models.registry import (
    MODELS,
    accepts_kwarg,
    make_model,
    model_trait,
    omp_family,
)
from battery_rul.splits.loco import independent_fold_cells, loco_folds
from battery_rul.splits.toyota import grouped_kfold, official_split
from battery_rul.tasks.labels import eol_table, label_source
from battery_rul.tasks.samples import (
    PreparedCycles,
    TaskSpec,
    build_samples,
    merge_curve_features,
    prepare_cycles,
)
from battery_rul.train.config import (
    ExperimentConfig,
    ModelConfig,
    horizons_for,
    resolve_tuned_models,
)
from battery_rul.utils import (
    PROCESSED_DIR,
    PROJECT_ROOT,
    config_hash,
    resolve_device,
    seed_everything,
)

log = logging.getLogger("battery_rul.runner")

SMOOTH_WINDOW = 5
VALID_TASKS = ("soh", "forecast", "rul")


class UntunedModelError(ValueError):
    """PROTOCOL §4 rule 6: a tunable model was configured without tuning provenance."""


# --------------------------------------------------------------------------------------
# Plans
# --------------------------------------------------------------------------------------
@dataclass(frozen=True)
class FoldPlan:
    """One outer fold. ``tests`` maps a split tag ("test" for LOCO, "test1"/"test2" Toyota)."""

    name: str
    train: tuple[str, ...]
    tests: tuple[tuple[str, tuple[str, ...]], ...]
    inner: tuple[tuple[tuple[str, ...], tuple[str, ...]], ...]  # (inner_train, inner_val)


@dataclass(frozen=True)
class UnitSpec:
    dataset: str
    task: str
    model: ModelConfig
    fold: str
    seed: int
    lookback: int
    key: str
    unit_cfg: dict[str, Any] = field(compare=False, hash=False, default_factory=dict)


def plan_folds(dataset: str, cells: pd.DataFrame) -> list[FoldPlan]:
    if dataset == "toyota":
        split = official_split(cells)
        inner = tuple(grouped_kfold(split["train"], k=5, seed=0))
        tests = tuple((s, split[s]) for s in ("test1", "test2") if split[s])
        return [FoldPlan("official", split["train"], tests, inner)]
    plans = []
    for f in loco_folds(list(cells["cell_id"].astype(str))):
        inner = tuple((i.train, (i.val,)) for i in f.inner)
        plans.append(FoldPlan(f.test, f.train, (("test", (f.test,)),), inner))
    return plans


def effective_lookback(cfg: ExperimentConfig, model: ModelConfig) -> int:
    return int(model.params.get("lookback", cfg.lookback))


def model_ctor_params(model: ModelConfig) -> dict[str, Any]:
    return {k: v for k, v in model.params.items() if k != "lookback"}


def check_rule6(cfg: ExperimentConfig) -> None:
    for m in cfg.models:
        if m.name not in MODELS:
            raise KeyError(f"unknown model {m.name!r}; registered: {sorted(MODELS)}")
        if (
            model_trait(MODELS[m.name], "tunable")
            and m.tuned_from is None
            and not cfg.allow_untuned
        ):
            raise UntunedModelError(
                f"model {m.name!r} is tunable but has no `tuned_from` tuning run ID "
                "(PROTOCOL §4 rule 6); set allow_untuned=true only for smoke/debug runs"
            )


def unit_config(
    cfg: ExperimentConfig,
    dataset: str,
    task: str,
    m: ModelConfig,
    fold: str,
    seed: int,
    lookback: int,
) -> dict[str, Any]:
    return {
        "dataset": dataset,
        "task": task,
        "model": {"name": m.name, "params": model_ctor_params(m), "tuned_from": m.tuned_from},
        "fold": fold,
        "seed": seed,
        "lookback": lookback,
        "horizons": list(horizons_for(cfg, dataset)),
        "feature_set": cfg.feature_set,
        "theta": cfg.theta,
        "eval_origins": list(cfg.eval_origins),
        "protocol_version": cfg.protocol_version,
    }


# --------------------------------------------------------------------------------------
# Per-process data caches
# --------------------------------------------------------------------------------------
@dataclass
class DatasetCtx:
    cycles: pd.DataFrame
    cells: pd.DataFrame
    eol: pd.DataFrame
    smooth: pd.Series  # centred 5-cycle median SOH, indexed by (cell_id, cycle_idx)


@lru_cache(maxsize=4)
def dataset_ctx(dataset: str, processed_dir: str, theta: float) -> DatasetCtx:
    t = read_tables(dataset, Path(processed_dir), curves=False)
    cycles = t.cycles.sort_values(["cell_id", "cycle_idx"]).reset_index(drop=True)
    eol = eol_table(cycles, t.cells, theta)
    sm = cycles.groupby("cell_id", sort=False)["soh"].transform(
        lambda s: s.rolling(SMOOTH_WINDOW, center=True, min_periods=1).median()
    )
    smooth = pd.Series(
        sm.to_numpy(), index=pd.MultiIndex.from_frame(cycles[["cell_id", "cycle_idx"]])
    )
    return DatasetCtx(cycles=cycles, cells=t.cells, eol=eol, smooth=smooth)


class _LRU:
    def __init__(self, size: int) -> None:
        self.size, self.d = size, OrderedDict[tuple[Any, ...], Any]()

    def get(self, key: tuple[Any, ...], build: Callable[[], Any]) -> Any:
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        val = build()
        self.d[key] = val
        while len(self.d) > self.size:
            self.d.popitem(last=False)
        return val


_PREPARED = _LRU(4)
_SAMPLES = _LRU(6)


@dataclass
class FoldData:
    train: SampleSet
    tests: dict[tuple[str, str], SampleSet]  # (split_tag, origin policy) -> samples
    y_smooth: dict[tuple[str, str], tuple[np.ndarray, np.ndarray]]  # -> (values, valid mask)


def _is_no_samples(e: ValueError) -> bool:
    return "no samples" in str(e)


def fold_data(
    ctx: DatasetCtx,
    plan: FoldPlan,
    cfg: ExperimentConfig,
    dataset: str,
    task: str,
    lookback: int,
    processed_dir: str,
) -> FoldData:
    horizons = horizons_for(cfg, dataset)
    base = (processed_dir, dataset, plan.name, cfg.feature_set, cfg.theta)

    def prep() -> PreparedCycles:
        cyc = ctx.cycles
        if cfg.feature_set == "mc_curve":
            cyc = merge_curve_features(cyc, load_curve_features(dataset, Path(processed_dir)))
        return prepare_cycles(cyc, plan.train, cfg.feature_set)  # type: ignore[arg-type]

    prepared: PreparedCycles = _PREPARED.get(base, prep)

    def build() -> FoldData:
        spec = TaskSpec(
            task=task,  # type: ignore[arg-type]
            lookback=lookback,
            horizons=horizons,
            feature_set=cfg.feature_set,  # type: ignore[arg-type]
        )
        train = build_samples(prepared, plan.train, ctx.eol, spec, "all")
        tests: dict[tuple[str, str], SampleSet] = {}
        sm: dict[tuple[str, str], tuple[np.ndarray, np.ndarray]] = {}
        for tag, cells in plan.tests:
            for policy in cfg.eval_origins:
                try:
                    ss = build_samples(prepared, cells, ctx.eol, spec, policy)  # type: ignore[arg-type]
                except ValueError as e:
                    if not _is_no_samples(e):
                        raise
                    log.info("no %s test samples for %s/%s/%s", policy, dataset, plan.name, task)
                    continue
                tests[(tag, policy)] = ss
                if task == "forecast":
                    sm[(tag, policy)] = _smooth_targets(ctx, ss)
        return FoldData(train, tests, sm)

    key = (*base, task, lookback, horizons, tuple(cfg.eval_origins))
    out: FoldData = _SAMPLES.get(key, build)
    return out


def _smooth_targets(ctx: DatasetCtx, ss: SampleSet) -> tuple[np.ndarray, np.ndarray]:
    cell = ss.meta["cell_id"].to_numpy()
    origin = ss.meta["origin_cycle"].to_numpy()
    vals = np.full(ss.y.shape, np.nan)
    for j, h in enumerate(ss.horizons):
        idx = pd.MultiIndex.from_arrays([cell, origin + h])
        vals[:, j] = ctx.smooth.reindex(idx).to_numpy()
    return np.nan_to_num(vals), np.isfinite(vals) & ss.y_mask


# --------------------------------------------------------------------------------------
# Metrics
# --------------------------------------------------------------------------------------
def compute_metrics(
    ss: SampleSet, pred: Prediction, smooth: tuple[np.ndarray, np.ndarray] | None
) -> dict[str, dict[str, float]]:
    """Metrics per start_kind plus ``overall``: ``{kind: {metric: value}}``."""
    kinds = ss.meta["start_kind"].to_numpy().astype(str)
    groups: dict[str, np.ndarray] = {"overall": np.ones(len(ss), dtype=bool)}
    for k in sorted(set(kinds) - {"all"}):
        groups[k] = kinds == k
    out: dict[str, dict[str, float]] = {}
    for kind, m in groups.items():
        met: dict[str, float] = {}
        y, ym, p = ss.y[m], ss.y_mask[m], pred.point[m]
        if ss.task == "forecast":
            he = horizon_errors(y, p, ym, ss.horizons)
            for h, v in he.items():
                met[f"rmse_h{h}"], met[f"mae_h{h}"] = v["rmse"], v["mae"]
            if smooth is not None:
                hs = horizon_errors(smooth[0][m], p, smooth[1][m], ss.horizons)
                for h, v in hs.items():
                    met[f"rmse_smooth_h{h}"] = v["rmse"]
        elif ss.task == "soh":
            sel = ym[:, 0]
            if sel.any():
                met["rmse"] = rmse_pct(y[sel, 0], p[sel, 0])
                met["mae"] = mae_pct(y[sel, 0], p[sel, 0])
        else:  # rul
            sel = ym[:, 0] & (y[:, 0] > 0)
            if sel.any():
                e = rul_errors(y[sel, 0], p[sel, 0])
                met.update(rul_mae=e.mae, rul_bias=e.bias, rul_rel_mae=e.rel_mae)
                if kind.startswith("frac:"):
                    met["alpha_lambda_acc"] = alpha_lambda_accuracy(y[sel, 0], p[sel, 0])
        out[kind] = {k: float(v) for k, v in met.items() if np.isfinite(v)}
    return out


def pred_frame(ss: SampleSet, pred: Prediction, extra: dict[str, Any]) -> pd.DataFrame:
    cols: dict[str, Any] = dict(extra)
    for j, h in enumerate(ss.horizons):
        cols[f"y_h{h}"] = ss.y[:, j]
        cols[f"y_mask_h{h}"] = ss.y_mask[:, j]
        cols[f"point_h{h}"] = pred.point[:, j]
        if pred.quantiles is not None:
            for qi, lvl in enumerate(pred.quantile_levels):
                cols[f"q{lvl:g}_h{h}"] = pred.quantiles[:, j, qi]
    return pd.concat(
        [ss.meta.reset_index(drop=True), pd.DataFrame(cols, index=range(len(ss)))], axis=1
    )


def average_predictions(preds: list[Prediction]) -> Prediction:
    """Mean of sub-model points and (per level) quantiles."""
    point = np.mean([p.point for p in preds], axis=0)
    if any(p.quantiles is None for p in preds):
        return Prediction(point=point)
    levels = preds[0].quantile_levels
    if any(p.quantile_levels != levels for p in preds):
        raise ValueError("sub-models disagree on quantile levels")
    q = np.mean([p.quantiles for p in preds if p.quantiles is not None], axis=0)
    return Prediction(point=point, quantiles=q, quantile_levels=levels)


# --------------------------------------------------------------------------------------
# One unit (runs in a worker or inline)
# --------------------------------------------------------------------------------------
@dataclass
class UnitResult:
    key: str
    status: str  # ok | skipped | error
    message: str = ""
    params: dict[str, str] = field(default_factory=dict)
    metrics: dict[str, float] = field(default_factory=dict)
    predictions: pd.DataFrame | None = None
    inner_val: pd.DataFrame | None = None


def _make(unit: UnitSpec, cfg: ExperimentConfig) -> Model:
    params = model_ctor_params(unit.model)
    if accepts_kwarg(MODELS[unit.model.name], "device") and "device" not in params:
        params["device"] = resolve_device(cfg.device)  # type: ignore[arg-type]
    return make_model(unit.model.name, **params)


def execute_unit(unit: UnitSpec, cfg: ExperimentConfig, processed_dir: str) -> UnitResult:
    try:
        return _execute_unit(unit, cfg, processed_dir)
    except Exception:
        return UnitResult(unit.key, "error", traceback.format_exc())


def _execute_unit(unit: UnitSpec, cfg: ExperimentConfig, processed_dir: str) -> UnitResult:
    ctx = dataset_ctx(unit.dataset, processed_dir, cfg.theta)
    plan = next(p for p in plan_folds(unit.dataset, ctx.cells) if p.name == unit.fold)
    try:
        fd = fold_data(ctx, plan, cfg, unit.dataset, unit.task, unit.lookback, processed_dir)
    except ValueError as e:
        if _is_no_samples(e):
            return UnitResult(unit.key, "skipped", f"no train samples: {e}")
        raise
    if not fd.tests:
        return UnitResult(unit.key, "skipped", "no test samples for any eval origin")

    probe = _make(unit, cfg)
    do_cross_fit = model_trait(probe, "cross_fit")
    train_cells = fd.train.meta["cell_id"].to_numpy()
    subs: list[tuple[Model, SampleSet | None, str]] = []
    infos: list[FitInfo] = []
    t0 = time.perf_counter()
    if do_cross_fit:
        for i, (tr, va) in enumerate(plan.inner):
            seed_everything(unit.seed)
            m = _make(unit, cfg)
            va_ss = fd.train.subset(np.isin(train_cells, list(va)))
            infos.append(m.fit(fd.train.subset(np.isin(train_cells, list(tr))), va_ss))
            subs.append((m, va_ss, f"inner{i}:" + "+".join(va)))
    else:
        seed_everything(unit.seed)
        m = _make(unit, cfg)
        infos.append(m.fit(fd.train, None))
        subs.append((m, None, "all"))
    fit_s = time.perf_counter() - t0

    metrics: dict[str, float] = {
        "fit_seconds": fit_s,
        "n_sub_models": float(len(subs)),
        "n_train": float(len(fd.train)),
    }
    bvl = [i.best_val_loss for i in infos if i.best_val_loss is not None]
    if bvl:
        metrics["best_val_loss_mean"] = float(np.mean(bvl))
    frames = []
    for (tag, policy), ss in fd.tests.items():
        pred = average_predictions([m.predict(ss) for m, _, _ in subs])
        for kind, mm in compute_metrics(ss, pred, fd.y_smooth.get((tag, policy))).items():
            for name, v in mm.items():
                metrics[f"{tag}/{policy}/{kind}/{name}"] = v
        frames.append(pred_frame(ss, pred, {"split": tag, "origin_policy": policy}))
    inner = None
    if do_cross_fit:
        parts = [
            pred_frame(va_ss, m.predict(va_ss), {"inner_fold": i, "inner_val": label})
            for i, (m, va_ss, label) in enumerate(subs)
            if va_ss is not None
        ]
        inner = pd.concat(parts, ignore_index=True)
    return UnitResult(
        unit.key,
        "ok",
        metrics=metrics,
        predictions=pd.concat(frames, ignore_index=True),
        inner_val=inner,
    )


def _worker_init() -> None:
    # Limit threads via the environment *before* any OpenMP runtime loads; importing torch here
    # would put torch's libomp into LightGBM workers (see models/registry.py).
    for var in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
        os.environ[var] = "1"
    torch = sys.modules.get("torch")
    if torch is not None:
        torch.set_num_threads(1)


# --------------------------------------------------------------------------------------
# MLflow side (main process only)
# --------------------------------------------------------------------------------------
@lru_cache(maxsize=1)
def git_info() -> tuple[str, bool]:
    def run(*a: str) -> str:
        return subprocess.run(
            ["git", *a], cwd=PROJECT_ROOT, capture_output=True, text=True, check=True
        ).stdout.strip()

    try:
        return run("rev-parse", "HEAD"), bool(run("status", "--porcelain"))
    except (subprocess.SubprocessError, OSError):
        return "unknown", False


def _artifact_root(tracking_uri: str) -> str | None:
    if tracking_uri.startswith("sqlite:///"):
        db = Path(tracking_uri.removeprefix("sqlite:///")).resolve()
        return (db.parent / "mlruns").as_uri()
    return None


def get_experiment_id(name: str, tracking_uri: str) -> str:
    import mlflow

    mlflow.set_tracking_uri(tracking_uri)
    exp = mlflow.get_experiment_by_name(name)
    if exp is not None:
        return str(exp.experiment_id)
    return str(mlflow.create_experiment(name, artifact_location=_artifact_root(tracking_uri)))


def finished_unit_keys(experiment_id: str) -> set[str]:
    from mlflow.tracking import MlflowClient

    client = MlflowClient()
    keys: set[str] = set()
    token = None
    while True:
        page = client.search_runs(
            [experiment_id], "attributes.status = 'FINISHED'", max_results=1000, page_token=token
        )
        keys |= {r.data.tags["unit_key"] for r in page if "unit_key" in r.data.tags}
        token = page.token
        if not token:
            return keys


def _log_unit(
    unit: UnitSpec, res: UnitResult, cfg: ExperimentConfig, cells: pd.DataFrame, exp_id: str
) -> None:
    import mlflow

    sha, dirty = git_info()
    plan = next(p for p in plan_folds(unit.dataset, cells) if p.name == unit.fold)
    ind = independent_fold_cells(unit.dataset, list(cells["cell_id"].astype(str)))
    test_cells = [c for _, cs in plan.tests for c in cs]
    probe_tuned = model_trait(MODELS[unit.model.name], "tunable")
    mlflow.start_run(
        run_name=f"{unit.dataset}/{unit.task}/{unit.model.name}/{unit.fold}/s{unit.seed}",
        nested=True,
        experiment_id=exp_id,
        tags={"unit_key": unit.key, "dataset": unit.dataset, "task": unit.task},
    )
    status = "FINISHED"
    try:
        if res.status == "error":
            status = "FAILED"
            mlflow.set_tag("error", res.message[-5000:])
            return
        params: dict[str, Any] = {
            "dataset": unit.dataset,
            "task": unit.task,
            "model": unit.model.name,
            "fold": unit.fold,
            "test_cell": unit.fold
            if plan.tests[0][0] == "test"
            else "+".join(t for t, _ in plan.tests),
            "n_test_cells": len(test_cells),
            "seed": unit.seed,
            "config_hash": unit.key,
            "git_sha": sha,
            "git_dirty": dirty,
            "protocol_version": cfg.protocol_version,
            "label_source": label_source(unit.dataset),
            "theta": cfg.theta,
            "feature_set": cfg.feature_set,
            "lookback": unit.lookback,
            "independent_fold": bool(plan.tests[0][0] == "test" and unit.fold in ind),
            "tuned_from": unit.model.tuned_from or "none",
            "tunable": probe_tuned,
            "eval_origins": ",".join(cfg.eval_origins),
        }
        params.update({f"model.{k}": v for k, v in model_ctor_params(unit.model).items()})
        mlflow.log_params(params)
        mlflow.log_metrics(res.metrics)
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            if res.predictions is not None:
                res.predictions.to_parquet(d / "predictions.parquet", index=False)
                mlflow.log_artifact(str(d / "predictions.parquet"))
            if res.inner_val is not None:
                res.inner_val.to_parquet(d / "inner_val_predictions.parquet", index=False)
                mlflow.log_artifact(str(d / "inner_val_predictions.parquet"))
            (d / "config.yaml").write_text(yaml.safe_dump(unit.unit_cfg, sort_keys=True))
            mlflow.log_artifact(str(d / "config.yaml"))
    except BaseException:
        status = "FAILED"
        raise
    finally:
        mlflow.end_run(status=status)


@dataclass
class RunSummary:
    parent_run_id: str
    n_units: int
    n_run: int
    n_resumed: int
    n_skipped: int
    n_unsupported: int
    n_failed: int


def run_experiment(
    cfg: ExperimentConfig, processed_dir: Path | None = None, n_jobs: int | None = None
) -> RunSummary:
    import mlflow

    cfg = resolve_tuned_models(cfg)
    check_rule6(cfg)
    for t in cfg.tasks:
        if t not in VALID_TASKS:
            raise ValueError(f"unknown task {t!r}")
    pdir = str(processed_dir or PROCESSED_DIR)
    n_jobs = n_jobs or cfg.n_jobs

    exp_id = get_experiment_id(cfg.name, cfg.tracking_uri)
    done = finished_unit_keys(exp_id)

    units: list[UnitSpec] = []
    cells_by_ds: dict[str, pd.DataFrame] = {}
    n_unsupported = n_resumed = 0
    for ds in cfg.datasets:
        ctx = dataset_ctx(ds, pdir, cfg.theta)
        cells_by_ds[ds] = ctx.cells
        plans = plan_folds(ds, ctx.cells)
        for task in cfg.tasks:
            for m in cfg.models:
                if m.tuned_task is not None and m.tuned_task != task:
                    log.info("skip: %s tuned for %s, not %s", m.name, m.tuned_task, task)
                    continue
                probe = (
                    make_model(m.name, **{**model_ctor_params(m)})
                    if not accepts_kwarg(MODELS[m.name], "device")
                    else make_model(m.name, **model_ctor_params(m), device="cpu")
                )
                if task not in probe.supported_tasks:
                    log.warning("skip: %s does not support task %s", m.name, task)
                    n_unsupported += 1
                    continue
                lb = effective_lookback(cfg, m)
                for plan in plans:
                    for seed in cfg.seeds:
                        ucfg = unit_config(cfg, ds, task, m, plan.name, seed, lb)
                        key = config_hash(ucfg)
                        if key in done:
                            n_resumed += 1
                            continue
                        units.append(UnitSpec(ds, task, m, plan.name, seed, lb, key, ucfg))
    units.sort(key=lambda u: (u.dataset, u.task, u.fold, u.lookback, u.model.name, u.seed))

    mlflow.set_tracking_uri(cfg.tracking_uri)
    n_run = n_skipped = n_failed = 0
    with mlflow.start_run(
        experiment_id=exp_id, run_name=f"{cfg.name}-{time.strftime('%Y%m%d-%H%M%S')}"
    ) as parent:
        mlflow.set_tags({"protocol_version": cfg.protocol_version, "kind": "experiment"})
        mlflow.log_text(yaml.safe_dump(asdict(cfg), sort_keys=False), "experiment_config.yaml")
        by_key = {u.key: u for u in units}

        def handle(res: UnitResult) -> None:
            nonlocal n_run, n_skipped, n_failed
            u = by_key[res.key]
            if res.status == "skipped":
                log.warning(
                    "skip %s/%s/%s/%s: %s", u.dataset, u.task, u.model.name, u.fold, res.message
                )
                n_skipped += 1
                return
            _log_unit(u, res, cfg, cells_by_ds[u.dataset], exp_id)
            if res.status == "error":
                n_failed += 1
                log.error("unit failed %s:\n%s", u.key, res.message)
            else:
                n_run += 1

        # OpenMP isolation (models/registry.py): if the experiment mixes torch and LightGBM
        # models, every unit runs in a fresh worker process (max_tasks_per_child=1), even with
        # n_jobs=1, so the two runtimes never share a process.
        families = {omp_family(u.model.name, u.model.params) for u in units} - {None}
        isolate = len(families) > 1
        if (n_jobs > 1 and len(units) > 1) or isolate:
            with ProcessPoolExecutor(
                max_workers=max(1, n_jobs),
                mp_context=mp.get_context("spawn"),
                initializer=_worker_init,
                max_tasks_per_child=1 if isolate else None,
            ) as ex:
                futs = [ex.submit(execute_unit, u, cfg, pdir) for u in units]
                for f in as_completed(futs):
                    handle(f.result())
        else:
            for u in units:
                handle(execute_unit(u, cfg, pdir))
        parent_id = parent.info.run_id
    if n_failed:
        raise RuntimeError(f"{n_failed} unit(s) failed; see FAILED runs in experiment {cfg.name!r}")
    return RunSummary(
        parent_id, len(units) + n_resumed, n_run, n_resumed, n_skipped, n_unsupported, n_failed
    )
