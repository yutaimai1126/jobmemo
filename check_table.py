import sqlite3

dbname = 'interest.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# terminalで実行したSQL文と同じようにexecute()に書く
cur.execute('SELECT * FROM persons')

# 中身を全て取得するfetchall()を使って、printする。
print(cur.fetchall())

cur.close()
conn.close()