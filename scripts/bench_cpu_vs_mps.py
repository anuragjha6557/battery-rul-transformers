"""Measure CPU vs MPS training throughput for the model sizes used in this project.

Output feeds ADR-0007 (compute strategy). Run on an otherwise idle machine:

    uv run python -u scripts/bench_cpu_vs_mps.py

Each configuration trains a small Transformer encoder (the shape family of the
time-token Transformer / iTransformer baselines) for a fixed number of steps
and reports steps/second. The comparison that matters for the benchmark is
*aggregate* throughput of N concurrent processes, because hyperparameter
search and seed/fold sweeps are embarrassingly parallel.
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
    steps: int  # timed steps (sized so each measurement takes seconds, not minutes)


SHAPES = [
    Shape("small (NASA/CALCE)", d_model=64, n_layers=2, seq_len=32, batch=64, steps=200),
    Shape("medium", d_model=128, n_layers=2, seq_len=64, batch=128, steps=60),
    Shape("large (Toyota pretrain)", d_model=128, n_layers=3, seq_len=128, batch=512, steps=15),
]
WARMUP = 5


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

    def sync() -> None:
        if device == "mps":
            torch.mps.synchronize()

    for _ in range(WARMUP):
        step()
    sync()
    t0 = time.perf_counter()
    for _ in range(shape.steps):
        step()
    sync()
    return shape.steps / (time.perf_counter() - t0)


def _worker(args: tuple[Shape, str, int]) -> float:
    shape, device, threads = args
    os.environ["OMP_NUM_THREADS"] = str(threads)
    return run(shape, device, threads)


def aggregate(shape: Shape, device: str, n_procs: int, threads: int) -> float:
    """Aggregate steps/second across n_procs concurrent processes."""
    with ProcessPoolExecutor(max_workers=n_procs) as ex:
        return sum(ex.map(_worker, [(shape, device, threads)] * n_procs))


def main() -> None:
    n_cores = os.cpu_count() or 1
    mps_ok = torch.backends.mps.is_available()
    configs: list[tuple[str, str, int, int]] = [
        # (label, device, n_procs, threads_per_proc)
        ("cpu 1 proc x 1 thread", "cpu", 1, 1),
        (f"cpu 1 proc x {n_cores} threads", "cpu", 1, n_cores),
        ("cpu 5 procs x 2 threads", "cpu", 5, 2),
        ("cpu 10 procs x 1 thread", "cpu", 10, 1),
    ]
    if mps_ok:
        configs += [
            ("mps 1 proc", "mps", 1, 1),
            ("mps 2 procs", "mps", 2, 1),
            ("mps 4 procs", "mps", 4, 1),
        ]
    rows = []
    for shape in SHAPES:
        row: dict[str, object] = {"shape": asdict(shape)}
        for label, device, n_procs, threads in configs:
            t0 = time.perf_counter()
            if n_procs == 1:
                sps = run(shape, device, threads)
            else:
                sps = aggregate(shape, device, n_procs, threads)
            row[label] = round(sps, 2)
            print(
                f"{shape.name:26s} {label:26s} {sps:9.2f} steps/s "
                f"(wall {time.perf_counter() - t0:5.1f}s)",
                flush=True,
            )
        rows.append(row)

    out = {
        "machine": platform.platform(),
        "processor": platform.processor(),
        "cpu_count": n_cores,
        "torch": torch.__version__,
        "mps_available": mps_ok,
        "results_steps_per_second": rows,
    }
    REPORTS_DIR.joinpath("tables").mkdir(parents=True, exist_ok=True)
    path = REPORTS_DIR / "tables" / "bench_cpu_vs_mps.json"
    path.write_text(json.dumps(out, indent=2))
    print(f"\nWrote {path}")


if __name__ == "__main__":
    main()
