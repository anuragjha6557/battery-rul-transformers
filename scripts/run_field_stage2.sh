#!/usr/bin/env bash
# PLAN_PHASE2 Stage 2 (long lookback). Resumable. PatchTST runs with one worker (memory).
set -uo pipefail
cd "$(dirname "$0")/.."
export MLFLOW_TRACKING_URI="${MLFLOW_TRACKING_URI:-sqlite:///$PWD/mlflow.db}" MLFLOW_DISABLE_AGENT_HINT=1 PYTHONWARNINGS=ignore
UV="${UV:-$HOME/.local/bin/uv}"; LOG=reports/ablations/run.log
for spec in field_lookback_toyota:4 field_lookback_calce:4 field_lookback_toyota_patchtst:1 field_lookback_calce_patchtst:1; do
  cfg=${spec%%:*}; nj=${spec##*:}
  echo "$(date '+%F %T') START $cfg" | tee -a "$LOG"
  "$UV" run battery-rul benchmark --config "$cfg" --n-jobs "$nj" > "reports/ablations/$cfg.log" 2>&1 \
    && echo "$(date '+%F %T') DONE $cfg" | tee -a "$LOG" || echo "$(date '+%F %T') FAIL $cfg" | tee -a "$LOG"
done
"$UV" run battery-rul report --experiment field_lookback >> reports/ablations/field_lookback_report.log 2>&1
echo "$(date '+%F %T') STAGE2 DONE" | tee -a "$LOG"
