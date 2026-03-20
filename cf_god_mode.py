import requests

# 您的新 Token
TOKEN = "lYlApayAuQgzY7sUoHHpQ_mQHNK7qCQ4P7dK4d3H"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

def run_mission():
    print("🚀 正在验证 Token 并搜索区域...")
    
    # 1. 自动获取所有区域，寻找 seekapi.ai
    zones_res = requests.get("https://api.cloudflare.com/client/v4/zones", headers=HEADERS).json()
    
    if not zones_res.get('success'):
        print(f"❌ Token 验证失败: {zones_res.get('errors')}")
        return

    target_zone = None
    for zone in zones_res.get('result', []):
        if zone['name'] == 'seekapi.ai':
            target_zone = zone['id']
            break
    
    if not target_zone:
        print("❌ 在您的账户中未找到 seekapi.ai，请检查 Token 权限是否包含该区域。")
        return

    print(f"✅ 锁定目标区域 ID: {target_zone}")

    # 2. 寻找并删除拦截路由
    routes_url = f"https://api.cloudflare.com/client/v4/zones/{target_zone}/workers/routes"
    routes = requests.get(routes_url, headers=HEADERS).json().get('result', [])
    
    for route in routes:
        if 'insights' in route['pattern'] or 'blog' in route['pattern']:
            del_res = requests.delete(f"{routes_url}/{route['id']}", headers=HEADERS).json()
            if del_res.get('success'):
                print(f"🔥 已物理粉碎拦截路由: {route['pattern']}")

    # 3. 强制刷新全球缓存
    purge_url = f"https://api.cloudflare.com/client/v4/zones/{target_zone}/purge_cache"
    purge_res = requests.post(purge_url, headers=HEADERS, json={"purge_everything": True}).json()
    if purge_res.get('success'):
        print("✨ Cloudflare 全球边缘节点已完成清场！")
        print("\n--- 任务成功：请在 30 秒后访问 https://seekapi.ai/insights ---")

if __name__ == "__main__":
    run_mission()
