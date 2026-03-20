def generate_final_worker():
    print("🛠️ 正在生成“全能合规版”Worker 代码...")
    
    # 法律条文内容
    tos_text = "<h1>Terms of Service</h1><p>Last Updated: March 2026</p><h3>1. Acceptance</h3><p>By using SeekAPI.ai, you agree to our terms...</p>"
    privacy_text = "<h1>Privacy Policy</h1><p>We protect your data...</p>"
    refund_text = "<h1>Refund Policy</h1><p>7-day money-back guarantee for unused credits...</p>"

    # 要注入首页的页脚 HTML
    footer_html = """
    <footer style="text-align:center; padding:40px 20px; font-size:13px; color:#666; background:#fafafa; border-top:1px solid #eee; font-family:sans-serif;">
        <div style="margin-bottom:10px;">
            <a href="/terms" style="margin:0 10px; color:#666; text-decoration:none;">Terms of Service</a> | 
            <a href="/privacy" style="margin:0 10px; color:#666; text-decoration:none;">Privacy Policy</a> | 
            <a href="/refund" style="margin:0 10px; color:#666; text-decoration:none;">Refund Policy</a>
        </div>
        <p>© 2026 SeekAPI.ai | Contact: support@seekapi.ai</p>
        <p style="font-size:11px; color:#999;">Operated by SeekAPI Global (Hong Kong) Limited</p>
    </footer>
    """

    worker_code = f"""
async function handleRequest(request) {{
  const url = new URL(request.url);
  const path = url.pathname;
  
  // 1. 拦截法律页面
  if (path === '/terms') return new Response(render('Terms', `{tos_text}`), {{headers:{{'content-type':'text/html;charset=UTF-8'}}}});
  if (path === '/privacy') return new Response(render('Privacy', `{privacy_text}`), {{headers:{{'content-type':'text/html;charset=UTF-8'}}}});
  if (path === '/refund') return new Response(render('Refund', `{refund_text}`), {{headers:{{'content-type':'text/html;charset=UTF-8'}}}});
  
  // 2. 获取原始网页 (Vercel 首页)
  let response = await fetch(request);
  
  // 3. 如果是首页，强行注入页脚
  if (path === '/' && response.headers.get('content-type')?.includes('text/html')) {{
    let html = await response.text();
    // 在 </body> 标签前插入页脚
    html = html.replace('</body>', `{footer_html}</body>`);
    return new Response(html, response);
  }}
  
  return response;
}}

function render(title, content) {{
  return `<html><head><meta charset="UTF-8"><title>${{title}} - SeekAPI.ai</title><style>body{{font-family:sans-serif;line-height:1.6;max-width:800px;margin:0 auto;padding:50px;}}a{{color:#0070f3;}}</style></head><body><a href="/">← Back</a><hr>${{content}}</body></html>`;
}}

addEventListener('fetch', event => {{ event.respondWith(handleRequest(event.request)) }})
"""
    print("\n" + "★"*30)
    print("🚀 全能合规代码已就绪！请执行以下操作：")
    print("1. 登录 Cloudflare -> Workers -> seekapi-blog-router")
    print("2. 点击 'Edit Code'，清空旧代码，粘贴下面的全部内容：")
    print("-" * 30)
    print(worker_code)
    print("-" * 30)
    print("3. 点击 'Save and Deploy'")
    print("★"*30)

if __name__ == "__main__":
    generate_final_worker()
