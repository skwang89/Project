# rwork2.R start

# 교재 3장

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






































































