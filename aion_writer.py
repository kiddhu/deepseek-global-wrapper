import base64
import os
import re
from datetime import datetime
import xml.etree.ElementTree as ET

import requests

from db_utils import get_db_connection, is_duplicate_content, log_action
from notifier import send_alert


TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
REPO = "kiddhu/deepseek-global-wrapper"
API_KEY = os.environ.get("DEEPSEEK_API_KEY", "").strip()
API_URL = "http://45.152.64.217:3000/v1/chat/completions"
VERCEL_HOOK = os.environ.get("VERCEL_HOOK_URL", "").strip()
GITHUB_API_BASE = "https://api.github.com"


LANG_CONFIG = {
    "en": "English",
    "zh": "Chinese (Simplified)",
    "ja": "Japanese",
    "fr": "French",
    "es": "Spanish",
}


def build_frontmatter(title: str, slug: str, lang: str, tags=None) -> str:
    if tags is None:
        tags = ["ai", "deepseek"]
    date = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = ["---"]
    lines.append(f'title: "{title}"')
    lines.append(f'date: "{date}"')
    lines.append(f'lang: "{lang}"')
    lines.append(f'slug: "{slug}"')
    lines.append(f"tags: {tags}")
    lines.append("---")
    return "\n".join(lines)


def put_markdown_to_github(path: str, content: str) -> None:
    if not TOKEN:
        raise RuntimeError("Missing GITHUB_TOKEN env var for GitHub API writes.")
    if not REPO:
        raise RuntimeError("Missing REPO configuration.")
    url = f"{GITHUB_API_BASE}/repos/{REPO}/contents/{path}"
    message = f"chore(blog): publish {os.path.basename(path)}"
    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    payload = {"message": message, "content": encoded}
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    res = requests.put(url, json=payload, headers=headers, timeout=30)
    res.raise_for_status()


def generate_multilang_articles(title: str, abstract: str) -> dict[str, str]:
    articles: dict[str, str] = {}
    if not API_KEY:
        raise RuntimeError("Missing DEEPSEEK_API_KEY env var for content generation.")
    for lang, lang_label in LANG_CONFIG.items():
        user_prompt = (
            f"请用{lang_label}写一篇面向工程师的技术博文，"
            f"主题为论文《{title}》，并结合以下摘要进行说明：\n\n{abstract}"
        )
        resp = requests.post(
            API_URL,
            json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": user_prompt}],
            },
            headers={"Authorization": f"Bearer {API_KEY}"},
            timeout=120,
        )
        data = resp.json()
        body = data["choices"][0]["message"]["content"].strip()
        articles[lang] = body
    return articles


def main():
    try:
        res_xml = requests.get(
            "http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=1",
            timeout=30,
        )
        root = ET.fromstring(res_xml.content)
        entry = root.find("{http://www.w3.org/2005/Atom}entry")
        if entry is None:
            raise RuntimeError("Arxiv 返回为空，未找到 entry 节点。")

        title_node = entry.find("{http://www.w3.org/2005/Atom}title")
        summary_node = entry.find("{http://www.w3.org/2005/Atom}summary")
        if title_node is None or summary_node is None:
            raise RuntimeError("Arxiv 返回缺少 title 或 summary。")

        title = title_node.text.strip()
        abstract = summary_node.text.strip()

        if is_duplicate_content(title):
            print(f"跳过已存在内容: {title}")
            return

        articles = generate_multilang_articles(title, abstract)

        today = datetime.utcnow().strftime("%Y%m%d")
        base_slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")

        for lang in LANG_CONFIG.keys():
            body = articles.get(lang, "").strip()
            if not body:
                continue

            slug = f"{base_slug}_{lang}"

            if lang == "en":
                filename = f"{today}_en_{base_slug}.md"
            else:
                filename = f"{today}_{lang}_{base_slug}.md"

            frontmatter = build_frontmatter(title, slug, lang)
            full_md = f"{frontmatter}\n\n{body}"
            path = f"blog/{filename}"
            put_markdown_to_github(path, full_md)

        conn = get_db_connection()
        cur = conn.cursor()
        for lang in LANG_CONFIG.keys():
            cur.execute(
                "INSERT INTO content_index (title) VALUES (%s)",
                (f"{title} [{lang}]",),
            )
        conn.commit()
        cur.close()
        conn.close()

        log_action("The Scholar", "PUBLISH", title, "Success", "SUCCESS")
        send_alert(
            "The Scholar",
            "SUCCESS",
            f"5 篇独立博文已全线发布: {title[:40]}",
        )

        if VERCEL_HOOK:
            try:
                requests.post(VERCEL_HOOK, timeout=5)
            except Exception:
                pass

    except Exception as e:
        log_action("The Scholar", "ERROR", "System", str(e), "FAILED")
        send_alert("The Scholar", "ERROR", str(e))


if __name__ == "__main__":
    main()