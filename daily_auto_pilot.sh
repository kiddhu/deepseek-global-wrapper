#!/bin/bash
cd /root/OpenClaw
source venv/bin/activate

echo "--- 自动化流水线启动 ---"

# 02:00 - 流量统计
python3 traffic_spy.py

# 02:05 - 算力套利检测
python3 arbitrage_engine.py

# 02:10 - 全链路自检 (幽灵注册员)
python3 ghost_registrar.py

# 02:20 - pSEO 引擎 (生成新页面)
python3 pseo_engine.py
python3 arxiv_harvester.py
python3 aion_bomber.py
python3 generate_index.py
python3 wealth_engine.py

# 02:30 - 更新项目宣言
python3 manifest_generator.py

echo "--- 任务全部完成 ---"
