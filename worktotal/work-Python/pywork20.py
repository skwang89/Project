# Scikit-Learn
# 사이킷런에 내장된 예제 데이터
# 사이킷런에는 별도의 외부 웹사이트에서 데이터 세트를 다욲로드 받을 필요
# 없이 예제로 활용할 수 있는 간단하면서도 좋은 데이터 세트가 내장되어 있다.
# 이 데이터는 datasets 모듈에 있는 여러 API를 호출해 만들 수 있다.
#
# <분류나 회귀 연습용 예제 데이터>
# API명                            설명
# datasets.load_digits()          분류용, 0에서 9까지 숫자 이미지 픽셀 데이터셋
# datasets.load_iris()            분류용, 붓꽃에 대한 피처를 가짂 데이터셋
# datasets.load_breast_cancer()   분류용, 위스콘신 유방암 피처들과 악성/음성 레이블
# datasets.load_boston()          회귀용, 미국 보스톤 집 피처들과 가격 데이터셋
# datasets.load_diabetes()        회귀용, 당뇨 데이터셋

# 회귀분석
# 머신러닝(Machine Learning)은 인공지능의 한 분야로 기계 스스로 대량의
# 데이터로부터 지식이나 패턴을 찾아 학습하고 예측하는 알고리즘 기법을
# 통칭한다.
#
# < 예측 알고리즘 >
# Types           Tasks           Algorithms
# ----------------------------------------------------------------
# 지도 학습        예측             Linear Regression
# (Supervised     (Prediction)    SVM : Support Vector Machine
# Learning)                       Random Forest
#                                 KNN : K Nearest Neighbor

# 회귀 분석 분류
#  독립변수의 개수로 분류
#
# 1. 단순 회귀 분석(Simple Linear Regression)
# 독립변수가 1개인 회귀 분석 방법
# y = ax + b # a : 회귀계수(기울기), b : 절편, x : 독립변수
#
# 2. 다중 회귀 분석(Mulple Linear Regression)
# 독립변수가 2개 이상인 회귀 분석 방법
# y = ax1 + bx2 + cx3 + d # 독립변수 : x1, x2, x3

# 회귀 분석 분류
# 일반적으로 소득이 증가하면 소비가 증가하는 것처럼, 어떤 변수 (독립변수 X)가
# 다른변수(종속변수 Y)에 영향을 준다면 두 변수 사이에 선형 관계가 있다고 말한다.
# 이와 같은 선형관계를 알고 있다면 새로욲 독립변수 X값이 주어졌을 때 거기에
# 대응하는 종속변수 Y값을 예측할 수 있다.
# 이처럼 두 변수 사이에 일대일로 대응되는 확률적, 통계적 상관성을 찾는 알고리즘을
# 단순회귀분석(Simple Linear Regression)이라고 말한다.
# 단순회귀분석을 대표적인 지도학습의 유형이다.

# 수학적으로 종속 변수 Y와 독립 변수 X 사이의 관계를 1차함수 Y = aX + b로 나타낸다.
# 단순회귀분석 알고리즘은 훈련 데이터를 이용하여 직선의 기욳기(a)와 직선이
# y축과 교차하는 지점인 y절편(b)을 반복 학습을 통해서 찾는다.
# 일차 방정식의 계수 a(기울기)와 b(절편)를 찾는 과정이 단순회귀분석 알고리즘이다.

# 최소 제곱법(Method of Least Squares)
#  scikit-learn 에서 최소 제곱법 구현 방법
# linear_model . LinearRegression()

# 단순선형 회귀 예제
# y = ax + b 처럼 데이터를 만들어 회귀문제를 풀어 보자.
# 여기서는 y = 3x – 2 인 경우에 최소 제곱법으로 기울기와 절편을 구해보자?
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# 학습 데이터 생성
x = np.random.rand(100, 1)  # 0 ~ 1까지 난수 100개 생성
# print(x)
x = x * 4 -2             # -2 <= x <=2
y = 3 * x - 2            # 회귀식

# 모델 생성: 최소제곱법이 적용되어 있음
model = linear_model.LinearRegression()

# 모델 학습
model.fit(x, y)

# 회귀계수(기울기), 절편
print('기울기:', model.coef_)          # 3.0
print('절편:', model.intercept_)       # -2.0

# 산점도 그래프
plt.scatter(x, model.predict(x), marker='o')    # 예측
plt.scatter(x, y, marker='+')                   # 실제값(=관측값)
plt.show()

# 단순선형 회귀 예제
# y = ax + b 처럼 데이터를 만들어 회귀문제를 풀어 보자.
# 여기서는 y = 3x – 2에 정규분포 난수를 더했을때, 최소 제곱법으로 기울기와 절편을
# 예측해 보자.
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# 학습 데이터 생성
x = np.random.rand(100, 1)  # 0 ~ 1사이의 난수 100개 생성
x = x*4-2
y = 3*x-2       # 회귀식

# 표준 정규분포 난수(평균:0, 표준편차:1) 난수 추가
y += np.random.rand(100, 1)

# 모델 생성
model = linear_model.LinearRegression()

# 모델 학습
model.fit(x, y)

# 회귀계수(기울기), 절편
print('기울기:', model.coef_)         # 기울기: [[2.987655]]
print('절편:', model.intercept_)     # 절편: [-1.5318569]

# 결정계수
r2 = model.score(x, y)
print('결정계수:', r2)               # 결정계수: 0.9927507988078351

# 산점도 그래프로 출력
plt.scatter(x, y, marker='+')                   # 실제값(관측값)
plt.scatter(x, model.predict(x), marker='o')    # 예측값
plt.show()

# 결정계수 (R**2)
#  회귀 결과의 타당성을 객관적으로 평가하는 지표로 결정계수를 사용한다.
#  결정계수가 0 에 가까욳 수록 예측 성능이 좋지 않고,
# 1 에 가까울 수록 예측 성능이 좋다고 할 수 있다.
#  scikit-learn 에서 결정계수는 model.score() 함수로 구할 수 있다.

# 단순선형 회귀 예제 : 결정계수
# y = ax + b 처럼 데이터를 만들어 회귀문제를 풀어 보자.
# 여기서는 y = 3x – 2에 정규분포 난수를 더했을때, 최소 제곱법으로 기울기와 절편을
# 예측해 보자.
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# 학습 데이터 생성
x = np.random.rand(100, 1)  # 0 ~ 1 사이의 난수 100개 생성
x = x*4 -2       # -2 <= x <= 2
y = 3*x**2 -2   # 회귀식  y = 3x^2 -2

# 표준정규분포(평균:0, 표준편차:1) 난수 추가
y += np.random.rand(100, 1)

# 모델 생성
model = linear_model.LinearRegression()

# 모델 학습
model.fit(x**2, y)

# 회귀계수(기울기), 절펹, 결정계수
print('기울기:', model.coef_)               # 기울기: [[2.99431121]]
print('절편:', model.intercept_)            # 절편: [-1.46210643]
print('결정계수:', model.score(x**2, y))    # 결정계수: 0.9986616451071157

# 산점도 그래프 출력
plt.scatter(x, y, marker='+')                       # 실제값(관측값)
plt.scatter(x, model.predict(x**2), marker='o')     # 예측값
plt.show()

# 다중 선형 회귀 예제
# y = ax1 + bx2 + c 형태의 데이터를 만들어 회귀문제를 풀어 보자.
# 여기서는 y = 3x1 – 2x2 + 1 에 정규분포 난수를 더했을때, 최소 제곱법으로 회귀계수와 절편을
# 예측해 보자.
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# 학습 데이터 생성
x1 = np.random.rand(100, 1)     # 0~1 사이의 난수 100개 생성
x1 = x1 * 4 - 2                 # -2 <= x1 <= 2
x2 = np.random.rand(100, 1)     # 0~1 사이의 난수 100개 생성
x = x2 * 4 - 2                  # -2 <= x2 <= 2
y = 3 * x1 - 2 * x2 + 1         # 회귀식

# 표준정규분포 난수 추가
y += np.random.randn(100, 1)

# x1, x2를 행렬로 변환
x1_x2 = np.c_[x1, x2]

# 모델 생성
model = linear_model.LinearRegression()

# 모델 학습
model.fit(x1_x2, y)

# 회귀계수(기울기), 절펹, 결정계수
print('기울기:', model.coef_)              # 기울기: [[ 2.88031101 -0.85384519]]
print('절편:', model.intercept_)           # 절편: [0.50146622]
print('결정계수:', model.score(x1_x2, y))  # 결정계수: 0.8973148729036522

# 산점도
y_ = model.predict(x1_x2)                   # 회귀식으로 예측
plt.subplot(1, 2, 1)                        # 1행 2열 배치 , 1번째 subplot
plt.scatter(x1, y, marker='+')
plt.scatter(x1, y_, marker='o')
plt.xlabel('x1')
plt.ylabel('y')

plt.subplot(1, 2, 2)                        # 1행 2열 배치 , 2번째 subplot
plt.scatter(x2, y, marker='+')
plt.scatter(x2, y_, marker='o')
plt.xlabel('x2')
plt.ylabel('y')
plt.tight_layout()                          # 자동으로 레이아웃을 설정해주는 함수
plt.show()

# 보스턴 주택가격 회귀분석
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston

# 보스턴 데이터 불러오기
boston = load_boston()
print(boston)

# boston 데이터를 읽어와서 데이터 프레임 생성
bostonDF = pd.DataFrame(boston.data, columns=boston.feature_names)
# print(bostonDF)       # [506 rows x 13 columns]
#     CRIM    ZN  INDUS  CHAS    NOX  ...  RAD    TAX  PTRATIO       B  LSTAT
# 0    0.00632  18.0   2.31   0.0  0.538  ...  1.0  296.0     15.3  396.90   4.98
# 1    0.02731   0.0   7.07   0.0  0.469  ...  2.0  242.0     17.8  396.90   9.14

# boston 데이터셋의 targer열(컬럼) 추가
bostonDF['PRICE'] = boston.target

# 열 추가 확인
print(bostonDF.shape)           # (506, 14)
print(bostonDF.head())          # [5 rows x 14 columns]
#      CRIM    ZN  INDUS  CHAS    NOX  ...    TAX  PTRATIO       B  LSTAT  PRICE
# 0  0.00632  18.0   2.31   0.0  0.538  ...  296.0     15.3  396.90   4.98   24.0
# 1  0.02731   0.0   7.07   0.0  0.469  ...  242.0     17.8  396.90   9.14   21.6
# 2  0.02729   0.0   7.07   0.0  0.469  ...  242.0     17.8  392.83   4.03   34.7
# 3  0.03237   0.0   2.18   0.0  0.458  ...  222.0     18.7  394.63   2.94   33.4
# 4  0.06905   0.0   2.18   0.0  0.458  ...  222.0     18.7  396.90   5.33   36.2

# 2개의 행과 4개의 열을 가진 subplots 로 시각화, axs는 4x2개의 ax를 가짐
fig, axs = plt.subplots(figsize=(12, 8), ncols=4, nrows=2)
lm_features = ['RM', 'ZN', 'INDUS', 'NOX', 'AGE', 'PTRATIO', 'LSTAT', 'RAD']

for i, feature in enumerate(lm_features):
    row = int(i/4)
    col = i%4
    # 시본(seaborn)의 regplot을 이용해 산점도와 선형 회귀선을 출력
    sns.regplot(x=feature, y='PRICE', data=bostonDF, ax=axs[row][col])
plt.show()

# RM(방개수)와 LSTAT(하위 계층의 비율)이 PRICE에 영향도가 가장 두드러지게 나타남.
# 1. RM(방개수)은 양 방향의 선형성(Positive Linearity)이 가장 크다.
# 방의 개수가 많을수록 가격이 증가하는 모습을 확연히 보여준다.
# 2. LSTAT(하위 계층의 비율)는 음 방향의 선형성(Negative Linearity)이 가장 크다.
# 하위 계층의 비율이 낮을수록 PRICE 가 증가하는 모습을 확연히 보여준다.

# LinearRegression 클래스를 이용해서 보스턴 주택 가격의 회귀 모델을 만들어 보자
# train_test_split()을 이용해 학습과 테스트 데이터셋을 분리해서 학습과 예측을 수행한다.
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 데이터 프레임에서 'PRICE' 컬럼을 삭제한 나머지 데이터를 반환
y_target = bostonDF['PRICE']
x_data = bostonDF.drop(['PRICE'], axis=1, inplace=False)

# train data와 test data를 분할(7:3 비율)
x_train, x_test, y_train, y_test = train_test_split(x_data,
                                                    y_target,
                                                    test_size=0.3,
                                                    random_state=1)

# 선형회귀 모델생성 / 모델학습 / 모델예측 / 모델평가 수행
# 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x_train, y_train)

# 모델 예측
y_predict = model.predict(x_test)

# 모델 성능 평가
print('결정계수:', r2_score(y_test, y_predict))     # 결정계수: 0.7836295385076268

# LinearRegression 으로 생성한 주택가격 모델의 회귀계수(coefficients)와
# 절편(intercept)을 구해보자
print('회귀계수(기울기):', np.round(model.coef_, 1))
print('절편:', model.intercept_)
# 회귀계수(기울기): [ -0.1   0.1   0.1   2.4 -21.5   2.8   0.
#                           -1.5   0.3  -0.   -1.    0.  -0.6]
# 절편: 46.39649387182395

# 회귀계수가 큰 값 순으로 내림차순 정렬
coff = pd.Series(data=np.round(model.coef_, 1), index=x_data.columns)
print(coff.sort_values(ascending=False))
# RM          2.8
# CHAS        2.4
# RAD         0.3
# INDUS       0.1
# ZN          0.1
# B           0.0
# TAX        -0.0
# AGE         0.0
# CRIM       -0.1
# LSTAT      -0.6
# PTRATIO    -1.0
# DIS        -1.5
# NOX       -21.5
# dtype: float64

# 결과
#  RM(방개수)와 LSTAT(하위 계층의 비율)이 PRICE에 영향도가 가장 두드러지게 나타남.
#  RM(방개수)은 양 방향의 선형성(Positive Linearity)이 가장 크다.
#       방의 개수가 많을수록 가격이 증가하는 모습을 확연히 보여준다.
#  LSTAT(하위 계층의 비율)는 음 방향의 선형성(Negative Linearity)이 가장 크다.
# 하위 계층의 비율이 낮을수록 PRICE 가 증가하는 모습을 확연히 보여준다.

# UCI(University of California, Irvine) 자동차 연비 데이터셋으로
#  단순회귀분석을 해보자
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# auto-map.csv 파일 읽어오기
df = pd.read_csv('data/auto-mpg.csv', header=None)
print(df)           # 컬럼 번호로 출력 ( 0 ~ 8 ) # [398 rows x 9 columns]

# 행, 열 데이터 모두 출력
pd.set_option('display.max_rows', 398)
pd.set_option('display.max_columns', 9)
# print(df)

# 컬럼번호 대신에 컬럼 이름 설정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print(df.head())

# 데이터의 자료형
print(df.info())        # horsepower  object(문자형)

# 통계적인 정보 확인
print(df.describe())    # horsepower컬럼 object(문자형) 출력안됨

# horsepower 열의 고유값 확인
print(df['horsepower'].unique())
# ['130.0' '165.0' '150.0' '140.0' '198.0' '220.0' '215.0' '225.0' '190.0'
#  '170.0' '160.0' '95.00' '97.00' '85.00' '88.00' '46.00' '87.00' '90.00'
#  '113.0' '200.0' '210.0' '193.0' '?' '100.0' '105.0' '175.0' '153.0'
#  '180.0' '110.0' '72.00' '86.00' '70.00' '76.00' '65.00' '69.00' '60.00'
#  '80.00' '54.00' '208.0' '155.0' '112.0' '92.00' '145.0' '137.0' '158.0'
#  '167.0' '94.00' '107.0' '230.0' '49.00' '75.00' '91.00' '122.0' '67.00'
#  '83.00' '78.00' '52.00' '61.00' '93.00' '148.0' '129.0' '96.00' '71.00'
#  '98.00' '115.0' '53.00' '81.00' '79.00' '120.0' '152.0' '102.0' '108.0'
#  '68.00' '58.00' '149.0' '89.00' '63.00' '48.00' '66.00' '139.0' '103.0'
#  '125.0' '133.0' '138.0' '135.0' '142.0' '77.00' '62.00' '132.0' '84.00'
#  '64.00' '74.00' '116.0' '82.00']

# horsepower 데이터 수정
df['horsepower'].replace('?', np.nan, inplace=True)     # '?'를 np.nan 치환
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')     # 문자형을 살수형으로 변환
print(df.describe())

# 분석에 필요한 열을 구해온다 (연비, 실린더, 출력, 중량)
ndf = df[['mpg','cylinders','horsepower','weight']]
print(ndf.head())

# 독립변수(x) weight(중량)dhk 종속변수(y)인 mpg(연비) 간의 선형관게를 산점도 그래프로 확인
# 1. matplotlib로 산점도 그리기
ndf.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10, 5))
plt.show()
plt.close()

# 2. seaborn으로 산점도 그리기
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1)      # 1행 2열 첫번째 그래프
ax2 = fig.add_subplot(1, 2, 2)      # 1행 2열 두번쨰 그래프
sns.regplot(x='weight', y='mpg', data=ndf, ax= ax1, fit_reg=True)   # 회귀선 표시
sns.regplot(x='weight', y='mpg', data=ndf, ax= ax2, fit_reg=False)   # 회귀선 표시
plt.show()
plt.close()

# 3. seaborn 조인트 그래프 - 산점도, 히스토그램
sns.jointplot(x='weight', y='mpg', data=ndf)                # 회귀선 없음
sns.jointplot(x='weight', y='mpg', kind='reg', data=ndf)    # 회귀선 표시
plt.show()
plt.close()

# 4.seaborn pariplot으로 두 변수 간의 모든 경우의 수 그리기
sns.pairplot(ndf)
plt.show()
plt.close()

# 독립변수, 종속변수
x = ndf[['weight']]     # 중량
y = ndf[['mpg']]        # 연비

# train data와 test data를 분할(7:3 비율)
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,              # 독립변수
                                                    y,              # 종속변수
                                                    test_size=0.3,  # 테스트 데이터 30%
                                                    random_state=1)
print('train data 갯수:', len(x_train))       # train data 갯수: 274
print('test data 갯수:', len(x_test))         # test data 갯수: 118

from sklearn.linear_model import LinearRegression

# 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x_train, y_train)

# 모델 성능 평가
print('결정계수:', model.score(x_test, y_test))     # 결정계수: 0.7165757749167567

# 회귀계수(기울기), 절편
print('회귀계수(기울기):', model.coef_)        # 회귀계수(기울기): [[-0.00744855]]
print('절편:', model.intercept_)              # 절편: [45.43576662]

# 예측
y_hat = model.predict(x)

plt.figure(figsize=(10, 5))
ax1 = sns.distplot(y, hist=False, label='y')                    # 실제값
ax2 = sns.distplot(y_hat, hist=False, label='y_hat', ax=ax1)    # 예측값
plt.show()

# <모델이 예측한 값(y_hat)와 실제 값(y) 비교 결과>
# 출력된 결과를 보면 실제 값은 왼쪽으로 편향되어 있고, 예측값은 반대로 오른쪽으로
# 편중되는 경향을 보인다. 따라서 독립변수(weight)와 종속변수(mpg) 사이에 선형관계가
# 있지만, 모델의 오차를 더 줄일 필요가 있어 보인다.

# 다항회귀분석(Polynomial Regression)
# 단순회귀분석은 두 변수 갂의 관계를 직선 형태로 설명하는 알고리즘이다.
# 독립변수 x와 종속변수 y 사이에 선형의 상관관계가 있지만, 직선보다는
# 곡선으로 설명하는 것이 적합할 때는 단순회귀분석은 부적합하다.
# 이를 경우에 다항 함수를 사용하면 보다 복잡한 곡선 형태의 회귀선을 표현 할 수 있다.

# 다항회귀분석(Polynomial Regression)은 2차함수 이상의 다항 함수를 이용
# 하여 두 변수 사이의 선형관계를 설명하는 알고리즘이다.

# 예를 들면, 2차함수는 종속변수 y와 독립변수 x사이의 관계를
# y = ax^2 + bx + c 로 표시하여 설명한다.
# 다항회귀분석 모형은 학습을 통해서 3개의 계수 a, b, c 를 찾아서 모델을 만든다.

# 다항 회귀분석
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

# 데이터 파일 불러오기
df = pd.read_csv('data/auto-mpg.csv', header=None)
print(df)           # [398 rows x 9 columns]

# 행, 열 데이터 모두 출력
pd.set_option('display.max_rows', 398)
pd.set_option('display.max_columns', 9)

# 열(컬럼)이름 설정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','orgin','name']
print(df.head())

# 데이터의 자료형
print(df.info())            # horsepower  object(문자형)

# 통계적이 정보 확인
print(df.describe())        # horsepower컬럼 object(문자형) 출력안됨

# horsepower 열의 고유값 확인
print(df['horsepower'].unique())

# horsepower 데이터 수정
df['horsepower'].replace('?', np.nan, inplace=True)    # '?'를 np.nan 치환
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')   # 문자형을 실수형으로 변환

print(df.describe())

# 분석에 필요한 정보 추출 (연비, 실린더, 출력, 중량)
ndf = df[['mpg','cylinders','horsepower','weight']]

# 독립변수(weight), 종속변수(mpg)
x = ndf[['weight']]
y = ndf[['mpg']]

from sklearn.model_selection import train_test_split

# train data와 test data 분할(7:3 비율)
x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.3, # test data : 30%
                                                    random_state=1)
print('훈련 데이터:', x_train.shape)             # 훈련 데이터: (274, 1)
print('테스트 데이터:', x_test.shape)            # 테스트 데이터: (118, 1)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures    # 다항식 변환

# 다항식 변환
poly = PolynomialFeatures(degree=2)     # 2차항
x_train_poly = poly.fit_transform(x_train)
print(x_train_poly)

print('훈련 데이터:', x_train.shape)                # 훈련 데이터: (274, 1)
print('2차항 변환 데이터:', x_train_poly.shape)      # 2차항 변환 데이터: (274, 3)

# 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x_train_poly, y_train)

# 결정 계수
x_test_poly = poly.fit_transform(x_test)
r_square = model.score(x_test_poly, y_test)
print('결정계수:', r_square)            # 결정계수: 0.7443148755056594

# 예측
y_hat_test = model.predict(x_test_poly)

# 선점도 그래프 출력
fig = plt.figure(figsize=(10, 5))      # 그래프 크기 설정
ax = fig.add_subplot(1, 1, 1,)
ax.plot(x_train, y_train, 'o', label='Train Data')
ax.plot(x_test, y_hat_test, 'r+', label='Predicted Value')
ax.legend(loc='best')
plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()

# 실제값과 예측값의 분포 차이 비교
x_poly = poly.fit_transform(x)      # x 데이터를 2차항으로 변환
y_hat = model.predict(x_poly)

# displot(): 히스토그램 + 커널밀도 함수
plt.figure(figsize=(10, 5))
ax1 = sns.distplot(y, hist=False, label='y')                    # 실제값
ax2 = sns.distplot(y_hat, hist=False, label='y_hat', ax=ax1)    # 예측값

# 다중회귀분석(Multivariate Regression)
# 단순회귀분석은 소득이 증가하면 소비도 증가하는 것처럼 종속변수에 y에 영향을
# 주는 독립변수가 x가 하나인 경우를 말한다. 하지만 소비에 영향을 주는 독립변수에는
# 소득 외에도 자녀의 수, 거주지, 직업 등 다른 요인이 있을 수 있다.
# 이처럼 여러 개의 독립변수가 종속 변수에 영향을 주고 선형 관계를 갖는 경우에
# 다중회귀분석(Multivariate Regression)을 사용핚다.
# 수학적으로 종속변수 y와 독립변수 x간의 관계를 Y = b + a1X1 + a2X2+.....+anXn 와
# 같은 함수식으로 표현핚다.
# 다중회귀분석 알고리즘은 각 독립 변수의 계수(a1, a2,.... an) 와 상수항(b)에 적절한
# 값들을 찾아서 모델을 완성한다.
# 모델의 예측값인 종속 변수에 대한 실제 데이터를 알고 있는 상태에서 학습하기 때문에
# 지도학습으로 분류된다.

# 다중 회귀분석
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
df = pd.read_csv('auto-mpg.csv', header=None)
print(df)           # [398 rows x 9 columns]

# 행, 열 데이터 모두 출력
pd.set_option('display.max_rows', 398)
pd.set_option('display.max_columns', 9)

# 열(컬럼)이름 설정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','orgin','name']
print(df.head())

# 데이터의 자료형
print(df.info())            # horsepower  object(문자형)

# 통계적이 정보 확인
print(df.describe())        # horsepower컬럼 object(문자형) 출력안됨

# horsepower 열의 고유값 확인
print(df['horsepower'].unique())

# horsepower 데이터 수정
df['horsepower'].replace('?', np.nan, inplace=True)    # '?'를 np.nan 치환
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')   # 문자형을 실수형으로 변환

print(df.describe())

# 분석에 필요한 열을 구해오기 (연비, 실린더, 출력, 중량)
ndf = df[['mpg','cylinders','horsepower','weight']]

# 독립변수, 종속변수
x = ndf[['cylinders','horsepower','weight']]    # 독립변수
y = ndf[['mpg']]                                # 종속변수

from sklearn.model_selection import train_test_split

# train data와 test data 분할 (7:3 비율)
x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.3, # test data 30%
                                                    random_state=1)

from  sklearn.linear_model import LinearRegression

# 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(x_train, y_train)

# 모델 평가 : 결정계수
r_square = model.score(x_test, y_test)
print('결정계수:', r_square)            # 결정계수: 0.7306455170640521

# 회귀계수(기울기), 절편
print('회귀계수:', model.coef_)         # 회귀계수: [[-0.32960792 -0.04558883 -0.00507007]]
print('절편:', model.intercept_)        # 절편: [44.87421435]

# 예측
y_hat = model.predict(x_test)
print(y_hat)

# 모델이 예측한 값과 실제값을 그래프로 출력
# displot() : 히스토그램 + 커널밀도 함수
plt.figure(figsize=(10, 5))
ax1 = sns.distplot(y_test, hist=False, label='y_test')          # 실제값
ax2 = sns.distplot(y_hat, hist=False, label='y_hat', ax=ax1 )   # 예측값
plt.show()

