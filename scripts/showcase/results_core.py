# ruff: noqa: E501, RUF001, RUF005
"""Build web/showcase/data/results_core.json: headline tiles, rank/horizon/fan/history/per-cell data.

All SOH values in the JSON are %SOH (fractions x 100); horizons and cycle indices are cycles.
MLflow is read-only here.
"""

from __future__ import annotations

import json
from pathlib import Path

import mlflow
import numpy as np
import pandas as pd

from battery_rul.data.io import read_tables

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "web/showcase/data/results_core.json"
mlflow.set_tracking_uri(f"sqlite:///{ROOT / 'mlflow.db'}")

FAN_MODELS = ["itransformer", "lgbm", "itransformer_sc", "persistence"]
BAND_MODELS = ["itransformer", "lgbm"]
HIST_MODELS = ["itransformer", "lgbm", "itransformer_sc", "nlinear", "persistence"]
CELL_MODELS = ["itransformer", "lgbm", "itransformer_sc", "persistence"]
LOAD_MODELS = sorted(set(FAN_MODELS + HIST_MODELS + CELL_MODELS))
SEEDS = [0, 1, 2, 3, 4]
PANELS = [
    ("calce", "loco", "CALCE"),
    ("nasa", "loco", "NASA"),
    ("toyota", "test1", "Toyota test 1"),
    ("toyota", "test2", "Toyota test 2"),
]
BINS = [
    (1, 20, "1–20"),
    (21, 40, "21–40"),
    (41, 60, "41–60"),
    (61, 80, "61–80"),
    (81, 10**9, "81+"),
]


def r(x: float, d: int = 2) -> float:
    return round(float(x), d)


# ---------------------------------------------------------------- MLflow access
_runs = mlflow.search_runs(experiment_names=["benchmark"], max_results=100000)
_runs = _runs[(_runs["status"] == "FINISHED") & (_runs["params.task"] == "forecast")]
_cache: dict[tuple, pd.DataFrame] = {}


def run_id(ds: str, model: str, seed: int, fold: str) -> str:
    q = _runs[
        (_runs["params.dataset"] == ds)
        & (_runs["params.model"] == model)
        & (_runs["params.seed"] == str(seed))
        & (_runs["params.fold"] == fold)
    ]
    assert len(q) == 1, (ds, model, seed, fold, len(q))
    return str(q.run_id.iloc[0])


def preds(ds: str, model: str, seed: int, fold: str) -> pd.DataFrame:
    key = (ds, model, seed, fold)
    if key not in _cache:
        p = mlflow.artifacts.download_artifacts(
            run_id=run_id(ds, model, seed, fold), artifact_path="predictions.parquet"
        )
        _cache[key] = pd.read_parquet(p)
    return _cache[key]


def calibrated(ds: str, model: str, seed: int, fold: str) -> pd.DataFrame:
    p = mlflow.artifacts.download_artifacts(
        run_id=run_id(ds, model, seed, fold), artifact_path="calibrated_predictions.parquet"
    )
    return pd.read_parquet(p)


def folds(ds: str) -> list[str]:
    q = _runs[_runs["params.dataset"] == ds]["params.fold"].unique()
    return sorted(q)


def horizons_of(df: pd.DataFrame) -> list[int]:
    return sorted(int(c[len("point_h") :]) for c in df.columns if c.startswith("point_h"))


def all_preds(ds: str, model: str, seed: int) -> pd.DataFrame:
    """Predictions of every held-out cell of ds (one run per cell on NASA/CALCE)."""
    return pd.concat([preds(ds, model, seed, f) for f in folds(ds)], ignore_index=True)


# ---------------------------------------------------------------- tables
bench = pd.read_csv(ROOT / "reports/tables/benchmark.csv")
ranks = pd.read_csv(ROOT / "reports/tables/benchmark_ranks.csv").sort_values("mean_rank")
calib = pd.read_csv(ROOT / "reports/tables/benchmark_calibration.csv")
cycles = {
    ds: read_tables(ds, ROOT / "data/processed", curves=False).cycles
    for ds in ["nasa", "calce", "toyota"]
}


def bench_val(ds: str, split: str, model: str, h: int) -> float:
    q = bench[
        (bench.dataset == ds)
        & (bench.split == split)
        & (bench.task == "forecast")
        & (bench.policy == "all")
        & (bench.kind == "overall")
        & (bench.model == model)
        & (bench.metric == f"rmse_h{h}")
    ]
    return float(q["mean"].iloc[0]) if len(q) else float("inf")


def horizon_block() -> list[dict]:
    out = []
    for ds, split, title in PANELS:
        q = bench[
            (bench.dataset == ds)
            & (bench.split == split)
            & (bench.task == "forecast")
            & (bench.policy == "all")
            & (bench.kind == "overall")
            & bench.metric.str.startswith("rmse_h")
        ].copy()
        q["h"] = q.metric.str[len("rmse_h") :].astype(int)
        hs = sorted(q.h.unique())
        models = {}
        for m, g in q.groupby("model"):
            g = g.set_index("h").reindex(hs)
            models[m] = {
                k: [None if pd.isna(v) else r(v, 3) for v in g[c]]
                for k, c in [("mean", "mean"), ("lo", "ci_lo"), ("hi", "ci_hi")]
            }
        out.append(
            {
                "key": f"{ds}-{split}",
                "title": title,
                "horizons": [int(h) for h in hs],
                "models": models,
            }
        )
    return out


# ---------------------------------------------------------------- fan chart
def fan_block() -> tuple[list[dict], list[str]]:
    notes = []
    panels = []

    # choose cells: median iTransformer h50 abs error at the frac:0.5 origin
    def frac_rows(df: pd.DataFrame) -> pd.DataFrame:
        return df[(df.origin_policy == "start_points") & (df.start_kind == "frac:0.5")]

    specs = [("nasa", "nasa", "B0018", "NASA B0018")]
    cand = {}
    for ds, split in [("calce", "loco"), ("toyota", "test1"), ("toyota", "test2")]:
        d = frac_rows(all_preds(ds, "itransformer", 0))
        d = d[(d.split == split) | (ds != "toyota")] if ds == "toyota" else d
        d = d[d.y_mask_h50.astype(bool)]
        err = (d.point_h50 - d.y_h50).abs() * 100
        err.index = d.cell_id
        med = err.median()
        pick = (err - med).abs().sort_values(kind="stable").index[0]
        cand[(ds, split)] = (pick, float(err[pick]), float(med), len(err))
    specs += [
        ("calce", "loco", cand[("calce", "loco")][0], "CALCE"),
        ("toyota", "test1", cand[("toyota", "test1")][0], "Toyota test 1"),
        ("toyota", "test2", cand[("toyota", "test2")][0], "Toyota test 2"),
    ]
    for ds, split, cell, name in [("nasa", "loco", "B0018", "NASA")] + specs[1:]:
        fold = "official" if ds == "toyota" else cell
        tr = cycles[ds][cycles[ds].cell_id == cell].sort_values("cycle_idx")
        entry = {
            "cell": cell,
            "name": name,
            "traj_x": [int(c) for c in tr.cycle_idx],
            "traj_y": [r(v * 100, 3) for v in tr.soh],
            "models": {},
        }
        soh_at = dict(zip(tr.cycle_idx.astype(int), tr.soh * 100, strict=True))
        itr_err = None
        for m in FAN_MODELS:
            df = frac_rows(preds(ds, m, 0, fold))
            df = df[(df.cell_id == cell) & ((df.split == split) | (ds != "toyota"))]
            assert len(df) == 1, (ds, cell, m, len(df))
            row = df.iloc[0]
            o = int(row.origin_cycle)
            hs = horizons_of(df)
            cal = None
            if m in BAND_MODELS:
                cd = calibrated(ds, m, 0, fold)
                cd = cd[
                    (cd.cell_id == cell)
                    & (cd.origin_cycle == o)
                    & (cd.start_kind == "frac:0.5")
                    & (cd.origin_policy == "start_points")
                ]
                if ds == "toyota":
                    cd = cd[cd.split == split]
                cal = cd.set_index("horizon")
            pts = []
            for h in hs:
                if not bool(row[f"y_mask_h{h}"]):
                    continue
                p = {
                    "h": h,
                    "x": o + h,
                    "point": r(row[f"point_h{h}"] * 100, 3),
                    "meas": r(row[f"y_h{h}"] * 100, 3),
                }
                if cal is not None and h in cal.index:
                    p["lo"] = r(cal.loc[h, "lo_cal"] * 100, 3)
                    p["hi"] = r(cal.loc[h, "hi_cal"] * 100, 3)
                pts.append(p)
            entry["origin"] = o
            entry["origin_soh"] = r(soh_at[o], 3)
            entry["max_h"] = max(hs)
            entry["models"][m] = pts
            if m == "itransformer":
                p50 = next(p for p in pts if p["h"] == 50)
                itr_err = abs(p50["point"] - p50["meas"])
        entry["itr_h50_err"] = r(itr_err, 2)
        entry["eol_cycle"] = None if pd.isna(row.eol_cycle) else int(row.eol_cycle)
        if ds == "toyota" or ds == "calce":
            c = cand[(ds, split)]
            entry["note"] = "median cell"
            entry["median_err"] = r(c[2], 2)
            entry["n_cells"] = c[3]
        else:
            entry["note"] = "rig-independent cell"
        notes.append(
            f"{name} {cell}: iTransformer h50 error {itr_err:.2f} %SOH at origin {entry['origin']} ({entry['note']})"
        )
        panels.append(entry)
    return panels, notes


# ---------------------------------------------------------------- history & per-cell
def history_block() -> dict:
    res = {m: [] for m in HIST_MODELS}
    n_per_bin = None
    for m in HIST_MODELS:
        d = pd.concat([all_preds("nasa", m, s) for s in SEEDS], ignore_index=True)
        d = d[(d.origin_policy == "all") & d.y_mask_h50.astype(bool)]
        e2 = ((d.point_h50 - d.y_h50) * 100) ** 2
        vals, ns = [], []
        for lo, hi, _ in BINS:
            sel = (d.origin_cycle >= lo) & (d.origin_cycle <= hi)
            vals.append(r(np.sqrt(e2[sel].mean()), 2))
            ns.append(int(sel.sum() / len(SEEDS)))
        res[m] = vals
        n_per_bin = ns
    return {"bins": [b[2] for b in BINS], "n_per_bin": n_per_bin, "models": res}


def cells_block() -> dict:
    out = {}
    for ds in ["nasa", "calce"]:
        cells = folds(ds)
        models = {}
        for m in CELL_MODELS:
            per_seed = []
            for s in SEEDS:
                d = all_preds(ds, m, s)
                d = d[(d.origin_policy == "all") & d.y_mask_h50.astype(bool)]
                e2 = ((d.point_h50 - d.y_h50) * 100) ** 2
                g = e2.groupby(d.cell_id).mean() ** 0.5
                per_seed.append([r(g[c], 3) for c in cells])
            arr = np.array(per_seed)
            models[m] = {"seeds": arr.T.tolist(), "mean": [r(v, 3) for v in arr.mean(0)]}
        out[ds] = {"cells": cells, "models": models}
    return out


# ---------------------------------------------------------------- hero + note
NAMES = {
    "itransformer": "iTransformer", "itransformer_sc": "iTransformer SC", "lgbm": "LightGBM",
    "persistence": "persistence", "nlinear": "NLinear", "patchtst": "PatchTST",
}  # fmt: skip


def hero_and_note() -> tuple[list[dict], str]:
    n_cells = {ds: int(cycles[ds].cell_id.nunique()) for ds in cycles}
    n_runs = 0
    for e in ["benchmark", "benchmark_local"]:
        x = mlflow.search_runs(experiment_names=[e], max_results=100000)
        unit = x["tags.unit_key"].notna() if "tags.unit_key" in x else True
        n_runs += int(((x["status"] == "FINISHED") & unit).sum())  # unit runs, not parents
    allruns = pd.concat(
        [
            mlflow.search_runs(experiment_names=[e], max_results=100000)
            for e in ["benchmark", "benchmark_local"]
        ]
    )
    n_models = allruns["params.model"].nunique()
    best = ranks.iloc[0]
    t1_best = min(
        (m for m in bench.model.unique() if m != "persistence"),
        key=lambda m: bench_val("toyota", "test1", m, 50),
    )
    cal = calib[
        (calib.task == "forecast")
        & (calib.horizon == 50)
        & (calib.policy == "all")
        & (calib.kind == "overall")
    ]
    cal = cal[cal.raw_picp > 0]  # quantile models only (as in ADR-0011)
    ok = int(cal.cal_picp.between(0.85, 0.95).sum())
    hero = [
        {"k": "Cells", "v": str(sum(n_cells.values())),
         "s": f"NASA {n_cells['nasa']} · CALCE {n_cells['calce']} · Toyota {n_cells['toyota']}"},
        {"k": "Benchmark runs", "v": f"{n_runs:,}".replace(",", " "),
         "s": f"{n_models} model configurations × 3 tasks × test cells × 5 seeds"},
        {"k": "Best mean rank", "v": f"{NAMES.get(best.model, best.model)} {best.mean_rank:.2f}",
         "s": f"over {int(best.n_conditions)} conditions"},
        {"k": "Toyota 50-cycle forecast", "v": f"{bench_val('toyota', 'test1', t1_best, 50):.2f} % SOH",
         "s": f"{NAMES.get(t1_best, t1_best)}, test 1, vs {bench_val('toyota', 'test1', 'persistence', 50):.2f} % for persistence"},
        {"k": "Calibrated 90 % intervals", "v": f"{ok} / {len(cal)}",
         "s": "50-cycle conditions within 90 ± 5 %"},
    ]  # fmt: skip
    nb = [m for m in bench.model.unique()]

    def best_at(ds: str, split: str, h: int) -> tuple[str, float]:
        m = min((m for m in nb if m != "persistence"), key=lambda m: bench_val(ds, split, m, h))
        return m, bench_val(ds, split, m, h)

    def nm(m: str) -> str:
        return NAMES.get(m, m)

    bn, bv = best_at("nasa", "loco", 1)
    bc, bcv = best_at("calce", "loco", 1)
    note1 = (
        f"At h = 1 there is almost nothing to beat: on NASA persistence scores "
        f"{bench_val('nasa', 'loco', 'persistence', 1):.2f} % SOH against {bv:.2f} % for the best model ({nm(bn)}), "
        f"and on CALCE the floor is higher ({bench_val('calce', 'loco', 'persistence', 1):.2f} % for persistence, {bcv:.2f} % for {nm(bc)}). "
        "That floor is cycle-to-cycle noise (capacity regeneration on NASA, dips from the CALCE test artefact) that no model can predict."
    )
    h50 = []
    for ds, split, lab in PANELS:
        m, v = best_at(ds, split, 50)
        h50.append(f"{lab} {nm(m)} ({v:.2f} %)")
    note2 = "At h = 50 the best model per dataset is " + ", ".join(h50) + "."
    note3 = (
        f"The NASA h = 100 column shows iTransformer at {bench_val('nasa', 'loco', 'itransformer', 100):.2f} % versus "
        f"{bench_val('nasa', 'loco', 'lgbm', 100):.2f} % for LightGBM; the history-length chart below shows why."
    )
    return hero, f"{note1} {note2} {note3}"


def main() -> None:
    horizon = horizon_block()
    fan, fan_notes = fan_block()
    hist = history_block()
    cells = cells_block()
    hero, note = hero_and_note()
    rk = [
        {
            "model": row.model,
            "rank": r(row.mean_rank, 3),
            "n": int(row.n_conditions),
            "missing": int(row.n_missing),
        }
        for row in ranks.itertuples()
    ]
    data = {
        "hero": hero,
        "horizon_note": note,
        "rank": rk,
        "horizon": horizon,
        "fan": fan,
        "history": hist,
        "cells": cells,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, separators=(",", ":")))
    print(json.dumps(hero, indent=1, ensure_ascii=False))
    print(note)
    print("\n".join(fan_notes))
    print(pd.DataFrame(hist["models"], index=hist["bins"]).T.to_string(), hist["n_per_bin"])
    print(f"{OUT} {OUT.stat().st_size / 1e6:.2f} MB")


if __name__ == "__main__":
    main()
