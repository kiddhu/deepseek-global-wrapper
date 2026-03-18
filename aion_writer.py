import requests, base64, os, re, xml.etree.ElementTree as ET
from datetime import datetime
from notifier import send_alert

TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()
REPO = 'kiddhu/deepseek-global-wrapper'
API_KEY = 'sk-RrRZvw7hsptHDZwE164164E31cE748Da8dCeCbCcCd56B90b'
API_URL = 'http://45.152.64.217:3000/v1/chat/completions'
VERCEL_HOOK = 'https://api.vercel.com/v1/integrations/deploy/prj_MuIfU5xCyvQ8iJLupWAcp8i7sBaQ/Ok08VWRVPu'
LANGS = {'cn': '中文', 'en': 'English', 'jp': '日本語', 'fr': 'Français', 'es': 'Español'}

def main():
    send_alert('The Scholar', 'START', '矩阵模式：正在生成 5 国独立博文...')
    try:
        res_xml = requests.get('http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=1&sortBy=submittedDate&sortOrder=descending')
        root = ET.fromstring(res_xml.content)
        entry = root.find('{http://www.w3.org/2005/Atom}entry')
        raw_title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip().replace('\n', ' ')
        date_now = datetime.now().strftime('%Y-%m-%d')
        
        for lang_code, lang_name in LANGS.items():
            prompt = f'你是一个硅谷顶级技术博主。请针对论文《{raw_title}》写一篇极具传播力的技术分析。要求：1. 使用语言：{lang_name}。2. 严禁政治。3. 结尾植入 SeekAPI.ai。4. 返回纯 Markdown。'
            res = requests.post(API_URL, json={'model': 'deepseek-chat', 'messages': [{'role': 'user', 'content': prompt}]}, headers={'Authorization': f'Bearer {API_KEY}'})
            article_body = res.json()['choices'][0]['message']['content']
            
            safe_title = ''.join([c for c in raw_title[:30] if c.isalnum() or c==' ']).replace(' ', '_')
            filename = f'{date_now}_{lang_code}_{safe_title}.md'
            final_md = f'---\ntitle: "[{lang_code.upper()}] {raw_title[:60]}"\ndate: "{date_now}"\n---\n\n' + article_body
            
            url = f'https://api.github.com/repos/{REPO}/contents/blog/{filename}'
            requests.put(url, json={'message': f'Matrix: {lang_code}', 'content': base64.b64encode(final_md.encode()).decode()}, headers={'Authorization': f'token {TOKEN}'})
            print(f'✅ 已上传: {filename}')
            
        requests.post(VERCEL_HOOK)
        os.system('python3 /root/OpenClaw/seo_pusher.py')
        send_alert('The Scholar', 'SUCCESS', '5 篇独立博文已全线发布。')
    except Exception as e:
        send_alert('The Scholar', 'ERROR', str(e))

if __name__ == "__main__":
    main()