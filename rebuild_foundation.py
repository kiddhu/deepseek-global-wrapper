import requests
import base64
import json

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def rebuild():
    # 1. 强行创建一个基础的 package.json
    pkg_url = f"https://api.github.com/repos/{REPO}/contents/package.json"
    pkg_data = {
        "name": "seekapi-web",
        "version": "1.0.0",
        "scripts": {"dev": "next dev", "build": "next build", "start": "next start"},
        "dependencies": {
            "react": "latest",
            "react-dom": "latest",
            "next": "latest",
            "gray-matter": "latest",
            "next-mdx-remote": "latest"
        }
    }
    
    # 检查 package.json 是否存在
    res = requests.get(pkg_url, headers=HEADERS)
    payload = {
        "message": "AION: Rebuilding project foundation",
        "content": base64.b64encode(json.dumps(pkg_data, indent=2).encode()).decode()
    }
    if res.status_code == 200: payload["sha"] = res.json()['sha']
    requests.put(pkg_url, json=payload, headers=HEADERS)
    print("✅ package.json 已强行注入根目录")

    # 2. 部署一个“绝对安全”的 insights 页面 (不使用复杂插件)
    page_url = f"https://api.github.com/repos/{REPO}/contents/app/insights/page.jsx"
    safe_code = """
export default function TestPage() {
  return (
    <div style={{backgroundColor: '#000', color: '#fff', minHeight: '100vh', padding: '50px', textAlign: 'center'}}>
      <h1 style={{fontSize: '3rem', color: '#3b82f6'}}>AION Insights</h1>
      <p style={{fontSize: '1.5rem'}}>帝国基石已修复。正在等待内容同步...</p>
      <div style={{marginTop: '30px', border: '1px solid #333', padding: '20px'}}>
        <a href="/" style={{color: '#3b82f6'}}>返回首页</a>
      </div>
    </div>
  );
}
"""
    res_page = requests.get(page_url, headers=HEADERS)
    payload_page = {
        "message": "AION: Deploying safe-mode insights page",
        "content": base64.b64encode(safe_code.encode()).decode()
    }
    if res_page.status_code == 200: payload_page["sha"] = res_page.json()['sha']
    requests.put(page_url, json=payload_page, headers=HEADERS)
    print("✅ 安全模式 Insights 页面已部署")

if __name__ == "__main__":
    rebuild()
