import requests, base64, os

def update():
    TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
    REPO = "kiddhu/deepseek-global-wrapper"
    url = f"https://api.github.com/repos/{REPO}/contents/public/guides/index.html"
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>SeekAPI Documentation</title>
        <style>
            body { background: #0d1117; color: #c9d1d9; font-family: sans-serif; padding: 50px; line-height: 1.6; }
            .container { max-width: 800px; margin: auto; }
            h1 { color: #58a6ff; border-bottom: 1px solid #30363d; padding-bottom: 10px; }
            .card { background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 8px; margin-top: 20px; }
            a { color: #58a6ff; text-decoration: none; font-weight: bold; }
            code { background: #222; padding: 2px 5px; border-radius: 4px; color: #79c0ff; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>SeekAPI.ai 开发者文档中心</h1>
            <div class="card">
                <h2>快速开始 (Quick Start)</h2>
                <p>只需将您的 OpenAI Base URL 替换为：<code>https://api.seekapi.ai/v1</code></p>
                <a href="/guides/quickstart.html">查看详细集成指南 →</a>
            </div>
            <div class="card">
                <h2>多语言 SDK</h2>
                <p>支持 Python, Node.js, Go 等主流语言。100% 兼容 OpenAI 官方库。</p>
                <a href="https://github.com/kiddhu/deepseek-global-wrapper" target="_blank">访问 GitHub 仓库 →</a>
            </div>
        </div>
    </body>
    </html>
    """
    
    res = requests.get(url, headers=headers)
    payload = {"message": "AION: Final Docs Index Update", "content": base64.b64encode(html_content.encode()).decode()}
    if res.status_code == 200:
        payload["sha"] = res.json()['sha']
    
    put_res = requests.put(url, json=payload, headers=headers)
    if put_res.status_code in [200, 201]:
        print("✅ 文档索引页已物理更新至 GitHub。")
    else:
        print(f"❌ 更新失败: {put_res.text}")

if __name__ == "__main__":
    update()
