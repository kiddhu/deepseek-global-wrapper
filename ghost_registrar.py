import asyncio
from playwright.async_api import async_playwright
import time, random

async def run_test():
    print("👻 幽灵注册员 V3 启动：正在执行破防自检...")
    async with async_playwright() as p:
        # 关键：增加模拟参数，减少“机器人”特征
        browser = await p.chromium.launch(headless=True, args=['--disable-blink-features=AutomationControlled'])
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        page = await context.new_page()
        
        try:
            await page.goto("https://dash.seekapi.ai/register", wait_until="networkidle")
            await page.wait_for_timeout(8000) # 给 Cloudflare 验证留出时间
            
            # 拍照：这是最重要的证据
            await page.screenshot(path="last_check_view.png")
            
            # 尝试寻找 One-API 的标准输入框
            # 如果你的 One-API 改过代码，这里可能需要调整
            if await page.is_visible("input[name='username']"):
                await page.fill("input[name='username']", f"ghost_{random.randint(100,999)}")
                print("🟢 成功定位到注册表单！")
                status = "SUCCESS 🟢"
            else:
                print("🔴 依然找不到表单，请查看仪表盘截图。")
                status = "BLOCKED_BY_CF_OR_TEMPLATE 🔴"
                
            with open("registrar_check.txt", "w") as f:
                f.write(f"Last Check: {time.ctime()} - {status}")
        except Exception as e:
            print(f"❌ 运行崩溃: {e}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_test())
