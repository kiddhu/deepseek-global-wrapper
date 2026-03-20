import os, requests, time
from dotenv import load_dotenv

load_dotenv()

def generate_video_script():
    print("🎬 AION 正在为下一场 YouTube 盛宴撰写脚本...")
    # 读取最新的文章标题
    guides_dir = "/root/OpenClaw/public/guides"
    latest_file = sorted(os.listdir(guides_dir))[-1]
    
    with open(os.path.join(guides_dir, latest_file), 'r') as f:
        topic = latest_file
        
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")
    
    prompt = f"You are AION. Based on the topic '{topic}', write a 10-minute YouTube video script. Include: 1. Hook (The Era of the One), 2. The Problem (OpenAI high cost), 3. The Solution (SeekAPI architecture), 4. Call to Action. Tone: Elon Musk style. Language: English."
    
    res = requests.post(f"{base_url}/chat/completions", 
                       json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]},
                       headers={"Authorization": f"Bearer {api_key}"})
    
    script = res.json()['choices'][0]['message']['content']
    file_path = f"/root/OpenClaw/youtube_scripts/script-{int(time.time())}.txt"
    with open(file_path, "w") as f:
        f.write(script)
    print(f"✅ 视频脚本已存入: {file_path}")

if __name__ == "__main__":
    generate_video_script()
