"""Reproduce Severson et al. 2019 cycle-life prediction on the Toyota/MIT-Stanford data.

Usage: ``BATTERY_RUL_DATA_DIR=<dir with processed/> uv run python scripts/severson_repro.py``

Trains ElasticNet (4-fold CV over alpha / l1_ratio, as in the paper) on log10(cycle life) with the
official train split and evaluates on test1 (primary) and test2 (secondary). Writes
``reports/tables/severson_repro.md``. Cycle life = ``cells.reported_cycle_life`` (the provider's
label); this script is a benchmark-reproduction tool, so using the label as a *target* is fine.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import ElasticNetCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from battery_rul.data.io import read_tables
from battery_rul.features.severson import severson_feature_table

OUT = Path(__file__).resolve().parents[1] / "reports" / "tables" / "severson_repro.md"

MODELS: dict[str, list[str]] = {
    "variance": ["dq_var"],
    "discharge": ["dq_min", "dq_var", "dq_skew", "dq_kurt", "q2", "qmax_minus_q2"],
    "full": [
        "dq_min",
        "dq_var",
        "dq_skew",
        "dq_kurt",
        "q2",
        "qmax_minus_q2",
        "fade_slope",
        "fade_intercept",
        "charge_time_mean_2_6",
        "ir_min",
        "ir_delta",
        "temp_integral",
    ],
}

# Recalled from Severson 2019 Table 1 (mean % error, [train, primary test, secondary test]).
# NOT verified against the paper text in this environment -- check before citing.
PUBLISHED_UNVERIFIED = {
    "variance": "~14 / ~15 / ~11",
    "discharge": "~10 / ~13 / ~11",
    "full": "~5.6 / ~7.5 / ~10.7 (abstract: 9.1 % test error)",
}


def _fit(x: pd.DataFrame, y: np.ndarray) -> Pipeline:
    pipe = Pipeline(
        [
            ("impute", SimpleImputer(strategy="median")),
            ("scale", StandardScaler()),
            (
                "enet",
                ElasticNetCV(
                    l1_ratio=[0.1, 0.5, 0.7, 0.9, 0.95, 0.99, 1.0],
                    cv=4,
                    max_iter=100000,
                    random_state=0,
                ),
            ),
        ]
    )
    return pipe.fit(x, y)


def _metrics(life_true: np.ndarray, life_pred: np.ndarray) -> tuple[float, float]:
    rmse = float(np.sqrt(np.mean((life_pred - life_true) ** 2)))
    pct = float(np.mean(np.abs(life_pred - life_true) / life_true) * 100)
    return rmse, pct


def main() -> None:
    t = read_tables("toyota")
    feats = severson_feature_table(t.cycles, t.curves)
    cells = t.cells.set_index("cell_id")
    life = cells["reported_cycle_life"]
    split = cells["split"]
    ok = life.notna() & feats["dq_var"].notna()
    dropped = int((~ok).sum())

    rows = []
    for name, cols in MODELS.items():
        tr = (split == "train") & ok
        model = _fit(feats.loc[tr, cols], np.log10(life[tr].to_numpy()))
        for part in ("train", "test1", "test2"):
            m = (split == part) & ok
            pred = 10 ** model.predict(feats.loc[m, cols])
            rmse, pct = _metrics(life[m].to_numpy(), pred)
            rows.append((name, part, int(m.sum()), rmse, pct))
    df = pd.DataFrame(rows, columns=["model", "split", "n_cells", "rmse_cycles", "mean_pct_error"])

    lines = [
        "# Severson 2019 reproduction (Toyota / MIT-Stanford, cycles 1-100 features)",
        "",
        "Target: log10(cycle life) (provider label); ElasticNetCV (4-fold), official train split.",
        f"Cells dropped for missing features/label: {dropped}.",
        "Temperature feature uses per-cycle `discharge_temp_max_c` (only one available).",
        "",
        "| model | split | n cells | RMSE (cycles) | mean % error |",
        "|---|---|---|---|---|",
    ]
    lines += [
        f"| {r.model} | {r.split} | {r.n_cells} | {r.rmse_cycles:.0f} | {r.mean_pct_error:.1f} |"
        for r in df.itertuples()
    ]
    lines += [
        "",
        "Published mean % error (train / primary test / secondary test), recalled from Severson",
        "et al. 2019 Table 1 -- **published values to verify** against the paper before citing:",
        "",
        "| model | published (unverified) |",
        "|---|---|",
        *[f"| {k} | {v} |" for k, v in PUBLISHED_UNVERIFIED.items()],
        "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
