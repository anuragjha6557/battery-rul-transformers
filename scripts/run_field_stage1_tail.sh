#!/usr/bin/env bash
# Resume Stage 1 field_curve arm with one worker (Toyota PatchTST at 35 channels exhausts memory when 3 run in parallel).
set -uo pipefail
cd "$(dirname "$0")/.."
export MLFLOW_TRACKING_URI="${MLFLOW_TRACKING_URI:-sqlite:///$PWD/mlflow.db}" MLFLOW_DISABLE_AGENT_HINT=1 PYTHONWARNINGS=ignore
UV="${UV:-$HOME/.local/bin/uv}"; LOG=reports/ablations/run.log; cfg=field_screen_field_curve
echo "$(date '+%F %T') RESTART $cfg --n-jobs 1 (186/189 done)" | tee -a "$LOG"
"$UV" run battery-rul benchmark --config "$cfg" --n-jobs 1 > "reports/ablations/$cfg.log" 2>&1 \
  && "$UV" run battery-rul report --experiment "$cfg" >> "reports/ablations/$cfg.log" 2>&1 \
  && echo "$(date '+%F %T') DONE $cfg" | tee -a "$LOG" || echo "$(date '+%F %T') FAIL $cfg" | tee -a "$LOG"
echo "$(date '+%F %T') STAGE1 DONE" | tee -a "$LOG"
