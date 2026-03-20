async function handleRequest(request) {
  var url = new URL(request.url);
  var path = url.pathname;
  var blog_url = "https://raw.githubusercontent.com/kiddhu/deepseek-global-wrapper/main/blog-post.md";

  // 1. 法律页面路由
  if (path === '/terms') return new Response(render('Terms', '<h1>Terms of Service</h1><p>Governed by HKSAR Laws...</p>'), {headers:{'content-type':'text/html;charset=UTF-8'}});
  if (path === '/privacy') return new Response(render('Privacy', '<h1>Privacy Policy</h1><p>We value your data...</p>'), {headers:{'content-type':'text/html;charset=UTF-8'}});
  if (path === '/refund') return new Response(render('Refund', '<h1>Refund Policy</h1><p>7-day money back...</p>'), {headers:{'content-type':'text/html;charset=UTF-8'}});

  // 2. 首页注入逻辑
  var response = await fetch(request);
  var contentType = response.headers.get('content-type') || '';

  if (path === '/' && contentType.includes('text/html')) {
    var html = await response.text();
    
    // 注入 A: 等待名单输入框 (放在 Hero 区域下方)
    var waitlistHtml = '<div style="background:#eff6ff; padding:40px; text-align:center; border-radius:12px; margin:20px auto; max-width:600px; border:1px solid #bfdbfe; font-family:sans-serif;">' +
      '<h2 style="color:#1e40af; margin-bottom:10px;">🎁 Get $10 Free Credits on Launch!</h2>' +
      '<p style="color:#1e3a8a; margin-bottom:20px;">Join 500+ developers on our waitlist. We are launching soon.</p>' +
      '<form action="mailto:support@seekapi.ai" method="post" enctype="text/plain">' +
        '<input type="email" name="email" placeholder="Enter your email" required style="padding:12px; width:250px; border-radius:6px; border:1px solid #93c5fd; margin-right:10px;">' +
        '<button type="submit" style="padding:12px 24px; background:#2563eb; color:white; border:none; border-radius:6px; cursor:pointer; font-weight:bold;">Join Waitlist</button>' +
      '</form>' +
      '</div>';

    // 注入 B: 专业页脚
    var footerHtml = '<div style="background:#f9fafb; padding:40px 20px; text-align:center; border-top:1px solid #e5e7eb; font-family:sans-serif; margin-top:50px;">' +
      '<div style="margin-bottom:15px;"><a href="/terms" style="margin:0 15px; color:#374151; text-decoration:none;">Terms</a> | <a href="/privacy" style="margin:0 15px; color:#374151; text-decoration:none;">Privacy</a> | <a href="/refund" style="margin:0 15px; color:#374151; text-decoration:none;">Refund</a></div>' +
      '<p style="color:#6b7280; font-size:12px;">© 2026 SeekAPI.ai | Operated by SeekAPI Global (Hong Kong) Limited</p>' +
      '<p style="color:#6b7280; font-size:12px;">Address: Unit 1603, 16/F, The Metropolis Tower, 10 Metropolis Drive, Hung Hom, Kowloon, Hong Kong</p>' +
      '</div>';

    // 寻找一个合适的位置插入 (通常在第一个 </section> 后面)
    html = html.replace('</section>', '</section>' + waitlistHtml);
    html = html.replace('</body>', footerHtml + '</body>');
    
    return new Response(html, response);
  }

  return response;
}

function render(title, content) {
  return '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>' + title + ' - SeekAPI.ai</title><style>body{font-family:sans-serif;line-height:1.6;max-width:800px;margin:0 auto;padding:50px;}</style></head><body><nav><a href="/">← Back</a></nav><hr>' + content + '</body></html>';
}

addEventListener('fetch', event => { event.respondWith(handleRequest(event.request)) });
