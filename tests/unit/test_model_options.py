"""Opt-in model options (Phase 6): defaults bit-identical, recursive rollout, Huber, revin,
deep ensemble. CPU only."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, ClassVar

import numpy as np
import pandas as pd
import pytest
import torch

from battery_rul.models.base import FitInfo, Prediction, SampleSet
from battery_rul.models.itransformer import ITransformer
from battery_rul.models.linear import NLinear
from battery_rul.models.neural import masked_huber, masked_mse
from battery_rul.models.recurrent import RecurrentModel
from battery_rul.models.registry import MODELS, omp_family
from battery_rul.models.transformer import TimeTransformer
from battery_rul.uq.ensemble import ensemble_frames, ensemble_predictions
from battery_rul.utils import seed_everything


def _samples(n: int = 48, L: int = 12, c: int = 3, pad: bool = True) -> SampleSet:
    rng = np.random.default_rng(0)
    slope = rng.uniform(0.001, 0.004, n)
    soh = rng.uniform(0.85, 1.0, n)[:, None] - slope[:, None] * np.arange(L)[None, :]
    exog = np.concatenate(
        [np.repeat(slope[:, None, None] * 300, L, axis=1), rng.normal(size=(n, L, c - 1))], axis=2
    )
    x = np.concatenate([soh[..., None], exog], axis=2).astype(np.float32)
    mask = np.ones((n, L), bool)
    if pad:
        mask[:5, :4] = False
        x[:5, :4] = np.nan
    H = (1, 5)
    y = np.stack([soh[:, -1] - slope * h for h in H], 1)
    return SampleSet(
        task="forecast",
        x_hist=x,
        hist_mask=mask,
        x_tab=rng.normal(size=(n, 2)).astype(np.float32),
        y=y.astype(np.float32),
        y_mask=np.ones_like(y, dtype=bool),
        horizons=H,
        channel_names=("soh", *[f"c{i}" for i in range(c)]),
        feature_names=("t0", "t1"),
        meta=pd.DataFrame({"dataset": "x", "cell_id": "c", "origin_cycle": np.arange(n)}),
    )


# --------------------------------------------------------------------------------------
# Defaults unchanged
# --------------------------------------------------------------------------------------
# Reference outputs (first 6 samples, 3 epochs, seed 0, CPU) recorded from the code *before* the
# options existed. Loose tolerance: platform BLAS differences, not behaviour changes.
_GOLDEN: dict[str, list[list[float]]] = {
    "transformer_pt": [[0.7450419, 0.4791808], [1.1526169, 0.9415424], [0.9052965, 0.480533], [0.9394887, 0.6894607], [0.7211028, 0.8772188], [0.6850303, 0.8681145]],  # noqa: E501
    "transformer_q": [[0.4760823, 0.7611247], [0.8992372, 1.0590454], [0.6308206, 1.0346485], [0.6660706, 0.9708608], [0.5435522, 0.9233492], [0.5429112, 0.9561041]],  # noqa: E501
    "lstm_pt": [[1.2611306, 1.041889], [1.0209538, 0.8879719], [1.0974733, 1.0892412], [0.8959564, 0.8259207], [0.8986353, 0.7620909], [0.5768248, 0.5929101]],  # noqa: E501
    "lstm_q": [[1.0486413, 0.8696085], [1.1760504, 1.0555455], [1.0923011, 1.0635385], [1.0490211, 0.9659277], [0.9847268, 1.0416558], [0.711268, 0.8191024]],  # noqa: E501
    "nlinear_pt": [[0.7831155, 0.8490994], [0.9090156, 0.9769289], [0.9106624, 0.9797781], [0.829409, 0.8986531], [0.8954526, 0.9605101], [0.7683247, 0.8263839]],  # noqa: E501
    "nlinear_q": [[1.05773, 0.8937707], [1.1855598, 1.0148753], [1.1884092, 1.0135338], [1.1072842, 0.9319611], [1.1691406, 1.0084105], [1.0350141, 0.8836457]],  # noqa: E501
    "itransformer_pt": [[0.8315927, 0.8257031], [0.9552965, 0.9515585], [0.9560717, 0.9534227], [0.8746387, 0.8723338], [0.9438238, 0.9370985], [0.8132975, 0.8060907]],  # noqa: E501
    "itransformer_q": [[0.8301263, 0.8312285], [0.9542002, 0.9556055], [0.9554765, 0.9558948], [0.8740375, 0.8747055], [0.9421732, 0.9444675], [0.809908, 0.8175694]],  # noqa: E501
}  # fmt: skip

_MAKERS: dict[str, Callable[[Any], Any]] = {
    "transformer": lambda q: TimeTransformer(
        d_model=16, n_heads=2, n_layers=1, quantiles=q, max_epochs=3, device="cpu"
    ),
    "lstm": lambda q: RecurrentModel(
        cell="lstm", hidden=16, layers=1, quantiles=q, max_epochs=3, device="cpu"
    ),
    "nlinear": lambda q: NLinear(quantiles=q, max_epochs=3, device="cpu"),
    "itransformer": lambda q: ITransformer(
        d_model=16, n_heads=2, n_layers=1, quantiles=q, max_epochs=3, device="cpu"
    ),
}


@pytest.mark.parametrize("name", sorted(_MAKERS))
@pytest.mark.parametrize("mode", ["pt", "q"])
def test_defaults_reproduce_pre_option_outputs(name: str, mode: str) -> None:
    s = _samples()
    seed_everything(0)
    m = _MAKERS[name](None if mode == "pt" else (0.1, 0.5, 0.9))
    m.fit(s, s)
    got = m.predict(s).point[:6]
    np.testing.assert_allclose(got, np.array(_GOLDEN[f"{name}_{mode}"]), atol=2e-4)


@pytest.mark.parametrize("name", ["transformer", "lstm"])
def test_explicit_defaults_identical_to_implicit(name: str) -> None:
    s = _samples()
    extra = {"revin": False, "loss": "mse", "huber_delta": 0.01}
    outs = []
    for kw in ({}, extra):
        seed_everything(3)
        if name == "transformer":
            m: Any = TimeTransformer(d_model=16, n_heads=2, n_layers=1, quantiles=None, **kw)
        else:
            m = RecurrentModel(hidden=16, layers=1, quantiles=None, **kw)
        m.device, m.max_epochs = torch.device("cpu"), 3
        m.fit(s, s)
        outs.append(m.predict(s).point)
    assert np.array_equal(outs[0], outs[1])


# --------------------------------------------------------------------------------------
# Huber
# --------------------------------------------------------------------------------------
def test_huber_matches_half_mse_on_small_errors_and_is_linear_beyond() -> None:
    torch.manual_seed(0)
    pred = torch.randn(32, 2, 1) * 0.001
    y = torch.randn(32, 2) * 0.001
    m = torch.ones(32, 2, dtype=torch.bool)
    h = masked_huber(pred, y, m, delta=1.0)
    assert float(h) == pytest.approx(0.5 * float(masked_mse(pred, y, m)), rel=1e-5)
    big = masked_huber(torch.tensor([[[10.0]]]), torch.zeros(1, 1), torch.ones(1, 1).bool(), 0.5)
    assert float(big) == pytest.approx(0.5 * (10 - 0.25))
    masked = masked_huber(pred, y, torch.zeros(32, 2, dtype=torch.bool), 1.0)
    assert float(masked) == 0.0


def test_huber_option_trains_point_and_is_ignored_for_quantiles() -> None:
    s = _samples()
    seed_everything(0)
    m = NLinear(quantiles=None, loss="huber", huber_delta=0.01, max_epochs=3, device="cpu")
    m.fit(s, s)
    assert np.isfinite(m.predict(s).point).all()
    with pytest.raises(ValueError):
        NLinear(loss="l1")
    outs = []
    for loss in ("mse", "huber"):
        seed_everything(0)
        q = NLinear(quantiles=(0.1, 0.5, 0.9), loss=loss, max_epochs=3, device="cpu")
        q.fit(s, s)
        outs.append(q.predict(s).point)
    assert np.array_equal(outs[0], outs[1])  # pinball either way


# --------------------------------------------------------------------------------------
# RevIN
# --------------------------------------------------------------------------------------
@pytest.mark.parametrize("name", ["transformer", "lstm"])
@pytest.mark.parametrize("revin", [False, True])
def test_revin_on_off_both_train(name: str, revin: bool) -> None:
    s = _samples()
    seed_everything(0)
    if name == "transformer":
        m: Any = TimeTransformer(d_model=16, n_heads=2, n_layers=1, revin=revin, max_epochs=3)
    else:
        m = RecurrentModel(hidden=16, layers=1, revin=revin, max_epochs=3)
    m.device = torch.device("cpu")
    info = m.fit(s, s)
    p = m.predict(s)
    assert p.point.shape == (len(s), 2) and p.quantiles is not None
    assert np.isfinite(p.quantiles).all() and info.epochs is not None


@pytest.mark.parametrize("name", ["transformer", "lstm"])
def test_revin_is_level_invariant_and_zero_module_is_persistence(name: str) -> None:
    s = _samples(pad=False)
    seed_everything(0)
    if name == "transformer":
        m: Any = TimeTransformer(d_model=16, n_heads=2, n_layers=1, revin=True, max_epochs=1)
    else:
        m = RecurrentModel(hidden=16, layers=1, revin=True, max_epochs=1)
    m.device, m.quantiles = torch.device("cpu"), None
    m.fit(s)
    shifted = SampleSet(**{**s.__dict__, "x_hist": s.x_hist + np.array([0.1, 0, 0, 0], "f4")})
    a, b = m.predict(s).point, m.predict(shifted).point
    np.testing.assert_allclose(b - a, 0.1, atol=1e-5)  # residual output unchanged by level
    assert m.module is not None
    for p in m.module.parameters():
        torch.nn.init.zeros_(p)
    last = s.x_hist[:, -1, 0][:, None]
    np.testing.assert_allclose(m.predict(s).point, np.repeat(last, 2, 1), atol=1e-6)


# --------------------------------------------------------------------------------------
# Recursive wrapper
# --------------------------------------------------------------------------------------
class _PerfectOneStep:
    """Mock one-step model: extrapolates the last step of the SOH channel exactly."""

    name = "mock_onestep"
    seen: ClassVar[list[np.ndarray]] = []
    fit_horizons: tuple[int, ...] = ()

    def __init__(self, **_: Any) -> None:
        pass

    def fit(self, train: SampleSet, val: SampleSet | None = None) -> FitInfo:
        type(self).fit_horizons = train.horizons
        assert train.y.shape[1] == 1
        return FitInfo(n_train=len(train))

    def predict(self, samples: SampleSet) -> Prediction:
        x = samples.x_hist
        type(self).seen.append(x.copy())
        nxt = 2 * x[:, -1, 0] - x[:, -2, 0]
        return Prediction(point=np.repeat(nxt[:, None], len(samples.horizons), 1))


@pytest.fixture
def mock_registered() -> Any:
    MODELS["mock_onestep"] = _PerfectOneStep
    _PerfectOneStep.seen = []
    yield
    MODELS.pop("mock_onestep")


def test_recursive_reproduces_linear_trend_and_holds_exog(mock_registered: Any) -> None:
    from battery_rul.models.recursive import RecursiveWrapper

    s = _samples(pad=False)
    # exact linear SOH: s.x_hist[..., 0] is linear in t by construction
    horizons = (1, 5)
    w = RecursiveWrapper(base_name="mock_onestep")
    w.fit(s, s)
    assert _PerfectOneStep.fit_horizons == (1,)
    p = w.predict(s)
    np.testing.assert_allclose(p.point, s.y, atol=2e-6)
    assert p.quantiles is None and len(horizons) == p.point.shape[1]
    # inspection: at the last rollout step the appended rows hold exog constant, mask True
    last_seen = _PerfectOneStep.seen[-1]  # input to step 5: 4 appended rows
    orig = s.x_hist
    for k in range(1, 5):
        np.testing.assert_array_equal(last_seen[:, -5 + k, 1:], orig[:, -1, 1:])
    assert last_seen.shape == orig.shape
    np.testing.assert_array_equal(last_seen[:, :-4], orig[:, 4:])  # window slid, history intact


def test_recursive_holds_last_valid_value_with_padding(mock_registered: Any) -> None:
    from battery_rul.models.recursive import RecursiveWrapper

    s = _samples(pad=True)
    w = RecursiveWrapper(base_name="mock_onestep")
    w.fit(s)
    w.predict(s)  # NaN pads at the left must not leak into the held values
    assert not np.isnan(_PerfectOneStep.seen[-1][:, -4:, 1:]).any()


def test_recursive_needs_horizon_one_and_registry_family() -> None:
    from battery_rul.models.recursive import RecursiveWrapper

    s = _samples(pad=False)
    no_h1 = SampleSet(
        **{**s.__dict__, "y": s.y[:, 1:], "y_mask": s.y_mask[:, 1:], "horizons": (5,)}
    )
    MODELS["mock_onestep"] = _PerfectOneStep
    try:
        with pytest.raises(ValueError, match="horizon 1"):
            RecursiveWrapper(base_name="mock_onestep").fit(no_h1)
    finally:
        MODELS.pop("mock_onestep")
    assert omp_family("recursive", {"base_name": "itransformer"}) == "torch"
    assert omp_family("recursive", {"base_name": "lgbm"}) == "lightgbm"
    assert "recursive" in MODELS and MODELS["recursive"].tunable is False


def test_recursive_with_real_neural_base_runs() -> None:
    from battery_rul.models.recursive import RecursiveWrapper

    s = _samples()
    w = RecursiveWrapper(
        base_name="nlinear", base_params={"quantiles": None, "max_epochs": 2}, device="cpu"
    )
    w.fit(s, s)
    p = w.predict(s)
    assert p.point.shape == (len(s), 2) and np.isfinite(p.point).all()


# --------------------------------------------------------------------------------------
# Deep ensemble
# --------------------------------------------------------------------------------------
def _pred(offset: float) -> Prediction:
    base = np.arange(6, dtype=float).reshape(3, 2)
    q = np.stack([base - 1 + offset, base + offset, base + 1 + offset], axis=2)
    return Prediction(point=base + offset, quantiles=q, quantile_levels=(0.1, 0.5, 0.9))


def test_ensemble_predictions_mean_per_level() -> None:
    e = ensemble_predictions([_pred(0.0), _pred(2.0), _pred(4.0)])
    np.testing.assert_allclose(e.point, _pred(2.0).point)
    assert e.quantiles is not None
    np.testing.assert_allclose(e.quantiles, _pred(2.0).quantiles)
    assert e.quantile_levels == (0.1, 0.5, 0.9)
    assert (np.diff(e.quantiles, axis=2) >= 0).all()
    only_point = ensemble_predictions([_pred(0.0), Prediction(point=_pred(1.0).point)])
    assert only_point.quantiles is None
    with pytest.raises(ValueError):
        ensemble_predictions([])
    bad = Prediction(
        point=_pred(0).point, quantiles=_pred(0).quantiles, quantile_levels=(0.1, 0.5, 0.95)
    )
    with pytest.raises(ValueError):
        ensemble_predictions([_pred(0.0), bad])


def _frame(offset: float) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "cell_id": ["a", "a", "b"],
            "origin_cycle": [1, 2, 3],
            "y_h1": [1.0, 2.0, 3.0],
            "point_h1": np.array([1.0, 2.0, 3.0]) + offset,
            "q0.05_h1": np.array([0.5, 1.5, 2.5]) + offset,
            "q0.95_h1": np.array([1.5, 2.5, 3.5]) + offset,
        }
    )


def test_ensemble_frames() -> None:
    e = ensemble_frames([_frame(0.0), _frame(1.0), _frame(5.0)])
    np.testing.assert_allclose(e["point_h1"], np.array([1.0, 2.0, 3.0]) + 2.0)
    np.testing.assert_allclose(e["q0.05_h1"], np.array([0.5, 1.5, 2.5]) + 2.0)
    np.testing.assert_array_equal(e["y_h1"], [1.0, 2.0, 3.0])
    assert (e["q0.05_h1"] <= e["q0.95_h1"]).all()
    shifted = _frame(0.0).assign(y_h1=[9.0, 2.0, 3.0])
    with pytest.raises(ValueError, match="y_h1"):
        ensemble_frames([_frame(0.0), shifted])
