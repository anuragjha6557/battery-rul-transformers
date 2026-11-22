#!/usr/bin/env bash
# PLAN_PHASE2 Stage 3, second wave (ADR-0020): regeneration arm (field_regen, 2 workers) in parallel
# with PatchTST in field_final (1 worker, MPS memory). Resumable.
set -uo pipefail
cd "$(dirname "$0")/.."
export MLFLOW_TRACKING_URI="${MLFLOW_TRACKING_URI:-sqlite:///$PWD/mlflow.db}" MLFLOW_DISABLE_AGENT_HINT=1 PYTHONWARNINGS=ignore
UV="${UV:-$HOME/.local/bin/uv}"; LOG=reports/ablations/run.log
run() {  # cfg n_jobs
  echo "$(date '+%F %T') START $1" | tee -a "$LOG"
  "$UV" run battery-rul benchmark --config "$1" --n-jobs "$2" > "reports/ablations/$1.log" 2>&1 \
    && echo "$(date '+%F %T') DONE $1" | tee -a "$LOG" || echo "$(date '+%F %T') FAIL $1" | tee -a "$LOG"
}
(
  for cfg in field_regen_nasa_token field_regen_nasa_tab field_regen_calce_token field_regen_calce_tab; do
    run "$cfg" 2
  done
  "$UV" run battery-rul report --experiment field_regen >> reports/ablations/field_regen_report.log 2>&1
  echo "$(date '+%F %T') REGEN DONE" | tee -a "$LOG"
) &
for cfg in field_final_nasa_patchtst field_final_calce_patchtst field_final_toyota_patchtst; do
  run "$cfg" 1
done
wait
"$UV" run battery-rul report --experiment field_final >> reports/ablations/field_final_report.log 2>&1
echo "$(date '+%F %T') STAGE3B DONE" | tee -a "$LOG"
