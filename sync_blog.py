import os
import requests
from dotenv import load_dotenv

load_dotenv()

def check_blog_visibility():
    print("🌐 正在检查 SeekAPI 官网博客同步状态...")
    repo = os.getenv("GITHUB_REPO")
    url = f"https://api.github.com/repos/{repo}/contents/blog-post.md"
    
    res = requests.get(url)
    if res.status_code == 200:
        print("✅ 发现大龙虾撰写的博客文件：blog-post.md")
        print(f"🔗 请检查你的官网：https://seekapi.ai/blog (如果尚未配置该页面，请告知架构师)")
    else:
        print("❌ 尚未在仓库中发现博客文件，请运行 content_factory.py")

if __name__ == "__main__":
    check_blog_visibility()
