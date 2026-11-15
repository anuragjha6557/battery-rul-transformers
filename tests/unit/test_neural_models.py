"""Phase-4 neural baselines: NLinear / DLinear / RLinear / LSTM / GRU / Transformer."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import numpy as np
import pandas as pd
import pytest
import torch
from torch import nn

from battery_rul.models.base import Model, SampleSet
from battery_rul.models.linear import DLinear, NLinear, RLinear
from battery_rul.models.neural import NeuralModel, last_valid_soh
from battery_rul.models.recurrent import RecurrentModel
from battery_rul.models.transformer import MAX_PARAMS, TimeTransformer
from battery_rul.utils import seed_everything

L, HZ = 8, (1, 5)


def _samples(n: int = 48, pad: int = 0, seed: int = 0) -> SampleSet:
    """Linear SOH decay with 2 extra channels; the first ``pad`` steps are NaN-padded."""
    rng = np.random.default_rng(seed)
    slope = rng.uniform(0.001, 0.004, n)
    base = rng.uniform(0.85, 1.0, n)
    soh = base[:, None] - slope[:, None] * np.arange(L)[None, :]
    hist = np.stack([soh, rng.normal(size=(n, L)), rng.normal(size=(n, L))], axis=2)
    mask = np.ones((n, L), bool)
    if pad:
        hist[:, :pad] = np.nan
        mask[:, :pad] = False
    y = np.stack([soh[:, -1] - slope * h for h in HZ], axis=1)
    return SampleSet(
        task="forecast",
        x_hist=hist.astype(np.float32),
        hist_mask=mask,
        x_tab=(slope[:, None] * 100).astype(np.float32),
        y=y.astype(np.float32),
        y_mask=np.ones_like(y, dtype=bool),
        horizons=HZ,
        channel_names=("soh", "a", "b"),
        feature_names=("slope",),
        meta=pd.DataFrame({"dataset": "x", "cell_id": "c", "origin_cycle": np.arange(n)}),
    )


Factory = Callable[..., NeuralModel]
FACTORIES: dict[str, Factory] = {
    "nlinear": NLinear,
    "dlinear": DLinear,
    "rlinear": RLinear,
    "lstm": lambda **kw: RecurrentModel(cell="lstm", hidden=32, layers=1, dropout=0.0, **kw),
    "gru": lambda **kw: RecurrentModel(cell="gru", hidden=32, layers=1, dropout=0.0, **kw),
    "transformer": lambda **kw: TimeTransformer(
        d_model=32, n_heads=2, n_layers=1, dropout=0.0, **kw
    ),
}
NAMES = list(FACTORIES)


@pytest.mark.parametrize("name", NAMES)
def test_conforms_to_model_protocol(name: str) -> None:
    assert isinstance(FACTORIES[name](device="cpu"), Model)


@pytest.mark.parametrize("name", NAMES)
@pytest.mark.parametrize("q", [1, 5])
def test_output_shape(name: str, q: int) -> None:
    s = _samples()
    quantiles = None if q == 1 else (0.05, 0.25, 0.5, 0.75, 0.95)
    m = FACTORIES[name](quantiles=quantiles, max_epochs=1, device="cpu")
    m.fit(s)
    assert m.module is not None
    xh, xt = m._x(s)
    assert m.module(xh, xt).shape == (len(s), len(HZ), q)
    assert m.predict(s).point.shape == s.y.shape


@pytest.mark.parametrize("name", NAMES)
def test_overfits_small_batch(name: str) -> None:
    s = _samples()
    lr, epochs = (3e-3, 3000) if name.endswith("linear") else (1e-2, 1000)
    m = FACTORIES[name](
        quantiles=None, lr=lr, weight_decay=0.0, max_epochs=epochs, patience=epochs, device="cpu"
    )
    seed_everything(0)
    m.fit(s, val=s)
    err = np.abs(m.predict(s).point - s.y)
    assert err.mean() < 1e-3


@pytest.mark.parametrize("name", NAMES)
def test_handles_nan_padded_history(name: str) -> None:
    s = _samples(pad=5)
    m = FACTORIES[name](max_epochs=3, device="cpu")
    m.fit(s, val=s)
    p = m.predict(s)
    assert np.isfinite(p.point).all() and p.quantiles is not None
    assert np.isfinite(p.quantiles).all()


@pytest.mark.parametrize("name", NAMES)
def test_zero_module_is_persistence(name: str) -> None:
    s = _samples(pad=3)
    m = FACTORIES[name](quantiles=None, max_epochs=1, device="cpu")
    m.fit(s)
    assert m.module is not None
    for p in m.module.parameters():
        nn.init.zeros_(p)
    np.testing.assert_allclose(
        m.predict(s).point, np.repeat(last_valid_soh(s)[:, None], len(HZ), axis=1), atol=1e-6
    )


def test_nlinear_extrapolates_linear_trend_exactly() -> None:
    train, test = _samples(n=64, seed=0), _samples(n=32, seed=1)
    m = NLinear(
        quantiles=None, lr=3e-2, weight_decay=0.0, max_epochs=1500, patience=1500, device="cpu"
    )
    seed_everything(0)
    m.fit(train, val=train)
    err = np.abs(m.predict(test).point - test.y)  # unseen slopes and levels
    assert err.max() < 1e-3  # SOH fraction (0.1 %SOH); the floor is float32 round-off


@pytest.mark.parametrize("use_exog", [False, True])
def test_linear_exog_flag(use_exog: bool) -> None:
    s = _samples()
    m = NLinear(use_exog=use_exog, quantiles=None, max_epochs=1, device="cpu")
    m.fit(s)
    assert m.module is not None
    names = {n for n, _ in m.module.named_parameters()}
    assert ("exog.weight" in names) is use_exog


def test_linear_ignores_other_channels_by_default() -> None:
    s = _samples()
    m = DLinear(quantiles=None, max_epochs=2, device="cpu")
    m.fit(s)
    s2 = SampleSet(**{**s.__dict__, "x_hist": s.x_hist.copy(), "x_tab": s.x_tab * 7})
    s2.x_hist[:, :, 1:] += 5.0
    np.testing.assert_allclose(m.predict(s).point, m.predict(s2).point, atol=1e-6)


def test_unknown_arch_kwarg_rejected() -> None:
    with pytest.raises(TypeError):
        NLinear(hidden=3)


# -- parameter cap over the whole search space -------------------------------------------------
# Realistic worst case for inputs: 13 history channels + mask, 10 tab features, L=64, 8 horizons.
C, F, LB, H, Q = 14, 10, 64, 8, 5


def _n_params(module: nn.Module) -> int:
    return sum(p.numel() for p in module.parameters())


def _build(model: NeuralModel) -> nn.Module:
    return model.build_module(C, F, LB, H, Q)


@pytest.mark.parametrize("cell", ["lstm", "gru"])
def test_recurrent_max_config_within_budget(cell: str) -> None:
    m = RecurrentModel(cell=cell, hidden=128, layers=2, dropout=0.3, device="cpu")
    assert _n_params(_build(m)) <= MAX_PARAMS


@pytest.mark.parametrize("d_model", [32, 64, 128])
@pytest.mark.parametrize("n_layers", [1, 2, 3])
def test_transformer_whole_grid_within_budget(d_model: int, n_layers: int) -> None:
    for n_heads in (2, 4):
        m = TimeTransformer(d_model=d_model, n_heads=n_heads, n_layers=n_layers, device="cpu")
        assert _n_params(_build(m)) <= MAX_PARAMS


def test_linear_max_config_within_budget() -> None:
    for cls in (NLinear, DLinear, RLinear):
        assert _n_params(_build(cls(use_exog=True, device="cpu"))) <= MAX_PARAMS


def test_default_configs_build() -> None:
    kw: dict[str, Any] = {"device": "cpu"}
    for m in (
        NLinear(**kw),
        DLinear(**kw),
        RLinear(**kw),
        RecurrentModel(**kw),
        TimeTransformer(**kw),
    ):
        module = _build(m)
        out = module(torch.zeros(3, LB, C), torch.zeros(3, F))
        assert out.shape == (3, H, Q)
