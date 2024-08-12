import streamlit as st
import sqlite3
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Streamlitアプリケーションのタイトル
st.title('志望度の重回帰分析')

# データベース接続
dbname = 'interest.db'
conn = sqlite3.connect(dbname)

# データを読み込む
query = 'SELECT * FROM Interest'
df = pd.read_sql(query, conn)

# 重回帰分析のためのデータ準備
# 志望度を目的変数とし、その他の列を説明変数とする
X = df[['働き方', '給与', '福利厚生', 'やりがい', '企業理念']]
y = df['志望度']

# 定数項を加える（切片を含む）
X = sm.add_constant(X)

# 重回帰モデルの適用
model = sm.OLS(y, X).fit()
coefficients = model.params

# 結果を表示
st.write('重回帰分析結果:')
st.write(model.summary())

# 重要度（係数）を棒グラフで表示
fig, ax = plt.subplots(figsize=(10, 6))
coefficients.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('各説明変数の係数')
ax.set_xlabel('説明変数')
ax.set_ylabel('係数')

# グラフをStreamlitに表示
st.pyplot(fig)

# 接続を閉じる
conn.close()
