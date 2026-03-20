import os
import requests
from dotenv import load_dotenv

load_dotenv()

def list_all_repos():
    token = os.getenv("GITHUB_TOKEN")
    print("🔍 正在从 GitHub 调取你的所有仓库清单（含私有）...")
    
    # 获取所有仓库，按更新时间排序
    url = "https://api.github.com/user/repos?per_page=100&sort=updated"
    headers = {"Authorization": f"Bearer {token}"}
    
    res = requests.get(url, headers=headers)
    
    if res.status_code != 200:
        print(f"❌ 无法连接 GitHub，请检查 Token 是否正确。错误: {res.text}")
        return

    repos = res.json()
    print("\n--- 你的仓库清单 ---")
    for i, r in enumerate(repos, 1):
        print(f"[{i}] 名字: {r['full_name']}  (私有: {r['private']})")
    
    print("\n💡 提示：请在上面列表中找到那个和 v0 相关的名字，并告诉我。")

if __name__ == "__main__":
    list_all_repos()
