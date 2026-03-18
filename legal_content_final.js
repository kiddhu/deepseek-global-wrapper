async function handleRequest(request) {
  const url = new URL(request.url);
  const path = url.pathname;
  const blog_url = "https://raw.githubusercontent.com/kiddhu/deepseek-global-wrapper/main/blog-post.md";

  // --- 1. 极其严格的法律条文定义 ---

  const TOS_CONTENT = `
    <h1>Terms of Service</h1>
    <p>Last Updated: March 2026</p>
    <h3>1. Service Description</h3>
    <p>SeekAPI.ai provides a high-performance API gateway for large language models. We act as a technical intermediary and do not generate content ourselves.</p>
    <h3>2. Limitation of Liability</h3>
    <p>SeekAPI.ai provides services on an "AS IS" basis. We are not responsible for the accuracy, legality, or reliability of AI-generated outputs. Users assume all risks associated with the use of AI models.</p>
    <h3>3. Governing Law</h3>
    <p>These Terms shall be governed by and construed in accordance with the laws of the <b>Hong Kong Special Administrative Region (HKSAR)</b>.</p>
    <h3>4. Acceptable Use</h3>
    <p>Users are prohibited from using the service for any illegal activities, including but not limited to fraud, harassment, or generating malicious code.</p>
  `;

  const PRIVACY_CONTENT = `
    <h1>Privacy Policy</h1>
    <p>Last Updated: March 2026</p>
    <h3>1. Data Collection</h3>
    <p>We collect minimal data necessary for service delivery: email addresses for account management and API usage logs for billing purposes.</p>
    <h3>2. Data Security</h3>
    <p>We implement industry-standard security measures to protect your data. We do not sell or share your personal information with third parties for marketing purposes.</p>
    <h3>3. Payment Processing</h3>
    <p>Payment information is processed securely by our third-party provider, <b>Stripe</b>. SeekAPI.ai does not store your credit card details.</p>
  `;

  const REFUND_CONTENT = `
    <h1>Refund Policy</h1>
    <p>Last Updated: March 2026</p>
    <h3>1. 7-Day Money-Back Guarantee</h3>
    <p>We offer a full refund for <b>unused credits</b> within 7 days of purchase. If you are unsatisfied with our service, please contact support@seekapi.ai.</p>
    <h3>2. Non-Refundable Items</h3>
    <p>Credits that have already been consumed for API calls are non-refundable. Promotional or bonus credits have no cash value and are non-refundable.</p>
    <h3>3. Processing Time</h3>
    <p>Refunds will be issued to the original payment method within 5-10 business days after approval.</p>
  `;

  // --- 2. 路由逻辑 ---

  if (path === '/terms') return new Response(render('Terms of Service', TOS_CONTENT), {headers:{'content-type':'text/html;charset=UTF-8'}});
  if (path === '/privacy') return new Response(render('Privacy Policy', PRIVACY_CONTENT), {headers:{'content-type':'text/html;charset=UTF-8'}});
  if (path === '/refund') return new Response(render('Refund Policy', REFUND_CONTENT), {headers:{'content-type':'text/html;charset=UTF-8'}});

  if (path.startsWith('/blog')) {
    const res = await fetch(blog_url);
    const md = await res.text();
    return new Response(render('SeekAPI Blog', '<h1>SeekAPI AI Insights</h1><pre style="white-space:pre-wrap; background:#f9f9f9; padding:15px;">' + md + '</pre>'), {headers:{'content-type':'text/html;charset=UTF-8'}});
  }

  // --- 3. 首页注入逻辑 ---

  let response = await fetch(request);
  let contentType = response.headers.get('content-type') || '';

  if (contentType.includes('text/html')) {
    let html = await response.text();
    const footerHtml = `
      <div style="background:#f9fafb; padding:40px 20px; text-align:center; border-top:1px solid #e5e7eb; font-family:sans-serif; width:100%; margin-top:50px;">
        <div style="margin-bottom:15px;">
          <a href="/terms" style="margin:0 15px; color:#374151; text-decoration:none; font-weight:500;">Terms of Service</a>
          <a href="/privacy" style="margin:0 15px; color:#374151; text-decoration:none; font-weight:500;">Privacy Policy</a>
          <a href="/refund" style="margin:0 15px; color:#374151; text-decoration:none; font-weight:500;">Refund Policy</a>
        </div>
        <p style="color:#6b7280; font-size:12px;">© 2026 SeekAPI.ai | Operated by SeekAPI Global (Hong Kong) Limited</p>
        <p style="color:#9ca3af; font-size:11px;">Contact: support@seekapi.ai</p>
      </div>
    `;
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
  return `<!DOCTYPE html><html><head><meta charset="UTF-8"><title>${title} - SeekAPI.ai</title><style>body{font-family:-apple-system,sans-serif;line-height:1.6;max-width:800px;margin:0 auto;padding:50px;color:#1f2937;}a{color:#2563eb;text-decoration:none;}hr{border:0;border-top:1px solid #e5e7eb;margin:30px 0;}h1{font-size:24px;margin-bottom:20px;}h3{font-size:18px;margin-top:30px;}</style></head><body><nav><a href="/">← Back to Home</a></nav><hr>${content}<footer style="margin-top:50px; color:#9ca3af; font-size:12px;">© 2026 SeekAPI.ai</footer></body></html>`;
}

addEventListener('fetch', event => { event.respondWith(handleRequest(event.request)) });
