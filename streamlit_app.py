import streamlit as st
import sqlite3

st.set_page_config(page_title="Job Memo", page_icon='icon.png')

name = 'タクヤ'

st.title(f"{name}さんのマイページ")

first_time = st.radio(
    f'はじめまして{name}さん、JobMemoの利用は初めてですか？',
    ['はい','いいえ']
    )

if first_time == 'はい':
    st.header(f'はじめまして{name}さん。会社説明会お疲れさまでした')

    company_name = st.text_input('会社名', '')

    # st.text()

    ziku = st.radio(
        f'{name}さんは就活の軸が決まっていますか？',
        ['決まっている','決まっていない']
        )

    if ziku == '決まっている':
        st.subheader(f'{company_name}')
        st.text(f'{name}さんは何に興味を持ちましたか？')
    elif ziku == '決まっていない':
        st.subheader(f'{company_name}')
        st.text(f'{name}さんの就活の軸は何ですか？')
    
    interest_list = ['働き方','給与','福利厚生','やりがい','企業理念']
    for interest in interest_list:
        st.checkbox(interest)
    


# データベースに接続する
conn = sqlite3.connect('interest.db')
c = conn.cursor()

def show_data():
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    for d in data:
        st.write(d)

interest_list = ['国内シェア','海外進出度','将来性']
for interest in interest_list:
    st.checkbox(interest)

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