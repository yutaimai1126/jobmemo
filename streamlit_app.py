import streamlit as st

st.set_page_config(page_title="Job Memo", page_icon='icon.png')

st.title("タクヤさんのマイページ")

st.header('会社説明会')

st.subheader('株式会社マネッセ')

st.text('タクヤさんは何に興味を持ちましたか？')

interests = ['国内シェア','海外進出度','将来性']
for interest in interests:
    st.checkbox(interest)