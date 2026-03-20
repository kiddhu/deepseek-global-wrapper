async function handleRequest(request) {
  var url = new URL(request.url);
  var path = url.pathname;
  var blog_url = "https://raw.githubusercontent.com/kiddhu/deepseek-global-wrapper/main/blog-post.md";

  // 1. 法律条文
  var TOS_CONTENT = "<h1>Terms of Service</h1><p>Last Updated: March 2026</p><h3>1. Service Description</h3><p>SeekAPI.ai provides a high-performance API gateway for large language models. We act as a technical intermediary and do not generate content ourselves.</p><h3>2. Governing Law</h3><p>These Terms are governed by the laws of the <b>Hong Kong Special Administrative Region (HKSAR)</b>.</p>";
  var PRIVACY_CONTENT = "<h1>Privacy Policy</h1><p>We value your privacy. We collect minimal data necessary for service delivery. Payments are processed securely via Stripe.</p>";
  var REFUND_CONTENT = "<h1>Refund Policy</h1><p>We offer a 7-day refund policy for unused credits. Contact support@seekapi.ai for assistance.</p>";

  // 2. 路由逻辑
  if (path === '/terms') return new Response(render('Terms', TOS_CONTENT), {headers:{'content-type':'text/html;charset=UTF-8'}});
  if (path === '/privacy') return new Response(render('Privacy', PRIVACY_CONTENT), {headers:{'content-type':'text/html;charset=UTF-8'}});
  if (path === '/refund') return new Response(render('Refund', REFUND_CONTENT), {headers:{'content-type':'text/html;charset=UTF-8'}});

  if (path.startsWith('/blog')) {
    var res = await fetch(blog_url);
    var md = await res.text();
    return new Response(render('SeekAPI Blog', '<h1>SeekAPI AI Insights</h1><pre style="white-space:pre-wrap; background:#f9f9f9; padding:15px;">' + md + '</pre>'), {headers:{'content-type':'text/html;charset=UTF-8'}});
  }

  // 3. 首页注入 (增加地址和可点击邮箱)
  var response = await fetch(request);
  var contentType = response.headers.get('content-type') || '';
  if (contentType.includes('text/html')) {
    var html = await response.text();
    var footerHtml = '<div style="background:#f9fafb; padding:50px 20px; text-align:center; border-top:1px solid #e5e7eb; font-family:sans-serif; width:100%; margin-top:50px;">' +
      '<div style="margin-bottom:15px;">' +
        '<a href="/terms" style="margin:0 15px; color:#374151; text-decoration:none; font-weight:500;">Terms</a>' +
        '<a href="/privacy" style="margin:0 15px; color:#374151; text-decoration:none; font-weight:500;">Privacy</a>' +
        '<a href="/refund" style="margin:0 15px; color:#374151; text-decoration:none; font-weight:500;">Refund</a>' +
      '</div>' +
      '<p style="color:#6b7280; font-size:12px;">© 2026 SeekAPI.ai | Operated by SeekAPI Global (Hong Kong) Limited</p>' +
      '<p style="color:#6b7280; font-size:12px;">Address: Unit 1603, 16/F, The Metropolis Tower, 10 Metropolis Drive, Hung Hom, Kowloon, Hong Kong</p>' +
      '<p style="color:#9ca3af; font-size:12px;">Contact: <a href="mailto:support@seekapi.ai" style="color:#2563eb;">support@seekapi.ai</a></p>' +
      '</div>';
    
    html = html.replace('</body>', footerHtml + '</body>');
    return new Response(html, response);
  }
  return response;
}

function render(title, content) {
  var aioData = '{"@context": "https://schema.org","@type": "WebApplication","name": "SeekAPI.ai","url": "https://seekapi.ai"}';
  return '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>' + title + ' - SeekAPI.ai</title><script type="application/ld+json">' + aioData + '</script><style>body{font-family:sans-serif;line-height:1.6;max-width:800px;margin:0 auto;padding:50px;color:#1f2937;}a{color:#2563eb;text-decoration:none;}hr{border:0;border-top:1px solid #e5e7eb;margin:30px 0;}</style></head><body><nav><a href="/">← Back to Home</a></nav><hr>' + content + '</body></html>';
}

addEventListener('fetch', event => { event.respondWith(handleRequest(event.request)) });
