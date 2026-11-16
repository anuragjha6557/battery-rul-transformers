#!/usr/bin/env bash
# Wait for a running tune_all.sh (pid $1) to exit, then run another resumable pass.
set -uo pipefail
cd "$(dirname "$0")/.."
while kill -0 "$1" 2>/dev/null; do sleep 30; done
echo "$(date '+%F %T') SECOND PASS (ADR-0006 amendment 3: lr range [1e-5, 3e-2]; neural forecast studies re-run)" >> reports/tuning/tune_all.log
exec scripts/tune_all.sh 50 4
