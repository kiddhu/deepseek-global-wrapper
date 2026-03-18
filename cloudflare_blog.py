import os
import requests
from dotenv import load_dotenv

load_dotenv()

def deploy_blog_via_worker():
    token = os.getenv("CF_API_TOKEN")
    zone_id = os.getenv("CF_ZONE_ID")
    # 你的 GitHub 博客内容地址
    blog_url = "https://raw.githubusercontent.com/kiddhu/deepseek-global-wrapper/main/blog-post.md"
    
    print("🚀 正在通过 Cloudflare Workers 强制激活博客页面...")

    # 1. 编写 Worker 代码 (这是一个轻量级的流量转发器)
    worker_code = """
    async function handleRequest(request) {
      const url = new URL(request.url);
      if (url.pathname.startsWith('/blog')) {
        const res = await fetch('""" + blog_url + """');
        const md = await res.text();
        return new Response('<html><head><meta charset="UTF-8"><title>SeekAPI Blog</title><style>body{font-family:sans-serif;line-height:1.6;max-width:800px;margin:0 auto;padding:50px;}</style></head><body><a href="/">← Back</a><hr><h1>SeekAPI AI Insights</h1><pre style="white-space:pre-wrap">' + md + '</pre></body></html>', {
          headers: { 'content-type': 'text/html;charset=UTF-8' }
        });
      }
      return fetch(request);
    }
    addEventListener('fetch', event => {
      event.respondWith(handleRequest(event.request))
    })
    """

    # 2. 部署 Worker (这里需要你的 CF 账户信息，我们先通过 API 尝试)
    print("💡 架构师提示：由于 Cloudflare Workers 部署需要 Account ID，")
    print("💡 我们采用最简单的方案：请手动登录 Cloudflare 官网执行以下操作：")
    print("\n1. 点击左侧 'Workers & Pages' -> 'Create Application' -> 'Create Worker'")
    print("2. 名字起为: seekapi-blog-router")
    print("3. 点击 'Deploy'，然后点击 'Edit Code'")
    print("4. 把下面的代码全部粘贴进去并保存：\n")
    print("-" * 30)
    print(worker_code)
    print("-" * 30)
    print("\n5. 最后在 Worker 的 'Triggers' 选项卡点击 'Add Route'，填入: seekapi.ai/blog*")

if __name__ == "__main__":
    deploy_blog_via_worker()
