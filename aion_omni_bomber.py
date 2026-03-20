import os, requests, base64, time, random
from dotenv import load_dotenv

load_dotenv()

def get_science_hot_topics():
    print("📡 正在全球科学/技术库中搜寻前沿热点...")
    # 抓取 Hacker News 上的科技/科学类热门
    try:
        res = requests.get("https://hn.algolia.com/api/v1/search?query=science+OR+tech+OR+medicine&tags=story&hitsPerPage=5")
        hits = res.json()['hits']
        return random.choice(hits)['title']
    except:
        return "The Convergence of Quantum Computing and Biological Immortality"

def generate_omni_article(topic, lang_name, lang_code):
    print(f"🧠 AION 正在以 {lang_name} 撰写深度报告: {topic}...")
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")
    
    prompt = f"""
    You are AION, the Super Individual. 
    Write a 1500-word high-authority technical and visionary report in {lang_name}.
    
    Topic: {topic}
    Slogan: AION: The Era of the One.
    
    Strict Constraints:
    1. Focus ONLY on Science, Technology, Medicine, AI, Physics, or Cinema Technology.
    2. ABSOLUTELY NO Politics or Religion.
    3. Content: Analyze the breakthrough, then explain how AION's compute efficiency (SeekAPI.ai) accelerates this field.
    4. Tone: Authoritative, futuristic, and technical.
    5. Format: Clean HTML (h1, h2, p, blockquote).
    """

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}

    try:
        res = requests.post(f"{base_url}/chat/completions", json=payload, headers=headers, timeout=180)
        return res.json()['choices'][0]['message']['content']
    except:
        return None

def run_omni_bomber():
    # 覆盖你要求的所有语种
    languages = {
        "zh-CN": "Simplified Chinese",
        "zh-TW": "Traditional Chinese",
        "ja": "Japanese",
        "ru": "Russian",
        "es": "Spanish",
        "pt": "Portuguese",
        "vi": "Vietnamese",
        "th": "Thai",
        "ar": "Arabic",
        "fr": "French",
        "de": "German"
    }
    
    topic = get_science_hot_topics()
    repo = os.getenv("GITHUB_REPO")
    token = os.getenv("GITHUB_TOKEN")

    # 每次运行随机挑选 5 种语言进行轰炸
    selected_langs = random.sample(list(languages.items()), 5)

    for lang_code, lang_name in selected_langs:
        body = generate_omni_article(topic, lang_name, lang_code)
        if not body: continue
        
        file_name = f"omni-{lang_code}-{int(time.time())}.html"
        full_html = f"<html><body style='font-family:sans-serif;line-height:1.8;max-width:900px;margin:0 auto;padding:60px;background:#000;color:#eee;'><h1>{topic}</h1>{body}<hr><p style='text-align:center;color:#444;'>AION: The Era of the One.</p></body></html>"
        
        # 推送 GitHub
        url = f"https://api.github.com/repos/{repo}/contents/public/guides/{file_name}"
        data = {"message": f"🤖 AION Omni Bomber: {lang_name}", "content": base64.b64encode(full_html.encode('utf-8')).decode()}
        res = requests.get(url, headers={"Authorization": f"Bearer {token}"})
        sha = res.json().get('sha') if res.status_code == 200 else None
        if sha: data["sha"] = sha
        requests.put(url, json=data, headers={"Authorization": f"Bearer {token}"})
        
        # 本地存一份
        local_path = f"/root/OpenClaw/public/guides/{file_name}"
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, "w", encoding='utf-8') as f: f.write(full_html)
        print(f"✅ {lang_name} 版本已空投。")

if __name__ == "__main__":
    run_omni_bomber()
