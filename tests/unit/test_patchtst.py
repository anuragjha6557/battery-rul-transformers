"""PatchTST: conformance, persistence, channel independence, parameter cap."""

from __future__ import annotations

import itertools

import numpy as np
import pytest
import torch
from test_neural_models import HZ, _samples
from torch import nn

from battery_rul.models.base import Model, SampleSet
from battery_rul.models.neural import last_valid_soh
from battery_rul.models.patchtst import MAX_PARAMS, PatchTST, count_params
from battery_rul.utils import seed_everything

KW = {"patch_len": 4, "d_model": 32, "n_heads": 2, "n_layers": 1, "dropout": 0.0}


def _model(**kw: object) -> PatchTST:
    return PatchTST(**{**KW, "device": "cpu", **kw})  # type: ignore[arg-type]


def test_conforms_to_model_protocol() -> None:
    assert isinstance(_model(), Model)


@pytest.mark.parametrize("q", [1, 5])
@pytest.mark.parametrize("channels", ["soh", "all"])
def test_output_shape(q: int, channels: str) -> None:
    s = _samples()
    quantiles = None if q == 1 else (0.05, 0.25, 0.5, 0.75, 0.95)
    m = _model(quantiles=quantiles, channels=channels, max_epochs=1)
    m.fit(s)
    assert m.module is not None
    xh, xt = m._x(s)
    assert m.module(xh, xt).shape == (len(s), len(HZ), q)
    assert m.predict(s).point.shape == s.y.shape


def test_zero_module_is_persistence() -> None:
    s = _samples(pad=3)
    m = _model(quantiles=None, max_epochs=1)
    m.fit(s)
    assert m.module is not None
    for p in m.module.parameters():
        nn.init.zeros_(p)
    np.testing.assert_allclose(
        m.predict(s).point, np.repeat(last_valid_soh(s)[:, None], len(HZ), axis=1), atol=1e-6
    )


def test_overfits_small_batch() -> None:
    s = _samples()
    m = _model(quantiles=None, lr=1e-2, weight_decay=0.0, max_epochs=1000, patience=1000)
    seed_everything(0)
    m.fit(s, val=s)
    assert np.abs(m.predict(s).point - s.y).mean() < 1e-3


def test_channel_independence_exact() -> None:
    s = _samples()
    m = _model(channels="all", max_epochs=2)
    m.fit(s)
    s2 = SampleSet(**{**s.__dict__, "x_hist": s.x_hist.copy(), "x_tab": s.x_tab * 7})
    s2.x_hist[:, :, 1:] += 5.0
    s2.x_hist[:, :, 1] *= -3.0
    assert np.array_equal(m.predict(s).point, m.predict(s2).point)


def test_padded_short_histories() -> None:
    s = _samples(pad=6)  # 2 valid steps of 8
    m = _model(max_epochs=3, channels="all")
    m.fit(s, val=s)
    p = m.predict(s)
    assert np.isfinite(p.point).all() and p.quantiles is not None
    assert np.isfinite(p.quantiles).all()


def test_unknown_arch_kwarg_rejected() -> None:
    with pytest.raises(TypeError):
        PatchTST(hidden=3)


# Realistic worst-case inputs: 13 history channels + mask, 10 tab features, 8 horizons, 5 quantiles
C, F, H, Q = 14, 10, 8, 5


@pytest.mark.parametrize("lookback", [16, 32, 64])
@pytest.mark.parametrize("patch_len", [4, 8, 16])
def test_all_lookback_patch_combos_run(lookback: int, patch_len: int) -> None:
    mod = PatchTST(patch_len=patch_len, device="cpu").build_module(C, F, lookback, H, Q)
    x = torch.randn(3, lookback, C)
    x[:, :, -1] = 1.0
    assert mod(x, torch.zeros(3, F)).shape == (3, H, Q)


def test_whole_grid_within_budget() -> None:
    for lb, pl, d, nh, nl, ch in itertools.product(
        (16, 32, 64), (4, 8, 16), (32, 64, 128), (2, 4), (1, 2, 3), ("soh", "all")
    ):
        m = PatchTST(patch_len=pl, d_model=d, n_heads=nh, n_layers=nl, channels=ch, device="cpu")
        assert count_params(m.build_module(C, F, lb, H, Q)) <= MAX_PARAMS, (lb, pl, d, nh, nl)
