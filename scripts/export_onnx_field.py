"""Export the field-mode models (ADR-0022) to ONNX for the browser demo.

For each protocol (``nasa``, ``calce``, ``toyota``) and task (``soh``, ``forecast``, ``rul``) one
ONNX graph averages **all** cross-fit members, exactly as the deployed Python prediction does:

    inputs:  hist (1, L, C+1) float32  scaled channels (NaN/missing -> 0) + validity mask as the
                                       last channel, oldest row first, left-padded with zeros
             tab  (1, 1)      float32  raw log1p(last cycle_idx)
    output:  q    (1, H, Q)    float32 quantiles (SOH fraction or cycles), mean over members of
                                       the member quantiles sorted along Q

Inside the graph, per member: tab standardised with the member's tab_mu/tab_sd, the member module,
target -> output units (soh/forecast: + member y_offset per horizon; rul: x member rul_scale,
clipped at 0), sort along Q (rearrangement); then the mean over members. The point forecast is
the 0.5 quantile of the output, as in ``NeuralModel.predict``.

Also writes, per protocol, ``field_serve_meta.json`` (everything ``web/field.mjs`` needs), and
``tests/web/field_vectors.json`` plus a copy of each meta as ``tests/web/field_serve_meta_<p>.json``
(small, committed): demo uploads as CSV text with the Python
hist/tab tensors, the ONNX outputs and the final ``FieldPredictor.predict`` JSON, for
``tests/web/test_field.mjs``. ONNX vs ``FieldPredictor`` parity is checked on real windows and the
script exits non-zero when it is exceeded.

Needs the demo CSVs from ``scripts/make_field_examples.py``.

Usage: uv run python scripts/export_onnx_field.py [--weights artifacts/deploy_field]
           [--out artifacts/web/field] [--examples app/examples/field]
"""

from __future__ import annotations

import argparse
import io
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import torch
from torch import nn

from battery_rul.data import cleaning as cl
from battery_rul.data.quality import LONG_REST_S
from battery_rul.serve import field as sf
from battery_rul.serve.field import FieldPredictor
from battery_rul.tasks.samples import CLIP_Z, SKIPPED_CV_S

ROOT = Path(__file__).resolve().parents[1]
OPSET = 17
TOL_FRAC = 1e-5  # soh / forecast, absolute (SOH fraction)
TOL_RUL = 1e-5  # rul, relative to max(1, |value|) in cycles (float32 resolution)
N_PARITY_ORIGINS = 12


class _Member(nn.Module):
    def __init__(self, m: Any, task: str) -> None:
        super().__init__()
        self.module = m.module.eval()
        mu = np.atleast_1d(np.asarray(m._tab_mu, dtype=np.float64))
        sd = np.atleast_1d(np.asarray(m._tab_sd, dtype=np.float64))
        self.register_buffer("mu", torch.tensor(mu, dtype=torch.float32))
        self.register_buffer("sd", torch.tensor(sd, dtype=torch.float32))
        self.register_buffer(
            "off", torch.tensor(np.asarray(m._y_offset), dtype=torch.float32)[None, :, None]
        )
        self.task, self.rul_scale = task, float(m._rul_scale)

    def forward(self, hist: torch.Tensor, tab: torch.Tensor) -> torch.Tensor:
        t = self.module(hist, (tab - self.mu) / self.sd)
        y = torch.clamp(t * self.rul_scale, min=0.0) if self.task == "rul" else t + self.off
        return torch.sort(y, dim=2)[0]


class FieldWrapper(nn.Module):
    """Mean over all members of the sorted member quantiles (the deployed prediction)."""

    def __init__(self, members: list[Any], task: str) -> None:
        super().__init__()
        self.members = nn.ModuleList([_Member(m, task) for m in members])

    def forward(self, hist: torch.Tensor, tab: torch.Tensor) -> torch.Tensor:
        return torch.stack([m(hist, tab) for m in self.members]).mean(dim=0)


def export_task(fp: FieldPredictor, task: str, out: Path) -> None:
    t = fp.tasks[task]
    w = FieldWrapper(t.members, task).eval()
    hist = torch.zeros(1, t.lookback, len(fp.channels) + 1)
    hist[:, :, -1] = 1.0
    torch.onnx.export(
        w,
        (hist, torch.zeros(1, 1)),
        str(out / f"{task}.onnx"),
        input_names=["hist", "tab"],
        output_names=["q"],
        opset_version=OPSET,
        dynamo=False,
    )


def window_inputs(ss: Any) -> tuple[np.ndarray, np.ndarray]:
    """hist/tab exactly as ``NeuralModel._x`` builds them (before tab standardisation)."""
    hist = np.concatenate(
        [np.nan_to_num(ss.x_hist.astype(np.float32)), ss.hist_mask[..., None].astype(np.float32)],
        axis=2,
    )
    return hist, ss.x_tab.astype(np.float32)


def check_parity(fp: FieldPredictor, sessions: dict[str, Any], dfs: list[pd.DataFrame]) -> float:
    """Max |ONNX - FieldPredictor member mean| over prefixes of the demo cells, per task."""
    worst = {t: 0.0 for t in sf.TASKS}
    n = 0
    for df in dfs:
        origins = np.unique(np.linspace(sf.MIN_CYCLES, len(df), N_PARITY_ORIGINS).astype(int))
        for k in origins:
            prepared, _, _ = fp.prepare(df.iloc[:k])
            for task in sf.TASKS:
                ss, pred = fp._predict(task, prepared)
                hist, tab = window_inputs(ss)
                q = sessions[task].run(None, {"hist": hist, "tab": tab})[0]
                ref = pred.quantiles
                scale = np.maximum(1.0, np.abs(ref)) if task == "rul" else 1.0
                worst[task] = max(worst[task], float(np.max(np.abs(q - ref) / scale)))
            n += 1
    for task, tol in (("soh", TOL_FRAC), ("forecast", TOL_FRAC), ("rul", TOL_RUL)):
        if worst[task] > tol:
            raise SystemExit(f"ONNX parity FAILED for {fp.protocol}/{task}: {worst[task]:.2e}")
    print(
        f"  {fp.protocol}: ONNX vs FieldPredictor over {n} windows, max |diff| "
        + ", ".join(f"{t} {v:.1e}" for t, v in worst.items())
        + " (rul relative)"
    )
    return max(worst.values())


def cleaning_constants() -> dict[str, Any]:
    return {
        "physical_ranges": {k: list(v) for k, v in cl.PHYSICAL_RANGES.items()},
        "robust_cols": list(cl.ROBUST_COLS),
        "robust_window": cl.ROBUST_WINDOW,
        "robust_k": cl.ROBUST_K,
        "robust_min_history": cl.ROBUST_MIN_HISTORY,
        "robust_rel_floor": cl.ROBUST_REL_FLOOR,
        "pause_factor": cl.PAUSE_FACTOR,
        "pause_min_history": 3,  # expanding(min_periods=3) in cleaning.input_outliers
        "long_rest_s": LONG_REST_S,
        "charge_duration_cols": list(cl.CHARGE_DURATION_COLS),
        "charge_duration_prefixes": list(cl.CHARGE_DURATION_PREFIXES),
        "skipped_cv_s": SKIPPED_CV_S,
        "clip_z": CLIP_Z,
    }


def serve_meta(fp: FieldPredictor) -> dict[str, Any]:
    m = fp.meta
    o = m["ood"]
    cells = m["cells"]
    return {
        "model_version": m.get("model_version"),
        "protocol": fp.protocol,
        "feature_set": fp.feature_set,
        "channels": list(fp.channels),
        "inputs": list(fp.inputs),
        "optional_inputs": list(sf.OPTIONAL_INPUTS),
        "derived_from": dict(sf.DERIVED_FROM),
        "scaler": {
            "mean": [float(m["scaler"]["mean"][c]) for c in fp.channels],
            "scale": [float(m["scaler"]["scale"][c]) for c in fp.channels],
        },
        "min_cycles": sf.MIN_CYCLES,
        "max_cycles": sf.MAX_CYCLES,
        "theta": sf.THETA,
        "useful_frac": sf.USEFUL_FRAC,
        "tasks": {
            t: {
                "lookback": b.lookback,
                "horizons": list(b.horizons),
                "quantiles": list(b.members[0].quantiles),
                "alpha": b.alpha,
                "cqr_correction": b.correction,
                "n_members": len(b.members),
            }
            for t, b in fp.tasks.items()
        },
        "ood": {
            "method": o["method"],
            "mean": [float(v) for v in o["mean"]],
            "precision": np.linalg.pinv(np.asarray(o["cov"], dtype=np.float64)).tolist(),
            "threshold": float(o["threshold"]),
            "inner_false_alarm": o.get("inner_false_alarm"),
        },
        "cleaning": cleaning_constants(),
        "cells": {"train": cells["train"], "heldout": cells["heldout"]},
        "heldout": m.get("heldout", {}),
        "display": {
            "toyota_test2_coverage": 0.66,
            "notes": [
                "Field models are protocol-specific: use the one that matches your charging "
                "protocol and cell type.",
                "Intervals are conformal (CQR, 90 %) but only calibrated for cells like the "
                "training cells.",
            ],
        },
    }


# --------------------------------------------------------------------------------------
# JS test vectors
# --------------------------------------------------------------------------------------
def r8(a: Any) -> Any:
    return np.round(np.asarray(a, dtype=np.float64), 8).tolist()


def make_uploads(df: pd.DataFrame, proto: str, name: str) -> list[tuple[str, str, pd.DataFrame]]:
    """Variants of one demo cell: (variant, csv text, frame as pandas reads that text)."""
    n = len(df)
    inputs = [c for c in df.columns if c not in ("cycle_idx", "soh_measured")]

    def csv(d: pd.DataFrame, rename: dict[str, str] | None = None) -> str:
        return d.rename(columns=rename or {}).to_csv(index=False, float_format="%.8g")

    # A: shorter than every lookback, upper-case headers, one signal column blank
    a = df.iloc[:12].copy()
    a["ir_ohm"] = np.nan
    text_a = csv(a, {c: c.upper() for c in a.columns})
    # B: a mid-life prefix, clean
    b = df.iloc[: max(int(0.45 * n), 140)].copy()
    # C: a long prefix with injected outliers (each trips one cleaning rule)
    c = df.iloc[: max(int(0.8 * n), 150)].copy().reset_index(drop=True)
    last = len(c) - 1
    c.loc[last - 9, "ir_ohm"] *= 3.0  # robust z
    c.loc[last - 6, "charge_time_s"] *= 4.0  # charge pause (masks the duration columns)
    c.loc[last - 3, "fld_relax_v0"] = 9.0  # physical range
    c.loc[last - 1, "cv_time_s"] = np.nan  # a blank value (forward filled)
    assert "ir_ohm" in inputs and "charge_time_s" in inputs
    out = []
    for variant, d, text in (("short", a, text_a), ("mid", b, None), ("outliers", c, None)):
        text = text if text is not None else csv(d)
        out.append((f"{name}:{variant}", text, pd.read_csv(io.StringIO(text))))
    return out


def vector_entry(
    fp: FieldPredictor, sessions: dict[str, Any], name: str, text: str, df: pd.DataFrame
) -> dict[str, Any]:
    prepared, _, counts = fp.prepare(df)
    e: dict[str, Any] = {"name": name, "protocol": fp.protocol, "csv": text}
    e["scaled_last"] = r8(prepared.cycles[list(fp.channels)].to_numpy()[-1])
    e["hist"], e["tab"], e["q"] = {}, {}, {}
    for task in sf.TASKS:
        t = fp.tasks[task]
        ss, _ = fp._predict(task, prepared)
        hist, tab = window_inputs(ss)
        q = sessions[task].run(None, {"hist": hist, "tab": tab})[0]
        e["hist"][task] = r8(hist[0])
        e["tab"][task] = r8(tab[0])
        e["q"][task] = r8(q[0])
        assert hist.shape == (1, t.lookback, len(fp.channels) + 1)
    e["predict"] = fp.predict(df)
    e["counts"] = counts
    return e


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--weights", default="artifacts/deploy_field")
    ap.add_argument("--out", default="artifacts/web/field")
    ap.add_argument("--examples", default="app/examples/field")
    ap.add_argument("--vectors", default=str(ROOT / "tests" / "web" / "field_vectors.json"))
    ap.add_argument("--protocols", nargs="*", default=list(sf.PROTOCOLS))
    args = ap.parse_args()
    import onnxruntime as ort

    demos = json.loads((Path(args.examples) / "demos.json").read_text())
    vectors: list[dict[str, Any]] = []
    for proto in args.protocols:
        out = Path(args.out) / proto
        out.mkdir(parents=True, exist_ok=True)
        fp = FieldPredictor(Path(args.weights) / proto)
        print(f"[{proto}] exporting {', '.join(sf.TASKS)}")
        for task in sf.TASKS:
            export_task(fp, task, out)
        sessions = {
            t: ort.InferenceSession(str(out / f"{t}.onnx"), providers=["CPUExecutionProvider"])
            for t in sf.TASKS
        }
        mine = [d for d in demos if d["protocol"] == proto]
        dfs = [pd.read_csv(Path(args.examples) / f"{d['name']}.csv") for d in mine]
        check_parity(fp, sessions, dfs)
        meta_text = json.dumps(serve_meta(fp), indent=1)
        (out / "field_serve_meta.json").write_text(meta_text)
        (Path(args.vectors).parent / f"field_serve_meta_{proto}.json").write_text(meta_text)
        # vectors: one demo cell per protocol (Toyota: b3c44 when present)
        pick = next((i for i, d in enumerate(mine) if d["cell"] == "b3c44"), 0)
        for name, text, df in make_uploads(dfs[pick], proto, mine[pick]["name"]):
            e = vector_entry(fp, sessions, name, text, df)
            vectors.append(e)
            p = e["predict"]
            print(
                f"  vector {name}: {len(df)} rows, counts {p['cleaning']}, "
                f"ood {p['ood']['is_ood']}, soh {p['soh_now']['soh']:.4f}"
            )
        sizes = {f.name: f.stat().st_size // 1024 for f in sorted(out.glob("*"))}
        print(f"  wrote {out}: {sizes} KB")
    if not any(v["predict"]["cleaning"] for v in vectors):
        raise SystemExit("no vector triggers a cleaning rule")
    Path(args.vectors).write_text(json.dumps(vectors, separators=(",", ":")))
    print(f"wrote {args.vectors}: {Path(args.vectors).stat().st_size / 1e6:.2f} MB")


if __name__ == "__main__":
    main()
