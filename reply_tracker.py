import os
import json
import requests

# 这是一个简单的“已回复帖子”数据库
TRACKER_FILE = "tracked_threads.json"

def add_to_tracker(url, title):
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []
    
    if url not in [item['url'] for item in data]:
        data.append({"url": url, "title": title, "status": "posted"})
        with open(TRACKER_FILE, "w") as f:
            json.dump(data, f)
        print(f"✅ 已将帖子加入监控清单: {title}")

def check_replies():
    print("🕵️ 大龙虾正在回头检查你的帖子是否有新回复...")
    # 这里未来会集成 Playwright 去爬取你回复过的页面
    # 目前先作为逻辑占位
    print("🟢 目前暂无新回复。")

if __name__ == "__main__":
    check_replies()
