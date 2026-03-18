async function handleRequest(request) {
  const url = new URL(request.url);
  const path = url.pathname;
  const blog_url = "https://raw.githubusercontent.com/kiddhu/deepseek-global-wrapper/main/blog-post.md";

  // 1. 拦截法律页面 (Stripe 审核必备)
  if (path === '/terms') return new Response(render('Terms of Service', '<h1>Terms of Service</h1><p>Last Updated: March 2026</p><h3>1. Acceptance</h3><p>By using SeekAPI.ai, you agree to these terms.</p>'), {headers:{'content-type':'text/html;charset=UTF-8'}});
  if (path === '/privacy') return new Response(render('Privacy Policy', '<h1>Privacy Policy</h1><p>We value your privacy. Data is processed securely.</p>'), {headers:{'content-type':'text/html;charset=UTF-8'}});
  if (path === '/refund') return new Response(render('Refund Policy', '<h1>Refund Policy</h1><p>7-day refund policy for unused credits.</p>'), {headers:{'content-type':'text/html;charset=UTF-8'}});

  // 2. 拦截博客页面
  if (path.startsWith('/blog')) {
    const res = await fetch(blog_url);
    const md = await res.text();
    return new Response(render('SeekAPI Blog', '<h1>SeekAPI AI Insights</h1><pre style="white-space:pre-wrap; background:#f9f9f9; padding:15px;">' + md + '</pre>'), {headers:{'content-type':'text/html;charset=UTF-8'}});
  }

  // 3. 处理首页：获取 Vercel 内容并强行注入页脚
  let response = await fetch(request);
  let contentType = response.headers.get('content-type') || '';

  if (contentType.includes('text/html')) {
    let html = await response.text();
    
    // 注入合规页脚 (带样式的灰色长条)
    const footerHtml = `
      <div style="background:#f9fafb; padding:40px 20px; text-align:center; border-top:1px solid #e5e7eb; font-family:sans-serif; width:100%; margin-top:50px;">
        <div style="margin-bottom:15px;">
          <a href="/terms" style="margin:0 15px; color:#374151; text-decoration:none; font-weight:500;">Terms</a>
          <a href="/privacy" style="margin:0 15px; color:#374151; text-decoration:none; font-weight:500;">Privacy</a>
          <a href="/refund" style="margin:0 15px; color:#374151; text-decoration:none; font-weight:500;">Refund</a>
        </div>
        <p style="color:#6b7280; font-size:12px;">© 2026 SeekAPI.ai | Operated by SeekAPI Global (Hong Kong) Limited</p>
        <p style="color:#9ca3af; font-size:11px;">Contact: support@seekapi.ai</p>
      </div>
    `;
    
    // 强行在 </body> 之前插入，如果找不到 </body> 就直接加在最后
    if (html.includes('</body>')) {
      html = html.replace('</body>', footerHtml + '</body>');
    } else {
      html = html + footerHtml;
    }
    
    return new Response(html, response);
  }

  return response;
}

function render(title, content) {
  const aioData = {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "SeekAPI.ai",
    "url": "https://seekapi.ai"
  };
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><title>${title}</title><script type="application/ld+json">${JSON.stringify(aioData)}</script><style>body{font-family:sans-serif;line-height:1.6;max-width:800px;margin:0 auto;padding:50px;}a{color:#2563eb;text-decoration:none;}hr{border:0;border-top:1px solid #eee;margin:20px 0;}</style></head><body><a href="/">← Home</a><hr>${content}</body></html>`;
}

addEventListener('fetch', event => { event.respondWith(handleRequest(event.request)) });
