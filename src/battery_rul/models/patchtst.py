"""PatchTST (Nie et al., ICLR 2023): channel-*independent* patch Transformer.

This is the deliberate foil to iTransformer's channel-*mixing* thesis (PLAN §6.4 row 7): every
channel is a separate univariate series; there is no operation anywhere that lets one channel
influence another's forecast.

- **Channels.** ``channels="soh"`` (default) reads only the SOH channel. ``channels="all"``
  pushes every non-mask channel through the same backbone as independent series (channels folded
  into the batch dimension, so weights are *shared*), then takes the SOH forecast from the SOH
  channel's output only. Channel independence means that this is functionally identical to
  ``"soh"`` (other channels receive no loss and cannot affect the SOH output, which the tests
  assert exactly); it exists to document that fact and to cost-match iTransformer's inputs. The
  paper's optional per-channel heads are not used: they would multiply head parameters by the
  channel count and the other heads' outputs would be discarded anyway. ``x_tab`` is ignored.
- **RevIN-style normalisation** (per instance, per channel): location = last valid value and
  scale = masked std of the valid window, as in RLinear, so the de-normalised output is the
  residual ``y - x_last`` and the zero function is persistence. No affine parameters.
- **Padding.** Left-padded steps (mask 0) are filled with the first valid value before patching
  (``linear.prepare_soh``).
- **Patching.** ``stride = patch_len // 2``; the end is replicate-padded by ``stride``; each patch
  goes through Linear(patch_len -> d_model) + learned positional embedding, then a pre-norm
  ``nn.TransformerEncoder`` (LayerNorm rather than the paper's BatchNorm: BatchNorm over
  folded (batch*channel) tokens is unstable on MPS and train/eval-dependent). Head: flatten ->
  Linear(n_patches * d_model -> H * Q).
- **Parameter cap (PROTOCOL §6, <= 250 k).** The flatten head and the ``4 d^2 + 2 d ff`` encoder
  layers overflow in the largest corners (e.g. d_model 128, 3 layers, patch 4, lookback 64).
  The builder then deterministically shrinks the feed-forward width first, and if that is still
  not enough inserts a per-patch bottleneck ``Linear(d_model -> r)`` before the flatten head
  (r in 16, 8, 4). Only the largest corners trigger it; the default config is untouched.
"""

from __future__ import annotations

from typing import Any

import torch
import torch.nn.functional as nnf
from torch import nn

from battery_rul.models.linear import prepare_soh
from battery_rul.models.neural import SOH_CHANNEL, NeuralModel

MAX_PARAMS = 250_000
_ALLOWED_ARCH = {
    "patch_len",
    "d_model",
    "n_heads",
    "n_layers",
    "dropout",
    "channels",
    "lookback",
}


def count_params(module: nn.Module) -> int:
    return sum(p.numel() for p in module.parameters())


def _fill_and_last(series: torch.Tensor, valid: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    """series (B, L), valid (B, L) bool -> first-valid-filled series and last valid value (B,1)."""
    n = series.shape[1]
    first = series.gather(1, valid.to(series.dtype).argmax(dim=1, keepdim=True))
    filled = torch.where(valid, series, first)
    last_idx = n - 1 - valid.flip(1).to(series.dtype).argmax(dim=1, keepdim=True)
    return filled, filled.gather(1, last_idx)


class _PatchTST(nn.Module):
    def __init__(
        self,
        lookback: int,
        n_h: int,
        n_q: int,
        patch_len: int,
        d_model: int,
        n_heads: int,
        n_layers: int,
        dropout: float,
        ff_dim: int,
        bottleneck: int | None,
        all_channels: bool,
        n_field_vars: int = 0,
    ) -> None:
        super().__init__()
        #: Field setting (no SOH channel): every channel is encoded independently (PatchTST's
        #: design), tagged with a learned channel embedding, then mean-pooled across channels
        #: before the head - the minimal cross-channel readout needed to map signals to SOH.
        self.n_field_vars = n_field_vars
        self.patch_len = patch_len
        self.stride = max(1, patch_len // 2)
        self.n_patches = (lookback + self.stride - patch_len) // self.stride + 1
        self.n_h, self.n_q, self.all_channels = n_h, n_q, all_channels
        self.embed = nn.Linear(patch_len, d_model)
        self.pos = nn.Parameter(torch.zeros(1, self.n_patches, d_model))
        nn.init.normal_(self.pos, std=0.02)
        if n_field_vars:
            self.ch_emb = nn.Parameter(torch.zeros(n_field_vars, 1, d_model))
            nn.init.normal_(self.ch_emb, std=0.02)
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
        self.reduce: nn.Module = (
            nn.Linear(d_model, bottleneck) if bottleneck is not None else nn.Identity()
        )
        self.drop = nn.Dropout(dropout)
        self.head = nn.Linear(self.n_patches * (bottleneck or d_model), n_h * n_q)

    def _normalise(self, x_hist: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Series (B*K, L) in last-value/std units and their stds (B, 1) for the SOH channel."""
        valid = x_hist[:, :, -1] > 0.5
        n = valid.sum(1, keepdim=True).clamp_min(1).to(x_hist.dtype)
        field = bool(self.n_field_vars)
        chans = range(x_hist.shape[2] - 1) if (self.all_channels or field) else (SOH_CHANNEL,)
        xs, stds = [], []
        for c in chans:
            if c == SOH_CHANNEL and not field:
                filled, last = prepare_soh(x_hist)
            else:
                filled, last = _fill_and_last(x_hist[:, :, c], valid)
            mean = (filled * valid).sum(1, keepdim=True) / n
            std = torch.sqrt((((filled - mean) ** 2) * valid).sum(1, keepdim=True) / n + 1e-8)
            xs.append((filled - last) / std)
            stds.append(std)
        return torch.cat(xs, dim=0), stds[0]  # channel-major stacking: SOH block first

    def forward(self, x_hist: torch.Tensor, x_tab: torch.Tensor) -> torch.Tensor:
        b = x_hist.shape[0]
        xn, std = self._normalise(x_hist)  # (K*B, L)
        xn = nnf.pad(xn[:, None, :], (0, self.stride), mode="replicate")[:, 0]
        patches = xn.unfold(1, self.patch_len, self.stride)  # (K*B, P, patch_len)
        e = self.embed(patches) + self.pos
        if self.n_field_vars:  # channel-major blocks of B rows: add each channel's identity
            k = self.n_field_vars
            e = (e.view(k, b, *e.shape[1:]) + self.ch_emb[:, :, None, :]).view(k * b, *e.shape[1:])
        h = self.encoder(e)
        h = self.reduce(h)
        if self.n_field_vars:
            z = h.flatten(1).view(self.n_field_vars, b, -1).mean(dim=0)  # pool across channels
            return self.head(self.drop(z)).view(b, self.n_h, self.n_q)  # absolute SOH
        out = self.head(self.drop(h.flatten(1)))  # (K*B, H*Q)
        out = out[:b]  # SOH channel only: the other channels' forecasts are discarded
        return (out * std).view(b, self.n_h, self.n_q)


class PatchTST(NeuralModel):
    """Channel-independent PatchTST; see module docstring."""

    name = "patchtst"

    def __init__(
        self,
        *,
        patch_len: int = 8,
        d_model: int = 64,
        n_heads: int = 4,
        n_layers: int = 2,
        dropout: float = 0.1,
        channels: str = "soh",
        **kwargs: Any,
    ) -> None:
        super().__init__(
            patch_len=patch_len,
            d_model=d_model,
            n_heads=n_heads,
            n_layers=n_layers,
            dropout=dropout,
            channels=channels,
            **kwargs,
        )
        extra = set(self.arch) - _ALLOWED_ARCH
        if extra:
            raise TypeError(f"unexpected architecture arguments {sorted(extra)}")
        if d_model % n_heads:
            raise ValueError("d_model must be divisible by n_heads")
        if channels not in ("soh", "all"):
            raise ValueError("channels must be 'soh' or 'all'")

    def build_module(
        self, n_channels: int, n_tab: int, lookback: int, n_h: int, n_q: int
    ) -> nn.Module:
        a = self.arch
        d = int(a["d_model"])
        patch_len = min(int(a["patch_len"]), lookback)
        candidates: list[tuple[int, int | None]] = [(f * d, None) for f in (4, 3, 2, 1)]
        candidates += [(d // 2, None), (d // 4, None)]
        candidates += [(f, r) for r in (16, 8, 4) for f in (d, d // 2, d // 4)]
        module: nn.Module | None = None
        for ff, r in candidates:
            module = _PatchTST(
                lookback,
                n_h,
                n_q,
                patch_len,
                d,
                int(a["n_heads"]),
                int(a["n_layers"]),
                float(a["dropout"]),
                ff,
                r,
                a["channels"] == "all",
                (n_channels - 1) if getattr(self, "_field", False) else 0,
            )
            if count_params(module) <= MAX_PARAMS:
                break
        assert module is not None
        return module
