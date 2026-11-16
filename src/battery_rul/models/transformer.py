"""The paper's "vanilla Transformer" baseline: one token per time step.

Linear(C -> d_model) embeds each step, a learned positional embedding is added, a pre-norm
``nn.TransformerEncoder`` mixes steps (padded steps are excluded through the key-padding mask
built from the mask channel), valid tokens are mean-pooled and concatenated with an MLP of the
tabular features, and a linear head emits all ``H * Q`` outputs directly.

Parameter cap (PROTOCOL §6, <= 250 k): a transformer layer costs ~``4 d^2 + 2 d * ff``, so the
corner ``d_model=128, n_layers=3`` with the standard ``ff_mult=4`` would be ~600 k. When the
requested width would exceed the cap, the feed-forward width is shrunk (never the attention
dims, which the search space controls) until the module fits. This is deterministic in the
config, only triggers in the largest corner of the search space, and is reported in
``FitInfo.extra['n_params']``.
"""

from __future__ import annotations

from typing import Any

import torch
from torch import nn

from battery_rul.models.neural import NeuralModel, revin_inputs

MAX_PARAMS = 250_000
TAB_HIDDEN = 32
_ALLOWED_ARCH = {"d_model", "n_heads", "n_layers", "dropout", "ff_mult", "lookback"}


def count_params(module: nn.Module) -> int:
    return sum(p.numel() for p in module.parameters())


class _TimeTransformer(nn.Module):
    def __init__(
        self,
        n_channels: int,
        n_tab: int,
        lookback: int,
        n_h: int,
        n_q: int,
        d_model: int,
        n_heads: int,
        n_layers: int,
        dropout: float,
        ff_dim: int,
        revin: bool = False,
        denorm_soh: bool = False,
    ) -> None:
        super().__init__()
        self.revin, self.denorm_soh = revin, denorm_soh
        self.embed = nn.Linear(n_channels, d_model)
        self.pos = nn.Parameter(torch.zeros(1, lookback, d_model))
        nn.init.normal_(self.pos, std=0.02)
        layer = nn.TransformerEncoderLayer(
            d_model,
            n_heads,
            dim_feedforward=ff_dim,
            dropout=dropout,
            batch_first=True,
            norm_first=True,
        )
        self.encoder = nn.TransformerEncoder(
            layer, n_layers, norm=nn.LayerNorm(d_model), enable_nested_tensor=False
        )
        self.tab: nn.Module = (
            nn.Sequential(nn.Linear(n_tab, TAB_HIDDEN), nn.ReLU()) if n_tab else nn.Identity()
        )
        self.head = nn.Linear(d_model + (TAB_HIDDEN if n_tab else 0), n_h * n_q)
        self.n_h, self.n_q, self.has_tab = n_h, n_q, n_tab > 0

    def forward(self, x_hist: torch.Tensor, x_tab: torch.Tensor) -> torch.Tensor:
        scale = None
        if self.revin:
            x_hist, scale = revin_inputs(x_hist)
        valid = x_hist[:, :, -1] > 0.5  # (B, L)
        h = self.embed(x_hist) + self.pos
        h = self.encoder(h, src_key_padding_mask=~valid)
        w = valid.to(h.dtype).unsqueeze(-1)
        z = (h * w).sum(1) / w.sum(1).clamp_min(1.0)
        if self.has_tab:
            z = torch.cat([z, self.tab(x_tab)], dim=1)
        out = self.head(z).view(-1, self.n_h, self.n_q)
        if scale is not None and self.denorm_soh:
            out = out * scale
        return out


class TimeTransformer(NeuralModel):
    """Vanilla time-token Transformer; see module docstring."""

    name = "transformer"

    def __init__(
        self,
        *,
        d_model: int = 64,
        n_heads: int = 4,
        n_layers: int = 2,
        dropout: float = 0.1,
        ff_mult: int = 4,
        revin: bool = False,
        **kwargs: Any,
    ) -> None:
        self.revin = revin  # opt-in instance normalisation (ADR-0013 E); not an arch param
        super().__init__(
            d_model=d_model,
            n_heads=n_heads,
            n_layers=n_layers,
            dropout=dropout,
            ff_mult=ff_mult,
            **kwargs,
        )
        extra = set(self.arch) - _ALLOWED_ARCH
        if extra:
            raise TypeError(f"unexpected architecture arguments {sorted(extra)}")
        if d_model % n_heads:
            raise ValueError("d_model must be divisible by n_heads")

    def build_module(
        self, n_channels: int, n_tab: int, lookback: int, n_h: int, n_q: int
    ) -> nn.Module:
        a = self.arch
        ff = int(a["ff_mult"]) * int(a["d_model"])
        while True:
            module = _TimeTransformer(
                n_channels,
                n_tab,
                lookback,
                n_h,
                n_q,
                int(a["d_model"]),
                int(a["n_heads"]),
                int(a["n_layers"]),
                float(a["dropout"]),
                ff,
                self.revin,
                getattr(self, "_task", "forecast") != "rul",
            )
            if count_params(module) <= MAX_PARAMS or ff <= 4:
                return module
            ff = max(4, ff * 3 // 4)
