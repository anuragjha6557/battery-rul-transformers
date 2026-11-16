"""LSTM / GRU baseline (the IEEE ITEC 2024 paper's recurrent comparison).

Deviation from the paper, on purpose: the paper rolls a one-step model forward recursively;
here the last hidden state feeds a *direct* multi-horizon head (PROTOCOL §2), so no teacher
forcing or error compounding is involved.

Input is all ``C`` history channels (incl. the appended mask channel). Histories are
left-padded, so the final time step is always a real observation and ``h_n`` of the top layer
summarises the window. Tabular features go through a small MLP and are concatenated.
"""

from __future__ import annotations

from typing import Any

import torch
from torch import nn

from battery_rul.models.neural import NeuralModel, revin_inputs

TAB_HIDDEN = 32
_ALLOWED_ARCH = {"cell", "hidden", "layers", "dropout", "lookback"}


class _Recurrent(nn.Module):
    def __init__(
        self,
        cell: str,
        n_channels: int,
        n_tab: int,
        n_h: int,
        n_q: int,
        hidden: int,
        layers: int,
        dropout: float,
        revin: bool = False,
        denorm_soh: bool = False,
    ) -> None:
        super().__init__()
        self.revin, self.denorm_soh = revin, denorm_soh
        rnn = {"lstm": nn.LSTM, "gru": nn.GRU}[cell]
        self.rnn = rnn(
            n_channels,
            hidden,
            num_layers=layers,
            batch_first=True,
            dropout=dropout if layers > 1 else 0.0,
        )
        self.tab: nn.Module = (
            nn.Sequential(nn.Linear(n_tab, TAB_HIDDEN), nn.ReLU()) if n_tab else nn.Identity()
        )
        self.head = nn.Linear(hidden + (TAB_HIDDEN if n_tab else 0), n_h * n_q)
        self.n_h, self.n_q, self.has_tab = n_h, n_q, n_tab > 0

    def forward(self, x_hist: torch.Tensor, x_tab: torch.Tensor) -> torch.Tensor:
        scale = None
        if self.revin:
            x_hist, scale = revin_inputs(x_hist)
        _, state = self.rnn(x_hist)
        h = state[0] if isinstance(state, tuple) else state  # LSTM: (h_n, c_n)
        z = h[-1]
        if self.has_tab:
            z = torch.cat([z, self.tab(x_tab)], dim=1)
        out = self.head(z).view(-1, self.n_h, self.n_q)
        if scale is not None and self.denorm_soh:
            out = out * scale
        return out


class RecurrentModel(NeuralModel):
    """``cell`` in {"lstm", "gru"}; ``hidden``, ``layers``, ``dropout`` as in PyTorch."""

    name = "recurrent"

    def __init__(
        self,
        *,
        cell: str = "lstm",
        hidden: int = 64,
        layers: int = 2,
        dropout: float = 0.1,
        revin: bool = False,
        **kwargs: Any,
    ) -> None:
        self.revin = revin  # opt-in instance normalisation (ADR-0013 E); not an arch param
        if cell not in ("lstm", "gru"):
            raise ValueError("cell must be 'lstm' or 'gru'")
        super().__init__(cell=cell, hidden=hidden, layers=layers, dropout=dropout, **kwargs)
        extra = set(self.arch) - _ALLOWED_ARCH
        if extra:
            raise TypeError(f"unexpected architecture arguments {sorted(extra)}")

    def build_module(
        self, n_channels: int, n_tab: int, lookback: int, n_h: int, n_q: int
    ) -> nn.Module:
        a = self.arch
        return _Recurrent(
            a["cell"],
            n_channels,
            n_tab,
            n_h,
            n_q,
            int(a["hidden"]),
            int(a["layers"]),
            a["dropout"],
            self.revin,
            getattr(self, "_task", "forecast") != "rul",
        )
