"""Per-cell report aggregation on synthetic prediction frames (no MLflow)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from battery_rul.eval.report import cell_metrics, rank_table, tables_from_long

HZ = (1, 10)


def _frame(cells: list[str], err: float, split: str, rng: np.random.Generator) -> pd.DataFrame:
    rows = []
    for c in cells:
        n = 30
        y = 0.9 - 0.001 * np.arange(n)[:, None] * np.array([[1, 10]])
        noise = rng.normal(0, 1, (n, 2))
        d: dict[str, object] = {
            "dataset": "x",
            "cell_id": c,
            "origin_cycle": np.arange(n),
            "start_kind": ["fixed:5"] * 5 + ["all"] * 25,
            "split": split,
            "origin_policy": "all",
        }
        for j, h in enumerate(HZ):
            d[f"y_h{h}"] = y[:, j]
            d[f"y_mask_h{h}"] = True
            d[f"point_h{h}"] = y[:, j] + err * noise[:, j]
        rows.append(pd.DataFrame(d))
    return pd.concat(rows, ignore_index=True)


def _long(
    ds: str, split_tag: str, cells: list[str], seeds: list[int], errs: dict[str, float]
) -> pd.DataFrame:
    parts = []
    for model, err in errs.items():
        for s in seeds:
            f = _frame(cells, err, split_tag, np.random.default_rng(100 * s + len(model)))
            parts.append(
                cell_metrics(f, "forecast").assign(
                    dataset=ds, task="forecast", model=model, seed=s, run_id=f"{model}{s}"
                )
            )
    return pd.concat(parts, ignore_index=True)


def test_cell_metrics_matches_manual_rmse() -> None:
    f = _frame(["a", "b"], 0.01, "test", np.random.default_rng(0))
    cm = cell_metrics(f, "forecast")
    assert set(cm["split"]) == {"loco"} and set(cm["cell"]) == {"a", "b"}
    assert set(cm["kind"]) == {"overall", "fixed:5"}
    g = f[f["cell_id"] == "a"]
    want = float(np.sqrt(np.mean((g["point_h10"] - g["y_h10"]) ** 2)) * 100)
    got = cm[(cm.cell == "a") & (cm.kind == "overall") & (cm.metric == "rmse_h10")]["value"].iloc[0]
    assert np.isclose(got, want)


def test_rul_metrics_per_cell() -> None:
    n = 10
    f = pd.DataFrame(
        {
            "cell_id": "a",
            "start_kind": ["frac:0.5"] * n,
            "split": "test",
            "origin_policy": "start_points",
            "y_h0": np.full(n, 100.0),
            "y_mask_h0": True,
            "point_h0": np.r_[np.full(5, 110.0), np.full(5, 150.0)],
        }
    )
    cm = cell_metrics(f, "rul")
    ov = cm[cm.kind == "overall"].set_index("metric")["value"]
    assert np.isclose(ov["rul_mae"], 30.0) and np.isclose(ov["rul_bias"], 30.0)
    assert "alpha_lambda_acc" not in ov
    fr = cm[cm.kind == "frac:0.5"].set_index("metric")["value"]
    assert np.isclose(fr["alpha_lambda_acc"], 0.5)


def test_loco_consistency_and_ci() -> None:
    cells = ["c1", "c2", "c3", "c4"]
    long = _long("nasa", "test", cells, [0, 1, 2], {"persistence": 0.03, "good": 0.01})
    t = tables_from_long(long)["nasa_forecast"]
    r = t[(t.model == "good") & (t.metric == "rmse_h10") & (t.kind == "overall")].iloc[0]
    assert r.baseline == "persistence" and r.consistency == "4/4 cells, 12/12 cell-seeds"
    assert r.n_cells == 4 and r.ci_lo <= r["mean"] <= r.ci_hi
    b = t[(t.model == "persistence") & (t.metric == "rmse_h10") & (t.kind == "overall")].iloc[0]
    assert b.consistency == "" and b.baseline == "" and "p_holm" in t.columns


def test_toyota_wilcoxon_over_cells_and_rank() -> None:
    cells = [f"t{i}" for i in range(12)]
    errs = {"persistence": 0.03, "last_slope": 0.05, "good": 0.01}
    long = pd.concat(
        [
            _long("toyota", "test1", cells, [0, 1], errs),
            _long("toyota", "test2", cells[:8], [0, 1], errs),
        ],
        ignore_index=True,
    )
    tabs = tables_from_long(long)
    t = tabs["toyota_forecast"]
    assert set(t.split) == {"test1", "test2"}
    sel = (t.metric == "rmse_h10") & (t.kind == "overall")
    r = t[sel & (t.split == "test1") & (t.model == "good")].iloc[0]
    assert r.n_cells == 12 and r.baseline == "persistence"
    assert r.consistency == "" and r.p_holm < 0.01  # all 12 cells improve
    worse = t[sel & (t.split == "test1") & (t.model == "last_slope")].iloc[0]
    assert worse.p_holm < 0.01 and worse["mean"] > r["mean"]
    assert t[sel & (t.split == "test2") & (t.model == "good")].iloc[0].n_cells == 8

    ranks = rank_table(tabs).set_index("model")["mean_rank"]
    assert ranks["good"] == 1.0 and ranks["persistence"] == 2.0 and ranks["last_slope"] == 3.0


def test_arm_labels_split_ablation_arms_only() -> None:
    from battery_rul.eval.report import with_arm_labels

    runs = pd.DataFrame(
        {
            "params.task": ["forecast"] * 4 + ["soh"],
            "params.model": ["lstm", "lstm", "lstm", "gru", "lstm"],
            "params.model.loss": ["huber", "mse", None, "mse", "mse"],
            "params.model.revin": [None, None, "True", None, None],
            "params.model.hidden": ["64"] * 5,
        }
    )
    arms = with_arm_labels(runs)["arm"].tolist()
    assert arms == ["lstm[loss=huber]", "lstm[loss=mse]", "lstm[revin=True]", "gru", "lstm"]
