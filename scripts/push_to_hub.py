"""Publish the deployed model and the demo Space to the Hugging Face Hub.

``--weights`` uploads ``artifacts/deploy/*`` (PyTorch) and ``artifacts/web/*`` (ONNX graphs +
``serve_meta.json`` from ``scripts/export_onnx.py``) to a model repo, with a minimal model card.
``--space`` assembles the **static** Space (``web/*`` page, the ONNX graphs, ``app/examples``)
and uploads it. Free CPU hosting of Gradio Spaces needs HF PRO (ADR-0015 amendment), so the
public demo runs in the browser; the Gradio app in ``app/`` remains for local use. When
``artifacts/web`` is absent (CI), the ONNX files are fetched from the model repo.
``--dry-run`` only assembles the staging dir and prints the plan
(no network, no token needed).
The token is read from ``HF_TOKEN`` (CI) or the ``hf auth login`` cache.

Usage: uv run python scripts/push_to_hub.py (--weights | --space) [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL_REPO = "anurag6557/battery-rul-itransformer-v2"
DEFAULT_SPACE_REPO = "anurag6557/battery-rul-itransformer-v2"
GITHUB = "https://github.com/anuragjha6557/battery-rul-transformers"
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")


def model_card(meta: dict) -> str:
    cov = {t: meta["tasks"][t]["cal_coverage_cqr"] for t in meta["tasks"]}
    return f"""---
license: mit
library_name: pytorch
tags: [battery, remaining-useful-life, time-series, conformal-prediction]
---

# Battery RUL: iTransformer-v2 weights

`{meta.get("model_version", "itransformer-v2")}`: single-channel iTransformer (SOH history plus
causal SOH summaries) with direct multi-horizon quantile heads and conformalized quantile
regression (90% intervals). Trained on pooled NASA, CALCE and Toyota/MIT-Stanford cells; the
calibration cells were never trained on.

Files: `forecast.pt` (SOH, horizons 1/10/25/50/100), `rul.pt` (cycles to 80% SOH), their ONNX
exports with pre/post-processing folded in (`forecast.onnx`, `rul.onnx`, `serve_meta.json`),
`deploy_meta.json` (CQR corrections, out-of-distribution statistics, cell split, provenance).

Calibration-set coverage after CQR (target 0.90): `{json.dumps(cov)}`

Intended use: research demo. Intervals hold only for cells resembling the training data; RUL for
unseen chemistries or protocols is unreliable. Code, benchmark and limitations: {GITHUB}
Demo Space: https://huggingface.co/spaces/{DEFAULT_SPACE_REPO}
"""


WEB_FILES = ("forecast.onnx", "rul.onnx", "serve_meta.json")


def assemble_space(dest: Path, web_dir: Path, model_repo: str) -> list[Path]:
    """Static Space: web/* + ONNX graphs + demo examples; return the relative file list."""
    shutil.copytree(ROOT / "web", dest, ignore=IGNORE, dirs_exist_ok=True)
    shutil.copytree(ROOT / "app" / "examples", dest / "examples", ignore=IGNORE)
    for n in WEB_FILES:
        if (web_dir / n).exists():
            shutil.copy2(web_dir / n, dest / n)
        else:
            from huggingface_hub import hf_hub_download

            shutil.copy2(hf_hub_download(model_repo, n), dest / n)
    return sorted(p.relative_to(dest) for p in dest.rglob("*") if p.is_file())


def push_weights(args: argparse.Namespace) -> None:
    src = Path(args.weights_dir)
    web = Path(args.web_dir)
    names = ("forecast.pt", "rul.pt", "deploy_meta.json")
    missing = [n for n in names if not (src / n).exists()]
    missing += [n for n in WEB_FILES if not (web / n).exists()]
    if missing:
        sys.exit(f"missing: {missing}; run scripts/train_deploy.py and scripts/export_onnx.py")
    meta = json.loads((src / "deploy_meta.json").read_text())
    with tempfile.TemporaryDirectory() as tmp:
        stage = Path(tmp)
        for n in names:
            shutil.copy2(src / n, stage / n)
        for n in WEB_FILES:
            shutil.copy2(web / n, stage / n)
        (stage / "README.md").write_text(model_card(meta))
        files = sorted(p.name for p in stage.iterdir())
        print(f"[weights] {args.model_repo} (model): {files}")
        if args.dry_run:
            print("[weights] dry run: nothing uploaded")
            return
        api = _api()
        api.create_repo(args.model_repo, repo_type="model", exist_ok=True)
        api.upload_folder(
            folder_path=str(stage), repo_id=args.model_repo, repo_type="model",
            commit_message="Upload iTransformer-v2 weights",
        )  # fmt: skip
        print(f"[weights] uploaded to https://huggingface.co/{args.model_repo}")


def push_space(args: argparse.Namespace) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        stage = Path(tmp) / "space"
        files = assemble_space(stage, Path(args.web_dir), args.model_repo)
        print(f"[space] {args.space_repo} (space, static): {len(files)} files")
        for f in files:
            print(f"  {f}")
        if args.dry_run:
            print("[space] dry run: nothing uploaded")
            return
        api = _api()
        api.create_repo(args.space_repo, repo_type="space", space_sdk="static", exist_ok=True)
        api.upload_folder(
            folder_path=str(stage), repo_id=args.space_repo, repo_type="space",
            commit_message="Deploy static demo",
        )  # fmt: skip
        print(f"[space] uploaded to https://huggingface.co/spaces/{args.space_repo}")


def _api():
    from huggingface_hub import HfApi, get_token

    token = os.environ.get("HF_TOKEN") or get_token()  # env (CI) or `hf auth login` cache
    if not token:
        sys.exit("no Hugging Face token: set HF_TOKEN or run `hf auth login`")
    return HfApi(token=token)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--weights", action="store_true", help="upload artifacts/deploy to the model repo"
    )
    ap.add_argument("--space", action="store_true", help="upload the static demo Space")
    ap.add_argument("--dry-run", action="store_true", help="assemble and print only; no network")
    ap.add_argument("--weights-dir", default=str(ROOT / "artifacts" / "deploy"))
    ap.add_argument("--web-dir", default=str(ROOT / "artifacts" / "web"))
    ap.add_argument("--model-repo", default=DEFAULT_MODEL_REPO)
    ap.add_argument("--space-repo", default=DEFAULT_SPACE_REPO)
    args = ap.parse_args()
    if not (args.weights or args.space):
        ap.error("pass --weights and/or --space")
    if args.weights:
        push_weights(args)
    if args.space:
        push_space(args)


if __name__ == "__main__":
    main()
