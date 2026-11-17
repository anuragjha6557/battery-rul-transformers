#!/usr/bin/env bash
# Phase 4/5 benchmark: local extrapolators first (fast), then the full tuned benchmark. Resumable.
set -uo pipefail
cd "$(dirname "$0")/.."
export MLFLOW_TRACKING_URI="${MLFLOW_TRACKING_URI:-sqlite:///$PWD/mlflow.db}" MLFLOW_DISABLE_AGENT_HINT=1 PYTHONWARNINGS=ignore
UV="${UV:-$HOME/.local/bin/uv}"; mkdir -p reports/benchmark; LOG=reports/benchmark/run.log
for cfg in benchmark_local benchmark; do
  echo "$(date '+%F %T') START $cfg" | tee -a "$LOG"
  if "$UV" run battery-rul benchmark --config "$cfg" --n-jobs 4 > "reports/benchmark/$cfg.log" 2>&1; then
    echo "$(date '+%F %T') DONE $cfg | $(tail -c 300 reports/benchmark/$cfg.log | tr '\n' ' ')" | tee -a "$LOG"
  else
    echo "$(date '+%F %T') FAIL $cfg (see reports/benchmark/$cfg.log)" | tee -a "$LOG"
  fi
done
echo "$(date '+%F %T') ALL DONE" | tee -a "$LOG"
