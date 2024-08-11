import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Job Memo", page_icon='icon.png')

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
    # 新しいデータフレームを作成
    df = pd.DataFrame(index=[company_name], columns=interest_list)
else:
    df = pd.read_sql('SELECT * FROM sample', conn, index_col='index')

st.text(f'{name}さんが最も興味を持ったことは何ですか？')
for interest in interest_list:
    df.loc[company_name, interest] =  st.radio(interest)

# データフレームの表示
st.write(df)

# 保存ボタンを追加
if st.button('保存'):
    df.to_sql('sample', conn, if_exists='append', index=True)
    conn.commit()  # 変更をコミット
    st.success("データが保存されました。")

# データベースをクローズする
cur.close()
conn.close()
