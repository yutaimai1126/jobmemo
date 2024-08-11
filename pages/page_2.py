import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Streamlitアプリケーションのタイトル
st.title('各項目の合計')

# データベース接続
dbname = 'interest.db'
conn = sqlite3.connect(dbname)

# データを読み込む
query = 'SELECT * FROM Interest'
df = pd.read_sql(query, conn)

st.write(df)

# 各項目について合計を計算する
interest_list = ['働き方', '給与', '福利厚生', 'やりがい', '企業理念']
sum_interests = df[interest_list].sum()

# グラフを作成
fig, ax = plt.subplots(figsize=(10, 6))

# 各項目の合計を棒グラフで表示
sum_interests.plot(kind='bar', color='black', ax=ax)

# グラフのタイトルとラベルを設定
ax.set_title('各項目の合計')
ax.set_xlabel('Interest')
ax.set_ylabel('Total Count')

# グラフをStreamlitに表示
st.pyplot(fig)

# 接続を閉じる
conn.close()
