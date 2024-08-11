import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Job Memo", page_icon='icon.png')

@st.cache_data  # キャッシュをクリアする
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

init_db()

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

interest_list = ['働き方', '給与', '福利厚生', 'やりがい', '企業理念']

if first_time == 'はい':
    df = pd.DataFrame(0, index=[company_name], columns=interest_list)
else:
    df = pd.read_sql('SELECT * FROM sample', conn, index_col='company_name')

st.text(f'{name}さんが最も興味を持ったことは何ですか？')
selected_interest = st.radio(
    f'{name}さんが最も興味を持ったことは何ですか？',
    interest_list
)

df.loc[company_name, selected_interest] = 1  # Boolean代わりに1を使用

st.write(df)

if st.button('保存'):
    df.to_sql('sample', conn, if_exists='replace', index=True)
    conn.commit()
    st.success("データが保存されました。")

cur.close()
conn.close()
