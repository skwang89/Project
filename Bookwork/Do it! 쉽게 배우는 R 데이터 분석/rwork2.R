# rwork2.R start

# <<교재 3장 시작>>

# 여러 값으로 구성된 변수 만들기
var1 <- c(1,2,5,7,8)
var1
# [1] 1 2 5 7 8

var2 <- c(1:5)
var2
# [1] 1 2 3 4 5

var2 <- 1:5
var2
# [1] 1 2 3 4 5

# seq() 함수
var3 <- seq(1, 5)
var3
# [1] 1 2 3 4 5

var4 <- seq(1, 10, by=2)
var4
# [1] 1 2 3 4 5

var5 <- seq(1, 10, by=3)
var5

# [1]  1  4  7 10

# 문자로된 변수 만들기
str1 <- "a"
str1
# [1] "a"

str2 <- "text"
str2
# [1] "text"

str3 <- "Hello World~!!"
str3
# [1] "Hello World~!!"

# 연속 문자 변수 만들기
str4 <- c('a','b','c')
str4
# [1] "a" "b" "c"

str5 <- c('Hello','World','is','good')
str5
# [1] "Hello" "World" "is"    "good" 

# 문자형 변수는 산술연살을 할 수 없다.
str1 + 2    # 오류발생생
# Error in str1 + 2 : 이항연산자에 수치가 아닌 인수입니다

# 통계 분석 함수
x <- c(1,2,3)
x

# 평균
mean(x)
# [1] 2

# 최대값
max(x)
# [1] 3

# 최소값
min(x)
# [1] 1


# 문자 처리 함수
# paste(): 문자들을 합쳐주는 역할

str5
# [1] "Hello" "World" "is"    "good" 
paste(str5, collapse = ",")   # 쉼표(,)로 문자들을 결합합
# [1] "Hello,World,is,good"
paste(str5, collapse = " ")   # 공백으로 문자들을 결합
# [1] "Hello World is good"

# 패키지(package)
# 패키지 = 함수 + 데이터셋

# ggplot2 패키지 설치 및 로딩
install.packages('ggplot2')   # ggplot2 패키지 설치치

library(ggplot2)              # ggplot2 패키지 로딩

#  여러 문자로 구성된 변수 생성
x <- c('a','a','b','c')
x

# 빈도 막대 그래프
qplot(x)

# ggplot2에 내장된 자동차 연비 정보를 가진 데이터셋
mpg

# ggplot2의 mpg 데이터로 그래프 그리기
# data에 mpg, x축은 hwy(고속도로 연비)
qplot(data=mpg, x=hwy)

# qplot() 파라미터 바꿔보기 
# data에 mpg, x축은 cty(도시연비)
qplot(data=mpg, x=cty)

# data에 mpg, x축 drv, y축 hwy
qplot(data = mpg, x=drv, y=hwy)

# x축 drv, y축 hwy, 선 그래프 형태
qplot(data=mpg, x=drv, y=hwy, geom="line")

# x축 drv, y축 hwy, 상자 그림 형태
qplot(data=mpg, x=drv, y=hwy, geom = "boxplot")

# x축 drv, y축 hwy, 상자 그림 형태, drv별 색 표현
qplot(data=mpg, x=drv, y=hwy, geom = "boxplot", colour=drv)
qplot(data=mpg, x=drv, y=hwy, geom = "boxplot", color=drv)

# 함수 기능이 궁금할 때 
?qplot

# ================================================================
#   혼자서 해보기
# Q1. 시험 점수 변수 만들고 출력하기
# 다섯 명의 학생이 시험을 봤습니다. 학생 다섯 명의 시험 점수를 
# 담고 있는 변수를 만들어 출력해 보세요. 각
# 학생의 시험 점수는 다음과 같습니다.
# 80, 60, 70, 50, 90
score <- c(80,60,70,50,90)
score
# [1] 80 60 70 50 90

# Q2. 전체 평균 구하기
# 앞 문제에서 만든 변수를 이용해서 이 학생들의 전체 평균 점수를 구해보세요.
mean(score)
# [1] 70

# Q3. 전체 평균 변수 만들고 출력하기
# 전체 평균 점수를 담고 있는 새 변수를 만들어 출력해 보세요. 
# 앞 문제를 풀 때 사용한 코드를 응용하면 됩니다.
avg <- mean(score)
avg  
# [1] 70

# <<교재 3장 끝>>


# <<교재 4장 시작>>
# 데이터 프레임 만들기
# 데이터 프레임: 행과 열을 가진 2차원 표

# 1. 영어 점수 변수 생성
english <- c(90,80,60,70)
english
# [1] 90 80 60 70

# 2 수학 점수 변수 생성
math <- c(50,60,100,20)
math
# [1]  50  60 100  20

# 3. 데이터 프레임 생성
df_midterm <- data.frame(english, math)
df_midterm
#   english math
# 1      90   50
# 2      80   60
# 3      60  100
# 4      70   20

# 4. 반(클래스) 변수 생성
class <- c(1,1,2,2)
class
# [1] 1 1 2 2

# 5. 3개의 변수를 이용해서 데이터 프레임 생성
df_midterm <- data.frame(english, math, class)
df_midterm
#   english math class
# 1      90   50     1
# 2      80   60     1
# 3      60  100     2
# 4      70   20     2

# 6.english 점수의 평균값
df_midterm$english
# [1] 90 80 60 70
mean(df_midterm$english)
#[1] 75

# 7.math 점수의 평균값
df_midterm$math
# [1]  50  60 100  20
mean(df_midterm$math)
# [1] 57.5

# 데이터 프레임 한 번에 만들기
df_midterm <- data.frame(english = c(90,80,60,70),
                         math = c(50,60,100,20),
                         class = c(1,1,2,2))
df_midterm
#   english math class
# 1      90   50     1
# 2      80   60     1
# 3      60  100     2
# 4      70   20     2

# ================================================================
#   혼자서 해보기
# #Q1. data.frame()과 c()를 조합해서 표의 내용을 
# 데이터 프레임으로 만들어 출력해보세요.
# 제품 가격 판매량
# 사과 1800 24
# 딸기 1500 38
# 수박 3000 13
fruits <- data.frame(제품 = c('사과','딸기','수박'),
                       가격 = c(1800, 1500, 3000),
                       판매량 = c(24, 38, 13))
fruits
#   제품 가격 판매량
# 1 사과 1800     24
# 2 딸기 1500     38
# 3 수박 3000     13

# Q2. 앞에서 만든 데이터 프레임을 이용해서 
# 과일 가격 평균, 판매량 평균을 구해보세요.
mean(fruits$가격)
# [1] 2100
mean(fruits$판매량)
# [1] 25

# 외부 데이터 이용하기
# readxl 패키지 설치
install.packages("readxl")
library(readxl)
















































