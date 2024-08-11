import streamlit as st
import sqlite3

st.set_page_config(page_title="Job Memo", page_icon='icon.png')

st.title("タクヤさんのマイページ")

st.header('会社説明会お疲れさまでした')

company_name = st.text_input('会社名', '')


st.subheader(f'{company_name}')
st.text('タクヤさんは何に興味を持ちましたか？')

interest_list = ['国内シェア','海外進出度','将来性']
for interest in interest_list:
    st.checkbox(interest)

# データベースに接続する
conn = sqlite3.connect('TEST.db')
c = conn.cursor()

# データを表示する
def show_data():
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    for d in data:
        st.write(d)

# データを追加する
def add_data(name, age):
    c.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    st.write('Data added. Please reload page.')

# データベースにテーブルを作成する
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)')

# データの表示
show_data()

# データの追加
name = st.text_input('Name')
age = st.number_input('Age')
if st.button('Add data'):
    add_data(name, age)

# データベースをクローズする
conn.close()