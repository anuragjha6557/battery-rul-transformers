#!/usr/bin/env bash
# ADR-0016 (rest-aware forecasting) and ADR-0017 (CALCE artifact cycles). Resumable.
set -uo pipefail
cd "$(dirname "$0")/.."
export MLFLOW_TRACKING_URI="${MLFLOW_TRACKING_URI:-sqlite:///$PWD/mlflow.db}" MLFLOW_DISABLE_AGENT_HINT=1 PYTHONWARNINGS=ignore
UV="${UV:-$HOME/.local/bin/uv}"; mkdir -p reports/ablations; LOG=reports/ablations/run.log
for cfg in abl_future_rest abl_calce_clean; do
  echo "$(date '+%F %T') START $cfg" | tee -a "$LOG"
  "$UV" run battery-rul benchmark --config "$cfg" --n-jobs 4 > "reports/ablations/$cfg.log" 2>&1 \
    && "$UV" run battery-rul report --experiment "$cfg" >> "reports/ablations/$cfg.log" 2>&1 \
    && echo "$(date '+%F %T') DONE $cfg" | tee -a "$LOG" || echo "$(date '+%F %T') FAIL $cfg" | tee -a "$LOG"
done
echo "$(date '+%F %T') REGEN ALL DONE" | tee -a "$LOG"
