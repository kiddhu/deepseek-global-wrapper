import sys

from db_utils import get_db_connection


def main() -> int:
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1")
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row and row[0] == 1:
            print("✅ Supabase 大脑连接成功（SELECT 1 返回正常）。")
            return 0
        print("⚠️ 已连接但返回结果异常：", row)
        return 1
    except Exception as e:
        print("❌ Supabase 大脑连接失败：", repr(e))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

