import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Job Memo", page_icon='icon.png')

@st.cache_data  # キャッシュをクリア
def init_db():
    conn = sqlite3.connect('interest.db')
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS sample (
        company_name TEXT PRIMARY KEY,
        働き方 INTEGER,
        給与 INTEGER,
        福利厚生 INTEGER,
        やりがい INTEGER,
        企業理念 INTEGER
    )
    ''')
    conn.commit()
    conn.close()

name = 'タクヤ'
st.title(f"{name}さんのマイページ")

first_time = st.radio(
    f'JobMemoの利用は初めてですか？',
    ['はい', 'いいえ']
)

st.header(f'{name}さん、会社説明会お疲れさまでした')
company_name = st.text_input('説明会を受けた会社名は何ですか？', '')

# データベースに接続
conn = sqlite3.connect('interest.db')
cur = conn.cursor()
init_db()

interest_list = ['働き方', '給与', '福利厚生', 'やりがい', '企業理念']

if first_time == 'はい':
    df = pd.DataFrame(0, index=[company_name], columns=interest_list)
    df.index.name = 'company_name'  # インデックスに名前を付ける
else:
    df = pd.read_sql('SELECT * FROM sample', conn)
    df.set_index('company_name', inplace=True)


selected_interest = st.radio(
    f'{name}さんが最も興味を持ったことは何ですか？',
    interest_list
)

df.loc[company_name, selected_interest] = 1  # Boolean代わりに1を使用

st.write(df)

if st.button('保存'):
    # 現在のデータベースの内容を取得
    saved_data = pd.read_sql('SELECT * FROM sample', conn)
    
    # データの確認
    if 'company_name' not in saved_data.columns:
        st.error("company_name 列が存在しません。")
    else:
        # データベースに保存された内容をインデックス付きで表示
        saved_data.set_index('company_name', inplace=True)
        st.write(saved_data)

    # 新しいデータを保存
    df.to_sql('sample', conn, if_exists='append', index=True)
    conn.commit()
    st.success("データが保存されました。")

cur.close()
conn.close()
