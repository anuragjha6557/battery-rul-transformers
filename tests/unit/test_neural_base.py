"""Shared neural trainer: overfit wiring, determinism, quantile monotonicity, target transforms."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest
import torch
from torch import nn

from battery_rul.models.base import Model, SampleSet
from battery_rul.models.neural import NeuralModel, last_valid_soh
from battery_rul.utils import seed_everything


class _MLP(nn.Module):
    def __init__(self, c: int, f: int, L: int, h: int, q: int) -> None:
        super().__init__()
        self.h, self.q = h, q
        self.net = nn.Sequential(nn.Linear(c * L + f, 64), nn.ReLU(), nn.Linear(64, h * q))

    def forward(self, xh: torch.Tensor, xt: torch.Tensor) -> torch.Tensor:
        z = torch.cat([xh.flatten(1), xt], dim=1)
        return self.net(z).view(-1, self.h, self.q)


class TinyMLP(NeuralModel):
    name = "tiny_mlp"

    def build_module(self, n_channels: int, n_tab: int, lookback: int, n_h: int, n_q: int):
        return _MLP(n_channels, n_tab, lookback, n_h, n_q)


def _samples(n: int = 64, task: str = "forecast", seed: int = 0) -> SampleSet:
    rng = np.random.default_rng(seed)
    L, H = 8, (1, 5)
    slope = rng.uniform(0.001, 0.004, n)
    base = rng.uniform(0.85, 1.0, n)
    hist = base[:, None] - slope[:, None] * np.arange(L)[None, :]
    if task == "forecast":
        y = np.stack([hist[:, -1] - slope * h for h in H], axis=1)
        hz = H
    else:  # rul
        y = ((hist[:, -1] - 0.8) / slope)[:, None]
        hz = (0,)
    return SampleSet(
        task=task,  # type: ignore[arg-type]
        x_hist=hist[:, :, None].astype(np.float32),
        hist_mask=np.ones((n, L), bool),
        x_tab=slope[:, None].astype(np.float32) * 100,
        y=y.astype(np.float32),
        y_mask=np.ones_like(y, dtype=bool),
        horizons=hz,
        channel_names=("soh",),
        feature_names=("slope",),
        meta=pd.DataFrame({"dataset": "x", "cell_id": "c", "origin_cycle": np.arange(n)}),
    )


def test_conforms_to_model_protocol() -> None:
    assert isinstance(TinyMLP(device="cpu"), Model)


def test_overfits_one_batch_point() -> None:
    s = _samples()
    m = TinyMLP(quantiles=None, lr=3e-3, max_epochs=400, patience=400, device="cpu")
    seed_everything(0)
    m.fit(s, val=s)
    err = np.abs(m.predict(s).point - s.y)
    # targets span ~0.15 SOH; fitting them to ~0.1 %SOH proves the loop/loss/targets are wired
    assert err.mean() < 1e-3 and err.max() < 5e-3


@pytest.mark.parametrize("task", ["forecast", "rul"])
def test_quantile_outputs_monotone_and_median_is_point(task: str) -> None:
    s = _samples(task=task)
    m = TinyMLP(max_epochs=30, patience=30, device="cpu")
    seed_everything(0)
    m.fit(s, val=s)
    p = m.predict(s)
    assert p.quantiles is not None
    assert (np.diff(p.quantiles, axis=2) >= 0).all()
    np.testing.assert_allclose(p.point, p.quantiles[..., 2])
    if task == "rul":
        assert (p.point >= 0).all()


def test_deterministic_on_cpu() -> None:
    s = _samples()
    preds = []
    for _ in range(2):
        seed_everything(123)
        m = TinyMLP(quantiles=None, max_epochs=5, patience=5, device="cpu")
        m.fit(s, val=s)
        preds.append(m.predict(s).point)
    np.testing.assert_array_equal(preds[0], preds[1])


def test_untrained_residual_target_is_persistence() -> None:
    """With an all-zero module, forecasts equal the last observed SOH (residual targets)."""
    s = _samples()
    m = TinyMLP(quantiles=None, max_epochs=1, device="cpu")
    m.fit(s)
    assert m.module is not None
    for p in m.module.parameters():
        nn.init.zeros_(p)
    np.testing.assert_allclose(
        m.predict(s).point, np.repeat(last_valid_soh(s)[:, None], 2, axis=1), atol=1e-6
    )


def test_quantiles_must_include_median() -> None:
    with pytest.raises(ValueError, match="median"):
        TinyMLP(quantiles=(0.1, 0.9))
