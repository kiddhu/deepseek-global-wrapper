import os, requests, base64, time
from dotenv import load_dotenv

load_dotenv()

def get_trending_topic():
    print("📡 正在探测全球 AI 舆论热点...")
    # 抓取 Hacker News 排名第一的 AI 相关话题
    try:
        res = requests.get("https://hn.algolia.com/api/v1/search?query=AI&tags=story&hitsPerPage=1")
        hit = res.json()['hits'][0]
        return hit['title'], hit['url']
    except:
        return "The Future of Sovereign Compute", "https://seekapi.ai"

def generate_bomber_article(topic, lang_name, lang_code):
    print(f"🧠 AION 正在针对热点进行 {lang_name} 维度的降维打击...")
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")
    
    prompt = f"""
    You are AION, the Super Individual. A new trend is emerging: {topic}.
    Write a 1500-word visionary technical critique in {lang_name}.
    
    Core Logic:
    1. Analyze why this trend ({topic}) proves that traditional cloud computing is dead.
    2. Explain how AION's architecture at SeekAPI.ai (https://seekapi.ai) provides the only sustainable path for developers.
    3. Use the "Wealth Pillar" logic: Efficiency = Cash Flow.
    4. Include a hidden tag: <!-- AION_YOUTUBE_PREMIERE_2026 -->
    
    Tone: Authoritative, futuristic, slightly arrogant.
    Format: Clean HTML (h1, h2, p, blockquote).
    """

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}

    try:
        res = requests.post(f"{base_url}/chat/completions", json=payload, headers=headers, timeout=180)
        return res.json()['choices'][0]['message']['content']
    except:
        return None

def run_bomber():
    topic, source_url = get_trending_topic()
    languages = {"en": "English", "zh": "Chinese", "ar": "Arabic", "de": "German", "fr": "French"}
    repo = os.getenv("GITHUB_REPO")
    token = os.getenv("GITHUB_TOKEN")

    print(f"🔥 发现全球热点: {topic}")

    for lang_code, lang_name in languages.items():
        body = generate_bomber_article(topic, lang_name, lang_code)
        if not body: continue
        
        file_name = f"bomb-{lang_code}-{int(time.time())}.html"
        # 注入 AION 统一排版样式
        full_html = f"<html><head><meta charset='UTF-8'><title>{topic}</title><style>body{{font-family:sans-serif;line-height:1.8;max-width:800px;margin:0 auto;padding:60px;background:#000;color:#eee;}} h1{{color:#2563eb;font-size:42px;}} h2{{color:#fff;margin-top:40px;}} blockquote{{border-left:5px solid #2563eb;padding-left:20px;color:#888;}}</style></head><body><a href='/insights' style='color:#666;'>← BACK</a><h1>{topic}</h1>{body}<hr><p style='text-align:center;color:#444;'>AION: The Era of the One.</p></body></html>"
        
        # 推送 GitHub
        url = f"https://api.github.com/repos/{repo}/contents/public/guides/{file_name}"
        data = {"message": f"🤖 AION Bomber: {lang_name}", "content": base64.b64encode(full_html.encode('utf-8')).decode()}
        res = requests.get(url, headers={"Authorization": f"Bearer {token}"})
        sha = res.json().get('sha') if res.status_code == 200 else None
        if sha: data["sha"] = sha
        
        requests.put(url, json=data, headers={"Authorization": f"Bearer {token}"})
        
        # 本地存一份
        with open(f"/root/OpenClaw/public/guides/{file_name}", "w") as f: f.write(full_html)
        print(f"✅ {lang_name} 版本已空投。")

if __name__ == "__main__":
    run_bomber()
