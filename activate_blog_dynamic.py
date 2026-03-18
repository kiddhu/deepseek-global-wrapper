import requests
import base64

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def activate():
    # 升级 app/blog/page.jsx，使其具备自动读取文件夹的能力
    dynamic_code = """
import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

export default async function BlogPage() {
  const blogDir = path.join(process.cwd(), 'blog')
  let posts = []
  
  if (fs.existsSync(blogDir)) {
    const files = fs.readdirSync(blogDir).filter(f => f.endswith('.md'))
    posts = files.map(filename => {
      const content = fs.readFileSync(path.join(blogDir, filename), 'utf8')
      const { data } = matter(content)
      return {
        slug: filename.replace('.md', ''),
        title: data.title || 'AION Intelligence Report',
        date: data.date || '2025-03-16'
      }
    }).sort((a, b) => new Date(b.date) - new Date(a.date))
  }

  return (
    <div className="min-h-screen bg-black text-white p-8 md:p-24 font-sans">
      <h1 className="text-5xl font-extrabold mb-12 bg-gradient-to-r from-blue-500 to-purple-500 bg-clip-text text-transparent">
        AION Insights Hub
      </h1>
      <div className="grid gap-6">
        {posts.length > 0 ? posts.map(post => (
          <a href={`/blog/${post.slug}`} key={post.slug} className="block p-6 bg-zinc-900 border border-zinc-800 rounded-2xl hover:border-blue-500 transition-all">
            <h2 className="text-2xl font-bold text-blue-400 mb-2">{post.title}</h2>
            <p className="text-zinc-500 text-sm">{post.date}</p>
          </a>
        )) : <p className="text-zinc-400">正在同步全球算力情报...</p>}
      </div>
    </div>
  )
}
"""
    url = f"https://api.github.com/repos/{REPO}/contents/app/blog/page.jsx"
    res = requests.get(url, headers=HEADERS)
    payload = {
        "message": "AION: Activating dynamic blog loader",
        "content": base64.b64encode(dynamic_code.encode()).decode(),
        "sha": res.json()['sha'] if res.status_code == 200 else None
      }
    requests.put(url, json=payload, headers=HEADERS)
    print("✅ Blog 页面已升级为动态模式。")

if __name__ == "__main__":
    activate()
