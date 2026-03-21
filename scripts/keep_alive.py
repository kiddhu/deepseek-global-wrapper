#!/usr/bin/env python3
"""
Periodic health checks + append-only heartbeat log for Imperial HQ visibility.

Default: every 10 minutes check dash.seekapi.ai, local dashboard, and One-API upstream.
"""

from __future__ import annotations

import json
import os
import subprocess
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

REPO_ROOT = os.path.abspath(os.environ.get("AION_REPO_ROOT", os.path.expanduser("~/OpenClaw")))
LOG_DIR = os.path.join(REPO_ROOT, "logs")
HEARTBEAT_PATH = os.path.join(LOG_DIR, "heartbeat.log")

DASH_SEEKAPI_URL = os.environ.get("AION_DASH_SEEKAPI_URL", "https://dash.seekapi.ai/").strip()
DASHBOARD_URL = os.environ.get("AION_DASHBOARD_URL", "http://127.0.0.1:8080/").strip()
DASHBOARD_TOKEN = os.environ.get("AION_DASHBOARD_TOKEN", "").strip()
ONE_API_URL = os.environ.get("AION_ONEAPI_URL", "http://45.152.64.217:3000/").strip()
CHECK_INTERVAL_SECONDS = int(os.environ.get("AION_KEEPALIVE_INTERVAL_SECONDS", "600"))


def is_online(url: str, timeout: int = 12, headers: dict[str, str] | None = None) -> bool:
    try:
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status < 500
    except urllib.error.HTTPError as exc:
        return exc.code < 500
    except Exception:
        return False


def restart_dashboard() -> None:
    script = os.path.join(REPO_ROOT, "scripts", "start_dashboard.sh")
    if os.path.isfile(script):
        subprocess.run(["bash", script], check=False, timeout=90)


def restart_one_api() -> None:
    cmd = os.environ.get("AION_ONEAPI_RESTART_CMD", "").strip()
    if not cmd:
        return
    subprocess.run(cmd, shell=True, check=False, timeout=90)


def append_heartbeat(
    dash_seekapi_ok: bool,
    dashboard_ok: bool,
    one_api_ok: bool,
) -> None:
    os.makedirs(LOG_DIR, exist_ok=True)
    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "dash_seekapi": "ok" if dash_seekapi_ok else "fail",
        "dashboard": "ok" if dashboard_ok else "fail",
        "one_api": "ok" if one_api_ok else "fail",
        "dash_seekapi_url": DASH_SEEKAPI_URL,
    }
    line = json.dumps(record, ensure_ascii=False) + "\n"
    with open(HEARTBEAT_PATH, "a", encoding="utf-8") as f:
        f.write(line)


def main() -> None:
    while True:
        dash_seekapi_ok = is_online(DASH_SEEKAPI_URL)

        dashboard_headers: dict[str, str] = {}
        if DASHBOARD_TOKEN:
            dashboard_headers["X-AION-TOKEN"] = DASHBOARD_TOKEN
        dashboard_ok = is_online(DASHBOARD_URL, headers=dashboard_headers)

        one_api_ok = is_online(ONE_API_URL)

        append_heartbeat(dash_seekapi_ok, dashboard_ok, one_api_ok)

        if not dashboard_ok:
            restart_dashboard()
        if not one_api_ok:
            restart_one_api()

        time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
