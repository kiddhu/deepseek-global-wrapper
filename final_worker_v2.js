async function handleRequest(request) {
  const url = new URL(request.url);
  const path = url.pathname;
  const blog_url = "https://raw.githubusercontent.com/kiddhu/deepseek-global-wrapper/main/blog-post.md";

  // 1. 路由：法律页面
  if (path === '/terms') return new Response(render('Terms of Service', '<h1>Terms of Service</h1><p>Last Updated: March 2026</p><h3>1. Acceptance</h3><p>By using SeekAPI.ai, you agree to these terms. We provide high-performance AI gateway services.</p><h3>2. Governing Law</h3><p>These terms are governed by the laws of the Hong Kong SAR.</p>'), {headers:{'content-type':'text/html;charset=UTF-8'}});
  if (path === '/privacy') return new Response(render('Privacy Policy', '<h1>Privacy Policy</h1><p>We value your privacy. We only collect data necessary for API processing and billing. Your data is never sold.</p>'), {headers:{'content-type':'text/html;charset=UTF-8'}});
  if (path === '/refund') return new Response(render('Refund Policy', '<h1>Refund Policy</h1><p>We offer a 7-day refund policy for unused credits. Contact support@seekapi.ai for assistance.</p>'), {headers:{'content-type':'text/html;charset=UTF-8'}});

  // 2. 路由：博客页面
  if (path.startsWith('/blog')) {
    const res = await fetch(blog_url);
    const md = await res.text();
    return new Response(render('SeekAPI Blog', '<h1>SeekAPI AI Insights</h1><pre style="white-space:pre-wrap; background:#f9f9f9; padding:15px; border-radius:5px;">' + md + '</pre>'), {headers:{'content-type':'text/html;charset=UTF-8'}});
  }

  // 3. 首页逻辑：获取 Vercel 内容并注入页脚
  let response = await fetch(request);
  if (path === '/' && response.headers.get('content-type')?.includes('text/html')) {
    let html = await response.text();
    
    // 注入合规页脚 HTML
    const footerHtml = `
      <footer style="background:#f4f4f7; padding:50px 20px; text-align:center; border-top:1px solid #e5e7eb; font-family:sans-serif;">
        <div style="max-width:1200px; margin:0 auto;">
          <div style="margin-bottom:20px;">
            <a href="/terms" style="margin:0 15px; color:#4b5563; text-decoration:none; font-size:14px;">Terms of Service</a>
            <a href="/privacy" style="margin:0 15px; color:#4b5563; text-decoration:none; font-size:14px;">Privacy Policy</a>
            <a href="/refund" style="margin:0 15px; color:#4b5563; text-decoration:none; font-size:14px;">Refund Policy</a>
          </div>
          <p style="color:#9ca3af; font-size:12px;">© 2026 SeekAPI.ai | Operated by SeekAPI Global (Hong Kong) Limited</p>
          <p style="color:#9ca3af; font-size:12px;">Contact: support@seekapi.ai</p>
        </div>
      </footer>
    `;
    
    // 在 </body> 标签前插入页脚
    html = html.replace('</body>', footerHtml + '</body>');
    return new Response(html, response);
  }

  return response;
}

// 通用渲染函数（包含 AIO 结构化数据）
function render(title, content) {
  const aioData = {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "SeekAPI.ai",
    "description": "Global high-performance gateway for DeepSeek R1 and V3. 90% cheaper than OpenAI.",
    "url": "https://seekapi.ai",
    "offers": { "@type": "Offer", "price": "0.50", "priceCurrency": "USD" }
  };

  return `
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">
        <title>${title} - SeekAPI.ai</title>
        <script type="application/ld+json">${JSON.stringify(aioData)}</script>
        <style>
          body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 40px; color: #1f2937; }
          a { color: #2563eb; text-decoration: none; }
          hr { border: 0; border-top: 1px solid #e5e7eb; margin: 30px 0; }
          pre { font-family: inherit; font-size: 14px; color: #4b5563; }
        </style>
      </head>
      <body>
        <nav><a href="/">← Back to Home</a></nav>
        <hr>
        <main>${content}</main>
        <footer style="margin-top:50px; color:#9ca3af; font-size:12px;">© 2026 SeekAPI.ai</footer>
      </body>
    </html>
  `;
}

addEventListener('fetch', event => { event.respondWith(handleRequest(event.request)) });
