"""iTransformer (Liu et al., ICLR 2024) for battery prognostics: the source paper's method,
re-implemented cleanly (the official MIT-licensed repo was used as a reference, not vendored).

Inverted view: each *variate* (SOH, charge-phase channels, discharge history channels) is one
token whose embedding is ``Linear(L -> d_model)`` of its whole lookback window. Self-attention
then mixes **variates**, not time steps. This is the "multivariate correlation" thesis the paper
relied on, and PatchTST (channel-independent) is its direct foil in the benchmark.

Choices beyond the original, each documented as a deviation:
1. **Instance normalisation keeps the level.** Each variate is normalised by its last valid
   value (location) and masked std (scale), as in iTransformer's series stationarisation. The
   location and log-scale are *also* fed to the token embedding (``Linear(L + 2 -> d)``),
   because RUL depends on how far SOH is from the EOL threshold, which pure stationarisation
   discards.
2. **Learned variate embeddings.** Channels here have fixed meanings (unlike generic
   multivariate benchmarks), so a per-variate identity embedding is added to each token.
3. **Tabular summaries as tokens.** Each scalar feature in ``x_tab`` becomes one token
   (``x * w_f + b_f``), so attention can relate trajectory summaries to variates.
4. **Residual convention.** Forecasts are read from the SOH token. For soh/forecast tasks the
   output is multiplied by the SOH instance scale, so a zero module equals persistence (shared
   NeuralModel convention). For RUL the output is in the scaled-RUL target space.
5. **Padding.** Positions before the first valid cycle are filled with that cycle's value. The
   mask channel is *not* a token: it would encode history length, an age proxy for the first
   L cycles (PROTOCOL §4 rule 4).

Variants via ``channels``: ``"all"`` (MC, the paper's multi-channel model) and ``"soh"`` (SC,
one variate token plus tabular tokens; the degenerate case the paper never reported).

Rest-schedule token (ADR-0020 Stage 3, ``rest_token=True``, forecast with ``future_rest_seq``):
the past rest channel (``log_rest_s`` over the lookback, padding zeroed) and the planned rest of
the next K cycles (``rest_seq_*`` features) are concatenated into one series of length L + K and
embedded as one extra variate token (``Linear(L + K -> d)``). This is the inverted model's natural
way to take a known-future covariate: one token whose window spans past and future, instead of
K scalar tabular tokens (ADR-0016, where iTransformer gained least from the schedule).

Parameter cap (PROTOCOL §6, ≤ 250 k): as in ``transformer.py``, only the FFN width shrinks, and
only at the largest corner of the search space.
"""

from __future__ import annotations

from typing import Any, Literal

import torch
from torch import nn

from battery_rul.models.neural import NeuralModel
from battery_rul.models.transformer import MAX_PARAMS, count_params
from battery_rul.tasks.samples import REST_SEQ_PREFIX

Channels = Literal["all", "soh"]
_ALLOWED_ARCH = {
    "d_model",
    "n_heads",
    "n_layers",
    "dropout",
    "ff_mult",
    "channels",
    "use_tab",
    "lookback",
    "rest_token",
}
_EPS = 1e-3


def fill_and_normalise(x_hist: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Per-variate fill + instance normalisation.

    Args:
        x_hist: (B, L, V+1) with the validity mask as the last channel.
    Returns:
        z (B, V, L) normalised series, loc (B, V) last valid value, scale (B, V) masked std.
    """
    x, valid = x_hist[..., :-1], x_hist[..., -1:] > 0.5  # (B,L,V), (B,L,1)
    first_idx = valid.to(x.dtype).argmax(dim=1, keepdim=True).expand(-1, 1, x.shape[2])
    first = x.gather(1, first_idx)
    filled = torch.where(valid, x, first)
    n = x.shape[1]
    last_idx = (n - 1 - valid.flip(1).to(x.dtype).argmax(dim=1, keepdim=True)).expand(
        -1, 1, x.shape[2]
    )
    loc = filled.gather(1, last_idx)  # (B,1,V)
    w = valid.to(x.dtype)
    cnt = w.sum(dim=1, keepdim=True).clamp_min(1.0)
    mean = (filled * w).sum(dim=1, keepdim=True) / cnt
    var = (((filled - mean) ** 2) * w).sum(dim=1, keepdim=True) / cnt
    scale = var.sqrt().clamp_min(_EPS)
    z = (filled - loc) / scale
    return z.transpose(1, 2), loc[:, 0], scale[:, 0]


class _ITransformer(nn.Module):
    def __init__(
        self,
        n_vars: int,
        n_tab: int,
        lookback: int,
        n_h: int,
        n_q: int,
        d_model: int,
        n_heads: int,
        n_layers: int,
        dropout: float,
        ff: int,
        denorm_soh: bool,
        readout: str = "first",
        rest: tuple[int, list[int], list[int]] | None = None,
    ) -> None:
        """``rest``: (index of the past rest channel, x_tab columns of the future rest sequence,
        x_tab columns kept as tabular tokens); None = no rest token, every column is a token."""
        super().__init__()
        self.n_vars, self.n_tab, self.n_h, self.n_q = n_vars, n_tab, n_h, n_q
        self.denorm_soh = denorm_soh
        #: "first": read the SOH token (variate 0). "mean": pool all tokens (field setting: no
        #: SOH variate exists; health is a function of all the measured variates).
        self.readout = readout
        self.embed = nn.Linear(lookback + 2, d_model)
        self.var_emb = nn.Parameter(torch.zeros(n_vars, d_model))
        self.tab_w = nn.Parameter(torch.zeros(n_tab, d_model))
        self.tab_b = nn.Parameter(torch.zeros(n_tab, d_model))
        layer = nn.TransformerEncoderLayer(
            d_model, n_heads, ff, dropout, batch_first=True, norm_first=True
        )
        self.encoder = nn.TransformerEncoder(
            layer, n_layers, norm=nn.LayerNorm(d_model), enable_nested_tensor=False
        )
        self.head = nn.Linear(d_model, n_h * n_q)
        self.rest_ch = -1
        if rest is not None:
            self.rest_ch = rest[0]
            self.register_buffer("rest_idx", torch.tensor(rest[1], dtype=torch.long))
            self.register_buffer("keep_idx", torch.tensor(rest[2], dtype=torch.long))
            self.rest_embed = nn.Linear(lookback + len(rest[1]), d_model)
            self.rest_emb = nn.Parameter(torch.zeros(d_model))
        nn.init.normal_(self.var_emb, std=0.02)
        nn.init.normal_(self.tab_w, std=0.02)

    def forward(self, x_hist: torch.Tensor, x_tab: torch.Tensor) -> torch.Tensor:
        if x_hist.shape[2] - 1 != self.n_vars:  # SC variant: keep SOH (channel 0) + mask
            x_hist = torch.cat([x_hist[..., : self.n_vars], x_hist[..., -1:]], dim=2)
        z, loc, scale = fill_and_normalise(x_hist)
        stats = torch.stack([loc, torch.log(scale)], dim=2)  # (B, V, 2)
        tokens = self.embed(torch.cat([z, stats], dim=2)) + self.var_emb  # (B, V, d)
        if self.rest_ch >= 0:
            past = x_hist[..., self.rest_ch] * (x_hist[..., -1] > 0.5)  # (B, L), padding -> 0
            rest_idx: torch.Tensor = self.rest_idx  # type: ignore[assignment]
            keep_idx: torch.Tensor = self.keep_idx  # type: ignore[assignment]
            series = torch.cat([past, x_tab[:, rest_idx]], dim=1)  # (B, L + K)
            rest_tok = (self.rest_embed(series) + self.rest_emb)[:, None]
            tokens = torch.cat([tokens, rest_tok], dim=1)
            x_tab = x_tab[:, keep_idx]
        if self.n_tab:
            tab_tokens = x_tab[..., None] * self.tab_w + self.tab_b  # (B, F, d)
            tokens = torch.cat([tokens, tab_tokens], dim=1)
        h = self.encoder(tokens)
        z0 = h[:, 0] if self.readout == "first" else h.mean(dim=1)
        out = self.head(z0).view(-1, self.n_h, self.n_q)  # SOH token is variate 0
        if self.denorm_soh:
            out = out * scale[:, :1, None]
        return out


class ITransformer(NeuralModel):
    """iTransformer; see the module docstring. ``channels="all"`` = MC, ``"soh"`` = SC."""

    name = "itransformer"

    def __init__(
        self,
        *,
        d_model: int = 64,
        n_heads: int = 4,
        n_layers: int = 2,
        dropout: float = 0.1,
        ff_mult: int = 4,
        channels: Channels = "all",
        use_tab: bool = True,
        rest_token: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            d_model=d_model,
            n_heads=n_heads,
            n_layers=n_layers,
            dropout=dropout,
            ff_mult=ff_mult,
            channels=channels,
            use_tab=use_tab,
            rest_token=rest_token,
            **kwargs,
        )
        extra = set(self.arch) - _ALLOWED_ARCH
        if extra:
            raise TypeError(f"unexpected architecture arguments {sorted(extra)}")
        if d_model % n_heads:
            raise ValueError("d_model must be divisible by n_heads")
        if channels not in ("all", "soh"):
            raise ValueError("channels must be 'all' or 'soh'")

    def build_module(
        self, n_channels: int, n_tab: int, lookback: int, n_h: int, n_q: int
    ) -> nn.Module:
        a = self.arch
        field = bool(getattr(self, "_field", False))
        if field and a["channels"] != "all":
            raise ValueError(
                "the SC variant needs an SOH channel; use channels='all' in the field setting"
            )
        n_vars = (n_channels - 1) if a["channels"] == "all" else 1  # minus the mask channel
        n_tab_used = n_tab if a["use_tab"] else 0
        rest = None
        if a.get("rest_token"):
            ch_names, f_names = getattr(self, "_names", ((), ()))
            seq = [i for i, f in enumerate(f_names) if f.startswith(REST_SEQ_PREFIX)]
            if "log_rest_s" not in ch_names or not seq or a["channels"] != "all":
                raise ValueError(
                    "rest_token needs channels='all', the log_rest_s history channel and "
                    "future_rest_seq features (forecast with future_rest_seq > 0)"
                )
            keep = [i for i in range(n_tab) if i not in seq] if a["use_tab"] else []
            rest = (ch_names.index("log_rest_s"), seq, keep)
            n_tab_used = len(keep)
        denorm = getattr(self, "_task", "forecast") != "rul" and not field
        ff = int(a["ff_mult"]) * int(a["d_model"])
        while True:
            module = _ITransformer(
                n_vars,
                n_tab_used,
                lookback,
                n_h,
                n_q,
                int(a["d_model"]),
                int(a["n_heads"]),
                int(a["n_layers"]),
                float(a["dropout"]),
                ff,
                denorm,
                "mean" if field else "first",
                rest,
            )
            if count_params(module) <= MAX_PARAMS:
                # with a rest token the module selects its own tab columns
                return _TabGate(module, use_tab=bool(a["use_tab"]) or rest is not None)
            if ff <= 4:  # was silently returned over the cap (PLAN_PHASE2 Stage 2 fix)
                raise ValueError(
                    f"iTransformer exceeds the {MAX_PARAMS} parameter cap "
                    f"({count_params(module)}) at lookback {lookback}, d_model {a['d_model']}"
                )
            ff = max(4, ff * 3 // 4)


class _TabGate(nn.Module):
    """Drops x_tab when ``use_tab`` is False so the inner module sees F = 0."""

    def __init__(self, inner: _ITransformer, use_tab: bool) -> None:
        super().__init__()
        self.inner, self.use_tab = inner, use_tab

    def forward(self, x_hist: torch.Tensor, x_tab: torch.Tensor) -> torch.Tensor:
        if not self.use_tab:
            x_tab = x_tab[:, :0]
        return self.inner(x_hist, x_tab)
