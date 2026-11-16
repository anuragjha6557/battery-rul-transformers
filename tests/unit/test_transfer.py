"""Transfer tests: synthetic data, CPU, tiny models (ADR-0012)."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
import pytest

from battery_rul.data.schema import add_soh, empty_optional_features
from battery_rul.tasks.samples import SHARED_CHANNELS, TaskSpec, build_samples, prepare_cycles
from battery_rul.train.runner import DatasetCtx
from battery_rul.train.transfer import (
    SHARED_HORIZONS,
    build_bundle,
    fewshot_samples,
    fine_tune,
    head_module,
    load_pretrained,
    pretrain,
    run_arm,
)

PARAMS: dict[str, Any] = {
    "d_model": 16,
    "n_heads": 2,
    "n_layers": 1,
    "max_epochs": 3,
    "patience": 2,
    "batch_size": 128,
    "device": "cpu",
}
LOOKBACK = 8
N_CYC = 120


def _ctx(dataset: str, n_cells: int, extra_cols: bool = True, seed: int = 0) -> DatasetCtx:
    rng = np.random.default_rng(seed)
    rows = []
    for j in range(n_cells):
        cap = 1.1 - 0.003 * np.arange(N_CYC) * (1 + 0.1 * j) + 0.002 * rng.standard_normal(N_CYC)
        for k in range(N_CYC):
            r: dict[str, Any] = {
                "dataset": dataset,
                "cell_id": f"{dataset[0]}{j}",
                "cycle_idx": k + 1,
                "capacity_ah": cap[k],
                "charge_time_s": 3000 + 5 * k + rng.normal(0, 5),
                "cc_time_s": 2000 - 3 * k + rng.normal(0, 5),
                "cv_time_s": 1000 + 8 * k,
                "charge_throughput_ah": cap[k] * 1.01,
                "ir_ohm": 0.09 + 0.0002 * k,
            }
            if extra_cols:  # raw columns only some datasets have; never shared
                r.update(rest_before_s=200.0, discharge_time_s=cap[k] * 3000)
            rows.append(r)
    cyc = add_soh(empty_optional_features(pd.DataFrame(rows)))
    cyc = cyc.sort_values(["cell_id", "cycle_idx"]).reset_index(drop=True)
    cells = pd.DataFrame({"cell_id": sorted(cyc["cell_id"].unique())})
    eol = pd.DataFrame({"cell_id": cells["cell_id"], "eol_cycle": float(N_CYC - 5)})
    smooth = pd.Series(
        cyc["soh"].to_numpy(), index=pd.MultiIndex.from_frame(cyc[["cell_id", "cycle_idx"]])
    )
    return DatasetCtx(cycles=cyc, cells=cells, eol=eol, smooth=smooth)


@pytest.fixture(scope="module")
def pre(tmp_path_factory: pytest.TempPathFactory) -> Any:
    out = tmp_path_factory.mktemp("pre")
    return pretrain(
        "itransformer",
        PARAMS,
        "forecast",
        out,
        lookback=LOOKBACK,
        ctx=_ctx("toyota", 6),
        log_mlflow=False,
    )


@pytest.fixture(scope="module")
def bundle() -> Any:
    return build_bundle(_ctx("nasa", 4, seed=3), "nasa", "n0", "forecast", LOOKBACK)


def test_pretrain_save_load_roundtrip_identical_predictions(pre: Any, bundle: Any) -> None:
    ss = bundle.tests["all"]
    ref = pre.model.predict(ss)
    for _ in range(2):  # every load is an independent, identical copy
        loaded = load_pretrained(pre.path, "cpu")
        got = loaded.predict(ss)
        np.testing.assert_allclose(got.point, ref.point, atol=1e-6)
        assert got.quantiles is not None and ref.quantiles is not None
        np.testing.assert_allclose(got.quantiles, ref.quantiles, atol=1e-6)


def test_ft_head_changes_only_head_params(pre: Any, bundle: Any) -> None:
    m = load_pretrained(pre.path, "cpu")
    before = {k: v.clone() for k, v in m.module.state_dict().items()}  # type: ignore[union-attr]
    head_names = {f"{n}" for n, _ in m.module.named_parameters() if ".head." in f".{n}."}  # type: ignore[union-attr]
    assert head_names
    ss = bundle.train
    fine_tune(m, ss, ss, head_only=True)
    after = m.module.state_dict()  # type: ignore[union-attr]
    changed = {k for k in before if not np.array_equal(before[k].numpy(), after[k].numpy())}
    assert changed and changed <= head_names
    assert head_module(m.module) is not None
    assert all(p.requires_grad for p in m.module.parameters())  # type: ignore[union-attr]


@pytest.mark.parametrize("t_p", [30, 50, 77])
def test_fewshot_targets_never_beyond_tp(bundle: Any, t_p: int) -> None:
    few = fewshot_samples(bundle.test_all, t_p)
    assert few is not None
    origin = few.meta["origin_cycle"].to_numpy()
    h = np.asarray(few.horizons)
    assert (origin <= t_p).all()
    target = origin[:, None] + h[None, :]
    assert (target[few.y_mask] <= t_p).all()  # every trained-on target is observed by T_p
    assert (few.y[~few.y_mask] == 0).all()
    assert few.y_mask.any(axis=1).all()
    assert set(few.meta["cell_id"]) == {"n0"}


def test_shared_channel_order_identical_across_datasets() -> None:
    a = _ctx("toyota", 4, extra_cols=False)  # no rest / discharge columns at all
    b = _ctx("nasa", 4, extra_cols=True)
    spec = TaskSpec(task="forecast", lookback=LOOKBACK, horizons=SHARED_HORIZONS)
    names = []
    for ctx, ds in ((a, "toyota"), (b, "nasa")):
        cells = tuple(ctx.cells["cell_id"])
        prep = prepare_cycles(ctx.cycles, cells[:3], "shared")
        ss = build_samples(prep, cells[:3], ctx.eol, spec, "all")
        names.append(ss.channel_names)
        assert ds
    assert names[0] == names[1] == ("soh", *SHARED_CHANNELS)


def test_shared_requires_all_channels() -> None:
    ctx = _ctx("nasa", 4)
    bad = ctx.cycles.assign(cv_time_s=np.nan)
    with pytest.raises(ValueError, match="shared"):
        prepare_cycles(bad, ("n0", "n1", "n2"), "shared")


def test_zero_shot_runs_without_target_training(
    pre: Any, bundle: Any, monkeypatch: pytest.MonkeyPatch
) -> None:
    import battery_rul.models.neural as neural
    import battery_rul.train.transfer as tr

    def boom(*a: Any, **k: Any) -> None:
        raise AssertionError("target-domain training attempted")

    monkeypatch.setattr(tr, "fine_tune", boom)
    monkeypatch.setattr(neural.NeuralModel, "fit", boom)
    res = run_arm(
        "zero_shot", bundle, model_name="itransformer", params=PARAMS, pretrained=pre.path, seed=0
    )
    assert res.metrics["n_sub_models"] == 1
    assert any(k.startswith("test/all/overall/rmse_h10") for k in res.metrics)
    assert np.isfinite(res.predictions["point_h10"]).all()


@pytest.mark.parametrize("arm", ["scratch", "ft_head", "ft_full", "few_shot"])
def test_other_arms_run(pre: Any, bundle: Any, arm: str) -> None:
    res = run_arm(
        arm, bundle, model_name="itransformer", params=PARAMS, pretrained=pre.path, seed=0
    )
    assert res.metrics["n_sub_models"] == 3
    assert any(k.startswith("test/start_points/") for k in res.metrics)
    if arm == "few_shot":
        assert res.metrics["n_few_shot"] > 0
        assert set(res.predictions["origin_policy"]) == {"start_points"}


def test_leakage_free_scaler_per_dataset() -> None:
    """Domain normalisation: each dataset's scaler sees only its own training cells."""
    ctx = _ctx("nasa", 4)
    prep = prepare_cycles(ctx.cycles, ("n0", "n1", "n2"), "shared")
    assert prep.scaler is not None
    assert prep.scaler.fitted_cells_ == ("n0", "n1", "n2")
