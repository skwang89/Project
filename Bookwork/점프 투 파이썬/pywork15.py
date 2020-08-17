# pywork15.py start
# <<강의 복습 8. 시작>>


# numpy
# 1. numpy는 Numerical Python의 줄임말로 고성능의 과학계산 컴퓨팅과 데이터
# 분석에 필요핚 패키지.
# 2. numpy 는 수치 계산을 효율적으로 하기 위핚 모듈로서, 다차원 배열과
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











































all = [var for var in globals() if var[0] != "-"]
for var in all:
    del globals()[var]
del(all)
dae(var)

import sys
sys.modules[__name__].__dict__.clear()


# <<강의 복습 8. 끝>>
# pywork15.py end