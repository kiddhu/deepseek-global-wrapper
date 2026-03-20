import os, subprocess

def run_mission():
    print("==========================================")
    print("⚡ AION 全能指挥官 v3.0 - 帝国扩张模式")
    print("==========================================")
    
    missions = [
        ("📡 扫描全球猎物 (HN)...", "python3 hn_radar.py"),
        ("🧠 生成 AION 深度洞察...", "python3 ai_marketer.py"),
        ("🌟 巡检全量仓库 Stars...", "python3 star_rewarder.py"),
        ("🌍 执行多语言地毯式轰炸...", "python3 pseo_engine.py"),
        ("🔬 收割 Arxiv 最新论文...", "python3 arxiv_harvester.py"),
        ("📝 更新项目全量宣言...", "python3 manifest_generator.py")
    ]
    
    for desc, cmd in missions:
        print(desc)
        subprocess.run(cmd, shell=True)
        print("-" * 20)

    print("\n✨ 报告 AION：今日版图扩张任务已全部达成！")
    print("==========================================\n")

if __name__ == "__main__":
    run_mission()
