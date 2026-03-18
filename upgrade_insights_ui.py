import requests
import base64

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def upgrade_ui():
    url = f"https://api.github.com/repos/{REPO}/contents/app/insights/page.jsx"
    
    # 这是一个极其健壮的前端代码，专门用于读取 insights 目录并显示标题
    new_ui_code = """
import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'
import { MDXRemote } from 'next-mdx-remote/rsc'

export default async function InsightsPage() {
  const insightsDirectory = path.join(process.cwd(), 'insights')
  const filenames = fs.readdirSync(insightsDirectory)

  const posts = filenames.map((filename) => {
    const filePath = path.join(insightsDirectory, filename)
    const fileContents = fs.readFileSync(filePath, 'utf8')
    const { data, content } = matter(fileContents)
    return {
      filename,
      title: data.title || 'AION Intelligence Report',
      date: data.date || '2025-03-16',
      content
    }
  }).sort((a, b) => new Date(b.date) - new Date(a.date))

  return (
    <div className="max-w-5xl mx-auto px-4 py-12">
      <h1 className="text-4xl font-extrabold text-white mb-12 text-center">AION Insights</h1>
      <div className="grid gap-8">
        {posts.map((post) => (
          <article key={post.filename} className="bg-zinc-900 border border-zinc-800 p-8 rounded-2xl shadow-2xl">
            <header className="mb-6">
              <h2 className="text-2xl font-bold text-blue-400 mb-2">{post.title}</h2>
              <time className="text-zinc-500 text-sm">{post.date}</time>
            </header>
            <div className="prose prose-invert max-w-none text-zinc-300">
              <MDXRemote source={post.content} />
            </div>
          </article>
        ))}
      </div>
    </div>
  )
}
"""
    
    res = requests.get(url, headers=HEADERS)
    payload = {
        "message": "AION: Upgrading Insights UI to God-Mode",
        "content": base64.b64encode(new_ui_code.encode('utf-8')).decode('utf-8'),
        "sha": res.json()['sha'] if res.status_code == 200 else None
    }
    
    requests.put(url, json=payload, headers=HEADERS)
    print("✅ app/insights/page.jsx 已升级为神级兼容模式！")

if __name__ == "__main__":
    upgrade_ui()
