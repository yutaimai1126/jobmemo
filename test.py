import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# データベース接続
dbname = 'interest.db'
conn = sqlite3.connect(dbname)

# データを読み込む
query = 'SELECT * FROM Interest'
df = pd.read_sql(query, conn)

# 各項目について合計を計算する
interest_list = ['働き方', '給与', '福利厚生', 'やりがい', '企業理念']
sum_interests = df[interest_list].sum()

# グラフを作成
plt.figure(figsize=(10, 6))

# 各項目の合計を棒グラフで表示
sum_interests.plot(kind='bar', color='skyblue')

# グラフのタイトルとラベルを設定
plt.title('各項目の合計')
plt.xlabel('Interest')
plt.ylabel('Total Count')

# グラフを表示
plt.tight_layout()
plt.show()

# 接続を閉じる
conn.close()
