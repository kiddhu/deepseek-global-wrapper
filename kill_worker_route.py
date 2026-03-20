import requests
import json

ZONE_ID = "911409f583f766e9526e033322d645e2"
TOKEN = "lYlApayAuQgzY7sUoHHpQ_mQHNK7qCQ4P7dK4d3H"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

def execute_cleanup():
    # 获取所有路由
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/workers/routes"
    res = requests.get(url, headers=HEADERS).json()
    
    if not res.get('success'):
        print(f"❌ 授权失败: {res.get('errors')}")
        return

    routes = res.get('result', [])
    found = False
    for route in routes:
        pattern = route.get('pattern', '')
        # 锁定所有拦截 insights 和 blog 的旧路由
        if 'insights' in pattern or 'blog' in pattern:
            del_url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/workers/routes/{route['id']}"
            del_res = requests.delete(del_url, headers=HEADERS).json()
            if del_res.get('success'):
                print(f"✅ 成功斩断拦截路由: {pattern}")
                found = True
    
    if not found:
        print("ℹ️ 未发现残留拦截路由，路径已纯净。")

    # 强制执行全球缓存刷新
    purge_url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/purge_cache"
    purge_res = requests.post(purge_url, headers=HEADERS, json={"purge_everything": True}).json()
    if purge_res.get('success'):
        print("✅ Cloudflare 全球边缘节点缓存已清空！")

if __name__ == "__main__":
    execute_cleanup()
