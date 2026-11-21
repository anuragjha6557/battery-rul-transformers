"""Shared base for every neural benchmark entry (ADR-0006: identical training procedure).

A subclass only defines ``build_module``: an ``nn.Module`` mapping
``(x_hist[B, L, C+1], x_tab[B, F]) -> out[B, H, Q]`` (Q = 1 for point models). Everything else
is shared, so model comparisons differ only in architecture:

- **Inputs:** NaN -> 0 in history, plus the validity mask appended as an extra channel. Tabular
  features are standardised with *training-sample* statistics (fit inside ``fit``).
- **Targets:**
  - soh/forecast are learned as residuals ``y - last observed SOH``, so the model learns
    change rather than level and persistence is the zero function.
  - rul is learned as ``y / s``, with ``s`` the median training RUL.
- **Loss:** masked MSE (point) or masked pinball (quantiles; the median must be one of them).
- **Optimiser:** Adam + early stopping on the inner-validation cell(s) (patience 20, ≤ 300 epochs,
  PROTOCOL §6), keeping the best epoch's weights. Gradient clipping at 1.0.
- **Quantile outputs:** rearranged to be non-decreasing (Chernozhukov et al. 2010).
"""

from __future__ import annotations

import copy
from collections.abc import Callable
from typing import Any, ClassVar

import numpy as np
import torch
from torch import nn

from battery_rul.models.base import (
    DEFAULT_QUANTILES,
    FitInfo,
    Prediction,
    SampleSet,
    TaskName,
)
from battery_rul.utils import resolve_device

SOH_CHANNEL = 0


def has_soh(samples: SampleSet) -> bool:
    """False in the field setting (PLAN_PHASE2): no SOH channel, targets are absolute."""
    return bool(samples.channel_names) and samples.channel_names[0] == "soh"


def last_valid_soh(samples: SampleSet) -> np.ndarray:
    """Last observed SOH per sample (cycle T_p for B/C, k-1 for Task A)."""
    mask = samples.hist_mask
    if not mask.any(axis=1).all():
        raise ValueError("every sample needs at least one valid history point")
    last = mask.shape[1] - 1 - np.argmax(mask[:, ::-1], axis=1)
    return samples.x_hist[np.arange(len(samples)), last, SOH_CHANNEL].astype(np.float64)


def masked_mse(pred: torch.Tensor, y: torch.Tensor, m: torch.Tensor) -> torch.Tensor:
    """pred (B,H,1), y (B,H), m (B,H) bool."""
    err = (pred[..., 0] - y) ** 2
    return (err * m).sum() / m.sum().clamp_min(1)


def masked_huber(
    pred: torch.Tensor, y: torch.Tensor, m: torch.Tensor, delta: float
) -> torch.Tensor:
    """Masked Huber loss, pred (B,H,1), y (B,H), m (B,H) bool.

    ``0.5 e^2`` for ``|e| <= delta`` (i.e. MSE/2 on small errors), ``delta (|e| - delta/2)``
    beyond. Targets are residuals in SOH fraction units, so ``delta`` is in SOH fraction.
    """
    e = (pred[..., 0] - y).abs()
    err = torch.where(e <= delta, 0.5 * e**2, delta * (e - 0.5 * delta))
    return (err * m).sum() / m.sum().clamp_min(1)


def masked_pinball(
    pred: torch.Tensor, y: torch.Tensor, m: torch.Tensor, q: torch.Tensor
) -> torch.Tensor:
    """pred (B,H,Q), y (B,H), m (B,H), q (Q,)."""
    diff = y[..., None] - pred
    loss = torch.maximum(q * diff, (q - 1) * diff)
    return (loss * m[..., None]).sum() / (m.sum().clamp_min(1) * q.numel())


def revin_inputs(x_hist: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
    """Instance normalisation of every history channel (ADR-0013 E), opt-in via ``revin=True``.

    Reuses iTransformer's ``fill_and_normalise``: each channel is centred on its last valid
    value and divided by its masked std (padding filled with the first valid value first).

    Args:
        x_hist: (B, L, C+1) with the validity mask as the last channel.
    Returns:
        x_norm (B, L, C+1), same layout (mask channel unchanged), and the SOH scale (B, 1, 1)
        by which a residual-space SOH output must be multiplied (same convention as
        iTransformer's ``denorm_soh``). The absolute level is discarded, as in RevIN.
    """
    from battery_rul.models.itransformer import fill_and_normalise  # lazy: circular import

    z, _, scale = fill_and_normalise(x_hist)  # (B, V, L), _, (B, V)
    x_norm = torch.cat([z.transpose(1, 2), x_hist[..., -1:]], dim=2)
    return x_norm, scale[:, :1, None]


class NeuralModel:
    """Base class; subclasses set ``name``/``supported_tasks`` and implement ``build_module``."""

    name: ClassVar[str] = "neural"
    supported_tasks: ClassVar[frozenset[TaskName]] = frozenset({"soh", "forecast", "rul"})
    probabilistic: ClassVar[bool] = True  # instances may be point-only (quantiles=None)
    cross_fit: ClassVar[bool] = True
    tunable: ClassVar[bool] = True

    def __init__(
        self,
        *,
        lr: float = 1e-3,
        weight_decay: float = 1e-4,
        batch_size: int = 256,
        max_epochs: int = 300,
        patience: int = 20,
        quantiles: tuple[float, ...] | None = DEFAULT_QUANTILES,
        grad_clip: float = 1.0,
        loss: str = "mse",
        huber_delta: float = 0.01,
        device: str = "auto",
        epoch_callback: Callable[[int, float], None] | None = None,
        **arch: Any,
    ) -> None:
        if quantiles is not None and 0.5 not in quantiles:
            raise ValueError("quantiles must include the median 0.5")
        self.lr, self.weight_decay, self.batch_size = lr, weight_decay, batch_size
        self.max_epochs, self.patience, self.grad_clip = max_epochs, patience, grad_clip
        self.quantiles = tuple(sorted(quantiles)) if quantiles is not None else None
        if loss not in ("mse", "huber"):
            raise ValueError("loss must be 'mse' or 'huber'")
        #: Point-mode loss (ADR-0013 F); quantile mode always uses pinball.
        self.loss_name, self.huber_delta = loss, float(huber_delta)
        self.device = resolve_device(device)  # type: ignore[arg-type]
        #: Called as ``epoch_callback(epoch, val_loss)`` after each epoch's validation loss
        #: (1-based epoch). Used by tuning for pruning; an exception raised here (e.g.
        #: ``optuna.TrialPruned``) propagates out of ``fit``.
        self.epoch_callback = epoch_callback
        self.arch = arch
        self.module: nn.Module | None = None

    # -- to implement -------------------------------------------------------------------------
    def build_module(
        self, n_channels: int, n_tab: int, lookback: int, n_h: int, n_q: int
    ) -> nn.Module:
        raise NotImplementedError

    # -- data plumbing ------------------------------------------------------------------------
    def _x(self, s: SampleSet) -> tuple[torch.Tensor, torch.Tensor]:
        hist = np.nan_to_num(s.x_hist.astype(np.float32))
        hist = np.concatenate([hist, s.hist_mask[..., None].astype(np.float32)], axis=2)
        tab = np.nan_to_num((s.x_tab.astype(np.float64) - self._tab_mu) / self._tab_sd)
        return (
            torch.from_numpy(hist).to(self.device),
            torch.from_numpy(tab.astype(np.float32)).to(self.device),
        )

    def _y_to_target(self, s: SampleSet) -> np.ndarray:
        if s.task == "rul":
            return s.y.astype(np.float64) / self._rul_scale
        if not has_soh(s):  # field setting: SOH relative to the training cells' mean (labels only)
            return s.y.astype(np.float64) - self._y_offset[None, :]
        return s.y.astype(np.float64) - last_valid_soh(s)[:, None]

    def _target_to_y(self, s: SampleSet, t: np.ndarray) -> np.ndarray:
        """t: (n, H, Q) in target space -> SOH or cycles."""
        if s.task == "rul":
            return np.maximum(t * self._rul_scale, 0.0)
        if not has_soh(s):
            return t + self._y_offset[None, :, None]
        return t + last_valid_soh(s)[:, None, None]

    def _loss(self, pred: torch.Tensor, y: torch.Tensor, m: torch.Tensor) -> torch.Tensor:
        if self.quantiles is None:
            if self.loss_name == "huber":
                return masked_huber(pred, y, m, self.huber_delta)
            return masked_mse(pred, y, m)
        q = torch.tensor(self.quantiles, dtype=pred.dtype, device=pred.device)
        return masked_pinball(pred, y, m, q)

    # -- Model protocol -----------------------------------------------------------------------
    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        self._task = train.task
        self._tab_mu = np.nanmean(train.x_tab, axis=0) if train.x_tab.shape[1] else 0.0
        sd = np.nanstd(train.x_tab, axis=0) if train.x_tab.shape[1] else 1.0
        self._tab_sd = np.where(np.asarray(sd) > 0, sd, 1.0)
        self._rul_scale = (
            float(np.median(train.y[train.y_mask])) if train.task == "rul" else 1.0
        ) or 1.0
        n_q = len(self.quantiles) if self.quantiles is not None else 1
        self._field = not has_soh(train)
        # field setting: per-horizon mean training target (a label statistic, never an input)
        ym = np.where(train.y_mask, train.y, np.nan).astype(np.float64)
        self._y_offset = (
            np.nan_to_num(np.nanmean(ym, axis=0)) if self._field else np.zeros(ym.shape[1])
        )
        self.module = self.build_module(
            train.x_hist.shape[2] + 1,
            train.x_tab.shape[1],
            train.x_hist.shape[1],
            len(train.horizons),
            n_q,
        ).to(self.device)
        opt = torch.optim.Adam(self.module.parameters(), lr=self.lr, weight_decay=self.weight_decay)

        xh, xt = self._x(train)
        y = torch.from_numpy(self._y_to_target(train).astype(np.float32)).to(self.device)
        m = torch.from_numpy(train.y_mask).to(self.device)
        if val is not None:
            vxh, vxt = self._x(val)
            vy = torch.from_numpy(self._y_to_target(val).astype(np.float32)).to(self.device)
            vm = torch.from_numpy(val.y_mask).to(self.device)

        n = len(train)
        gen = torch.Generator().manual_seed(torch.initial_seed() % (2**31))
        best, best_state, bad, epochs_run = float("inf"), None, 0, 0
        for epoch in range(1, self.max_epochs + 1):
            epochs_run = epoch
            self.module.train()
            perm = torch.randperm(n, generator=gen).to(self.device)
            for i in range(0, n, self.batch_size):
                idx = perm[i : i + self.batch_size]
                opt.zero_grad(set_to_none=True)
                loss = self._loss(self.module(xh[idx], xt[idx]), y[idx], m[idx])
                loss.backward()
                nn.utils.clip_grad_norm_(self.module.parameters(), self.grad_clip)
                opt.step()
            if val is None:
                continue
            self.module.eval()
            with torch.no_grad():
                # chunked forward: one pass over a large validation set can exhaust memory
                # (PatchTST folds channels into the batch); the loss is computed once on the
                # concatenated outputs, so the value is identical to the unchunked pass
                vout = torch.cat(
                    [
                        self.module(vxh[i : i + 256], vxt[i : i + 256])
                        for i in range(0, len(vxh), 256)
                    ]
                )
                v = float(self._loss(vout, vy, vm))
            if self.epoch_callback is not None:
                self.epoch_callback(epoch, v)
            if v < best - 1e-7:
                best, best_state, bad = v, copy.deepcopy(self.module.state_dict()), 0
            else:
                bad += 1
                if bad >= self.patience:
                    break
        if best_state is not None:
            self.module.load_state_dict(best_state)
        n_params = sum(p.numel() for p in self.module.parameters())
        return FitInfo(
            n_train=n,
            n_val=len(val) if val is not None else 0,
            epochs=epochs_run,
            best_val_loss=best if val is not None else None,
            extra={"n_params": n_params},
        )

    def predict(self, samples: SampleSet) -> Prediction:
        if self.module is None:
            raise RuntimeError("fit() first")
        self.module.eval()
        xh, xt = self._x(samples)
        outs = []
        with torch.no_grad():
            for i in range(0, len(samples), 256):
                outs.append(self.module(xh[i : i + 256], xt[i : i + 256]).float().cpu().numpy())
        t = np.concatenate(outs).astype(np.float64)  # (n, H, Q)
        y = self._target_to_y(samples, t)
        if self.quantiles is None:
            return Prediction(point=y[..., 0])
        y = np.sort(y, axis=2)  # rearrangement: monotone quantiles
        median = y[..., self.quantiles.index(0.5)]
        return Prediction(point=median, quantiles=y, quantile_levels=self.quantiles)
