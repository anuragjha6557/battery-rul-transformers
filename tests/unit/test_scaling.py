"""Unit tests for battery_rul.splits.scaling.FoldScaler (leakage rule 1)."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from battery_rul.splits.scaling import FoldScaler


def _df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "cell_id": ["a", "a", "b", "b", "t", "t"],
            "x": [1.0, 3.0, 5.0, 7.0, 100.0, 200.0],
            "y": [0.0, np.nan, 2.0, 4.0, 9.0, 9.0],
            "other": list("uvwxyz"),
        }
    )


def test_fit_transform_hand() -> None:
    sc = FoldScaler().fit(_df(), ["a", "b"], ["x", "y"])
    # x train = 1,3,5,7: mean 4, population std sqrt(5)  ; y train (NaN ignored) = 0,2,4: mean 2,
    # std sqrt(8/3)
    assert sc.mean_ is not None and sc.scale_ is not None
    assert sc.mean_["x"] == pytest.approx(4.0)
    assert sc.scale_["x"] == pytest.approx(np.sqrt(5.0))
    assert sc.mean_["y"] == pytest.approx(2.0)
    assert sc.scale_["y"] == pytest.approx(np.sqrt(8 / 3))
    assert sc.fitted_cells_ == ("a", "b")
    out = sc.transform(_df())
    assert out["x"].iloc[0] == pytest.approx((1 - 4) / np.sqrt(5))
    assert np.isnan(out["y"].iloc[1])  # NaN preserved
    assert out["other"].tolist() == list("uvwxyz")  # untouched column
    assert _df()["x"].iloc[0] == 1.0  # input not mutated


def test_fit_ignores_non_train_rows_bit_identical() -> None:
    base = _df()
    sc1 = FoldScaler().fit(base, ["a", "b"], ["x", "y"])
    perturbed = base.copy()
    is_test = ~perturbed["cell_id"].isin(["a", "b"])
    perturbed.loc[is_test, "x"] = perturbed.loc[is_test, "x"] * 1000
    perturbed.loc[is_test, "y"] = np.nan
    perturbed.loc[is_test.idxmax(), "x"] = np.nan
    sc2 = FoldScaler().fit(perturbed, ["a", "b"], ["x", "y"])
    assert sc1.mean_ is not None and sc2.mean_ is not None
    assert sc1.scale_ is not None and sc2.scale_ is not None
    assert sc1.mean_.to_numpy().tobytes() == sc2.mean_.to_numpy().tobytes()
    assert sc1.scale_.to_numpy().tobytes() == sc2.scale_.to_numpy().tobytes()


def test_constant_column_warns_scale_one() -> None:
    df = pd.DataFrame({"cell_id": ["a", "a", "b"], "k": [2.0, 2.0, 2.0]})
    with pytest.warns(UserWarning, match="constant"):
        sc = FoldScaler().fit(df, ["a"], ["k"])
    assert sc.scale_ is not None and sc.scale_["k"] == 1.0
    assert sc.transform(df)["k"].tolist() == [0.0, 0.0, 0.0]


def test_fit_errors() -> None:
    df = _df()
    with pytest.raises(ValueError, match="absent"):
        FoldScaler().fit(df, ["a", "zzz"], ["x"])
    with pytest.raises(ValueError, match="empty"):
        FoldScaler().fit(df, [], ["x"])
    with pytest.raises(ValueError, match="empty"):
        FoldScaler().fit(df, ["a"], [])
    with pytest.raises(ValueError, match="not in df"):
        FoldScaler().fit(df, ["a"], ["nope"])
    with pytest.raises(ValueError, match="cell_id"):
        FoldScaler().fit(df.drop(columns="cell_id"), ["a"], ["x"])
    with pytest.raises(ValueError, match="NaN"):
        FoldScaler().fit(df.assign(x=np.nan), ["a"], ["x"])


def test_transform_errors() -> None:
    with pytest.raises(RuntimeError):
        FoldScaler().transform(_df())
    sc = FoldScaler().fit(_df(), ["a"], ["x"])
    with pytest.raises(ValueError):
        sc.transform(_df().drop(columns="x"))
