import os

import requests, re
from notifier import send_alert

def push():
    try:
        token = os.environ.get("GITHUB_TOKEN", "").strip()
        dev_to_key = os.environ.get("DEV_TO_API_KEY", "").strip()
        if not token:
            raise RuntimeError("Missing GITHUB_TOKEN env var for GitHub reads.")
        if not dev_to_key:
            raise RuntimeError("Missing DEV_TO_API_KEY env var for Dev.to writes.")
        url = 'https://api.github.com/repos/kiddhu/deepseek-global-wrapper/contents/blog'
        res = requests.get(url, headers={'Authorization': f'token {token}'}).json()
        md_files = sorted([f for f in res if f['name'].endswith('.md') and '_en_' in f['name']], key=lambda x: x['name'], reverse=True)
        if not md_files: return
        latest = md_files[0]
        raw_content = requests.get(latest['download_url']).text
        
        # 【核心修复】使用正则表达式剥离 --- 之间的元数据
        clean_body = re.sub(r'^---.*?---', '', raw_content, flags=re.DOTALL).strip()
        title = latest['name'].replace('.md', '').split('_', 1)[-1].replace('_', ' ')
        
        headers = {'api-key': dev_to_key, 'Content-Type': 'application/json'}
        data = {'article': {'title': title, 'published': True, 'body_markdown': clean_body, 'tags': ['ai', 'deepseek']}}
        
        post_res = requests.post('https://dev.to/api/articles', json=data, headers=headers)
        if post_res.status_code == 201:
            print('🚀 AION 帝国文章已成功穿透时区限制，在 Dev.to 上线！')
            send_alert('SEO Pusher', 'SUCCESS', f'全球分发成功：{title}')
        else:
            print(f'❌ 依然失败: {post_res.text}')
    except Exception as e:
        print(f'💥 错误: {e}')

if __name__ == "__main__":
    push()