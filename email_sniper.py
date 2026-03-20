import requests
import os
from notifier import send_alert
from db_utils import is_duplicate_lead, log_action, get_db_connection

# --- 配置 ---
N8N_PROD_WEBHOOK = 'http://43.153.221.23:5678/webhook/github-leads'
TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()

def hunt():
    print('🚀 AION 猎手正在执行带记忆的深度扫描...')
    url = 'https://api.github.com/search/code?q=import+openai+language:python&sort=indexed'
    
    try:
        res = requests.get(url, headers={'Authorization': f'token {TOKEN}'})
        items = res.json().get('items', [])[:5]
        
        new_leads_count = 0
        for item in items:
            username = item['repository']['owner']['login']
            repo = item['repository']['name']
            
            # --- 记忆检查 ---
            if is_duplicate_lead(username):
                print(f'跳过已知巨鲸: {username}')
                continue

            # 推送至 n8n (进而触发 Discord)
            data = {'user': username, 'repo': repo, 'language': 'Python'}
            requests.post(N8N_PROD_WEBHOOK, json=data)
            
            # 写入数据库
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO lead_tracking (username, repo, status) VALUES (%s, %s, %s)',
                        (username, repo, 'CAPTURED'))
            conn.commit()
            cur.close()
            conn.close()
            
            new_leads_count += 1
            print(f'✅ 成功捕获新巨鲸: {username}')

        if new_leads_count > 0:
            log_action('The Hunter', 'HUNT', 'GitHub', f'Captured {new_leads_count} new leads', 'SUCCESS')
            send_alert('The Hunter', 'SUCCESS', f'本次巡逻发现 {new_leads_count} 位新巨鲸，已入库。')
        else:
            print('本次未发现新面孔。')

    except Exception as e:
        log_action('The Hunter', 'ERROR', 'GitHub', str(e), 'FAILED')
        send_alert('The Hunter', 'ERROR', str(e))

if __name__ == "__main__":
    hunt()