import os
import resend
from dotenv import load_dotenv

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY")

def send_reward_code(customer_email, github_user, code):
    print(f"🚀 正在向 {customer_email} 发送企业级奖励邮件...")
    
    # 邮件正文 HTML 模板
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; }}
            .container {{ max-width: 600px; margin: 20px auto; border: 1px solid #e5e7eb; border-radius: 12px; overflow: hidden; }}
            .header {{ background-color: #1e40af; padding: 30px; text-align: center; color: white; }}
            .content {{ padding: 40px; background-color: #ffffff; }}
            .reward-box {{ background-color: #f8fafc; border: 2px dashed #cbd5e1; padding: 20px; text-align: center; margin: 30px 0; border-radius: 8px; }}
            .code {{ font-family: 'Courier New', monospace; font-size: 28px; font-weight: bold; color: #1e40af; letter-spacing: 3px; }}
            .button {{ display: inline-block; padding: 14px 28px; background-color: #2563eb; color: #ffffff !important; text-decoration: none; border-radius: 6px; font-weight: 600; margin-top: 20px; }}
            .footer {{ background-color: #f9fafb; padding: 30px; text-align: center; font-size: 12px; color: #6b7280; border-top: 1px solid #e5e7eb; }}
            .steps {{ text-align: left; display: inline-block; margin: 0 auto; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1 style="margin:0; font-size: 24px;">SeekAPI.ai</h1>
                <p style="margin:5px 0 0 0; opacity: 0.8;">Global DeepSeek R1/V3 Gateway</p>
            </div>
            <div class="content">
                <h2 style="margin-top:0;">Dear {github_user},</h2>
                <p>We noticed your support on GitHub. Thank you for starring our repository and joining the SeekAPI ecosystem.</p>
                <p>As a token of our appreciation, we have generated an exclusive <b>$1.00 Free Credit</b> for your account.</p>
                
                <div class="reward-box">
                    <div style="font-size: 14px; color: #64748b; margin-bottom: 10px;">YOUR REDEMPTION CODE</div>
                    <div class="code">{code}</div>
                </div>

                <div style="text-align: center;">
                    <p><b>How to redeem:</b></p>
                    <div class="steps">
                        1. Sign in to <a href="https://dash.seekapi.ai">SeekAPI Console</a><br>
                        2. Navigate to the <b>Redemption</b> section<br>
                        3. Enter the code above to claim your credits
                    </div>
                    <br>
                    <a href="https://dash.seekapi.ai" class="button">Go to Console</a>
                </div>
            </div>
            <div class="footer">
                <p>© 2026 SeekAPI Global (Hong Kong) Limited</p>
                <p>Unit 1603, 16/F, The Metropolis Tower, 10 Metropolis Drive, Hung Hom, Kowloon, Hong Kong</p>
                <p>
                    <a href="https://seekapi.ai/terms" style="color: #6b7280;">Terms</a> | 
                    <a href="https://seekapi.ai/privacy" style="color: #6b7280;">Privacy</a> | 
                    <a href="https://seekapi.ai/refund" style="color: #6b7280;">Refund Policy</a>
                </p>
                <p>If you have any questions, reply to this email or contact <a href="mailto:support@seekapi.ai">support@seekapi.ai</a></p>
            </div>
        </div>
    </body>
    </html>
    """
    
    try:
        resend.Emails.send({
            "from": "SeekAPI Support <support@seekapi.ai>",
            "to": [customer_email],
            "subject": "🎁 Your SeekAPI.ai Credits are Ready!",
            "html": html_content
        })
        print(f"✅ 成功！专业奖励邮件已发送至 {customer_email}")
    except Exception as e:
        print(f"❌ 发送失败: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("💡 使用方法: python3 dispatch_reward.py [邮箱] [用户名] [兑换码]")
    else:
        send_reward_code(sys.argv[1], sys.argv[2], sys.argv[3])
