import os, base64, requests
from dotenv import load_dotenv

load_dotenv()

def sync():
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPO")
    guides_dir = "/root/OpenClaw/public/guides"
    
    for f_name in os.listdir(guides_dir):
        if f_name.endswith('.html'):
            path = f"public/guides/{f_name}"
            url = f"https://api.github.com/repos/{repo}/contents/{path}"
            headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
            
            with open(os.path.join(guides_dir, f_name), 'r', encoding='utf-8') as f:
                content = f.read()
            
            res = requests.get(url, headers=headers)
            sha = res.json().get('sha') if res.status_code == 200 else None
            
            data = {"message": "🧹 AION: Content Deep Cleaning", "content": base64.b64encode(content.encode()).decode()}
            if sha: data["sha"] = sha
            requests.put(url, json=data, headers=headers)
            print(f"🚀 已同步修复后的文件: {f_name}")

if __name__ == "__main__":
    sync()
