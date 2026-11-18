# Battery RUL, phase 2: a field-realistic study (no SOH history at prediction time)

## Context
The owner is not satisfied with the results, and is right on five points:
1. **Every model relies on lab measurements.** All of them use measured past SOH, i.e. full-discharge capacity, as an input. A real BMS does not have that.
2. **Regeneration is not predicted.** Without the rest schedule, no model forecasts capacity regeneration.
3. **iTransformer is not justified by its own strengths.** It must be justified by what its paper claims (Liu et al., ICLR 2024): variate tokens that model correlations among many variates, and good use of long lookbacks.
4. **Outliers were never systematically cleaned** before training.
5. **Many intervals are too wide to be useful:** NASA h50 is 13–21 % SOH wide; RUL intervals are 75–550 cycles, often wider than the RUL itself.

The goal of this phase is the **field setting**:
- **Inputs:** only BMS-measurable signals plus cycle count (owner decision). Measured SOH or capacity is a training/evaluation label only, never an input.
- **Regeneration:** characterise it and predict it where that is physically possible.
- **iTransformer:** test its paper's claims head-on, and make intervals informative.

Everything is pre-registered (ADRs), reuses the existing infrastructure, and weeds out work that has already failed.

---

## 1. Where we stand (results so far)
**Strong:**
- A leakage-free, equal-budget benchmark: 1,692 runs, 18 configurations, 3 datasets, 5 seeds, CIs, Holm-corrected Wilcoxon, mean rank.
- iTransformer has the best mean rank (3.08). In-distribution on Toyota it leads (h50 0.40 % SOH vs 2.50 for persistence).
- CQR fixes severe under-coverage (NASA 46 % → 90 %).
- Direct heads beat recursive rollout. Honest negative results are recorded (RevIN, Huber, curve features, transfer).
- Infrastructure is reusable end to end: data pipeline, leakage tests, runner/MLflow, stats, ONNX in-browser demo, dashboards, showcase.

**Weak:**
- **(a) Lab-only inputs.** Measured SOH history, discharge quantities, and `charge_throughput_ah` (ρ ≈ 0.99 with SOH, a disguised capacity measurement).
- **(b) Thin evidence on NASA/CALCE.** LightGBM matches or beats iTransformer there; with 4 cells each, the CIs are wide.
- **(c) No regeneration forecasting.** Only the oracle-schedule variant anticipates it, and iTransformer gains least from that schedule (ADR-0016).
- **(d) RUL is weak.** α-λ accuracy is low on NASA/CALCE, long Toyota lives are under-predicted, and CALCE is pessimistic.
- **(e) Uninformative intervals** on NASA/CALCE, and coverage fails under shift (Toyota test2).
- **(f) Lookbacks were only searched in {16, 32, 64}**, so iTransformer's long-context strength was never exercised.
- **(g) Outlier treatment was ad hoc.**
  - CALCE CV-skip dips stay in targets and inputs.
  - 45 Toyota charge-pause cycles (charge time up to 179,653 s) enter models unclipped beyond z = ±5.
  - The NASA cycle-31 8 V spike is untreated.
  - There are 154 Toyota Tdlin and 1,258 Qdlin garbage samples.

## 2. Why charge features were limited, and the full feature inventory
**Charge features were not absent.** NASA and CALCE used CC/CV/total charge time, throughput, IR, temperatures, rest and the CV-skip flag; these were the paper's "multi-channel" inputs. Charge *curves* were limited for three reasons:
1. **The original protocol assumed SOH history was available,** as the paper did. Under that assumption, curve features added nothing (ADR-0009).
2. **Toyota charge curves were deliberately excluded** (PLAN §2). The charge protocol is Toyota's experimental variable (72 fast-charge policies), so curve shape encodes the policy, and through it the cycle life. The standardised 4C discharge was used instead, but that is a lab measurement.
3. **Relaxation-voltage and pulse-resistance signals were never extracted.** In hindsight this was an oversight: they are the best-documented field SOH signals (Zhu et al., *Nat. Commun.* 2022).

| Feature | NASA | CALCE | Toyota | BMS-measurable? | Field decision and reason |
|---|---|---|---|---|---|
| capacity / SOH history | ✓ | ✓ | ✓ | no (full discharge) | **Label only.** It is the quantity we must infer. |
| discharge time / energy / Q(V) curves (`dis_*`, Severson ΔQ) | ✓ | ✓ | ✓ | no | **Drop.** Near-copies of capacity. Kept only in the "lab reference" results. |
| charge_throughput_ah | ✓ | ✓ | ✓ | only for a full charge from empty | **Drop.** ρ = 0.89–0.99 with SOH: a capacity measurement in disguise. |
| charge_time_s, cc_time_s | ✓ | ✓ | ✓ | depend on starting SOC | **Drop.** Replaced by fixed-voltage-window features. |
| cv_time_s (+ skipped_cv flag) | ✓ | ✓ | ✓ (protocol-common 1C CC-CV at 3.6 V) | yes, if the charge reaches CV | **Keep.** |
| Fixed-window charge features (ΔQ and Δt between V1 and V2, ICA peak v/h/area) | ✓ (`chg_*`, 3.80–4.19 V) | ✓ (80 % of cycles) | to extract: common final 1C segment | yes; works from a partial charge | **Keep.** Core field health signal. |
| Voltage-grid Q(V) points inside the window (16–32 variates) | ✓ (curves table) | ✓ | to extract | yes | **Keep as many-variate input.** This tests iTransformer's claim 1. |
| Relaxation voltage | to extract: OCV at charge start after rest | to extract: 90 s rest between CC and CV, 4.12 → 4.10 V | to extract: 60 s rest at 80 % SOC, 3.47 → 3.30 V | yes | **Add.** Strongest literature signal; also reflects regeneration. |
| Pulse / DC resistance | to extract: −4 A pulse at charge start | Arbin IR (periodic) | summary IR | yes | **Keep / add.** NASA EIS IR is a lab test and is replaced by the pulse resistance. |
| Rest before cycle (log) | ✓ | ✓ | – (not logged) | yes (timer) | **Keep.** Drives regeneration. |
| Temperature | charge T ✓ | – (no sensor) | raw charge T (to extract), summary Tmax | yes | **Keep** as a stress covariate where present. |
| Cycle count | ✓ | ✓ | ✓ | yes | **Keep** (owner decision), plus an age-only baseline. |
| Toyota policy id, NASA EIS Re/Rct, CALCE AC impedance | | | | no / lab / all zero | **Drop.** |

## 3. Regeneration: what it is and what can be predicted
**Facts (EDA so far):**
- **NASA:** real regeneration. +3.1 % SOH after each rest longer than 6 h (20 events).
- **CALCE:** mostly the CV-skip artifact. True rest recovery is only +0.8 %.
- **Toyota:** no logged rests.

**Mechanisms (literature):**
- Lithium redistribution into and out of the anode overhang during rest.
- Relaxation of plated lithium.

**Real-world relevance:**
- Rest-induced recovery is documented in intermittent-use (non-lab-cycled) systems, sometimes larger and more persistent than in lab cycling. It masks the true SOH.
- No direct EV-fleet evidence was found. The demo and README will state this honestly.

**What is predictable:**
- **(i) At the moment it happens.** Relaxation voltage, resistance and rest duration are all measurable, so a field SOH estimator can see a regeneration as it occurs.
- **(ii) Ahead of time, only with the planned rest schedule.** ADR-0016 showed this works for LSTM, the time-step Transformer and LightGBM.
- **(iii) Not from history alone.**

**The iTransformer fix:**
- It gained least from the schedule because the schedule entered as one tabular token.
- Fix: feed rest duration as a **variate token whose window spans past and planned-future cycles**. This is the natural iTransformer way to take known future inputs, and costs one code change.

## 4. Intervals too wide: diagnosis and mitigation
**Measured:**
- Calibrated width is 2.5–4× RMSE (≈ 3.3× is the Gaussian-consistent value), so CQR is not inflating artificially. Widths are large because the errors are large and heteroscedastic.
- A single constant correction per horizon over-widens mid-life and under-widens early life and regeneration cycles.
- **Uninformative today:**
  - NASA h50 widths: 13–21 % SOH (h100 up to 60).
  - CALCE h50: ~9–12 % SOH.
  - RUL at start points: NASA 75–90 cycles (true RUL 30–90), CALCE 240–430, Toyota 390–2,600.
- Already narrow and useful: Toyota forecasts (0.5–1.5 % SOH at h50).

**Mitigation, in order of value:**
1. **Post-hoc, no retraining.** These reuse the stored `inner_val_predictions` and `predictions` of all existing runs.
   - Locally adaptive CQR: Mondrian bins on life stage / history length, plus scaled (multiplicative) CQR.
   - RUL conformal in relative (log) space.
   - Exclude label-outlier residuals from calibration.
   - Pre-registered target: keep 0.90 ± 0.05 marginal coverage, plus ≥ 0.85 in every life-stage bin, with ≥ 20 % narrower mean width.
2. **Narrow at the source.** Fewer errors from outlier cleaning, field signals and long lookbacks (Stages 1–3).
3. **Report informativeness.**
   - New metric: width ÷ (SOH − 80 %) remaining, plus the share of predictions that are "useful" (width < 50 % of the distance to EOL).
   - Dashboards hatch and label uninformative bands instead of presenting them as meaningful.
   - NASA/CALCE claims are stated as 4-cell results.

## 5. Reuse (no retraining)
- **All infrastructure:** data pipeline, splits, leakage tests, runner + MLflow resumability (identical config hashes skip), stats/`compare_arms.py`, `calibrate`, report, showcase/dashboards, ONNX/web, `future_rest` covariate code.
- **The 1,692 benchmark runs and all ablations** become the **lab reference ("SOH history available")** in every new table. No reruns.
- **Their stored predictions** are reused for interval-method work (§4.1) and for the "lab vs field" gap.
- **Tuned hyperparameters** (`configs/tuned/*.yaml`) are reused per model family for field models. There is no new tuning; lookback and feature set are the studied factors, and every model is treated equally.
- **Existing code:** `features/curves.py` (window ICA/ΔQ features), `models/itransformer.py` (variate tokens), `tasks/samples.py` feature sets, `data/quality.py` flags.

## 6. Dropped (unpromising or already settled)
- **Settled:** Toyota → NASA/CALCE transfer (ADR-0012), RevIN/Huber (0013), recursive rollout (0010), deep ensembles (5× cost for +2/40), Severson discharge features (lab-only).
- **Not defined without SOH history:** N/D/RLinear, GRU, parametric fits and GPR (they extrapolate the SOH series itself). Persistence is replaced by **age-only** (SOH vs cycle count, fitted on training cells) and **signal-only LightGBM/ElasticNet** baselines.
- **Hyperparameter re-tuning** (equal-budget rule, reuse instead).
- **New datasets.**

---

## 7. Plan, staged with gates
**Owner decisions (2026-11-18):**
- Inputs are field signals plus cycle count, with an age-only baseline.
- Re-extract the Toyota charge-side signals.

### Stage 0: EDA, cleaning, field features (no model training except probes). Lead: Opus. Sonnet agents for extraction and plots.
- **0a. Outlier taxonomy and policy (ADR-0018)**, implemented in a new `data/cleaning.py` with tests.
  - **Label outliers** (hindsight allowed, labels only): CALCE CV-skip capacity (drop as target), NASA partial-charge cycles 1/31/46/56 (drop), Toyota Qdlin ≈ 0 cycle (drop).
  - **Input outliers** (causal rules only: robust z against the cell's own past median): Toyota charge-pause cycles (mask charge-time-derived inputs), NASA cycle-31 voltage spike, Toyota Tdlin/Qdlin garbage samples (mask), IR NaNs (forward fill).
  - **Kept as real signal:** NASA regeneration, the Toyota break-in rise (SOH > 1 up to 1.008), the knee.
  - **Tests:** detectors use only past data (perturbation test); counts reproduced.
- **0b. Field feature extraction** (`features/field.py`):
  - NASA: OCV at charge start, pulse resistance.
  - CALCE: CC→CV rest relaxation ΔV and end voltage.
  - All datasets: fixed-window ΔQ/Δt and 16–32 Q(V) grid variates.
  - Toyota (approved): stream the raw batches once, extracting the final 1C CC-CV segment window, the 80 % SOC rest relaxation and charge temperature. One-off, ~1–2 h unattended, run by a Sonnet agent against a precise spec.
- **0c. New feature sets** `field` (scalars + cycle count) and `field_curve` (+ Q(V) variates).
  - Leakage tests: corrupting capacity, SOH, discharge, throughput or charge/CC time of *every* cycle leaves all inputs bit-identical. Future-input rules are unchanged.
- **0d. EDA report** (`reports/eda_field.md` + a showcase section):
  - signal availability matrix;
  - Spearman correlation and mutual information of each field signal with SOH per dataset, and their cross-dataset consistency;
  - regeneration characterisation: jump vs rest duration (regression), decay half-life over the following cycles, which field signals move at regeneration cycles;
  - outlier counts before and after cleaning.
- **0e. Probes, cheap (minutes):**
  - LightGBM field SOH estimation per dataset vs the age-only baseline.
  - Interval-method rescoring on the existing runs (§4.1). It writes ADR-0019 immediately.
- **Gate (owner):**
  - EDA report reviewed.
  - Datasets where field signals do not beat age-only are reported and deprioritised.

### Stage 1: Field SOH estimation screen (the "virtual SOH sensor", foundation of everything)
- **Design:**
  - Task F-A: SOH at cycle k from field inputs of cycles ≤ k.
  - Models: iTransformer (MC), PatchTST, time-step Transformer, LSTM, LightGBM, ElasticNet, plus the age-only baseline.
  - Feature sets: {`field`, `field_curve`}. L = 64. 3 seeds; NASA/CALCE LOCO, Toyota official split (train stride 4).
- **Size:** 6 × 2 × 9 units × 3 = **324 runs**, about 1.5 h.
- **Pre-registered (claim 1 of the iTransformer paper):** iTransformer gains most from `field` → `field_curve`, i.e. from many correlated variates, more than PatchTST (channel-independent), LSTM, Transformer and LightGBM.
- **Gate:** pick each model's feature set.

### Stage 2: Long-lookback test (claim 2; the attention-vs-RNN question)
- **Design:**
  - Tasks F-A and F-B (h = 50 forecast from field inputs).
  - L ∈ {32, 128, 512}. Models: iTransformer, time-step Transformer, PatchTST, LSTM.
  - CALCE (4 cells) and Toyota (official split), with the best feature set from Stage 1. 3 seeds.
  - NASA is excluded: cells of 132–168 cycles cannot support long windows.
- **Size:** 3 × 4 × 2 × 5 units × 3 = **360 runs**.
- **Required fix:** the parameter cap. `itransformer.py:188` silently exceeds 250k at L = 512 (the embedding is (L+2)·d). Make it fail loudly or shrink d.
- **Pre-registered:** iTransformer error falls monotonically with L. The time-step Transformer and LSTM plateau or degrade. Tested by paired Δ (L=512 vs L=32) with CI.

### Stage 3: Final field benchmark + regeneration (5 seeds)
- **Main grid:** tasks F-A, F-B (h = 1…100/200), F-C (RUL); 6 models + age-only, each at its Stage 1–2 configuration.
  - Seeds 0–2 already exist from the screens and are skipped by config hash, so only seeds 3–4 and new tasks run.
  - **≈ 600 new runs.**
- **Regeneration arm:**
  - F-B with the planned rest schedule on NASA/CALCE: iTransformer with a **past+future rest variate token** (new), versus LSTM/Transformer/LightGBM with `future_rest` (existing code).
  - **≈ 160 runs.**
  - Pre-registered: the new token closes iTransformer's gap. Regeneration-cycle error reduction ≥ LSTM's 26 % (h = 1).
- **Afterwards:**
  - CQR plus the Stage 0e adaptive method on all runs.
  - Paired comparisons, field vs lab gap tables.
  - **ADR-0020:** field results.
  - **ADR-0021:** iTransformer justification verdict, positive or negative, reported either way.

### Stage 4: Deliverables
- Showcase "field setting" section: EDA, regeneration, iTransformer claims, lab-vs-field gap.
- Dashboards gain a field mode: method comparison over held-out cells, informativeness badges on intervals.
- If a field model is adopted:
  - retrain the deployed model on field inputs (`train_deploy.py`, < 2 min) and export to ONNX;
  - change the demo's input contract to a signal CSV (cv_time, rest, resistance, window ΔQ/Δt, temperature, cycle count);
  - port the extra field features to JS with a parity test.
- README, model card, interview notes (Phase 9).

**Compute:** about 1,450 new runs in total, similar to the original benchmark, about 8–10 h on 4 MPS workers plus CPU for LightGBM.

**Delegation:**
- **Opus:** cleaning policy, leakage rules, ADRs, statistics, the iTransformer token change, interpretation.
- **Sonnet:** extraction, plots, EDA tables, dashboard work, each against a precise spec.
- Parallel waves of up to 3 agents in worktrees; no merges into main while sweeps run.

## 8. Critical files
- **New:** `src/battery_rul/data/cleaning.py`, `src/battery_rul/features/field.py`, `configs/experiment/field_{screen,lookback,final,regen}.yaml`, `docs/decisions/0018–0021`, `reports/eda_field.md`.
- **Modified:**
  - `tasks/samples.py`: `field` / `field_curve` feature sets; cleaning hooks.
  - `models/itransformer.py`: parameter-cap fix; known-future variate token.
  - `data/toyota.py`: charge-side extraction, if approved.
  - `uq/conformal.py`: Mondrian / scaled CQR, relative RUL.
  - `tests/unit/test_leakage.py`: field-input rules.
- **Reused as is:** runner, report, `scripts/compare_arms.py`, `uq/calibrate.py`, `features/curves.py`, `scripts/make_demo_compare.py`, web dashboards.

## 9. Verification
- `make lint typecheck test` green, including the new leakage and cleaning tests (mutation-checked: an injected capacity leak must be caught).
- Default configs keep their unit keys, so the lab benchmark stays reproducible.
- Each stage gate produces paired tables with CIs from MLflow run IDs.
- Interval methods must show marginal coverage of 0.90 ± 0.05 and per-bin coverage ≥ 0.85.
- Dashboards are screenshot-checked. JS/Python parity tests are extended to the new field features before deploy.
