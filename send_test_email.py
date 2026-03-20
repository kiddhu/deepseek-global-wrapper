import os
import resend
from dotenv import load_dotenv

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY")

def send_test():
    print("📧 Sending test email to 2155559@qq.com ...")
    try:
        r = resend.Emails.send({
            "from": "SeekAPI Support <support@seekapi.ai>",
            "to": ["2155559@qq.com"],
            "subject": "Hello from SeekAPI Command Center!",
            "html": "<h1>It Works!</h1><p>Your professional email system is now online.</p>"
        })
        print(f"✅ Success! Email ID: {r['id']}")
    except Exception as e:
        print(f"❌ Failed: {e}")

if __name__ == "__main__":
    send_test()
