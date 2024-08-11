import sqlite3

dbname = 'TEST.db'
conn = sqlite3.connect(dbname)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# personsというtableを作成してみる
# 大文字部はSQL文。小文字でも問題ない。
# "name"に"Taro"を入れる
cur.execute('INSERT INTO persons(name) values("Taro")')
# 同様に
cur.execute('INSERT INTO persons(name) values("Hanako")')
cur.execute('INSERT INTO persons(name) values("Hiroki")')

conn.commit()

# データベースへコミット。これで変更が反映される。
conn.commit()
conn.close()