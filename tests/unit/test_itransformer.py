"""iTransformer: contract, residual convention, channel mixing (vs PatchTST's independence)."""

from __future__ import annotations

import itertools

import numpy as np
import pandas as pd
import pytest
import torch

from battery_rul.models.base import Model, SampleSet
from battery_rul.models.itransformer import ITransformer, fill_and_normalise
from battery_rul.models.neural import last_valid_soh
from battery_rul.models.transformer import MAX_PARAMS, count_params
from battery_rul.utils import seed_everything


def _samples(n: int = 64, L: int = 16, c_exog: int = 3, task: str = "forecast") -> SampleSet:
    rng = np.random.default_rng(0)
    slope = rng.uniform(0.001, 0.004, n)
    soh = rng.uniform(0.85, 1.0, n)[:, None] - slope[:, None] * np.arange(L)[None, :]
    # exogenous channel 1 carries the slope (so channel mixing is *useful*), others are noise
    exog = np.concatenate(
        [np.repeat(slope[:, None, None] * 300, L, axis=1), rng.normal(size=(n, L, c_exog - 1))],
        axis=2,
    )
    x = np.concatenate([soh[..., None], exog], axis=2).astype(np.float32)
    H = (1, 5)
    if task == "forecast":
        y = np.stack([soh[:, -1] - slope * h for h in H], 1)
        hz = H
    else:
        y = ((soh[:, -1] - 0.8) / slope)[:, None]
        hz = (0,)
    return SampleSet(
        task=task,  # type: ignore[arg-type]
        x_hist=x,
        hist_mask=np.ones((n, L), bool),
        x_tab=rng.normal(size=(n, 2)).astype(np.float32),
        y=y.astype(np.float32),
        y_mask=np.ones_like(y, dtype=bool),
        horizons=hz,
        channel_names=("soh", *[f"c{i}" for i in range(c_exog)]),
        feature_names=("t0", "t1"),
        meta=pd.DataFrame({"dataset": "x", "cell_id": "c", "origin_cycle": np.arange(n)}),
    )


def _model(**kw: object) -> ITransformer:
    base = dict(d_model=32, n_heads=2, n_layers=1, dropout=0.0, device="cpu")
    return ITransformer(**{**base, **kw})  # type: ignore[arg-type]


def test_conformance_and_shapes() -> None:
    s = _samples()
    for q in (None, (0.05, 0.25, 0.5, 0.75, 0.95)):
        m = _model(quantiles=q, max_epochs=2)
        assert isinstance(m, Model)
        m.fit(s, val=s)
        p = m.predict(s)
        assert p.point.shape == (len(s), 2)
        if q is not None:
            assert p.quantiles is not None and p.quantiles.shape == (len(s), 2, 5)


def test_zero_module_is_persistence() -> None:
    s = _samples()
    m = _model(quantiles=None, max_epochs=1)
    m.fit(s)
    assert m.module is not None
    for p in m.module.parameters():
        torch.nn.init.zeros_(p)
    np.testing.assert_allclose(
        m.predict(s).point, np.repeat(last_valid_soh(s)[:, None], 2, 1), atol=1e-6
    )


def test_overfits_small_batch() -> None:
    s = _samples()
    seed_everything(0)
    m = _model(quantiles=None, lr=3e-3, weight_decay=0.0, max_epochs=400, patience=400)
    m.fit(s, val=s)
    err = np.abs(m.predict(s).point - s.y)
    assert err.mean() < 1e-3


def test_channels_mix_in_mc_and_are_ignored_in_sc() -> None:
    """MC: perturbing an exogenous channel changes the SOH forecast (variate attention).
    SC: it cannot. This is the property PatchTST's channel independence removes."""
    s = _samples()
    pert = s.x_hist.copy()
    pert[..., 2] += 5.0
    s2 = SampleSet(**{**s.__dict__, "x_hist": pert})
    for channels, should_change in (("all", True), ("soh", False)):
        seed_everything(1)
        m = _model(channels=channels, quantiles=None, max_epochs=3)
        m.fit(s)
        changed = not np.allclose(m.predict(s).point, m.predict(s2).point)
        assert changed is should_change, channels


def test_fill_and_normalise_ignores_padding() -> None:
    x = torch.tensor([[[9.0, 0.0], [9.0, 0.0], [1.0, 1.0], [0.9, 1.0], [0.8, 1.0]]])
    z, loc, scale = fill_and_normalise(x)
    assert loc.item() == pytest.approx(0.8)
    # padded steps take the first valid value, so they don't distort the scale
    assert z.shape == (1, 1, 5) and torch.isfinite(z).all()
    assert scale.item() == pytest.approx(float(np.std([1.0, 0.9, 0.8])), rel=1e-5)


def test_rul_task_trains_and_is_nonnegative() -> None:
    s = _samples(task="rul")
    m = _model(max_epochs=5)
    m.fit(s, val=s)
    assert (m.predict(s).point >= 0).all()


@pytest.mark.parametrize(
    ("d_model", "n_heads", "n_layers", "lookback"),
    list(itertools.product([32, 64, 128], [2, 4], [1, 2, 3], [16, 32, 64])),
)
def test_param_cap_over_search_space(
    d_model: int, n_heads: int, n_layers: int, lookback: int
) -> None:
    m = _model(d_model=d_model, n_heads=n_heads, n_layers=n_layers)
    m._task = "forecast"
    module = m.build_module(n_channels=14, n_tab=10, lookback=lookback, n_h=8, n_q=5)
    assert count_params(module) <= MAX_PARAMS
