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
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODEL_REPO = "anurag6557/battery-rul-itransformer-v2"
DEFAULT_SPACE_REPO = "anurag6557/battery-rul-itransformer-v2"
GITHUB = "https://github.com/anuragjha6557/battery-rul-transformers"
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")


FIELD_BLOCK = re.compile(r"<!-- FIELD:START -->.*?<!-- FIELD:END -->\n?", re.S)
REL_LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)]+)\)")


def _field_table(field_meta: dict) -> str:
    """Per-protocol summary from ``field_meta.json`` files (keys read defensively)."""
    rows = []
    for proto, m in sorted(field_meta.items()):
        cells = m.get("cells") or {}
        held = cells.get("held_out", cells.get("test")) if isinstance(cells, dict) else None
        lb = m.get("lookbacks")
        rows.append(
            f"| {proto} | {len(m.get('channels') or [])} | "
            f"{json.dumps(lb) if lb else '-'} | {json.dumps(held) if held else '-'} |"
        )
    head = "| Protocol | Channels | Lookbacks | Held-out cells |\n|---|---|---|---|\n"
    return (
        "\nShipped under `field/` in this repo (`field_meta.json` per protocol):\n\n"
        + head
        + ("\n".join(rows) + "\n")
    )


def model_card(meta: dict, field_meta: dict | None = None) -> str:
    """HF model card: the repo's MODEL_CARD.md plus the shipped-weights header.

    The "Field models" block (between ``<!-- FIELD:START -->`` / ``<!-- FIELD:END -->``) is
    kept only when ``field_meta`` (protocol -> parsed ``field_meta.json``) is given.
    """
    cov = {t: meta["tasks"][t]["cal_coverage_cqr"] for t in meta["tasks"]}
    body = (ROOT / "MODEL_CARD.md").read_text()
    if field_meta:
        body = body.replace("<!-- FIELD:START -->", "").replace("<!-- FIELD:END -->", "")
        body = body.replace(
            "- **One model per protocol**",
            _field_table(field_meta) + "\n- **One model per protocol**",
            1,
        )
    else:
        body = FIELD_BLOCK.sub(
            "Field models (no SOH history) are not part of this upload; see the GitHub "
            "repository and ADR-0022.\n",
            body,
        )
    body = REL_LINK.sub(lambda m: f"]({GITHUB}/blob/main/{m.group(1)})", body)
    return f"""---
license: mit
library_name: pytorch
tags: [battery, remaining-useful-life, time-series, conformal-prediction]
---

# Battery RUL: iTransformer-v2 weights

`{meta.get("model_version", "itransformer-v2")}`. Files: `forecast.pt` (SOH, h = 1/10/25/50/100),
`rul.pt` (cycles to 80% SOH), their ONNX exports with pre/post-processing folded in
(`forecast.onnx`, `rul.onnx`, `serve_meta.json`), `deploy_meta.json` (CQR corrections,
out-of-distribution statistics, cell split, provenance).

Calibration-set coverage after CQR (target 0.90): `{json.dumps(cov)}`

{body}"""


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
        field_meta = {}
        field_src = src.parent / "deploy_field"  # written by scripts/train_deploy_field.py
        for fm in sorted(field_src.glob("*/field_meta.json")):
            field_meta[fm.parent.name] = json.loads(fm.read_text())
            shutil.copytree(fm.parent, stage / "field" / fm.parent.name, ignore=IGNORE)
        (stage / "README.md").write_text(model_card(meta, field_meta or None))
        files = sorted(str(p.relative_to(stage)) for p in stage.rglob("*") if p.is_file())
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
