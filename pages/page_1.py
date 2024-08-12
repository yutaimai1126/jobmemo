import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import japanize_matplotlib
# from matplotlib import font_manager as fm
import re
import unicodedata
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud

# フォントを追加
# prop = fm.FontProperties(fname='C:/WINDOWS/Fonts/BIZ-UDMinchoM.ttc')
# plt.rcParams['font.family'] = prop.get_name()

# 良い点

# テキストファイルを読み込み、不要な文字や記号を削除
with open('p_comment.txt', encoding='utf-8') as f:
    text = f.read().replace('\n', '').replace(' ', '')

text = re.sub('\u3000', '', text)
text = re.sub('・', '', text)
text = re.sub('「', '', text)
text = re.sub('」', '', text)
text = re.sub('（', '', text)
text = re.sub('）', '', text)
text = re.sub('\n', ' ', text)
text = re.sub('\\n', '', text)
text = re.sub('\\n', ' ', text)

# Unicode正規化
text_sample = unicodedata.normalize('NFKC', text)
print('UNICODEの正規化後：{}'.format(text_sample))

# janomeを使った形態素解析
t = Tokenizer()
tokenized_text = t.tokenize(text)

words_list = []
for token in tokenized_text:
    tokenized_word = token.surface
    hinshi = token.part_of_speech.split(',')[0]
    hinshi2 = token.part_of_speech.split(',')[1]
    if hinshi == "名詞":
        if (hinshi2 != "数") and (hinshi2 != "代名詞") and (hinshi2 != "非自立"):
            words_list.append(tokenized_word)

words_wakachi = " ".join(words_list)
print(words_wakachi)

# WordCloudの生成と表示
font = 'ipag.ttf'
stopWords = ['ので', 'そう', 'から', 'ため', '活', '的', '内', '感', '度', 'タイム']

# WordCloudを作成
word_cloud = WordCloud(font_path=font, width=1500, height=900,
                      stopwords=set(stopWords), min_font_size=5,
                      collocations=False, background_color='white',
                      max_words=400).generate(words_wakachi)

# 新しいfigureとaxesを作成
fig, ax = plt.subplots(figsize=(9, 6))
ax.set_title('ポジティブ軸',fontsize=18)
ax.imshow(word_cloud, interpolation='bilinear')
ax.tick_params(labelbottom=False, labelleft=False)
ax.set_xticks([])
ax.set_yticks([])

# Streamlitでの表示
st.pyplot(fig)


# 悪い点

# テキストファイルを読み込み、不要な文字や記号を削除
with open('n_comment.txt', encoding='utf-8') as f:
    text = f.read().replace('\n', '').replace(' ', '')

text = re.sub('\u3000', '', text)
text = re.sub('・', '', text)
text = re.sub('「', '', text)
text = re.sub('」', '', text)
text = re.sub('（', '', text)
text = re.sub('）', '', text)
text = re.sub('\n', ' ', text)
text = re.sub('\\n', '', text)
text = re.sub('\\n', ' ', text)

# Unicode正規化
text_sample = unicodedata.normalize('NFKC', text)
print('UNICODEの正規化後：{}'.format(text_sample))

# janomeを使った形態素解析
t = Tokenizer()
tokenized_text = t.tokenize(text)

words_list = []
for token in tokenized_text:
    tokenized_word = token.surface
    hinshi = token.part_of_speech.split(',')[0]
    hinshi2 = token.part_of_speech.split(',')[1]
    if hinshi == "名詞":
        if (hinshi2 != "数") and (hinshi2 != "代名詞") and (hinshi2 != "非自立"):
            words_list.append(tokenized_word)

words_wakachi = " ".join(words_list)
print(words_wakachi)

# WordCloudの生成と表示
font = 'ipag.ttf'
stopWords = ['ので', 'そう', 'から', 'ため', '自分', '投資', '運用']

# WordCloudを作成
word_cloud = WordCloud(font_path=font, width=1500, height=900,
                      stopwords=set(stopWords), min_font_size=5,
                      collocations=False, background_color='white',
                      max_words=400).generate(words_wakachi)

# 新しいfigureとaxesを作成
fig, ax = plt.subplots(figsize=(9, 6))
ax.set_title('ネガティブ軸',fontsize=18)
ax.imshow(word_cloud, interpolation='bilinear')
ax.tick_params(labelbottom=False, labelleft=False)
ax.set_xticks([])
ax.set_yticks([])

# Streamlitでの表示
st.pyplot(fig)