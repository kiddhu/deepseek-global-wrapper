import requests

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def nuke_junk():
    url = f"https://api.github.com/repos/{REPO}/contents/blog"
    res = requests.get(url, headers=HEADERS).json()
    
    if not isinstance(res, list): return

    for file in res:
        name = file['name']
        # 如果文件名不是以 "202" (代表202x年) 开头，或者是旧的 insight_ 开头，则删除
        if not name.startswith("202") or name.startswith("insight_"):
            print(f"🔥 正在清理垃圾文件: {name}")
            requests.delete(file['url'], json={"message": "Cleanup junk", "sha": file['sha']}, headers=HEADERS)

    print("✅ 清理完成！现在您的 Blog 列表将只显示专业的日期标题。")

if __name__ == "__main__":
    nuke_junk()
