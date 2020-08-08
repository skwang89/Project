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
# ================================================================

# <<교재 3장 끝>>
# rwork2.R end
