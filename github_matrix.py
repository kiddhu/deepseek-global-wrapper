import urllib.request
import json
import base64
from datetime import datetime
import time
import os

# ==========================================
# ⚙️ AION 帝国 - GitHub 生态截流与矩阵生成器 (V1.0)
# ==========================================

# 🛑 请通过环境变量注入密钥（不要把 Token 写进仓库）
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
GITHUB_REPO = "kiddhu/deepseek-global-wrapper"
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "").strip()
ONE_API_URL = "http://45.152.64.217:3000/v1/chat/completions"

def fetch_trending_ai_repos():
    """搜索 GitHub 上最近更新且高 Star 的 OpenAI 兼容项目"""
    print("📡 AION 雷达正在扫描 GitHub 爆款 AI 项目...")
    # 搜索包含 "openai api" 的高赞项目
    url = "https://api.github.com/search/repositories?q=openai+api+topic:llm&sort=stars&order=desc&per_page=3"
    headers = {"User-Agent": "AION-System-Core"}
    
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req).read()
    data = json.loads(response)
    
    repos = []
    for item in data.get('items',[]):
        repos.append({
            "name": item['name'],
            "full_name": item['full_name'],
            "description": item['description'] or "An awesome AI project",
            "url": item['html_url']
        })
    return repos

def generate_integration_guide(repo):
    """调用 DeepSeek 生成无缝接入 SeekAPI 的教程，并植入 Star 诱饵"""
    print(f"🧠 AION 正在生成截流教程: {repo['name']}")
    prompt = f"""
    You are a DevRel engineer at SeekAPI.ai. Write a short, highly practical Markdown tutorial on how to use the open-source project "{repo['name']}" ({repo['description']}) with SeekAPI's OpenAI-compatible endpoint.
    
    Requirements:
    1. Title: "How to use {repo['name']} with SeekAPI (Save 90% on API Costs)"
    2. Add a prominent hook at the very beginning: "🎁 **BONUS:** Star this repository (kiddhu/deepseek-global-wrapper) and email your GitHub handle to support@seekapi.ai to receive a **$2 Free Compute Pack** instantly!"
    3. Provide the exact Base URL they need to use: `https://api.seekapi.ai/v1`
    4. Provide fake API Key examples: `sk-your-seekapi-key`
    5. Output ONLY the raw Markdown text. No extra conversational text.
    """
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5
    }
    
    req = urllib.request.Request(ONE_API_URL, data=json.dumps(data).encode('utf-8'), headers=headers)
    response = urllib.request.urlopen(req).read()
    result = json.loads(response)
    return result['choices'][0]['message']['content']

def push_to_github(repo_name, content):
    """将教程推送到仓库的 integrations 目录下"""
    print(f"🚀 正在部署矩阵资产: {repo_name}-integration.md")
    if not GITHUB_TOKEN:
        raise RuntimeError("Missing GITHUB_TOKEN env var for GitHub writes.")
    safe_name = "".join([c if c.isalnum() else "-" for c in repo_name]).lower()
    file_path = f"integrations/{safe_name}-guide.md"
    
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{file_path}"
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # 检查文件是否已存在（简化版：直接尝试创建，如果存在就忽略报错，说明之前搞过了）
    data = {
        "message": f"AION Auto-Matrix: Add integration guide for {repo_name}",
        "content": encoded_content,
        "branch": "main"
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers, method='PUT')
    try:
        urllib.request.urlopen(req)
        print("✅ 矩阵资产部署成功！")
    except urllib.error.HTTPError as e:
        if e.code == 422:
            print(f"⚠️ 文件已存在，跳过: {repo_name}")
        else:
            print(f"❌ 部署失败: {e}")

def main():
    repos = fetch_trending_ai_repos()
    for repo in repos:
        md_content = generate_integration_guide(repo)
        push_to_github(repo['name'], md_content)
        time.sleep(10)
    print("🎉 AION 今日 GitHub 截流矩阵部署完毕！")

if __name__ == "__main__":
    main()
