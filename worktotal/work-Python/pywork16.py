# pywork16.py start
# <<강의 복습 9. 시작>>


# wordcloud
# 앨리스 워드클라우드
import numpy as np
import matplotlib.pyplot as plt
import platform
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

# data1/alice.txt  파일 읽어오기
text = open('data1/alice.txt', 'r').read()
print(text)

# data1/alice_mast.png 이미지 읽어오기
alice_mask = np.array(Image.open('data1/alice_mask.png'))
# print(alice_mask)

# 제오할 단어를 등록
stopwords = set(STOPWORDS)
# stopwords.add('a')
# stopwords.add('the')
# stopwords.add('and')
stopwords.add('said')
# stopwords.add('said Alice')

# wordcloud 생성
wc = WordCloud(
               background_color='yellow',
               max_words=200,
               mask=alice_mask,
               stopwords=stopwords).generate(text)
print(wc.words_)              # 빈도수 출력
wc.to_file('alice.png')       # alice.png 파일로 저장

# 앨리스 이미지와 wordcloud를 겹쳐서 출력
plt.figure(figsize=(8, 8))
plt.imshow(wc)
plt.axis('off')
plt.show()

# 스타워즈 워드클라우드
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

# data1/a_new_hope.txt 파일 읽기
text = open('data1/a_new_hope.txt', 'r').read()
print(text)

# data1/stormtrooper_mask.png 파일 읽기
mask = np.array(Image.open('data1/stormtrooper_mask.png'))
# print(mask)

# stopword 등록
stopwords = set(STOPWORDS)
stopwords.add('int')
stopwords.add('ext')

# 워드클라우드 생성
wc = WordCloud(
            # background_color='white',
            max_words=500,
            mask=mask,
            stopwords=stopwords).generate(text)
print(wc.words_)                    # 단어의 빈도수
# print(type(wc.words_))
# for key in wc.words_.keys():
#     print(key, ":", wc.words_[key])
wc.to_file('starwars.png')

plt.figure(figsize=(8,8))           # 그래프의 크기설정
plt.imshow(wc)                      # wordcloud를 그래프에 부착
plt.axis('off')                     # x, y축을 나타나지 않도록 설정
plt.show()

# "육아휴직 법안 제 18098990호" 에 대한 wordcloud를 이용한 시각화
import nltk
from konlpy.corpus import kobill

doc_ko = kobill.open('1809890.txt').read()
# doc_ko = open(data1/hong.txt', 'r', encoding='utf8').read()
# doc_ko = open('contents_text.txt', 'r', encoding='utf8').read()
print(doc_ko)

# Okt 분석기로 명사 추출
from konlpy.tag import Okt

t = Okt()
tokens_ko = t.nouns(doc_ko)
print(tokens_ko)

ko = nltk.Text(tokens_ko)
#                                     # contents_text.txt 파일에서
# print(len(ko.tokens))               # 수집된 단어의 총갯수 : 253669
# print(len(set(ko.tokens)))          # 중복을 제외한 단어 갯수 : 9679
                                    # 1809890.txt 파일에서
print(len(ko.tokens))               # 수집된 단어의 총갯수 : 735
print(len(set(ko.tokens)))          # 중복을 제외한 단어 갯수 : 250

# stopwords로 등록한 단어를 그래프로 확인
import matplotlib.pyplot as plt
import matplotlib

# '맑은고딕'으로 한글 글꼴 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# 단어들의 빈도수를 그래프로 출력
plt.figure(figsize=(12, 6))
ko.plot(50)                 # 빈도수가 높은 단어 50개를 그래프에 출력
plt.show()

# stopword에 등록
# 1809890.txt
stop_words = ['.', '(', ')', ',', "'", '%', '-', 'X', ').', '×','의','자',
              '에','안','번','호','을','이','다','만','로','가','를','액',
              '세','제','위','월','수','중','것','표','명','및','법','생',
              '략','정','항','함']
# contents_text.txt
stop_words = ['.', '(', ')', ',', "'", '%', '-', 'X', ').', '×','의',
              '자','에','안','번', '호','을','이','다','만','로','가','를',
              '액','세','제','위','월','수','중','것','표','명','및','생','략',
              '정','법','함','항','저','것','분','그','답','삶','그','또','앞','안',
              '등','확','재','고','말','씨','전']

ko = [each_word for each_word in ko if each_word not in stop_words]

# stopword에서 제외 되었는지 그래프로 확인
ko = nltk.Text(ko)
plt.figure(figsize=(12,6))
ko.plot(50)                     # 빈도수가 높은 단어 50개를 그래프에 출력
plt.show()

# wordcloud 그리기
data = ko.vocab().most_common(150)      # wordcloud로 출력할 단어의 갯수 150개

from wordcloud import WordCloud

wc = WordCloud(font_path='c:/windows/Fonts/malgun.ttf',
               relative_scaling=0.1,
               background_color='white').generate_from_frequencies(dict(data))
print(wc.words_)             # 빈도수 출력
wc.to_file('words.png')      # words.png 파일로 저장

plt.figure(figsize=(12, 8))
plt.imshow(wc)
plt.axis('off')
plt.show()


# <<강의 복습 9. 끝>>
# pywork16.py end