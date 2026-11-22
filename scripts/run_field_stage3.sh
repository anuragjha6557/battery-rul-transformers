#!/usr/bin/env bash
# PLAN_PHASE2 Stage 3 main grid (ADR-0020). Resumable. 3 workers (PatchTST Stage 2 may run alongside on 1).
set -uo pipefail
cd "$(dirname "$0")/.."
export MLFLOW_TRACKING_URI="${MLFLOW_TRACKING_URI:-sqlite:///$PWD/mlflow.db}" MLFLOW_DISABLE_AGENT_HINT=1 PYTHONWARNINGS=ignore
UV="${UV:-$HOME/.local/bin/uv}"; LOG=reports/ablations/run.log
for cfg in field_final_nasa field_final_calce field_final_toyota; do
  echo "$(date '+%F %T') START $cfg" | tee -a "$LOG"
  "$UV" run battery-rul benchmark --config "$cfg" --n-jobs 3 > "reports/ablations/$cfg.log" 2>&1 \
    && echo "$(date '+%F %T') DONE $cfg" | tee -a "$LOG" || echo "$(date '+%F %T') FAIL $cfg" | tee -a "$LOG"
done
"$UV" run battery-rul report --experiment field_final >> reports/ablations/field_final_report.log 2>&1
echo "$(date '+%F %T') STAGE3 MAIN DONE" | tee -a "$LOG"
