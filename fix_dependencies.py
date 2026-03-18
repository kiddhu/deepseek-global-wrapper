import requests
import base64
import json

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}"}

def update_package_json():
    url = f"https://api.github.com/repos/{REPO}/contents/package.json"
    res = requests.get(url, headers=HEADERS).json()
    content = json.loads(base64.b64decode(res['content']).decode('utf-8'))
    
    # 强制添加必要的解析插件
    if 'dependencies' not in content: content['dependencies'] = {}
    content['dependencies']['gray-matter'] = 'latest'
    content['dependencies']['next-mdx-remote'] = 'latest'
    
    new_content = json.dumps(content, indent=2)
    payload = {
        "message": "AION: Adding required dependencies",
        "content": base64.b64encode(new_content.encode('utf-8')).decode('utf-8'),
        "sha": res['sha']
    }
    requests.put(url, json=payload, headers=HEADERS)
    print("✅ package.json 已更新，Vercel 将自动重新安装插件并编译。")

if __name__ == "__main__":
    update_package_json()
