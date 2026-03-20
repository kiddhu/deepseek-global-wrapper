import os
import requests
from dotenv import load_dotenv

load_dotenv()

def generate_outreach():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")
    
    print("🧠 大龙虾大脑正在重新装填精准子弹...")

    with open("real_leads.txt", "r") as f:
        leads = f.read()

    prompt = f"""
    下面是3个AI项目讨论：
    {leads}
    
    请针对这3个项目，分别写一段专业的英文评论。
    要求：
    1. 语气专业，针对项目痛点。
    2. 提到 SeekAPI.ai 能降低 90% 成本且 100% 兼容 OpenAI。
    3. 重要：每段话术之间必须用 '|||' 符号隔开！不要写“针对项目1”之类的标题。
    """

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(f"{base_url}/chat/completions", json=payload, headers=headers)
        content = response.json()['choices'][0]['message']['content']
        with open("outreach_messages.txt", "w") as f:
            f.write(content)
        print("✅ 子弹装填完毕。")
    except Exception as e:
        print(f"❌ 出错: {e}")

if __name__ == "__main__":
    generate_outreach()
