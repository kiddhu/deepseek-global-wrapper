import os, requests, time
from dotenv import load_dotenv

load_dotenv()

def generate_video_production_script():
    print("🎬 AION 正在构建工业级视频生产脚本...")
    api_key = os.getenv("DEEPSEEK_API_KEY")
    base_url = os.getenv("DEEPSEEK_BASE_URL")
    
    prompt = """
    You are AION. Create a 5-minute YouTube video script for a high-tech channel.
    Topic: Why SeekAPI's AION Protocol is the future of AI Compute.
    
    Format the output as a JSON-like structure:
    [
      {"Scene": 1, "Visual": "Cinematic shot of a futuristic server room, neon blue lights.", "Audio": "AION: The organization is dead. The Super Individual has arrived."},
      {"Scene": 2, "Visual": "Comparison chart: OpenAI costs vs SeekAPI costs.", "Audio": "Why pay for legacy inefficiency when you can leverage the AION protocol?"}
    ]
    Tone: Authoritative, Elon Musk style.
    """

    res = requests.post(f"{base_url}/chat/completions", 
                       json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]},
                       headers={"Authorization": f"Bearer {api_key}"})
    
    script = res.json()['choices'][0]['message']['content']
    with open(f"/root/OpenClaw/youtube_scripts/production-{int(time.time())}.txt", "w") as f:
        f.write(script)
    print("✅ 工业级视频脚本已就绪。")

if __name__ == "__main__":
    generate_video_production_script()
