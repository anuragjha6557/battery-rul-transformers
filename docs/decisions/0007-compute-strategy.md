# ADR-0007: Compute strategy — MPS for neural models, CPU cores for classical models (measured)

- **Status:** Accepted (supersedes the plan's untested "CPU-parallel first" assumption)
- **Date:** 2026-11-15

## Context
Everything runs on one Apple M4 Pro (12 CPU cores, 24 GB unified memory, Metal GPU). The benchmark is roughly 1 000 neural training runs plus hyperparameter search, so aggregate throughput, not single-run latency, decides wall-clock time. The plan (§8) assumed that for small models, kernel-launch overhead would make many single-threaded CPU processes beat MPS. That assumption had to be measured before any sweep was built on it.

## Options considered
1. **CPU only, N parallel processes.** Simple, deterministic, and identical to CI.
2. **MPS only, one process.** Uses the GPU but leaves it under-filled with small models.
3. **MPS with K concurrent processes for neural models, CPU cores for classical models** (LightGBM, GPR, parametric fits, sklearn).

## Evidence
`scripts/bench_cpu_vs_mps.py` was run on an idle machine (torch 2.15.0, macOS 26.6). It trains a Transformer encoder of the project's shape family, Adam, fp32. The raw output is in `reports/tables/bench_cpu_vs_mps.json`. Values are steps/s; multi-process values are aggregates.

| Shape | CPU 1×1 thr | CPU 1×12 thr | CPU 5×2 thr | CPU 10×1 thr | MPS 1 proc | MPS 2 procs | MPS 4 procs |
|---|---|---|---|---|---|---|---|
| small: d=64, L=2, 32 tok, batch 64 (NASA/CALCE) | 105 | 80 | 395 | 657 | 536 | 849 | **1 687** |
| medium: d=128, L=2, 64 tok, batch 128 | 14 | 18 | 49 | 58 | 90 | 97 | **106** |
| large: d=128, L=3, 128 tok, batch 512 (Toyota pretrain) | 0.85 | 1.23 | 0.85 | 0.45 | 5.31 | 5.65 | **6.11** |

What the numbers show:
- **The assumption was wrong.** One MPS process beats one CPU process by about 5× even at the smallest shape.
- **MPS processes stack at small shapes.** One small model leaves the GPU mostly idle, and 4 concurrent MPS processes give 3.1× the throughput of one. This is 2.6× the best CPU configuration.
- **At medium and large shapes the GPU saturates** (2–4 processes add about 7–15 %), but MPS still beats every CPU configuration by 1.8× to 13×.
- **Parallel CPU collapses at the large shape.** Ten processes give *less* total throughput than one (0.45 vs 0.85 steps/s), which points to memory-bandwidth contention on unified memory.
- **Multi-threading one CPU process barely helps** (1.2–1.5×) or hurts at the small shape.

## Decision
Option 3.
- **Neural models** train on `device="auto"` (MPS when available, otherwise CPU). Hyperparameter and seed sweeps run **4 concurrent MPS worker processes**, each with `torch.set_num_threads(1)`.
- **Classical models** (LightGBM, GPR, ElasticNet, parametric fits) run concurrently on CPU worker processes with 2 threads each, using the cores the MPS workers leave free (≈ 4–6 processes).
- **Toyota pre-training** (large shape) runs as a single MPS process; adding processes buys only about 15 %.
- `PYTORCH_ENABLE_MPS_FALLBACK=1` is set (Makefile) so a missing MPS kernel falls back to CPU instead of crashing.
- **Data loading:** in-memory tensors, no DataLoader workers (macOS spawn makes workers pure overhead at this size).

## Consequences
- **Reproducibility:** MPS kernels are not bitwise deterministic. Seeds fix initialisation and data order, and we report mean ± CI over 5 seeds anyway (ADR-0004). A CPU-determinism unit test still guards model wiring (PLAN §4). CI and the HF Space run CPU only. Results must not depend on the device beyond seed-level noise; the smoke benchmark checks one CPU-vs-MPS run pair for this.
- **Precision:** fp32 everywhere (MPS has no float64). Metrics are computed in float64 on CPU after `.cpu().double()`.
- **Changes:** `battery_rul.utils.resolve_device` defaults to `"auto"`. CLAUDE.md and PLAN §8 are updated to say MPS-first for neural models.
- **Re-run trigger:** re-run the script if torch is upgraded across a minor version or if model shapes leave the measured range.
