import requests
import base64
import os

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def clone_and_fix():
    # 1. 读取现有的 blog 页面模板
    blog_page_url = f"https://api.github.com/repos/{REPO}/contents/app/blog/page.jsx"
    res = requests.get(blog_page_url, headers=HEADERS)
    
    if res.status_code != 200:
        print("❌ 找不到 app/blog/page.jsx，请检查路径")
        return

    # 2. 替换逻辑：把所有的 blog 换成 insights
    content = base64.b64decode(res.json()['content']).decode('utf-8')
    new_content = content.replace("'blog'", "'insights'").replace('"blog"', '"insights"')
    
    # 3. 在 GitHub 创建新文件夹和文件 app/insights/page.jsx
    new_page_url = f"https://api.github.com/repos/{REPO}/contents/app/insights/page.jsx"
    
    # 检查是否已存在
    check_res = requests.get(new_page_url, headers=HEADERS)
    payload = {
        "message": "AION: Creating physical insights page",
        "content": base64.b64encode(new_content.encode('utf-8')).decode('utf-8')
    }
    if check_res.status_code == 200:
        payload["sha"] = check_res.json()['sha']

    put_res = requests.put(new_page_url, json=payload, headers=HEADERS)
    if put_res.status_code in [200, 201]:
        print("✅ 成功创建 app/insights/page.jsx！前端抽水管已接通。")
    else:
        print(f"❌ 创建失败: {put_res.text}")

if __name__ == "__main__":
    clone_and_fix()
