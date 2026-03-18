import requests
import base64
import json

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def run_pivot():
    # 1. 确保 package.json 存在于根目录
    pkg_data = {
        "name": "seekapi-web",
        "version": "1.1.0",
        "dependencies": {
            "react": "latest", "react-dom": "latest", "next": "latest",
            "gray-matter": "latest", "next-mdx-remote": "latest"
        }
    }
    res_pkg = requests.get(f"https://api.github.com/repos/{REPO}/contents/package.json", headers=HEADERS)
    payload_pkg = {"message": "AION: Pivot Foundation", "content": base64.b64encode(json.dumps(pkg_data, indent=2).encode()).decode()}
    if res_pkg.status_code == 200: payload_pkg["sha"] = res_pkg.json()['sha']
    requests.put(f"https://api.github.com/repos/{REPO}/contents/package.json", json=payload_pkg, headers=HEADERS)

    # 2. 重写 app/blog/page.jsx (神级兼容版)
    blog_ui_code = """
import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'
import { MDXRemote } from 'next-mdx-remote/rsc'

export default async function BlogPage() {
  const blogDirectory = path.join(process.cwd(), 'blog')
  if (!fs.existsSync(blogDirectory)) return <div className="text-white p-10">Blog folder not found.</div>
  
  const filenames = fs.readdirSync(blogDirectory).filter(f => f.endswith('.md'))
  const posts = filenames.map((filename) => {
    const fileContents = fs.readFileSync(path.join(blogDirectory, filename), 'utf8')
    const { data, content } = matter(fileContents)
    return { filename, title: data.title || 'AION Report', date: data.date || '', content }
  })

  return (
    <div className="max-w-5xl mx-auto px-4 py-12 bg-black min-h-screen text-white">
      <h1 className="text-4xl font-bold mb-12 text-center">AION Blog</h1>
      <div className="grid gap-8">
        {posts.map((post) => (
          <article key={post.filename} className="bg-zinc-900 p-8 rounded-xl border border-zinc-800">
            <h2 className="text-2xl font-bold text-blue-400 mb-2">{post.title}</h2>
            <div className="prose prose-invert"><MDXRemote source={post.content} /></div>
          </article>
        ))}
      </div>
    </div>
  )
}
"""
    res_ui = requests.get(f"https://api.github.com/repos/{REPO}/contents/app/blog/page.jsx", headers=HEADERS)
    payload_ui = {"message": "AION: Pivot Blog UI", "content": base64.b64encode(blog_ui_code.encode()).decode()}
    if res_ui.status_code == 200: payload_ui["sha"] = res_ui.json()['sha']
    requests.put(f"https://api.github.com/repos/{REPO}/contents/app/blog/page.jsx", json=payload_ui, headers=HEADERS)

    print("✅ 战略转移完成：基础配置与 UI 已回归 blog 路径。")

if __name__ == "__main__":
    run_pivot()
