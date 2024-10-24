import os
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

plt.rcParams["font.size"] = 18

font_path = os.path.abspath("font/fonts-japanese-gothic.ttf")
font_manager.fontManager.addfont(font_path)
plt.rc('font', family="IPAexGothic")

# Streamlitアプリケーションのタイトル
name = 'タクヤ'
st.title(f'{name}さんの興味の傾向')

# データベース接続
dbname = 'interest.db'
conn = sqlite3.connect(dbname)

# データを読み込む
query = 'SELECT * FROM Interest'
df = pd.read_sql(query, conn)

# st.write(df)

# 各項目について合計を計算する
interest_list = ['働き方', '給与', '福利厚生', 'やりがい', '企業理念']
sum_interests = df[interest_list].sum()

# グラフを作成
fig, ax = plt.subplots(figsize=(10, 6))

# 各項目の合計を棒グラフで表示
sum_interests.plot(kind='bar', ax=ax)

# グラフのタイトルとラベルを設定
ax.set_title('各項目の合計')
ax.set_xlabel('興味')
ax.set_ylabel('興味を持った回数')

# グラフをStreamlitに表示
st.pyplot(fig)

# グラフを作成
plt.figure(figsize=(10, 6))

# 各企業の志望度を棒グラフで表示
df.plot(kind='bar', x='company_name', y='志望度', legend=False)

# グラフのタイトルとラベルを設定
plt.title('志望度の比較')
plt.xlabel('会社名')
plt.ylabel('志望度（%）')

# グラフを表示
st.pyplot(plt)

# 接続を閉じる
conn.close()
