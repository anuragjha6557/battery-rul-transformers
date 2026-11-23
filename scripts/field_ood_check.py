"""ADR-0022 OOD guard: choose the distance from training cells only, then report held-out rates.

For each protocol (deployed ``artifacts/deploy_field/<protocol>``) and each candidate
distance on the scaled channel vector of a cycle:

* ``full``: Mahalanobis with the sample covariance;
* ``ledoit_wolf``: Mahalanobis with the Ledoit-Wolf shrunk covariance;
* ``diagonal``: Euclidean norm of per-channel z-scores (independent channels).

**Selection (training cells only):** the deployed model's inner folds (NASA/CALCE: leave one
training cell out; Toyota: the 5 grouped folds) fit the statistics and the 99th-percentile
threshold on the inner-training cells, and count flagged cycles of the inner-validation cells.
A cell like the training cells should be flagged about 1 % of the time; the method whose mean
inner false-alarm rate is closest to 1 % is chosen (ties: simpler method).

**Report (held-out cells, not used for the choice):** statistics refit on all training cells,
then the flag rate on each held-out split. Toyota test2 is the known batch shift (EDA §5).

Usage: uv run python scripts/field_ood_check.py
Writes reports/tables/field_ood_check.csv/.md and the chosen method into each field_meta.json.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.covariance import LedoitWolf

from battery_rul.serve.field import PROTOCOLS, FieldPredictor
from battery_rul.tasks.samples import merge_field_features
from battery_rul.train.runner import dataset_ctx

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "artifacts" / "deploy_field"
METHODS = ("diagonal", "ledoit_wolf", "full")  # simplest first (tie-break)
NOMINAL = 0.01


def fit_stats(x: np.ndarray, method: str) -> dict:
    mu = x.mean(axis=0)
    if method == "full":
        cov = np.cov(x, rowvar=False)
    elif method == "ledoit_wolf":
        cov = LedoitWolf().fit(x).covariance_
    else:
        cov = np.diag(np.maximum(x.var(axis=0), 1e-12))
    prec = np.linalg.pinv(cov)
    d = dist(x, mu, prec)
    return {"mean": mu, "cov": cov, "prec": prec, "threshold": float(np.quantile(d, 0.99))}


def dist(x: np.ndarray, mu: np.ndarray, prec: np.ndarray) -> np.ndarray:
    z = x - mu
    return np.sqrt(np.einsum("ij,jk,ik->i", z, prec, z).clip(min=0))


def scaled_by_cell(fp: FieldPredictor, ds: str) -> dict[str, np.ndarray]:
    cyc = dataset_ctx(ds, str(ROOT / "data" / "processed"), 0.8).cycles
    feats = pd.read_parquet(ROOT / "data" / "processed" / ds / "field_features.parquet")
    cyc = merge_field_features(cyc, feats)
    cols = [c for c in [*fp.inputs, "charge_time_s"] if c in cyc.columns]
    out = {}
    for cell, g in cyc.groupby("cell_id"):
        prep, _, _ = fp.prepare(g[cols])
        out[str(cell)] = prep.cycles[list(fp.channels)].to_numpy(dtype=np.float64)
    return out


def main() -> None:
    rows = []
    for ds in PROTOCOLS:
        d = DEPLOY / ds
        if not (d / "field_meta.json").exists():
            continue
        fp = FieldPredictor(d)
        meta = fp.meta
        x = scaled_by_cell(fp, ds)
        train = list(meta["cells"]["train"])
        inner = meta["cells"]["inner"]
        fa = {}
        for method in METHODS:
            rates = []
            for tr, va in inner:
                st = fit_stats(np.vstack([x[c] for c in tr]), method)
                rates += [
                    float((dist(x[c], st["mean"], st["prec"]) > st["threshold"]).mean()) for c in va
                ]
            fa[method] = float(np.mean(rates))
            st = fit_stats(np.vstack([x[c] for c in train]), method)
            row = {"protocol": ds, "method": method, "inner_false_alarm": fa[method]}
            for tag, cells in meta["cells"]["heldout"].items():
                row[f"flag_rate_{tag}"] = float(
                    np.mean(
                        [
                            (dist(x[c], st["mean"], st["prec"]) > st["threshold"]).mean()
                            for c in cells
                        ]
                    )
                )
            rows.append(row)
        chosen = min(METHODS, key=lambda m: (abs(fa[m] - NOMINAL), METHODS.index(m)))
        st = fit_stats(np.vstack([x[c] for c in train]), chosen)
        meta["ood"] = {
            "method": chosen,
            "mean": st["mean"].tolist(),
            "cov": st["cov"].tolist(),
            "threshold": st["threshold"],
            "inner_false_alarm": fa[chosen],
            "selection": "inner-fold false-alarm rate closest to 1 % (field_ood_check.py)",
        }
        (d / "field_meta.json").write_text(json.dumps(meta, indent=2))
        for r in rows:
            if r["protocol"] == ds:
                r["chosen"] = r["method"] == chosen
    df = pd.DataFrame(rows)
    out = ROOT / "reports" / "tables" / "field_ood_check"
    df.to_csv(out.with_suffix(".csv"), index=False)
    cols = [c for c in df.columns if c not in ("protocol", "method", "chosen")]
    lines = [
        "| protocol | method | " + " | ".join(cols) + " | chosen |",
        "|---|---|" + "---|" * len(cols) + "---|",
    ]
    for r in df.itertuples(index=False):
        d_ = r._asdict()
        vals = " | ".join("" if pd.isna(d_[c]) else f"{d_[c]:.1%}" for c in cols)
        lines.append(f"| {r.protocol} | {r.method} | {vals} | {'**yes**' if r.chosen else ''} |")
    out.with_suffix(".md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
