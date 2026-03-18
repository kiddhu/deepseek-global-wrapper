import os
import requests
import base64
from dotenv import load_dotenv

load_dotenv()

def generate_and_push_blog():
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")
    gh_token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPO")
    
    print("🏭 大龙虾内容工厂启动：正在撰写深度技术博客...")

    # 1. 让 AI 撰写博客内容
    prompt = "Write a professional technical blog post in English. Title: 'How to Slash Your AI Inference Costs by 90% using DeepSeek R1 and SeekAPI'. Focus on developers using OpenAI who are struggling with high bills. Mention compatibility, latency, and global access. Format as Markdown."
    
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        # 生成内容
        res = requests.post(f"{base_url}/chat/completions", json=payload, headers=headers)
        blog_markdown = res.json()['choices'][0]['message']['content']
        
        # 2. 将内容推送到 GitHub (存放在 blog-post.md)
        file_path = "blog-post.md"
        url = f"https://api.github.com/repos/{repo}/contents/{file_path}"
        gh_headers = {"Authorization": f"Bearer {gh_token}", "Accept": "application/vnd.github+json"}
        
        # 获取旧文件 SHA (如果存在)
        get_res = requests.get(url, headers=gh_headers)
        sha = get_res.json().get('sha') if get_res.status_code == 200 else None

        # 提交更新
        encoded_content = base64.b64encode(blog_markdown.encode('utf-8')).decode('utf-8')
        put_data = {
            "message": "🤖 OpenClaw: 自动发布最新技术博客",
            "content": encoded_content
        }
        if sha: put_data["sha"] = sha

        put_res = requests.put(url, json=put_data, headers=gh_headers)
        
        if put_res.status_code in [200, 201]:
            print("\n" + "✅"*10)
            print("✅ 博客内容已生成并成功推送到 GitHub！")
            print(f"✅ Vercel 正在自动部署，几分钟后访问 seekapi.ai 即可看到更新。")
            print("✅"*10)
        else:
            print(f"❌ 推送 GitHub 失败: {put_res.text}")

    except Exception as e:
        print(f"❌ 内容工厂运行出错: {e}")

if __name__ == "__main__":
    generate_and_push_blog()
