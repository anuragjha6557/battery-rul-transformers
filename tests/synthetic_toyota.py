"""Synthetic Toyota-like processed tables shared by the tune tests (no torch/lightgbm import)."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from battery_rul.data.io import DatasetTables, finalize_and_validate, write_tables

N_CYC = 130
TRAIN = [f"t{i}" for i in range(6)]


def write_toyota(root: Path) -> None:
    ids = [*TRAIN, "a1", "b1"]
    splits = ["train"] * 6 + ["test1", "test2"]
    rng = np.random.default_rng(1)
    rows = []
    for i, c in enumerate(ids):
        cap = 1.1 * (1 - (0.3 + 0.03 * i) * np.arange(N_CYC) / N_CYC) + rng.normal(0, 0.002, N_CYC)
        rows.append(
            pd.DataFrame(
                {
                    "dataset": "toyota",
                    "cell_id": c,
                    "cycle_idx": np.arange(1, N_CYC + 1),
                    "capacity_ah": cap,
                    "charge_throughput_ah": cap * 1.02,
                    "cc_time_s": 1000.0 + rng.normal(0, 5, N_CYC),
                    "cv_time_s": 900.0 + rng.normal(0, 5, N_CYC),
                    "discharge_time_s": cap * 3000,
                }
            )
        )
    cells = pd.DataFrame(
        {
            "dataset": "toyota",
            "cell_id": ids,
            "chemistry": "x",
            "nominal_capacity_ah": 1.1,
            "charge_protocol": "cc",
            "discharge_protocol": "cc",
            "ambient_temp_c": 25.0,
            "v_max": 4.2,
            "v_min": 2.7,
            "batch": None,
            "split": splits,
            "reported_cycle_life": 100.0,
            "source_file": "synthetic",
        }
    )
    curves = pd.DataFrame(
        {
            "dataset": "toyota",
            "cell_id": ids[0],
            "cycle_idx": [1],
            "phase": ["charge"],
            "sample_idx": [0],
            "t_s": [0.0],
            "voltage_v": [3.7],
            "current_a": [1.0],
            "temp_c": [25.0],
            "charge_ah": [0.0],
        }
    )
    t = finalize_and_validate(cells, pd.concat(rows, ignore_index=True), curves)
    write_tables("toyota", DatasetTables(t.cells, t.cycles, t.curves), root)
