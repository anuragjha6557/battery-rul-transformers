"""Small cross-cutting utilities: seeding, device selection, paths, config hashing."""

from __future__ import annotations

import hashlib
import json
import os
import random
from pathlib import Path
from typing import Any, Literal

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
# Override with BATTERY_RUL_DATA_DIR to share one data/ across git worktrees (data is gitignored).
DATA_DIR = Path(os.environ.get("BATTERY_RUL_DATA_DIR", PROJECT_ROOT / "data")).resolve()
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
REPORTS_DIR = PROJECT_ROOT / "reports"

DeviceName = Literal["cpu", "mps", "auto"]


def seed_everything(seed: int) -> None:
    """Seed Python, NumPy and PyTorch (CPU + MPS) for reproducible runs.

    The project's single seeding entry point; every training run must call it.
    """
    random.seed(seed)
    # Legacy global RNG is seeded on purpose: third-party code (e.g. sklearn defaults) draws
    # from it. Our own code must take an explicit np.random.Generator instead.
    np.random.seed(seed)  # noqa: NPY002
    os.environ["PYTHONHASHSEED"] = str(seed)
    try:
        import torch

        torch.manual_seed(seed)
        if torch.backends.mps.is_available():
            torch.mps.manual_seed(seed)
    except ImportError:  # pragma: no cover - torch is a hard dependency
        pass


def resolve_device(name: DeviceName = "auto") -> str:
    """Return a torch device string.

    ``"auto"`` (default) picks MPS when available, else CPU. Measured in ADR-0007:
    MPS beats every CPU configuration for this project's model shapes (2.6x at the
    smallest shape with 4 concurrent MPS processes, up to 13x at Toyota pre-training size).
    CI and the HF Space have no MPS and fall back to CPU automatically.
    """
    if name == "cpu":
        return "cpu"
    import torch

    mps_ok = torch.backends.mps.is_available()
    if name == "mps":
        if not mps_ok:
            raise RuntimeError("MPS requested but not available on this machine.")
        return "mps"
    return "mps" if mps_ok else "cpu"


def config_hash(cfg: dict[str, Any]) -> str:
    """Stable short hash of a (resolved) config dict; used as a run/cache key."""
    payload = json.dumps(cfg, sort_keys=True, default=str).encode()
    return hashlib.sha256(payload).hexdigest()[:12]
