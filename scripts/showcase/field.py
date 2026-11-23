"""Showcase part `field`: the field setting (no SOH/capacity history), ADR-0018..0022.

Writes web/showcase/data/field.json from CSVs in reports/tables:
* benchmark.csv: lab best model per condition (with SOH history);
* field_final.csv: field models and age-only, 5 seeds;
* field_screen_paired.csv, field_lookback_paired_{soh,forecast}.csv, field_regen_events.csv,
  field_final_paired.csv: the iTransformer claim tests (ADR-0021);
* field_final_intervals.csv: CQR coverage / width / useful share.
The signal tables are encoded as constants from reports/eda_field.md (sections 1 and 3).

Usage: uv run python scripts/showcase/field.py [--tables DIR]
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]

CONDS = [
    ("nasa", "loco", "NASA"),
    ("calce", "loco", "CALCE"),
    ("toyota", "test1", "Toyota test 1"),
    ("toyota", "test2", "Toyota test 2"),
]
TASKS = [
    ("soh", "rmse", "F-A SOH estimation (% SOH)"),
    ("forecast", "rmse_h50", "F-B forecast, h = 50 (% SOH)"),
    ("rul", "rul_mae", "F-C RUL (cycles MAE)"),
]
MODELS = ["age_only", "itransformer", "transformer", "lstm", "lgbm", "elasticnet", "patchtst"]
LEARNED = [m for m in MODELS if m != "age_only"]

# reports/eda_field.md section 1 (signal availability), section 3 (Spearman rho with SOH,
# per-cell median)
SIGNALS = [
    ["Cycle count", "yes", "yes", "yes", "allowed (owner decision)"],
    [
        "CV time (+ CV-skip flag)",
        "yes",
        "yes",
        "yes",
        "Toyota CV is timer-bounded and switches regime with age",
    ],
    ["Internal resistance", "pulse R at charge start", "Arbin IR", "summary IR", ""],
    ["Rest before the cycle", "yes", "yes", "not logged", "drives regeneration"],
    [
        "Relaxation voltage",
        "OCV at charge start",
        "90 s rest between CC and CV",
        "80 % SOC rest, fixed 8 s read",
        "Toyota test 2 rests only ~10 s",
    ],
    [
        "Fixed-window charge dQ, dt, 15 Q(V) points, ICA peak",
        "3.85-4.15 V, 94.8 % of cycles",
        "3.85-4.15 V, 87.2 %",
        "3.50-3.58 V, 92 %",
        "works from a partial charge",
    ],
    ["Charge temperature", "yes", "no", "yes", ""],
    [
        "Forbidden (leakage-tested)",
        "capacity, SOH, throughput from empty, total/CC charge time, all discharge quantities",
        "",
        "",
        "",
    ],
]
SPEARMAN = [
    {"feature": "Window dQ", "nasa": 0.99, "calce": 0.98, "toyota": -0.69},
    {"feature": "ICA peak height", "nasa": 0.98, "calce": 0.97, "toyota": -0.49},
    {"feature": "Relaxation voltage", "nasa": -0.93, "calce": 0.95, "toyota": -1.00},
    {"feature": "CV time", "nasa": -0.88, "calce": -0.76, "toyota": 0.24},
    {"feature": "Pulse / IR resistance", "nasa": -0.32, "calce": None, "toyota": None},
]


def fam(model: str) -> str:
    return re.sub(r"\[.*\]", "", model)


def num(v) -> float | None:
    return None if pd.isna(v) else float(v)


def headline(df: pd.DataFrame) -> pd.DataFrame:
    """policy all, kind overall, the task's headline metric; one row per family/condition."""
    df = df[(df.policy == "all") & (df.kind == "overall")].copy()
    keep = pd.Series(False, index=df.index)
    for t, m, _ in TASKS:
        keep |= (df.task == t) & (df.metric == m)
    df = df[keep]
    df["family"] = df.model.map(fam)
    return df.sort_values("mean").drop_duplicates(["dataset", "split", "task", "family"])


def gap(bench: pd.DataFrame, field: pd.DataFrame) -> list[dict]:
    out = []
    for t, _, tl in TASKS:
        for ds, sp, cl in CONDS:
            b, f = (d[(d.dataset == ds) & (d.split == sp) & (d.task == t)] for d in (bench, field))
            fl = f[f.family != "age_only"]
            if b.empty or fl.empty:
                continue
            bb, ff, ao = b.iloc[0], fl.iloc[0], f[f.family == "age_only"]
            out.append(
                {
                    "task": t, "task_label": tl, "cond": cl,
                    "lab_model": bb.family, "lab": float(bb["mean"]),
                    "field_model": ff.family, "field": float(ff["mean"]),
                    "age_only": num(ao["mean"].iloc[0]) if len(ao) else None,
                }
            )  # fmt: skip
    return out


def heat(field: pd.DataFrame) -> list[dict]:
    rows = []
    for t, _, tl in TASKS:
        for ds, sp, cl in CONDS:
            g = field[(field.dataset == ds) & (field.split == sp) & (field.task == t)]
            for _, r in g.iterrows():
                if r.family in MODELS:
                    rows.append(
                        {
                            "task": t, "task_label": tl, "cond": cl, "model": r.family,
                            "mean": float(r["mean"]), "lo": num(r.ci_lo), "hi": num(r.ci_hi),
                            "lookback": (re.search(r"lookback=(\d+)", r.model) or [None, None])[1],
                        }
                    )  # fmt: skip
    return rows


def mean_ranks(field: pd.DataFrame) -> list[dict]:
    """Mean rank among learned models over the 12 task x condition cells (ADR-0021)."""
    f = field[field.family.isin(LEARNED)].copy()
    f["rank"] = f.groupby(["dataset", "split", "task"])["mean"].rank()
    r = f.groupby("family")["rank"].agg(["mean", "count"]).sort_values("mean")
    return [{"model": m, "rank": float(v["mean"]), "n": int(v["count"])} for m, v in r.iterrows()]


def claims(T: Path) -> dict:
    cond_label = {(d, s): c for d, s, c in CONDS}
    sp = pd.read_csv(T / "field_screen_paired.csv")
    sp = sp[sp.reference.str.contains("field_screen_field:")]
    variates = [
        {
            "model": fam(r.candidate.split(":")[1]), "cond": cond_label[(r.dataset, r.split)],
            "delta": r.delta, "lo": r.ci_lo, "hi": r.ci_hi, "k": r.k_cells,
        }
        for r in sp.itertuples()
    ]  # fmt: skip
    lookback = []
    for task in ("soh", "forecast"):
        lb = pd.read_csv(T / f"field_lookback_paired_{task}.csv")
        for r in lb.itertuples():
            lookback.append(
                {
                    "task": task, "model": fam(r.candidate.split(":")[1]),
                    "cond": cond_label[(r.dataset, r.split)], "delta": r.delta,
                    "lo": r.ci_lo, "hi": r.ci_hi, "k": r.k_cells,
                }
            )  # fmt: skip
    ev = pd.read_csv(T / "field_regen_events.csv")
    ev = ev[(ev.h == 1) & (ev.targets == "regen")]
    regen = [
        {
            "dataset": r.dataset.upper(),
            "arm": r.arm, "model": r.arm.split("+")[0], "kind": r.arm.split("+")[1],
            "reduction": r.reduction, "k": r.k_cells, "n": int(r.n_targets),
            "rmse_cand": r.rmse_cand, "rmse_base": r.rmse_base,
        }
        for r in ev.itertuples()
    ]  # fmt: skip
    fp = pd.read_csv(T / "field_final_paired.csv")
    fp = fp[fp.candidate.str.contains("itransformer") & fp.reference.str.contains("patchtst")]
    mixing = [
        {
            "task": r.task, "cond": cond_label[(r.dataset, r.split)], "metric": r.metric,
            "delta": r.delta, "lo": r.ci_lo, "hi": r.ci_hi, "k": r.k_cells,
            "p_holm": num(r.p_holm),
        }
        for r in fp.itertuples()
    ]  # fmt: skip
    return {"variates": variates, "lookback": lookback, "regen": regen, "mixing": mixing}


def intervals(T: Path) -> dict:
    iv = pd.read_csv(T / "field_final_intervals.csv")
    iv = iv[iv.method == "cqr"]
    out = {}
    for task, h in (("forecast", 50), ("rul", 0)):
        g = iv[(iv.task == task) & (iv.horizon == h)]
        a = (
            g.groupby(["dataset", "split", "model"])
            .agg(
                picp=("picp", "mean"),
                width=("width", "mean"),
                useful=("useful_share", "mean"),
                seeds=("seed", "nunique"),
            )
            .reset_index()
        )
        rows = []
        for r in a.itertuples():
            cond = {
                ("nasa", "test"): "NASA",
                ("calce", "test"): "CALCE",
                ("toyota", "test1"): "Toyota test 1",
                ("toyota", "test2"): "Toyota test 2",
            }[(r.dataset, r.split)]
            rows.append(
                {
                    "cond": cond,
                    "model": r.model,
                    "picp": r.picp,
                    "width": r.width,
                    "useful": num(r.useful),
                    "seeds": int(r.seeds),
                }
            )
        out[task] = rows
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tables", type=Path, default=ROOT / "reports" / "tables")
    T = ap.parse_args().tables
    field = headline(pd.read_csv(T / "field_final.csv"))
    bench = headline(pd.read_csv(T / "benchmark.csv"))
    out = {
        "signals": SIGNALS, "spearman": SPEARMAN,
        "conds": [c for _, _, c in CONDS], "tasks": [{"id": t, "label": tl} for t, _, tl in TASKS],
        "gap": gap(bench, field), "heat": heat(field), "ranks": mean_ranks(field),
        **claims(T), "intervals": intervals(T),
    }  # fmt: skip
    dest = ROOT / "web" / "showcase" / "data" / "field.json"
    dest.write_text(json.dumps(out, default=float))
    print(f"wrote {dest} ({dest.stat().st_size / 1e3:.0f} kB)")


if __name__ == "__main__":
    main()
