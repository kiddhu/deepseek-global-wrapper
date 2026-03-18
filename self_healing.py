import subprocess
import requests
import time

def check_and_heal():
    # 监控目标：你的 API 门户
    target = "https://dash.seekapi.ai"
    print(f"[{time.ctime()}] 🛡️ OpenClaw 正在巡检 SeekAPI 状态...")
    
    try:
        # 尝试访问，超时时间 10 秒
        res = requests.get(target, timeout=10)
        if res.status_code == 200:
            print("🟢 系统运行正常，无需干预。")
            return
        else:
            print(f"⚠️ 检测到异常状态码: {res.status_code}")
    except Exception as e:
        print(f"🔴 无法访问目标: {e}")

    print("🚨 启动自愈程序：正在远程重启香港服务器容器...")
    # 远程执行重启指令
    cmd = "ssh -p 20515 root@45.152.64.217 'docker restart one-api'"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("⚡ 自愈成功：One-API 容器已重启。")
    else:
        print(f"❌ 自愈失败，错误信息: {result.stderr}")

if __name__ == "__main__":
    print("🤖 OpenClaw 自愈 Agent 已启动，每 60 秒巡检一次...")
    while True:
        check_and_heal()
        time.sleep(60)
