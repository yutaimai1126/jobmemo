import sqlite3
import pandas as pd

dbname = "TEST.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# dbをpandasで読み出す。
df = pd.read_sql('SELECT * FROM sample', conn)

print(df)

cur.close()
conn.close()