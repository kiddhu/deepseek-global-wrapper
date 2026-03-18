import os, re, time, requests, base64
from dotenv import load_dotenv

load_dotenv()

def get_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'<h1>(.*?)</h1>', content)
        return match.group(1).strip() if match else "Untitled Insight"

def generate():
    guides_dir = "/root/OpenClaw/public/guides"
    files_data = []
    for f in os.listdir(guides_dir):
        if f.endswith('.html') and f != 'index.html':
            path = os.path.join(guides_dir, f)
            files_data.append({
                "name": f,
                "title": get_title(path),
                "time": os.path.getmtime(path)
            })
    
    files_data.sort(key=lambda x: x['time'], reverse=True)
    
    links_html = ""
    for item in files_data[:40]: # 分页逻辑：每页40篇
        date_str = time.strftime('%Y-%m-%d', time.localtime(item['time']))
        links_html += f"""
        <li style='margin-bottom:15px; padding:20px; border:1px solid #111; border-radius:12px; background:#050505;'>
            <div style='color:#444; font-size:12px;'>{date_str}</div>
            <a href='/guides/{item['name']}' style='color:#fff; text-decoration:none; font-size:20px; font-weight:bold;'>{item['title']}</a>
        </li>"""

    index_html = f"<html><head><meta charset='UTF-8'><title>AION Insights</title><style>body{{font-family:sans-serif;padding:60px;background:#000;color:#fff;max-width:800px;margin:0 auto;}} h1{{color:#2563eb;font-size:48px;letter-spacing:-2px;}} ul{{list-style:none;padding:0;}}</style></head><body><a href='/' style='color:#444;text-decoration:none;'>← Back</a><h1>AION Insights</h1><ul>{links_html}</ul></body></html>"
    
    # 推送到 GitHub
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPO")
    url = f"https://api.github.com/repos/{repo}/contents/public/guides/index.html"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    res = requests.get(url, headers=headers)
    sha = res.json().get('sha') if res.status_code == 200 else None
    data = {"message": "🤖 AION: Index Cleanup", "content": base64.b64encode(index_html.encode()).decode()}
    if sha: data["sha"] = sha
    requests.put(url, json=data, headers=headers)
    print("✅ 智库索引页已刷新。")

if __name__ == "__main__":
    generate()
