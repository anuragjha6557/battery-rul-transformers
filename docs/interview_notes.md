# Interview notes

Defensible talking points, each with a pointer to the ADR or report that holds the evidence. Numbers are from this repo's generated tables, never from the source paper.

## The one-minute version
I rebuilt my own ITEC 2024 paper as a leakage-free benchmark on NASA, CALCE and Toyota/MIT-Stanford, without trying to match its numbers. The result is dataset-dependent: iTransformer leads in-distribution on Toyota, and a tuned LightGBM or ElasticNet matches it on 4-cell NASA/CALCE ([ADR-0014](decisions/0014-final-model-selection.md), [ADR-0008](decisions/0008-baseline-findings.md)). Phase 2 asks the harder question: what happens with only BMS-measurable inputs and no SOH history? There iTransformer is not the winner, and I report that ([ADR-0021](decisions/0021-itransformer-field-verdict.md)).

## 1. Leakage rules
- **Claim:** seven rules, each enforced by a unit test, and the tests were mutation-checked (PROTOCOL §4, `tests/test_leakage.py`, [ADR-0004](decisions/0004-evaluation-protocol.md)).
- **Example that matters:** discharge quantities of cycle k are near-copies of the target capacity at k. So SOH estimation may use only charge-side features of cycle k plus history before k. Tasks B and C use only cycles up to the origin.
- **Field setting:** a test corrupts every forbidden column of every cycle and checks that the inputs are bit-identical ([ADR-0018](decisions/0018-outlier-policy-and-field-inputs.md)).
- Scalers are fitted on training cells only. Absolute `cycle_idx` and cell id are never model inputs in the lab setting.
- **If pushed:** a green leakage suite is necessary, not sufficient. That is why the tests are mutated: break the rule on purpose and confirm the test fails.

## 2. The CALCE CV-skip artifact
- In 109 CALCE cycles (about 3 %) the charger's constant-voltage step ended after one sample. The next discharge delivers about 10.6 % less capacity and the cell returns to trend one cycle later ([ADR-0005](decisions/0005-eol-definition.md), [ADR-0017](decisions/0017-calce-artifact-cycles.md)).
- It also changes RUL labels. A naive EOL rule trips on a dip, so the EOL rule requires a masked and sustained crossing. The paper never mentions this.
- I tested "treat them as invalid measurements" as a pre-registered hypothesis. It was not adopted as the default (forecast gain, RUL loss), but artifact-free scoring was added.
- In the field setting the skip flag is a legitimate causal input (it comes from the charge), and the cycles are dropped as labels only ([ADR-0018](decisions/0018-outlier-policy-and-field-inputs.md)).

## 3. The shared NASA rig
- B0005, B0006 and B0007 share one rig and rest schedule, so their regeneration jumps co-occur at the same cycle index. Leave-one-cell-out on them is not independent ([ADR-0004](decisions/0004-evaluation-protocol.md)).
- I report B0018 as the one rig-independent fold, and I do not give absolute `cycle_idx` to models, so they cannot memorise rig-mates' regeneration cycles.
- With 4 cells I use cluster-bootstrap CIs and k-of-4 direction counts, not p-values. Real tests (Holm-corrected Wilcoxon) are used only on Toyota.

## 4. Equal-budget tuning
- Every model gets 50 TPE trials with Hyperband pruning, the same learning-rate range, the same parameter cap (250 k), early stopping and seeds. Search spaces are committed before the sweep ([ADR-0006](decisions/0006-equal-budget-tuning.md)).
- Tuning is on Toyota (41 training cells), not on 4 cells: tuning on 4 cells is winner's curse.
- The boundary-hit check paid off. It fired on learning rate and weight decay, and the range was widened for all models at once, never for one.
- **If pushed:** tuned on Toyota and applied to NASA/CALCE is a real limitation, stated in the ADR.

## 5. CQR and why it fails under shift
- Raw quantile heads under-cover (iTransformer 46 % on NASA at h = 50). Split-conformal CQR on held-out inner-fold cells fixes 30 of 40 conditions ([ADR-0011](decisions/0011-uq-method.md)).
- Conformal assumes exchangeability. Toyota test2 is a different batch (rest at 80 % SOC of 10 s instead of 61 s, CV time 348 s instead of 716 s; `reports/eda_field.md` §5), so the guarantee does not hold: field iTransformer covers 0.66 at h = 50 there.
- Accuracy and calibration under shift diverge: iTransformer is the most accurate on test2, LightGBM keeps 0.87 coverage.
- Coverage is also not usefulness. On NASA, intervals reach about 90 % coverage with a useful share near zero. So every interval table reports the useful share ([ADR-0019](decisions/0019-adaptive-intervals.md)). I tried adaptive (Mondrian, scaled) calibration; it did not narrow intervals without losing coverage.
- The demo says this on the page and raises an OOD flag.

## 6. The lab to field gap
- Lab (SOH history): SOH RMSE 0.66 / 0.70 / 0.11 / 0.02 %SOH (CALCE, NASA, Toyota test1, test2; the lab reference quoted in ADR-0020). Field (iTransformer): 3.28 / 4.59 / 1.06 / 1.55.
- Field signals still beat age-only on Toyota and CALCE, so the information is real. The cost of losing SOH history is 4-75x ([ADR-0020](decisions/0020-field-benchmark.md)).
- The honest message: published lab numbers with a capacity log say little about a BMS. Regeneration is visible in field signals when it happens but not forecastable at this error level.

## 7. The negative iTransformer verdict, and why it is a good result
- The rule was pre-registered before the final runs: best mean rank among learned models and at most one significant loss on Toyota test1. Mean rank was 2.33 against LSTM's 2.25, and competitors beat it in two of three tasks, so the verdict is **negative**.
- I state the borderline. If a competitor must win under both the CI rule and Holm-Wilcoxon, it reads mixed. I did not choose the reading after seeing the result ([ADR-0021](decisions/0021-itransformer-field-verdict.md)).
- I tested the paper's claims separately: many variates (chemistry-conditional), long lookbacks (not supported), known-future covariates as a token (not supported; -8.9 % against a +26 % bar), channel mixing vs independence (supported, beats PatchTST in 12 of 12).
- **Why it is good:** the project can say where the architecture helps (shift robustness on Toyota, NASA RUL) and where it does not, with the test that would have shown otherwise. I still deploy it for the field demo because the deploy criterion is robustness under shift, and I say that is a different criterion ([ADR-0022](decisions/0022-field-deployment.md)).

## 8. What I would do next
- **More cells.** NASA and CALCE have 4 cells each, so their conclusions are weak. Adding datasets is out of scope here by decision; the next step would be field data with real fleet protocols.
- **Shift-aware calibration.** The CQR failure on Toyota test2 is the clearest open problem. Candidates are calibrating on a held-out batch or using shift-aware (weighted) conformal methods. These are ideas, not tested here.
- **Protocol-invariant field signals,** so one model transfers across charging protocols instead of one per protocol.
- **Narrower intervals from better predictions.** Calibration tricks did not help (ADR-0019).

## Quick answers
| Question | Answer | Where |
|---|---|---|
| Why not reproduce the paper? | Owner decision: its numbers may be wrong; the paper supplies the idea | `CLAUDE.md`, [ADR-0014](decisions/0014-final-model-selection.md) |
| Why direct, not recursive, forecasting? | Recursive error compounds: 1.15-5.6x worse at h = 50 | [ADR-0010](decisions/0010-direct-vs-recursive.md) |
| Why is Toyota pre-training not the default? | Cuts NASA h = 50 error by 28 %, hurts CALCE | [ADR-0012](decisions/0012-toyota-transfer.md) |
| Why a static browser demo? | HF requires PRO for free-CPU Gradio Spaces; ONNX in the browser is free and private | [ADR-0015](decisions/0015-deployment.md) amendment 1 |
| Why one field model per protocol? | Voltage windows and batches differ; a pooled model hides it | [ADR-0022](decisions/0022-field-deployment.md) |
