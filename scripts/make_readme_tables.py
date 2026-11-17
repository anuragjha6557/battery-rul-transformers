"""Generate the README results block from the CSV tables in ``reports/tables/``.

Writes the block between ``<!-- RESULTS:START -->`` / ``<!-- RESULTS:END -->`` in
README.md (markers appended if absent) and to ``reports/results.md``. Idempotent.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "reports" / "tables"
FIG_DIR = ROOT / "reports" / "figures" / "results"
START, END = "<!-- RESULTS:START -->", "<!-- RESULTS:END -->"

NAMES = {
    "itransformer": "iTransformer (MC)",
    "itransformer_sc": "iTransformer (SC)",
    "lgbm": "LightGBM",
    "elasticnet": "ElasticNet",
    "patchtst": "PatchTST",
    "nlinear": "NLinear",
    "dlinear": "DLinear",
    "rlinear": "RLinear",
    "lstm": "LSTM",
    "gru": "GRU",
    "transformer": "Transformer",
    "persistence": "Persistence",
    "last_slope": "Last slope",
    "prev_soh": "Previous SOH",
}
COLS = [
    ("calce", "loco", "CALCE"),
    ("nasa", "loco", "NASA"),
    ("toyota", "test1", "Toyota test1"),
    ("toyota", "test2", "Toyota test2"),
]
NAIVE = ("persistence", "last_slope", "prev_soh")


def nm(m: str) -> str:
    return NAMES.get(m, m)


def md_table(header: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out)


def read(name: str) -> pd.DataFrame | None:
    p = TABLES / name
    return pd.read_csv(p) if p.exists() else None


def fig(name: str) -> str:
    if (FIG_DIR / f"{name}.png").exists():
        return f"![](reports/figures/results/{name}.png)"
    return ""


def join(parts: list[str]) -> str:
    return "\n\n".join(p for p in parts if p)


def ranks_section(rk: pd.DataFrame) -> str:
    rk = rk.sort_values("mean_rank")
    rows = [
        [str(i + 1), nm(r.model), f"{r.mean_rank:.3f}", str(int(r.n_conditions))]
        for i, r in enumerate(rk.itertuples())
    ]
    return join(
        [
            "### Mean rank",
            md_table(["#", "Model", "Mean rank", "Conditions"], rows),
            "Lower is better; rank is averaged over all dataset x task x metric conditions.",
            fig("mean_rank"),
        ]
    )


def headline_table(
    bm: pd.DataFrame,
    task: str,
    metric: str,
    policy: str,
    digits: int,
    title: str,
    unit: str,
) -> str:
    d = bm[
        (bm.task == task) & (bm.metric == metric) & (bm.policy == policy) & (bm.kind == "overall")
    ]
    models = [m for m in NAMES if m in set(d.model)]
    subs: dict[tuple[str, str], pd.DataFrame] = {}
    for ds, sp, _ in COLS:
        subs[(ds, sp)] = d[(d.dataset == ds) & (d.split == sp)].set_index("model")
    rows = []
    for m in models:
        row = [nm(m)]
        for ds, sp, _ in COLS:
            sub = subs[(ds, sp)]
            if m not in sub.index:
                row.append("-")
                continue
            r = sub.loc[m]
            s = f"{r['mean']:.{digits}f} [{r.ci_lo:.{digits}f}, {r.ci_hi:.{digits}f}]"
            if r["mean"] == sub["mean"].min():
                s = f"**{s}**"
            row.append(s)
        rows.append(row)
    return join(
        [
            f"#### {title}",
            md_table(["Model"] + [c[2] for c in COLS], rows),
            f"Unit: {unit}. Cell = mean [95 % CI]; best per column in bold.",
        ]
    )


def naive_section(bm: pd.DataFrame) -> str:
    d = bm[
        (bm.task == "forecast")
        & (bm.metric == "rmse_h50")
        & (bm.policy == "start_points")
        & (bm.kind == "overall")
    ]
    rows = []
    for ds, sp, label in COLS:
        sub = d[(d.dataset == ds) & (d.split == sp)].set_index("model")
        if "persistence" not in sub.index:
            continue
        learned = sub.drop(index=[m for m in NAIVE if m in sub.index])
        b = learned["mean"].idxmin()
        bv, pv = sub.loc[b, "mean"], sub.loc["persistence", "mean"]
        rows.append([label, nm(b), f"{bv:.2f}", f"{pv:.2f}", f"{(1 - bv / pv) * 100:.0f} %"])
    header = [
        "Dataset / split",
        "Best learned model",
        "RMSE h50",
        "Persistence RMSE h50",
        "Reduction",
    ]
    return join(
        [
            "### Naive-baseline check",
            md_table(header, rows),
            "Forecast RMSE at horizon 50 in %SOH, start-point origins only.",
        ]
    )


def calibration_section(cal: pd.DataFrame, ens: pd.DataFrame | None) -> str:
    models = ["itransformer", "itransformer_sc", "lgbm", "patchtst", "lstm"]
    c = cal[
        (cal.horizon == 50)
        & (cal.policy == "all")
        & (cal.kind == "overall")
        & (cal.task == "forecast")
    ]
    e = None
    if ens is not None:
        e = ens[
            (ens.horizon == 50)
            & (ens.policy == "all")
            & (ens.kind == "overall")
            & (ens.arm == "ens_cal")
            & (ens.task == "forecast")
        ]
    rows = []
    for ds, sp, label in COLS:
        for m in models:
            r = c[(c.dataset == ds) & (c.split == sp) & (c.model == m)]
            if r.empty:
                continue
            r = r.iloc[0]
            ev = "-"
            if e is not None:
                x = e[(e.dataset == ds) & (e.split == sp) & (e.model == m)]
                if len(x):
                    ev = f"{x.iloc[0].picp:.3f}"
            rows.append([label, nm(m), f"{r.raw_picp:.3f}", f"{r.cal_picp:.3f}", ev])
    header = ["Dataset / split", "Model", "Raw PICP", "CQR PICP", "Ensemble + CQR PICP"]
    return join(
        [
            "### Calibration",
            md_table(header, rows),
            "Forecast horizon 50, all origins; nominal coverage target 0.90.",
            fig("calibration_h50"),
        ]
    )


def clean_label(cand: str, ref: str) -> tuple[str, str]:
    c, r = cand.split(":", 1)[-1], ref.split(":", 1)[-1]
    if c == r:
        return f"{c} (ablation)", f"{r} (benchmark)"
    return c, r


def ablation_section() -> str:
    groups = [
        ("Norm / loss", "abl_norm_loss_paired.csv"),
        ("Curve features", "abl_curve_paired_soh.csv"),
        ("Curve features", "abl_curve_paired_forecast.csv"),
        ("Transfer", "transfer_paired_all.csv"),
        ("Transfer (RUL)", "transfer_rul_paired_all.csv"),
        ("Transfer (RUL)", "transfer_rul_paired.csv"),
        ("Transfer (RUL)", "transfer_rul_paired_start_points.csv"),
    ]
    rows = []
    for grp, f in groups:
        d = read(f)
        if d is None:
            continue
        if "rul" in f:
            d = d[d.metric == "rul_mae"]
        else:
            d = d[d.metric.isin(["rmse_h50", "rmse"]) & (d.policy == "all")]
        for r in d.itertuples():
            c, ref = clean_label(r.candidate, r.reference)
            dg = 0 if r.metric == "rul_mae" else 2
            ds = r.dataset if r.split == "loco" else f"{r.dataset} {r.split}"
            delta = f"{r.delta:+.{dg}f} [{r.ci_lo:+.{dg}f}, {r.ci_hi:+.{dg}f}]"
            rows.append([grp, f"{c} vs {ref}", ds, r.metric, delta, str(r.k_cells)])
    header = [
        "Study",
        "Candidate vs reference",
        "Dataset",
        "Metric",
        "Delta [95 % CI]",
        "Cells better",
    ]
    return join(
        [
            "### Ablations",
            md_table(header, rows),
            "Delta = candidate minus reference (negative = candidate better); %SOH for "
            "rmse metrics, cycles for rul_mae. Cells better = k of n cells where the "
            "candidate wins.",
        ]
    )


def build() -> str:
    bm = pd.read_csv(TABLES / "benchmark.csv")
    cal = pd.read_csv(TABLES / "benchmark_calibration.csv")
    parts = [
        "## Results",
        ranks_section(pd.read_csv(TABLES / "benchmark_ranks.csv")),
        "### Headline results",
        headline_table(bm, "soh", "rmse", "all", 2, "SOH estimation (RMSE)", "%SOH"),
        headline_table(
            bm, "forecast", "rmse_h50", "all", 2, "Capacity forecast, horizon 50 (RMSE)", "%SOH"
        ),
        fig("forecast_h50"),
        fig("forecast_example"),
        headline_table(
            bm,
            "rul",
            "rul_mae",
            "start_points",
            0,
            "RUL prediction (MAE, start-point origins)",
            "cycles",
        ),
        naive_section(bm),
        calibration_section(cal, read("benchmark_ensemble_calibration.csv")),
        ablation_section(),
        "Generated by `scripts/make_readme_tables.py` from MLflow-derived tables in "
        "`reports/tables/`; every number maps to the `run_ids` column there.",
    ]
    return join(parts) + "\n"


def main() -> None:
    block = build()
    (ROOT / "reports" / "results.md").write_text(block)
    readme = ROOT / "README.md"
    text = readme.read_text()
    wrapped = f"{START}\n{block}{END}"
    if START in text and END in text:
        pre, rest = text.split(START, 1)
        _, post = rest.split(END, 1)
        text = pre + wrapped + post
    else:
        text = text.rstrip("\n") + "\n\n" + wrapped + "\n"
    readme.write_text(text)
    print(f"wrote {readme} and reports/results.md")


if __name__ == "__main__":
    main()
