# ADR-0018: Outlier policy and field-setting inputs

- **Status:** Accepted (2026-11-20). Implementation:
  - `src/battery_rul/data/cleaning.py`, enabled with `ExperimentConfig.clean`;
  - `tasks/samples.py` feature sets `field` / `field_curve`;
  - `features/field.py` and `data/toyota_field.py`.

## Context
Phase 2 (`docs/PLAN_PHASE2.md`) targets the **field setting**: at prediction time only BMS-measurable signals are available, and measured SOH/capacity is a label, never an input. Outliers had been handled ad hoc. Some were label errors that inflated errors and interval widths; others were corrupt inputs.

## Decision 1: two kinds of outlier, two kinds of rule
| Kind | Rule | Causal? | Treatment | NASA | CALCE | Toyota |
|---|---|---|---|---|---|---|
| Label: CV-skip (CALCE charger artifact, cv_time_s < 300 s) | dataset rule | n/a (labels only) | drop the cycle | 0 | 109 | 0 (CV-free policies are protocol, not artifact) |
| Label: partial charge (throughput < 0.5 × local median) | hindsight | n/a | drop | 9 | 20 | 0 |
| Label: isolated one-cycle glitch (neighbours agree, excursion > max(5 × local \|Δ\|, 1 %)) | hindsight | n/a | drop | 0 | 4 | 33 |
| Input: paused charge (charge_time > 3 × median of the cell's *past* cycles) | yes | yes | mask all charge-duration-derived inputs of that cycle | 0 | 0 | 45 |
| Input: physical range (IR, temperatures, relaxation V) | yes | yes | mask | 0 | 0 | 0 |
| Input: robust z (\|x − past-25 median\| > 8 × max(MAD, 2 % of the median)), IR and temperatures only | yes | yes | mask | 11 (T) | 12 (IR) | 13 (IR) |

Masked inputs are forward-filled causally by `prepare_cycles` and flagged in the mask channel.

**Kept as real signal:**
- NASA regeneration. The glitch rule never matches it: 0 of the 20 regeneration cycles are flagged, as checked.
- The Toyota break-in rise (SOH up to 1.008).
- The knee.
- **Toyota CV-time regime switches (625 → 1,260 s).** A statistical rule on durations wrongly flagged 1.6 % of Toyota cycles. Those switches are health information (ρ ≈ −0.47 with SOH), so durations are excluded from the robust rule.

**Tests:** `tests/unit/test_cleaning.py`.
- Regeneration is not flagged.
- Glitches are caught in both directions.
- Input rules are causal: corrupting future cycles never changes earlier masks.

## Decision 2: field inputs (`field`, `field_curve`)
**Allowed:**
- cycle count (owner decision);
- CV time and the CV-skip flag;
- IR;
- log rest;
- charge temperature;
- relaxation voltage: NASA OCV at charge start; CALCE CC→CV rest; Toyota 80 % SOC rest;
- NASA pulse resistance from the −4 A step at charge start;
- fixed-voltage-window charge features (ΔQ and Δt in [3.85, 4.15] V for NASA/CALCE and [3.50, 3.58] V for Toyota; ICA peak);
- `field_curve` adds 15 Q(V) grid points as variates.

**Forbidden** (`FIELD_FORBIDDEN`): capacity, SOH, charge throughput from empty, total and CC charge time, all discharge quantities.

**Enforced by tests:**
- `test_field_inputs_never_read_capacity_derived_columns`: corrupting every forbidden column of every cycle leaves inputs bit-identical.
- `test_field_rule2_no_future_inputs`.

**Window:** field Task A uses the window ending at cycle k. All of cycle k's field signals come from its charge, which precedes the discharge that measures the label.

## Decision 3: models in the field setting
| Model | Field-mode change |
|---|---|
| Neural (all) | Targets are absolute SOH, centred on the training cells' per-horizon mean (a label statistic). |
| iTransformer | Mean-pools all variate tokens (there is no SOH token). The SC variant is undefined. |
| PatchTST | Channel-independent encoder, plus a learned channel-identity embedding and a mean-pool across channels. This is the minimal cross-channel readout. |
| LightGBM / ElasticNet | Inputs: last value, window mean and window change of every channel. |
| Age-only (new) | Monotone isotonic SOH(cycle) on training cells; RUL = median training EOL − age. |

**Dropped** because they are undefined without SOH history: N/D/RLinear, GRU, parametric fits, GPR, persistence.

## Evidence (feature ↔ SOH, Spearman; per-cell median)
- **NASA:** window ΔQ 0.99, ICA height 0.98, relaxation OCV −0.93, CV time −0.88.
- **CALCE:** window ΔQ 0.98, ICA height 0.97, relaxation V 0.95.
- **Toyota:** relaxation V −1.00 per cell (−0.79 pooled); window ΔQ −0.69.
  - The window features are weak on Toyota because of LFP's flat voltage plateau. This is expected physics and reported as such.
- **Regeneration:** window ΔQ and ICA height jump by 3–6× their ordinary change after long rests (NASA, CALCE). So a field estimator can see regeneration as it happens.
