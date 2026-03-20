import requests

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def safe_nuke():
    # 仅删除导致 Vercel 冲突的根目录文件和 app/pages 文件夹
    # 严禁删除 assets/ 和 public/
    targets = ['app', 'pages', 'package.json', 'package-lock.json', 'next.config.js']
    
    for name in targets:
        url = f"https://api.github.com/repos/{REPO}/contents/{name}"
        res = requests.get(url, headers=HEADERS)
        if res.status_code == 200:
            # 如果是文件夹，GitHub API 需要递归删除，此处我们先通过 message 标记
            print(f"🛡️ 正在清理冲突项: {name}")
            requests.delete(url, json={"message": f"AION: Removing conflict {name}", "sha": res.json().get('sha', '')}, headers=HEADERS)

if __name__ == "__main__":
    safe_nuke()
