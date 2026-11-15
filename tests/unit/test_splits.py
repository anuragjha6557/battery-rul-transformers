"""Unit tests for battery_rul.splits.loco and battery_rul.splits.toyota."""

from __future__ import annotations

import pandas as pd
import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from battery_rul.splits.loco import independent_fold_cells, loco_folds
from battery_rul.splits.toyota import grouped_kfold, official_split

_ids = st.lists(
    st.text("abcdefgh0123", min_size=1, max_size=4), min_size=3, max_size=9, unique=True
)


@settings(max_examples=60)
@given(_ids)
def test_loco_properties(ids: list[str]) -> None:
    folds = loco_folds(ids)
    assert [f.test for f in folds] == sorted(ids)
    assert len(folds) == len(ids)
    for f in folds:
        assert f.test not in f.train
        assert sorted((*f.train, f.test)) == sorted(ids)
        # inner folds cover each training cell exactly once as val, val in train, test absent
        assert sorted(i.val for i in f.inner) == sorted(f.train)
        for i in f.inner:
            assert i.val in f.train and i.val not in i.train
            assert set(i.train) | {i.val} == set(f.train)
            assert f.test not in i.train


def test_loco_hand_and_validation() -> None:
    folds = loco_folds(["c", "a", "b"])
    assert folds[0].test == "a" and folds[0].train == ("b", "c")
    assert [(i.train, i.val) for i in folds[0].inner] == [(("c",), "b"), (("b",), "c")]
    with pytest.raises(ValueError):
        loco_folds(["a", "b"])
    with pytest.raises(ValueError):
        loco_folds(["a", "a", "b"])


def test_independent_fold_cells() -> None:
    assert independent_fold_cells("nasa") == ("B0018",)
    assert independent_fold_cells("calce", ["CS2_37", "CS2_36"]) == ("CS2_36", "CS2_37")
    with pytest.raises(ValueError):
        independent_fold_cells("calce")
    with pytest.raises(ValueError):
        independent_fold_cells("nope")


def test_official_split() -> None:
    cells = pd.DataFrame(
        {"cell_id": ["b2", "b1", "t1", "u1"], "split": ["train", "train", "test1", "test2"]}
    )
    assert official_split(cells) == {"train": ("b1", "b2"), "test1": ("t1",), "test2": ("u1",)}
    only_train = cells.iloc[:2]
    assert official_split(only_train)["test2"] == ()
    with pytest.raises(ValueError):
        official_split(cells.assign(split=[None, "train", "test1", "test2"]))
    with pytest.raises(ValueError):
        official_split(cells.assign(split=["x", "train", "test1", "test2"]))
    with pytest.raises(ValueError):
        official_split(cells.drop(columns="split"))
    with pytest.raises(ValueError):
        official_split(cells.iloc[:0])


@settings(max_examples=60)
@given(
    st.lists(st.integers(0, 10_000), min_size=5, max_size=60, unique=True),
    st.integers(2, 5),
    st.integers(0, 99),
)
def test_grouped_kfold_partitions(nums: list[int], k: int, seed: int) -> None:
    ids = [f"cell{n}" for n in nums]
    folds = grouped_kfold(ids, k=k, seed=seed)
    assert len(folds) == k
    vals = [c for _, v in folds for c in v]
    assert sorted(vals) == sorted(ids)  # each cell in exactly one val fold
    sizes = [len(v) for _, v in folds]
    assert max(sizes) - min(sizes) <= 1
    for train, val in folds:
        assert not set(train) & set(val)
        assert set(train) | set(val) == set(ids)
    assert folds == grouped_kfold(list(reversed(ids)), k=k, seed=seed)  # deterministic


def test_grouped_kfold_validation() -> None:
    with pytest.raises(ValueError):
        grouped_kfold(["a", "b"], k=5)
    with pytest.raises(ValueError):
        grouped_kfold(["a", "b"], k=1)
    with pytest.raises(ValueError):
        grouped_kfold(["a", "a", "b"], k=2)
    assert grouped_kfold([f"c{i}" for i in range(10)], seed=0) != grouped_kfold(
        [f"c{i}" for i in range(10)], seed=1
    )
