import streamlit as st
import sqlite3
import pandas as pd
import csv  # 追加します

st.set_page_config(page_title="Job Memo", page_icon='icon.png')

name = 'タクヤ'
st.title(f"{name}さんのマイページ")


first_time = st.radio(
    'JobMemoの利用は初めてですか？',
    ['はい', 'いいえ'],
    key='first_time_radio'
)

st.header(f'会社説明会お疲れさまでした')
company_name = st.text_input('説明会を受けた会社名は何ですか？', '', key='company_name_input')

interest_list = ['働き方', '給与', '福利厚生', 'やりがい', '企業理念']
selected_interest = st.radio(
    f'{name}さんが最も興味を持ったことは何ですか？',
    interest_list,
    key='interest_radio'
)

p_comment = st.text_area(f'{company_name}の良い点を入力してください', value='', height=100, key='p_comment_area')
n_comment = st.text_area(f'{company_name}の悪い点を入力してください', value='', height=100, key='n_comment_area')

aspiration = st.slider('志望度', 0, 100, 50)

submit_button = st.button(label='保存')

if submit_button:
    dbname = 'interest.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Interest (
        company_name TEXT PRIMARY KEY,
        働き方 INTEGER,
        給与 INTEGER,
        福利厚生 INTEGER,
        やりがい INTEGER,
        企業理念 INTEGER,
        良い点 TEXT,
        悪い点 TEXT,
        志望度 INTEGER
    )
    ''')
    conn.commit()

    if first_time == 'はい':
        df = pd.DataFrame(0, index=[company_name], columns=interest_list + ['良い点', '悪い点', '志望度'])
        df.index.name = 'company_name'
    else:
        df = pd.read_sql('SELECT * FROM Interest', conn)
        if df.empty:
            df = pd.DataFrame(0, index=[company_name], columns=interest_list + ['良い点', '悪い点', '志望度'])
            df.index.name = 'company_name'
        else:
            df.set_index('company_name', inplace=True)
            # 新しい会社名が存在しない場合、データフレームに追加
            if company_name not in df.index:
                df.loc[company_name] = [0] * len(interest_list) + [''] * 3

    # データの更新
    if company_name:
        df.loc[company_name, selected_interest] = 1
        df.loc[company_name, '良い点'] = p_comment
        df.loc[company_name, '悪い点'] = n_comment
        df.loc[company_name, '志望度'] = aspiration

    st.write(df)

    # データベースに保存
    try:
        df.to_sql('Interest', conn, if_exists='replace', index=True)
        
        # テキスト形式で出力
        df['良い点'].to_csv('text/p_comment.txt', index=False, header=False, sep='\t', quoting=csv.QUOTE_MINIMAL)
        df['悪い点'].to_csv('text/n_comment.txt', index=False, header=False, sep='\t', quoting=csv.QUOTE_MINIMAL)
        
        st.success("データが保存されました。")
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")

    cur.close()
    conn.close()
