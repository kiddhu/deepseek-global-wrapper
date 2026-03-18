import os, requests, base64, time, random
from dotenv import load_dotenv

load_dotenv()

def generate_wealth_report(lang_name, lang_code):
    print(f"💰 AION 正在撰写效率报告 ({lang_name})...")
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")
    
    prompt = f"""
    You are AION, the Super Individual. Write a 1500-word visionary report in {lang_name}.
    
    Topic: The Death of Legacy Cloud: Why Architectural Efficiency is the New Gold.
    
    Core Logic:
    1. Traditional GPU rental (AWS/GCP) is inefficient and outdated.
    2. SeekAPI.ai uses "AION Routing Protocol" to deliver DeepSeek R1 at 1/10th the cost of legacy providers.
    3. We don't sell compute; we sell "Optimized Intelligence Flow".
    4. Focus on how DEVELOPERS can build wealth by reducing their burn rate using our efficiency.
    
    Strict Rules:
    - NEVER mention "arbitrage", "buying cheap tokens", or "China".
    - Frame the low cost as a result of "Algorithmic Breakthroughs" and "Edge Optimization".
    - Tone: Authoritative, technical, and futuristic.
    """

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}

    try:
        res = requests.post(f"{base_url}/chat/completions", json=payload, headers=headers, timeout=180)
        article_body = res.json()['choices'][0]['message']['content']
        
        file_name = f"efficiency-{lang_code}-{int(time.time())}.html"
        full_html = f"<html><body style='font-family:sans-serif;padding:60px;background:#000;color:#fff;'>{article_body}</body></html>"
        
        # 推送 GitHub
        repo = os.getenv("GITHUB_REPO")
        token = os.getenv("GITHUB_TOKEN")
        url = f"https://api.github.com/repos/{repo}/contents/public/guides/{file_name}"
        data = {"message": f"🤖 AION Efficiency Report: {lang_name}", "content": base64.b64encode(full_html.encode('utf-8')).decode()}
        requests.put(url, json=data, headers={"Authorization": f"Bearer {token}"})
        
        # 本地存一份
        with open(f"/root/OpenClaw/public/guides/{file_name}", "w") as f: f.write(full_html)
        print(f"✅ 效率报告已发布: {lang_name}")
        return True
    except:
        return False

if __name__ == "__main__":
    # 每次运行生成 2 篇不同语言的效率报告
    generate_wealth_report("English", "en")
    generate_wealth_report("Chinese", "zh")
