import html
import http.server
import os
import re
import socketserver
from urllib.parse import parse_qs, urlparse

PORT = int(os.environ.get("DASHBOARD_PORT", "8080"))
HOST = os.environ.get("DASHBOARD_HOST", "0.0.0.0")
AUTH_TOKEN = os.environ.get("DASHBOARD_TOKEN", "").strip()
AUDIT_PATH = "/root/OpenClaw/audit.log"
BLOG_PATH = "/root/OpenClaw/blog"


def parse_metrics_from_audit() -> dict:
    leads = 0
    latest_lead = "N/A"
    if not os.path.exists(AUDIT_PATH):
        return {"leads": 0, "latest_lead": latest_lead}

    with open(AUDIT_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if "[The Hunter]" in line and "捕获" in line and "条生产线索" in line:
            m = re.search(r"捕获\s+(\d+)\s+条生产线索", line)
            if m:
                leads += int(m.group(1))
                latest_lead = line.strip()
    return {"leads": leads, "latest_lead": latest_lead}


def count_blog_markdown() -> int:
    if not os.path.isdir(BLOG_PATH):
        return 0
    return len([name for name in os.listdir(BLOG_PATH) if name.endswith(".md")])


class AIONHandler(http.server.SimpleHTTPRequestHandler):
    def _is_authorized(self):
        if not AUTH_TOKEN:
            return True
        query = parse_qs(urlparse(self.path).query)
        token = query.get("token", [""])[0]
        header = self.headers.get("X-AION-TOKEN", "")
        return token == AUTH_TOKEN or header == AUTH_TOKEN

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path != "/":
            super().do_GET()
            return

        if not self._is_authorized():
            self.send_response(401)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Unauthorized: provide ?token=... or X-AION-TOKEN header")
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        metrics = parse_metrics_from_audit()
        leads = metrics["leads"]
        latest_lead = html.escape(metrics["latest_lead"])
        blog_count = count_blog_markdown()

        logs = []
        if os.path.exists(AUDIT_PATH):
            with open(AUDIT_PATH, "r", encoding="utf-8") as f:
                logs = f.readlines()[-15:][::-1]
        log_html = "".join(
            [
                f"<div style='border-bottom:1px solid #332b16;padding:8px;color:#d4af37;'>{html.escape(l.strip())}</div>"
                for l in logs
            ]
        )

        html_doc = f"""
        <html><head><title>AION Dashboard</title><style>
            body {{ background:#000; color:#d4af37; font-family:ui-sans-serif, sans-serif; padding:28px; }}
            .grid {{ display:grid; grid-template-columns:repeat(4, 1fr); gap:16px; }}
            .card {{ background:#0a0a0a; border:1px solid #3a2f14; padding:18px; border-radius:8px; }}
            .stat {{ font-size:2.2rem; color:#f1d37a; font-weight:700; }}
            h1,h2 {{ color:#f1d37a; }}
            .mono {{ background:#050505; font-family:ui-monospace, monospace; }}
        </style></head><body>
            <h1>AION Imperial HQ</h1>
            <div class="grid">
                <div class="card">SEO Assets (/blog .md)<div class="stat">{blog_count}</div></div>
                <div class="card">Lead Total<div class="stat">{leads}</div></div>
                <div class="card">Host<div class="stat">{HOST}:{PORT}</div></div>
                <div class="card">Access Mode<div class="stat">{'TOKEN' if AUTH_TOKEN else 'OPEN'}</div></div>
            </div>
            <h2>Latest Lead Event</h2>
            <div class="card mono">{latest_lead}</div>
            <h2>Audit Stream</h2>
            <div class="card mono">{log_html}</div>
        </body></html>
        """
        self.wfile.write(html_doc.encode("utf-8"))


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer((HOST, PORT), AIONHandler) as httpd:
    print(f"AION Dashboard running on http://{HOST}:{PORT}")
    if AUTH_TOKEN:
        print("Auth enabled: use ?token=*** or X-AION-TOKEN header")
    httpd.serve_forever()
