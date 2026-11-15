"""Measure CPU vs MPS training throughput for the model sizes used in this project.

Output feeds ADR-0007 (compute strategy). Run with:

    uv run python scripts/bench_cpu_vs_mps.py

Each configuration trains a small Transformer encoder (the same shape family as
the time-token Transformer / iTransformer baselines) for a fixed number of
steps and reports steps/second. The comparison that matters for the
benchmark is *aggregate* throughput: N parallel single-threaded CPU processes
vs one MPS process.
"""

from __future__ import annotations

import json
import os
import platform
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, dataclass

import torch
from torch import nn

from battery_rul.utils import REPORTS_DIR


@dataclass(frozen=True)
class Shape:
    name: str
    d_model: int
    n_layers: int
    seq_len: int  # tokens (time steps for vanilla, variates for iTransformer)
    batch: int


SHAPES = [
    Shape("small (NASA/CALCE)", d_model=64, n_layers=2, seq_len=32, batch=64),
    Shape("medium", d_model=128, n_layers=2, seq_len=64, batch=128),
    Shape("large (Toyota pretrain)", d_model=128, n_layers=3, seq_len=128, batch=512),
]
STEPS = 60
WARMUP = 10


def _make(shape: Shape, device: str) -> tuple[nn.Module, torch.optim.Optimizer]:
    layer = nn.TransformerEncoderLayer(
        d_model=shape.d_model, nhead=4, dim_feedforward=4 * shape.d_model, batch_first=True
    )
    model = nn.Sequential(nn.TransformerEncoder(layer, num_layers=shape.n_layers)).to(device)
    return model, torch.optim.Adam(model.parameters(), lr=1e-3)


def run(shape: Shape, device: str, threads: int) -> float:
    """Return training steps/second for one process."""
    torch.set_num_threads(threads)
    torch.manual_seed(0)
    model, opt = _make(shape, device)
    x = torch.randn(shape.batch, shape.seq_len, shape.d_model, device=device)

    def step() -> None:
        opt.zero_grad(set_to_none=True)
        loss = model(x).pow(2).mean()
        loss.backward()
        opt.step()

    for _ in range(WARMUP):
        step()
    if device == "mps":
        torch.mps.synchronize()
    t0 = time.perf_counter()
    for _ in range(STEPS):
        step()
    if device == "mps":
        torch.mps.synchronize()
    return STEPS / (time.perf_counter() - t0)


def _worker(args: tuple[Shape, int]) -> float:
    shape, threads = args
    os.environ["OMP_NUM_THREADS"] = str(threads)
    return run(shape, "cpu", threads)


def parallel_cpu(shape: Shape, n_procs: int, threads: int) -> float:
    """Aggregate steps/second across n_procs concurrent CPU processes."""
    with ProcessPoolExecutor(max_workers=n_procs) as ex:
        return sum(ex.map(_worker, [(shape, threads)] * n_procs))


def main() -> None:
    n_cores = os.cpu_count() or 1
    mps_ok = torch.backends.mps.is_available()
    rows = []
    for shape in SHAPES:
        row: dict[str, object] = {"shape": asdict(shape)}
        row["cpu_1proc_1thread"] = run(shape, "cpu", 1)
        row[f"cpu_1proc_{n_cores}threads"] = run(shape, "cpu", n_cores)
        row["cpu_6proc_2threads_aggregate"] = parallel_cpu(shape, 6, 2)
        row["cpu_10proc_1thread_aggregate"] = parallel_cpu(shape, 10, 1)
        row["mps_1proc"] = run(shape, "mps", 1) if mps_ok else None
        rows.append(row)
        print(json.dumps(row, indent=2))

    out = {
        "machine": platform.platform(),
        "processor": platform.processor(),
        "cpu_count": n_cores,
        "torch": torch.__version__,
        "mps_available": mps_ok,
        "steps_per_config": STEPS,
        "results_steps_per_second": rows,
    }
    REPORTS_DIR.joinpath("tables").mkdir(parents=True, exist_ok=True)
    path = REPORTS_DIR / "tables" / "bench_cpu_vs_mps.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"\nWrote {path}")


if __name__ == "__main__":
    main()
