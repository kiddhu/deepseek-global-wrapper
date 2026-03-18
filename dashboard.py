import http.server
import socketserver
import os

PORT = 8080
LOG_PATH = '/root/OpenClaw/audit.log'

class AIONHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            log_html = ""
            if os.path.exists(LOG_PATH):
                with open(LOG_PATH, 'r') as f:
                    lines = f.readlines()
                    # 取最近 20 条记录并反转顺序（最新的在上面）
                    for line in reversed(lines[-20:]):
                        if ']' in line:
                            # 简单的颜色标记
                            color = "#4ade80" if "SUCCESS" in line else "#f87171"
                            if "START" in line: color = "#fbbf24"
                            log_html += f"<div style='border-bottom:1px solid #30363d;padding:12px;font-family:monospace;font-size:0.9rem;'><span style='color:{color};'>●</span> {line}</div>"

            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>AION CEO Board</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body {{ background: #0d1117; color: #c9d1d9; font-family: -apple-system, sans-serif; padding: 20px; margin: 0; }}
                    .container {{ max-width: 900px; margin: auto; }}
                    .header {{ display: flex; align-items: center; margin-bottom: 30px; border-bottom: 1px solid #30363d; padding-bottom: 20px; }}
                    .dot {{ width: 12px; height: 12px; background: #238636; border-radius: 50%; margin-right: 15px; box-shadow: 0 0 10px #238636; }}
                    .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; }}
                    h1 {{ color: #f0f6fc; font-size: 1.5rem; margin: 0; }}
                    .log-container {{ background: #010409; border-radius: 8px; margin-top: 15px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <div class="dot"></div>
                        <h1>AION 帝国总指挥部 v6.0</h1>
                    </div>
                    <div class="card">
                        <h2 style="font-size:1.1rem; color:#58a6ff; margin-top:0;">Agent 实时作业流水 (Proof of Work)</h2>
                        <div class="log-container">
                            {log_html or "<div style='padding:20px;color:#8b949e;'>等待 Agent 汇报战果...</div>"}
                        </div>
                    </div>
                    <p style="text-align:center; color:#8b949e; font-size:0.8rem; margin-top:30px;">
                        AION: The Era of the One. 系统运行中。
                    </p>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        else:
            super().do_GET()

if __name__ == "__main__":
    # 允许端口重用，防止重启时报 Address already in use
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), AIONHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
