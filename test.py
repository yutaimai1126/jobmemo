# MIcrosoft Visual Studio をインストール
# https://visualstudio.microsoft.com/ja/vs/community/

import re

with open('comment.txt', encoding='utf-8') as f:
    text = f.read().replace('\n', '').replace(' ', '')
print(text)

#変数text中に格納されたアンケート内の不要な文字や記号を削除する。
#re.subで正規表現を使った文字列の削除。
text = re.sub('\u3000', '', text)
text = re.sub('・', '', text)
text = re.sub('「', '', text)
text = re.sub('」', '', text)
text = re.sub('（', '', text)
text = re.sub('）', '', text)
#re.subで正規表現を使った文字列の半角空白への置換。
text = re.sub('\n', ' ', text)
text = re.sub('\\n', '', text)
text = re.sub('\\n', ' ', text)

#ユニコード正規化
import unicodedata

text_sample = unicodedata.normalize('NFKC', text)
print('UNICODEの正規化後：{}'.format(text_sample))

# janomeを使った形態素解析
from janome.tokenizer import Tokenizer

#対象のテキストをtokenizeする
t = Tokenizer()
tokenized_text = t.tokenize(text)

words_list=[]
#tokenizeされたテキストをfor文を使ってhinshiとhinshi2に格納する。
for token in tokenized_text:
    tokenized_word = token.surface
    hinshi = token.part_of_speech.split(',')[0]
    hinshi2 = token.part_of_speech.split(',')[1]
    #抜き出す品詞を指定する
    if hinshi == "名詞":
        if (hinshi2 != "数") and (hinshi2 != "代名詞") and (hinshi2 != "非自立"):
            words_list.append(tokenized_word)

words_wakachi=" ".join(words_list)
print(words_wakachi)

# ワードクラウドによる頻出単語の可視化
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#日本語のフォントを指定する
font = 'ipag.ttf'

#意味なさそうな単語（ストップワード）を除去する。
stopWords = ['ので','そう','から','ため','自分', '投資','運用']

#WordCloudを表示
word_cloud = WordCloud(font_path=font, width=1500, height=900,
                        stopwords=set(stopWords),min_font_size=5, 
                        collocations=False, background_color='white', 
                        max_words=400).generate(words_wakachi)
figure = plt.figure(figsize=(15,10))
plt.imshow(word_cloud)
plt.tick_params(labelbottom=False, labelleft=False)
plt.xticks([])
plt.yticks([])
plt.show()
