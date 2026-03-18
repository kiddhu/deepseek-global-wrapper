import requests
import base64

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def update_footer():
    url = f"https://api.github.com/repos/{REPO}/contents/assets/footer.html"
    res = requests.get(url, headers=HEADERS).json()
    if 'content' not in res: return
    content = base64.b64decode(res['content']).decode('utf-8')
    # 将 AION Insights 的指向从 /insights 改为 /blog
    new_content = content.replace('href="/insights"', 'href="/blog"')
    payload = {
        "message": "AION: Update footer link to /blog",
        "content": base64.b64encode(new_content.encode('utf-8')).decode('utf-8'),
        "sha": res['sha']
    }
    requests.put(url, json=payload, headers=HEADERS)
    print("✅ 终端操作成功：GitHub 页脚链接已修正。")

if __name__ == "__main__":
    update_footer()
