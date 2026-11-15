"""EOL / RUL labels per ADR-0005 (incl. Amendment 1).

Labels are computed in hindsight from each cell's full trajectory. That is legitimate for
targets and never for inputs; the feature/sample builders must not import this module's
results except as targets (PROTOCOL.md §4, rule 5).

- NASA, CALCE: ``masked`` + ``sustained(n=5)`` on SOH, with mask = skipped CV step | partial
  charge (artifacts, not degradation). A run cut off by the end of the record counts as censored.
- Toyota: the provider's ``reported_cycle_life`` (cycles to 0.88 Ah = 80 % of nominal). Tests
  were stopped at EOL by design, so the sustained rule is structurally censored there.
"""

from __future__ import annotations

from typing import Final, Literal

import numpy as np
import pandas as pd

from battery_rul.data.quality import KEY_COLS, flag_anomalies
from battery_rul.tasks.eol import eol_masked, eol_sustained

LabelSource = Literal["rule", "provider"]
SUSTAINED_N: Final = 5
EOL_MASK_FLAGS: Final = ("flag_skipped_cv", "flag_partial_charge")
TOYOTA_EOL_AH: Final = 0.88  # Severson's EOL: 80 % of 1.1 Ah nominal


def label_source(dataset: str) -> LabelSource:
    return "provider" if dataset == "toyota" else "rule"


def eol_mask(cycles: pd.DataFrame) -> pd.Series:
    """Boolean Series aligned with ``cycles.index``: cycles excluded from EOL labelling."""
    flags = flag_anomalies(cycles)
    merged = cycles[list(KEY_COLS)].merge(flags, on=list(KEY_COLS), how="left", validate="1:1")
    mask = np.zeros(len(cycles), dtype=bool)
    for col in EOL_MASK_FLAGS:
        mask |= merged[col].fillna(False).to_numpy(dtype=bool)
    return pd.Series(mask, index=cycles.index, name="eol_mask")


def eol_table(cycles: pd.DataFrame, cells: pd.DataFrame, theta: float = 0.8) -> pd.DataFrame:
    """One row per cell: ``cell_id, eol_cycle (float, NaN if censored), censored, label_source,
    theta, soh_ref_ah`` (``soh_ref_ah`` = the first-5-cycle reference capacity)."""
    datasets = cycles["dataset"].unique()
    if len(datasets) != 1:
        raise ValueError("eol_table expects a single dataset")
    dataset = str(datasets[0])
    src = label_source(dataset)
    cycles = cycles.sort_values(["cell_id", "cycle_idx"])
    mask = eol_mask(cycles) if src == "rule" else None
    provider = cells.set_index("cell_id")["reported_cycle_life"]

    rows = []
    for cell_id, g in cycles.groupby("cell_id", sort=True):
        soh_ref = float((g["capacity_ah"] / g["soh"]).iloc[0])
        if src == "provider":
            life = provider.get(cell_id, np.nan)
            eol, censored = (float(life), False) if np.isfinite(life) else (np.nan, True)
            th = TOYOTA_EOL_AH / soh_ref  # SOH-equivalent of 0.88 Ah for this cell
        else:
            assert mask is not None
            res = eol_masked(
                g["cycle_idx"].to_numpy(),
                g["soh"].to_numpy(),
                theta,
                mask.loc[g.index].to_numpy(),
                base=lambda c, s, t: eol_sustained(c, s, t, n=SUSTAINED_N),
            )
            eol = float(res.eol_cycle) if res.eol_cycle is not None else np.nan
            censored, th = res.censored, theta
        rows.append(
            {
                "cell_id": cell_id,
                "eol_cycle": eol,
                "censored": censored,
                "label_source": src,
                "theta": th,
                "soh_ref_ah": soh_ref,
            }
        )
    return pd.DataFrame(rows)
