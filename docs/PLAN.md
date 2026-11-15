# Battery RUL v2 — End-to-End ML Project Plan

> **Handoff note for the lead (Opus 5.5):** This plan is the contract. Sections 1–3 are fixed decisions; Section 4+ are phases with explicit *what/why/owner-model/parallelism/gate*. Every methodological choice must end up as a short ADR in `docs/decisions/` so the owner can defend it in an interview. Do not spend effort reproducing the paper's exact numbers — the owner has said those numbers are **not to be trusted**. The deliverable is an honest, leakage-free benchmark + a stronger method + a public demo, not a confirmation of the paper.

---

## 1. Context

**Source paper:** *iTransformer Network Based Approach for Accurate Remaining Useful Life Prediction in Lithium-Ion Batteries* (Jha, Dorkar, Biswas, Emadi — IEEE ITEC 2024). The owner is the first author. PDF: `docs/paper/jha2024_itransformer_rul.pdf` (local only, gitignored — IEEE copyright; cite DOI 10.1109/ITEC60657.2024.10598898). Extracted text (for agents): `docs/paper/jha2024_itransformer_rul.txt` (re-extract with `swift scripts/pdftext.swift <pdf>` if needed — no PDF libs are installed system-wide).

**What the paper did:** Capacity (SOH) trajectory forecasting on NASA PCoE cells B0005/06/07/18 (2 Ah, EOL = 1.4 Ah) and CALCE CS2_35/36/37/38 (1.1 Ah LiCoO2). Two input modes: *single-channel* (capacity history, lookback window L, recursive one-step-ahead rollout) and *multi-channel* (capacity + 10-point uniformly resampled charging V/I/T curves for NASA, resistance for CALCE). Min-max normalization; 3-fold CV across the 4 cells; grid search over window ∈{16,32,64,128}, hidden ∈{16,32,64,128}, LR ∈{1e-3…5e-1}; dropout 0.1; Adam. Models: LSTM, vanilla Transformer, iTransformer. Metrics RMSE/MAE/RE. Claimed iTransformer RMSE gains of 44.6 % (NASA) and 29 % (CALCE).

**Why rebuild from scratch (owner's instruction + independent reasons):**
1. The numbers may be wrong; no code survives. Treat the paper as the *idea*, not the *baseline*.
2. Protocol weaknesses that could invalidate the result, ranked by severity (verify each empirically in Phase 3/4, don't assume):
   - **The multi-channel results are almost certainly nowcasting, not forecasting.** Recursion is only defined for single-channel; future V/I/T curves don't exist, so MC models must have been scored one-step-ahead with *measured* charging curves — likely of the target cycle itself. That is SOH *estimation* (the paper's own ref [20], Choi 2019). The claim that the model "predicts regeneration peaks" of B0018 is the tell: regeneration after a rest is not predictable from prior cycles, only readable from the regenerated cycle's own charge curve. The SC-vs-MC "50 % gain" is therefore an apples-to-oranges comparison (hundreds of compounding recursive steps vs one step with ground-truth exogenous data). Expect a **persistence baseline** to land in the same RMSE band as the paper's MC numbers — run it first.
   - **RUL is never actually evaluated.** No prediction-start point, no horizon, RUL_pred in Eq. (11) undefined; RE of 0.003 on CALCE (~2–8 cycles on ~900-cycle lives) is only possible by reading the threshold crossing off a one-step track of the truth. B0007 barely grazes the 1.4 Ah threshold → its RUL is **censored**, yet RE is reported.
   - Min-max scaling fitted over each cell's *full* life (incl. the test cell's EOL minimum) → leakage; RMSE in normalized units makes cells/datasets non-comparable, so "44.6 %" is a ratio of quantities on different scales.
   - 4 cells, no seeds, no CI, winner's-curse grid search (96 configs selected on one validation cell).
   - Unfair/under-tuned baselines (LR grid up to 0.5 for Adam diverges time-token Transformers); window 128 / hidden 128 on a 168-cycle cell is memorization; no linear/GPR/GBM baselines, which the LTSF literature (Zeng et al. 2023) shows routinely beat Transformers on small data. SC-iTransformer (N=1 variate = an MLP on the window) is never reported.
   - Underspecified preprocessing ("cleaned to remove abnormal data"; 10 points uniform in *time* or *index*? CC duration shrinks with age, so this choice is itself a feature).
   - No uncertainty quantification; no cross-chemistry/generalization test (the paper's own stated future work).

**Intended outcome:** A public GitHub repo + live Hugging Face Space where anyone can upload cycle data and receive a calibrated RUL distribution, backed by a defensible benchmark on NASA + CALCE + Toyota/MIT-Stanford (Severson 2019, 124 LFP cells), with every design decision justified by an experiment or an ADR.

---

## 2. Fixed decisions (do not re-litigate)

| Decision | Choice | Why |
|---|---|---|
| Hardware | Apple M4 Pro, 12 cores, 24 GB, 272 GB free. Everything runs locally. | Owner constraint. All models here are tiny (cells have 150–2 000 cycles); the bottleneck is *number of runs*, not run size → parallelize across cores. |
| Python / env | `uv` (installed at `~/.local/bin/uv`), **pin Python 3.12** in `pyproject.toml` / `.python-version` | Homebrew default is 3.14; torch 2.9 only has *preview* 3.14 wheels and parts of the ecosystem (mlflow, lightgbm, gradio deps) lag. 3.12 is the safe, defensible choice. |
| DL framework | PyTorch, **MPS-first for neural models** (measured in Phase 0, ADR-0007 — the original CPU-parallel assumption was wrong). | MPS beat every CPU configuration at all model sizes (2.6×–13× aggregate). |
| Tracking | MLflow, local file store at `./mlruns` (gitignored) + `mlflow ui` | Owner choice; no cloud accounts needed. |
| VCS / CI | GitHub (public repo), GitHub Actions: ruff + pytest on push; HF Space sync on tag. `gh` CLI must be installed (`brew install gh && gh auth login`). | Owner choice. |
| Hosting | Hugging Face Spaces, **CPU Basic (2 vCPU / 16 GB, free — confirmed on huggingface.co/pricing 2026-11-15)**, Gradio SDK. Model weights in an HF Model repo. Fallback if free tier is unavailable at deploy time: Streamlit Community Cloud. | Owner choice. Forum reports (mid-2026) of free-tier restrictions exist → verify the Space builds in Phase 8 early, not last. |
| Datasets | NASA PCoE (B0005/06/07/18) + CALCE (CS2_35–38) retained; **add Toyota/MIT-Stanford Severson 2019** (124 LFP cells, 3 MATLAB v7.3 batches, ~5 GB). | Owner choice. Toyota gives statistical power (n=124 vs 4) and a different chemistry (LFP vs NMC/LCO) for a transfer-learning story. |
| Scope | Deep on NASA+CALCE+Toyota; no further datasets unless Phase 7 finishes early. | Owner choice. |
| Core idea retained | Inverted (variate-token) attention over multi-channel **per-cycle curve features** for battery prognostics. On NASA/CALCE those are charging curves (as in the paper); on Toyota the charging protocol is the *experimental variable* (varies per cell by design) while the 4C discharge is standardized, so Toyota uses discharge-derived curve features. | Owner constraint; reframed so the thesis survives the Toyota protocol confound. |
| Config system | Hydra with structured (dataclass) configs; resolved YAML + hash logged to every MLflow run. | Standard, composable (`data × model × task × experiment` groups), interview-recognizable. |
| Repo framing | GitHub repo `battery-rul` presented as a **benchmark + one new entry (iTransformer-v2)**, not a rerun of the paper. | Honest headline survives whatever the results are. |

---

## 3. Success criteria (what "significantly improved" means)

The project is done when all of these hold. They replace "beat the paper's RMSE".

1. **Rigor:** Leakage-free, leave-one-cell-out benchmark of ≥ 9 methods (Section 6) on 3 datasets, ≥ 5 seeds each, reported as mean ± 95 % CI with paired statistical tests; every number traceable to an MLflow run ID; results tables auto-generated into `reports/`.
2. **Honest task framing:** Three clearly separated tasks — SOH estimation, multi-horizon capacity forecasting (no teacher forcing), direct RUL — with RUL evaluated at multiple prediction-start points and the α-λ prognostic metric.
3. **Uncertainty:** Probabilistic RUL/capacity with prediction intervals whose empirical coverage on held-out cells is within ±5 pp of nominal (90 %).
4. **Generalization:** A quantified cross-chemistry result (train Toyota → zero-shot and fine-tune on NASA/CALCE) — positive or negative, reported either way.
5. **Deployment:** Public HF Space (upload CSV or pick a demo cell → forecast plot + RUL interval), installable Python package (`pip install battery-rul`), green CI, model card, README with results and ADR index.
6. **Defensibility:** Every non-trivial choice has an ADR (`docs/decisions/NNNN-*.md`) in the *Context / Options considered / Decision / Evidence* format, ≤ 1 page each.

Non-goals: physics-based models, real-time BMS integration, GPU cloud training, more than 3 datasets.

---

## 4. Repository layout (create in Phase 0)

```
RUL_project/                      # git root — rename repo "battery-rul" on GitHub
├── pyproject.toml                # uv-managed; [project.scripts] battery-rul = "battery_rul.cli:app"
├── .python-version               # 3.12
├── Makefile                      # make env | data | test | lint | bench | app
├── README.md                     # results tables generated by scripts/make_readme_tables.py
├── PROTOCOL.md                   # tasks, splits, leakage rules, metrics, stats — written BEFORE any sweep
├── MODEL_CARD.md
├── configs/                      # Hydra groups + structured configs (see ADR-0003)
│   ├── data/{nasa,calce,toyota}.yaml
│   ├── model/{persistence,trend,gpr,lgbm,dlinear,lstm,transformer,patchtst,itransformer,itransformer_v2}.yaml
│   ├── task/{soh,forecast,rul}.yaml
│   └── experiment/*.yaml         # one file per benchmark table
├── src/battery_rul/
│   ├── data/      download.py (checksummed), nasa.py, calce.py, toyota.py, schema.py (pandera), registry.py
│   ├── features/  curves.py (voltage-grid resample, CC/CV split, ICA dQ/dV, ΔQ(V)), capacity.py (rolling stats), build.py
│   ├── tasks/     soh.py, forecast.py, rul.py (label construction, EOL rules incl. censoring, start-point sweep)
│   ├── splits/    loco.py (leave-one-cell-out, nested), toyota.py (Severson official split + grouped 5-fold), scaling.py (train-only scalers)
│   ├── models/    base.py (fit/predict/predict_dist protocol), persistence.py, paramfit.py, gpr.py, lgbm.py, linear.py (ElasticNet),
│   │              dlinear.py, lstm.py, transformer.py, patchtst.py, itransformer.py, heads.py (point/quantile/RUL), blend.py
│   ├── uq/        ensemble.py, quantile.py, conformal.py (CQR), ood.py (Mahalanobis on feature vector)
│   ├── train/     trainer.py (torch loop, early stop, seed), tune.py (Optuna, equal budget), runner.py
│   ├── eval/      metrics.py (RMSE/MAE/RUL-err/α-λ/PICP/MPIW/pinball/CRPS), stats.py (paired bootstrap, Wilcoxon), report.py
│   ├── serve/     predictor.py (ONNX/TorchScript weights, validate input, OOD score, return dict), schema.py (pydantic input contract — same as data/schema.py)
│   └── cli.py     typer: download, build-features, train, tune, benchmark, report, serve
├── app/           gradio_app.py, examples/ (one demo CSV per dataset), README.md (HF Space card)
├── scripts/       bench_cpu_vs_mps.py, make_readme_tables.py, export_weights.py, push_to_hub.py
├── tests/         unit (fast, synthetic data) + integration (marked slow, use tiny real subsets)
├── notebooks/     01_eda_nasa.ipynb … (exploration only; nothing in notebooks is load-bearing)
├── reports/       figures/, tables/, results.md (generated), data_quality.md
├── docs/decisions/ 0001-record-architecture-decisions.md …
├── data/          raw/ processed/ (gitignored; `make data` rebuilds with checksums) + data/README.md
└── .github/workflows/ ci.yml, deploy-space.yml
```

Code conventions (enforce in CI): ruff (lint+format), mypy on `src/` (lenient), pytest ≥ 80 % line coverage on `src/battery_rul/{features,tasks,splits,eval,uq,serve}`, every model implements the `Model` protocol in `models/base.py` so the benchmark runner is model-agnostic, every experiment is a config file (no CLI-arg soup), seeds set via one `seed_everything(seed)` utility, no notebook is required to reproduce a table.

Testing strategy: unit tests use **synthetic fixtures only** (synthetic curves with a known ICA peak; windowing with `hypothesis`; metrics vs hand-computed cases incl. censored RUL; scaler-leakage perturbation test; LOCO disjointness; quantile monotonicity). Per-model: fit/predict shape test on a 2-cell synthetic set < 10 s, "overfit one batch" wiring test, CPU determinism test. Integration: `train` end-to-end on synthetic data with `fast_dev_run`. Real-data checks (checksums, B0005 = 168 cycles, B0018 = 132) are `@pytest.mark.data` and skipped in CI.

CI (`ci.yml`, Ubuntu, target < 5 min): `uv sync --frozen` with the **CPU-only torch index** configured in `pyproject.toml` (avoids a 2 GB CUDA download) + uv cache → ruff check/format → mypy → pytest excluding `data`/`slow` → second job launches the Gradio app and POSTs one example request. `deploy-space.yml` on tag: `huggingface_hub` upload to the Space via a repo secret. Pre-commit: ruff, nbstripout.

---

## 5. Data

### 5.1 Sources (verified 2026-11-15)
| Dataset | URL | Format | Notes |
|---|---|---|---|
| NASA PCoE Battery Data Set #5 | `https://phm-datasets.s3.amazonaws.com/NASA/5.+Battery+Data+Set.zip` | `.mat` (v5) per cell, nested struct of `cycle` entries (charge/discharge/impedance) | Use B0005/06/07/18 only. Capacity is in each *discharge* cycle; charge curves in *charge* cycles. Pairing charge→next discharge must be explicit. |
| CALCE CS2 | `https://web.calce.umd.edu/batteries/data/` → CS2_35…38 | zip of `.xlsx` per test day (Arbin) | Capacity per cycle must be *computed* (integrate discharge current). Known issues: duplicate cycle indices across files, date-ordering of files, a few junk cycles — document each in `reports/data_quality.md`. |
| Toyota/MIT-Stanford (Severson 2019) | `https://data.matr.io/1/projects/5c48dd2bc625d700019f3204` (3 batches; JS page — download links appear in-browser) | MATLAB **v7.3** `.mat` (HDF5, ~1–1.5 GB each) → stream with `h5py`, dereference per cell, extract per-cycle summaries + the pre-interpolated 1000-point `Qdlin/Vdlin/Tdlin` **discharge** curves (these give ΔQ(V) directly), resample to our grid, write parquet, discard. Peak RAM < 3 GB. | Apply the official cleaning from the rdbraatz repo's `BuildPkl_Batch*.ipynb` (open processing code; the *modelling* code is licensed — don't copy it): drop documented bad cells in batch 1, merge batch-1 cells that continue into batch 2. Use the **Severson official train / primary-test / secondary-test split** so Toyota numbers are literature-comparable. Charging protocols vary per cell by design → do not use Toyota charge curves as model input. This is the slowest step in the project; cache it once. |

Download is scripted with SHA-256 checks (`src/battery_rul/data/download.py`); raw data is **never** committed. If the Toyota links can't be fetched headlessly, the lead asks the owner to download once in a browser into `data/raw/toyota/`.

### 5.2 Canonical schema (`data/schema.py`, pandera-validated)
- `cycles.parquet`: `dataset, cell_id, cycle_idx, capacity_ah, soh (=capacity/nominal), is_eol, rul_cycles, charge_time_s, cc_time_s, cv_time_s, t_to_4v2_s, charge_throughput_ah, temp_max_c, ir_ohm (where available), …`
- `curves.parquet`: `dataset, cell_id, cycle_idx, phase ∈ {charge, discharge}, grid_idx, V, I, T, Q` — curves resampled on a **fixed voltage grid** (default 64 points; paper used 10 uniform-in-time points — kept as the `paper10` feature set for the ablation, config `features.curve_grid`). Voltage-grid resampling is what makes ΔQ(V) and cross-protocol transfer possible.
- `soh = capacity / mean(capacity of first 5 cycles)` (per-cell, uses only the cell's own early cycles — no future). Nominal capacity per dataset in `configs/data/*.yaml` for reference only.
- **EOL threshold: 80 % SOH for all datasets** (primary; CALCE/Toyota convention) with a **70 % sensitivity table** (NASA design threshold). Cells that never cross a threshold (B0007 at 70 %) are **censored**: RUL label is marked censored and excluded from RUL metrics at that threshold, never silently included (ADR-0005).
- EOL rule: first cycle where a 5-cycle centered median of SOH < threshold (robust to regeneration spikes). Alternative rules evaluated in Phase 2, decision in ADR-0005.

### 5.3 Data quality report (Phase 2 deliverable)
Per cell: cycle count, capacity range, missing/duplicated cycles, regeneration events, EOL cycle under each rule, plots. This is what makes "we cleaned the data" defensible.

---

## 6. Methodology

### 6.1 Tasks (all three are first-class; config `task/*.yaml`)
| Task | Input at cycle k | Target | Why it's separate |
|---|---|---|---|
| **A. SOH estimation (nowcasting)** | curve features of cycle k only (optionally recent history) | SOH_k | This is what the paper's "multi-channel" actually measured. Legitimate and useful in deployment when capacity isn't directly measurable. Metrics in %SOH. |
| **B. Capacity forecasting** | everything up to T_p (SOH history + curve features, cycles ≤ T_p) — **no measured features beyond T_p, ever** | SOH_{T_p+1..T_p+H}, **direct multi-horizon**, H ∈ {1, 10, 50, 100} (200 for Toyota); also recursive rollout to EOL *without* teacher forcing; report RMSE on raw and on 5-cycle-smoothed truth (regeneration is noise at multi-step) | Exposes the recursive-lag illusion; H>1 direct heads are the honest forecasting test. |
| **C. RUL** | same as B | distribution over cycles until EOL. Start points: **fixed-cycle** (NASA 50/100; CALCE 200/400; Toyota 100 — these are the deployable ones, lead with them) **and** %-of-life λ ∈ {0.3, 0.5, 0.7} (literature-comparable, but they leak life length — say so) | The actual business question. Two estimators compared: (a) first-crossing of the forecast trajectory, (b) direct RUL head. Censored cells handled explicitly. |

Never mix tasks in one table. `PROTOCOL.md` is written and reviewed before any sweep runs.

### 6.2 Splits (ADR-0004)
- **NASA, CALCE:** leave-one-cell-out (LOCO) across the 4 cells (the paper's 3-fold CV is dropped). **Hyperparameters are tuned on Toyota** (large) and the chosen config is transferred to NASA/CALCE, with only early stopping on one inner held-out training cell — this avoids winner's curse at n=4 and is a defensible interview answer. (Nested LOCO on the 3 training cells is run once as a sanity check that the Toyota-chosen config isn't pathological.) Repeat every configuration with **5 seeds**. Report per cell and mean ± 95 % cluster-bootstrap CI over cells (it will be wide — say so; this is *why* Toyota is included).
- **Toyota:** Severson official train / primary-test / secondary-test split (literature-comparable) **plus** 5-fold GroupKFold by cell for CIs; 3 seeds.
- **Transfer:** train on all Toyota cells → (i) zero-shot on NASA/CALCE LOCO test cells, (ii) fine-tune on the LOCO training cells → test. Compare to from-scratch.
- **Scalers fitted on training cells only**, inside the fold; per-cell normalization uses only the first 5 cycles. Unit test: perturb test-cell values → assert no training-time statistic changes.
- **Temporal honesty:** a sample at cycle k may only use data with cycle_idx ≤ k. Unit test on the feature builder asserts no future columns; windowing test asserts the target is never inside the input.
- **Few-shot on the test cell's own first T_p cycles** is legal (it's before T_p) and is one of the transfer conditions.

### 6.3 Metrics (`eval/metrics.py`)
- Capacity/SOH: RMSE, MAE **in %SOH and Ah (physical units, never normalized units)**, per-horizon.
- RUL: absolute error (cycles) and relative error at each start point; **α-λ accuracy** (α = 0.2, λ ∈ {0.3, 0.5, 0.7}) — the standard prognostics metric (Saxena et al. 2008); prognostic horizon; early/late bias; censored cells handled (test cases for no-crossing).
- Probabilistic: PICP & MPIW at 90 %, pinball loss (q=0.05/0.25/0.5/0.75/0.95), CRPS (validated against `properscoring`), quantile monotonicity check.
- Stats (`eval/stats.py`): cluster bootstrap over cells for CIs; paired comparisons on (cell, T_p, seed) tuples — Wilcoxon signed-rank on Toyota (40+ test cells, meaningful); on NASA/CALCE show per-cell paired dot plots and report "direction consistent in k/4 cells" rather than p-values; aggregate across datasets by **mean rank** (Demšar 2006). Multiple-comparison note in the report. Every run logs git SHA, resolved config, config hash.

### 6.4 Method ladder (equal tuning budget each — ADR-0006)
Every neural model is tuned with Optuna on Toyota: **same trial count (50; raise to 100 if time allows), same early-stopping rule, same seeds, LR log-uniform in [1e-4, 1e-2], model size capped by a shared parameter budget** rather than per-model grids; trials run in parallel across cores (Section 8). Ordered from trivial to strong; all are mandatory for credibility.

| # | Model | Role | Owner model for implementation |
|---|---|---|---|
| 0 | Persistence (SOH_{k+h} = SOH_k); last value + mean slope of last 10 cycles | sanity floor — exposes whether one-step metrics are trivial | Sonnet |
| 1 | Parametric fits extrapolated from history: linear, double-exponential (He et al. 2011), power law | classical prognostics; strong on smooth fade with few cells | Sonnet |
| 2 | GPR with composite kernel (linear + Matérn; optional periodic) on SOH history (Richardson et al. 2017) | reference for calibrated UQ on NASA | Sonnet |
| 3 | ElasticNet and LightGBM on hand-crafted features (Severson 2019 set: var/min of ΔQ(V), fade slope/intercept, CC/CV times, IC peak location/height, T_max, resistance), direct multi-horizon + direct RUL | what practitioners deploy; **reproducing Severson's ~9 % cycle-life test error on Toyota is a milestone in its own right** | Sonnet |
| 4 | NLinear / DLinear / RLinear (Zeng 2023) | the "linear beats Transformers" check — non-negotiable | Sonnet |
| 5 | LSTM (GRU as config flag), direct multi-horizon | paper's baseline | Sonnet |
| 6 | Vanilla time-token Transformer encoder | paper's baseline; continuity | Sonnet |
| 7 | PatchTST (Nie 2023) | channel-*independent* foil to iTransformer's channel-*mixing* thesis; if PatchTST ≈ iTransformer, the multivariate-attention story is dead | Sonnet (spec from Opus) |
| 8 | **iTransformer** (clean re-implementation, ~150 lines; official repo is MIT — reference, don't vendor), SC and MC variants | paper's method | Opus writes/reviews core; Sonnet tests |
| 9 | **iTransformer-v2** = iTransformer + voltage-grid/ICA/ΔQ(V) features + direct multi-horizon & RUL quantile heads + CQR + Toyota pre-training | the project's contribution | Opus |
| 10 | Blend: mean of GBM + NLinear + iTransformer-v2 medians (+ 5-seed deep ensemble) | often the best entry on small data; costs nothing | Sonnet |
| opt. | Chronos-Bolt-small zero-shot (runs on CPU in seconds) | "no training" reference point; include only if Phase 4 finishes early | Sonnet |

### 6.5 Improvements to explore (each is an experiment with a pre-registered hypothesis; keep what wins)
| Improvement | What | Why it should help | How validated | Est. cost |
|---|---|---|---|---|
| A. Direct multi-horizon **quantile** head + **CQR** (highest value, lowest cost) | One forward pass → SOH at horizons 1..H and RUL, pinball loss at q ∈ {0.05, 0.25, 0.5, 0.75, 0.95} (MQ-RNN/TFT style), wrapped with Conformalized Quantile Regression (Romano 2019) calibrated on the inner held-out training cell | Removes compounding recursive error; distribution-free coverage guarantee; defensible in interviews | Recursive vs direct at every T_p; reliability diagrams; PICP/MPIW/CRPS table. Secondary UQ: 5-seed deep ensemble (epistemic); GPR as reference. **Skip MC-dropout** (poorly calibrated, well documented) | 1 day |
| B. Physics-informed curve features | Voltage-grid resampling (64 pts) replacing 10 uniform-in-time points; ICA dQ/dV (Savitzky-Golay) peak position/height; CC time, CV time, time-to-4.2 V, charge throughput; cycle-to-cycle ΔQ(V); rolling SOH stats | The paper's downsampling discards the aging signatures the literature shows are most informative (SEI growth, LAM); voltage-grid features are what make transfer across protocols possible | Ablation `paper10` vs `vgrid` vs `vgrid+ICA` on LightGBM *and* iTransformer, Tasks A and B | 1 day (NASA sampling is irregular) |
| C. Toyota pre-training → transfer | Pre-train iTransformer-v2 on 124 LFP cells (~100k cycles) with chemistry-agnostic inputs (SOH fraction, ΔQ(V) on a voltage grid, normalized CC/CV durations, temperature stats); conditions: scratch-LOCO / zero-shot / fine-tune (head-only vs full) / few-shot on the test cell's first T_p cycles | n=4 cannot train a Transformer; LFP→LCO/NMC transfer is the genuinely interesting scientific question; gives a sample size where HPO and significance mean something. State caveats: LFP's flat voltage plateau; Toyota charge protocols vary | 4 conditions × 5 seeds on NASA/CALCE LOCO | 1–2 days (Toyota preprocessing dominates) |
| D. Joint multivariate rollout (tests the paper's thesis honestly) | Inverted attention emits a future for *every* variate token → forecast the exogenous channels jointly and roll forward with no measured future features | This is the one experiment that actually tests "channel interactions help forecasting" | Joint-rollout vs direct head (A) vs encoder-only exogenous use | 0.5 day |
| E. Input normalization | Per-cell first-5-cycle SOH normalization vs train-set global scaling vs RevIN | Non-stationarity across cells; RevIN is standard in LTSF | Ablation | 0.5 day |
| F. Loss | MSE vs Huber vs pinball (for A) | Regeneration spikes are outliers | Ablation | 0.25 day |

Decision rule for keeping an improvement: it must improve the primary metrics (RUL α-λ accuracy at the fixed-cycle start *and* H=50 SOH RMSE) on Toyota with CI excluding zero **and** be direction-consistent on ≥ 3/4 cells in both NASA and CALCE LOCO. Negative results are reported, not deleted. **Pre-register** the hypothesis for each ablation in its ADR before running it.

---

## 7. Phases, tasks, owners, gates

Owner key: **O** = Opus 5.5 (lead or Opus subagent), **S** = Sonnet 5.5 subagent. `∥` = tasks in a wave run in parallel (use `isolation: "worktree"` for code-writing agents; lead merges). Durations are laptop wall-clock with parallel agents.

### Phase 0 — Bootstrap (½ day) — O leads
- Install `gh` (ask owner to run `! brew install gh && gh auth login`), `git init`, create `anuragjha/battery-rul` public repo.
- `uv init`, pin 3.12, add deps: torch (CPU index for CI), numpy, pandas, polars, pyarrow, h5py, scipy, scikit-learn, lightgbm, optuna, mlflow, hydra-core, pandera, pydantic, typer, matplotlib, gradio, huggingface_hub, onnx + onnxruntime; dev: pytest, hypothesis, properscoring, ruff, mypy, pre-commit, nbstripout.
- Skeleton from Section 4, `Makefile`, pre-commit (ruff), CI workflow (lint + unit tests), ADR-0001/0002/0003.
- `scripts/bench_cpu_vs_mps.py`: time a 2-layer d=64 Transformer on 1k samples, CPU(1 thread)/CPU(all)/MPS → ADR-0007 (compute strategy).
- **Gate:** CI green on an empty-ish package; `uv run battery-rul --help` works.

### Phase 1 — Data acquisition & canonical loaders (1–2 days) — Wave of 3 S agents ∥, O reviews
- ∥ S: `nasa.py` (mat → cycles/curves parquet, explicit charge→discharge pairing).
- ∥ S: `calce.py` (xlsx ingestion, file ordering, capacity integration, dedupe).
- ∥ S: `toyota.py` (h5py streaming per batch, batch corrections, memory ≤ 8 GB).
- Each agent gets: the schema contract, a tiny fixture to write tests against, and acceptance tests (row counts per cell, monotonic cycle_idx, SOH in [0.5, 1.1], no NaNs in required cols).
- O: reviews pairing/EOL logic for leakage; writes `download.py` checksums.
- **Gate:** `make data` builds all three parquet sets; schema tests pass; cell counts match literature (NASA 4, CALCE 4, Toyota ≈ 124 after corrections).

### Phase 2 — EDA & data-quality report (1 day) — S builds plots, O interprets
- Capacity curves, regeneration events, charge-curve evolution, ICA peaks, EOL under each rule, cross-dataset SOH distributions.
- Output: `reports/data_quality.md` + figures, ADR-0005 (EOL rule & thresholds).
- **Gate:** owner skims the report; EOL cycles per cell frozen in `configs/data/*.yaml`.

### Phase 3 — Evaluation harness FIRST (1–2 days) — O designs, S implements ∥
- O: writes `PROTOCOL.md` (tasks, splits, start points, leakage rules, metrics, stats, equal-budget tuning) → ADR-0004/0006. Owner reviews it (gate marked "owner").
- ∥ S: `tasks/*.py` label construction + leakage unit tests.
- ∥ S: `splits/*.py` + `eval/metrics.py` with hand-computed test vectors.
- ∥ S: `train/runner.py` + MLflow logging + `eval/report.py` (tables/figures from MLflow).
- **Gate:** running the benchmark with the Persistence model end-to-end produces a results table and MLflow runs for all 3 datasets. *Nothing deep-learned exists yet — by design.*

### Phase 4 — Baseline ladder (2 days) — Wave of 4 S agents ∥
- ∥ S: models 0 + 1 + 2; ∥ S: model 3 (ElasticNet/LightGBM + Severson features; target: reproduce ~9 % cycle-life error on Toyota's official split); ∥ S: model 4 (N/D/RLinear); ∥ S: models 5 + 6 (LSTM, Transformer) + `train/trainer.py`.
- O: reviews the `Model` protocol conformance; runs the Optuna sweep for all baselines overnight (parallel workers).
- **Gate:** Table 1 (all baselines × 3 datasets × 3 tasks) generated; Severson reproduction within a few pp; **persistence vs the paper's claimed MC RMSE band documented**; ADR-0008 records any surprising baseline strength (e.g., if LightGBM/NLinear ≈ Transformers — say so).

### Phase 5 — iTransformer & PatchTST (2 days) — O core, S periphery
- O: `itransformer.py` (variate tokens, inverted attention, layer norm per variate, FFN, projection; SC + MC variants; multi-horizon + RUL + quantile heads; joint-rollout mode). S: PatchTST per spec; S: shape tests, "overfit one batch to ~0 loss" wiring test, CPU determinism test for both.
- Tune with the same budget. **Gate:** Table 1 complete for models 7–8; paper-style single- vs multi-channel comparison *under the honest protocol* (Task A vs Task B separately) reported.

### Phase 6 — Improvements A–F (3–4 days) — mix
- ∥ S: curve features (B) + tests; ∥ S: UQ module (A: quantile + CQR + ensemble) + calibration plots; ∥ S: normalization/loss ablations (E, F) as configs; S: blend model (10).
- O: direct/quantile heads wiring (A), joint rollout (D), Toyota pre-training/transfer (C), reads every ablation result and writes ADR-0009…0014.
- **Gate:** iTransformer-v2 config frozen; decision rule from 6.5 applied and documented.

### Phase 7 — Final benchmark, statistics, report (1–2 days)
- O: runs the full frozen benchmark (all models × datasets × tasks × seeds) from one `configs/experiment/final.yaml`; S: `reports/results.md`, figures (forecast overlays with intervals per cell, α-λ plots, reliability diagrams, transfer bars), README tables.
- O: writes the honest narrative: what improved, by how much, with CIs; what didn't.
- **Gate:** every number in README maps to an MLflow run ID; `make bench` reproduces Table 1 from scratch.

### Phase 8 — Packaging & deployment (2 days) — S builds, O reviews
- S: `serve/predictor.py` + input contract (CSV columns: `cycle_idx, capacity_ah[, charge_time_s, …]`; or raw curve long-format matching `data/schema.py`) with pydantic/pandera validation and clear error messages; **OOD score** (Mahalanobis distance on the feature vector + conformal interval width) that triggers a visible "outside training distribution — RUL unreliable" warning; `scripts/export_weights.py` → ONNX/TorchScript (no MPS code in the serving path) → HF Model repo `anuragjha/battery-rul-itransformer-v2`.
- S: `app/gradio_app.py`: upload CSV or pick demo cell (one per dataset) → SOH estimate, forecast plot with 90 % band, RUL distribution (point + interval), EOL threshold slider, model selector (v2 vs LightGBM vs blend), OOD banner, "how to format your data" tab. Must run in ≤ 2 vCPU / 16 GB; cold start < 30 s. RUL for unseen chemistries/protocols is unreliable — the UI says so.
- S: `deploy-space.yml` (push `app/` + weights ref to the Space on git tag), `pyproject` publishable; O: smoke-tests the live Space.
- **Do this gate early in Phase 8 (free-tier risk):** a hello-world Gradio Space deploys from the owner's HF account.
- **Gate:** public URL works for a stranger with the example CSV; README "Try it" link.

### Phase 9 — Docs & defensibility (1 day)
- ADR index, model card (intended use, data, metrics, limitations, chemistry caveats), `CONTRIBUTING.md`, architecture diagram, and `docs/interview_notes.md`: 10 likely interview questions with answers grounded in ADRs (e.g., "why not just LightGBM?", "how do you know there's no leakage?", "what did the Transformer actually buy you?").

**Total:** ~13–16 working days of wall-clock with parallel agents.

---

## 8. Maximizing the M4 Pro

- **Parallelism model (measured, ADR-0007 — supersedes the original CPU-first assumption):** one Optuna study per (model, task) backed by **`JournalStorage`** (file-based; robust under concurrent writers), TPE sampler + Hyperband pruner. **Neural models: 4 concurrent MPS worker processes** (`torch.set_num_threads(1)` each) — 4 MPS processes gave 1 687 steps/s at the NASA/CALCE shape vs 657 for the best CPU configuration (10 procs). **Classical models (LightGBM/GPR/sklearn): 4–6 CPU worker processes × 2 threads**, running concurrently on the remaining cores. **Toyota pre-training: one MPS process** (GPU saturates; CPU-parallel collapses from memory-bandwidth contention at that size). fp32 only on MPS; metrics computed in float64 on CPU. `PYTORCH_ENABLE_MPS_FALLBACK=1`.
- **Data loading:** keep datasets as in-memory tensors; **no DataLoader workers** (macOS uses spawn; fork overhead is pure loss at this size).
- **Memory:** cap concurrent workers so RSS < 16 GB total (Toyota per-cycle features are small once extracted; raw `.mat` streaming via h5py peaks < 3 GB and runs once). LightGBM uses `num_threads=2` per trial.
- **Data:** Parquet + polars for feature building; cached per-fold tensors in `data/processed/cache/` keyed by config hash so retuning doesn't rebuild features.
- **Budget estimate:** NASA/CALCE runs are 1–3 min each; ~9 models × 8 cells × 3 start points × 5 seeds ≈ 1 000 runs ≈ 4–6 h with 6 workers. Toyota HPO (50 trials × 9 models) is the other overnight job.
- **Overnight runs:** `make bench` writes to MLflow incrementally; resumable (skip runs whose config hash exists). MLflow backend: `sqlite:///mlflow.db`.
- **Agents:** code-writing subagents run in git worktrees so 3–4 can work at once without conflicts; benchmark processes are started by the lead with `run_in_background` and polled via Monitor, not by subagents.

---

## 9. Subagent delegation policy (for the Opus 5.5 lead)

**Decision rubric — ask these in order for every task:**
1. Is the *spec* already precise (interface + acceptance tests + file paths)? If **no** → Opus writes the spec first (or does the task).
2. Does correctness hinge on subtle judgment (leakage, label construction, statistical reporting, architecture fidelity, interpreting ambiguous results)? If **yes** → Opus.
3. Otherwise → **Sonnet 5.5**, `effort: "lower"` for mechanical work (loaders from a schema, plots, tests, docs, YAML, CI, Gradio UI, refactors, running sweeps and tabulating), default effort for model implementations from a spec.

**Typical split:** Opus ≈ design docs, ADRs, `itransformer.py`, `tasks/rul.py`, `eval/stats.py`, code review of every PR-sized merge, results narrative. Sonnet ≈ everything else (~70 % of code volume).

**Every delegation prompt must contain:** goal; exact file paths to create/modify (and which are off-limits); the interface contract (signatures / schema); acceptance tests to make pass; constraints (Python 3.12, no new deps without listing them, no network except dataset URLs, worktree isolation); and "return: summary of what was built, test output, open questions". Agents never commit; the lead reviews the diff, runs `make lint test`, then commits with a conventional message.

**Parallel waves (max 3–4 concurrent, to keep RAM/CPU for benchmarks):** Phase 1 (3 loaders), Phase 3 (3 harness parts), Phase 4 (4 baselines), Phase 6 (3 ablation streams), Phase 8 (predictor ∥ app ∥ CI).

**Lead cadence:** after each wave → merge, run tests, update `docs/STATUS.md` (what's done, what's next, open risks), commit. Keep the owner informed with a 5-line status at every gate; ask the owner only at gates marked "owner" or when a Fixed Decision (Section 2) seems wrong.

---

## 10. Verification (end-to-end)

1. `make env && make lint && make test` — CI-identical, must be green locally.
2. `make data` → three parquet sets; `uv run battery-rul validate-data` prints cell/cycle counts and passes schema checks.
3. Leakage tests: `pytest tests/test_leakage.py` (scaler-fit-on-train, no-future-columns, EOL label uses no future at inference).
4. `uv run battery-rul benchmark --config configs/experiment/smoke.yaml` (1 seed, 2 trials, tiny) finishes in < 10 min and produces `reports/tables/smoke.md`.
5. `make bench` (full) overnight → `reports/results.md`, README tables regenerated, `mlflow ui` shows all runs.
6. `uv run python app/gradio_app.py` locally → upload `app/examples/nasa_B0005.csv` → forecast + RUL interval rendered; then the live HF Space does the same from a fresh browser session.
7. Fresh-clone test: `git clone … && make env && make test && uv run battery-rul predict app/examples/calce_CS2_35.csv` works on a clean machine (simulate with a new `uv` venv).

---

## 11. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Toyota download requires a browser (JS page) | Owner downloads once manually; loader validates checksums; document in `data/README.md`. |
| HF free CPU tier changed/removed | Deploy a hello-world Space in Phase 8 day 1; fallback Streamlit Community Cloud; app code stays framework-thin (`serve/predictor.py` is UI-agnostic). |
| Results show Transformers ≈ linear/GBM on n=4 cells (**expected**) | This is a *finding*, not a failure: the honest conclusion becomes "the contribution is the features/protocol/UQ, not the architecture". Repo is framed as a benchmark; headline leans on the rigorous protocol, the Severson reproduction, calibrated UQ, and cross-chemistry transfer. Say so in README. |
| Toyota charge-protocol confound | Toyota inputs are discharge-derived (standardized 4C); thesis reframed to "per-cycle curve features" (Section 2). |
| Torch/MPS instability or non-determinism on macOS 26 | `device=auto` falls back to CPU; `PYTORCH_ENABLE_MPS_FALLBACK=1`; 5-seed reporting absorbs MPS non-determinism; smoke benchmark checks a CPU-vs-MPS run pair agrees within seed noise. |
| Scope creep in Phase 6 | Pre-registered hypotheses + decision rule (6.5); time-box each ablation to its estimate ×1.5. |
| CALCE parsing ambiguities | Data-quality report lists every manual rule; unit-test each. |

---

## 12. ADR list to produce (titles)
0001 record decisions · 0002 toolchain (uv/3.12/torch/MLflow) · 0003 config system · 0004 evaluation protocol & splits · 0005 EOL definition & thresholds · 0006 equal-budget tuning · 0007 compute strategy (MPS-first, measured) · 0008 baseline findings · 0009 feature set · 0010 direct vs recursive · 0011 UQ method · 0012 Toyota transfer · 0013 normalization · 0014 final model selection · 0015 deployment target & input contract.
