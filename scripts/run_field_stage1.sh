#!/usr/bin/env bash
# PLAN_PHASE2 Stage 1 (field SOH estimation screen). Resumable.
set -uo pipefail
cd "$(dirname "$0")/.."
export MLFLOW_TRACKING_URI="${MLFLOW_TRACKING_URI:-sqlite:///$PWD/mlflow.db}" MLFLOW_DISABLE_AGENT_HINT=1 PYTHONWARNINGS=ignore
UV="${UV:-$HOME/.local/bin/uv}"; LOG=reports/ablations/run.log
for cfg in field_screen_field field_screen_field_curve; do
  echo "$(date '+%F %T') START $cfg" | tee -a "$LOG"
  "$UV" run battery-rul benchmark --config "$cfg" --n-jobs 4 > "reports/ablations/$cfg.log" 2>&1 \
    && "$UV" run battery-rul report --experiment "$cfg" >> "reports/ablations/$cfg.log" 2>&1 \
    && echo "$(date '+%F %T') DONE $cfg" | tee -a "$LOG" || echo "$(date '+%F %T') FAIL $cfg" | tee -a "$LOG"
done
echo "$(date '+%F %T') STAGE1 DONE" | tee -a "$LOG"
