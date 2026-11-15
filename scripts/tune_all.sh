#!/usr/bin/env bash
# Equal-budget tuning sweep on Toyota (ADR-0006): every tunable model x every task, 50 trials.
# Resumable: a study whose configs/tuned/<model>__<task>.yaml exists is skipped, and Optuna's
# journal resumes a study that was interrupted mid-way.
# Usage: scripts/tune_all.sh [n_trials] [n_jobs]   (logs to reports/tuning/tune_all.log)
set -uo pipefail
cd "$(dirname "$0")/.."
N_TRIALS="${1:-50}"
N_JOBS="${2:-4}"
UV="${UV:-$HOME/.local/bin/uv}"
export MLFLOW_TRACKING_URI="${MLFLOW_TRACKING_URI:-sqlite:///$PWD/mlflow.db}"
export MLFLOW_DISABLE_AGENT_HINT=1 PYTHONWARNINGS=ignore
mkdir -p reports/tuning
LOG=reports/tuning/tune_all.log

# Cheapest first, so early results arrive quickly and a crash costs least.
MODELS=(elasticnet lgbm nlinear dlinear rlinear patchtst itransformer_sc itransformer transformer gru lstm)
TASKS=(forecast soh rul)

for task in "${TASKS[@]}"; do
  for model in "${MODELS[@]}"; do
    out="configs/tuned/${model}__${task}.yaml"
    if [[ -f "$out" ]]; then
      echo "$(date '+%F %T') SKIP ${model}__${task} (exists)" | tee -a "$LOG"
      continue
    fi
    echo "$(date '+%F %T') START ${model}__${task}" | tee -a "$LOG"
    start=$(date +%s)
    if "$UV" run battery-rul tune --model "$model" --task "$task" \
        --n-trials "$N_TRIALS" --n-jobs "$N_JOBS" > "reports/tuning/${model}__${task}.log" 2>&1; then
      best=$(grep -m1 -iE "best value|best_value" "reports/tuning/${model}__${task}.log" | tail -c 120)
      flags=$(grep -iE "boundary" "reports/tuning/${model}__${task}.log" | tr '\n' ' ' | tail -c 200)
      echo "$(date '+%F %T') DONE ${model}__${task} $(( $(date +%s) - start ))s | ${best} | ${flags}" | tee -a "$LOG"
    else
      echo "$(date '+%F %T') FAIL ${model}__${task} $(( $(date +%s) - start ))s (see reports/tuning/${model}__${task}.log)" | tee -a "$LOG"
    fi
  done
done
echo "$(date '+%F %T') ALL DONE" | tee -a "$LOG"
