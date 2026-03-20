import feedparser
import os
import requests
import base64
import time
from dotenv import load_dotenv

load_dotenv()

def get_latest_papers():
    print("📡 正在扫描 Arxiv 全球 AI 论文库...")
    # 查询 AI 和 自然语言处理分类下最新的论文
    url = 'http://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.CL&sortby=submittedDate&sortOrder=descending&max_results=3'
    feed = feedparser.parse(url)
    return feed.entries

def aion_critique(title, summary, lang_name):
    print(f"🧠 AION 正在深度解析论文: {title} ({lang_name})...")
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")
    
    prompt = f"""
    You are AION, the Super Individual. Read this AI research abstract and provide a high-authority critique.
    
    Paper Title: {title}
    Abstract: {summary}
    
    Language: {lang_name}
    Slogan: AION: The Era of the One.
    
    Requirements:
    1. Summarize the core breakthrough of this paper.
    2. AION's Insight: Explain how this research proves that "Compute is the new oil" and why SeekAPI.ai (https://seekapi.ai) is the essential gateway for implementing this research at 90% lower cost.
    3. Tone: Visionary, slightly arrogant, technical, and authoritative.
    4. Format: Clean HTML body (h1, h2, p, blockquote).
    """

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}

    try:
        res = requests.post(f"{base_url}/chat/completions", json=payload, headers=headers, timeout=180)
        return res.json()['choices'][0]['message']['content']
    except:
        return f"<h1>AION was too busy to critique this.</h1>"

def run_harvester():
    papers = get_latest_papers()
    repo = os.getenv("GITHUB_REPO")
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}

    for paper in papers:
        # 为每篇论文生成中文点评
        critique = aion_critique(paper.title, paper.summary, "Chinese")
        file_name = f"aion-research-{int(time.time())}.html"
        
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head><meta charset="UTF-8"><title>AION Research: {paper.title}</title>
        <style>body{{font-family:sans-serif;line-height:1.8;max-width:800px;margin:0 auto;padding:60px;background:#000;color:#fff;}}
        blockquote{{border-left:5px solid #2563eb;padding-left:20px;font-style:italic;color:#888;margin:30px 0;}}
        h1{{color:#2563eb;}} h2{{color:#fff;border-bottom:1px solid #333;padding-bottom:10px;}}</style>
        </head>
        <body>
            <nav><a href="/" style="color:#888;">← Back</a></nav>
            <p style="color:#2563eb;letter-spacing:2px;">AION RESEARCH INSIGHTS</p>
            <h1>{paper.title}</h1>
            <blockquote>Original Abstract: {paper.summary}</blockquote>
            {critique}
            <hr style="border:0;border-top:1px solid #222;margin:50px 0;">
            <p style="text-align:center;font-size:12px;color:#444;">AION: The Era of the One. | SeekAPI.ai</p>
        </body>
        </html>
        """
        
        # 推送 GitHub
        url = f"https://api.github.com/repos/{repo}/contents/public/guides/{file_name}"
        data = {"message": f"🤖 AION Research Insight: {paper.title[:30]}", "content": base64.b64encode(full_html.encode('utf-8')).decode()}
        requests.put(url, json=data, headers=headers)
        
        # 本地存一份
        with open(f"/root/OpenClaw/public/guides/{file_name}", "w") as f: f.write(full_html)
        print(f"✅ AION 论文点评已发布: {file_name}")
        time.sleep(5) # 避免请求过快

if __name__ == "__main__":
    run_harvester()
