import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# 记录已经发过奖的用户，防止重复领钱
REWARDED_LOG = "rewarded_users.json"

def get_rewarded_users():
    if os.path.exists(REWARDED_LOG):
        with open(REWARDED_LOG, "r") as f:
            return json.load(f)
    return []

def save_rewarded_user(username):
    users = get_rewarded_users()
    users.append(username)
    with open(REWARDED_LOG, "w") as f:
        json.dump(users, f)

def create_oneapi_redeem_code(amount=1.0):
    """调用 One-API 接口生成兑换码"""
    admin_token = os.getenv("SEEKAPI_MASTER_KEY")
    # One-API 默认的兑换码创建接口
    url = "https://dash.seekapi.ai/api/redemption"
    
    headers = {
        "Authorization": f"Bearer {admin_token}",
        "Content-Type": "application/json"
    }
    
    # 兑换码配置：名字包含用户ID，额度为 amount
    # 注意：One-API 的额度通常是 500000 =  (取决于你的倍率设置)
    data = {
        "name": f"Star-Reward-{int(os.urandom(2).hex(), 16)}",
        "quota": 500000, # 这里假设 500000 是 ，请根据你后台倍率调整
        "count": 1
    }
    
    try:
        res = requests.post(url, json=data, headers=headers)
        if res.status_code == 200:
            return res.json().get('data') # 返回生成的兑换码字符串
        return None
    except:
        return None

def check_stars_and_reward():
    print("🌟 大龙虾正在执行“点赞发钱”任务...")
    repos = ['deepseek-global-wrapper', 'aion-bench', 'aion-sdk-python']
    for repo_name in repos:
        repo = f'kiddhu/{repo_name}'
    token = os.getenv("GITHUB_TOKEN")
    
    url = f"https://api.github.com/repos/{repo}/stargazers"
    headers = {"Authorization": f"Bearer {token}"}
    
    res = requests.get(url, headers=headers)
    
    if res.status_code != 200:
        print(f"❌ GitHub 连接失败: {res.json().get('message')}")
        return

    stargazers = res.json()
    rewarded_list = get_rewarded_users()
    
    new_stars = 0
    for user in stargazers:
        username = user['login']
        if username not in rewarded_list:
            print(f"🎁 发现新点赞用户: {username}")
            # 真正去 One-API 生成一个兑换码
            code = create_oneapi_redeem_code()
            if code:
                print(f"✅ 已为 {username} 生成 $1.00 兑换码: {code}")
                # 将结果存入一个专门的文件，方便你发给用户
                with open("coupons_to_send.txt", "a") as f:
                    f.write(f"User: {username} | Code: {code}\n")
                save_rewarded_user(username)
                new_stars += 1
            else:
                print(f"⚠️ 兑换码生成失败，请检查 One-API 管理令牌。")

    if new_stars == 0:
        print("😴 暂时没有新点赞。")
    else:
        print(f"🚀 本次任务共发放 {new_stars} 个奖励！")

if __name__ == "__main__":
    check_stars_and_reward()
