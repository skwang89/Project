# pywork17.py start
# <<강의 복습 10. 시작>>


# 데이터 시각화 방법
#  matplotlib 그래프
#  pandas 그래프
#  seaborn 그래프

# matplot 그래프

# matplotlib 모듈
# matplotlib 모듈은 파이썬에서 데이터를 효과적으로 시각화하기 위해서
# 만든 라이버러리 이다.
# matplotlib은 MATLAB(과학 및 공학 연산을 위한 소프트웨어)의 시각화
# 기능을 모델링해서 만들어졌다.
# matplotlib 모듈을 이용하면 2차원 선 그래프(line), 산점도(scatter),
# 막대그래프(bar chart), 히스토그램(histogram), 파이 그래프(pie chart)
# 등을 그릴 수 있다.
# matplotlib 모듈은 아나콘다가 설치 될 때 같이 설치 되므로, 따로 설치
# 하지 않아도 된다.

# 선그래프
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()

# x, y축 라벨 설정
plt.plot([0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

# x, y축 한글 라벨 설정
import matplotlib.pyplot as plt
import matplotlib
x = [1,2,3,4,5]
y = [1,2,3,4,5]

# 한글 라벨 설정: '맑은 고딕' 으로 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# matplotlib.rcParams['font.family'] = '맑은고딕'
plt.xlabel('x축')
plt.ylabel('y축')
plt.plot(x, y)
plt.show()

# 선의 색깔 설정
x = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]
plt.figure(figsize=(8, 5))      # 그래프의 크기
plt.plot(x,y, color='green')    # 선의 색깔 : green
plt.show()

# 선의 색깔, 모양 설정
x = [1,2,3,4,5]
y = [1,2,3,4,5]
# plt.plot(x, y, 'r-')          # r-, g-, b-  : 선그래프
# plt.plot(x, y, 'ro')          # ro, go, bo  : o 표시
# plt.plot(x, y, 'rv')          # rv, gv, bv  : v 표시
plt.plot(x, y, 'r>')            # r>, g>, b>  : > 표시
plt.show()

# 점선 그래프 그리기
# 점선 : plot()함수에 linestyle='dashed' 추가
x = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]
plt.figure(figsize=(8,5))
plt.plot(x, y, color='green', linestyle='dashed')
plt.show()

# 점선 그래프 : linestyle = 'dashed'
# 마커 표시  : marker = 'o'
#             marker = 'v'
x = [0,1,2,3,4,5,6]
y = [1,4,5,8,9,5,3]
plt.figure(figsize=(8,5))
plt.plot(x, y, color='green', linestyle='dashed', marker='v')
plt.show()

# 점선 그래프 : linestyle = 'dashed'
# 마커 표시 : marker = 'o'
# 마커 색깔 : markerfacecolor = 'red'
# 마커 크기 : makersize = 12
x = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]
plt.figure(figsize=(8, 5))
plt.plot(x, y, color='green',               # 선의 색깔
               linestyle = 'dashed',        # 점선
               marker = 'o',                # o 표시
               markerfacecolor = 'red',     # 마커의 색깔
               markersize = 12 )            # 마커의 크기
plt.show()

# 산점도
# 산점도는 2개의 요소로 이루어진 데이터 집합의 관계 (예를들면, 키와 몸무게
# 와의 관계, 공부시간과 시험점수와의 관계, 기온과 아이스크림 판매량과의
# 관계)를 시각화하는데 유용하다.
# 산점도를 그리기 위해서는 plot()함수 대신에 scatter()함수 사용함
#  산점도 형식
# plt.scatter( x, y [, s = size, c = colors, marker = ‘marker_string ‘,
# alpha = alpha_f ] )
# s : 마커의 크기
# c : 마커의 색깔
# marker : 마커 모양
# alpha : 투명도 : 0(완전 투명) ~ 1(완전 불투명)
# 옵션을 지정하지 않으면, 기본값 (s=40, c=‘b’, marker=‘o’, alpha=1 )으로 지정

# 산점도
# plot()함수 대신에 scatter()함수 사용함
x = [0,1,2,3,4,5,6,7,8,9]
y = [9,8,7,9,8,3,2,4,3,4]
plt.figure(figsize=(8,5))
plt.scatter(x,y)
plt.show()

# marker 의 모양 변경 : scatter()함수에 marker = '>' 추가
# marker의 크기 변경 : s = 50
# x의 값에 따라 y축 값의 색상을 바꾸는 colormap 추가
# scatter()함수에 c=colormap
# plt.colorbar()
x = [0,1,2,3,4,5,6,7,8,9]
y = [9,8,7,9,8,3,2,4,3,4]
plt.figure(figsize=(8, 5))
plt.scatter(x, y, s=60, c=x, marker='>')
plt.colorbar()
plt.show()

# 산점도 : 각 도시의 인구밀도를 산점도로 출력
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 맑은고딕으로 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

city = ['서울', '인천', '대전', '대구', '울산', '부산', '광주']

# 위도, 경도
lat = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]
lon = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85]

# 인구밀도(명/km^2) : 2017년 통계청 자료
pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995]

size = np.array(pop_den) * 0.3              # 마커의 크기
color = ['r','g','b','c','m','k','y']       # 마커의 색깔

plt.scatter(lon, lat, s=size, c=color, alpha=0.5)
# scatter() 인자 s: 도형의 크기, c: 도형의 색상, alpha: 색상의 투명도
plt.xlabel('경도(longitude)')
plt.ylabel('위도(latitude)')
plt.title('지역별 인구밀도(2017년)')

# 도시명 출력
for x, y, name in zip(lon, lat, city):
    plt.text(x, y,name)
plt.show()

# 막대 그래프
# 막대그래프는 값을 막대의 높이를 나타내므로 여러 항목의 수량이 많고 적음을
# 한눈에 파악할 수 있다. 따라서 여러 항목의 데이터를 서로 비교할 때 주로
# 이용한다.

#  막대 그래프 형식
# plt.bar( x, height [, width = width_f, color = colors, tick_label = tick_labels,
# align = ‘center’ (기본) , label = labels ] )
# x : height와 길이가 일치하는 데이터로 x축에 표시될 위치를 지정
# height : 시각화 하고자 하는 막대 그래프 데이터
# width : [0, 1]사이의 실수를 지정해 막대의 폭을 조절
# width 옵션을 입력하지 않으면 기본값인 0.8이 입력
# color : fmt옵션의 컬러지정 약어로 막대그래프의 색을 지정
# tick_label : 막대 그래프 x축의 tick 라벨 이름을 지정 (기본값은 숫자 라벨)
# align : 막대 그래프의 위치를 가운데로 할지(center) 한쪽으로 치우치게 할지(edge)
# 설정 (기본값은 center )
# label : 범례에 사용될 문자열을 지정
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# '맑은 고딕' 으로 한글 글꼴 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

member_ID = ['m_01', 'm_02', 'm_03', 'm_04']        # 회원 ID
before_ex = [27, 25, 40, 33]                        # 운동전 윗몸일으키기 횟수
after_ex = [30, 38, 42, 37]                         # 운동후 윗몸일으키기 횟수

# 1. 기본값으로 막대 그래프 출력
n_data = len(member_ID)                   # 4
index = np.arange(n_data)                 # 0 ~ 3
plt.bar(index, before_ex)
plt.show()
# 2. tick_label 설정
plt.bar(index, before_ex, tick_label = member_ID)
plt.show()
# 3. 막대 그래프의 색깔 설정
colors = ['r', 'g', 'b', 'm']
plt.bar(index, before_ex, color=colors, tick_label=member_ID)
plt.show()
# 4. 막대 그래프의 폭(width) 설정 - (기본값: 0.8)
plt.bar(index, before_ex, width=0.6, tick_label=member_ID)
plt.show()
# 5. 수평 막대 그래프: barh()
plt.barh(index, before_ex, color=colors, tick_label=member_ID)
plt.show()
# 6. 최종 막대 그래프 출력
plt.bar(index, before_ex, color='c', align='edge', width=0.4, label='before')
plt.bar(index+0.4, after_ex, color='m', align='edge', width=0.4, label='after')
plt.xticks(index+0.4, member_ID)
plt.legend()
plt.xlabel('회원ID')
plt.ylabel('윗몸 일으키기 횟수')
plt.title('운동 전후의 근지구력 변화 비교')
plt.show()

# 히스토그램
# 히스토그램(histogram)은 데이터를 정해진 간격으로 나눈 후 그 간격 안에
# 들어간 데이터 개수를 막대로 표시한 그래프로, 데이터가 어떤 분포를 갖는지를
# 볼 때 주로 사용한다.
# 즉, 히스토그램은 도수 분포표를 막대 그래프로 시각화한 것이다.
# 히스토그램은 주로 통계 분야에서 데이터가 어떻게 분포하는지 알아볼 때 많이
# 사용한다.
#  히스토그램 형식
# plt.hist ( x [,bins = bins_n 혹은 ‘auto’ ] )
# x : 변량 데이터
# bins : 계급의 개수 ( 기본값은 10 )
# bins = ‘auto’ 가 입력되면, x에 맞게 자동으로 bins에 값이 들어간다.

# 도수 분포표의 용어
#  변량(variate) : 자료를 측정해 숫자로 표시한 것
# ex) 점수, 키, 몸무게, 판매량, 시간 등
#  계급(class) : 변량을 정해진 간격으로 나눈 구간
# ex) 시험점수를 60~70, 70~80, 80~90, 90~100점 구간으로 나눔
#  계급의 간격(class width) : 계급을 나눈 크기 (기본값은 10)
#  도수(frequency) : 나눠진 계급에 속하는 변량의 수
# ex) 각 계급에서 발생한 수
#  도수 분포표(frequency distribution table) : 계급에 도수를 표시한 것

# 히스토그램
# 25명 학생들의 수학점수를 히스토그램으로 시각화
import matplotlib.pyplot as plt
import matplotlib

# '맑은 고딕' 글꼴 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# 25명 학생들의 수학성적
math = [76, 82, 84, 83, 90, 86, 85, 92, 72, 71, 100, 87, 81, 76, 94, 78,
        81, 60, 79, 69, 74, 87, 82, 68, 79]

# 계급의 갯수: 10
plt.hist(math)
plt.show()

# 계급의 간격:5, 계급의 갯수: 8
plt.hist(math, bins=8)
plt.xlabel('시험점수')
plt.ylabel('도수(frequency)')
plt.title('수학 시험의 히스토그램')
plt.grid()
plt.show()

# 파이 그래프
# 파이(pie) 그래프는 원안에 데이터의 각 항목이 차지하는 비율만큼 부채꼴의
# 크기를 갖는 영역으로 이루어진 그래프이다.
# 파이 그래프는 전체 데이터에서 각 항목이 차지한 비율을 비교할 때 많이
# 사용한다.

# 파이 그래프 형식
# plt.pie(x [, labels = label_seq , #부채꼴에 출력되는 문자열
# autopct = ‘비율 표시 형식(ex: %.1f)’ ,
# shadow = False(기본) 혹은 True , # 그림자효과
# explode = explode_seq , # 부채꼴부분이 원에서 돌출
# counterclock = True(기본) 혹은 False , #부채꼴이 그려지는 순서
# #기본값은 반시계방향(True)
# startangle = 각도 (기본은 0 ) #처음 부채꼴부분이 그려지는
# # 각도(기본값은 0)

# pie 그래프
import matplotlib.pyplot as plt
import matplotlib

#'맑은 고딕'  한글 글꼴 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

fruit = ['사과','바나나','딸기','오렌지','포도']
result = [7, 6, 3, 2, 2]

# 1. 파이 그래프
plt.pie(result)
plt.show()
# 2. 파이 그래프의 크기 설정
plt.figure(figsize=(7, 7))
plt.pie(result)
plt.show()
# 3. 라벨과 비율 설정
plt.figure(figsize=(7, 7))
plt.pie(result, labels=fruit, autopct='%.1f%%')
plt.show()
# 4. 90도에서 시작해서 시계방향으로 설정
plt.figure(figsize=(7, 7))
plt.pie(result, labels=fruit, autopct='%.1f%%',
                startangle=90, counterclock=False)
plt.show()
# 5. 그림자 효과를 추가하고, 사과 부채꼴만 강조
plt.figure(figsize=(7, 7))
plt.pie(result, labels=fruit, autopct='%.1f%%',
                startangle=90, counterclock=False,
                explode=(0.1,0,0,0,0), shadow=True)
plt.show()

# pandas 그래프

# pandas 그래프 구조
# pandas의 Series나 DataFrame으로 생성한 데이터가 있을 경우에는
# pandas 모듈로 그래프를 그릴 수 있다.
# Series_data . plot( [ kind = ‘ graph_kind ’ ] [ ,option ] )
# DataFrame_data . plot( [ x=label 혹은 potion , y=label 혹은 potions ,]
# [ kind = ‘ graph_kind ‘ ] [ , option ] )
# ex)
# Series_data . plot ( kind = ‘ line ‘ ) : 선그래프
# kind 옵션을 생략하면 기본적으로 선 그래프가 그려진다.
























all = [var for var in globals() if var[0] != "-"]
for var in all:
    del globals()[var]
del(all)
del(var)

import sys
sys.modules[__name__].__dict__.clear()


# <<강의 복습 10. 끝>>
# pywork17.py end