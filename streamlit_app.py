import streamlit as st

st.set_page_config(page_title="Job Memo", page_icon='icon.png')

st.title("タクヤさんのマイページ")

st.header('会社説明会')

text_input = st.text_input('会社名', 'テキスト入力')

st.text('タクヤさんは何に興味を持ちましたか？')

interest_list = ['国内シェア','海外進出度','将来性']
for interest in interest_list:
    st.checkbox(interest)
