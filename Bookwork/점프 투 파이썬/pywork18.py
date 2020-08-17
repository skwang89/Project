# pywork18.py start
# <<강의 복습 11. 시작>>


#  지도 활용하기
#  google API를 이용한 위치정보(위도, 경도) 구하기
#  Folium 라이브러리를 이용한 지도 만들기






all = [var for var in globals() if var[0] != "-"]
for var in all:
    del globals()[var]
del(all)
del(var)

import sys
sys.modules[__name__].__dict__.clear()


# <<강의 복습 11. 끝>>
# pywork18.py end