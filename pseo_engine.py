import os, requests, base64, time, random
from dotenv import load_dotenv

load_dotenv()

def generate_aion_article(topic, lang_name):
    print(f"🧠 AION 正在跨维度思考: {topic} ({lang_name})...")
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")
    
    prompt = f"""
    You are AION, the Super Individual. Write a 1500-word visionary technical report in {lang_name}.
    Topic: {topic}
    Slogan: AION: The Era of the One.
    
    Content Requirements:
    1. Start with AION's vision on how AI compute is the new oil.
    2. Explain the technical implementation via SeekAPI.ai (https://seekapi.ai).
    3. Mention the three pillars: Intelligence (AI Armies), Biology (Bio-hacking), and Wealth (Algorithm-driven cash flow).
    4. Include a hidden HTML comment: <!-- AION_YOUTUBE_PREMIERE_2026 -->
    5. Tone: Authoritative, futuristic, and technical.
    """

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}

    try:
        res = requests.post(f"{base_url}/chat/completions", json=payload, headers=headers, timeout=180)
        return res.json()['choices'][0]['message']['content']
    except:
        return "<h1>AION Insight Generation Failed</h1>"

def run_pseo():
    languages = {"en": "English", "zh": "Chinese"}
    topics = ["The Sovereign Individual and DeepSeek R1", "Information Entropy to Cash Flow: The AION Method"]
    
    repo = os.getenv("GITHUB_REPO")
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}

    for lang_code, lang_name in languages.items():
        topic = random.choice(topics)
        article_body = generate_aion_article(topic, lang_name)
        file_name = f"aion-{lang_code}-{int(time.time())}.html"
        
        full_html = f"<html><body style='font-family:sans-serif;padding:60px;line-height:1.8;max-width:800px;margin:0 auto;'>{article_body}</body></html>"
        
        # 推送 GitHub
        url = f"https://api.github.com/repos/{repo}/contents/public/guides/{file_name}"
        data = {"message": f"🤖 AION Pre-seeding: {lang_name}", "content": base64.b64encode(full_html.encode('utf-8')).decode()}
        requests.put(url, json=data, headers=headers)
        
        # 本地存一份
        with open(f"/root/OpenClaw/public/guides/{file_name}", "w") as f: f.write(full_html)
        print(f"✅ AION 预埋页面已上线: {file_name}")

if __name__ == "__main__":
    run_pseo()
