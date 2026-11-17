"""Gradio demo: SOH forecast and RUL with calibrated intervals (iTransformer-v2). CPU only."""

from __future__ import annotations

import importlib.util
import json
import os
import sys
import tempfile
from pathlib import Path

import gradio as gr
import numpy as np
import pandas as pd
from matplotlib.figure import Figure

HERE = Path(__file__).resolve().parent
# Space layout: battery_rul/ sits next to app.py. Local dev: fall back to ../src.
if importlib.util.find_spec("battery_rul") is None:
    for _p in (HERE, HERE.parent / "src"):
        if (_p / "battery_rul").is_dir():
            sys.path.insert(0, str(_p))
            break

from battery_rul.serve.predictor import InputError, Predictor  # noqa: E402

EXAMPLES = HERE / "examples"
UPLOAD = "(upload my own CSV)"
THETA = 0.8
GITHUB = "https://github.com/anuragjha6557/battery-rul-transformers"
DOI = "https://doi.org/10.1109/ITEC60657.2024.10598898"
WEIGHT_FILES = ("forecast.pt", "rul.pt", "deploy_meta.json")

# colours: colour-blind-safe pair + neutrals
C_HIST, C_FC, C_TRUTH, C_EOL, C_RUL = "#1f4e79", "#d55e00", "#444444", "#b00020", "#e69f00"


def weights_dir() -> Path:
    env = os.environ.get("BATTERY_RUL_WEIGHTS")
    if env:
        return Path(env)
    from huggingface_hub import hf_hub_download

    repo = os.environ.get("BATTERY_RUL_MODEL_REPO", "anuragjha6557/battery-rul-itransformer-v2")
    paths = [Path(hf_hub_download(repo_id=repo, filename=f)) for f in WEIGHT_FILES]
    return paths[0].parent


_PREDICTOR: Predictor | None = None


def get_predictor() -> Predictor:
    global _PREDICTOR
    if _PREDICTOR is None:
        _PREDICTOR = Predictor(weights_dir())
    return _PREDICTOR


def demo_names() -> list[str]:
    return sorted(p.stem for p in EXAMPLES.glob("*.csv") if not p.stem.endswith("_full"))


# --------------------------------------------------------------------------------------
def true_eol(df: pd.DataFrame, run: int = 5, level: float = THETA) -> float | None:
    """First cycle where SOH stays below ``level`` (default 80 %) for ``run`` cycles, else None."""
    d = df.sort_values("cycle_idx").reset_index(drop=True)
    soh = d["capacity_ah"].to_numpy() / d["capacity_ah"].iloc[:5].mean()
    below = soh < level
    for i in range(len(below) - run + 1):
        if below[i : i + run].all():
            return float(d["cycle_idx"].iloc[i])
    return None


def make_figure(res: dict, truth: pd.DataFrame | None) -> Figure:
    fig = Figure(figsize=(9, 5), dpi=110)
    ax = fig.subplots()
    hc, hs = np.asarray(res["history"]["cycle"]), np.asarray(res["history"]["soh"]) * 100
    fc = res["forecast"]
    last = res["last_cycle"]
    rul = res["rul"]
    cov = round(res["coverage"] * 100)

    ax.plot(hc, hs, color=C_HIST, lw=1.8, label="measured SOH (input)")
    if truth is not None:
        t = truth.sort_values("cycle_idx")
        ts = t["capacity_ah"].to_numpy() / t["capacity_ah"].iloc[:5].mean() * 100
        later = t["cycle_idx"].to_numpy() > last
        ax.plot(
            t["cycle_idx"].to_numpy()[later],
            ts[later],
            color=C_TRUTH,
            ls="--",
            lw=1.4,
            label="measured later (hidden from the model)",
        )
    fx = np.array([last] + [f["cycle"] for f in fc])
    fy = np.array([hs[-1]] + [f["soh"] * 100 for f in fc])
    flo = np.array([hs[-1]] + [f["lo"] * 100 for f in fc])
    fhi = np.array([hs[-1]] + [f["hi"] * 100 for f in fc])
    ax.fill_between(fx, flo, fhi, color=C_FC, alpha=0.22, lw=0, label=f"{cov}% interval (SOH)")
    ax.plot(fx, fy, color=C_FC, lw=2, marker="o", ms=4, label="forecast (median)")
    ax.axhline(THETA * 100, color=C_EOL, lw=1.2, label="80% end-of-life threshold")

    if not rul["already_below_threshold"]:
        ax.axvspan(
            last + rul["lo"],
            last + rul["hi"],
            color=C_RUL,
            alpha=0.25,
            lw=0,
            label=f"RUL {cov}% interval",
        )
        ax.axvline(rul["eol_cycle"], color=C_RUL, lw=1.6, ls=":", label="predicted EOL")
    ax.axvline(last, color="#888888", lw=0.8)
    ax.text(last, 1.0, " last observed", transform=ax.get_xaxis_transform(), va="top",
            fontsize=8, color="#666666")  # fmt: skip

    xmax = max(float(fx.max()), min(last + rul["hi"], 3.0 * last))
    if truth is not None:
        t_end = true_eol(truth, level=THETA - 0.05)  # show truth a little past the threshold
        xmax = max(xmax, t_end if t_end is not None else float(truth["cycle_idx"].max()))
    ymin = min(THETA * 100 - 8, float(flo.min()) - 3)
    ax.set_xlim(hc.min(), xmax * 1.03)
    ax.set_ylim(ymin, max(hs.max(), fhi.max()) + 4)
    ax.set_xlabel("cycle")
    ax.set_ylabel("state of health, % of initial capacity")
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right", fontsize=8, framealpha=0.9)
    ax.set_title("SOH forecast and remaining useful life")
    fig.tight_layout()
    return fig


def summary_md(res: dict, truth: pd.DataFrame | None) -> str:
    rul, cov = res["rul"], round(res["coverage"] * 100)
    last = res["last_cycle"]
    lines = [
        f"**Current SOH (cycle {last}):** {res['history']['soh'][-1] * 100:.1f}%  \n"
        f"**History used:** {res['n_cycles']} cycles  \n",
        "### SOH forecast",
        f"| horizon (cycles ahead) | cycle | SOH median | {cov}% interval |",
        "|---:|---:|---:|:---|",
    ]
    for f in res["forecast"]:
        lines.append(
            f"| {f['horizon']} | {f['cycle']} | {f['soh'] * 100:.1f}% | "
            f"{f['lo'] * 100:.1f}% to {f['hi'] * 100:.1f}% |"
        )
    lines.append("\n### Remaining useful life (to 80% SOH)")
    if rul["already_below_threshold"]:
        lines.append(
            "The last measured SOH is already below 80%: the cell is past end of life "
            "by the usual definition. The model's RUL output below is not meaningful."
        )
    lines.append(
        f"- **RUL:** {rul['cycles']:.0f} cycles ({cov}% interval {rul['lo']:.0f} to "
        f"{rul['hi']:.0f})\n"
        f"- **Predicted EOL cycle:** {rul['eol_cycle']:.0f} "
        f"(interval {last + rul['lo']:.0f} to {last + rul['hi']:.0f})"
    )
    if truth is not None:
        lab = truth.attrs.get("eol")
        eol = lab["eol_cycle"] if lab and np.isfinite(lab["eol_cycle"]) else true_eol(truth)
        how = f" ({lab['label']})" if lab else ""
        txt = (
            f"cycle {eol:.0f}{how} (true RUL {eol - last:.0f} cycles)"
            if eol is not None
            else "not reached by the 80% rule within the recorded data"
        )
        lines.append(f"- *Demo ground truth (hidden from the model):* EOL at {txt}")
    return "\n".join(lines)


def ood_md(res: dict) -> str:
    o = res["ood"]
    if o["is_ood"]:
        items = "\n".join(f"- {f}" for f in o["flags"])
        return (
            "## WARNING: this input looks unlike the training cells\n"
            "The intervals below are **not guaranteed** to hold and the RUL may be unreliable.\n\n"
            f"{items}"
        )
    return (
        "Inputs resemble the training cells "
        f"(distance {o['distance']:.1f} vs threshold {o['threshold']:.1f}), so the "
        "calibrated intervals are expected to be roughly valid."
    )


def _read_input(upload, demo: str) -> tuple[pd.DataFrame, pd.DataFrame | None]:
    if demo and demo != UPLOAD:
        path = EXAMPLES / f"{demo}.csv"
        full = EXAMPLES / f"{demo}_full.csv"
        truth = pd.read_csv(full) if full.exists() else None
        lab = EXAMPLES / f"{demo}_eol.json"
        if truth is not None and lab.exists():
            truth.attrs["eol"] = json.loads(lab.read_text())
        return pd.read_csv(path), truth
    if upload is None:
        raise InputError("upload a CSV file or pick a demo cell")
    path = upload if isinstance(upload, str) else getattr(upload, "name", str(upload))
    try:
        return pd.read_csv(path), None
    except Exception as exc:
        raise InputError(f"could not read the file as CSV ({type(exc).__name__}: {exc})") from exc


def predict_ui(upload, demo: str):
    """Return (figure | None, summary markdown, OOD markdown). Never raises for bad input."""
    try:
        df, truth = _read_input(upload, demo)
        res = get_predictor().predict(df)
    except InputError as exc:
        gr.Warning(str(exc))
        return None, f"**Input problem:** {exc}", ""
    return make_figure(res, truth), summary_md(res, truth), ood_md(res)


def template_file() -> str:
    d = Path(tempfile.mkdtemp())
    p = d / "template.csv"
    pd.DataFrame(
        {"cycle_idx": range(1, 13), "capacity_ah": [2.0 - 0.002 * i for i in range(12)]}
    ).round(4).to_csv(p, index=False)
    return str(p)


FORMAT_MD = """
## CSV format

One row per charge/discharge cycle, two columns:

| column | meaning |
|---|---|
| `cycle_idx` | cycle number, integer, unique (rows are sorted for you) |
| `capacity_ah` | discharge capacity of that cycle in **ampere-hours**, positive |

- At least **10 cycles**; more history gives a better forecast (the model looks at the last 32).
- Extra columns are ignored. Header names are case-insensitive.
- State of health is computed as `capacity / mean(first 5 cycles)`, so the **first 5 rows
  must be the cell's fresh capacity** (define SOH = 100%). Do not start mid-life.
- End of life is 80% SOH. Forecast horizons are 1, 10, 25, 50 and 100 cycles ahead.
"""

ABOUT_MD = f"""
## What this is

**iTransformer-v2** is a single-channel iTransformer: it reads only the state-of-health (SOH)
history of a cell plus a few causal summaries of it (so any cycler's capacity log works). It
predicts several horizons directly with quantile heads (no recursive roll-out), and the
quantile intervals are corrected with **conformalized quantile regression (CQR)** on
calibration cells that were never used for training. Remaining useful life (RUL) is a second
model with the same recipe, giving cycles to 80% SOH with a 90% interval.

## Training data

Pooled cells from NASA (PCoE), CALCE and the Toyota/MIT-Stanford (Severson 2019) data sets.
Cells are split by cell, never by window. The demo cells are calibration cells, so the model
did not train on them.

## Limitations

- Intervals are calibrated only for cells that **resemble the training data** (lab-cycled
  18650 and LFP cells, roughly constant-current protocols). The out-of-distribution warning
  is a heuristic, not a guarantee.
- RUL for unseen chemistries, temperatures or load profiles is unreliable.
- Few calibration cells per data set, so the interval coverage itself is noisy.
- Short or very noisy histories give wide, less useful predictions.
- This is a research demo, not a safety tool.

## Links

- Code, benchmark results and model card: [{GITHUB}]({GITHUB})
- Paper: Jha et al., ITEC 2024, [10.1109/ITEC60657.2024.10598898]({DOI})
"""


def build() -> gr.Blocks:
    with gr.Blocks(title="Battery RUL — iTransformer-v2") as demo:
        gr.Markdown(
            "# Battery RUL — iTransformer-v2\n"
            "Forecast a Li-ion cell's capacity fade and remaining useful life "
            "with calibrated 90% intervals."
        )
        with gr.Tabs():
            with gr.Tab("Predict"):
                with gr.Row():
                    with gr.Column(scale=1):
                        demo_dd = gr.Dropdown(
                            [UPLOAD, *demo_names()],
                            value=(demo_names() or [UPLOAD])[0],
                            label="Demo cell (first ~55% of its life) or upload",
                        )
                        up = gr.File(label="CSV (cycle_idx, capacity_ah)", file_types=[".csv"])
                        btn = gr.Button("Predict", variant="primary")
                    with gr.Column(scale=2):
                        ood = gr.Markdown()
                        plot = gr.Plot(label="Forecast")
                        summ = gr.Markdown()
                btn.click(predict_ui, [up, demo_dd], [plot, summ, ood])
            with gr.Tab("Data format"):
                gr.Markdown(FORMAT_MD)
                tpl = gr.DownloadButton("Download CSV template", value=template_file())
                del tpl
            with gr.Tab("About"):
                gr.Markdown(ABOUT_MD)
    return demo


demo = build()

if __name__ == "__main__":
    demo.launch()
