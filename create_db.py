import sqlite3

# TEST.dbを作成する
# すでに存在していれば、それにアスセスする。
dbname = 'interest.db'
conn = sqlite3.connect(dbname)

# データベースへのコネクションを閉じる。(必須)
conn.close()