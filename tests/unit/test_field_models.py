"""Every field-setting model fits and predicts on synthetic field samples (no SOH channel)."""

from __future__ import annotations

import numpy as np
import pytest
from test_leakage import EOL, TEST, TRAIN, _field_cycles

from battery_rul.models.registry import make_model
from battery_rul.tasks.samples import TaskSpec, build_samples, prepare_cycles

TINY = {"max_epochs": 2, "patience": 1, "device": "cpu", "batch_size": 64}


def _sets(task: str):
    cyc = _field_cycles()
    prep = prepare_cycles(cyc, TRAIN, "field_curve")
    spec = TaskSpec(task=task, lookback=8, horizons=(1, 5), feature_set="field_curve")  # type: ignore[arg-type]
    return build_samples(prep, TRAIN, EOL, spec), build_samples(prep, TEST, EOL, spec)


@pytest.mark.parametrize("task", ["soh", "forecast", "rul"])
@pytest.mark.parametrize(
    ("name", "params"),
    [
        ("itransformer", {"d_model": 16, "n_heads": 2, "n_layers": 1, "channels": "all", **TINY}),
        ("patchtst", {"d_model": 16, "n_heads": 2, "n_layers": 1, "patch_len": 4, **TINY}),
        ("lstm", {"hidden": 8, "layers": 1, "cell": "lstm", **TINY}),
        ("transformer", {"d_model": 16, "n_heads": 2, "n_layers": 1, **TINY}),
        ("age_only", {}),
        ("elasticnet", {}),
    ],
)
def test_field_model_fit_predict(name: str, params: dict, task: str) -> None:
    tr, te = _sets(task)
    m = make_model(name, **params)
    m.fit(tr, te)
    p = m.predict(te)
    assert p.point.shape == te.y.shape and np.isfinite(p.point).all()
    if task != "rul":  # absolute SOH, not a residual around a (non-existent) SOH channel
        assert 0.0 < float(np.median(p.point)) < 1.5


def test_sc_variant_rejected_in_field_setting() -> None:
    tr, te = _sets("forecast")
    m = make_model("itransformer", d_model=16, n_heads=2, n_layers=1, channels="soh", **TINY)
    with pytest.raises(ValueError, match="SOH channel"):
        m.fit(tr, te)


def _seq_sets(k: int = 6):
    prep = prepare_cycles(_field_cycles(), TRAIN, "field_curve")
    spec = TaskSpec(
        task="forecast", lookback=8, horizons=(1, 5), feature_set="field_curve", future_rest_seq=k
    )
    return build_samples(prep, TRAIN, EOL, spec), build_samples(prep, TEST, EOL, spec)


def test_itransformer_rest_token_uses_the_future_schedule() -> None:
    """The rest token is built, consumes the rest_seq columns, and its output depends on them."""
    import torch

    tr, te = _seq_sets()
    m = make_model(
        "itransformer", d_model=16, n_heads=2, n_layers=1, channels="all", rest_token=True, **TINY
    )
    m.fit(tr, te)
    inner = m.module.inner
    assert inner.rest_ch == tr.channel_names.index("log_rest_s")
    assert len(inner.rest_idx) == 6 and len(inner.keep_idx) == len(tr.feature_names) - 6
    p = m.predict(te)
    assert p.point.shape == te.y.shape and np.isfinite(p.point).all()
    with torch.no_grad():
        nn_ = inner.rest_embed
        nn_.weight[:, -6:] += 1.0  # make the future part matter, then perturb it
    te2 = te.__class__(**{**te.__dict__, "x_tab": te.x_tab.copy()})
    te2.x_tab[:, [te.feature_names.index(f"rest_seq_{j:03d}") for j in range(1, 7)]] += 5.0
    assert not np.allclose(m.predict(te).point, m.predict(te2).point)


def test_rest_token_requires_the_sequence() -> None:
    tr, te = _sets("forecast")
    m = make_model(
        "itransformer", d_model=16, n_heads=2, n_layers=1, channels="all", rest_token=True, **TINY
    )
    with pytest.raises(ValueError, match="rest_token needs"):
        m.fit(tr, te)
