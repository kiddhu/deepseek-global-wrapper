import http.server
import os
import re
import socketserver
from datetime import datetime

import requests

PORT = 8080
AUDIT_PATH = "/root/OpenClaw/audit.log"


def parse_metrics_from_audit() -> dict:
    """
    从 audit.log 中解析今日线索数与文章数。
    """
    leads = 0
    articles = 0
    today = datetime.now().strftime("%Y-%m-%d")

    if not os.path.exists(AUDIT_PATH):
        return {"leads": 0, "articles": 0}

    with open(AUDIT_PATH, "r") as f:
        for line in f:
            if not line.startswith(f"[{today}"):
                continue

            if "[The Hunter]" in line and "捕获" in line and "条生产线索" in line:
                m = re.search(r"捕获\s+(\d+)\s+条生产线索", line)
                if m:
                    leads += int(m.group(1))

            if "[The Scholar]" in line and "篇独立博文已全线发布" in line:
                m = re.search(r"(\d+)\s*篇独立博文已全线发布", line)
                if m:
                    articles += int(m.group(1))

    return {"leads": leads, "articles": articles}


class AIONHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            # UV：当前无真实数据源，显示 N/A
            uv = "N/A"

            try:
                res = requests.get("http://45.152.64.217:3000/api/status", timeout=2)
                reg_users = res.json().get("data", {}).get("user_count", 0)
            except Exception:
                reg_users = "Offline"

            metrics = parse_metrics_from_audit()
            leads = metrics["leads"]
            articles = metrics["articles"]

            logs = (
                open(AUDIT_PATH, "r").readlines()[-15:][::-1]
                if os.path.exists(AUDIT_PATH)
                else []
            )
            log_html = "".join(
                [
                    f"<div style='border-bottom:1px solid #333;padding:8px;'>{l}</div>"
                    for l in logs
                ]
            )

            html = f"""
            <html><head><title>AION Dashboard</title><style>
                body {{ background:#0d1117; color:#c9d1d9; font-family:sans-serif; padding:30px; }}
                .grid {{ display:grid; grid-template-columns:repeat(4, 1fr); gap:20px; }}
                .card {{ background:#161b22; border:1px solid #30363d; padding:20px; border-radius:12px; }}
                .stat {{ font-size:2.5rem; color:#58a6ff; font-weight:bold; }}
                h1 {{ color:#f0f6fc; }}
            </style></head><body>
                <h1>AION 帝国总指挥部 v7.1</h1>
                <div class="grid">
                    <div class="card">今日访客 (UV)<div class="stat">{uv}</div></div>
                    <div class="card">注册用户<div class="stat">{reg_users}</div></div>
                    <div class="card">线索总数<div class="stat">{leads}</div></div>
                    <div class="card">SEO 资产<div class="stat">{articles}</div></div>
                </div>
                <h2>实时作业流水 (Proof of Work)</h2>
                <div class="card" style="background:#010409; font-family:monospace;">{log_html}</div>
            </body></html>
            """
            self.wfile.write(html.encode())
        else:
            super().do_GET()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), AIONHandler) as httpd:
    httpd.serve_forever()
