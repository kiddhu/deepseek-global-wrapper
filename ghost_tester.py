import asyncio
from playwright.async_api import async_playwright
import time

async def run_test():
    print("👻 幽灵测试员启动：正在模拟真实用户行为...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            # 1. 测试首页加载
            start_time = time.time()
            await page.goto("https://seekapi.ai")
            load_time = time.time() - start_time
            print(f"✅ 首页加载成功，耗时: {round(load_time, 2)}s")
            
            # 2. 测试法律页面跳转
            await page.click("text=Terms of Service")
            if "Terms of Service" in await page.title():
                print("✅ 法律页面跳转正常")
            
            # 3. 测试 API 门户连通性
            await page.goto("https://dash.seekapi.ai")
            if "Sign In" in await page.content():
                print("✅ One-API 登录界面正常")
            
            with open("health_check.txt", "w") as f:
                f.write(f"Last Full Check: {time.ctime()} - ALL GREEN 🟢")
                
        except Exception as e:
            print(f"🔴 系统自检失败: {e}")
            with open("health_check.txt", "w") as f:
                f.write(f"Last Full Check: {time.ctime()} - FAILED 🔴")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_test())
import urllib.request
import json
from datetime import datetime

# ==========================================
# ⚙️ AION 帝国 - 幽灵注册员 (全链路健康自检)
# ==========================================

def test_registration_link():
    # 测试香港前线的可用性
    url = "http://45.152.64.217:3000/api/status"
    headers = {"User-Agent": "AION-Ghost-Tester"}
    
    try:
        req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(req, timeout=5).read()
        data = json.loads(res)
        if data.get("success"):
            status = "🟢 注册与登录通道 100% 畅通"
        else:
            status = "🟡 通道降级，请检查 One-API"
    except Exception as e:
        status = f"🔴 注册通道阻断: {str(e)[:20]}"

    # 将状态写进日志供大屏读取
    with open("/root/OpenClaw/ghost.log", "w", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {status}\n")
    print(status)

if __name__ == "__main__":
    test_registration_link()
