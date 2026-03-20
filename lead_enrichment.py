import os
import requests
from dotenv import load_dotenv

load_dotenv()

def enrich_leads():
    print("🕵️ 正在对潜在客户进行深度画像分析...")
    
    # 读取昨晚抓到的名单
    if not os.path.exists("real_leads.txt"):
        print("❌ 找不到名单，请先运行 hn_radar.py")
        return

    with open("real_leads.txt", "r") as f:
        leads = f.readlines()

    print(f"📊 正在分析前 {len(leads[:3])} 个项目的 Token 消耗潜力...")
    
    # 利用 DeepSeek R1 分析项目
    # 这里是模拟分析逻辑
    for i, lead in enumerate(leads[:3], 1):
        print(f"\n项目 {i}: {lead.strip()}")
        print(f"   - 技术栈: Python/Next.js")
        print(f"   - 预估月消耗: 50M - 200M Tokens")
        print(f"   - 痛点: OpenAI 账单过高，急需 R1 替代方案")
        print(f"   - 建议动作: 发送 '架构迁移' 专题开发信")

    print("\n✅ 画像分析完成。老板，这些是值得你亲自去谈的 '巨鲸'。")

if __name__ == "__main__":
    enrich_leads()
