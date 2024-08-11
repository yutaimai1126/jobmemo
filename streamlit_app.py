import streamlit as st
import sqlite3
import pandas as pd
import os

st.set_page_config(page_title="Job Memo", page_icon='icon.png')

def check_db_schema():
    db_path = 'interest.db'
    
    if not os.path.exists(db_path):
        st.write(f"{db_path} は存在しません。")
        return
    
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        
        if tables:
            st.write("データベース内のテーブル:")
            for table in tables:
                st.write(f"- {table[0]}")
                
                cur.execute(f"PRAGMA table_info({table[0]});")
                columns = cur.fetchall()
                st.write("カラム情報:")
                for column in columns:
                    st.write(f"  - {column[1]}: {column[2]}")
        else:
            st.write("データベースにはテーブルがありません。")

st.title("データベース状態確認")
check_db_schema()

@st.cache_data
def init_db():
    with sqlite3.connect('interest.db') as conn:
        cur = conn.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS sample (
            company_name TEXT PRIMARY KEY,
            働き方 INTEGER,
            給与 INTEGER,
            福利厚生 INTEGER,
            やりがい INTEGER,
            企業理念 INTEGER,
            コメント TEXT
        )
        ''')
        conn.commit()

name = 'タクヤ'
st.title(f"{name}さんのマイページ")

init_db()

first_time = st.radio(
    'JobMemoの利用は初めてですか？',
    ['はい', 'いいえ'],
    key='first_time_radio'
)

st.header(f'{name}さん、会社説明会お疲れさまでした')
company_name = st.text_input('説明会を受けた会社名は何ですか？', '', key='company_name_input')

# データベースに接続
with sqlite3.connect('interest.db') as conn:
    cur = conn.cursor()
    interest_list = ['働き方', '給与', '福利厚生', 'やりがい', '企業理念']

    if first_time == 'はい':
        df = pd.DataFrame(0, index=[company_name], columns=interest_list + ['コメント'])
        df.index.name = 'company_name'
    else:
        df = pd.read_sql('SELECT * FROM sample', conn)
        df.set_index('company_name', inplace=True)

    selected_interest = st.radio(
        f'{name}さんが最も興味を持ったことは何ですか？',
        interest_list,
        key='interest_radio'
    )

    if company_name:
        df.loc[company_name, selected_interest] = 1
    
    comment = st.text_area('コメントを入力してください', value='', height=100)
    df.loc[company_name, 'コメント'] = comment

    st.write(df)

    if st.button('保存'):
        try:
            with sqlite3.connect('interest.db') as conn:
                df.to_sql('sample', conn, if_exists='replace', index=True)
                conn.commit()
                st.success("データが保存されました。")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
