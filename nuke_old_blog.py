import requests

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def nuke():
    # 1. 获取 blog 文件夹下的所有文件
    url = f"https://api.github.com/repos/{REPO}/contents/blog"
    res = requests.get(url, headers=HEADERS).json()
    
    if isinstance(res, list):
        for file in res:
            # 逐个物理删除
            del_url = f"https://api.github.com/repos/{REPO}/contents/blog/{file['name']}"
            requests.delete(del_url, json={"message": "Nuking old blog junk", "sha": file['sha']}, headers=HEADERS)
            print(f"🔥 已铲除旧数据: {file['name']}")
        print("✅ blog 文件夹已清空。")
    else:
        print("ℹ️ blog 文件夹似乎已经不存在或已清空。")

if __name__ == "__main__":
    nuke()
