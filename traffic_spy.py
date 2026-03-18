import requests
import os
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def get_stats():
    print("📡 正在通过 GraphQL 协议提取流量数据...")
    zone_id = os.getenv("CF_ZONE_ID")
    api_token = os.getenv("CF_API_TOKEN")
    url = "https://api.cloudflare.com/client/v4/graphql"
    
    # 获取昨天的日期
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    # Cloudflare GraphQL 查询语句
    query = """
    query {
      viewer {
        zones(filter: {zoneTag: "%s"}) {
          httpRequests1dGroups(limit: 1, filter: {date_gt: "%s"}) {
            sum {
              requests
              pageViews
            }
            uniq {
              uniques
            }
          }
        }
      }
    }
    """ % (zone_id, yesterday)

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    try:
        res = requests.post(url, json={'query': query}, headers=headers)
        result = res.json()
        
        if 'errors' in result and result['errors']:
            print(f"❌ GraphQL 报错: {result['errors'][0]['message']}")
            return

        data = result['data']['viewer']['zones'][0]['httpRequests1dGroups'][0]
        
        stats = f"--- 过去 24 小时流量报告 (GraphQL) ---\n"
        stats += f"🚀 总请求数: {data['sum']['requests']}\n"
        stats += f"👥 唯一访客: {data['uniq']['uniques']}\n"
        stats += f"📄 页面浏览: {data['sum']['pageViews']}\n"
        stats += f"🕒 更新时间: {datetime.now().strftime('%H:%M:%S')}"
        
        with open("traffic_stats.txt", "w") as f:
            f.write(stats)
        print("✅ 流量数据已成功更新。")
        
    except Exception as e:
        print(f"❌ 脚本崩溃: {e}")

if __name__ == "__main__":
    get_stats()
