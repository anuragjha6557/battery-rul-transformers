# ADR-0001: Record decisions as ADRs

- **Status:** Accepted
- **Date:** 2026-11-15

## Context
This project rebuilds a published paper whose methodology turned out to be underspecified (preprocessing, RUL definition, split protocol). The new project has to be defensible in technical interviews: for every non-trivial choice, the "what" and the "why" must be easy to retrieve, including the alternatives that were rejected.

## Options considered
1. **Comments in code / README only.** These are cheap, but rationale gets scattered and rejected alternatives are lost.
2. **One long design doc.** Hard to reference, and it drifts out of date.
3. **Architecture Decision Records** (Nygard format), one short file per decision. Append-only, numbered and linkable.

## Decision
Use ADRs in `docs/decisions/NNNN-kebab-title.md` with the sections *Context / Options considered / Decision / Evidence / Consequences*, each at most one page. ADRs that come from an experiment must cite the MLflow run IDs or the report figure that supports them. An ablation's ADR is **written before the run** (pre-registered hypothesis), and the outcome is appended afterwards. Superseded ADRs are marked and kept, never deleted.

## Consequences
- `docs/decisions/README.md` indexes all ADRs; `docs/PLAN.md §12` lists the expected set.
- Every interview question of the form "why X?" should map to an ADR.
