#!/usr/bin/env bash
set -euo pipefail

cd /root/OpenClaw
mkdir -p /root/OpenClaw/blog /root/OpenClaw/logs
touch /root/OpenClaw/logs/audit.log

if [ -f /root/OpenClaw/config/dashboard.env ]; then
  # shellcheck disable=SC1091
  source /root/OpenClaw/config/dashboard.env
fi

export DASHBOARD_HOST="${DASHBOARD_HOST:-0.0.0.0}"
export DASHBOARD_PORT="${DASHBOARD_PORT:-8080}"
export DASHBOARD_TOKEN="${DASHBOARD_TOKEN:-}"

pkill -f "python3 dashboard.py" || true
nohup python3 /root/OpenClaw/dashboard.py >/tmp/aion-dashboard.log 2>&1 &
