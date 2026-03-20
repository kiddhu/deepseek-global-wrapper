import html
import os
import re
import socket
from flask import Flask, Response, request

from db_utils import get_db_connection

HOST = os.environ.get("DASHBOARD_HOST", "0.0.0.0")
PORT = int(os.environ.get("DASHBOARD_PORT", "8080"))
AUTH_TOKEN = os.environ.get("DASHBOARD_TOKEN", "").strip()

BLOG_PATH = "/root/OpenClaw/blog"
LOG_DIR = "/root/OpenClaw/logs"
AUDIT_PATH = f"{LOG_DIR}/audit.log"

app = Flask(__name__)


def ensure_paths():
    os.makedirs(BLOG_PATH, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)
    if not os.path.exists(AUDIT_PATH):
        with open(AUDIT_PATH, "a", encoding="utf-8"):
            pass


def count_blog_posts() -> int:
    return len([n for n in os.listdir(BLOG_PATH) if n.endswith(".md")])


def parse_leads_from_audit() -> tuple[int, str]:
    leads = 0
    latest = "N/A"
    with open(AUDIT_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if "[The Hunter]" in line and "捕获" in line and "条生产线索" in line:
                m = re.search(r"捕获\s+(\d+)\s+条生产线索", line)
                if m:
                    leads += int(m.group(1))
                    latest = line.strip()
    return leads, latest


def hk_oneapi_online() -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    try:
        return sock.connect_ex(("45.152.64.217", 3000)) == 0
    finally:
        sock.close()


def today_agent_memory_count() -> int:
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM agent_memory WHERE created_at::date = CURRENT_DATE")
        count = int(cur.fetchone()[0] or 0)
        cur.close()
        conn.close()
        return count
    except Exception:
        return 0


def auth_ok() -> bool:
    if not AUTH_TOKEN:
        return True
    token_qs = request.args.get("token", "")
    token_header = request.headers.get("X-AION-TOKEN", "")
    return token_qs == AUTH_TOKEN or token_header == AUTH_TOKEN


@app.get("/")
def index() -> Response:
    if not auth_ok():
        return Response("Unauthorized", status=401)

    ensure_paths()
    blog_total = count_blog_posts()
    leads, latest_lead = parse_leads_from_audit()
    hk_status = "ONLINE" if hk_oneapi_online() else "OFFLINE"
    traffic = today_agent_memory_count()

    html_doc = f"""
    <html>
    <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width,initial-scale=1" />
      <title>AION Imperial HQ</title>
      <style>
        body {{
          margin: 0;
          background-color: #000;
          color: #d4af37;
          font-family: Inter, ui-sans-serif, sans-serif;
          background-image:
            linear-gradient(rgba(212,175,55,0.06) 1px, transparent 1px),
            linear-gradient(90deg, rgba(212,175,55,0.06) 1px, transparent 1px);
          background-size: 26px 26px;
        }}
        .wrap {{ max-width: 1180px; margin: 0 auto; padding: 28px; }}
        .top {{ display:flex; align-items:center; gap:12px; }}
        .live-dot {{
          width:10px; height:10px; border-radius:50%; background:#ff2d2d;
          box-shadow:0 0 10px #ff2d2d; animation: pulse 1.4s infinite;
        }}
        .grid {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:16px; margin-top: 16px; }}
        .card {{
          border: 1px solid #d4af37;
          background: rgba(212, 175, 55, 0.05);
          border-radius: 12px;
          padding: 16px;
        }}
        .label {{ opacity:.9; font-size: .9rem; }}
        .value {{ font-size: 3rem; font-weight: bold; color: #fff; text-shadow: 0 0 10px #d4af37; }}
        .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; white-space: pre-wrap; }}
        @media (max-width: 960px) {{
          .grid {{ grid-template-columns:1fr 1fr; }}
          .value {{ font-size: 2.1rem; }}
        }}
        @keyframes pulse {{
          0% {{ opacity: .3; transform: scale(.9); }}
          50% {{ opacity: 1; transform: scale(1.05); }}
          100% {{ opacity: .3; transform: scale(.9); }}
        }}
      </style>
    </head>
    <body>
      <div class="wrap">
        <div class="top">
          <div class="live-dot"></div>
          <h1>AION Imperial HQ - BlackGold Console</h1>
        </div>
        <div class="grid">
          <div class="card"><div class="label">Empire Assets (/blog)</div><div class="value">{blog_total}</div></div>
          <div class="card"><div class="label">Captured Leads (audit.log)</div><div class="value">{leads}</div></div>
          <div class="card"><div class="label">System Heartbeat (45.152.64.217:3000)</div><div class="value">{hk_status}</div></div>
          <div class="card"><div class="label">Traffic Radar (today agent_memory)</div><div class="value">{traffic}</div></div>
        </div>
        <h3>Latest Lead Event</h3>
        <div class="card mono">{html.escape(latest_lead)}</div>
      </div>
    </body>
    </html>
    """
    return Response(html_doc, mimetype="text/html; charset=utf-8")


if __name__ == "__main__":
    ensure_paths()
    app.run(host=HOST, port=PORT)
