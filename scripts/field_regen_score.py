"""ADR-0020 Stage 3 regeneration arm (H3): forecast error at regeneration targets.

A regeneration target is a forecast target cycle (origin + h, by ``cycle_idx``) preceded by a rest
of more than 6 h (ADR-0016 definition), on held-out cells, ``origin_policy == "all"``. Every
``field_regen`` arm (``tab``: ADR-0016 ``future_rest`` covariates; ``token``: iTransformer
``rest_token``) is paired on (test cell, seed) with the same model's ``field_final`` forecast run
(same lookback, no rest schedule).

Reported per dataset, arm and horizon (1, 10): pooled RMSE at regeneration targets (candidate and
baseline, % SOH), the relative reduction, k/n cells with a reduction, and the overall RMSE at
h = 10 / 50 over all targets. Test predictions only; no model selection is done here.

Usage: uv run python scripts/field_regen_score.py
Writes reports/tables/field_regen_events.csv/.md.
"""

from __future__ import annotations

import os
from pathlib import Path

import mlflow
import numpy as np
import pandas as pd

from battery_rul.data.io import read_tables

ROOT = Path(__file__).resolve().parents[1]
REST_S = 6 * 3600
HORIZONS = (1, 10)


def _preds(run_id: str) -> pd.DataFrame:
    p = pd.read_parquet(
        mlflow.artifacts.download_artifacts(run_id=run_id, artifact_path="predictions.parquet")
    )
    return p[p.origin_policy == "all"]


def _runs(exp: str) -> pd.DataFrame:
    r = mlflow.search_runs(
        experiment_names=[exp], filter_string="params.task='forecast'", max_results=10000
    )
    return r[r["tags.unit_key"].notna() & (r["status"] == "FINISHED")]


def _arm(r: pd.Series) -> str:
    tok = str(r.get("params.model.rest_token", "")) == "True"
    return f"{r['params.model']}+{'token' if tok else 'tab'}"


def _sq_err(p: pd.DataFrame, h: int, ev: set | None) -> np.ndarray:
    m = p[f"y_mask_h{h}"].astype(bool) & np.isfinite(p[f"y_h{h}"]) & np.isfinite(p[f"point_h{h}"])
    if ev is not None:
        tgt = zip(p.cell_id, p.origin_cycle + h, strict=True)
        m &= np.array([t in ev for t in tgt])
    return ((p.loc[m, f"point_h{h}"] - p.loc[m, f"y_h{h}"]).to_numpy() * 100) ** 2


def main() -> None:
    mlflow.set_tracking_uri(
        os.environ.get("MLFLOW_TRACKING_URI", f"sqlite:///{ROOT / 'mlflow.db'}")
    )
    reg, base = _runs("field_regen"), _runs("field_final")
    rows = []
    for ds, g in reg.groupby("params.dataset"):
        c = read_tables(ds, ROOT / "data" / "processed", curves=False).cycles
        long = c[c.rest_before_s > REST_S]
        ev = set(zip(long.cell_id, long.cycle_idx, strict=True))
        b = base[base["params.dataset"] == ds]
        for arm, ga in g.assign(arm=g.apply(_arm, axis=1)).groupby("arm"):
            model = arm.split("+")[0]
            gb = b[b["params.model"] == model]
            lb = set(ga["params.lookback"]) | set(gb["params.lookback"])
            if len(lb) != 1:
                raise SystemExit(f"{ds} {arm}: lookbacks differ {lb}")
            lookback = int(lb.pop())
            bi = {(r["params.test_cell"], r["params.seed"]): r.run_id for _, r in gb.iterrows()}
            acc: dict = {}
            for _, r in ga.iterrows():
                key = (r["params.test_cell"], r["params.seed"])
                if key not in bi:
                    continue
                pc, pb = _preds(r.run_id), _preds(bi[key])
                for h in (*HORIZONS, 50):
                    for kind, evs in (("regen", ev), ("all", None)):
                        if kind == "regen" and h == 50:
                            continue
                        d = acc.setdefault((h, kind), {"c": [], "b": [], "cell": {}})
                        ec, eb = _sq_err(pc, h, evs), _sq_err(pb, h, evs)
                        d["c"].append(ec)
                        d["b"].append(eb)
                        cc = d["cell"].setdefault(key[0], [[], []])
                        cc[0].append(ec)
                        cc[1].append(eb)
            for (h, kind), d in sorted(acc.items()):
                rc = float(np.sqrt(np.concatenate(d["c"]).mean()))
                rb = float(np.sqrt(np.concatenate(d["b"]).mean()))
                k = sum(
                    np.concatenate(v[0]).mean() < np.concatenate(v[1]).mean()
                    for v in d["cell"].values()
                    if len(np.concatenate(v[0]))
                )
                n_cells = sum(len(np.concatenate(v[0])) > 0 for v in d["cell"].values())
                rows.append(
                    {
                        "dataset": ds,
                        "arm": arm,
                        "h": h,
                        "targets": kind,
                        "lookback": lookback,
                        "n_pairs": len(d["c"]),
                        "n_targets": int(sum(len(x) for x in d["c"])),
                        "rmse_cand": rc,
                        "rmse_base": rb,
                        "reduction": 1 - rc / rb,
                        "k_cells": f"{k}/{n_cells}",
                    }
                )
    df = pd.DataFrame(rows)
    out = ROOT / "reports" / "tables" / "field_regen_events"
    df.to_csv(out.with_suffix(".csv"), index=False)
    lines = [
        "| dataset | arm | h | targets | n | RMSE cand | RMSE field_final | reduction | k cells |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in df.itertuples():
        lines.append(
            f"| {r.dataset} | {r.arm} | {r.h} | {r.targets} | {r.n_targets} | {r.rmse_cand:.2f} | "
            f"{r.rmse_base:.2f} | {r.reduction:+.1%} | {r.k_cells} |"
        )
    out.with_suffix(".md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
