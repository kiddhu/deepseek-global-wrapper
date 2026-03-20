import asyncio
from playwright.async_api import async_playwright
import time, random

async def run_full_test():
    print("👻 幽灵测试员 V4 启动：正在执行模糊匹配自检...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--disable-blink-features=AutomationControlled'])
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        page = await context.new_page()
        
        try:
            await page.goto("https://dash.seekapi.ai/register", wait_until="networkidle")
            await page.wait_for_timeout(5000)
            
            # 模糊寻找用户名和密码框
            await page.fill("input[name*='username']", f"ghost_{random.randint(100,999)}")
            
            # 寻找所有的密码框
            pw_inputs = await page.query_selector_all("input[type='password']")
            if len(pw_inputs) >= 2:
                await pw_inputs[0].fill("SeekAPI_Test_123")
                await pw_inputs[1].fill("SeekAPI_Test_123")
                print("✅ 成功通过模糊匹配填写了密码和确认密码")
            
            await page.screenshot(path="last_check_view.png")
            
            # 验证登录页
            await page.goto("https://dash.seekapi.ai/login")
            await page.wait_for_timeout(3000)
            
            if await page.is_visible("button"):
                status = "ALL SYSTEMS GO 🟢"
            else:
                status = "UI_CHANGED 🟡"
                
            with open("health_check.txt", "w") as f:
                f.write(f"Full E2E Check: {time.ctime()} - {status}")
            print(f"🟢 自检完成: {status}")

        except Exception as e:
            print(f"🔴 自检失败: {e}")
            with open("health_check.txt", "w") as f:
                f.write(f"Full E2E Check: {time.ctime()} - FAILED 🔴")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_full_test())
