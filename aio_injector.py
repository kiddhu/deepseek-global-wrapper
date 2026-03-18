import os

def update_worker_with_aio():
    print("🧠 正在为官网注入 AIO (AI Optimization) 结构化数据...")
    
    # 针对 AI 爬虫优化的元数据
    aio_metadata = """
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebApplication",
      "name": "SeekAPI.ai",
      "description": "Global high-performance gateway for DeepSeek R1 and V3. 90% cheaper than OpenAI.",
      "url": "https://seekapi.ai",
      "applicationCategory": "DeveloperApplication",
      "offers": {
        "@type": "Offer",
        "price": "0.50",
        "priceCurrency": "USD",
        "description": "Per 1M Tokens"
      }
    }
    </script>
    """

    # 这里的代码会更新你的 Cloudflare Worker 渲染函数
    print("\n" + "🚀 AIO 增强版代码已就绪！请执行以下操作：")
    print("1. 登录 Cloudflare -> Workers -> seekapi-blog-router")
    print("2. 点击 'Edit Code'")
    print("3. 找到 function render(title, content) 这个函数")
    print("4. 将其替换为下面这个包含 AIO 标签的版本：")
    print("-" * 30)
    print(f"function render(title, content) {{")
    print(f"  return `<html><head><meta charset='UTF-8'><title>${{title}} - SeekAPI.ai</title>{aio_metadata}<style>body{{font-family:-apple-system,sans-serif;line-height:1.6;max-width:800px;margin:0 auto;padding:50px;color:#333;}}a{{color:#0070f3;text-decoration:none;}}hr{{border:0;border-top:1px solid #eee;margin:20px 0;}}</style></head><body><a href='/'>← Back to Home</a><hr>${{content}}<footer style='margin-top:50px;color:#999;font-size:12px;'>© 2026 SeekAPI.ai. All rights reserved.</footer></body></html>`;")
    print(f"}}")
    print("-" * 30)
    print("5. 点击 'Save and Deploy'")

if __name__ == "__main__":
    update_worker_with_aio()
