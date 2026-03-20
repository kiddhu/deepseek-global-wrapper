import os
import requests
import base64

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"

def update_github_file(path, old_str, new_str):
    url = f"https://api.github.com/repos/{REPO}/contents/{path}"
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        content = base64.b64decode(res.json()['content']).decode('utf-8')
        new_content = content.replace(old_str, new_str)
        
        payload = {
            "message": f"Redirecting {path} to insights",
            "content": base64.b64encode(new_content.encode('utf-8')).decode('utf-8'),
            "sha": res.json()['sha']
        }
        requests.put(url, json=payload, headers=headers)
        print(f"✅ 已修正文件路径: {path}")

# 尝试修正可能存在路径引用的核心文件
# 根据 v0.dev 惯例，通常在 app/insights/page.tsx 或类似位置
update_github_file("app/blog/page.tsx", "blog", "insights")
update_github_file("seekapi.py", "blog", "insights")
