import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

def update_github_sdk():
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPO")
    file_path = "seekapi.py"
    
    if not token or "ghp_" not in token:
        print("❌ 错误: .env 中没有找到有效的 GITHUB_TOKEN")
        return

    print(f"🚀 正在连接 GitHub 重构 SDK: {repo}...")

    # 1. 获取文件的 SHA (GitHub API 更新文件必须提供 SHA)
    url = f"https://api.github.com/repos/{repo}/contents/{file_path}"
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    
    res = requests.get(url, headers=headers)
    sha = res.json().get('sha') if res.status_code == 200 else None

    # 2. 真正的生产级 SDK 代码
    sdk_content = """import httpx
import os

class SeekAPI:
    \"\"\"SeekAPI.ai 官方 Python SDK - 跨境算力套利核心引擎\"\"\"
    def __init__(self, api_key=None, base_url="https://dash.seekapi.ai/v1"):
        self.api_key = api_key or os.getenv("SEEKAPI_API_KEY")
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def chat(self, model, messages, stream=False):
        \"\"\"调用推理算力 (支持 DeepSeek R1/V3)\"\"\"
        payload = {"model": model, "messages": messages, "stream": stream}
        with httpx.Client(timeout=60.0) as client:
            response = client.post(f"{self.base_url}/chat/completions", json=payload, headers=self.headers)
            return response.json()

    def get_balance(self):
        \"\"\"查询账户实时余额\"\"\"
        with httpx.Client() as client:
            response = client.get(f"{self.base_url}/user/quota", headers=self.headers)
            return response.json()
"""
    # 3. 提交到 GitHub
    encoded = base64.b64encode(sdk_content.encode('utf-8')).decode('utf-8')
    data = {"message": "🤖 OpenClaw: 自动重构 SDK 核心逻辑", "content": encoded}
    if sha: data["sha"] = sha

    put_res = requests.put(url, json=data, headers=headers)
    if put_res.status_code in [200, 201]:
        print("✅ GitHub 代码重构成功！你的 SDK 已正式上线。")
    else:
        print(f"❌ 重构失败: {put_res.text}")

if __name__ == "__main__":
    update_github_sdk()
