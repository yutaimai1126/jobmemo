import streamlit as st
import sqlite3
import pandas as pd
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import japanize_matplotlib


# テキストファイルを読み込み
with open("comment.txt", "r", encoding="utf-8") as f:
    text = f.read()

# テキストの表示
st.write(text)

# テキストが空でないかチェック
if not text.strip():
    st.error("テキストが空です。")
else:
    # WordCloudを生成
    wordcloud = WordCloud(background_color="white").generate(text)

    # WordCloudを表示
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    
    # Streamlitでの表示
    st.pyplot(plt)
    plt.imshow(wordcloud)

