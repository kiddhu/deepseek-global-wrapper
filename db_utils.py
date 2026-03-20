import os

import psycopg2


SUPABASE_ENV_PATH = "/root/OpenClaw/config/supabase.env"


def _load_env_config(path: str) -> dict:
    """
    稳健解析 supabase.env，支持注释与任意行顺序。
    """
    config: dict[str, str] = {}
    if not os.path.exists(path):
        raise RuntimeError(f"Supabase config file not found: {path}")

    with open(path, "r") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()
    return config


def get_db_connection():
    """
    创建到 Supabase Postgres 的连接。

    约定：config/supabase.env 中的 DB_URL 已经是合法的
    Postgres 连接串（密码部分若含特殊字符需预先 URL 编码）。
    """
    cfg = _load_env_config(SUPABASE_ENV_PATH)
    db_url = cfg.get("DB_URL")
    if not db_url:
        raise RuntimeError("DB_URL not found in config/supabase.env")

    return psycopg2.connect(db_url)


def log_action(agent_name, action_type, target, content, status):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO agent_memory (agent_name, action_type, target, content, status) VALUES (%s, %s, %s, %s, %s)",
        (agent_name, action_type, target, content, status),
    )
    conn.commit()
    cur.close()
    conn.close()


def is_duplicate_content(title: str) -> bool:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM content_index WHERE title = %s", (title,))
    exists = cur.fetchone() is not None
    cur.close()
    conn.close()
    return exists


def is_duplicate_lead(username: str) -> bool:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM lead_tracking WHERE username = %s", (username,))
    exists = cur.fetchone() is not None
    cur.close()
    conn.close()
    return exists