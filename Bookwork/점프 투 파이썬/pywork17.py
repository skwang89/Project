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

# pandas 그래프 종류
# kind 옵션    의 미
# line        선 그래프(기본)
# bar         수직 막대 그래프
# barh        수평 막대 그래프
# scatter     산점도(DataFrame 데이터만 가능)
# hist        히스토그램
# pie         파이 그래프

# pandas 그래프 그리기
# DataFrame_data . plot( kind = ‘ line ’ )
# DataFrame_data . plot . line()
# DataFrame_data . plot( kind = ‘ bar ’ )
# DataFrame_data . plot . bar()
# DataFrame_data . plot( kind = ‘ pie ’ )
# DataFrame_data . plot . pie()
# DataFrame_data . plot . hist()
# DataFrame_data . plot . scatter()

# pandas 선그래프
import pandas as pd
import matplotlib.pyplot as plt

# Series 생성
s = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(s)

# 선그래프
# s.plot(kind='line')
s.plot.line()
plt.show()

# Series 생성
s = pd.Series([1,2,3,4,5,6,7,8,9,10],
              index=pd.date_range('2020-01-01', periods=10))
print(s)
# 2020-01-01     1
# 2020-01-02     2
# 2020-01-03     3
# 2020-01-04     4
# 2020-01-05     5
# 2020-01-06     6
# 2020-01-07     7
# 2020-01-08     8
# 2020-01-09     9
# 2020-01-10    10

# 선 그래프
# s.plot()
s.plot.line()
plt.show()
# 격자 모양 추가
s.plot(grid=True)
plt.show()

# pandas 막대그래프
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 10행 3열 난수 발생
data_set = np.random.rand(10, 3)
print(data_set)
# 데이터 프레임 생성
df = pd.DataFrame(data_set, columns=['A', 'B', 'C'])
print(df)
# 수직 막대 그래프
# df.plot().bar()
df.plot(kind='bar')
plt.show()
# 수평 막대 그래프
df.plot(kind='barh')
plt.show()
# 영역 그래프
df.plot(kind='area', stacked=False)
plt.show()

# 학점별 학생수 막대 그래프
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 맑은 고딕 글꼴 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# 데이터셋
grade_num = [5, 14, 12, 3]
students = ['A','B','C','D']
# 데이터프레임 생성
df_grade = pd.DataFrame(grade_num, index=students, columns=['Student'] )
print(df_grade)
#       Student
# A        5
# B       14
# C       12
# D        3
bar = df_grade.plot.bar(grid=True)
bar.set_xlabel('학점')
bar.set_ylabel('학생수')
bar.set_title('학점별 학생수 막대 그래프')
plt.show()

# pandas로 산점도
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# '맑은 고딕' 글꼴 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

temperature = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1]
ice_cream_sales = [236500, 357500, 203500, 365200, 446600, 574200,
                   453200, 675400, 598400, 463100]
# 데이터 프레임 생성
dict_data = {'기온': temperature, '아이스크림 판매량': ice_cream_sales}
df = pd.DataFrame(dict_data)
print(df)
#    기온   아이스크림 판매량
# 0  25.2     236500
# 1  27.4     357500
# 2  22.9     203500
# 3  26.2     365200
# 4  29.5     446600
# 5  33.1     574200
# 6  30.4     453200
# 7  36.1     675400
# 8  34.4     598400
# 9  29.1     463100

# 산점도
df.plot.scatter(x='기온', y='아이스크림 판매량', grid=True,
                title='최고 기온과 아이스크림 판매량')
plt.show()

# pandas로 히스토그램
# 25명 학생들의 수학점수를 히스토그램으로 시각화
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# '맑은 고딕' 글꼴 설정
matplotlib.rcParams['font.family']='Malgun Gothic'
# 25명 학생들의 수학점수
math = [76,82,84,83,90,86,85,92,72,71,100,87,81,
        76,94,78,81,60,79,69,74,87,82,68,79]
# 데이터 프레임 생성
df = pd.DataFrame(math, columns=['Student'])
print(df)
#       Student
# 0        76
# 1        82
# 2        84
# 3        83
#   .....
# 21       87
# 22       82
# 23       68
# 24       79

# 히스토그램 생성 : 계급의 갯수 : (기본값:10)
hist = df.plot.hist(bins=8, grid='True')
hist.set_xlabel('시험점수')
hist.set_ylabel('도수(frequency)')
hist.set_title('수학 시험 히스토그램')
plt.show()

# pandas로 pie그래프 그리기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 난수 5개 생성
data = np.random.rand(5)
print(data)
# Series 생성
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
# pie 그래프
s.plot(kind='pie', autopct='%.2f%%', figsize=(7,7))
plt.show()

# pandas로 pie 그래프 그리기
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# '맑은 고딕' 한글 글꼴 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7, 6, 3, 2, 2]

df = pd.Series(result, index=fruit, name='선택한 학생수')
print(df)
df.plot.pie()
plt.show()

pie = df.plot.pie(figsize=(7, 7),               # pie그래프의 크기
                  autopct='%.1f%%',             # 비율 출력(소숫점 1째자리)
                  startangle = 90,              # 시작 위치
                  counterclock = False,         # 시계방향
                  explode = (0.1,0,0,0,0),      # 부채꼴을 돌출
                  shadow = True,                # 그림자 효과
                  table = True )                # 테이블 출력
pie.set_ylabel('')                              # y축 라벨 제거
pie.set_title('과일 선호도 조사 결과')            # 메인 타이틀
# pie 그래프를 이미지 파일로 저장
plt.savefig('fruit.png', dpi=200)
plt.show()

# # seaborn 그래프
# seaborn 모듈
# seaborn은 matplotlib의 기능과 스타일을 확장한 파이썬 시각화 도구의고급 버전이다.
# 그리고 matplotlib으로 표현하기 힘든, 좀더 정교한 그래프를 지원하고 있다.
#  seaborn으로 표현 가능한 그래프
#  산점도
#  히스토그램
#  커널 밀도 그래프
#  히트맵
#  막대 그래프
#  빈도 그래프
#  박스 플롯
#  바이올린 그래프
#  조인트 그래프

# Titanic Dataset
# seaborn 라이브러리에서 제공되는 ‘titanic’ 데이터셋을 가져와서 다양한
# 그래프로 출력 해보자.
# titanic = sns.load_dataset(‘titanic’)
# titanic 데이터셋에는 탑승객 891명의 정보가 담겨져 있다.
# index : 891 ( 0 ~ 890 )
# columns : 15 columns

# seaborn 그래프 그리기
import pandas as pd
import seaborn as sns

# titanic 데이터 불러오기
titanic = sns.load_dataset('titanic')
print(titanic)                  # [891 rows x 15 columns]
# 출력할 열의 개수 늘리기 : 15개 컬럼 출력
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 891)
print(titanic)

# with open('titanic.txt', 'w') as f:       # txt파일로 저장
#     f.write(str(titanic))
# titanic.to_excel('titanic.xlsx')          # excel파일로 저장

# 데이터 정보 구하기
print(titanic.head())           # 앞에서 5개의 데이터
print(titanic.head(10))         # 앞에서 10개의 데이터
print(titanic.info())           # 데이터의 자료형 확인

# 회귀선이 있는 산점도
# seaborn 모듈로 산점도를 그리기 위해서는 regplot() 함수를 이용한다.
# sns.regplot ( x = ‘age’ ,             # x축 변수
#               y = ‘fare’ ,            # y축 변수
#               data = titanic ,        # 데이터
#               ax = ax1 ,              # 1번째 그래프
#               fit_reg = True )        # 회귀선 표시

# 회귀선이 있는 산점도
import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')
print(titanic)              # [891 rows x 15 columns]
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')
# 그래프 크기, 서브 플롯 설정
fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(1,2,1)        # 1행 2열 - 1번째 그래프
ax2 = fig.add_subplot(1,2,2)        # 1행 2열 - 2번째 그래프
# 산점도 그래프 - 회귀선 표시
sns.regplot(x = 'age',              # x축
            y = 'fare',             # y축
            data=titanic,           # 데이터
            ax = ax1,               # 1번째 그래프
            fit_reg=True)           # 회귀선 표시(기본값)
# 산점도 그래프 - 회귀선  미표시
sns.regplot(x = 'age',              # x축
            y = 'fare',             # y축
            data=titanic,           # 데이터
            ax = ax2,               # 2번째 그래프
            fit_reg=False)          # 회귀선 미표시
plt.show()

# 범주형 데이터의 산점도
# 범주형 변수( class )에 들어 있는 각 범주별 데이터의 분포를 시각화하는
# 방법이다. 범주형 데이터의 산점도를 그릴때에는 stripplot() 함수와 swarmplot()
# 함수를 사용한다. swarmplot()함수는 데이터의 분산까지 고려하고, 데이터 포인트가
# 서로 중복되지 않도록 그래프를 그린다.
# 즉, 데이터가 퍼져있는 정도를 입체적으로 볼 수 있다.

# 이산형 변수의 분포 - 데이터 분산 미고려
# sns.stripplot(x="class",        # x축 변수
#               y="age",          # y축 변수
#               data=titanic,     # 데이터셋 - 데이터프레임
#               ax=ax1)           # axe 객체 - 1번째 그래프

# 이산형 변수의 분포 - 데이터 분산 고려 (중복 X)
# sns.swarmplot(x="class",        # x축 변수
#               y="age",          # y축 변수
#               data=titanic,     # 데이터셋 - 데이터프레임
#               ax=ax2)           # axe 객체 - 2번째 그래프

# 범주형 데이터의 산점도
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic)          # [891 rows x 15 columns]
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')
# 그래프 크기, 서브플롯 설정
fig = plt.figure(figsize=(12, 5))       # 그래프의 크기 설정
ax1 = fig.add_subplot(1,2,1)            # 1행 2열 - 1번째 그래프
ax2 = fig.add_subplot(1,2,2)            # 1행 2열 - 2번째 그래프
# 데이터 분산 미고려
sns.stripplot(x = 'class',              # x축 : class
              y = 'age',                # y축
              data=titanic,             # 데이터
              ax = ax1)                 # 1번째 그래프
# 데이터 분산 고려
sns.swarmplot(x = 'class',              # x축 : class
              y = 'age',                # y축
              data=titanic,             # 데이터
              ax = ax2)                 # 2번째 그래프
# 그래프 제목 출력
ax1.set_title('stripplot')
ax2.set_title('swarmplot')
plt.show()

# 히스토그램과 커널 밀도 함수
# 하나의 변수 데이터의 분포를 확인할 때, 주로 히스토그램과 커널 밀도 함수로
# 시각화하며, seaborn 모듈로 히스토그램과 커널 밀도 함수를 그리기 위해서는
# distplot() 함수를 이용한다.
# 커널 밀도 함수는 그래프와 x축 사이의 면적이 1이 되도록 그리는 밀도 분포함수이다.

# 기본값 : 히스토그램 + 커널밀도함수
sns.distplot(titanic['fare'], ax=ax1)
# hist=False : 커널밀도함수
sns.distplot(titanic['fare'], hist=False, ax=ax2)
# kde=False : 히스토그램
sns.distplot(titanic['fare'], kde=False, ax=ax3)

# 히스토그램과 커널 밀도 함수
# 커널 밀도 함수는 그래프와 x축 사이의 면적이 1이 되도록 그리는
# 밀도 분포함수이다
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic)              # [891 rows x 15 columns]

# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')
# 그래프 크기, 서브 플롯 설정
fig = plt.figure(figsize=(12, 5))           # 그래프의 크기 설정
ax1 = fig.add_subplot(1,3,1)                # 1행 3열 - 1번째 그래프
ax2 = fig.add_subplot(1,3,2)                # 1행 3열 - 2번째 그래프
ax3 = fig.add_subplot(1,3,3)                # 1행 3열 - 3번째 그래프
# 히스토그램 + 커널밀도 함수
sns.distplot(titanic['fare'], ax=ax1)
# hist=False : 커널밀도 함수
sns.distplot(titanic['fare'], ax=ax2, hist=False)
# kde=False : 히스토그램
sns.distplot(titanic['fare'], ax=ax3, kde=False)
plt.show()

# 히트맵
# seaborn 라이브러리는 히트맵(heatmap)을 그리는 heatmap() 함수를 제공한다.
# 히트맵은 2개의 범주형 변수를 각각 x, y축에 놓고 데이터를 매트릭스 형태로 분류한다.
# 피벗테이블로 범주형 변수를 각각 행, 열로 재구분하여 데이터프레임을 생성함
# aggfunc='size' 옵션은 데이터 값의 크기를 기준으로 집계한다는 의미
table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')
# 히트맵 그리기
sns.heatmap(table,                  # 데이터프레임
            annot=True, fmt='d',    # 데이터 값 표시 여부, 정수형 포맷
            cmap='YlGnBu',          # 컬러 맵
            linewidth=.5,           # 구분 선
            cbar=False)             # 컬러 바 표시 여부

# 히트맵
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

# 피벗테이블로 범주형 변수를 각각 행, 열로 재구분하여 데이터프레임을 생성함
# aggfunc='size' 옵션은 데이터 값의 크기를 기준으로 집계한다는 의미
table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')
print(table)
# class   First  Second  Third
# sex
# female     94      76    144
# male      122     108    347

# 히트맵 그리기
sns.heatmap(table,
            annot=True, fmt='d',
            cmap = 'YlGnBu',
            linewidths= .5,
            cbar = True)
plt.show()

# 막대 그래프
# seaborn 라이브러리는 막대 그래프를 그리기 위해 barplot() 함수를 제공한다.
# x축, y축에 변수 할당
sns.barplot(x='sex', y='survived', data=titanic, ax=ax1)
# x축, y축에 변수 할당하고, hue 옵션 추가하여 누적 출력순으로 출력
sns.barplot(x='sex', y='survived', hue='class', data=titanic, ax=ax2)
# x축, y축에 변수 할당하고, dodge=False 옵션으로 1개의 막대 그래프로 출력
sns.barplot(x='sex', y='survived', hue='class', dodge=False, data=titanic, ax=ax3)

# 막대 그래프
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic)      # [891 rows x 15 columns]

# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')
# 그래프 크기 설정, 서브 플롯 설정
fig = plt.figure(figsize=(12, 5))           # 그래프의 크기
ax1 = fig.add_subplot(1, 3, 1)              # 1행 3열 - 1번째 그래프
ax2 = fig.add_subplot(1, 3, 2)              # 1행 3열 - 2번째 그래프
ax3 = fig.add_subplot(1, 3, 3)              # 1행 3열 - 3번째 그래프
# 막대 그래프 생성
sns.barplot(x='sex', y='survived', data=titanic, ax=ax1)
# hue='class'
sns.barplot(x='sex', y='survived', hue='class', data=titanic, ax=ax2)
# hue='class', dodge=False
sns.barplot(x='sex', y='survived', hue='class', dodge=False, data=titanic, ax=ax3)
# 차트 제목 표시
ax1.set_title('titanic class')
ax2.set_title('titanic class - who')
ax3.set_title('titanic class - who(stacked)')
plt.show()

# 빈도 막대그래프
# seaborn 라이브러리는 빈도 막대그래프를 그리기 위해 countplot() 함수를 제공한다.
# 기본값 : palette='Set1' 로 색상 설정
sns.countplot(x='class', palette='Set1', data=titanic, ax=ax1)
# hue 옵션에 'who' 추가 : who(man, woman, child) 각각 빈도 막대그래프 출력
sns.countplot(x='class', hue='who', palette='Set2', data=titanic, ax=ax2)
# dodge=False 옵션 추가 (축 방향으로 분리하지 않고 누적 그래프 출력)
sns.countplot(x='class', hue='who', palette='Set3', dodge=False, data=titanic, ax=ax3)

# 빈도 막대 그래프
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

titanic = sns.load_dataset('titanic')
print(titanic)

# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')
# 한글 글꼴 설정 : 테마 설정 아래에 있어야 적용됨
# matplotlib.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['font.family'] = 'Malgun Gothic'
# 그래프 크기 설정, 서브 플로 설정
fig = plt.figure(figsize=(12, 5))           # 그래프의 크기 설정
ax1 = fig.add_subplot(1, 3, 1)              # 1행 3열 - 1번째 그래프
ax2 = fig.add_subplot(1, 3, 2)              # 1행 3열 - 2번째 그래프
ax3 = fig.add_subplot(1, 3, 3)              # 1행 3열 - 3번째 그래프
# 빈도 막대 그래프
sns.countplot(x='class', palette='Set1', data=titanic, ax=ax1)
# hue='who' : who(man, woman, child)
sns.countplot(x='class', hue='who', palette='Set2', data=titanic, ax=ax2)
# hue='who', dodge=False
sns.countplot(x='class', hue='who', dodge=False, palette='Set3', data=titanic, ax=ax3)
# 차트 제목 표시
ax1.set_title('titanic 클래스')
ax2.set_title('titanic class - who')
ax3.set_title('titanic class - who(stacked)')
plt.show()

# 박스플롯 / 바이올린 그래프
# 박스플롯은 범주형 데이터 분포와 주요 통계 지표를 함께 제공한다.
# 박스플롯 만으로는 데이터가 퍼져있는 분산의 정도를 정확하게 알기 어렵기 때문에
# 커널 밀도함수를 y축 방향에 추가하여 바이올린 그래프로 출력할 수 있다.
# 박스플롯은 boxplot() 함수로 그릴수 있고, 바이올린 그래프는 violinplot() 함수로 그릴수 있다.
# 다음은 타이타닉 생존자 분포를 박스플롯과 바이올린 그래프로 출력 해보자
# 박스 그래프 - 기본값
sns.boxplot(x='alive', y='age', data=titanic, ax=ax1)
# 박스 그래프 - hue = 'sex' 변수를 추가하여 남녀 데이터를 구분하여 출력
sns.boxplot(x='alive', y='age', hue='sex', data=titanic, ax=ax2)
# 바이올린 그래프 - 기본값
sns.violinplot(x='alive', y='age', data=titanic, ax=ax3)
# 바이올린 그래프 - hue = 'sex' 변수를 추가하여 남녀 데이터를 구분하여 출력
sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax=ax4)

# 박스 플롯 / 바이올린 그래프
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')
# 그래프 크기 설정, 서브플롯 설정
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(2, 2, 1)          # 2행 2열 - 1번째 그래프
ax2 = fig.add_subplot(2, 2, 2)          # 2행 2열 - 2번째 그래프
ax3 = fig.add_subplot(2, 2, 3)          # 2행 2열 - 3번째 그래프
ax4 = fig.add_subplot(2, 2, 4)          # 2행 2열 - 4번째 그래프
# 박스 그래프
sns.boxplot(x='alive', y='age', data=titanic, ax=ax1)
# 박스 그래프 : hue='sex'
sns.boxplot(x='alive', y='age', hue='sex', data=titanic, ax=ax2)
# 바이올린 그래프
sns.violinplot(x='alive', y='age', data=titanic, ax=ax3)
# 바이올린 그래프 : hue='sex'
sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax=ax4)
plt.show()

# 조인트 그래프
# 조인트 그래프는 jointplot() 함수로 산점도를 기본적으로 표시하고, x-y축에 각 변수에
# 대한 히스토그램을 동시에 보여주는 그래프 이다. 따라서 두 변수의 관계와 데이터가
# 분산되어 있는 정도를 한눈에 파악하기 좋은 그래프 이다.
# 예제에서는 산점도(기본값), 회귀선 추가(kind=‘reg’), 육각 산점도(kind=‘hex’),
# 커널밀집 그래프(kind=‘kde’) 순으로 조인트 그래프를 그려서 차이를 비교해보자.
# 조인트 그래프 - 산점도(기본값)
j1 = sns.jointplot(x='fare', y='age', data=titanic)
# 조인트 그래프 - 회귀선 : kind='reg'
j2 = sns.jointplot(x='fare', y='age', kind='reg', data=titanic)
# 조인트 그래프 - 육각 그래프 : kind='hex'
j3 = sns.jointplot(x='fare', y='age', kind='hex', data=titanic)
# 조인트 그래프 - 커럴 밀집 그래프 : kind='kde'
j4 = sns.jointplot(x='fare', y='age', kind='kde', data=titanic)

# 조인트 그래프
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')
# 조인트 그래프 - 산점도(기본값) + 히스토그램
j1 = sns.jointplot(x='fare', y='age', data=titanic)
# 조인트 그래프 : kind='reg' - 회귀선이 있는 산점도
j2 = sns.jointplot(x='fare', y='age', kind='reg', data=titanic)
# 조인트 그래프 : kind='hex' - 육각 그래프
j3 = sns.jointplot(x='fare', y='age', kind='hex', data=titanic)
# 조인 그래프 :  kind='kde' - 커널 밀집 그래프
j4 = sns.jointplot(x='fare', y='age', kind='kde', data=titanic)
# 차트 제목 표시
j1.fig.suptitle('titanic fare - scatter', size=15)
j2.fig.suptitle('titanic fare - reg', size=15)
j3.fig.suptitle('titanic fare - hex', size=15)
j4.fig.suptitle('titanic fare - kde', size=15)
plt.show()

# 조건을 적용하여 화면을 그리드로 분할한 그래프
# FacetGrid() 함수는 행, 열 방향으로 서로 다른 조건을 적용하여 여러 개의 서브플롯
# 그래프를 그려주는 역할을 한다. 그리고 각 서브플롯에 적용할 그래프 종류는 map()
# 함수를 이용하여 그리드 객체에 전달한다.
# 다음 예제는 열 방향으로는 ‘who’ 열의 탑승객 구분(man, woman, child) 값으로
# 구분하고, 행 방향으로는 ‘survived’ 열의 구조 여부(구조 survived=1, 구조실패
# survived=0) 값으로 구분하여 2행 3열 모양의 그리드로 그래프를 출력한다.
# 각 조건에 맞는 탑승객을 구분하여, ‘age’ 열의 나이를 기준으로 히스토그램을 그려보자
# 조건에 따라 그리드 나누기 : who(man, woman, child) , survived (0 or 1)
g = sns.FacetGrid(data=titanic, col='who', row='survived')
# 그래프 적용하기 : 히스토그램
g = g.map(plt.hist, 'age')

# 조건을 적용하여 화면을 그리드로 분할한 그래프
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')
# 조건에 따라 그리드 나누기 : who(man, woman, child) , survived(0 or 1)
g = sns.FacetGrid(data=titanic, col='who', row='survived')
# 그래프 적용하기 : 히스트그램
g = g.map(plt.hist, 'age')
plt.show()

# 데이터 분포 그래프
# pairplot() 함수는 인자로 전달되는 데이터프레임의 열을 두개씩 짝을 지을 수 있는
# 모든 조합에 대해서 그래프로 표현한다. 그래프를 그리기 위해서는 데이터의 개수
# 만큼 짝의 개수만큼 화면을 그리드로 나눈다.
# 다음에 예제는 3개의 열을 사용하기 때문에 3행 3열 크기로 모두 9개의 그리드를
# 만든다. 각 그리드에 두 변수 간의 관계를 나타내는 그래프를 하나씩 그린다.
# 같은 변수끼리 짝을 이루는 대각선 방향으로는 히스토그램을 그리고 서로 다른
# 변수 간에는 산점도를 그린다.
# titanic 데이터셋 중에서 분석 데이터 선택하기
titanic_pair = titanic[['age','pclass', 'fare']]
# 조건에 따라 그리드 나누기 : 3행 3열 그리드로 출력
g = sns.pairplot(titanic_pair)

# 데이터 분포 그래프
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
# print(titanic)

# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')
# 분석에 필요한 데이터 추출
titanic_pair = titanic[['age','pclass','fare']]
print(titanic_pair)
#       age  pclass     fare
# 0    22.0       3   7.2500
# 1    38.0       1  71.2833
# 2    26.0       3   7.9250
# 3    35.0       1  53.1000
# 4    35.0       3   8.0500
#           ...

# 조건에 따라 그리드로 나누기 : 3행 3열 그리드로 출력
g = sns.pairplot(titanic_pair)
plt.savefig('pairplot.png')
plt.show()



all = [var for var in globals() if var[0] != "-"]
for var in all:
    del globals()[var]
del(all)
del(var)

import sys
sys.modules[__name__].__dict__.clear()


# <<강의 복습 10. 끝>>
# pywork17.py end