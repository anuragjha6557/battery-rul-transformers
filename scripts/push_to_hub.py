"""Publish the deployed model and the Gradio Space to the Hugging Face Hub.

``--weights`` uploads ``artifacts/deploy/*`` to a model repo (with a minimal model card).
``--space`` assembles a staging dir (``app/*`` plus ``src/battery_rul`` as ``battery_rul/``) and
uploads it to a Space repo. ``--dry-run`` only assembles the staging dir and prints the plan
(no network, no token needed). The token is read from the ``HF_TOKEN`` environment variable.

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
DEFAULT_MODEL_REPO = "anuragjha6557/battery-rul-itransformer-v2"
DEFAULT_SPACE_REPO = "anuragjha6557/battery-rul-itransformer-v2"
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

Files: `forecast.pt` (SOH, horizons 1/10/25/50/100), `rul.pt` (cycles to 80% SOH),
`deploy_meta.json` (CQR corrections, out-of-distribution statistics, cell split, provenance).

Calibration-set coverage after CQR (target 0.90): `{json.dumps(cov)}`

Intended use: research demo. Intervals hold only for cells resembling the training data; RUL for
unseen chemistries or protocols is unreliable. Code, benchmark and limitations: {GITHUB}
Demo Space: https://huggingface.co/spaces/{DEFAULT_SPACE_REPO}
"""


def assemble_space(dest: Path) -> list[Path]:
    """Copy app/* and src/battery_rul -> dest/battery_rul; return the relative file list."""
    shutil.copytree(ROOT / "app", dest, ignore=IGNORE, dirs_exist_ok=True)
    shutil.copytree(ROOT / "src" / "battery_rul", dest / "battery_rul", ignore=IGNORE)
    return sorted(p.relative_to(dest) for p in dest.rglob("*") if p.is_file())


def push_weights(args: argparse.Namespace) -> None:
    src = Path(args.weights_dir)
    names = ("forecast.pt", "rul.pt", "deploy_meta.json")
    missing = [n for n in names if not (src / n).exists()]
    if missing:
        sys.exit(f"missing in {src}: {missing}; run scripts/train_deploy.py first")
    meta = json.loads((src / "deploy_meta.json").read_text())
    with tempfile.TemporaryDirectory() as tmp:
        stage = Path(tmp)
        for n in names:
            shutil.copy2(src / n, stage / n)
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
        files = assemble_space(stage)
        print(f"[space] {args.space_repo} (space, gradio): {len(files)} files")
        for f in files:
            print(f"  {f}")
        if args.dry_run:
            print("[space] dry run: nothing uploaded")
            return
        api = _api()
        api.create_repo(args.space_repo, repo_type="space", space_sdk="gradio", exist_ok=True)
        api.upload_folder(
            folder_path=str(stage), repo_id=args.space_repo, repo_type="space",
            commit_message="Deploy Gradio app",
        )  # fmt: skip
        print(f"[space] uploaded to https://huggingface.co/spaces/{args.space_repo}")


def _api():
    from huggingface_hub import HfApi

    token = os.environ.get("HF_TOKEN")
    if not token:
        sys.exit("HF_TOKEN is not set")
    return HfApi(token=token)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--weights", action="store_true", help="upload artifacts/deploy to the model repo"
    )
    ap.add_argument("--space", action="store_true", help="upload the Gradio Space")
    ap.add_argument("--dry-run", action="store_true", help="assemble and print only; no network")
    ap.add_argument("--weights-dir", default=str(ROOT / "artifacts" / "deploy"))
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
