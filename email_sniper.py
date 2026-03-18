import requests
import os
from notifier import send_alert

N8N_PROD_WEBHOOK = "http://43.153.221.23:5678/webhook/github-leads"
TOKEN = open('/root/OpenClaw/github_token.txt').read().strip()

def hunt():
    url = "https://api.github.com/search/code?q=import+openai+language:python&sort=indexed"
    res = requests.get(url, headers={"Authorization": f"token {TOKEN}"})
    items = res.json().get('items', [])[:3]
    for item in items:
        data = {"user": item['repository']['owner']['login'], "repo": item['repository']['name'], "language": "Python"}
        requests.post(N8N_PROD_WEBHOOK, json=data)
    send_alert("The Hunter", "SUCCESS", f"捕获 {len(items)} 条生产线索")

if __name__ == "__main__":
    hunt()
