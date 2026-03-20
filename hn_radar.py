import requests
import json
from datetime import datetime, timedelta

def run_hn_radar():
    print("🚀 大龙虾雷达 3.0 启动：黑客之眼（Hacker News 专项）...")
    
    # 搜索过去 24 小时内的帖子
    # 关键词：OpenAI expensive, OpenAI cost, DeepSeek
    query = "OpenAI expensive"
    tags = "story" # 只看帖子，不看评论
    
    # 调用 Algolia 提供的 HN 搜索 API (无需 API Key)
    url = f"https://hn.algolia.com/api/v1/search_by_date?query={query}&tags={tags}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        hits = data.get('hits', [])
        
        print(f"✅ 侦察完成，在 Hacker News 发现 {len(hits)} 条相关讨论：")
        
        with open("real_leads.txt", "w") as f:
            for i, hit in enumerate(hits[:10], 1): # 取前 10 条
                title = hit.get('title')
                url = hit.get('url') or f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
                author = hit.get('author')
                points = hit.get('points')
                
                line = f"[{i}] {title} (热度: {points})\n👤 作者: {author}\n🔗 {url}\n"
                print(line)
                f.write(line + "\n")
                
        if not hits:
            print("⚠️ 当前关键词未发现新帖，建议更换关键词为 'DeepSeek' 再次尝试。")
            
    except Exception as e:
        print(f"❌ 侦察出错: {e}")

if __name__ == "__main__":
    run_hn_radar()
