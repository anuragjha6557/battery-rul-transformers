"""ADR-0020 Stage 3 / ADR-0021: paired comparisons on the final field benchmark.

Each model family is matched to its own Stage 1-2 arm label per dataset and task (labels differ
because lookbacks were selected per model). Pairs: iTransformer vs every competitor and every
model vs age_only, paired on (test cell, seed) via ``compare_arms.compare``. Wilcoxon p-values
(Toyota only, cells >= 10) are Holm-adjusted within each (task, dataset, split) family.

Usage: uv run python scripts/field_stage3_pairs.py [--experiment field_final]
Writes reports/tables/field_final_paired.csv/.md and field_final_family_ranks.csv.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from battery_rul.eval.stats import holm_adjust

sys.path.insert(0, str(Path(__file__).parent))
from compare_arms import URI, _cache, _runs, compare

HEADLINE = {"soh": "rmse", "forecast": "rmse_h50", "rul": "rul_mae"}
ITR = "itransformer"


def family(label: str) -> str:
    return label.split("[", 1)[0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--experiment", default="field_final")
    args = ap.parse_args()
    exp = args.experiment
    _cache[exp] = runs = _runs(exp, URI)
    rows = []
    for task, metric in HEADLINE.items():
        t = runs[runs["params.task"] == task]
        for ds, g in t.groupby("params.dataset"):
            labels = {family(a): a for a in sorted(set(g["arm"]))}
            pairs = [(labels[ITR], labels[f]) for f in labels if f != ITR]
            pairs += [(labels[f], labels["age_only"]) for f in labels if f not in (ITR, "age_only")]
            for cand, ref in pairs:
                for r in compare(f"{exp}:{cand}", f"{exp}:{ref}", task, metric, "all"):
                    if r["dataset"] == ds:
                        rows.append({"task": task, **r})
    df = pd.DataFrame(rows)
    df["p_holm"] = np.nan
    for _, idx in df.groupby(["task", "dataset", "split"]).groups.items():
        p = df.loc[idx, "wilcoxon_p"]
        ok = p.notna()
        if ok.any():
            df.loc[p[ok].index, "p_holm"] = holm_adjust(p[ok].to_numpy())
    out = Path("reports/tables/field_final_paired")
    df.to_csv(out.with_suffix(".csv"), index=False)
    lines = [
        "| task | dataset | split | candidate | reference | cand | ref | delta [95% CI] | k_cells "
        "| p_holm |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in df.itertuples():
        lines.append(
            f"| {r.task} | {r.dataset} | {r.split} | {r.candidate.split(':', 1)[1]} | "
            f"{r.reference.split(':', 1)[1]} | {r.cand_mean:.3g} | {r.ref_mean:.3g} | "
            f"{r.delta:+.3f} [{r.ci_lo:+.3f}, {r.ci_hi:+.3f}] | {r.k_cells} | "
            f"{'' if np.isnan(r.p_holm) else f'{r.p_holm:.3g}'} |"
        )
    out.with_suffix(".md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
