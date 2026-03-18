import requests
import base64

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = "kiddhu/deepseek-global-wrapper"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}

def restore():
    # 构造一个符合 Manifest v5.0 描述的“硅谷极简白”首页
    homepage_code = """
export default function HomePage() {
  return (
    <div className="min-h-screen bg-white text-black font-sans flex flex-col items-center justify-center px-6">
      <nav className="absolute top-0 w-full p-6 flex justify-between items-center max-w-6xl">
        <div className="text-2xl font-bold tracking-tighter">SeekAPI.ai</div>
        <div className="space-x-6 text-sm font-medium">
          <a href="/blog" className="hover:text-blue-600 transition">Insights</a>
          <a href="https://dash.seekapi.ai" className="bg-black text-white px-4 py-2 rounded-full hover:bg-zinc-800 transition">Console</a>
        </div>
      </nav>
      
      <main className="text-center max-w-3xl">
        <h1 className="text-6xl md:text-8xl font-extrabold tracking-tight mb-6">
          DeepSeek R1, <br />
          <span className="text-blue-600">Globally Accessible.</span>
        </h1>
        <p className="text-xl text-zinc-500 mb-10 leading-relaxed">
          95% cheaper than OpenAI. 100% API compatible. No KYC required. <br />
          The bridge between high-demand compute and low-cost supply.
        </p>
        <div className="flex flex-col md:flex-row gap-4 justify-center">
          <a href="https://dash.seekapi.ai" className="bg-blue-600 text-white px-8 py-4 rounded-xl text-lg font-bold hover:bg-blue-700 transition shadow-lg shadow-blue-200">
            Get Started Free
          </a>
          <a href="/blog" className="bg-zinc-100 text-black px-8 py-4 rounded-xl text-lg font-bold hover:bg-zinc-200 transition">
            Read Case Studies
          </a>
        </div>
      </main>
      
      <footer className="absolute bottom-10 text-zinc-400 text-sm">
        © 2025 AION Empire. All rights reserved.
      </footer>
    </div>
  )
}
"""
    url = f"https://api.github.com/repos/{REPO}/contents/app/page.jsx"
    
    # 检查是否存在
    res = requests.get(url, headers=HEADERS)
    payload = {
        "message": "AION: Restoring homepage to GitHub root",
        "content": base64.b64encode(homepage_code.encode()).decode()
    }
    if res.status_code == 200:
        payload["sha"] = res.json()['sha']

    put_res = requests.put(url, json=payload, headers=HEADERS)
    if put_res.status_code in [200, 201]:
        print("✅ 首页文件已注入 GitHub。")
    else:
        print(f"❌ 注入失败: {put_res.text}")

if __name__ == "__main__":
    restore()
