# ruff: noqa: E501, PD010
"""Generate ``reports/data_quality.md`` and PNGs under ``reports/figures/data_quality/``.

Deterministic and re-runnable (no RNG). Every number in the report is computed here. Run::

    BATTERY_RUL_DATA_DIR=/path/to/data uv run python scripts/make_data_quality_report.py

To add Toyota later, append ``"toyota"`` to ``DATASETS`` (and, if wanted, to
``REPRESENTATIVE_CELL``); nothing else is dataset-specific.
"""

from __future__ import annotations

import math
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
from scipy.signal import savgol_filter
from scipy.stats import spearmanr

from battery_rul.data.io import read_tables
from battery_rul.data.quality import FLAG_COLS, KEY_COLS, flag_anomalies
from battery_rul.tasks.eol import (
    EOLResult,
    eol_masked,
    eol_raw,
    eol_rolling_median,
    eol_sustained,
)
from battery_rul.utils import PROCESSED_DIR, REPORTS_DIR

# ----------------------------------------------------------------------------- configuration
DATASETS = ["nasa", "calce"]  # add "toyota" here once its processed tables exist
REPRESENTATIVE_CELL = {"nasa": "B0005", "calce": "CS2_35"}
SHARED_RIG = {"nasa": ["B0005", "B0006", "B0007"]}  # cells cycled together (same timestamps)
THRESHOLDS = (0.8, 0.7)
RULE_COLS = ["raw", "rolling_median", "sustained", "masked"]  # the rules compared in the spread
SENSITIVITY_COL = "rolling_median_11"  # shown, not counted in the spread
SPREAD_HIGHLIGHT = 50  # cycles
MAX_PANELS = 8  # cap on small-multiple panels per dataset
#: flags whose cycles are removed (masked) when building labels; the other two are informational
MASK_FLAGS = ("flag_skipped_cv", "flag_partial_charge")
TASK_A_FEATURES = [
    "charge_time_s",
    "cc_time_s",
    "cv_time_s",
    "charge_throughput_ah",
    "charge_temp_max_c",
    "charge_temp_mean_c",
    "ir_ohm",
    "rest_before_s",
]
DISCHARGE_FEATURES = ["discharge_time_s", "discharge_energy_wh", "discharge_temp_max_c"]
LONG_REST_RIG_S = 1e5  # "weekend-scale" rest used in the shared-rig figure

OUT_MD = REPORTS_DIR / "data_quality.md"
FIG_DIR = REPORTS_DIR / "figures" / "data_quality"

# ----------------------------------------------------------------------------- style
BG = "#fcfcfb"
TXT = "#52514e"
TITLE = "#0b0b0b"
CAT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
RAMP = [
    "#86b6ef",
    "#6da7ec",
    "#5598e7",
    "#3987e5",
    "#2a78d6",
    "#256abf",
    "#1c5cab",
    "#184f95",
    "#104281",
    "#0d366b",
]
CMAP = LinearSegmentedColormap.from_list("blue_ramp", RAMP)
FLAG_PRIORITY = [
    "flag_skipped_cv",
    "flag_partial_charge",
    "flag_no_paired_charge",
    "flag_long_rest",
]
FLAG_MARKERS = ["x", "+", "D"]  # x, +, diamond (hollow)


def set_style() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": BG,
            "axes.facecolor": BG,
            "savefig.facecolor": BG,
            "axes.edgecolor": "#c9c8c4",
            "axes.labelcolor": TXT,
            "xtick.color": TXT,
            "ytick.color": TXT,
            "text.color": TXT,
            "axes.titlecolor": TITLE,
            "axes.titlesize": 10,
            "axes.labelsize": 9,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "legend.fontsize": 8,
            "legend.frameon": False,
            "axes.grid": True,
            "grid.color": "#bdbcb8",
            "grid.alpha": 0.3,
            "grid.linewidth": 0.6,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "lines.linewidth": 1.5,
            "font.size": 9,
        }
    )


def save(fig: plt.Figure, name: str) -> str:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / name, dpi=150, bbox_inches="tight", metadata={"Software": None})
    plt.close(fig)
    return f"figures/data_quality/{name}"


# ----------------------------------------------------------------------------- loading
def load_all() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return (cells, cycles incl. flag columns) for every dataset in DATASETS."""
    cells, cycles = [], []
    for ds in DATASETS:
        t = read_tables(ds, curves=False)
        cells.append(t.cells)
        cycles.append(t.cycles)
    cells_df = pd.concat(cells, ignore_index=True)
    cyc = pd.concat(cycles, ignore_index=True)
    cyc = cyc.sort_values(["dataset", "cell_id", "cycle_idx"]).reset_index(drop=True)
    flags = flag_anomalies(cyc)
    cyc = cyc.join(flags.drop(columns=list(KEY_COLS)))
    cyc["mask"] = cyc[list(MASK_FLAGS)].any(axis=1)
    prev = cyc.groupby(["dataset", "cell_id"])["cycle_idx"].diff()
    cyc["d_soh"] = cyc.groupby(["dataset", "cell_id"])["soh"].diff().where(prev == 1)
    prev_mask = cyc.groupby(["dataset", "cell_id"])["mask"].shift(1, fill_value=False)
    cyc["mask_or_prev"] = cyc["mask"] | prev_mask.astype(bool)
    cyc["d_cap"] = cyc.groupby(["dataset", "cell_id"])["capacity_ah"].diff().where(prev == 1)
    return cells_df, cyc


def cell_groups(cyc: pd.DataFrame, ds: str) -> list[tuple[str, pd.DataFrame]]:
    sub = cyc[cyc["dataset"] == ds]
    return [(str(c), g.reset_index(drop=True)) for c, g in sub.groupby("cell_id", sort=True)]


# ----------------------------------------------------------------------------- markdown helpers
def md_table(df: pd.DataFrame, index: bool = False) -> str:
    d = df.reset_index() if index else df
    head = "| " + " | ".join(str(c) for c in d.columns) + " |"
    sep = "|" + "|".join("---" for _ in d.columns) + "|"
    rows = ["| " + " | ".join(str(v) for v in r) + " |" for r in d.to_numpy().tolist()]
    return "\n".join([head, sep, *rows])


def f(x: float, nd: int = 3) -> str:
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.{nd}f}"


def pct(x: float) -> str:
    return f"{100 * x:.1f} %"


# ----------------------------------------------------------------------------- EOL
def eol_all_rules(g: pd.DataFrame, thr: float) -> dict[str, EOLResult]:
    ci = g["cycle_idx"].to_numpy()
    soh = g["soh"].to_numpy()
    mask = g["mask"].to_numpy()
    return {
        "raw": eol_raw(ci, soh, thr),
        "rolling_median": eol_rolling_median(ci, soh, thr, window=5),
        "sustained": eol_sustained(ci, soh, thr, n=5),
        "masked": eol_masked(ci, soh, thr, mask, base=eol_sustained),
        SENSITIVITY_COL: eol_rolling_median(ci, soh, thr, window=11),
    }


def spread_of(res: dict[str, EOLResult]) -> tuple[float, str, bool]:
    """(numeric spread or nan, display string, highlight?) across the core RULE_COLS."""
    vals = [res[r] for r in RULE_COLS]
    n_cens = sum(v.censored for v in vals)
    if n_cens == len(vals):
        return float("nan"), "all censored", False
    if n_cens:
        return float("nan"), f"mixed ({n_cens}/{len(vals)} censored)", True
    cyc = [v.eol_cycle for v in vals if v.eol_cycle is not None]
    sp = max(cyc) - min(cyc)
    return float(sp), str(sp), sp > SPREAD_HIGHLIGHT


def eol_tables(cyc: pd.DataFrame) -> tuple[dict[float, pd.DataFrame], pd.DataFrame]:
    """Per-threshold display tables plus a long frame (dataset, cell, thr, rule, eol, censored)."""
    tables: dict[float, pd.DataFrame] = {}
    long_rows: list[dict[str, Any]] = []
    for thr in THRESHOLDS:
        rows = []
        for ds in DATASETS:
            for cell, g in cell_groups(cyc, ds):
                res = eol_all_rules(g, thr)
                sp, sp_txt, hi = spread_of(res)
                row: dict[str, Any] = {"dataset": ds, "cell": cell}
                for rule in [*RULE_COLS, SENSITIVITY_COL]:
                    r = res[rule]
                    row[rule] = "censored" if r.censored else str(r.eol_cycle)
                    long_rows.append(
                        {
                            "dataset": ds,
                            "cell": cell,
                            "thr": thr,
                            "rule": rule,
                            "eol": r.eol_cycle,
                            "censored": r.censored,
                        }
                    )
                row["spread (max-min)"] = f"**{sp_txt}**" if hi else sp_txt
                row["_spread"] = sp
                row["_hi"] = hi
                rows.append(row)
        tables[thr] = pd.DataFrame(rows)
    return tables, pd.DataFrame(long_rows)


# ----------------------------------------------------------------------------- tables
def overview_table(cyc: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for ds in DATASETS:
        for cell, g in cell_groups(cyc, ds):
            row: dict[str, Any] = {
                "dataset": ds,
                "cell": cell,
                "n_cycles": len(g),
                "first Ah": f(g["capacity_ah"].iloc[0]),
                "last Ah": f(g["capacity_ah"].iloc[-1]),
                "min SOH": f(g["soh"].min()),
            }
            for col in FLAG_COLS:
                row[col.removeprefix("flag_")] = int(g[col].sum())
            row["masked (skipped_cv or partial)"] = int(g["mask"].sum())
            rows.append(row)
    return pd.DataFrame(rows)


def local_dev(g: pd.DataFrame) -> pd.Series:
    """SOH minus its centered 11-cycle rolling median (signed local deviation)."""
    return g["soh"] - g["soh"].rolling(11, center=True, min_periods=1).median()


def flag_effect_table(cyc: pd.DataFrame) -> pd.DataFrame:
    """Median signed / absolute local SOH deviation of flagged vs unflagged cycles."""
    rows = []
    for ds in DATASETS:
        parts = []
        for _, g in cell_groups(cyc, ds):
            g = g.copy()
            g["dev"] = local_dev(g)
            parts.append(g)
        d = pd.concat(parts)
        for col in FLAG_COLS:
            fl, ok = d[d[col]], d[~d[col]]
            rows.append(
                {
                    "dataset": ds,
                    "flag": col.removeprefix("flag_"),
                    "n flagged": len(fl),
                    "share of cycles": pct(len(fl) / len(d)),
                    "median signed dSOH vs local median (flagged)": f(fl["dev"].median(), 4),
                    "median abs dSOH (flagged)": f(fl["dev"].abs().median(), 4),
                    "median abs dSOH (unflagged)": f(ok["dev"].abs().median(), 4),
                }
            )
    return pd.DataFrame(rows)


def spearman(a: pd.Series, b: pd.Series) -> float:
    ok = a.notna() & b.notna()
    if ok.sum() < 10 or a[ok].nunique() < 2 or b[ok].nunique() < 2:
        return float("nan")
    return float(spearmanr(a[ok], b[ok]).statistic)


def feature_table(cyc: pd.DataFrame, features: list[str]) -> pd.DataFrame:
    """Spearman rho (per-cell, mean [min, max] over cells) of each feature with SOH."""
    rows = []
    for feat in features:
        row: dict[str, Any] = {"feature": feat}
        for ds in DATASETS:
            for label, only_clean in (("all cycles", False), ("masked cycles dropped", True)):
                rhos = []
                for _, g in cell_groups(cyc, ds):
                    gg = g[~g["mask"]] if only_clean else g
                    rhos.append(spearman(gg[feat], gg["soh"]))
                arr = np.array(rhos, dtype=float)
                if np.isnan(arr).all():
                    txt = "n/a"
                else:
                    txt = f"{np.nanmean(arr):+.2f} [{np.nanmin(arr):+.2f}, {np.nanmax(arr):+.2f}]"
                row[f"{ds}, {label}"] = txt
        rows.append(row)
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- figures
def fig_soh_panels(
    cyc: pd.DataFrame, ds: str, eol_long: pd.DataFrame, fname: str
) -> tuple[str, bool]:
    groups = cell_groups(cyc, ds)
    shown = groups[:MAX_PANELS]
    ncols = 2 if len(shown) > 1 else 1
    nrows = math.ceil(len(shown) / ncols)
    fig, axes = plt.subplots(
        nrows, ncols, figsize=(6.2 * ncols, 3.3 * nrows), sharey=True, squeeze=False
    )
    lo = float(min(g["soh"].min() for _, g in shown))
    tick_colors = {"raw": CAT[1], "sustained": CAT[2], "masked": CAT[3]}
    for ax, (cell, g) in zip(axes.ravel(), shown, strict=False):
        ax.plot(g["cycle_idx"], g["soh"], color=CAT[0], lw=1.5)
        for thr in THRESHOLDS:
            ax.axhline(thr, color=TXT, lw=1.0, ls="--" if thr == 0.8 else ":", alpha=0.8)
        # flag markers: top-2 named flags by priority with hits, rest folded into "other flag"
        present = [c for c in FLAG_PRIORITY if g[c].any()]
        named = present[:2]
        other_mask = g[[c for c in FLAG_PRIORITY if c not in named]].any(axis=1)
        handles = []
        for col, mk in zip(named, FLAG_MARKERS[:2], strict=False):
            sub = g[g[col]]
            ax.scatter(
                sub["cycle_idx"],
                sub["soh"],
                marker=mk,
                s=45,
                color=TITLE,
                linewidths=1.4,
                zorder=4,
            )
            handles.append(Line2D([], [], ls="", marker=mk, ms=7, color=TITLE, label=col[5:]))
        if other_mask.any():
            sub = g[other_mask & ~g[named].any(axis=1) if named else other_mask]
            if len(sub):
                ax.scatter(
                    sub["cycle_idx"],
                    sub["soh"],
                    marker="D",
                    s=36,
                    facecolors="none",
                    edgecolors=TITLE,
                    linewidths=1.2,
                    zorder=4,
                )
                handles.append(
                    Line2D(
                        [], [], ls="", marker="D", ms=6, mfc="none", color=TITLE, label="other flag"
                    )
                )
        # EOL ticks (bands at the top of the axes): 80 % band first, 70 % band below
        sel = eol_long[(eol_long["dataset"] == ds) & (eol_long["cell"] == cell)]
        for bi, thr in enumerate(THRESHOLDS):
            for ri, rule in enumerate(["raw", "sustained", "masked"]):
                row = sel[(sel["thr"] == thr) & (sel["rule"] == rule)]
                if row.empty or bool(row["censored"].iloc[0]):
                    continue
                x = float(row["eol"].iloc[0])
                top = 1.0 - (bi * 3 + ri) * 0.035
                ax.axvline(
                    x,
                    ymin=top - 0.033,
                    ymax=top,
                    color=tick_colors[rule],
                    lw=2.0,
                    solid_capstyle="butt",
                )
        ax.set_title(f"{ds.upper()} {cell}")
        ax.set_xlabel("cycle")
        ax.set_ylim(lo - 0.04, 1.25)
        if handles:
            ax.legend(handles=handles, loc="lower left", fontsize=7)
    for ax in axes.ravel()[len(shown) :]:
        ax.set_visible(False)
    for r in range(nrows):
        axes[r, 0].set_ylabel("SOH")
    legend_handles = [
        Line2D([], [], color=CAT[0], lw=1.5, label="SOH"),
        Line2D([], [], color=TXT, lw=1, ls="--", label="80 %"),
        Line2D([], [], color=TXT, lw=1, ls=":", label="70 %"),
        Line2D([], [], color=CAT[1], lw=2.5, label="EOL raw"),
        Line2D([], [], color=CAT[2], lw=2.5, label="EOL sustained"),
        Line2D([], [], color=CAT[3], lw=2.5, label="EOL masked"),
    ]
    fig.legend(
        handles=legend_handles, loc="lower center", ncol=6, bbox_to_anchor=(0.5, -0.02 / nrows)
    )
    fig.suptitle(
        f"{ds.upper()}: SOH vs cycle (EOL ticks: upper three = 80 %, lower three = 70 %)",
        color=TITLE,
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0.05 / nrows, 1, 0.97))
    return save(fig, fname), len(groups) > len(shown)


def fig_shared_rig(cyc: pd.DataFrame, ds: str, cells: list[str], fname: str) -> str:
    sub = cyc[(cyc["dataset"] == ds) & (cyc["cell_id"].isin(cells))]
    fig, ax = plt.subplots(figsize=(9, 4.2))
    long_cycles: set[int] = set()
    for i, cell in enumerate(cells):
        g = sub[sub["cell_id"] == cell]
        ax.plot(g["cycle_idx"], g["soh"], color=CAT[i], lw=1.5, label=cell)
        long_cycles |= set(g.loc[g["rest_before_s"] > LONG_REST_RIG_S, "cycle_idx"].tolist())
    for x in sorted(long_cycles):
        ax.axvline(x, color=TXT, lw=1.0, ls=":", alpha=0.8)
    ax.plot([], [], color=TXT, lw=1.0, ls=":", label="rest before cycle > 1e5 s")
    ax.set_xlabel("cycle_idx")
    ax.set_ylabel("SOH")
    ax.set_title(f"{ds.upper()} shared rig: {', '.join(cells)} aligned by cycle_idx")
    ax.legend(loc="lower left")
    return save(fig, fname)


def fig_regen_vs_rest(cyc: pd.DataFrame, fname: str) -> tuple[str, dict[str, dict[str, float]]]:
    fig, axes = plt.subplots(
        1, len(DATASETS), figsize=(5.4 * len(DATASETS), 4.2), sharey=True, squeeze=False
    )
    stats: dict[str, dict[str, float]] = {}
    for ax, ds in zip(axes[0], DATASETS, strict=True):
        d = cyc[(cyc["dataset"] == ds) & cyc["d_soh"].notna() & (cyc["rest_before_s"] > 0)].copy()
        x = np.log10(d["rest_before_s"])
        ax.scatter(
            x,
            d["d_soh"],
            s=36,
            marker="o",
            color=CAT[0],
            alpha=0.45,
            linewidths=0,
            label="all cycles",
        )
        sk = d["flag_skipped_cv"]
        ax.scatter(
            x[sk],
            d.loc[sk, "d_soh"],
            s=45,
            marker="+",
            color=TITLE,
            linewidths=1.4,
            label="skipped_cv",
        )
        ax.set_title(ds.upper())
        ax.set_xlabel("log10(rest_before_s)")
        ax.legend(loc="lower right")
        stats[ds] = {
            "rho_all": spearman(x, d["d_soh"]),
            "rho_clean": spearman(x[~d["mask_or_prev"]], d.loc[~d["mask_or_prev"], "d_soh"]),
            "n_clean": float((~d["mask_or_prev"]).sum()),
            "n_rebound": float(((d["d_soh"] > 0.05) & (d["rest_before_s"] < 3600)).sum()),
            "n_rebound_after_mask": float(
                ((d["d_soh"] > 0.05) & (d["rest_before_s"] < 3600) & d["mask_or_prev"]).sum()
            ),
            "n": float(len(d)),
        }
    axes[0, 0].set_ylabel("dSOH vs previous cycle")
    fig.tight_layout()
    return save(fig, fname), stats


def ica_curve(g: pd.DataFrame) -> tuple[np.ndarray, np.ndarray] | None:
    """dQ/dV (Ah/V) vs V on the CC part of one charge phase (5 mV grid, Savitzky-Golay)."""
    g = g.sort_values("sample_idx")
    i, v, q = g["current_a"].to_numpy(), g["voltage_v"].to_numpy(), g["charge_ah"].to_numpy()
    if len(g) < 20 or not np.isfinite(i).any():
        return None
    i_cc = np.median(i[i > 0.5 * np.nanmax(i)])
    inband = (i > 0.95 * i_cc) & (i < 1.05 * i_cc)
    idx = np.flatnonzero(inband)
    if idx.size == 0:
        return None
    start = idx[0]
    stop = start
    while stop < len(i) and inband[stop]:
        stop += 1
    vv = np.maximum.accumulate(v[start:stop])
    qq = q[start:stop]
    vu, first = np.unique(vv, return_index=True)
    if len(vu) < 12:
        return None
    grid = np.arange(np.ceil(vu[0] / 0.005) * 0.005, vu[-1], 0.005)
    if len(grid) < 12:
        return None
    qg = np.interp(grid, vu, qq[first])
    qs = savgol_filter(qg, 9, 3)
    return grid, np.gradient(qs, grid)


def fig_charge_curves(fname: str, steps: dict[str, int]) -> tuple[str, dict[str, list[int]]]:
    fig, axes = plt.subplots(
        len(DATASETS), 2, figsize=(11, 3.9 * len(DATASETS)), squeeze=False, constrained_layout=True
    )
    used: dict[str, list[int]] = {}
    for r, ds in enumerate(DATASETS):
        cell = REPRESENTATIVE_CELL[ds]
        c = pd.read_parquet(
            PROCESSED_DIR / ds / "curves.parquet",
            filters=[("cell_id", "==", cell), ("phase", "==", "charge")],
        )
        cycles_all = sorted(c["cycle_idx"].unique().tolist())
        sel = cycles_all[steps[ds] - 1 :: steps[ds]]
        used[ds] = sel
        for k in sel:
            g = c[c["cycle_idx"] == k]
            color = CMAP(k / cycles_all[-1])
            g = g[g["current_a"] > 0.05]
            axes[r, 0].plot(g["t_s"], g["voltage_v"], color=color, lw=1.5)
            ica = ica_curve(c[c["cycle_idx"] == k])
            if ica is not None:
                axes[r, 1].plot(ica[0], ica[1], color=color, lw=1.5)
        axes[r, 0].set_title(f"{ds.upper()} {cell}: charge voltage vs time")
        axes[r, 0].set_xlabel("time in charge phase (s)")
        axes[r, 0].set_ylabel("voltage (V)")
        axes[r, 1].set_title(f"{ds.upper()} {cell}: incremental capacity, CC charge")
        axes[r, 1].set_xlabel("voltage (V)")
        axes[r, 1].set_ylabel("dQ/dV (Ah/V)")
        sm = plt.cm.ScalarMappable(cmap=CMAP, norm=plt.Normalize(1, cycles_all[-1]))
        cb = fig.colorbar(sm, ax=axes[r].tolist(), shrink=0.9, pad=0.02)
        cb.set_label("cycle")
    return save(fig, fname), used


# ----------------------------------------------------------------------------- findings helpers
def nasa_curve_checks(ds: str = "nasa") -> pd.DataFrame:
    """Discharge-record checks from the curves: last voltage and integral(|I|dt) vs capacity."""
    c = pd.read_parquet(
        PROCESSED_DIR / ds / "curves.parquet",
        columns=["cell_id", "cycle_idx", "phase", "sample_idx", "t_s", "voltage_v", "current_a"],
    )
    cyc = read_tables(ds, curves=False).cycles
    rows = []
    d = c[c["phase"] == "discharge"].sort_values(["cell_id", "cycle_idx", "sample_idx"])
    last_v = d.groupby(["cell_id", "cycle_idx"])["voltage_v"].last()
    d = d.assign(absi=d["current_a"].abs())
    # trapezoid integral of |I| dt per cycle (vectorised over groups)
    d["dt"] = d.groupby(["cell_id", "cycle_idx"])["t_s"].diff().fillna(0.0)
    d["prev_i"] = d.groupby(["cell_id", "cycle_idx"])["absi"].shift(1).fillna(d["absi"])
    d["area"] = 0.5 * (d["absi"] + d["prev_i"]) * d["dt"] / 3600.0
    ah = d.groupby(["cell_id", "cycle_idx"])["area"].sum()
    cells = read_tables(ds, curves=False).cells.set_index("cell_id")
    for cell, g in cyc.groupby("cell_id"):
        lv = last_v.loc[cell]
        a = ah.loc[cell]
        cap = g.set_index("cycle_idx")["capacity_ah"]
        rel = ((a.reindex(cap.index) - cap).abs() / cap).dropna()
        rows.append(
            {
                "cell": cell,
                "v_min (cut-off)": f(float(cells.loc[cell, "v_min"]), 2),
                "median last discharge V": f(float(lv.median()), 3),
                "share of cycles ending > 0.1 V above cut-off": pct(
                    float((lv > cells.loc[cell, "v_min"] + 0.1).mean())
                ),
                "median |int|I|dt - capacity| / capacity": pct(float(rel.median())),
                "max": pct(float(rel.max())),
            }
        )
    return pd.DataFrame(rows)


def first_charge_spike(ds: str = "nasa") -> pd.DataFrame:
    c = pd.read_parquet(
        PROCESSED_DIR / ds / "curves.parquet",
        columns=["cell_id", "cycle_idx", "phase", "sample_idx", "current_a"],
        filters=[("phase", "==", "charge"), ("sample_idx", "<", 4)],
    )
    rows = []
    for cell, g in c.groupby("cell_id"):
        by = g.groupby("cycle_idx")["current_a"].min()
        rows.append(
            {
                "cell": cell,
                "cycles with a negative current in first 4 charge samples": int((by < -1.0).sum()),
                "of": len(by),
                "min current (A)": f(float(by.min()), 2),
            }
        )
    return pd.DataFrame(rows)


# ----------------------------------------------------------------------------- main
def main() -> None:
    set_style()
    _, cyc = load_all()
    eol_tabs, eol_long = eol_tables(cyc)
    overview = overview_table(cyc)
    fx = flag_effect_table(cyc)

    figs: dict[str, str] = {}
    truncated: dict[str, bool] = {}
    for ds in DATASETS:
        figs[f"soh_{ds}"], truncated[ds] = fig_soh_panels(cyc, ds, eol_long, f"soh_{ds}.png")
    for ds, rig in SHARED_RIG.items():
        figs[f"rig_{ds}"] = fig_shared_rig(cyc, ds, rig, f"shared_rig_{ds}.png")
    figs["regen"], regen_stats = fig_regen_vs_rest(cyc, "regen_vs_rest.png")
    figs["curves"], used = fig_charge_curves("charge_curves_ica.png", {"nasa": 10, "calce": 50})

    task_a = feature_table(cyc, TASK_A_FEATURES)
    forbidden = feature_table(cyc, DISCHARGE_FEATURES)

    md: list[str] = []
    w = md.append
    w("# Data-quality report (Phase 2)\n")
    w(
        "_Generated by `scripts/make_data_quality_report.py`; every number below is computed "
        "from `data/processed/`. Do not edit by hand._\n"
    )
    w(
        f"Datasets analysed: {', '.join(DATASETS)}. Flags come from "
        "`battery_rul.data.quality.flag_anomalies` (derived; the parsed tables are untouched). "
        "EOL rules come from `battery_rul.tasks.eol` and are computed in hindsight on the full "
        "trajectory, which is legitimate for labels and never for model inputs.\n"
    )

    w("## Flag definitions\n")
    from battery_rul.data import quality as q

    w(
        md_table(
            pd.DataFrame(
                [
                    [
                        "no_paired_charge",
                        "charge_time_s is NaN (no charge record before this discharge)",
                        "error",
                    ],
                    [
                        "partial_charge",
                        f"charge_throughput_ah < {q.PARTIAL_CHARGE_FRAC} x centered {q.PARTIAL_CHARGE_WINDOW}-cycle rolling median",
                        "error",
                    ],
                    [
                        "skipped_cv",
                        f"cv_time_s < {q.SKIPPED_CV_S:.0f} s (Arbin CV step ended after one sample)",
                        "error",
                    ],
                    ["long_rest", f"rest_before_s > {q.LONG_REST_S / 3600:.0f} h", "informational"],
                    [
                        "capacity_jump",
                        f"|capacity change| > {q.JUMP_FACTOR:.0f} x centered {q.JUMP_WINDOW}-cycle rolling-median |change|",
                        "informational",
                    ],
                ],
                columns=["flag", "rule", "type"],
            )
        )
    )
    w(
        "\nLabel mask used for the `masked` EOL rule: "
        + " or ".join(c.removeprefix("flag_") for c in MASK_FLAGS)
        + ".\n"
    )

    # ------------------------------------------------ per dataset
    for ds in DATASETS:
        w(f"## {ds.upper()}\n")
        w("### Per-cell overview and flag counts\n")
        w(md_table(overview[overview["dataset"] == ds].drop(columns="dataset")) + "\n")
        for thr in THRESHOLDS:
            t = eol_tabs[thr]
            t = t[t["dataset"] == ds]
            show = t.drop(columns=["dataset", "_spread", "_hi"]).rename(
                columns={
                    "rolling_median": "rolling_median (w=5)",
                    "sustained": "sustained (n=5)",
                    "masked": "masked (sustained)",
                    SENSITIVITY_COL: "rolling_median (w=11, sensitivity)",
                }
            )
            w(f"### EOL cycle at SOH < {thr:.0%}\n")
            w(md_table(show) + "\n")
            n_hi = int(t["_hi"].sum())
            w(
                f"Rule choice moves EOL by more than {SPREAD_HIGHLIGHT} cycles (or flips "
                f"censoring) in **{n_hi} of {len(t)}** cells (spread over raw, rolling_median, "
                "sustained, masked; the w=11 column is not counted).\n"
            )
        w("### SOH trajectories\n")
        w(f"![SOH {ds}]({figs[f'soh_{ds}']})\n")
        w(
            "_Black markers (x, +) are the two most frequent error-type flags in that panel; "
            'open diamonds fold the remaining error-type flags and long_rest into "other flag" '
            "(capacity_jump is not drawn, it marks too many cycles to read). Ticks at the top "
            "of each panel are EOL cycles: upper three bands 80 %, lower three bands 70 %._\n"
        )
        if truncated[ds]:
            w(f"_Only the first {MAX_PANELS} cells are drawn._\n")
        if ds in SHARED_RIG:
            w("### Shared rig\n")
            w(f"![shared rig {ds}]({figs[f'rig_{ds}']})\n")
            rig = SHARED_RIG[ds]
            wide = (
                cyc[(cyc["dataset"] == ds) & cyc["cell_id"].isin(rig)]
                .pivot(index="cycle_idx", columns="cell_id", values="rest_before_s")
                .dropna()
            )
            same = bool(np.allclose(wide.to_numpy(), wide.to_numpy()[:, [0]], rtol=1e-6, atol=1.0))
            n_same = int((wide.max(axis=1) - wide.min(axis=1) < 1.0).sum())
            lc = wide[(wide > LONG_REST_RIG_S).all(axis=1)].index.tolist()
            jump = (
                cyc[(cyc["dataset"] == ds) & cyc["cell_id"].isin(rig)]
                .pivot(index="cycle_idx", columns="cell_id", values="flag_capacity_jump")
                .fillna(False)
                .astype(bool)
            )
            any_j = jump.any(axis=1)
            all_j = jump.all(axis=1)
            npc = (
                cyc[(cyc["dataset"] == ds) & cyc["cell_id"].isin(rig)]
                .pivot(index="cycle_idx", columns="cell_id", values="flag_no_paired_charge")
                .fillna(False)
                .astype(bool)
            )
            npc_all = npc[npc.all(axis=1)].index.tolist()
            dsoh = cyc[(cyc["dataset"] == ds) & cyc["cell_id"].isin(rig)].pivot(
                index="cycle_idx", columns="cell_id", values="d_soh"
            )
            pair_txt = ", ".join(
                f"{a}-{b}: {f(spearman(dsoh[a], dsoh[b]), 2)}"
                for i, a in enumerate(rig)
                for b in rig[i + 1 :]
            )
            w(
                f"- `rest_before_s` agrees to within 1 s on **{n_same} of {len(wide)}** shared "
                f"cycles across {', '.join(rig)} (all identical: {same}).\n"
                f"- Cycles with rest > {LONG_REST_RIG_S:.0e} s on all three: {lc}.\n"
                f"- Cycles with no paired charge on all three: {npc_all}.\n"
                f"- capacity_jump flagged on at least one of the three at {int(any_j.sum())} "
                f"cycles, on all three at {int(all_j.sum())}.\n"
                f"- Spearman rho of cycle-to-cycle dSOH between cells: {pair_txt}.\n"
            )
            others = [c for c, _ in cell_groups(cyc, ds) if c not in rig]
            for oc in others:
                g = cyc[(cyc["dataset"] == ds) & (cyc["cell_id"] == oc)]
                lcs = g.loc[g["rest_before_s"] > LONG_REST_RIG_S, "cycle_idx"].tolist()
                w(
                    f"- {oc} (separate rig/schedule): cycles with rest > {LONG_REST_RIG_S:.0e} s: {lcs}.\n"
                )

    # ------------------------------------------------ cross dataset
    w("## Cross-dataset\n")
    w("### Flag prevalence\n")
    rows = []
    for ds in DATASETS:
        d = cyc[cyc["dataset"] == ds]
        row: dict[str, Any] = {"dataset": ds, "cells": d["cell_id"].nunique(), "cycles": len(d)}
        for col in FLAG_COLS:
            row[col.removeprefix("flag_")] = pct(float(d[col].mean()))
        rows.append(row)
    w(md_table(pd.DataFrame(rows)) + "\n")

    w("### Effect of each flag on SOH\n")
    w(
        "Local deviation = SOH minus its centered 11-cycle rolling median. A flag that should be "
        "masked for labels shows a large flagged deviation relative to unflagged cycles.\n"
    )
    w(md_table(fx) + "\n")

    w("### Rule sensitivity summary\n")
    rows = []
    for thr in THRESHOLDS:
        t = eol_tabs[thr]
        for ds in DATASETS:
            s = t[t["dataset"] == ds]
            sp = s["_spread"].dropna()
            rows.append(
                {
                    "dataset": ds,
                    "threshold": f"{thr:.0%}",
                    "cells": len(s),
                    f"cells with spread > {SPREAD_HIGHLIGHT} or mixed censoring": int(
                        s["_hi"].sum()
                    ),
                    "median spread (uncensored cells)": "n/a" if sp.empty else f"{sp.median():.0f}",
                    "max spread": "n/a" if sp.empty else f"{sp.max():.0f}",
                    "cells censored under sustained": int((s["sustained"] == "censored").sum()),
                }
            )
    w(md_table(pd.DataFrame(rows)) + "\n")

    w("### Regeneration vs rest\n")
    w(f"![regeneration vs rest]({figs['regen']})\n")
    cap = "; ".join(
        f"{ds}: rho = {f(s['rho_all'], 2)} (all {int(s['n'])} cycles), "
        f"{f(s['rho_clean'], 2)} ({int(s['n_clean'])} cycles, masked cycles and the cycle after "
        f"each dropped); rebounds (dSOH > +0.05 after rest < 1 h): {int(s['n_rebound'])}, of which "
        f"{int(s['n_rebound_after_mask'])} follow a masked cycle"
        for ds, s in regen_stats.items()
    )
    w(
        "_dSOH vs previous cycle against log10(rest before the cycle); + marks skipped_cv "
        f"cycles. Spearman rho: {cap}._\n"
    )

    w("### Charge-curve evolution\n")
    w(f"![charge curves and ICA]({figs['curves']})\n")
    w(
        "_"
        + "; ".join(
            f"{ds.upper()} {REPRESENTATIVE_CELL[ds]}: {len(v)} curves (cycles {v[0]} to {v[-1]})"
            for ds, v in used.items()
        )
        + ". ICA: charge_ah resampled onto a 5 mV voltage grid over the constant-current "
        "samples, Savitzky-Golay smoothed (window 9, order 3), then differentiated._\n"
    )

    w("### Feature preview for Task A (charge-phase features vs SOH)\n")
    w(
        "Spearman rho between a cycle's feature and its SOH, computed per cell; entries are the "
        "mean over cells with [min, max]. Only features available at charge time of cycle k.\n"
    )
    w(md_table(task_a) + "\n")
    w(
        "Discharge-phase quantities of the same cycle (not allowed as Task A inputs; shown to quantify the leakage):\n"
    )
    w(md_table(forbidden) + "\n")

    # ------------------------------------------------ carry-forward findings
    w("## Carry-forward findings, quantified\n")
    nasa_checks = nasa_curve_checks("nasa") if "nasa" in DATASETS else pd.DataFrame()
    if "nasa" in DATASETS:
        w("**NASA discharge records (finding 2).**\n")
        w(md_table(nasa_checks) + "\n")
        w("**NASA charge records (finding 3).**\n")
        n = cyc[cyc["dataset"] == "nasa"]
        c1 = n[n["cycle_idx"] == 1][["cell_id", "charge_throughput_ah"]]
        w(
            "Cycle-1 charge throughput (Ah): "
            + ", ".join(f"{r.cell_id} {f(r.charge_throughput_ah, 4)}" for r in c1.itertuples())
            + ".\n"
        )
        pc = n[n["flag_partial_charge"]]
        w(
            "Cycles flagged partial_charge (cycle: Ah): "
            + "; ".join(
                f"{cell}: "
                + ", ".join(
                    f"{int(r.cycle_idx)}: {f(r.charge_throughput_ah, 3)}" for r in g.itertuples()
                )
                for cell, g in pc.groupby("cell_id")
            )
            + ".\n"
        )
        w(md_table(first_charge_spike("nasa")) + "\n")
        w("**NASA SOH range and censoring (finding 4).**\n")
        rows = []
        for cell, g in cell_groups(cyc, "nasa"):
            rows.append(
                {
                    "cell": cell,
                    "min SOH": f(g["soh"].min()),
                    "censored at 80 % (sustained)": bool(
                        eol_sustained(g["cycle_idx"].to_numpy(), g["soh"].to_numpy(), 0.8).censored
                    ),
                    "censored at 70 % (sustained)": bool(
                        eol_sustained(g["cycle_idx"].to_numpy(), g["soh"].to_numpy(), 0.7).censored
                    ),
                }
            )
        w(md_table(pd.DataFrame(rows)) + "\n")
    if "calce" in DATASETS:
        w("**CALCE channels and ordering (finding 5).**\n")
        rows = []
        for cell, g in cell_groups(cyc, "calce"):
            rows.append(
                {
                    "cell": cell,
                    "cycles": len(g),
                    "cycle_idx strictly increasing": bool(
                        g["cycle_idx"].is_monotonic_increasing and g["cycle_idx"].is_unique
                    ),
                    "charge_temp_max_c missing": pct(float(g["charge_temp_max_c"].isna().mean())),
                    "ir_ohm available": pct(float(g["ir_ohm"].notna().mean())),
                }
            )
        w(md_table(pd.DataFrame(rows)) + "\n")
        w("**CALCE equipment artifact vs real recovery (finding 6).**\n")
        rows = []
        for cell, g in cell_groups(cyc, "calce"):
            sk = g[g["flag_skipped_cv"]]
            lr = g[g["flag_long_rest"] & ~g["flag_skipped_cv"]]
            rows.append(
                {
                    "cell": cell,
                    "skipped_cv cycles": len(sk),
                    "share": pct(len(sk) / len(g)),
                    "mean dCapacity vs previous cycle at skipped_cv (Ah)": f(sk["d_cap"].mean(), 3),
                    "min / max": f"{f(sk['d_cap'].min(), 3)} / {f(sk['d_cap'].max(), 3)}",
                    "mean dCapacity at long_rest cycles, not skipped (Ah)": f(
                        lr["d_cap"].mean(), 4
                    ),
                    "long_rest cycles": len(lr),
                }
            )
        w(md_table(pd.DataFrame(rows)) + "\n")
        t8 = eol_tabs[0.8]
        t8 = t8[t8["dataset"] == "calce"]
        w(
            "EOL (80 %) by raw first crossing vs 11-cycle rolling median: "
            + "; ".join(
                f"{r.cell} {r.raw} vs {getattr(r, SENSITIVITY_COL)}" for r in t8.itertuples()
            )
            + ".\n"
        )
        w(
            "**CALCE cycled past EOL (finding 7).** Min SOH: "
            + ", ".join(f"{c} {f(g['soh'].min(), 2)}" for c, g in cell_groups(cyc, "calce"))
            + ".\n"
        )
    w("**Feature availability (finding 8)** is quantified by the discharge-feature table above.\n")

    # ------------------------------------------------ recommendations
    w("## Recommendations for ADR-0005\n")
    w(recommendation_text(cyc, eol_tabs, fx))
    w("")

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"wrote {OUT_MD}")


def recommendation_text(
    cyc: pd.DataFrame, eol_tabs: dict[float, pd.DataFrame], fx: pd.DataFrame
) -> str:
    """Evidence block; every number is computed, wording is fixed."""
    out: list[str] = []
    for thr in THRESHOLDS:
        t = eol_tabs[thr]
        for ds in DATASETS:
            s = t[t["dataset"] == ds]
            both = s[(s["sustained"] != "censored") & (s["raw"] != "censored")]
            raw_gap = (both["sustained"].astype(int) - both["raw"].astype(int)).abs()
            rm = s[(s["sustained"] != "censored") & (s["rolling_median"] != "censored")]
            rm_gap = (rm["sustained"].astype(int) - rm["rolling_median"].astype(int)).abs()
            same_mask = int((s["masked"] == s["sustained"]).sum())
            out.append(
                f"- {ds} @ {thr:.0%}: rule choice moves EOL by > {SPREAD_HIGHLIGHT} cycles or "
                f"flips censoring in {int(s['_hi'].sum())}/{len(s)} cells; |sustained - raw| "
                f"max {int(raw_gap.max()) if len(raw_gap) else 'n/a'} cycles; |sustained - "
                f"rolling_median(5)| max {int(rm_gap.max()) if len(rm_gap) else 'n/a'}; masked "
                f"equals sustained in {same_mask}/{len(s)} cells."
            )
    sk = fx[(fx["flag"] == "skipped_cv") & (fx["dataset"] == "calce")].iloc[0]
    lr = fx[(fx["flag"] == "long_rest") & (fx["dataset"] == "calce")].iloc[0]
    out.append(
        f"- CALCE skipped_cv cycles sit {sk['median abs dSOH (flagged)']} SOH from their local "
        f"median versus {sk['median abs dSOH (unflagged)']} for unflagged cycles; CALCE long_rest "
        f"cycles only {lr['median abs dSOH (flagged)']} (see the flag-effect table)."
    )
    out.append(
        "\n**Recommendation (lead decides).** Label EOL with `masked` + `sustained` (n=5), "
        "masking skipped_cv and partial_charge, at the 80 % threshold as primary and 70 % as a "
        "secondary (censoring-heavy on NASA). Raw first-crossing is not defensible on CALCE "
        "(numbers above). Keep long_rest and capacity_jump as inputs/diagnostics only (they "
        "describe real regeneration, not corrupt capacity values); mask only the artifact flags "
        "in labels.\n\n"
        "**Strongest counter-argument.** Where the counts above show `masked` equal to plain "
        "`sustained`, the mask adds a hindsight-derived dependency without changing any label; "
        "`sustained` alone (or the centered median) is simpler, and the mask only pays off if "
        "artifacts cluster at the crossing."
    )
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    main()
