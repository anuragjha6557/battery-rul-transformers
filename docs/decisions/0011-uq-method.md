# ADR-0011: Uncertainty method, CQR vs deep ensemble vs GPR (pre-registered)

- **Status:** Proposed (registered 2026-11-16). Implementation: `uq/conformal.py`, `battery-rul calibrate`.

## Hypothesis
- Pooled split-conformal CQR (PROTOCOL §3, §5) brings 90 % interval coverage (PICP) on held-out cells to 0.90 ± 0.05 for every quantile model, at a mean interval width (MPIW) no more than 1.3× the raw interval's.
- Raw quantile models under-cover; LightGBM's raw coverage on CALCE was 0.74–0.79.
- GPR is the reference. Pilot: raw PICP 0.54 at h=50 on CALCE.

## Design
- **Arms:** raw quantiles; CQR-calibrated; 5-seed deep ensemble (quantiles averaged over seeds).
- **Metrics:** PICP, MPIW, interval score, CRPS, and reliability diagrams per dataset and horizon.
- **Decision rule:** the primary method is the one meeting the PICP target with the lowest interval score. If none meets it, report the shortfall honestly.

## Outcome
_Pending._
