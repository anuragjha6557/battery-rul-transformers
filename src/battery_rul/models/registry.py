"""Name -> model factory registry used by the benchmark runner.

Optional class-level traits (read with :func:`model_trait`, default ``True`` when absent):

- ``cross_fit``: fit one sub-model per inner fold (CV+, PROTOCOL §3). Models with nothing to
  fit (level-0 baselines) set it ``False`` so the runner fits once.
- ``tunable``: the model has hyperparameters that must come from a tuning run (PROTOCOL §4
  rule 6). Models with none set it ``False``.
"""

from __future__ import annotations

import inspect
from collections.abc import Callable
from typing import Any

from battery_rul.models.base import Model
from battery_rul.models.extrapolate import GPRExtrap, ParamFit, PrevSOH
from battery_rul.models.linear import DLinear, NLinear, RLinear
from battery_rul.models.persistence import LastSlope, Persistence
from battery_rul.models.recurrent import RecurrentModel
from battery_rul.models.tabular import ElasticNetModel, LGBMModel
from battery_rul.models.transformer import TimeTransformer

#: Keys are the ``name`` field of ``configs/model/*.yaml`` (one class may back several configs,
#: e.g. ParamFit with ``kind`` linear / exp2 / power).
MODELS: dict[str, Callable[..., Model]] = {
    Persistence.name: Persistence,
    LastSlope.name: LastSlope,
    "prev_soh": PrevSOH,
    "param_linear": ParamFit,
    "param_exp2": ParamFit,
    "param_power": ParamFit,
    "gpr": GPRExtrap,
    "elasticnet": ElasticNetModel,
    "lgbm": LGBMModel,
    "nlinear": NLinear,
    "dlinear": DLinear,
    "rlinear": RLinear,
    "lstm": RecurrentModel,  # config params set cell=lstm
    "gru": RecurrentModel,  # config params set cell=gru
    "transformer": TimeTransformer,
}


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
