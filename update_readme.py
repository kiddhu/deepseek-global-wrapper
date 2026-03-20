import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

def update_readme():
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPO")
    url = f"https://api.github.com/repos/{repo}/contents/README.md"
    headers = {"Authorization": f"Bearer {token}"}
    
    # 获取旧 SHA
    res = requests.get(url, headers=headers)
    sha = res.json().get('sha')

    new_content = """
# 🚀 SeekAPI.ai - Global DeepSeek R1/V3 Gateway

### 🎁 Limited Time Offer: Get $1.00 Free Credit!
**How to claim:**
1. **Star** this repository.
2. Our AI Agent (OpenClaw) will detect your star.
3. DM us on X (@YourXAccount) or email support@seekapi.ai with your GitHub username to get your redemption code!

---
- **90% Cheaper** than OpenAI.
- **100% Compatible** with OpenAI SDKs.
- **No KYC** required.
"""
    
    data = {
        "message": "🤖 OpenClaw: 增加 Star 奖励说明",
        "content": base64.b64encode(new_content.encode()).decode(),
        "sha": sha
    }
    requests.put(url, json=data, headers=headers)
    print("✅ GitHub README 已更新，诱饵已撒下！")

if __name__ == "__main__":
    update_readme()
