#!/usr/bin/env bash
# Calibrate (CQR, alpha=0.1) every benchmark run, then regenerate the reports.
set -uo pipefail
cd "$(dirname "$0")/.."
export MLFLOW_TRACKING_URI="${MLFLOW_TRACKING_URI:-sqlite:///$PWD/mlflow.db}" MLFLOW_DISABLE_AGENT_HINT=1 PYTHONWARNINGS=ignore
UV="${UV:-$HOME/.local/bin/uv}"; LOG=reports/benchmark/run.log
for exp in benchmark benchmark_local; do
  echo "$(date '+%F %T') CALIBRATE $exp" | tee -a "$LOG"
  "$UV" run battery-rul calibrate --experiment "$exp" --alpha 0.1 > "reports/benchmark/calibrate_$exp.log" 2>&1 \
    && echo "$(date '+%F %T') CALIBRATED $exp" | tee -a "$LOG" || echo "$(date '+%F %T') FAIL calibrate $exp" | tee -a "$LOG"
  "$UV" run battery-rul report --experiment "$exp" > "reports/benchmark/report_$exp.log" 2>&1 \
    && echo "$(date '+%F %T') REPORTED $exp" | tee -a "$LOG" || echo "$(date '+%F %T') FAIL report $exp" | tee -a "$LOG"
done
echo "$(date '+%F %T') POST DONE" | tee -a "$LOG"
