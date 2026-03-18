import asyncio
from playwright.async_api import async_playwright

async def run_radar():
    print("🚀 大龙虾雷达 2.0 启动（隐身模式）...")
    
    async with async_playwright() as p:
        # 模拟真实用户的浏览器特征
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        # 改用 DuckDuckGo，它对自动化脚本更宽容
        search_query = "site:reddit.com OpenAI expensive costly"
        print(f"🔍 正在通过 DuckDuckGo 侦察: {search_query}")
        
        # 访问 DuckDuckGo
        await page.goto(f"https://duckduckgo.com/html/?q={search_query}")
        
        # 等待结果加载
        await page.wait_for_timeout(3000)
        
        # 提取结果（DuckDuckGo HTML 版的标签是 .result__a）
        results = await page.evaluate('''() => {
            const links = document.querySelectorAll('.result__a');
            return Array.from(links).slice(0, 5).map(link => ({
                title: link.innerText,
                url: link.href
            }));
        }''')
        
        if not results:
            print("⚠️ 依然没有抓取到结果。尝试直接访问 Reddit 热门话题...")
            await page.goto("https://www.reddit.com/r/OpenAI/search/?q=expensive&restrict_sr=1&sr_nsfw=&sort=new")
            await page.wait_for_timeout(5000)
            # 尝试抓取 Reddit 内部搜索结果
            results = await page.evaluate('''() => {
                const posts = document.querySelectorAll('a[data-testid="post-title"]');
                return Array.from(posts).slice(0, 5).map(post => ({
                    title: post.innerText,
                    url: post.href
                }));
            }''')

        print(f"✅ 侦察完成，发现 {len(results)} 条高价值讨论：")
        
        with open("real_leads.txt", "w") as f:
            for i, res in enumerate(results, 1):
                line = f"[{i}] {res['title']}\n🔗 {res['url']}\n"
                print(line)
                f.write(line + "\n")
        
        await browser.close()
        print("🏁 侦察任务完成，名单已存入 real_leads.txt")

if __name__ == "__main__":
    asyncio.run(run_radar())
