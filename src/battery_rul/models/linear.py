"""Zeng et al. (2023) linear forecasters (NLinear, DLinear) and RLinear (Li et al. 2023).

"Are Transformers Effective for Time Series Forecasting?" (AAAI 2023): a single linear map from
the look-back window to the forecast horizon beats many Transformer forecasters. They are the
sanity floor of the neural ladder (PLAN §6.4): any deep model that cannot beat them is not
earning its parameters.

Conventions (shared by all three):

- **Channel independent**, as in the paper: only the SOH channel (channel 0) is read. The other
  history channels and ``x_tab`` are ignored unless ``use_exog=True``, in which case they are
  flattened and fed through one extra linear map whose output is *added* to the SOH branch.
- **Residual space.** ``NeuralModel`` trains on ``y - x_last`` (x_last = last observed SOH), so
  the zero function is persistence. NLinear's "subtract last, linear, add last" therefore
  reduces to ``Linear(x - x_last)`` here: the final "add back" is exactly what the base class
  does when it converts the residual back to SOH. DLinear and RLinear are expressed the same
  way (they work on the ``x - x_last`` series), so a zero-parameter module is persistence for all
  three and every model is invariant to the absolute SOH level.
- **Padding.** Short histories arrive left-padded with 0 and a 0 in the mask channel. Before any
  linear map, padded SOH positions are filled with the *first valid* value (flat extension into
  the past); zeros would look like a cliff from SOH 0 to ~1.
- Output ``(B, H, Q)``; ``Q`` quantile heads are just extra output units of the same linear map.
"""

from __future__ import annotations

from typing import Any, ClassVar

import torch
import torch.nn.functional as nnf
from torch import nn

from battery_rul.models.neural import SOH_CHANNEL, NeuralModel

MA_KERNEL = 25
_ALLOWED_ARCH = {"use_exog", "lookback"}  # lookback is consumed by the sample builder


def prepare_soh(x_hist: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    """Return ``(soh, last)``: SOH ``(B, L)`` with padding filled by the first valid value, and
    the last valid SOH ``(B, 1)``. The mask is the last channel of ``x_hist``."""
    soh = x_hist[:, :, SOH_CHANNEL]
    valid = x_hist[:, :, -1] > 0.5
    n = soh.shape[1]
    first_idx = valid.to(soh.dtype).argmax(dim=1, keepdim=True)
    first = soh.gather(1, first_idx)
    filled = torch.where(valid, soh, first)
    last_idx = n - 1 - valid.flip(1).to(soh.dtype).argmax(dim=1, keepdim=True)
    last = filled.gather(1, last_idx)
    return filled, last


def valid_mask(x_hist: torch.Tensor) -> torch.Tensor:
    return x_hist[:, :, -1] > 0.5


class _LinearForecaster(nn.Module):
    """Common plumbing: optional exogenous branch and reshape to (B, H, Q)."""

    def __init__(
        self, lookback: int, n_channels: int, n_tab: int, n_h: int, n_q: int, use_exog: bool
    ) -> None:
        super().__init__()
        self.n_h, self.n_q, self.lookback = n_h, n_q, lookback
        self.exog: nn.Linear | None = None
        if use_exog:
            self.exog = nn.Linear((n_channels - 1) * lookback + n_tab, n_h * n_q)

    def exog_term(self, x_hist: torch.Tensor, x_tab: torch.Tensor) -> torch.Tensor | float:
        if self.exog is None:
            return 0.0
        return self.exog(torch.cat([x_hist[:, :, 1:].flatten(1), x_tab], dim=1))


class _NLinear(_LinearForecaster):
    def __init__(self, *a: Any) -> None:
        super().__init__(*a)
        self.lin = nn.Linear(self.lookback, self.n_h * self.n_q)

    def forward(self, x_hist: torch.Tensor, x_tab: torch.Tensor) -> torch.Tensor:
        soh, last = prepare_soh(x_hist)
        out = self.lin(soh - last) + self.exog_term(x_hist, x_tab)
        return out.view(-1, self.n_h, self.n_q)


class _DLinear(_LinearForecaster):
    def __init__(self, *a: Any) -> None:
        super().__init__(*a)
        k = min(MA_KERNEL, self.lookback)
        self.kernel = k if k % 2 == 1 else k - 1  # odd so the average is centred
        self.lin_trend = nn.Linear(self.lookback, self.n_h * self.n_q)
        self.lin_seasonal = nn.Linear(self.lookback, self.n_h * self.n_q)

    def forward(self, x_hist: torch.Tensor, x_tab: torch.Tensor) -> torch.Tensor:
        soh, last = prepare_soh(x_hist)
        z = (soh - last)[:, None, :]  # (B, 1, L)
        p = (self.kernel - 1) // 2
        trend = nnf.avg_pool1d(nnf.pad(z, (p, p), mode="replicate"), self.kernel, stride=1)
        seasonal = z - trend
        out = (
            self.lin_trend(trend[:, 0])
            + self.lin_seasonal(seasonal[:, 0])
            + self.exog_term(x_hist, x_tab)
        )
        return out.view(-1, self.n_h, self.n_q)


class _RLinear(_LinearForecaster):
    """RevIN (affine) around one linear map.

    Deviation from vanilla RevIN, needed for the residual-target convention: the location
    statistic is the last valid SOH instead of the window mean, so the de-normalised output is
    already the residual ``y - x_last``. The scale is the std of the valid window.
    """

    EPS = 1e-8

    def __init__(self, *a: Any) -> None:
        super().__init__(*a)
        self.lin = nn.Linear(self.lookback, self.n_h * self.n_q)
        self.gamma = nn.Parameter(torch.ones(1))
        self.beta = nn.Parameter(torch.zeros(1))

    def forward(self, x_hist: torch.Tensor, x_tab: torch.Tensor) -> torch.Tensor:
        soh, last = prepare_soh(x_hist)
        valid = valid_mask(x_hist).to(soh.dtype)
        n = valid.sum(1, keepdim=True).clamp_min(1.0)
        mean = (soh * valid).sum(1, keepdim=True) / n
        var = (((soh - mean) ** 2) * valid).sum(1, keepdim=True) / n
        std = torch.sqrt(var + 1e-8)
        xn = (soh - last) / std * self.gamma + self.beta
        out_n = self.lin(xn) + self.exog_term(x_hist, x_tab)
        out = (out_n - self.beta) / (self.gamma + self.EPS * self.EPS)
        return (out * std).view(-1, self.n_h, self.n_q)  # std (B, 1) broadcasts over H*Q


class _LinearModel(NeuralModel):
    _impl: ClassVar[type[_LinearForecaster]]

    def __init__(self, *, use_exog: bool = False, **kwargs: Any) -> None:
        super().__init__(use_exog=use_exog, **kwargs)
        extra = set(self.arch) - _ALLOWED_ARCH
        if extra:
            raise TypeError(f"unexpected architecture arguments {sorted(extra)}")

    def build_module(
        self, n_channels: int, n_tab: int, lookback: int, n_h: int, n_q: int
    ) -> nn.Module:
        return self._impl(lookback, n_channels, n_tab, n_h, n_q, bool(self.arch["use_exog"]))


class NLinear(_LinearModel):
    """Linear(L -> H*Q) on ``soh - last``; see module docstring for the residual-space note."""

    name = "nlinear"
    _impl = _NLinear


class DLinear(_LinearModel):
    """Moving-average (kernel 25, replicate padding, clipped to L) trend/seasonal split with one
    Linear per component, outputs summed."""

    name = "dlinear"
    _impl = _DLinear


class RLinear(_LinearModel):
    """RevIN (affine) + Linear."""

    name = "rlinear"
    _impl = _RLinear
