import os
import sqlite3

def check_db_schema():
    db_path = 'interest.db'
    
    if not os.path.exists(db_path):
        print(f"{db_path} は存在しません。")
        return
    
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        
        if tables:
            print("データベース内のテーブル:")
            for table in tables:
                print(f"- {table[0]}")
                
                cur.execute(f"PRAGMA table_info({table[0]});")
                columns = cur.fetchall()
                print("カラム情報:")
                for column in columns:
                    print(f"  - {column[1]}: {column[2]}")
        else:
            print("データベースにはテーブルがありません。")

check_db_schema()
