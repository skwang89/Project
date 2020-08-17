# pywork16.py start
# <<강의 복습 9. 시작>>


# wordcloud
import numpy as np
import matplotlib.pyplot as plt
import platform
from wordclous import wordCloud, STOPWORDS
from PIL import Image

# data1/alice.txt  파일 읽어오기
text = open('data1/alice.txt', 'r').read()
print(text)

# data1/alice_mast.png 이미지 읽어오기
alice_mask = np.array(Image.open('data1.alice_mask.png'))
# print(alice_mask)

# 제오할 단어를 등록
stopwords = set(STOPWORDS)
stopwords.add('said')

# wordcloud 생성
wc = WordCloud(
                backg
)






















all = [var for var in globals() if var[0] != "-"]
for var in all:
    del globals()[var]
del(all)
del(var)

import sys
sys.modules[__name__].__dict__.clear()


# <<강의 복습 9. 끝>>
# pywork16.py end