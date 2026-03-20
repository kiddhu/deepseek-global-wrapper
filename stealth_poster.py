import asyncio
from playwright.async_api import async_playwright
import os
from dotenv import load_dotenv

load_dotenv()

async def auto_post_comment(target_url, comment_text):
    print(f"🚀 大龙虾隐身模式启动：准备前往 {target_url}")
    
    async with async_playwright() as p:
        # 1. 启动浏览器（模拟真实用户环境）
        # 如果你有代理，取消下面 proxy 行的注释并填入
        browser = await p.chromium.launch(
            headless=True, 
            # proxy={"server": "http://your_proxy_ip:port", "username": "user", "password": "pwd"}
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # 2. 登录 Hacker News (模拟登录)
        print("🔑 正在尝试登录 Hacker News...")
        await page.goto("https://news.ycombinator.com/login")
        await page.fill("input[name='acct']", "你的HN账号")
        await page.fill("input[name='pw']", "你的HN密码")
        await page.click("input[value='login']")
        await page.wait_for_timeout(3000)

        # 3. 前往目标帖子
        print(f"🎯 正在前往目标帖子: {target_url}")
        await page.goto(target_url)
        
        # 4. 寻找评论框并输入话术
        try:
            # HN 的评论框通常是一个 textarea
            await page.fill("textarea[name='text']", comment_text)
            await page.wait_for_timeout(2000) # 模拟思考时间
            
            # 5. 提交评论 (在测试阶段，我们先注释掉提交按钮，确保安全)
            # await page.click("input[value='add comment']")
            print("✅ 话术已填入评论框！(当前为模拟模式，未点击提交)")
            
        except Exception as e:
            print(f"❌ 无法找到评论框，可能需要先登录或帖子已关闭: {e}")

        await browser.close()

if __name__ == "__main__":
    # 模拟从 outreach_messages.txt 读取第一条话术
    test_url = "https://news.ycombinator.com/item?id=47322794" # 昨晚抓到的第一个项目
    test_msg = "Nice work on building a usage circuit breaker... (SeekAPI.ai can help slash costs by 90%)"
    asyncio.run(auto_post_comment(test_url, test_msg))
