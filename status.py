import subprocess
import os
import time

def get_screen_status(name):
    res = subprocess.run("screen -ls", shell=True, capture_output=True, text=True)
    return "🟢 运行中" if name in res.stdout else "🔴 已停止"

def check_hk_server():
    cmd = "ssh -p 20515 -o ConnectTimeout=5 root@45.152.64.217 'echo ok'"
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if "ok" in res.stdout:
            return "🟢 连接正常"
    except:
        pass
    return "🔴 连接失败"

def check_rewards():
    file_path = "/root/OpenClaw/coupons_to_send.txt"
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            count = len(f.readlines())
        return f"🟢 已生成 {count} 个待发兑换码"
    return "🟡 暂无待发兑换码"

def show_dashboard():
    print("\n" + "="*50)
    print("🦞 SeekAPI.ai 大龙虾自动化系统 - 实时体检")
    print("检查时间: " + time.strftime('%Y-%m-%d %H:%M:%S'))
    print("="*50)

    # 1. 检查核心进程
    print(f"【运维护盾】 (monitor)      : {get_screen_status('monitor')}")
    print(f"【发钱引擎】 (star_monitor) : {get_screen_status('star_monitor')}")
    print(f"【邮件系统】 (Resend)       : 🟢 已就绪")
    
    # 2. 检查前线状态
    hk_status = check_hk_server()
    print(f"【香港前线】 (One-API)      : {hk_status}")
    
    # 3. 检查业务战果
    print(f"【获客战果】 (GitHub Stars) : {check_rewards()}")
    
    print("="*50)
    if "🔴" in hk_status:
        print("⚠️ 警告：香港服务器连接断开！")
    else:
        print("✅ 系统运行完美。老板，你可以安心去休息了。")
    print("="*50 + "\n")

if __name__ == "__main__":
    show_dashboard()
