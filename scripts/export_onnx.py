"""Export the deployed models to ONNX for the browser demo (static HF Space, ADR-0015 amendment).

Each ONNX graph wraps the trained network *with* the model-side transforms so the browser only
has to build the input window and the five SOH summaries:

    inputs:  hist (1, L, 2) float32  - SOH window (NaN -> 0) and validity mask, oldest first
             tab  (1, 5)    float32  - raw SOH summaries (last, mean_5, slope_10, slope_50, curv_50)
    output:  q    (1, H, Q) float32  - quantiles in SOH fraction (forecast) or cycles (rul),
                                       sorted along Q (rearrangement)

Inside the graph: tab standardisation with the training mean/sd; forecast adds the last SOH
(residual target); rul multiplies by the training RUL scale and clips at 0.

Also writes ``serve_meta.json`` (lookback, horizons, quantile levels, CQR corrections, OOD
statistics with a precomputed precision matrix) and ``test_vectors.json`` (inputs + expected
outputs for the demo cells) used by the JS tests, and checks ONNX vs PyTorch parity.

Usage: uv run python scripts/export_onnx.py [--weights artifacts/deploy] [--out artifacts/web]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from torch import nn

from battery_rul.serve.predictor import (
    MIN_CYCLES,
    SOH_RANGE,
    Predictor,
    latest_sample,
    to_cycles,
    validate_cycles,
)


class ServeWrapper(nn.Module):
    def __init__(self, module: nn.Module, mu, sd, task: str, rul_scale: float) -> None:
        super().__init__()
        self.module = module
        self.register_buffer("mu", torch.tensor(np.atleast_1d(mu), dtype=torch.float32))
        self.register_buffer("sd", torch.tensor(np.atleast_1d(sd), dtype=torch.float32))
        self.task, self.rul_scale = task, float(rul_scale)

    def forward(self, hist: torch.Tensor, tab: torch.Tensor) -> torch.Tensor:
        t = self.module(hist, (tab - self.mu) / self.sd)
        if self.task == "rul":
            y = torch.clamp(t * self.rul_scale, min=0.0)
        else:
            y = t + hist[:, -1, 0][:, None, None]  # last window step = origin SOH
        return torch.sort(y, dim=2)[0]


def export(pred: Predictor, task: str, out: Path) -> None:
    m = pred.tasks[task].model
    m.module.eval()
    w = ServeWrapper(m.module, m._tab_mu, m._tab_sd, task, m._rul_scale).eval()
    L = pred.tasks[task].lookback
    hist = torch.zeros(1, L, 2)
    hist[:, :, 1] = 1.0
    tab = torch.zeros(1, 5)
    torch.onnx.export(
        w,
        (hist, tab),
        str(out / f"{task}.onnx"),
        input_names=["hist", "tab"],
        output_names=["q"],
        opset_version=17,
        dynamo=False,
    )


def sample_inputs(pred: Predictor, task: str, df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
    b = pred.tasks[task]
    cyc = to_cycles(validate_cycles(df))
    ss = latest_sample(cyc, task, b.lookback, b.horizons if task == "forecast" else (0,))
    hist = np.concatenate(
        [np.nan_to_num(ss.x_hist.astype(np.float32)), ss.hist_mask[..., None].astype(np.float32)],
        axis=2,
    )
    return hist, ss.x_tab.astype(np.float32)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--weights", default="artifacts/deploy")
    ap.add_argument("--out", default="artifacts/web")
    ap.add_argument("--examples", default="app/examples")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    pred = Predictor(args.weights)
    for task in ("forecast", "rul"):
        export(pred, task, out)

    import onnxruntime as ort

    vectors, worst = [], {"forecast": 0.0, "rul": 0.0}
    for csv in sorted(Path(args.examples).glob("*.csv")):
        if csv.stem.endswith("_full"):
            continue
        df = pd.read_csv(csv)
        entry: dict = {"name": csv.stem, "cycle_idx": df["cycle_idx"].tolist(),
                       "capacity_ah": df["capacity_ah"].tolist()}  # fmt: skip
        for task in ("forecast", "rul"):
            hist, tab = sample_inputs(pred, task, df)
            sess = ort.InferenceSession(str(out / f"{task}.onnx"))
            q_onnx = sess.run(None, {"hist": hist, "tab": tab})[0]
            b = pred.tasks[task]
            cyc = to_cycles(validate_cycles(df))
            ss = latest_sample(cyc, task, b.lookback, b.horizons if task == "forecast" else (0,))
            q_torch = b.model.predict(ss).quantiles
            worst[task] = max(worst[task], float(np.max(np.abs(q_onnx - q_torch))))
            entry[task] = {"hist": hist[0].tolist(), "tab": tab[0].tolist(),
                           "q": q_onnx[0].tolist()}  # fmt: skip
        entry["predict"] = pred.predict(df)  # full Python output, for end-to-end JS checks
        vectors.append(entry)
    print(
        f"ONNX vs PyTorch max |diff|: forecast {worst['forecast']:.1e} SOH, "
        f"rul {worst['rul']:.1e} cycles"
    )
    if worst["forecast"] > 1e-5 or worst["rul"] > 1e-2:
        raise SystemExit("ONNX parity check failed")

    o = pred.meta["ood"]
    meta = {
        "model_version": pred.meta.get("model_version"),
        "min_cycles": MIN_CYCLES,
        "soh_range": list(SOH_RANGE),
        "theta": 0.8,
        "tasks": {
            t: {
                "lookback": b.lookback,
                "horizons": list(b.horizons),
                "quantiles": list(b.model.quantiles),
                "alpha": b.alpha,
                "cqr_correction": b.correction,
            }
            for t, b in pred.tasks.items()
        },
        "ood": {
            "features": o["features"],
            "mean": o["mean"],
            "precision": np.linalg.pinv(np.asarray(o["cov"])).tolist(),
            "threshold": o["threshold"],
            "fade_per_100_range": o["fade_per_100_range"],
        },
    }
    (out / "serve_meta.json").write_text(json.dumps(meta, indent=1))
    (out / "test_vectors.json").write_text(json.dumps(vectors))
    print(f"wrote {out}: forecast.onnx, rul.onnx, serve_meta.json, test_vectors.json")


if __name__ == "__main__":
    main()
