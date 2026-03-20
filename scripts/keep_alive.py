#!/usr/bin/env python3
import os
import subprocess
import time
import urllib.error
import urllib.request


DASHBOARD_URL = os.environ.get("AION_DASHBOARD_URL", "http://127.0.0.1:8080/")
DASHBOARD_TOKEN = os.environ.get("AION_DASHBOARD_TOKEN", "").strip()
ONE_API_URL = os.environ.get("AION_ONEAPI_URL", "http://45.152.64.217:3000/")
CHECK_INTERVAL_SECONDS = int(os.environ.get("AION_KEEPALIVE_INTERVAL_SECONDS", "1800"))


def is_online(url: str, timeout: int = 8, headers: dict[str, str] | None = None) -> bool:
    try:
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status < 500
    except urllib.error.HTTPError as exc:
        # Auth failures still prove the process is listening.
        return exc.code < 500
    except Exception:
        return False


def restart_dashboard() -> None:
    subprocess.run(
        ["bash", os.path.expanduser("~/OpenClaw/scripts/start_dashboard.sh")],
        check=False,
        timeout=90,
    )


def restart_one_api() -> None:
    cmd = os.environ.get("AION_ONEAPI_RESTART_CMD", "").strip()
    if not cmd:
        return
    subprocess.run(cmd, shell=True, check=False, timeout=90)


def main() -> None:
    while True:
        dashboard_headers: dict[str, str] = {}
        if DASHBOARD_TOKEN:
            dashboard_headers["X-AION-TOKEN"] = DASHBOARD_TOKEN
        if not is_online(DASHBOARD_URL, headers=dashboard_headers):
            restart_dashboard()
        if not is_online(ONE_API_URL):
            restart_one_api()
        time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
