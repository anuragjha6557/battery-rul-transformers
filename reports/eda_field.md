# Field-setting EDA (PLAN_PHASE2 Stage 0)

Scope: what a real BMS can measure, the outliers and how they are treated, what drives capacity regeneration, and whether field signals carry health information. Decisions live in ADR-0018 (outliers, inputs) and ADR-0019 (intervals).

## 1. Signal availability (field-measurable only)
| Signal | NASA | CALCE | Toyota | Notes |
|---|---|---|---|---|
| Cycle count | ✓ | ✓ | ✓ | Owner decision: allowed |
| CV time (+ CV-skip flag) | ✓ | ✓ | ✓ | Toyota CV is timer-bounded and switches regime with age |
| Internal resistance | EIS (lab) → **pulse R** at charge start | Arbin IR (periodic) | summary IR | |
| Rest before cycle | ✓ | ✓ | – (not logged) | Drives regeneration |
| Relaxation voltage | OCV at charge start after rest | 90 s rest between CC and CV | rest at ~80 % SOC, read at a fixed 8 s | Toyota test2 rests only ~10 s, hence the fixed-time read |
| Fixed-window charge ΔQ, Δt, 15 Q(V) points, ICA peak | 3.85–4.15 V, 94.8 % of cycles | 3.85–4.15 V, 87.2 % | 3.50–3.58 V, 92 % | Works from a partial charge (coulomb count inside a voltage band) |
| Charge temperature | ✓ | – | ✓ (raw charge T) | |
| **Forbidden** | capacity, SOH, throughput from empty, total/CC charge time, all discharge quantities | | | Leakage-tested |

## 2. Outliers (ADR-0018)
| | NASA | CALCE | Toyota |
|---|---|---|---|
| Label outliers dropped (CV-skip / partial charge / one-cycle glitch) | 0 / 9 / 0 | 109 / 20 / 4 | 0 / 0 / 33 |
| Input values masked (paused charge / robust z on IR or T) | 0 / 11 | 0 / 12 | 45 / 13 |
| Kept as real signal | regeneration (0 of 20 flagged) | rest recovery | break-in rise, CV-time regime switches |

**A rule we rejected and why:** a statistical rule on durations flagged 1.6 % of Toyota cycles. These were CV-time jumps from 625 to 1,260 s as cells reach 3.6 V earlier inside a fixed charge timer. That is health information (ρ = −0.47 with SOH), so durations get only the paused-charge and physical-range rules.

## 3. Do field signals carry health information? (Spearman ρ with SOH, per-cell median)
| Feature | NASA | CALCE | Toyota |
|---|---|---|---|
| Window ΔQ | 0.99 | 0.98 | −0.69 |
| ICA peak height | 0.98 | 0.97 | −0.49 |
| Relaxation voltage | −0.93 (OCV) | 0.95 | −1.00 (pooled −0.79) |
| CV time | −0.88 | −0.76 | 0.24 |
| Pulse / IR resistance | −0.32 | n/a | – |

LFP (Toyota) has a flat voltage plateau, so a narrow top-of-charge window carries less information. Relaxation voltage is its strongest field signal.

## 4. Capacity regeneration
| | NASA | CALCE |
|---|---|---|
| Events (rest > 1 h) | 35 | 69 |
| Jump vs log10(rest hours) | **+1.66 % SOH per decade** (r = 0.65, p = 3e-5) | **+1.55 % per decade** (r = 0.43, p = 2e-4) |
| Mean jump: rest 1–6 h / 6–24 h / > 24 h | 1.1 / 2.3 / 3.8 % | 0.2 / −0.1 / 1.7 % |
| Persistence (excess over pre-rest trend) | about +1 % still at +5 and +10 cycles (long-lived) | fades in 1–2 cycles |
| Field signals at the regeneration cycle | window ΔQ jumps by +0.027 Ah (6× the ordinary change); ICA height +0.55; relaxation OCV +0.23 V; pulse R +5 mΩ | window ΔQ +0.017 Ah (17×); ICA height +0.20; relaxation V +2.5–4.9 mV |

**Interpretation:**
- Regeneration follows a consistent law: its size grows with the log of the rest duration. It is the behaviour expected from lithium redistributing (anode overhang) or plated lithium relaxing during rest.
- It is visible in measurable charge signals on the cycle where it happens. So a field estimator can track it, and a forecaster can anticipate it when the rest schedule is known (ADR-0016).
- It is not only a lab effect. Rest-induced recovery is reported in intermittent-use systems and can mask true SOH. We found no direct EV-fleet study, and say so.

## 5. Distribution shift between Toyota batches
At equal SOH (0.93–0.95), test2 (batch 2018-04-12) differs from train/test1:
- the rest at 80 % SOC is 10 s instead of 61 s;
- CV time is 348 s instead of 716 s;
- charge temperature is 34.8 °C instead of 31.4 °C;
- IR is 15.5 mΩ instead of 17.5 mΩ.

**Effect on the field probe (LightGBM SOH RMSE, % SOH):**
- Relaxation read at the end of the rest: 4.11, worse than age-only (3.67).
- Read at a fixed 8 s: 2.45.
- Lab reference (with SOH history): 0.02.

**Lesson:** BMS signals depend on the charging protocol and environment. A deployed field model must be trained on the target protocol or guarded by OOD detection. Tree models degrade far less than linear ones (ElasticNet 5.70).

## 6. Field probe: SOH estimation without any capacity input (1 seed)
| RMSE % SOH | CALCE | NASA | Toyota test1 | Toyota test2 |
|---|---|---|---|---|
| Age-only | 6.89 | 5.85 | 4.01 | 3.67 |
| LightGBM (field) | 4.58 | 4.00 | 0.97 | 2.45 |
| ElasticNet (field) | 4.70 | **2.27** | 1.15 | 5.70 |
| *Lab reference: best model with SOH history* | *0.66* | *0.70* | *0.11* | *0.02* |

- Field signals beat age on every dataset where the protocol matches training.
- Losing the SOH history costs 5–10×. That is the honest price of the real-world setting, and it is what Stages 1–3 attack with sequence models, many-variate curves and long lookbacks.

## 7. Intervals (ADR-0019)
Adaptive calibration does not narrow intervals: width is driven by the size of the errors. Useful share at h = 50:
- NASA ≈ 0 %;
- CALCE ≈ 4 %;
- Toyota ≈ 94–98 %.

Narrowing must come from better predictions. Meanwhile every report and dashboard states informativeness.
