import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

def universal_fix():
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPO")
    
    # 方案 1: 针对旧版 Next.js (pages 模式)
    path_pages = "pages/blog.js"
    # 方案 2: 针对新版 Next.js (app 模式)
    path_app = "app/blog/page.jsx"
    
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    
    code = """
import React, { useEffect, useState } from 'react';

export default function BlogPage() {
  const [content, setContent] = useState('Loading...');
  useEffect(() => {
    fetch('https://raw.githubusercontent.com/""" + repo + """/main/blog-post.md')
      .then(res => res.text()).then(text => setContent(text));
  }, []);
  return <div style={{padding: '50px', maxWidth: '800px', margin: '0 auto', fontFamily: 'sans-serif'}}>
    <a href="/">← Home</a>
    <pre style={{whiteSpace: 'pre-wrap', marginTop: '20px'}}>{content}</pre>
  </div>;
}
"""

    for path in [path_pages, path_app]:
        print(f"🚀 正在尝试在 {path} 创建页面...")
        url = f"https://api.github.com/repos/{repo}/contents/{path}"
        res = requests.get(url, headers=headers)
        sha = res.json().get('sha') if res.status_code == 200 else None
        
        data = {"message": f"🤖 OpenClaw: 修复 404 路径 {path}", "content": base64.b64encode(code.encode()).decode()}
        if sha: data["sha"] = sha
        
        requests.put(url, json=data, headers=headers)

    print("✅ 双路径修复指令已发出！")
    print("🔗 请在 2 分钟后访问：https://seekapi.ai/blog")

if __name__ == "__main__":
    universal_fix()
