import os, re

def clean_html_files():
    guides_dir = "/root/OpenClaw/public/guides"
    if not os.path.exists(guides_dir): return
    
    print("🧹 正在对 AION 内容库进行深度排版清洗...")
    
    for f_name in os.listdir(guides_dir):
        if f_name.endswith('.html') and f_name != 'index.html':
            path = os.path.join(guides_dir, f_name)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 1. 提取标题 (尝试从 <h1> 或第一行提取)
            title_match = re.search(r'<h1>(.*?)</h1>', content)
            if title_match:
                title = title_match.group(1)
            else:
                # 如果没找到 h1，尝试拿掉 HTML 标签后的前 50 个字符
                clean_text = re.sub('<[^<]+?>', '', content).strip()
                title = clean_text.split('\n')[0][:60]

            # 2. 重新注入 AION 顶级排版样式
            styled_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title} | AION Insights</title>
    <style>
        body {{ font-family: 'Inter', -apple-system, sans-serif; line-height: 1.8; max-width: 800px; margin: 0 auto; padding: 60px 20px; background: #000; color: #eee; }}
        h1 {{ font-size: 42px; color: #2563eb; letter-spacing: -2px; line-height: 1.1; margin-bottom: 30px; }}
        h2 {{ font-size: 24px; color: #fff; margin-top: 40px; border-left: 4px solid #2563eb; padding-left: 15px; }}
        p {{ margin-bottom: 20px; color: #ccc; font-size: 18px; }}
        code {{ background: #111; color: #0f0; padding: 2px 6px; border-radius: 4px; font-family: monospace; }}
        pre {{ background: #050505; padding: 20px; border-radius: 12px; border: 1px solid #222; overflow-x: auto; color: #0f0; }}
        .back {{ display: block; margin-bottom: 40px; color: #666; text-decoration: none; font-size: 14px; }}
        .back:hover {{ color: #2563eb; }}
        hr {{ border: 0; border-top: 1px solid #111; margin: 50px 0; }}
    </style>
</head>
<body>
    <a href="/insights" class="back">← BACK TO INSIGHTS HUB</a>
    <h1>{title}</h1>
    <div class="article-body">
        {content if '<h1>' in content else '<p>' + content.replace('\\n', '</p><p>') + '</p>'}
    </div>
    <hr>
    <p style="text-align:center; font-size: 12px; color: #444;">AION: The Era of the One. | SeekAPI.ai</p>
</body>
</html>"""
            with open(path, 'w', encoding='utf-8') as f:
                f.write(styled_content)
            print(f"✅ 已修复排版: {f_name}")

if __name__ == "__main__":
    clean_html_files()
