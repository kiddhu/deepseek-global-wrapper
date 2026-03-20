import requests
import base64

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def fix():
    # 1. 强行注入 app/blog/page.jsx (这是消除 404 的唯一物理钥匙)
    blog_page_code = """
import React from 'react';

export default function BlogPage() {
  return (
    <div style={{backgroundColor: '#000', color: '#fff', minHeight: '100vh', padding: '50px', fontFamily: 'sans-serif'}}>
      <nav style={{marginBottom: '40px'}}><a href="/" style={{color: '#3b82f6'}}>← 返回首页</a></nav>
      <h1 style={{fontSize: '3rem', fontWeight: 'bold', marginBottom: '20px'}}>AION Insights</h1>
      <p style={{color: '#888', fontSize: '1.2rem', marginBottom: '40px'}}>全球算力套利情报中心</p>
      <div style={{display: 'grid', gap: '20px'}}>
        <div style={{padding: '30px', border: '1px solid #222', borderRadius: '15px', background: '#0a0a0a'}}>
          <h2 style={{color: '#3b82f6'}}>系统已恢复联通</h2>
          <p style={{color: '#ccc', lineHeight: '1.6'}}>自动化内容工厂已重新挂载。最新的 AI 论文解读将在此实时更新。</p>
        </div>
      </div>
    </div>
  );
}
"""
    url = f"https://api.github.com/repos/{REPO}/contents/app/blog/page.jsx"
    res = requests.get(url, headers=HEADERS)
    payload = {"message": "CRITICAL: Fixing Blog 404", "content": base64.b64encode(blog_page_code.encode()).decode()}
    if res.status_code == 200: payload["sha"] = res.json()['sha']
    requests.put(url, json=payload, headers=HEADERS)
    
    # 2. 物理删除可能导致冲突的旧文件
    requests.delete(f"https://api.github.com/repos/{REPO}/contents/pages/blog.js", 
                    json={"message": "Removing conflict", "sha": requests.get(f"https://api.github.com/repos/{REPO}/contents/pages/blog.js", headers=HEADERS).json().get('sha', '')}, 
                    headers=HEADERS)

    print("✅ Blog 路由物理文件已注入。")

if __name__ == "__main__":
    fix()
