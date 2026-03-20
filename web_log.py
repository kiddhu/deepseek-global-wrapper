import http.server, socketserver, os, time

PORT = 8080
BASE_DIR = "/root/OpenClaw"
GUIDES_DIR = "/root/OpenClaw/public/guides"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        now = time.time()
        content = "<html><head><title>AION Command Center</title>"
        content += "<style>body{font-family:'Inter',sans-serif;padding:60px;background:#000;color:#fff;max-width:1000px;margin:0 auto;} .slogan{color:#666;letter-spacing:4px;text-transform:uppercase;font-size:14px;margin-bottom:10px;} h1{color:#fff;font-size:48px;letter-spacing:-2px;margin:0 0 40px 0;} .card{background:#0a0a0a;padding:30px;border-radius:16px;margin-bottom:30px;border:1px solid #1a1a1a;} h2{color:#2563eb;font-size:18px;text-transform:uppercase;letter-spacing:1px;} .new-badge{background:#2563eb;color:white;padding:2px 8px;border-radius:4px;font-size:10px;margin-left:10px;font-weight:bold;animation:blink 1.5s infinite;} @keyframes blink{0%{opacity:1;}50%{opacity:0.4;}100%{opacity:1;}} a{color:#fff;text-decoration:underline;text-underline-offset:4px;opacity:0.8;} a:hover{opacity:1;} pre{background:#050505;color:#ccc;padding:20px;border-radius:8px;white-space:pre-wrap;font-size:13px;border:1px solid #111;line-height:1.6;}</style></head><body>"
        content += "<div class='slogan'>AION: The Era of the One.</div>"
        content += "<h1>AION 实时指挥部</h1>"
        
        # 1. pSEO & Arxiv 内容库
        if os.path.exists(GUIDES_DIR):
            files = [(f, os.path.getmtime(os.path.join(GUIDES_DIR, f))) for f in os.listdir(GUIDES_DIR)]
            files.sort(key=lambda x: x[1], reverse=True)
            content += f"<div class='card'><h2>📚 全球布道内容库 (已生成: {len(files)} 篇)</h2><ul style='list-style:none;padding:0;'>"
            for f_name, mtime in files[:15]: # 显示最近15篇
                is_new = (now - mtime) < 86400
                badge = "<span class='new-badge'>NEW / 24H</span>" if is_new else ""
                content += f"<li style='margin-bottom:15px;font-size:15px;color:#888;'>{time.strftime('%m-%d %H:%M', time.localtime(mtime))} &nbsp; <a href='https://seekapi.ai/guides/{f_name}' target='_blank'>{f_name}</a> {badge}</li>"
            content += "</ul></div>"

        # 2. 核心宣言与自检报告
        core_files = {
            "📜 AION 项目全量宣言": "PROJECT_MANIFEST.md", 
            "📊 实时流量统计": "traffic_stats.txt",
            "🩺 系统全链路自检": "health_check.txt",
            "💰 算力套利引擎": "arbitrage_status.txt"
        }
        for title, f_name in core_files.items():
            full_path = os.path.join(BASE_DIR, f_name)
            content += f"<div class='card'><h2>{title}</h2>"
            if os.path.exists(full_path):
                with open(full_path, 'r') as f: content += f"<pre>{f.read()}</pre>"
            else:
                content += "<p style='color:#444;'>等待数据生成...</p>"
            content += "</div>"
        
        content += "</body></html>"
        self.wfile.write(content.encode('utf-8'))

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    httpd.serve_forever()
