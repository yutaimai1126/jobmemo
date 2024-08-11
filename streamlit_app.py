import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Job Memo", page_icon='icon.png')

name = 'タクヤ'
st.title(f"{name}さんのマイページ")

first_time = st.radio(
    f'JobMemoの利用は初めてですか？',
    ['はい','いいえ']
    )

st.header(f'{name}さん、会社説明会お疲れさまでした')
company_name = st.text_input('説明会を受けた会社名は何ですか？', '')

# データベースに接続
conn = sqlite3.connect('interest.db')
cur = conn.cursor()
if first_time == 'はい':
    # データフレーム読み込み
    interest_list = ['働き方','給与','福利厚生','やりがい','企業理念']
    df = pd.DataFrame(0,index=company_name, columns=interest_list)
else:
    df = pd.read_sql('SELECT * FROM sample', conn)

st.text(f'{name}さんが最も興味を持ったことは何ですか？')
for i, interest in enumerate(interest_list):
    df.loc[company_name,interest] = st.radio(interest)

df.to_sql('sample', conn, if_exists='replace')

# データベースをクローズする
cur.close()
conn.close()