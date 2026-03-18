import os

def generate_pro_legal_worker():
    print("⚖️ 正在生成针对 Stripe 审核优化的专业法律文档...")
    
    # 这里的文本是专门为 API 转发业务设计的合规条文
    tos_text = "<h1>Terms of Service</h1><p>Last Updated: March 2026</p><h3>1. Acceptance of Terms</h3><p>By accessing SeekAPI.ai, you agree to be bound by these terms. We provide AI inference gateway services compatible with OpenAI protocols.</p><h3>2. Governing Law</h3><p>These terms are governed by the laws of the Hong Kong Special Administrative Region.</p><h3>3. Usage Policy</h3><p>Users must not use the API for illegal activities. We reserve the right to terminate accounts violating these terms.</p>"
    
    privacy_text = "<h1>Privacy Policy</h1><p>SeekAPI.ai respects your privacy. We collect minimal data (email and usage logs) necessary for service delivery. We do not sell your data to third parties. Payments are processed securely via Stripe.</p>"
    
    refund_text = "<h1>Refund Policy</h1><p>We offer a 7-day refund policy for unused credits. If you are unsatisfied with our service, please contact support@seekapi.ai with your account details. Refunded amounts will be credited back to your original payment method.</p>"

    worker_code = f"""
async function handleRequest(request) {{
  const url = new URL(request.url);
  const path = url.pathname;
  const blog_url = "https://raw.githubusercontent.com/kiddhu/deepseek-global-wrapper/main/blog-post.md";
  
  // 路由逻辑
  if (path === '/terms') return new Response(render('Terms of Service', `{tos_text}`), {{headers:{{'content-type':'text/html;charset=UTF-8'}}}});
  if (path === '/privacy') return new Response(render('Privacy Policy', `{privacy_text}`), {{headers:{{'content-type':'text/html;charset=UTF-8'}}}});
  if (path === '/refund') return new Response(render('Refund Policy', `{refund_text}`), {{headers:{{'content-type':'text/html;charset=UTF-8'}}}});
  
  if (path.startsWith('/blog')) {{
    const res = await fetch(blog_url);
    const md = await res.text();
    return new Response(render('SeekAPI Blog', '<h1>SeekAPI AI Insights</h1><pre style="white-space:pre-wrap">' + md + '</pre>'), {{headers:{{'content-type':'text/html;charset=UTF-8'}}}});
  }}
  
  return fetch(request);
}}

function render(title, content) {{
  return `<html><head><meta charset="UTF-8"><title>${{title}} - SeekAPI.ai</title><style>body{{font-family:-apple-system,sans-serif;line-height:1.6;max-width:800px;margin:0 auto;padding:50px;color:#333;}}a{{color:#0070f3;text-decoration:none;}}hr{{border:0;border-top:1px solid #eee;margin:20px 0;}}</style></head><body><a href="/">← Back to Home</a><hr>${{content}}<footer style="margin-top:50px;color:#999;font-size:12px;">© 2026 SeekAPI.ai. All rights reserved.</footer></body></html>`;
}}

addEventListener('fetch', event => {{ event.respondWith(handleRequest(event.request)) }})
"""
    
    print("\n" + "★"*30)
    print("🚀 终极合规代码已生成！请立即更新 Cloudflare Worker：")
    print("1. 登录 Cloudflare -> Workers -> seekapi-blog-router")
    print("2. 点击 'Edit Code'，删除旧代码，粘贴下面的全部内容：")
    print("-" * 30)
    print(worker_code)
    print("-" * 30)
    print("3. 点击 'Save and Deploy'")
    print("4. 确保 Triggers 路由包含: seekapi.ai/terms, seekapi.ai/privacy, seekapi.ai/refund")
    print("★"*30)

if __name__ == "__main__":
    generate_pro_legal_worker()
