import requests

def spy_prices():
    print("🕵️ 大龙虾比价雷达启动...")
    
    # 监控目标：OpenRouter (全球最大的算力转售商)
    url = "https://openrouter.ai/api/v1/models"
    
    try:
        res = requests.get(url, timeout=10)
        models = res.json().get('data', [])
        
        # 寻找 DeepSeek 相关的定价
        print("\n--- 全球市场参考价 (每 1M Tokens) ---")
        for m in models:
            if "deepseek" in m['id'].lower():
                name = m['id']
                # 价格通常以美元计
                prompt_price = float(m['pricing']['prompt']) * 1000000
                completion_price = float(m['pricing']['completion']) * 1000000
                print(f"📍 {name}: ${round(prompt_price, 2)} / ${round(completion_price, 2)}")
        
        print("\n💡 架构师建议：SeekAPI 定价在 $0.5 - $1.5 之间可保持 80% 以上毛利且极具竞争力。")
        
    except Exception as e:
        print(f"❌ 比价失败: {e}")

if __name__ == "__main__":
    spy_prices()
