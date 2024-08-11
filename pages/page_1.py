import streamlit as st
import sqlite3
import pandas as pd
from wordcloud import WordCloud
from matplotlib import pyplot as plt


with open("comment.txt", "r", encoding="utf-8")as f:
    text=f.read()
st.write(text)
if not text.strip():
    st.error("テキストが空です。")
else:
    wordcloud = WordCloud(background_color="white").generate(text)

plt.imshow(wordcloud)