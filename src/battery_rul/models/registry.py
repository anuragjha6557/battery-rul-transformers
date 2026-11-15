"""Name -> model factory registry used by the benchmark runner.

Lazy by design: model modules are imported only when a model is constructed. On macOS, torch
and LightGBM each load their own OpenMP runtime, and the two cannot coexist in one process (a
torch-first process aborts LightGBM with ``OMP: Error #179``; a LightGBM-first process segfaults
in torch's parallel ops). Keeping imports lazy lets the runner keep each family in its own worker
process (:func:`omp_family`). Linux CI and the HF Space are unaffected (both use libgomp).

Optional class-level traits (read with :func:`model_trait`, default ``True`` when absent):

- ``cross_fit``: fit one sub-model per inner fold (CV+, PROTOCOL §3). Models with nothing to
  fit (level-0 baselines) set it ``False`` so the runner fits once.
- ``tunable``: the model has hyperparameters that must come from a tuning run (PROTOCOL §4
  rule 6). Models with none set it ``False``.
"""

from __future__ import annotations

import importlib
import inspect
from collections.abc import Callable, Iterator, Mapping
from typing import Any, Literal

from battery_rul.models.base import Model

OmpFamily = Literal["torch", "lightgbm"]

#: Keys are the ``name`` field of ``configs/model/*.yaml`` (one class may back several configs).
#: Values: (``"module:ClassName"``, OpenMP family or None).
_PATHS: dict[str, tuple[str, OmpFamily | None]] = {
    "persistence": ("battery_rul.models.persistence:Persistence", None),
    "last_slope": ("battery_rul.models.persistence:LastSlope", None),
    "prev_soh": ("battery_rul.models.extrapolate:PrevSOH", None),
    "param_linear": ("battery_rul.models.extrapolate:ParamFit", None),
    "param_exp2": ("battery_rul.models.extrapolate:ParamFit", None),
    "param_power": ("battery_rul.models.extrapolate:ParamFit", None),
    "gpr": ("battery_rul.models.extrapolate:GPRExtrap", None),
    "elasticnet": ("battery_rul.models.tabular:ElasticNetModel", None),
    "lgbm": ("battery_rul.models.tabular:LGBMModel", "lightgbm"),
    "nlinear": ("battery_rul.models.linear:NLinear", "torch"),
    "dlinear": ("battery_rul.models.linear:DLinear", "torch"),
    "rlinear": ("battery_rul.models.linear:RLinear", "torch"),
    "lstm": ("battery_rul.models.recurrent:RecurrentModel", "torch"),  # params set cell=lstm
    "gru": ("battery_rul.models.recurrent:RecurrentModel", "torch"),  # params set cell=gru
    "transformer": ("battery_rul.models.transformer:TimeTransformer", "torch"),
    "patchtst": ("battery_rul.models.patchtst:PatchTST", "torch"),
    "itransformer": ("battery_rul.models.itransformer:ITransformer", "torch"),  # channels=all
    "itransformer_sc": ("battery_rul.models.itransformer:ITransformer", "torch"),  # channels=soh
}


def _load(path: str) -> Callable[..., Model]:
    module, cls = path.split(":")
    return getattr(importlib.import_module(module), cls)


class _LazyModels(Mapping[str, Callable[..., Model]]):
    """Mapping view that imports a model class on first access. Tests may register extra
    factories with ``MODELS[name] = factory``."""

    def __init__(self) -> None:
        self._extra: dict[str, Callable[..., Model]] = {}

    def __getitem__(self, name: str) -> Callable[..., Model]:
        if name in self._extra:
            return self._extra[name]
        return _load(_PATHS[name][0])

    def __setitem__(self, name: str, factory: Callable[..., Model]) -> None:
        self._extra[name] = factory

    def __delitem__(self, name: str) -> None:
        del self._extra[name]

    def pop(self, name: str, default: Any = None) -> Any:
        """Remove a test-registered factory (built-in entries cannot be removed)."""
        return self._extra.pop(name, default)

    def __iter__(self) -> Iterator[str]:
        return iter([*_PATHS, *self._extra])

    def __len__(self) -> int:
        return len(_PATHS) + len(self._extra)

    def __contains__(self, name: object) -> bool:
        return name in _PATHS or name in self._extra


MODELS = _LazyModels()


def omp_family(name: str) -> OmpFamily | None:
    """Which OpenMP runtime the model's module loads (None: neither torch nor LightGBM)."""
    return _PATHS[name][1] if name in _PATHS else None


def make_model(name: str, **params: Any) -> Model:
    """Instantiate a registered model by name."""
    if name not in MODELS:
        raise KeyError(f"unknown model {name!r}; registered: {sorted(MODELS)}")
    return MODELS[name](**params)


def model_trait(model_or_factory: Any, trait: str, default: bool = True) -> bool:
    """Read an optional boolean class trait (``cross_fit`` / ``tunable``)."""
    return bool(getattr(model_or_factory, trait, default))


def accepts_kwarg(factory: Callable[..., Any], kwarg: str) -> bool:
    """True if ``factory(**{kwarg: ...})`` is a valid call."""
    try:
        params = inspect.signature(factory).parameters
    except (TypeError, ValueError):  # pragma: no cover - builtins without signatures
        return False
    return kwarg in params or any(p.kind is inspect.Parameter.VAR_KEYWORD for p in params.values())
