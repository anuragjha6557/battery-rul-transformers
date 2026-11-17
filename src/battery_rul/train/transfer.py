"""Cross-chemistry transfer: Toyota (LFP) pre-training -> NASA / CALCE (ADR-0012, PROTOCOL §3).

Source domain = Toyota, targets = NASA and CALCE, so **all 124 Toyota cells** (official
train + test1 + test2) may be used for pre-training: no Toyota cell is ever evaluated here.
The only held-out data are the NASA/CALCE LOCO test cells, which pre-training never sees.

Inputs are the chemistry-agnostic ``feature_set="shared"`` channels
(:data:`battery_rul.tasks.samples.SHARED_CHANNELS`). Each dataset is standardised with its *own*
training cells (domain normalisation): Toyota's scaler from all Toyota cells, a NASA/CALCE
fold's scaler from that fold's 3 training cells only (rule 1). Horizons are common to all
datasets (:data:`SHARED_HORIZONS`) so the output head transfers.

Arms (per LOCO fold, cross-fitted over the 3 inner folds exactly like the benchmark runner):

* ``scratch``   - ordinary training on the fold's training cells.
* ``zero_shot`` - pretrained weights, no target-domain training at all.
* ``ft_head``   - freeze everything but the output head; fine-tune (lr unchanged).
* ``ft_full``   - fine-tune all parameters with lr x 0.1.
* ``few_shot``  - ``ft_full`` plus the test cell's own samples with origin <= T_p, built per start
  point. Leakage safety: a few-shot sample reads only cycles <= its origin <= T_p, and each of
  its horizon targets is *masked out* unless ``origin + h <= T_p`` (so no target beyond T_p is
  ever trained on). T_p comes from the evaluation protocol (PROTOCOL §3), the same value at which
  the forecast is issued. Few-shot is evaluated on the start-point origins only.

Fine-tuning reuses the pretrained tabular standardisation (SOH summaries share one scale).
Torch is imported lazily (OpenMP isolation rule).
"""

from __future__ import annotations

import copy
import logging
import tempfile
import time
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final

import numpy as np
import pandas as pd
import yaml

from battery_rul.models.base import FitInfo, Prediction, SampleSet
from battery_rul.splits.toyota import grouped_kfold
from battery_rul.tasks.samples import (
    PreparedCycles,
    TaskSpec,
    build_samples,
    prepare_cycles,
)
from battery_rul.train.config import default_tracking_uri, tuned_path
from battery_rul.train.runner import (
    DatasetCtx,
    FoldPlan,
    _smooth_targets,
    average_predictions,
    compute_metrics,
    dataset_ctx,
    plan_folds,
    pred_frame,
)
from battery_rul.utils import PROCESSED_DIR, PROJECT_ROOT, config_hash, seed_everything

if TYPE_CHECKING:
    from battery_rul.models.neural import NeuralModel

log = logging.getLogger("battery_rul.transfer")

SHARED_HORIZONS: Final = (1, 10, 25, 50, 100)
ARMS: Final = ("scratch", "zero_shot", "ft_head", "ft_full", "few_shot")
SOURCE: Final = "toyota"
PRETRAIN_DIR: Final = PROJECT_ROOT / "artifacts" / "pretrained"
FT_FULL_LR_MULT: Final = 0.1
EVAL_ORIGINS: Final = ("start_points", "all")


def pretrained_path(model_name: str, task: str, out_dir: Path | None = None) -> Path:
    return (out_dir or PRETRAIN_DIR) / f"{model_name}__{task}.pt"


def load_params(model_name: str, task: str) -> tuple[dict[str, Any], int, str]:
    """(ctor params without ``lookback``, lookback, provenance text).

    Uses ``configs/tuned/<model>__<task>.yaml`` when present, else the model defaults.
    """
    path = tuned_path(f"{model_name}__{task}")
    if path.exists():
        raw = yaml.safe_load(path.read_text())
        params = dict(raw.get("params") or {})
        lookback = int(params.pop("lookback", 32))
        return params, lookback, f"tuned:{path.name} (tuned_from={raw.get('tuned_from')})"
    return {}, 32, "defaults (no tuned file)"


def _spec(task: str, lookback: int) -> TaskSpec:
    return TaskSpec(
        task=task,  # type: ignore[arg-type]
        lookback=lookback,
        horizons=SHARED_HORIZONS,
        feature_set="shared",
    )


def _make(model_name: str, params: dict[str, Any], device: str) -> NeuralModel:
    from battery_rul.models.registry import make_model

    model = make_model(model_name, **{**params, "device": device})
    return model  # type: ignore[return-value]


# --------------------------------------------------------------------------------------
# Persistence
# --------------------------------------------------------------------------------------
def save_pretrained(
    model: NeuralModel, path: Path, params: dict[str, Any], lookback: int, meta: dict[str, Any]
) -> None:
    """Save weights + everything needed to rebuild the model (no scaler: it is per-dataset)."""
    import torch

    assert model.module is not None
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {
            "model_name": model.name,
            "params": {k: v for k, v in params.items() if k != "device"},
            "task": model._task,
            "dims": model._dims,  # type: ignore[attr-defined]
            "lookback": lookback,
            "tab_mu": np.atleast_1d(model._tab_mu).tolist(),
            "tab_sd": np.atleast_1d(model._tab_sd).tolist(),
            "rul_scale": float(model._rul_scale),
            "state_dict": {k: v.detach().cpu() for k, v in model.module.state_dict().items()},
            "meta": meta,
        },
        path,
    )


def load_pretrained(path: Path, device: str = "auto") -> NeuralModel:
    """Rebuild a model from :func:`save_pretrained` output (fresh independent copy)."""
    import torch

    ck = torch.load(path, map_location="cpu", weights_only=True)
    model = _make(ck["model_name"], ck["params"], device)
    model._task = ck["task"]
    model._dims = ck["dims"]  # type: ignore[attr-defined]
    model._tab_mu = np.asarray(ck["tab_mu"], dtype=np.float64)
    model._tab_sd = np.asarray(ck["tab_sd"], dtype=np.float64)
    model._rul_scale = float(ck["rul_scale"])
    d = ck["dims"]
    model.module = model.build_module(
        d["n_channels"], d["n_tab"], d["lookback"], d["n_h"], d["n_q"]
    ).to(model.device)
    model.module.load_state_dict(ck["state_dict"])
    model.module.eval()
    return model


def _record_dims(model: NeuralModel, train: SampleSet) -> None:
    """Remember the build_module arguments of a fitted model (needed to reload it)."""
    n_q = len(model.quantiles) if model.quantiles is not None else 1
    model._dims = {  # type: ignore[attr-defined]
        "n_channels": int(train.x_hist.shape[2] + 1),
        "n_tab": int(train.x_tab.shape[1]),
        "lookback": int(train.x_hist.shape[1]),
        "n_h": len(train.horizons),
        "n_q": n_q,
    }


# --------------------------------------------------------------------------------------
# Pre-training on Toyota
# --------------------------------------------------------------------------------------
@dataclass
class PretrainResult:
    path: Path
    fit_seconds: float
    info: FitInfo
    params_source: str
    val_cells: tuple[str, ...]
    run_id: str | None = None
    model: NeuralModel | None = None  # the fitted in-memory model (tests, chaining)


def pretrain(
    model_name: str,
    params: dict[str, Any],
    task: str,
    out_dir: Path | None = None,
    *,
    lookback: int = 32,
    seed: int = 0,
    device: str = "auto",
    processed_dir: str | None = None,
    ctx: DatasetCtx | None = None,
    theta: float = 0.8,
    params_source: str = "given",
    tracking_uri: str | None = None,
    log_mlflow: bool = True,
) -> PretrainResult:
    """Fit on all Toyota cells (early stopping on a grouped ~10 % of cells) and save to
    ``<out_dir>/<model>__<task>.pt``. ``ctx`` overrides loading (tests)."""
    ctx = ctx or dataset_ctx(SOURCE, processed_dir or str(PROCESSED_DIR), theta)
    cells = sorted(ctx.cells["cell_id"].astype(str))
    k = min(10, len(cells))
    train_cells, val_cells = grouped_kfold(cells, k=k, seed=0)[0]
    prepared = prepare_cycles(ctx.cycles, tuple(cells), "shared")  # scaler on source cells
    spec = _spec(task, lookback)
    tr = build_samples(prepared, train_cells, ctx.eol, spec, "all")
    va = build_samples(prepared, val_cells, ctx.eol, spec, "all")

    seed_everything(seed)
    model = _make(model_name, params, device)
    t0 = time.perf_counter()
    info = model.fit(tr, va)
    secs = time.perf_counter() - t0
    _record_dims(model, tr)
    path = pretrained_path(model_name, task, out_dir)
    save_pretrained(
        model,
        path,
        params,
        lookback,
        {"seed": seed, "n_cells": len(cells), "val_cells": list(val_cells), "source": SOURCE},
    )
    res = PretrainResult(path, secs, info, params_source, val_cells, model=model)
    if log_mlflow:
        res.run_id = _log_pretrain(res, model_name, task, params, lookback, seed, tracking_uri)
    return res


def _log_pretrain(
    res: PretrainResult,
    model_name: str,
    task: str,
    params: dict[str, Any],
    lookback: int,
    seed: int,
    tracking_uri: str | None,
) -> str:
    import mlflow

    from battery_rul.train.runner import get_experiment_id, git_info

    uri = tracking_uri or default_tracking_uri()
    exp_id = get_experiment_id("pretrain", uri)
    sha, dirty = git_info()
    with mlflow.start_run(experiment_id=exp_id, run_name=f"{model_name}/{task}/{SOURCE}") as run:
        mlflow.log_params(
            {
                "model": model_name,
                "task": task,
                "source": SOURCE,
                "seed": seed,
                "lookback": lookback,
                "feature_set": "shared",
                "horizons": ",".join(map(str, SHARED_HORIZONS)),
                "params_source": res.params_source,
                "val_cells": ",".join(res.val_cells),
                "artifact_path": str(res.path),
                "git_sha": sha,
                "git_dirty": dirty,
                **{f"model.{k}": v for k, v in params.items()},
            }
        )
        mlflow.log_metrics(
            {
                "fit_seconds": res.fit_seconds,
                "epochs": float(res.info.epochs or 0),
                "n_train": float(res.info.n_train),
                "n_val": float(res.info.n_val),
                **(
                    {"best_val_loss": res.info.best_val_loss}
                    if res.info.best_val_loss is not None
                    else {}
                ),
            }
        )
        return str(run.info.run_id)


# --------------------------------------------------------------------------------------
# Fine-tuning
# --------------------------------------------------------------------------------------
def head_module(module: Any) -> Any:
    """The output head (``head`` attribute, looking through a wrapper's ``inner``)."""
    for m in (module, getattr(module, "inner", None)):
        if m is not None and hasattr(m, "head"):
            return m.head
    raise ValueError("model has no `head` module; head-only fine-tuning unsupported")


def fine_tune(
    model: NeuralModel,
    train: SampleSet,
    val: SampleSet | None,
    *,
    head_only: bool = False,
    lr_mult: float = 1.0,
) -> FitInfo:
    """Continue training ``model.module`` (same loop as ``NeuralModel.fit``, early stopping on
    ``val``, best-epoch weights). Keeps the pretrained tabular standardisation."""
    import torch
    from torch import nn

    assert model.module is not None
    module = model.module
    if head_only:
        head = head_module(module)
        for p in module.parameters():
            p.requires_grad_(False)
        for p in head.parameters():
            p.requires_grad_(True)
    params = [p for p in module.parameters() if p.requires_grad]
    opt = torch.optim.Adam(params, lr=model.lr * lr_mult, weight_decay=model.weight_decay)
    xh, xt = model._x(train)
    y = torch.from_numpy(model._y_to_target(train).astype(np.float32)).to(model.device)
    m = torch.from_numpy(train.y_mask).to(model.device)
    if val is not None:
        vxh, vxt = model._x(val)
        vy = torch.from_numpy(model._y_to_target(val).astype(np.float32)).to(model.device)
        vm = torch.from_numpy(val.y_mask).to(model.device)
    n = len(train)
    gen = torch.Generator().manual_seed(torch.initial_seed() % (2**31))
    best, best_state, bad, epochs_run = float("inf"), None, 0, 0
    for epoch in range(1, model.max_epochs + 1):
        epochs_run = epoch
        module.eval() if head_only else module.train()  # frozen backbone: no dropout noise
        perm = torch.randperm(n, generator=gen).to(model.device)
        for i in range(0, n, model.batch_size):
            idx = perm[i : i + model.batch_size]
            opt.zero_grad(set_to_none=True)
            loss = model._loss(module(xh[idx], xt[idx]), y[idx], m[idx])
            loss.backward()
            nn.utils.clip_grad_norm_(params, model.grad_clip)
            opt.step()
        if val is None:
            continue
        module.eval()
        with torch.no_grad():
            v = float(model._loss(module(vxh, vxt), vy, vm))
        if v < best - 1e-7:
            best, best_state, bad = v, copy.deepcopy(module.state_dict()), 0
        else:
            bad += 1
            if bad >= model.patience:
                break
    if best_state is not None:
        module.load_state_dict(best_state)
    for p in module.parameters():
        p.requires_grad_(True)
    return FitInfo(
        n_train=n,
        n_val=len(val) if val is not None else 0,
        epochs=epochs_run,
        best_val_loss=best if val is not None else None,
        extra={"n_trainable": int(sum(p.numel() for p in params))},
    )


# --------------------------------------------------------------------------------------
# Samples
# --------------------------------------------------------------------------------------
def concat_samples(a: SampleSet, b: SampleSet) -> SampleSet:
    if a.horizons != b.horizons or a.channel_names != b.channel_names or a.task != b.task:
        raise ValueError("cannot concatenate incompatible SampleSets")
    return SampleSet(
        task=a.task,
        x_hist=np.concatenate([a.x_hist, b.x_hist]),
        hist_mask=np.concatenate([a.hist_mask, b.hist_mask]),
        x_tab=np.concatenate([a.x_tab, b.x_tab]),
        y=np.concatenate([a.y, b.y]),
        y_mask=np.concatenate([a.y_mask, b.y_mask]),
        horizons=a.horizons,
        channel_names=a.channel_names,
        feature_names=a.feature_names,
        meta=pd.concat([a.meta, b.meta], ignore_index=True),
    )


def fewshot_samples(cell_samples: SampleSet, t_p: int) -> SampleSet | None:
    """The test cell's samples usable for few-shot at start point ``t_p`` (cycles).

    ``cell_samples`` are all-origin samples of the test cell. Keeps origins <= t_p and masks every
    horizon target whose cycle ``origin + h`` exceeds t_p; samples left with no target are
    dropped. Returns ``None`` if nothing remains.
    """
    origin = cell_samples.meta["origin_cycle"].to_numpy()
    h = np.asarray(cell_samples.horizons)
    ym = cell_samples.y_mask & (origin[:, None] + h[None, :] <= t_p)
    keep = (origin <= t_p) & ym.any(axis=1)
    if not keep.any():
        return None
    sub = cell_samples.subset(keep)
    ym = ym[keep]
    return replace(sub, y_mask=ym, y=np.where(ym, sub.y, 0.0).astype(sub.y.dtype))


# --------------------------------------------------------------------------------------
# One (arm, dataset, fold, seed) unit
# --------------------------------------------------------------------------------------
@dataclass
class FoldBundle:
    """All samples of one NASA/CALCE LOCO fold under ``feature_set="shared"``."""

    dataset: str
    plan: FoldPlan
    train: SampleSet
    tests: dict[str, SampleSet]  # origin policy -> test samples
    smooth: dict[str, tuple[np.ndarray, np.ndarray]]
    test_all: SampleSet  # all-origin samples of the test cell (few-shot source)
    prepared: PreparedCycles = field(repr=False, default=None)  # type: ignore[assignment]


def build_bundle(
    ctx: DatasetCtx,
    dataset: str,
    test_cell: str,
    task: str,
    lookback: int,
    eval_origins: tuple[str, ...] = EVAL_ORIGINS,
) -> FoldBundle:
    plan = next(p for p in plan_folds(dataset, ctx.cells) if p.name == test_cell)
    prepared = prepare_cycles(ctx.cycles, plan.train, "shared")  # scaler on 3 training cells
    spec = _spec(task, lookback)
    train = build_samples(prepared, plan.train, ctx.eol, spec, "all")
    tests, smooth = {}, {}
    for pol in eval_origins:
        ss = build_samples(prepared, (test_cell,), ctx.eol, spec, pol)  # type: ignore[arg-type]
        tests[pol] = ss
        if task == "forecast":
            smooth[pol] = _smooth_targets(ctx, ss)
    test_all = build_samples(prepared, (test_cell,), ctx.eol, spec, "all")
    return FoldBundle(dataset, plan, train, tests, smooth, test_all, prepared)


@dataclass
class ArmResult:
    arm: str
    metrics: dict[str, float]
    predictions: pd.DataFrame
    fit_seconds: float


def _inner_sets(b: FoldBundle) -> list[tuple[SampleSet, SampleSet]]:
    cells = b.train.meta["cell_id"].to_numpy()
    return [
        (b.train.subset(np.isin(cells, list(tr))), b.train.subset(np.isin(cells, list(va))))
        for tr, va in b.plan.inner
    ]


def _fit_arm_models(
    arm: str,
    inner: list[tuple[SampleSet, SampleSet]],
    extra: SampleSet | None,
    *,
    model_name: str,
    params: dict[str, Any],
    pretrained: Path | None,
    seed: int,
    device: str,
) -> list[NeuralModel]:
    models: list[NeuralModel] = []
    if arm == "zero_shot":
        assert pretrained is not None
        return [load_pretrained(pretrained, device)]
    for tr, va in inner:
        seed_everything(seed)
        if arm == "scratch":
            m = _make(model_name, params, device)
            m.fit(tr, va)
        else:
            assert pretrained is not None
            m = load_pretrained(pretrained, device)
            if arm == "ft_head":
                fine_tune(m, tr, va, head_only=True)
            else:
                if arm == "few_shot" and extra is not None:
                    tr = concat_samples(tr, extra)
                fine_tune(m, tr, va, lr_mult=FT_FULL_LR_MULT)
        models.append(m)
    return models


def _predict(models: list[NeuralModel], ss: SampleSet) -> Prediction:
    return average_predictions([m.predict(ss) for m in models])


def run_arm(
    arm: str,
    bundle: FoldBundle,
    *,
    model_name: str,
    params: dict[str, Any],
    pretrained: Path | None,
    seed: int,
    device: str = "auto",
) -> ArmResult:
    """Fit/evaluate one arm on one fold. Metric names match the benchmark runner
    (``test/<policy>/<kind>/rmse_h10`` ...)."""
    if arm not in ARMS:
        raise ValueError(f"unknown arm {arm!r}; expected one of {ARMS}")
    if arm != "scratch" and pretrained is None:
        raise ValueError(f"arm {arm!r} needs a pretrained checkpoint")
    inner = _inner_sets(bundle)
    kw = dict(model_name=model_name, params=params, pretrained=pretrained, seed=seed, device=device)
    t0 = time.perf_counter()
    preds: dict[str, Prediction] = {}
    n_few = 0.0
    if arm == "few_shot":
        ss = bundle.tests["start_points"]
        point = np.zeros(ss.y.shape)
        quant: np.ndarray | None = None
        levels: tuple[float, ...] | None = None
        kinds = ss.meta["start_kind"].to_numpy().astype(str)
        for kind in sorted(set(kinds)):
            sel = np.where(kinds == kind)[0]
            t_p = int(ss.meta["origin_cycle"].to_numpy()[sel[0]])
            extra = fewshot_samples(bundle.test_all, t_p)
            n_few += 0 if extra is None else len(extra)
            if extra is None:
                log.warning("no few-shot samples for %s at T_p=%d", bundle.plan.name, t_p)
            models = _fit_arm_models(arm, inner, extra, **kw)  # type: ignore[arg-type]
            p = _predict(models, ss.subset(sel))
            point[sel] = p.point
            if p.quantiles is not None:
                if quant is None:
                    quant = np.zeros((len(ss), *p.quantiles.shape[1:]))
                    levels = p.quantile_levels
                quant[sel] = p.quantiles
        preds["start_points"] = Prediction(
            point=point, quantiles=quant, quantile_levels=levels or ()
        )
    else:
        models = _fit_arm_models(arm, inner, None, **kw)  # type: ignore[arg-type]
        for pol, ss in bundle.tests.items():
            preds[pol] = _predict(models, ss)
    secs = time.perf_counter() - t0

    metrics: dict[str, float] = {
        "fit_seconds": secs,
        "n_sub_models": float(len(inner) if arm != "zero_shot" else 1),
        "n_train": float(len(bundle.train)),
        "n_few_shot": n_few,
    }
    frames = []
    for pol, pred in preds.items():
        ss = bundle.tests[pol]
        for kind, mm in compute_metrics(ss, pred, bundle.smooth.get(pol)).items():
            for name, v in mm.items():
                metrics[f"test/{pol}/{kind}/{name}"] = v
        frames.append(pred_frame(ss, pred, {"split": "test", "origin_policy": pol}))
    return ArmResult(arm, metrics, pd.concat(frames, ignore_index=True), secs)


# --------------------------------------------------------------------------------------
# Orchestration + MLflow
# --------------------------------------------------------------------------------------
def _file_sha(path: Path) -> str:
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def run_transfer(
    *,
    task: str = "forecast",
    datasets: tuple[str, ...] = ("nasa", "calce"),
    seeds: tuple[int, ...] = (0, 1, 2, 3, 4),
    arms: tuple[str, ...] = ARMS,
    folds: tuple[str, ...] | None = None,
    do_pretrain: bool = False,
    model_name: str = "itransformer",
    device: str = "auto",
    theta: float = 0.8,
    processed_dir: str | None = None,
    tracking_uri: str | None = None,
    experiment: str = "transfer",
) -> dict[str, Any]:
    """Run the pre-registered transfer experiment; one MLflow run per (arm, dataset, fold, seed)."""
    import mlflow

    from battery_rul.tasks.labels import label_source
    from battery_rul.train.runner import (
        finished_unit_keys,
        get_experiment_id,
        git_info,
    )

    if task not in ("forecast", "rul"):
        raise NotImplementedError("transfer supports Task B (forecast) and Task C (rul)")
    if task == "rul" and "few_shot" in arms:
        # RUL labels of the test cell's own cycles <= T_p need its future EOL: not leakage-free.
        raise ValueError("few_shot is undefined for rul (its labels need the test cell's EOL)")
    pdir = processed_dir or str(PROCESSED_DIR)
    uri = tracking_uri or default_tracking_uri()
    params, lookback, src = load_params(model_name, task)
    log.info("transfer params for %s/%s: %s", model_name, task, src)
    out: dict[str, Any] = {"params_source": src, "pretrain": None, "runs": []}
    if do_pretrain:
        pr = pretrain(
            model_name,
            params,
            task,
            lookback=lookback,
            device=device,
            processed_dir=pdir,
            theta=theta,
            params_source=src,
            tracking_uri=uri,
        )
        out["pretrain"] = pr
    ckpt = pretrained_path(model_name, task)
    needs_ckpt = any(a != "scratch" for a in arms)
    if needs_ckpt and not ckpt.exists():
        raise FileNotFoundError(f"{ckpt} missing; run with --pretrain first")
    ckpt_sha = _file_sha(ckpt) if ckpt.exists() else "none"

    exp_id = get_experiment_id(experiment, uri)
    done = finished_unit_keys(exp_id)
    sha, dirty = git_info()
    for ds in datasets:
        ctx = dataset_ctx(ds, pdir, theta)
        ids = sorted(ctx.cells["cell_id"].astype(str))
        for cell in ids:
            if folds and cell not in folds:
                continue
            bundle = build_bundle(ctx, ds, cell, task, lookback)
            for seed in seeds:
                for arm in arms:
                    ucfg = {
                        "dataset": ds,
                        "task": task,
                        "model": model_name,
                        "params": params,
                        "lookback": lookback,
                        "arm": arm,
                        "fold": cell,
                        "seed": seed,
                        "horizons": list(SHARED_HORIZONS),
                        "feature_set": "shared",
                        "theta": theta,
                        "pretrained": ckpt_sha if arm != "scratch" else "none",
                    }
                    key = config_hash(ucfg)
                    if key in done:
                        continue
                    res = run_arm(
                        arm,
                        bundle,
                        model_name=model_name,
                        params=params,
                        pretrained=ckpt if arm != "scratch" else None,
                        seed=seed,
                        device=device,
                    )
                    mlflow.set_tracking_uri(uri)
                    with mlflow.start_run(
                        experiment_id=exp_id,
                        run_name=f"{ds}/{task}/{model_name}+{arm}/{cell}/s{seed}",
                        tags={"unit_key": key, "dataset": ds, "task": task, "arm": arm},
                    ) as run:
                        mlflow.log_params(
                            {
                                "dataset": ds,
                                "task": task,
                                "model": f"{model_name}+{arm}",
                                "base_model": model_name,
                                "arm": arm,
                                "fold": cell,
                                "test_cell": cell,
                                "seed": seed,
                                "config_hash": key,
                                "git_sha": sha,
                                "git_dirty": dirty,
                                "protocol_version": "1.1",
                                "label_source": label_source(ds),
                                "theta": theta,
                                "feature_set": "shared",
                                "lookback": lookback,
                                "params_source": src,
                                "pretrained_sha": ucfg["pretrained"],
                                "eval_origins": ",".join(bundle.tests),
                                **{f"model.{k}": v for k, v in params.items()},
                            }
                        )
                        mlflow.log_metrics(res.metrics)
                        with tempfile.TemporaryDirectory() as td:
                            p = Path(td) / "predictions.parquet"
                            res.predictions.to_parquet(p, index=False)
                            mlflow.log_artifact(str(p))
                        out["runs"].append((ds, cell, seed, arm, run.info.run_id, res.metrics))
                    log.info("done %s %s %s s%d", ds, cell, arm, seed)
    return out
