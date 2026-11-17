"""App smoke test: the Gradio prediction function on the tiny weights (skips without gradio)."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pandas as pd
import pytest
from conftest import synthetic_cell

pytest.importorskip("gradio")

APP = Path(__file__).resolve().parents[2] / "app" / "app.py"


@pytest.fixture(scope="module")
def app_mod(tiny_weights: Path):
    mp = pytest.MonkeyPatch()
    mp.setenv("BATTERY_RUL_WEIGHTS", str(tiny_weights))
    spec = importlib.util.spec_from_file_location("rul_app", APP)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    yield mod
    mp.undo()


def test_predict_ui_upload(app_mod, tmp_path: Path) -> None:
    from matplotlib.figure import Figure

    csv = tmp_path / "cell.csv"
    synthetic_cell(n=60, seed=1).to_csv(csv, index=False)
    fig, summary, ood = app_mod.predict_ui(str(csv), app_mod.UPLOAD)
    assert isinstance(fig, Figure)
    assert "RUL" in summary and "SOH" in summary
    assert isinstance(ood, str) and ood


def test_predict_ui_bad_input_is_clean(app_mod, tmp_path: Path) -> None:
    csv = tmp_path / "bad.csv"
    pd.DataFrame({"x": [1, 2, 3]}).to_csv(csv, index=False)
    fig, summary, _ = app_mod.predict_ui(str(csv), app_mod.UPLOAD)
    assert fig is None and "Input problem" in summary


def test_blocks_builds(app_mod) -> None:
    assert app_mod.build() is not None
