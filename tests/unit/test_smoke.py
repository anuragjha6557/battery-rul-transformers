"""Phase-0 smoke tests: package imports, CLI wiring, utilities."""

from __future__ import annotations

import numpy as np
import torch
from typer.testing import CliRunner

import battery_rul
from battery_rul.cli import app
from battery_rul.utils import config_hash, resolve_device, seed_everything

runner = CliRunner()


def test_version_is_set() -> None:
    assert battery_rul.__version__ != ""


def test_cli_help_lists_commands() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    for cmd in ("download", "build-data", "benchmark", "predict", "version"):
        assert cmd in result.output


def test_unimplemented_command_exits_nonzero() -> None:
    result = runner.invoke(app, ["predict", "x.csv"])
    assert result.exit_code == 2
    assert "Not implemented yet" in result.output


def test_seed_everything_is_reproducible() -> None:
    # The legacy global RNG is exactly what seed_everything must control.
    seed_everything(123)
    a = (np.random.rand(3), torch.rand(3))  # noqa: NPY002
    seed_everything(123)
    b = (np.random.rand(3), torch.rand(3))  # noqa: NPY002
    np.testing.assert_array_equal(a[0], b[0])
    assert torch.equal(a[1], b[1])


def test_resolve_device_defaults_to_cpu() -> None:
    assert resolve_device() == "cpu"
    assert resolve_device("auto") in {"cpu", "mps"}


def test_config_hash_is_order_invariant_and_sensitive() -> None:
    assert config_hash({"a": 1, "b": 2}) == config_hash({"b": 2, "a": 1})
    assert config_hash({"a": 1}) != config_hash({"a": 2})
    assert len(config_hash({})) == 12
