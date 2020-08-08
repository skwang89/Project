# rwork4.R start
# <<교재 5장 시작>>


# 데이터 파악하기: 데이터 탐색에 사용되는 함수

# 함수      기능
#----------------------------------------------------
# head()    데이터 앞부분 출력 : 앞에서 6행까지 출력 
# tail()    데이터 뒷부분 출력 : 뒤에서 6행까지 출력 
# View()    뷰어 창에서 데이터 확인
# dim()     데이터 차원 출력
# str()     데이터 속성 출력
# summary() 요약통계량 출력

# CSV 파일 불러오기
exam <- read.csv('data/csv_exam.csv')
exam    # 데이터 프레임

# 1. head()
#    : 앞에서부터 6행까지 데이터 출력
head(exam)      # 앞에서부터 6행까지데이터 출력
head(exam, 10)  # 앞에서부터 10행까지데이터 출력

# 2. tail()
#    : 뒤에서부터 6행까지 데이터 출력
tail(exam)      # 앞에서부터 6행까지데이터 출력
tail(exam, 10)  # 앞에서부터 10행까지데이터 출력

# 3. View()
#    : 뷰어 창에서 데이터 확인할 때 사용되는 함수
#      View()에 'V'는 대문자로 표기할 것
View(exam)

# 4. dim()
#    : 데이터의 차원을 구해주는 함수
#      행의 수와 열의 수를 구해주는 함수
dim(exam)
# [1] 20  5

# 5. str()
#    : 데이터의 속성을 확인할 때 사용되는 함수
str(exam)

# 6. summary()
#    : 통계 요약정보를 구해주는 함수
summary(exam)

# mpg 데이터 파악하기
# ggplot2 패키지 로딩
library(ggplot2)

# ggplot2의 mpg 데이터셋 불러오기
mpg <- as.data.frame(ggplot2::mpg)
mpg

head(mpg)      # 앞에서 6행까지 데이터 불러오기 
tail(mpg)      # 끝에서 6행까지 데이터 불러오기
View(mpg)      # View 창으로 출력 
str(mpg)       # 데이터 속성 확인 
dim(mpg)       # 데이터의 차원 
# [1] 234  11  # 234행  11열 
summary(mpg)   # 통계요약 정보 출력  

# 변수명 바꾸기
# dplyr 패키지: 전처리를 할때 많이 사용하는 패키지

# dplyr 패키지 설치
install.packages('dplyr')

# dplyr 패키지 로딩
library(dplyr)

# 1. 데이터 프레임 생성
df_raw <- data.frame(var1=c(1,2,1),
                     var2=c(2,3,2))
df_raw
#   var1 var2
# 1    1    2
# 2    2    3
# 3    1    2

# 2. 복사본 데이터 프레임 생성
df_new <- df_raw
df_new
#   var1 var2
# 1    1    2
# 2    2    3
# 3    1    2

# 3. 변수명 변경
#    :rename() 함수를 이용해서 변수명을 수정

# var2 변수명을 v2로 변경
df_new <- rename(df_new, v2 = var2)
df_new


# ================================================================
# 혼자서 해보기
# mpg 데이터의 변수명은 긴 단어를 짧게 줄인 축약어로 되어있습니다.
# cty 변수는 도시 연비, hwy 변수는
# 고속도로 연비를 의미합니다. 변수명을 이해하기 쉬운 단어로
# 바꾸려고 합니다. mpg 데이터를 이용해서
# 아래 문제를 해결해 보세요.
# • Q1. ggplot2 패키지의 mpg 데이터를 사용할 수 있도록 불러온 뒤
# 복사본을 만드세요.
mpg <- as.data.frame(ggplot2::mpg)
mpg_new <- mpg

# • Q2. 복사본 데이터를 이용해서 cty는 city로, hwy는 highway로
# 변수명을 수정하세요.
mpg_new <- rename(mpg_new, city=cty, highway=hwy)

# • Q3. 데이터 일부를 출력해서 변수명이 바뀌었는지 확인해 보세요.
# 아래와 같은 결과물이 출력되어야 합니다.
# ## manufacturer model displ year cyl trans drv city highway fl class
# ## 1 audi a4 1.8 1999 4 auto(l5) f 18 29 p compact
# ## 2 audi a4 1.8 1999 4 manual(m5) f 21 29 p compact
# ## 3 audi a4 2.0 2008 4 manual(m6) f 20 31 p compact
# ## 4 audi a4 2.0 2008 4 auto(av) f 21 30 p compact
# ## 5 audi a4 2.8 1999 6 auto(l5) f 16 26 p compact
# ## 6 audi a4 2.8 1999 6 manual(m5) f 18 26 p compact
head(mpg_new)
# ================================================================ 

# 파생변수 만들기: 기존 변수를 이용해서 새고 생성된 변수

# 1. 데이터 프레임 생성
df <- data.frame(var1=c(4,3,8),
                 var2=c(2,6,1))
df
#   var1 var2
# 1    4    2
# 2    3    6
# 3    8    1

# 2. 합을 구하는 파생변수 생성: var_sum
df$var_sum <- df$var1 + df$var2
df
#   var1 var2 var_sum
# 1    4    2       6
# 2    3    6       9
# 3    8    1       9

# 3. 평균을 구하는 파생변수 생성: var_mean
df$var_mean <- (df$var1 + df$var2)/2
df
#   var1 var2 var_sum var_mean
# 1    4    2       6      3.0
# 2    3    6       9      4.5
# 3    8    1       9      4.5


# mpg 통합 연비 변수 만들기
# ggplot2의 mpg 데이터를 데이터프레임 형태로 불러오기 
mpg <- as.data.frame(ggplot2::mpg)
head(mpg)
dim(mpg)
# 234  11
View(mpg)

# 파생 변수 : total = (cty(도시연비) + hwy(고속도로 연비)) /2
mpg$total <- (mpg$cty + mpg$hwy)/2    # 통합 연비
head(mpg)

# 평균 통합연비
mean(mpg$total)
# [1] 20.14957

# 통합연비(total)에 통계요약정보 구하기
summary(mpg$total)
# Min.   1st Qu.  Median    Mean  3rd Qu.    Max. 
# 10.50   15.50   20.50    20.15   23.50    39.50 

# 히스토그램
hist(mpg$total)

# 조건문을 이용해서 합격 판정하는 파생변수 생성: test
# ifelse(a,b,c) 구문
# x <- ifelse(조건식, b,c)
# 조건식이 참이면 b값을 x에 할당
# 조건식이 거짓이면 c값을 x에 할당

# total 값이 20이상이면 pass,
# total 값이 20미만이면 fail 값을 할당
mpg$test <- ifelse(mpg$total >=20, "pass",'fail')
head(mpg, 10)
View(mpg)


# test 변수에 저장돈 데이터(pass, fail)의 빈도 구하기
table(mpg$test)
# fail pass 
# 106  128 

# 빈도 막대 그래프
library(ggplot2)
qplot(mpg$test)

# total 변수의 값에 따른 연비 등급을 저장하는 파생변수 생성: grade
# 등급 total 기준
# A    30 이상
# B    20~29
# C    20 미만

# total을 기준으로 A, B, C 등급 부여
mpg$grade <- ifelse(mpg$total >=30, "A",
                    ifelse(mpg$total >=20, "B", "c"))
head(mpg)

# grade 변수에 저장된 데이터(A, B, C)의 빈도 구하기
table(mpg$grade)
# A   B   C 
# 10 118 106 

# 빈도 막대 그래프 그리기
qplot(mpg$grade)


# [정리하기]
# # 1.데이터 준비, 패키지 준비
# mpg <- as.data.frame(ggplot2::mpg) # 데이터 불러오기
# library(dplyr) # dplyr 로드
# library(ggplot2) # ggplot2 로드

# # 2.데이터 파악
# head(mpg) # Raw 데이터 앞부분
# tail(mpg) # Raw 데이터 뒷부분
# View(mpg) # Raw 데이터 뷰어창에서 확인
# dim(mpg) # 차원
# str(mpg) # 속성
# summary(mpg) # 요약 통계량

# # 3.변수명 수정
# mpg <- rename(mpg, company = manufacturer)

# # 4.파생변수 생성
# mpg$total <- (mpg$cty + mpg$hwy)/2 # 변수 조합
# mpg$test <- ifelse(mpg$total >= 20, "pass", "fail") # 조건문 활용

# # 5.빈도 확인
# table(mpg$test) # 빈도표 출력
# qplot(mpg$test) # 막대 그래프 생성

# ================================================================
# 분석 도전!
#   
#   ggplot2 패키지에는 미국 동북중부 437개 지역의 인구통계 정보를
# 담은 midwest라는 데이터가 포함되어 있습니다. 
# midwest 데이터를 사용해 데이터 분석 문제를 해결해보세요.
# • 문제 1. ggplot2 의 midwest 데이터를 데이터 프레임 형태로
# 불러와서 데이터의 특성을 파악하세요.
midwest <- as.data.frame(ggplot2::midwest)
head(midwest)
tail(midwest)
View(midwest)
dim(midwest)
str(midwest)
summary(midwest)

# • 문제 2. poptotal(전체 인구)을 total 로, popasian(아시아 인구)을
# asian 으로 변수명을 수정하세요.
library(dplyr)
midwest <- rename(midwest, total=poptotal, asian=popasian)
View(midwest)

# • 문제 3. total, asian 변수를 이용해 '전체 인구 대비 
# 아시아 인구 백분율' 파생변수를 만들고, 히스토그램을
# 만들어 도시들이 어떻게 분포하는지 살펴보세요.
midwest$allperasian <- midwest$asian/midwest$total*100
hist(midwest$allperasian)

# • 문제 4. 아시아 인구 백분율 전체 평균을 구하고, 평균을 초과하면
# "large", 그 외에는 "small"을 부여하는 파생변수를 만들어 보세요.
mean(midwest$allperasian)
# [1] 0.4872462
midwest$LS <- ifelse(midwest$allperasian > 0.4872462, "large", "small")

# • 문제 5. "large"와 "small"에 해당하는 지역이 얼마나 되는지,
# 빈도표와 빈도 막대 그래프를 만들어 확인해 보세요.
table(midwest$LS)
# large small 
# 119   318 
library(ggplot2)
qplot(midwest$LS)
# ================================================================


# <<교재 5장 끝>>
# rwork4.R end
