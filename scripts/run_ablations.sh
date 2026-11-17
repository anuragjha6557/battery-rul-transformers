#!/usr/bin/env bash
# Phase 6 pre-registered ablations (ADR-0009, 0010, 0013) + transfer (ADR-0012). Resumable.
set -uo pipefail
cd "$(dirname "$0")/.."
export MLFLOW_TRACKING_URI="${MLFLOW_TRACKING_URI:-sqlite:///$PWD/mlflow.db}" MLFLOW_DISABLE_AGENT_HINT=1 PYTHONWARNINGS=ignore
UV="${UV:-$HOME/.local/bin/uv}"; mkdir -p reports/ablations; LOG=reports/ablations/run.log
"$UV" run battery-rul build-features all > reports/ablations/build_features.log 2>&1
for cfg in abl_recursive abl_norm_loss abl_curve; do
  echo "$(date '+%F %T') START $cfg" | tee -a "$LOG"
  "$UV" run battery-rul benchmark --config "$cfg" --n-jobs 4 > "reports/ablations/$cfg.log" 2>&1 \
    && echo "$(date '+%F %T') DONE $cfg" | tee -a "$LOG" || echo "$(date '+%F %T') FAIL $cfg" | tee -a "$LOG"
done
echo "$(date '+%F %T') START transfer" | tee -a "$LOG"
"$UV" run battery-rul transfer --task forecast --datasets nasa,calce --seeds 0,1,2,3,4 --pretrain > reports/ablations/transfer.log 2>&1 \
  && echo "$(date '+%F %T') DONE transfer" | tee -a "$LOG" || echo "$(date '+%F %T') FAIL transfer" | tee -a "$LOG"
echo "$(date '+%F %T') ALL DONE" | tee -a "$LOG"
