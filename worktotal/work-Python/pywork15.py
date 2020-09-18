# numpy
# 1. numpy는 Numerical Python의 줄임말로 고성능의 과학계산 컴퓨팅과 데이터
# 분석에 필요핚 패키지이다.
# 2. numpy 는 수치 계산을 효율적으로 하기 위한 모듈로서, 다차원 배열과
# 고수준의 수학 함수를 제공.
# 3. numpy / pandas 두 라이브러리는 C언어로 작성돼 있으므로, 파이썬으로
# 만들어진 라이브러리 보다 처리 속도가 빠르다.
# 4. numpy 를 사용하려면, 표준 모듈이 아니므로 따로 설치해야 한다.
# pip명령으로 설치하면 되는데, Anaconda 를 사용한다면 기본적으로 설치
# 되어 있다.

# 시퀀스 데이터로부터 배열 생성
#  배열(Array) 이란 순서가 있는 같은 종류의 데이터가 저장된 집합을 말한다.
#  시퀀스 데이터(seq_data)를 인자로 받아 numpy 의 배열 객체를 생성 해보자.
#  시퀀스 데이터(seq_data)로 리스트와 튜플 타입의 데이터를 모두 사용할 수
# 있지만 주로 리스트 데이터를 사용한다.

# 배열
import numpy as np

data1 = [0,1,2,3,4,5]           # 리스트
a1 = np.array(data1)            # 1차원 배열
print(a1)                       # [0 1 2 3 4 5]
print(type(a1))                 # 'numpy.ndarray'
print(a1.dtype)                 # int32

data2 = [0.1, 4, 4, 12, 0.5]    # 리스트 : 정수와 실수 혼용
a2 = np.array(data2)            # 1차원 배열
print(a2)                       # [ 0.1  4.   4.  12.   0.5]
print(a2.dtype)                 # float64

a3 = np.array([0.5, 2, 0.01, 8])
print(a3)                       # [0.5  2.   0.01 8.  ]
print(a3.dtype)                 # float64

# 2차원 배열
a4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a4)
print(a4.dtype)                 # int32
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# np.arange(start, stop, step)
a1 = np.arange(0, 10, 2)
print(a1)                           # [0 2 4 6 8]

# np.arange(start, stop)
a2 = np.arange(1, 10)
print(a2)                           # [1 2 3 4 5 6 7 8 9]

# np.arange(stop)
a3 = np.arange(5)
print(a3)                           # [0 1 2 3 4]

# arange(12)로 12개의 숫자 생성 후, reshape(4,3)으로 4x3 행렬을 만든다.
a4 = np.arange(12).reshape(4,3)
print(a4)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]
print(a4.shape)                     # (4, 3) : 4행 3열 행렬

# linspace(start, stop, num)
a5 = np.linspace(1,10,10)           # 1 ~ 10까지 10개의 데이터 생성
print(a5)                           # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

a6 = np.linspace(1, 10, 3)          # 1 ~ 10까지 3개의 데이터 생성
print(a6)                           # [ 1.   5.5 10. ]

# 0부터 pi까지 동일한 간격으로 떨어진 20개의 데이터를 생성
a7 = np.linspace(0, np.pi, 20)
print(a7)
# [0.         0.16534698 0.33069396 0.49604095 0.66138793 0.82673491
#  0.99208189 1.15742887 1.32277585 1.48812284 1.65346982 1.8188168
#  1.98416378 2.14951076 2.31485774 2.48020473 2.64555171 2.81089869
#  2.97624567 3.14159265]

# zeros()함수로 원소의 갯수가 10개인 1차원 배열 생성
a1 = np.zeros(10)
print(a1)                   # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# 특별한 형태의 배열 생성
# zeros()함수는 모든 원소가 0인 다차원 배열을 생성
# ones()함수는 모든 원소가 1인 다차원 배열을 생성
#  np.zeros(n) : n개의 원소가 모두 0인 1차원 배열
#  np.zeros((m, n)) : 모든 원소가 0인 m x n 형태의 2차원 배열(행렬)
#  np.ones(n) : n개의 원소가 모두 1인 1차원 배열
#  np.ones((m, n)) : 모든 원소가 1인 m x n 형태의 2차원 배열(행렬)
#  np.eye(n) : n x n 단위행렬을 갖는 2차원 배열(행렬)
# 단위행렬(identity matrix)은 n x n 인 정사각형 행렬에서 주 대각선이
# 모두 1이고 나머지는 0인 행렬을 의미한다.

# zeros()함수를 이용해 3 x 4의 2차원 배열을 생성
a2 = np.zeros((3,4))
print(a2)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# ones()함수로 원소의 갯수가 5인 1차원 배열 생성
a3 = np.ones(5)
print(a3)                   # [1. 1. 1. 1. 1.]

# ones()함수로 3x5인 2차원 배열 생성
a4 = np.ones((3,5))
print(a4)
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

# 3 x 3 단위행렬 생성
a5 = np.eye(3)
print(a5)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 배열의 데이터 타입 변환
#  numpy 배열은 숫자뿐만 아니라 문자열도 원소로 가질 수 있다.
# str_arr = np.array( ['1.5', '0.62' , '2' , '3.14' , '3.141592' ] )
#  numpy 배열이 문자열로 되어 있다면, 연산을 하기 위해서는 숫자(정수, 실수)로
# 형 변환을 해야한다.
#  numpy 배열을 형변환 하기 위해서는 astype() 함수를 사용한다.
# num_arr = str_arr . astype( dtype )

# 1.실수형 문자를 원소로 갖는 numpy 배열 생성
str_a1 = np.array(['1.567','0.123','5.123','9','8'])
print(str_a1)                   # ['1.567' '0.123' '5.123' '9' '8']
print(str_a1.dtype)             # <U5  : 유니코드 5자리 문자

# astype()함수로 문자를 실수형 형변환
num_a1 = str_a1.astype(float)
print(num_a1)                   # [1.567 0.123 5.123 9.    8.   ]
print(num_a1.dtype)             # float64

# 2. 정수형 문자를 원소를 갖는 numpy 배열 생성
str_a2 = np.array(['1','3','5','7','9'])
print(str_a2)                   # ['1' '3' '5' '7' '9']
print(str_a2.dtype)             # <U1 : 유니코드 문자 1자리

# astype() 함수로 문자를 정수형으로 형변환
num_a2 = str_a2.astype(int)
print(num_a2)                   # [1 3 5 7 9]
print(num_a2.dtype)             # int32

# 3. 실수를 원소로 갖는 numpy 배열 생성
num_f1 = np.array([10, 21, 0.549, 4.75, 5.98])
print(num_f1)                   # [10.    21.     0.549  4.75   5.98 ]
print(num_f1.dtype)             # float64

# astype()함수로 실수를 정수형으로 형변환
num_i1 = num_f1.astype(int)
print(num_i1)                   # [10 21  0  4  5]
print(num_i1.dtype)             # int32

# 난수 배열의 생성
#  Python 에서 제공되는 random 모듈을 이용해서 난수 발생
# random.random() : 0.0 <= 실수 <1.0 사이의 실수 형태의 난수 발생
# random.randint(1, 10) : 1<= 정수 <=10 사이의 정수 형태의 난수 발생
#  Numpy 모듈에서 제공되는 rand(), randint() 함수를 이용해서 난수 발생
# np.random.rand() : 0이상 1미만 사이의 실수 형태의 난수 발생
# np.random.rand(2, 3) : 0이상 1미만 사이의 실수 형태의 2행 3열 난수 발생
# np.random.randint([low], high,[size]) : low이상 high미만의 정수 형태의난수 발생
# np.random.randn() : 표준편차가 1이고, 평균값이 0인 정규분포에서 표본추출

# 0.0 <= r1 < 1.0 사이의 실수형태의 난수 발생
r1 = np.random.rand()
print(r1)
# 0.0 <= r1 < 1.0 사이의 실수형태의 2행 3열 난수 발생
r2 = np.random.rand(2, 3)
print(r2)
# 1 <= r3 < 30 사이의 정수형태의 난수 발생
r3 = np.random.randint(1, 30)
print(r3)
# 0 <= r4 < 10 사이의 정수형태의 3행 4열 난수 발생
r4 = np.random.randint(10, size=(3,4))
print(r4)

# 배열의 산술 연산
#  배열의 형태(shape)가 같은 경우에 덧셈, 뺄셈, 곱셈, 나눗셈을 핛 수 있다.
#  배열의 각 원소 끼리 산술 연산을 수행한다.

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

a1 = arr1 + arr2           # 배열 더하기 : 같은 위치의 원소끼리 연산
print(a1)                  # [11 22 33 44]
a2 = arr1 - arr2
print(a2)                  # [ 9 18 27 36]
a3 = arr2 * 2
print(a3)                  # [2 4 6 8]
a4 = arr2 ** 2             # 배열에 거듭제곱
print(a4)                  # [ 1  4  9 16]
a5 = arr1 * arr2          # 배열 곱하기 : 같은 위치의 원소끼리 곱하기
print(a5)                 # [ 10  40  90 160]
a6 = arr1 / arr2         # 배열 나누기 : 같은 위치의 원소끼리 나누기
print(a6)                # [10. 10. 10. 10.]
a7 = arr1 / (arr2 ** 2)  # 복합연산
print(a7)                # [10.          5.          3.33333333  2.5       ]

# 비교연산 : 각 원소와 비교해서 참이면 True, 거짓이면 False를 리턴
a8 = arr1 > 20
print(a8)               # [False False  True  True]

# numpy의 통계분석 함수
#  numpy 에서는 통계에서 자주 사용하는 함수들을 지원핚다
# sum() : 원소의 합
# mean() : 평균
# var() : 분산
# std() : 표준편차
# max() : 최대값
# min() : 최소값
# cumsum() : 각 원소의 누적 합
# cumprod() : 각 원소의 누적 곱

arr3 = np.arange(5)
print(arr3)                 # [0 1 2 3 4]
sum = arr3.sum()            # 배열 각 원소의 합
print(sum)                  # 10
mean = arr3.mean()          # 배열 원소의 평균
print(mean)                 # 2.0
var = arr3.var()            # 분산
print(var)                  # 2.0
std = arr3.std()            # 표준편차
print(std)                  # 1.4142135623730951
max = arr3.max()            # 최대값
print(max)                  # 4
min = arr3.min()            # 최소값
print(min)                  # 0
arr4 = np.arange(1, 5)
print(arr4)                 # [1 2 3 4]
cumsum = arr4.cumsum()      # 각 원소들의 누적합
print(cumsum)               # [ 1  3  6 10]
cumprod = arr4.cumprod()    # 각 원소들의 누적곱
print(cumprod)              # [ 1  2  6 24]

# 행렬 연산
#  Numpy 에서는 배열의 단순 연산뿐만 아니라, 선행대수(Linear Algebra)를
# 위한 행렬(2차원 배열) 연산도 지원핚다.
#  다양한 기능 중에서 행렬곱, 전치행렬, 역행렬, 행렬식을 구하는 방법을
# 알아보자
# 행렬곱(matrix product) A.dot(B) 혹은 np.dot(A,B)
# 전치행렬(transpose matrix) A.transpose() 혹은 np.transpose(A)
# 역행렬(inverse matrix) np.linalg.inv(A)
# 행렬식(determinant) np.linalg.det(A)

# 2 x 2 행렬 A와 B생성
A = np.array([0,1,2,3]).reshape(2,2)
B = np.array([3,2,0,1]).reshape(2,2)
print(A)
# [[0 1]
#  [2 3]]
print(B)
# [[3 2]
#  [0 1]]

# 행렬 곱
print(A.dot(B))
print(np.dot(A,B))
# [[0 1]
#  [6 7]]
# 행렬 A의 전치행렬
print(A.transpose())
print(np.transpose(A))
# [[0 2]
#  [1 3]]
# 행렬 A의 역행렬
print(np.linalg.inv(A))
# [[-1.5  0.5]
#  [ 1.   0. ]]

# 배열의 인덱싱
#  배열에서 선택된 원소의 값을 가져오거나 변경 할 수 있다.
# 배열의 위치나 조건을 지정해 배열의 원소를 선택하는 것을 인덱싱(indexing)
# 이라고 한다.
#  1차원 배열 인덱싱
# 배열명[index번호] : index번호의 원소1개를 인덱싱
# 배열명[ [index번호, index번호,...., index번호] ] : 여러 개의 원소를 인덱싱
#  2차원 배열 인덱싱
# 배열명[ 행 위치, 열 위치 ]
# 배열명[ [행 위치1,행 위치2,...,행 위치n] , [열 위치1,열 위치2,.....,열 위치n] ]
# 배열명[ 조건 ]

# 1차원 배열 생성
a1 = np.array([0,10,20,30,40,50])
print(a1)               # [ 0 10 20 30 40 50]
# 인덱스 번호 1번 위치의 원소 인덱싱
print(a1[1])            # 10
# 인덱스 번호 4번 위치의 원소 인덱싱
print(a1[4])            # 40
# 인덱스 번호 5번 위치의 원소값 50 -> 70으로 수정
a1[5] = 70
print(a1[5])            # 70
# 1차원 배열에서 여러개의 원소 인덱싱
print(a1[[1, 3, 4]])    # [10 30 40]

# 2차원 배열 생성: 10~90까지 10씩 증가된 배열
a2 = np.arange(10, 100, 10).reshape(3,3)
print(a2)
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
# 배열명[행위치, 열위치] : 0행 2열 원소를 인덱싱
print(a2[0, 2])             # 30
# 2행 2열의 원소의 값을 90 -> 95로 변경
a2[2, 2] = 95
print(a2[2,2])              # 95
print(a2)
# [[10 20 30]
#  [40 50 60]
#  [70 80 95]]

# 2차원 배열의 1행 전체를 변경 : [40 50 60] -> [45 55 65]
a2[1] = np.array([45, 55, 65])
print(a2)
# [[10 20 30]
#  [45 55 65]
#  [70 80 95]]

# 2차원 배열에서 여러개의 원소 인덱싱
# 배열명[[행위치1, 행위치2], [열위치1, 열위치2]]
# (0,0)위치의 원소 인덱싱 : 10
# (2,1)위치의 원소 인덱싱 : 80
print(a2[[0, 2],[0, 1]])            # [10 80]

# 2차원 배열에서 조건을 만족하는 원소 인덱싱
# 배열명[조건] : 조건에 맞는 원소만 리턴
a = np.array([1,2,3,4,5,6])
print(a[a > 3])                     # [4 5 6]

# 배열의 슬라이싱(Slicing)
#  배열에서 선택된 원소의 값을 가져오거나 변경 할 수 있다.
# 배열의 범위를 지정해서 배열의 원소를 선택하는 것을 슬라이싱(Slicing)
# 이라고 한다.
#  1차원 배열 슬라이싱
# 배열명[시작위치 : 끝위치] : 시작위치 ~ 끝위치 -1 번 원소 슬라이싱
# 배열명[시작위치 : ] : 시작위치 ~ 끝위치 원소 슬라이싱
# 배열명[ : 끝위치] : 처음부터 ~ 끝위치 -1 번 원소 슬라이싱
#  2차원 배열 슬라이싱
# 배열[행 시작위치 : 행 끝위치 , 열 시작위치 : 열 끝위치]
# 배열명[ [행 시작위치 : 행 끝위치] , [열 시작위치 : 열 끝위치] ]
# 배열명[행 위치] [열 시작위치 : 열 끝위치]

# 1차원 배열 슬라이싱
# 1차원 배열 정의
b1 = np.array([0, 10, 20, 30, 40, 50])
print(b1)               # [ 0 10 20 30 40 50]
# 배열명[시작위치 : 끝위치] : 시작위치 ~ 끝위치 -1 번 원소 슬라이싱
# 인덱스 1 ~ 3번 원소를 슬라이싱
print(b1[1:4])          # [10 20 30]
# 배열명[시작위치 : ] : 시작위치 ~ 끝위치 원소 슬라이싱
# 인덱스 2번 부터 끝까지 슬라이싱
print(b1[2:])           # [20 30 40 50]
# 배열명[ : 끝위치] : 처음부터 ~ 끝위치 -1 번 원소 슬라이싱
# 처음부터 인덱스 2번 까지 슬라이싱
print(b1[:3])           # [ 0 10 20]
# 슬라이싱으로 원소의 값 변경
# 인덱스 2~4번 원소의 값을 변경 : [20, 30, 40] -> [25, 35, 45]
b1[2:5] = np.array([25,35,45])
# b1[2:5] = [25,35,45]
print(b1[2:5])          # [25 35 45]
print(b1)               # [ 0 10 25 35 45 50]
# 인덱스 3~5번 원소의 값을 60으로 변경
b1[3:6] = 60
print(b1)               # [ 0 10 25 60 60 60]

# 2차원 배열의 슬라이싱
# 2차원 배열 정의 : 10~90까지 10씩 증가된 3행 3열 배열
b2 = np.arange(10, 100, 10).reshape(3,3)
print(b2)
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]
# 배열[행 시작위치 : 행 끝위치 , 열 시작위치 : 열 끝위치]
# 1~2행, 1~2열 슬라이싱
print(b2[1:3, 1:3])
# [[50 60]
#  [80 90]]
# 모든행, 1열부터 끝까지 슬라이싱
print(b2[:, 1:])
# [[20 30]
#  [50 60]
#  [80 90]]
# 배열명[행 위치] [열 시작위치 : 열 끝위치]
# 1행, 0~1열 데이터 슬라이싱
print(b2[1][0:2])           # [40 50]
# 2차원 배열에서 슬라이싱 된 배열에 새로운 값을 지정
# 0~1행, 1~2열 위치에 [25,35], [55,65]값으로 변경
b2[0:2, 1:3] = np.array([[25,35],[55,65]])
print(b2)
# [[10 25 35]
#  [40 55 65]
#  [70 80 90]]

# pandas
#  구조적 데이터 생성
# - Series를 활용한 데이터 생성 : Series()
# - 날짜 자동 생성 : date_range()
# - DataFrame을 홗용한 데이터 생성 : DataFrame()
#  데이터 연산
#  데이터 원하는 부분 추출하기
#  데이터 통합하기
#  데이터 파일 읽고 쓰기

# 1. numpy / pandas 는 고급 데이터 분석과 수치 계산 등의 기능을 제공하는
# 확장 모듈이다.
# 2. numpy 는 같은 데이터 타입의 배열맊 처리할 수 있는 데 반해서 pandas는
# 데이터 타입이 다양하게 섞여 있는 데이터도 처리할 수 있다.
# 3. pandas 는 데이터 분석 기능을 제공하는 라이브러리로서, CSV, 엑셀 파일 등의
# 데이터를 읽고 원하는 데이터 형식으로 변환해 줍니다.
# 4. numpy / pandas 두 라이브러리는 C언어로 작성돼 있으므로, 파이썬으로
# 만들어진 라이브러리 보다 처리 속도가 빠릅니다.
# 5. numpy / pandas 를 사용하려면, 표준 모듈이 아니므로 따로 설치해야
# 한다. pip명령으로 설치하면 되는데, Anaconda 를 사용한다면 기본적으로
# 설치 되어 있다.

# pandas 모듈은 데이터 형태에 따라 1차원 데이터인 Series와
# 2차원 데이터인 DataFrame을 사용한다.
#  1차원 데이터 : Series
#  2차원 데이터 : DataFrame
import numpy as np
import pandas as pd

# 1차원 데이터  Series 생성
s = pd.Series([1.0, 3.0, 5.0, 7.0, 9.0])
print(s)
# 1. 스칼라(scalar)  데이터
s1 = pd.Series(7, index=['a','b','c'])
print(s1)
# 2.  일차춴 배열 데이터
s2 = pd.Series(np.random.randn(5))
print(s2)
s3 = pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
print(s3)
# 3. 리스트 데이터
s4 = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s4)
# 4. 딕셔너리 데이터
s5 = pd.Series({'국어':80, '영어':90, '수학':85})
print(s5)

# 날짜 자동 생성 : date_range()
# pandas에서 제공되는 date_range() 함수는 연속적인 날짜를 자동으로 생성
# 해주는 역할을 한다.
# 형식 : pd.date_range ( start , end, periods, freq = 'D' )
# start : 시작 날짜
# end : 끝 날짜
# periods : 날짜 데이터 생성 기간
# freq : 입력하지 않으면 'D' 옵션이 설정돼 달력 날짜 기준으로 하루를
# 증가한다. ( 달력 날짜 기준 하루 기준 )
# start는 반드시 있어야하며 end나 periods는 둘 중 하나만 있어도 된다.
# 예) pd.data_range( start = '2019-01-01' , end = '2019-01-07' )

# 시작 날짜(start)와 끝 날짜(end)를 지정해서 날짜 데이터 생성
date1 = pd.date_range(start='2020-01-01', end='2020-01-07')
print(date1)
# 시작 날짜(start)와 날짜 생성 기간(periods)을 7로 지정해서 날짜 데이터 생성
date2 = pd.date_range(start='2020-01-01', periods=7)
print(date2)
# 2일씩 증가하는 날짜 생성
date3 = pd.date_range(start='2020-01-01', periods=7, freq='2D')
print(date3)
# 1시간 주기로 10개의 시간을 생성
date4 = pd.date_range(start='2020-01-01 08:00', periods=10, freq='H')
print(date4)
# 30분 단위로 4개의 시간을 생성
date5 = pd.date_range(start='2020-01-01 10:00', periods=5, freq='30min')
print(date5)
# 10초 단위로 4개의 시간을 생성
date6 = pd.date_range(start='2020-01-01 10:00:00', periods=5, freq='10S')
print(date6)

# DataFrame
# 1. pandas에서 사용하는 가장 기본 데이터는 데이터프레임(DataFrame)이다.
# 2. DataFrame을 정의할 때는 2차원 리스트를 매개변수로 사용한다.
# 형식 : pd.DataFrame( data [ , index = index_data , columns = columns_data ] )

# 데이터 프레임 생성
a = pd.DataFrame([[10,20,30],
                  [40,50,60],
                  [70,80,90]])
print(a)
#     0   1   2     --- 컬럼(열이름)
# 0  10  20  30     --  인덱스(행이름)
# 1  40  50  60
# 2  70  80  90

# 1. 2차원 배열 데이터로 데이터프레임 생성
data = np.array([[10,20,30],[40,50,60],[70,80,90]])
df1 = pd.DataFrame(data)
print(df1)
#     0   1   2      -- 컬럼(열이름)
# 0  10  20  30      -- 인덱스(행이름)
# 1  40  50  60
# 2  70  80  90

# 2. index, columns 를 지정해서 데이터프레임 생성
data = np.array([[10,20,30],[40,50,60],[70,80,90]])
index_date = pd.date_range('2020-01-01', periods=3)
columns_list = ['A','B','C']
df2 = pd.DataFrame(data, index=index_date, columns=columns_list)
print(df2)
#              A   B   C
# 2020-01-01  10  20  30
# 2020-01-02  40  50  60
# 2020-01-03  70  80  90

# 3. 딕셔너리 데이터를 이용해서 데이터프레임 생성
table_data = {'연도':[2015,2016,2016,2017,2017],
              '지사':['한국','한국','미국','한국','미국'],
              '고객수':[200,250,450,300,500]}
print(table_data)
df3 = pd.DataFrame(table_data)
# df3 = pd.DataFrame(table_data, index=['A','B','C','D','E'])
print(df3)
#   연도  지사  고객수         --- 컬럼(딕셔너리의 key)
# 0  2015  한국  200
# 1  2016  한국  250
# 2  2016  미국  450
# 3  2017  한국  300
# 4  2017  미국  500
print(df3.index)        # RangeIndex(start=0, stop=5, step=1)
print(df3.columns)      # Index(['연도', '지사', '고객수'], dtype='object')
print(df3.values)
# [[2015 '한국' 200]
#  [2016 '한국' 250]
#  [2016 '미국' 450]
#  [2017 '한국' 300]
#  [2017 '미국' 500]]

# 원하는 데이터 추출하기
# : 1차원 리스트가 들어있는 딕셔너리 자료형의 데이터가 있을 때 키(key)로
# 원하는 열의 데이터를 추출할 수 있다.

# 데이터프레임 : key를 이용해서 데이터 추출
# 키, 몸무게, 유형 정보를 이용해서 데이터프레임 생성
tbl = pd.DataFrame({'weight': [80.0, 70.4, 65.5, 45.9, 51.2],
                    'height': [170, 180, 155, 143, 154],
                    'type':   ['f','n','n','t','t']})
print(tbl)
#     weight  height  type       --- 컬럼명 : 딕셔너리의 key
# 0    80.0     170    f
# 1    70.4     180    n
# 2    65.5     155    n
# 3    45.9     143    t
# 4    51.2     154    t

# 몸무게 정보 구하기
print('몸무게 목록')
print(tbl['weight'])
# 0    80.0
# 1    70.4
# 2    65.5
# 3    45.9
# 4    51.2
# 키정보 구하기
print('키 목록')
print(tbl['height'])
# 0    170
# 1    180
# 2    155
# 3    143
# 4    154
# 몸무게와 키 정보 구하기
print('몸무게와 키 목록')
print(tbl[['weight','height']])
#     weight   height
# 0    80.0     170
# 1    70.4     180
# 2    65.5     155
# 3    45.9     143
# 4    51.2     154

# 데이터프레임의 데이터 슬라이싱
# 키, 몸무게, 유형 정보를 가진 데이터프레임 생성
tbl = pd.DataFrame({
        'weight' : [80.0, 70.4, 65.5, 45.9, 51.2, 72.5],
        'height' : [170, 180, 155, 143, 154, 160],
        'type'   : ['f', 'n', 'n', 't', 't', 't']
      })
print(tbl)
#     weight   height type       --- 컬럼명 : 딕셔너리의 KEY
# 0    80.0     170    f
# 1    70.4     180    n
# 2    65.5     155    n
# 3    45.9     143    t
# 4    51.2     154    t
# 5    72.5     160    t

# 인덱스 2~3번 데이터 슬라이싱
print(tbl[2:4])
#     weight  height type
# 2    65.5     155    n
# 3    45.9     143    t
# 인덱스 3번부터 끝까지 슬라이싱
print(tbl[3:])
#     weight  height type
# 3    45.9     143    t
# 4    51.2     154    t
# 5    72.5     160    t
# 처음부터 인덱스 3번까지 슬라이싱
print(tbl[:4])
#     weight  height  type
# 0    80.0     170    f
# 1    70.4     180    n
# 2    65.5     155    n
# 3    45.9     143    t

# 데이터프레임의 데이터 중에서 조건식을 만족하는 데이터 추출
# 몸무게, 키, 성별 정보를 가진 데이터프레임 생성
tbl = pd.DataFrame({
        'weight' : [80.0, 70.4, 65.5, 45.9, 51.2, 72.5],
        'height' : [170, 180, 155, 143, 154, 160],
        'gender' : ['f', 'm', 'm', 'f', 'f', 'm']
      })
print(tbl)
#      weight  height gender        --- 컬럼명
# 0    80.0     170      f
# 1    70.4     180      m
# 2    65.5     155      m
# 3    45.9     143      f
# 4    51.2     154      f
# 5    72.5     160      m

print('몸무게(weight)가 70 이상인 데이터 추출')
print(tbl[tbl.weight >= 70])
#      weight  height gender
# 0    80.0     170      f
# 1    70.4     180      m
# 5    72.5     160      m
print('키(height)가 160 이상인 데이터 추출')
print(tbl[tbl.height >= 160])
#     weight  height gender
# 0    80.0     170      f
# 1    70.4     180      m
# 5    72.5     160      m
print('성별(gender)이 남자(m) 데이터 추출')
print(tbl[tbl.gender == 'm'])
#     weight  height gender
# 1    70.4     180      m
# 2    65.5     155      m
# 5    72.5     160      m

# 데이터 정렬 : sort_values()
# 오름차순 정렬이 기본 정렬방식
# 몸무게, 키, 성별 정보를 가진 데이터프레임 생성
tbl = pd.DataFrame({
        'weight' : [80.0, 70.4, 65.5, 45.9, 51.2, 72.5],
        'height' : [170, 180, 155, 143, 154, 160],
        'gender' : ['f', 'm', 'm', 'f', 'f', 'm']
      })
print(tbl)
#      weight  height gender
# 0    80.0     170      f
# 1    70.4     180      m
# 2    65.5     155      m
# 3    45.9     143      f
# 4    51.2     154      f
# 5    72.5     160      m

print('키(height)로 오름차순 정렬')
print(tbl.sort_values(by='height'))
#      weight  height  gender
# 3    45.9     143      f
# 4    51.2     154      f
# 2    65.5     155      m
# 5    72.5     160      m
# 0    80.0     170      f
# 1    70.4     180      m
print('몸무게(weight)로 내림차순 정렬')
print(tbl.sort_values(by='weight', ascending=False))
#      weight  height gender
# 0    80.0     170      f
# 5    72.5     160      m
# 1    70.4     180      m
# 2    65.5     155      m
# 4    51.2     154      f
# 3    45.9     143      f

# 데이터프에임의 행과 열 바꾸기
tbl = pd.DataFrame([['A','B','C'],
                    ['D','E','F'],
                    ['G','H','I']])
print(tbl)
#    0  1  2    --- 컬럼
# 0  A  B  C
# 1  D  E  F
# 2  G  H  I
print('행과 열 바꾸기')
print(tbl.T)
#    0  1  2
# 0  A  D  G
# 1  B  E  H
# 2  C  F  I

# 정규화(normalization)
# 수식 : (요소값 - 최소값) / (최대값 - 최소값)
# 설명 : 전체 구갂을 0~100으로 설정하여 데이터를 관찰하는 방법으로,
# 특정 데이터의 위치를 확인할 수 있게 해줌

#  키와 몸무게 정규화
# 1. 키와 몸무게의 최대값을 각각 200과 100으로 결정한 뒤, 데이터를 나누면
# 데이터를 0과 1 사이의 값으로 만들 수 있다.
# 2. 다만 이 같은 방법은 키가 200이상, 몸무게가 100이상인 경우에는 제대로
# 정규화 하지 못 한다.
# 3. 조금 더 정확하게 정규화 하는 방법
# 수식 : (요소값 - 최소값) / (최대값 - 최소값)
# 설명 : 전체 구갂을 0~100으로 설정하여 데이터를 관찰하는 방법으로,
# 특정 데이터의 위치를 확인할 수 있게 해줌

# 키, 몸무게 정규화
# (요소값 - 최소값) / (최대값 - 최소값)
import pandas as pd

# 몸무게, 키, 성별 정보를 가진 데이터프레임 생성
tbl = pd.DataFrame({
        'weight' : [80.0, 70.4, 65.5, 45.9, 51.2, 72.5],
        'height' : [170, 180, 155, 143, 154, 160],
        'gender' : ['f', 'm', 'm', 'f', 'f', 'm']
      })
print(tbl)

def norm(tbl, key):
    # 최대값, 최소값 구하기
    c = tbl[key]                    # c = [80.0, 70.4, 65.5, 45.9, 51.2, 72.5]
    v_max = c.max()                 # 80.0
    v_min = c.min()                 # 45.9
    print(key,':',v_min,'-',v_max)
    # 몸무게, 키의 정규화
    tbl[key] = (c - v_min) / (v_max - v_min)

norm(tbl, 'weight')         # norm 함수 호출
norm(tbl, 'height')         # norm 함수 호출
print(tbl)
#    weight    height    gender
# 0  1.000000  0.729730      f
# 1  0.718475  1.000000      m
# 2  0.574780  0.324324      m
# 3  0.000000  0.000000      f
# 4  0.155425  0.297297      f
# 5  0.780059  0.459459      m

# Pandas 데이터의 연산
# 1. pandas의 Series() 와 DataFrame()으로 생성한 데이터 끼리는 산술연산을
# 할 수 있다.
# 2. numpy 배열은 원소의 개수가 다르면 연산을 할 수 없지맊, pandas는 원소의
# 갯수가 서로 달라도 산술연산을 할 수 있다.
# 단, 연산할 수 없는 부분은 NaN 으로 표시된다.
# 3. 같은 Series() 데이터 끼리 산술연산
# 4. 같은 DataFrame() 데이터 끼리 산술연산

# Series 데이터의 산술연산
# 1. 원소의 갯수가 같은 경우
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([10,20,30,40,50])
print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)
# 2. 원소의 갯수가 다른  경우
# 1) numpy배열은 원소의 갯수가 서로 다르면 산술연산을 할 수 없지만,
#    pandas는 원소의 갯수가 달라도 산술연산을 할 수 있다.
# 2) 연산을 할 수 없는 경우에는 NaN으로 출력됨
s3 = pd.Series([1,2,3,4])
s4 = pd.Series([10,20,30,40,50])
print(s3+s4)
print(s3-s4)
print(s3*s4)
print(s3/s4)

# 데이터 프레임의 산술연산
table_data1 = {'A':[1,2,3,4,5],
               'B':[10,20,30,40,50],
               'C':[100,200,300,400,500]}
table_data2 = {'A':[6,7,8],
               'B':[60,70,80],
               'C':[600,700,800]}
df1 = pd.DataFrame(table_data1)
print(df1)
#    A   B    C         --- 컬럼
# 0  1  10   100
# 1  2  20   200
# 2  3  30   300
# 3  4  40   400
# 4  5  50   500
df2 = pd.DataFrame(table_data2)
print(df2)
#    A   B    C         --- 컬럼
# 0  6  60  600
# 1  7  70  700
# 2  8  80  800
print(df1+df2)
print(df1-df2)
print(df1*df2)
print(df1/df2)

# pandas의 통계분석 함수
#  pandas 에서는 통계에서 자주 사용하는 함수들을 지원핚다
# sum() : 원소의 합
# mean() : 평균
# var() : 분산
# std() : 표준편차
# max() : 최대값
# min() : 최소값
# cumsum() : 각 원소의 누적 합
# cumprod() : 각 원소의 누적 곱
# describe() : 평균, 표준편차, 최소값, 최대값 등을 한꺼번에 구해줌

# axis 인자를 설정하지 않으면 기본값이 0이 설정됨
# axis = 0 이면 열(column)별로 합을 구함 : 각 계절별 강수량 합을 구함
# axis = 1 이면 행(row)별로 합을 구함 : 각 연도별 강수량 합을 구함

# 2012년 부터 2016년까지 우리나라 계절별 강수량 데이터 ( 단위 : mm )
table_data = {'봄' : [256.5, 264.3, 215.9, 223.2, 312.8],
              '여름' : [770.6, 567.5, 599.8, 387.1, 446.2],
              '가을' : [363.5, 231.2, 293.1, 247.7, 381.6],
              '겨울' : [139.3, 59.9, 76.9, 109.1, 108.1]}
# columns_list = ['봄', '여름', '가을', '겨울']
# index : 연도, columns : 계절
# df = pd.DataFrame(table_data, index=index_list, columns=columns_list)
index_list = ['2012','2013','2014','2015','2016']
df = pd.DataFrame(table_data, index=index_list)
print(df)
#        봄     여름    가을    겨울
# 2012  256.5  770.6  363.5  139.3
# 2013  264.3  567.5  231.2   59.9
# 2014  215.9  599.8  293.1   76.9
# 2015  223.2  387.1  247.7  109.1
# 2016  312.8  446.2  381.6  108.1

# 1. 2012 ~ 2016년 계절별 강수량의 합
print('계절별 강수량의 합')
sum0 = df.sum(axis=0)         # axis=0 : 열(column)로 합을 구함
print(sum0)
# 봄      1272.7
# 여름    2771.2
# 가을    1517.1
# 겨울     493.3
# 2. 2012 ~ 2016년 연도별 강수량의 합
print('연도별 강수량 합')
sum1 = df.sum(axis=1)       # axis=1 : 행(row)으로 합을 구함
print(sum1)
# 2012    1529.9
# 2013    1122.9
# 2014    1185.7
# 2015     967.1
# 2016    1248.7
# 3. 2012 ~ 2016년 계절별 강수량의 평균
print('계절별 강수량 평균')
mean0 = df.mean(axis=0)     # axis=0 : 열(column)로 평균을 구함
print(mean0)
# 봄      254.54
# 여름    554.24
# 가을    303.42
# 겨울     98.66
# 4. 2012 ~ 2016년 연도별 강수량의 평균
print('연도별 강수량 평균')
mean1 = df.mean(axis=1)     # axis=1 : 행(row)으로 평균을 구함
print(mean1)
# 2012    382.475
# 2013    280.725
# 2014    296.425
# 2015    241.775
# 2016    312.175
# 5. describe() : 평균, 표준편차, 최소값, 최대값 등을 한꺼번에 구해주는 함수
describe = df.describe()
print(describe)
#          봄          여름          가을         겨울
# count    5.000000    5.000000    5.000000    5.000000
# mean   254.540000  554.240000  303.420000   98.660000
# std     38.628267  148.888895   67.358496   30.925523
# min    215.900000  387.100000  231.200000   59.900000
# 25%    223.200000  446.200000  247.700000   76.900000
# 50%    256.500000  567.500000  293.100000  108.100000
# 75%    264.300000  599.800000  363.500000  109.100000
# max    312.800000  770.600000  381.600000  139.300000

# DataFrame 데이터 추출
#  DataFrame_data.head() : 첫 5개 행데이터 반환
#  DataFrame_data.head( n ) : 첫 n개 행데이터 반환
#  DataFrame_data.tail() : 마지막 5개 행데이터 반환
#  DataFrame_data.tail( n ) : 마지막 n개 행데이터 반환
#  DataFrame_data[ 행 시작위치 : 행 끝위치 ]
# : 행 시작위치 ~ 행 끝위치 – 1 까지 행데이터 반환 행 위치는 0부터 시작
#  DataFrame_data.loc[index_name]
# : index가 index_name인 행 데이터 반환
#  DataFrame_data.loc[start_index_name : end_index_name]
# : index가 start_index_name에서 end_index_name까지 구간의 행 데이터를 반환

# DataFrame_data[column_name]
# : 하나의 열(column_name)로 지정한 데이터반환
#  DataFrame_data[column_name] [start_index_name : end_index_name]
# : 하나의 열(column)을 선택한 후 start_index_name ~ end_index_name
#  DataFrame_data[column_name] [start_index_pos : end_index_pos]
# : 하나의 열(column)을 선택한 후 start_index_pos ~ end_index_pos-1

#  DataFrame 데이터 중에서 하나의 원소 선택하는 방법들
# 1. DataFrame_data.loc[index_name] [column_name]
# 2. DataFrame_data.loc[index_name , column_name]
# 3. DataFrame_data[column_name][index_name]
# 4. DataFrame_data[column_name][index_pos]
# 5. DataFrame_data[column_name].loc[index_name]
#  DataFrame_data.T : DataFrmae의 행과 열을 바꾸는 전치행렬을 맊들어준다.

# 2011년 부터 2017년까지 노선별 KTX이용자 수(단위: 천명) 데이터
KTX_data = {'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
            '경전선 KTX': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
            '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
            '동해선 KTX': [np.nan,np.nan, np.nan, np.nan, 2395, 3786, 6667]}
index_list = ['2011','2012','2013','2014','2015','2016','2017']
df_KTX = pd.DataFrame(KTX_data, index=index_list)
print(df_KTX)
#     경부선 KTX  호남선 KTX 경전선 KTX 전라선 KTX 동해선 KTX
# 2011    39060     7313     3627      309      NaN
# 2012    39896     6967     4168     1771      NaN
# 2013    42005     6873     4088     1954      NaN
# 2014    43621     6626     4424     2244      NaN
# 2015    41702     8675     4606     3146   2395.0
# 2016    41266    10622     4984     3945   3786.0
# 2017    32427     9228     5570     5766   6667.0

print(df_KTX.index)     # Index(['2011', '2012', '2013', '2014', '2015', '2016', '2017'], dtype='object')
print(df_KTX.columns)   # Index(['경부선 KTX', '호남선 KTX', '경전선 KTX', '전라선 KTX', '동해선 KTX'], dtype='object')
print(df_KTX.values)
print(df_KTX.head())    # DataFrame 데이터의 첫 5개 행 데이터 출력
print(df_KTX.head(3))   # DataFrame 데이터의 첫 3개 행 데이터 출력
print(df_KTX.tail())    # DataFrame 데이터의 마지막 5개 행 데이터 출력
print(df_KTX.tail(3))   # DataFrame 데이터의 마지막 3개 행 데이터 출력

# DataFrame_data[행 시작위치 : 행 끝위치] : 행 시작위치 ~ 행 끝위치-1 까지의 행데이터 반환
# 행의 위치는 0부터 시작
print(df_KTX[1:2])       # 1의 행 데이터 출력
print(df_KTX[2:5])       # 2에서 4의 행 데이터 출력

# 행의 index 항목 이름으로 데이터 추출
# DataFrame_data.loc[index_name]
print(df_KTX.loc['2011']) # 2011년 행 데이터 추출

# 행의 index 항목 이름으로 구갂을 지정해서 연속된 구간의 행 데이터 추출
# DataFrame_data.loc[start_index_name : end_index_name]
print(df_KTX.loc['2013' : '2016']) # 2013년부터 2016년까지 행 데이터 추출

# DataFrame_data[column_name]
# columns 항목중 '경부선 KTX'의 열 데이터 추출
print(df_KTX['경부선 KTX'])

# DataFrame_data[column_name][index_name]
# DataFrame_data[column_name][index_pos]
# '경부선 KTX' 열을 선택할 후 2012년에서 2014년까지 데이터 추출
print(df_KTX['경부선 KTX']['2012':'2014'])
# '경부선 KTX' 열을 선택할 후 2행에서 4행 데이터 추출
print(df_KTX['경부선 KTX'][1:4])

# DataFrame 의 행과 열을 바꾸는 전치 행렬을 만들어 준다.
print(df_KTX.T)

# DataFrame 데이터 중에서 하나의 원소 선택하는 방법들
# 1. DataFrame_data.loc[index_name] [column_name]
print(df_KTX.loc['2016']['호남선 KTX'])        # 10622.0
# 2. DataFrame_data.loc[index_name , column_name]
print(df_KTX.loc['2016','호남선 KTX'])         # 10622
# 3. DataFrame_data[column_name][index_name]
print(df_KTX['호남선 KTX']['2016'])            # 10622
# 4. DataFrame_data[column_name][index_pos]
print(df_KTX['호남선 KTX'][5])                 # 10622
# 5. DataFrame_data[column_name].loc[index_name]
print(df_KTX['호남선 KTX'].loc['2016'])        # 10622

# DataFrame 데이터 통합하기
# 2개의 DataFrame데이터를 하나로 통합하는 방법을 살펴보자.
#  DataFrame 데이터 통합방법
# 1. 세로로 증가하는 방향으로 통합하기
# DataFrame_data1.append(DataFrame_data2 [,ignore_index=True])
# 2. 가로로 증가하는 방향으로 통합하기
# DataFrame_data1.join(DataFrame_data2)
# 3. 특정 열을 기준으로 통합하기
# DataFrame_left_data.merge(DataFrame_right_data,
#                             how=merge_method,
#                             on=key_label)

#  merge() 함수의 how 선택 인자에 따른 통합 방법
# DataFrame_left_data.merge( DataFrame_right_data ,
#                             how = merge_method ,
#                             on = key_label )
# ● how 선택 인자: left, right, outer, inner
# left 왼쪽 데이터는 모두 선택하고 지정된 열(key)에 값이 있는 오른쪽 데이터를 선택
# right 오른쪽 데이터는 모두 선택하고 지정된 열(key)에 값이 있는 왼쪽 데이터를 선택
# outer 지정된 열(key)을 기준으로 왼쪽과 오른쪽 데이터를 모두 선택
# inner 지정된 열(key)을 기준으로 왼쪽과 오른쪽 데이터 중 공통 항목맊 선택(기본값)
# ● on 인자:
# 통합하려는 기준이 되는 특정 열의 라벨 이름을 입력한다.
# 해당 항목이 없으면 NaN 으로 출력됨

# 두 학급의 시험 점수가 담긴 DataFrame 생성
df1 = pd.DataFrame({'Class1':[95,92,98,100],
                    'Class2':[91,93,97,99]})
print(df1)
#     Class1  Class2     ---- 컬럼
# 0      95      91
# 1      92      93
# 2      98      97
# 3     100      99

# 두 학급에 전학온 학생들의 점수 DataFrame 생성
df2 = pd.DataFrame({'Class1':[87,89],
                    'Class2':[85,90]})
print(df2)
#     Class1  Class2     ---- 컬럼
# 0      87      85
# 1      89      90

# 1. 세로방향으로 합치기 : append()함수
print(df1.append(df2))                      # 기존 인덱스 번호가 유지됨
#       Class1  Class2
# 0      95      91
# 1      92      93
# 2      98      97
# 3     100      99
# 0      87      85
# 1      89      90
print(df1.append(df2, ignore_index=True))   # 새로운 인덱스 번호가 부여됨
#       Class1  Class2
# 0      95      91
# 1      92      93
# 2      98      97
# 3     100      99
# 4      87      85
# 5      89      90

df3 = pd.DataFrame({'Class1':[96, 83]})
print(df3)
#    class1
# 0      96
# 1      83

# df2와 df3 데이터프레임을 세로방향으로 합치기
print(df2.append(df3, ignore_index=True))   # 데이터가 없는 부분은 NaN으로 처리
#      Class1  Class2
# 0      87    85.0
# 1      89    90.0
# 2      96     NaN
# 3      83     NaN

# 2. 가로방향으로 합치기 : join()함수
df4 = pd.DataFrame({'Class3':[93,91,95,98]})
print(df4)
#    Class3
# 0      93
# 1      91
# 2      95
# 3      98

# df1과 df4 데이터 프레임을 가로방향으로 합치기
print(df1.join(df4))
#       Class1  Class2  Class3
# 0      95      91      93
# 1      92      93      91
# 2      98      97      95
# 3     100      99      98

# 인덱스 값으로 출력
index_label = ['a','b','c','d']
df1a = pd.DataFrame({'Class1' : [95, 92, 98, 100],
                     'Class2' : [91, 93, 97, 99]}, index=index_label)
df4a = pd.DataFrame({'Class3' : [93, 91, 95, 98]}, index=index_label)
print(df1a.join(df4a))
#     Class1  Class2  Class3
# a      95      91      93
# b      92      93      91
# c      98      97      95
# d     100      99      98

# df5 데이터프레임 생성
df5 = pd.DataFrame({'Class4': [82, 92]})
print(df5)
#    Class4
# 0      82
# 1      92

# df1과 df5 데이터프레임을 가로방향으로 합치기 : 데이터가 없는 부분을 NaN 으로 처리
print(df1.join(df5))
#        Class1  Class2  Class4
# 0      95      91    82.0
# 1      92      93    92.0
# 2      98      97     NaN
# 3     100      99     NaN

# 3. 특정 열을 기준으로 합치기
df_A_B = pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                       '제품A':[100, 150, 200, 130],
                       '제품B':[90, 110, 140, 170]})
print(df_A_B)

df_C_D = pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                       '제품C':[112, 141, 203, 134],
                       '제품D':[90, 110, 140, 170]})
print(df_C_D)

# df_A_B와 df_C_D 데이터 프레임 합치기 : 공통컬럼 - 판매월
print(df_A_B.merge(df_C_D))
#    판매월  제품A   제품B  제품C 제품D
# 0     1월  100      90  112   90
# 1     2월  150     110  141  110
# 2     3월  200     140  203  140
# 3     4월  130     170  134  170

# 특정 열을 기준으로 일부맊 공통 데이터를 가진 DataFrame 데이터를 통합핚 예
df_left = pd.DataFrame({'key':['A','B','C'], 'left':[1,2,3]})
print(df_left)
#   key  left
# 0   A     1
# 1   B     2
# 2   C     3

df_right = pd.DataFrame({'key':['A','B','D'], 'right':[4,5,6]})
print(df_right)
#   key  right
# 0   A      4
# 1   B      5
# 2   D      6

print(df_left.merge(df_right))  # how=inner(기본값) : 공통 데이터
#    key  left  right
# 0   A     1      4
# 1   B     2      5
print(df_left.merge(df_right, how='left', on = 'key')) # 왼쪽을 먼저 선택
#    key  left  right
# 0   A     1    4.0
# 1   B     2    5.0
# 2   C     3    NaN
print(df_left.merge(df_right, how='right', on = 'key')) # 오른쪽을 먼저 선택
#    key  left  right
# 0   A   1.0      4
# 1   B   2.0      5
# 2   D   NaN      6
print(df_left.merge(df_right, how='outer', on = 'key')) # 양쪽을 모두 선택
#    key  left   right
# 0   A   1.0    4.0
# 1   B   2.0    5.0
# 2   C   3.0    NaN
# 3   D   NaN    6.0
print(df_left.merge(df_right, how='inner', on = 'key')) # 공통 항목맊 선택
#    key  left   right
# 0   A     1      4
# 1   B     2      5

# Pandas로 CSV 파일 읽기
# pandas 는 표형식의 데이터 파일을 DataFrame 형식의 데이터로 읽어오는 방법과,
# DataFrame 형식의 데이터를 표형식으로 파일로 저장할 수 있는 방법을 제공한다.
#  Pandas로 CSV(Comma Separated Value)파일 읽기
# DataFrame_date = pd.read_csv( filename, encoding=‘utf-8’ )
# 파이썬에서 텍스트 파일을 생성하면 기본 문자 인코딩 형식이 utf-8 이다.
# 하지맊 윈도우의 메모장에서 파일을 저장하면 인코딩 형식이 cp949 가 된다.
# pandas의 read_csv()로 csv파일을 읽을때는 텍스트 파일의 인코딩 옵션을 설정 해야된다.
# 텍스트 파일이 utf-8로 인코딩 되어 있으면, encoding = ‘utf8’
# 텍스트 파일이 cp949로 인코딩 되어 있으면, encoding = ‘cp949’

# data1/sea_rain1.csv 파일 읽어오기
df = pd.read_csv('data1/sea_rain1.csv', encoding='utf8')
print(df)
#     연도    동해    남해      서해      전체
# 0  1996  17.4629  17.2288  14.4360  15.9067
# 1  1997  17.4116  17.4092  14.8248  16.1526
# 2  1998  17.5944  18.0110  15.2512  16.6044
# 3  1999  18.1495  18.3175  14.8979  16.6284
# 4  2000  17.9288  18.1766  15.0504  16.6178
print(df['동해'])
# 0    17.4629
# 1    17.4116
# 2    17.5944
# 3    18.1495
# 4    17.9288

# Pandas로 CSV 파일 저장
# pandas 는 표형식의 데이터 파일을 DataFrame 형식의 데이터로 읽어오는 방법과,
# DataFrame 형식의 데이터를 표형식으로 파일로 저장할 수 있는 방법을 제공한다.
#  Pandas로 CSV(Comma Separated Value)파일 저장
# DataFrame.to_csv( filename, encoding=‘utf8’ )
# filename은 csv 파일 저장 경로를 포함 할 수 있다. (상대경로, 젃대경로)
# 인코딩 방식을 지정하지 않으면, 인코딩 방식은 utf-8 이 된다.

# 몸무게, 키 정보를 가진 데이터 프레임 생성
df_wh = pd.DataFrame({'weight':[62, 67, 55, 74],
                      'height':[165,177,160,180]},
                     index=['id_1','id_2','id_3','id_4'])
print(df_wh)
#       weight  height
# id_1      62     165
# id_2      67     177
# id_3      55     160
# id_4      74     180

# 인덱스 name의 컬럼 설정
df_wh.index.name = 'user'
print(df_wh)
#       weight  height
# user
# id_1      62     165
# id_2      67     177
# id_3      55     160
# id_4      74     180

# 체질량 지수(BMI) = W / H * H
bmi = df_wh['weight'] / (df_wh['height']/100)**2
print(bmi)
# user
# id_1    22.773186
# id_2    21.385936
# id_3    21.484375
# id_4    22.839506

# bmi 정보를 df_wh 데이터프레임에 추가
df_wh['bmi'] = bmi

# df_wh 데이터프레임 출력
print(df_wh)
#        weight   height   bmi
# user
# id_1      62     165  22.773186
# id_2      67     177  21.385936
# id_3      55     160  21.484375
# id_4      74     180  22.839506

# df_wh 데이터프레임을 bmi.csv 파일로 저장
df_wh.to_csv('bmi.csv', encoding='utf8')


