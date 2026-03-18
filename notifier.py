import requests
import datetime
import os

def send_alert(agent_name, status, message):
    webhook_url = 'https://discord.com/api/webhooks/1482668735520313345/O_nLhZZvv9zZtV3EyrXdpeTk_wt6sPZrumDCU4p1IlKLDJM7JfpXkz3DN-gkBudHPejh'
    log_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'[{log_time}] [{agent_name}] [{status}] {message}\n'
    
    # 1. 物理写入本地审计日志
    try:
        with open('/root/OpenClaw/audit.log', 'a') as f:
            f.write(log_entry)
    except Exception as e:
        print(f'Log Write Error: {e}')
    
    # 2. 发送 Discord 通知
    payload = {
        'content': f'🚀 **[AION 报告]**\n**时间:** \n**Agent:** \n**状态:** {status}\n**详情:** {message}'
    }
    try:
        requests.post(webhook_url, json=payload, timeout=10)
    except:
        pass

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 3:
        send_alert(sys.argv[1], sys.argv[2], sys.argv[3])