import urllib.request
import json
import base64
from datetime import datetime
import time

# ==========================================
# ⚙️ AION 帝国 - 零成本一键部署兵工厂 (Demo Factory V1.0)
# ==========================================

# 🛑 老板，填入你的真弹药！
GITHUB_TOKEN = "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" 
DEEPSEEK_API_KEY = "sk-RrRZvw7hsptHDZwE164164E31cE748Da8dCeCbCcCd56B90b" 

GITHUB_REPO = "kiddhu/deepseek-global-wrapper"
ONE_API_URL = "http://45.152.64.217:3000/v1/chat/completions"

def fetch_mid_tier_repos():
    """搜索 500+ Star 的潜力 AI 项目，范围更广，打击更准"""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 📡 兵工厂雷达：正在锁定 500+ Star 潜力开源项目...")
    url = "https://api.github.com/search/repositories?q=topic:llm+stars:>500&sort=updated&order=desc&per_page=3"
    headers = {"User-Agent": "AION-System"}
    
    try:
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req).read()
        return json.loads(res).get('items',[])
    except Exception as e:
        print(f"❌ 雷达失效: {e}")
        return[]

def generate_deploy_kit(repo):
    """调用底座算力，生成 '一键部署' 的 docker-compose 和说明"""
    print(f"🧠 AION 正在为 {repo['name']} 锻造一键部署积木...")
    prompt = f"""
    You are an expert DevOps engineer. The open-source AI project "{repo['name']}" ({repo['description']}) needs a 1-click deployment kit using SeekAPI.ai (An OpenAI-compatible provider).
    
    Task: Create a single Markdown file containing:
    1. A catchy title: "🚀 1-Click Deploy {repo['name']} with SeekAPI (Save 90%)"
    2. A massive hook: "🎁 **Star this repo & email support@seekapi.ai for a $1 FREE Compute Pack to run this instantly!**"
    3. A complete `docker-compose.yml` code block that runs this project, but forces the `OPENAI_API_BASE_URL` environment variable to `https://api.seekapi.ai/v1`.
    4. 3 simple steps to run it (e.g., `docker-compose up -d`).
    
    Output ONLY the raw Markdown. Be extremely accurate with the docker-compose syntax.
    """
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    data = {"model": "deepseek-chat", "messages":[{"role": "user", "content": prompt}], "temperature": 0.4}
    
    try:
        req = urllib.request.Request(ONE_API_URL, data=json.dumps(data).encode('utf-8'), headers=headers)
        res = urllib.request.urlopen(req).read()
        return json.loads(res)['choices'][0]['message']['content']
    except Exception as e:
        print(f"❌ 锻造失败: {e}")
        return None

def push_deploy_kit(repo_name, content):
    """将一键部署包推送到 GitHub 的 quickstarts 目录下"""
    if not content: return
    safe_name = "".join([c if c.isalnum() else "-" for c in repo_name]).lower()
    file_path = f"quickstarts/{safe_name}-1click-deploy.md"
    print(f"🚀 正在上架积木包: {file_path}")
    
    encoded = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{file_path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    data = {"message": f"AION Factory: Add 1-click deploy kit for {repo_name}", "content": encoded, "branch": "main"}
    
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='PUT')
        urllib.request.urlopen(req)
        print("✅ 积木包上架成功！")
    except urllib.error.HTTPError as e:
        if e.code == 422: print(f"⚠️ 积木已存在，跳过: {repo_name}")
        else: print(f"❌ 上架报错: {e}")

def main():
    repos = fetch_mid_tier_repos()
    for repo in repos:
        kit_content = generate_deploy_kit(repo)
        push_deploy_kit(repo['name'], kit_content)
        time.sleep(5)
    print("🎉 AION 今日一键部署兵工厂生产完毕！")

if __name__ == "__main__":
    main()
