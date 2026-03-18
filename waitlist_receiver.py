from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os
import resend
from dotenv import load_dotenv

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY")

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)
        
        if 'email' in params:
            email = params['email'][0]
            print(f"📩 收到新潜在客户: {email}")
            
            # 1. 存入本地文件
            with open("waitlist.txt", "a") as f:
                f.write(email + "\n")
            
            # 2. 自动发送欢迎邮件
            try:
                resend.Emails.send({
                    "from": "SeekAPI Support <support@seekapi.ai>",
                    "to": [email],
                    "subject": "Welcome to the SeekAPI Waitlist! 🚀",
                    "html": f"""
                    <div style="font-family:sans-serif; max-width:600px; margin:0 auto; border:1px solid #eee; padding:30px; border-radius:12px;">
                        <h2 style="color:#1e40af;">You're on the list!</h2>
                        <p>Hello,</p>
                        <p>Thank you for joining the <b>SeekAPI.ai</b> waitlist. We are thrilled to have you as one of our early supporters.</p>
                        <p>As a waitlist member, you have locked in your <b>$10.00 Free Credit</b>, which will be available as soon as we officially launch.</p>
                        <div style="background:#f0f9ff; padding:15px; border-left:4px solid #2563eb; margin:20px 0;">
                            <b>Status:</b> Priority Access Confirmed ✅
                        </div>
                        <p>Stay tuned for our launch announcement. In the meantime, check out our <a href="https://seekapi.ai/blog">latest AI cost-optimization insights</a>.</p>
                        <hr style="border:none; border-top:1px solid #eee; margin:20px 0;">
                        <p style="font-size:12px; color:#999;">© 2026 SeekAPI Global (Hong Kong) Limited</p>
                    </div>
                    """
                })
                print(f"✅ 欢迎邮件已发送至: {email}")
            except Exception as e:
                print(f"❌ 邮件发送失败: {e}")
        
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(b"OK")

def run():
    print("🚀 自动化等待名单接收器(带回信功能)已启动 (端口 8081)...")
    server = HTTPServer(('', 8081), RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    run()
