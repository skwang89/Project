# rwork12.R start
# <<교재 13장 시작>>


# R을 활용한 평균, 중앙값, 분산, 표준편차 구하기
score <- c(85, 90, 93, 86, 82)
score

# 평균
mean(score)
# 87.2

# 중앙값
median(score)
# 86

# 분산: 편차제곱의 평균 
var(score)
# 18.7

# 표준편차 
sd(score)
# 4.32435

# 예. 5명 학생의 키, 몸무게
height <- c(168, 176, 167, 174, 169)
weight <- c(52,68,47,82,51)

#1. 학생들의 키의 평균
mean(height)
# 170.8

#2. 학생들의 몸무게의 평균
mean(weight)
# 60

#3. 학생들의 키의 표준편차
sd(height)
# 3.962323

#4. 학생들의 몸무게의 표준편차
sd(weight)
# 14.67992

#-------------------------------------------------------------------
# 상관 관계 분석

# 어떤 회사에서 신제품이 나왔을 때 안내메일(DM) 을 발송하는 회수와 
# 제품이 판매되는 것 사이에 어떤 관계가 있는지를 조사 했더니 
# 아래와 같은 결과가 나왔다고 합니다.
# 이들의 상관 계수를 구해 보세요.

# 제품 판매 개수(x) : 3 , 5 , 8 , 11 , 13
# DM 발송 회수(y) : 1 , 2 , 3 , 4 , 5
# 위 값에서 y 의 평균은 3 이고 x 의 평균은 8 입니다.

# 상관계수
# 사건 A와 사건 B 사이의 관련 정도를 숫자로 표현한 것.

# -1 <= r <= 1

x <- c(3, 5, 8, 11, 13)
y <- c(1, 2, 3, 4, 5)

# 상관계수 구하기
cor(x, y)
# 0.9970545

# DM 발송 횟수와 제품 판매 갯수 사이에는 밀접한 상관관계가 있다.

#--------------------------------------------------------------------
# 회귀분석
# : 어떤 결과값을 기준으로 다른 결과값을 예측하는 데이터 분석 방법 

# 회귀분석 방법
# 1. 선형 회귀분석 : 독립변수가 1개인 경우에 사용하는 분석 방법
# 2. 다중 회귀분석 : 독립변수가 2개 이상인 경우에 사용하는 분석 방법

# 선형회귀 분석

# 예
# 문제 1
# 부모의 두뇌 지수와 자녀의 두뇌지수를 조사핚 데이터를 분석해서 
# 회귀식을 구하고
# 부모의 IQ 가 117 일때 자녀의 IQ가 얼마나 될지 예측하시오 ?

# 부모의 IQ(x) : 110 , 120 , 130 , 140 , 150
# 자녀의 IQ(y) : 100 , 105 , 128 , 115 , 142


# R 프로그램으로 회귀 분석
x <- c(110, 120, 130, 140, 150)
y <- c(100, 105, 128, 115, 142)

# 회귀식 구하기 : y = 0.94 x - 4.20
line <- lm(y~x)
line
# Coefficients:
#   (Intercept)            x  
#          -4.20         0.94

# Q. 부모의 IQ가 117 일때 자녀의 IQ가 얼마일지 예측 ?
child_iq <-  (0.94 * 117 ) - 4.20 
child_iq
# 105.78

# 회귀식을 그래프로 출력
plot(x, y, pch=20, col="red")    # pch = 20 : 점의 모양

# 회귀선 출력
abline(line, col="blue")

#------------------------------------------------------------------
# 문제 2
# 아래 표는 학생별로 성적과 IQ , 학원수 , 게임하는 시간 , TV 시청시갂을 정리한 것인데 아래 표를 이용해서 성적과 IQ 갂의 회귀식을 구해서 IQ 가 125 인 사람의 성적을 예측해 보시오.

# R 프로그램으로 회귀 분석
score <- read.csv("data/score.txt", header = T, sep = ",")
attach(score)    # 한글로 된 열(변수)에 접근할수 있도록 해주는 역할 
score


# 회귀식 :   y = 0.6714 x  - 5.2918
lm1 <- lm(성적~IQ)
lm1
# Coefficients:
#   (Intercept)           IQ  
#        -5.2918       0.6714  

# Q. IQ가 125인 사람의 성적을 예측 하세요?
# 회귀식 :   y = 0.6714 x  - 5.2918 
y <- (0.6714 * 125 ) - 5.2918
y
# 78.6332           # 예상 점수 

# 그래프 출력
plot(IQ, 성적, pch=20, col="red")   # 산점도 
abline(lm1, col="blue")             # 회귀선 출력 

#----------------------------------------------------------------------
# 각 학생 별로 회귀식을 적용해서 IQ가 125 일 경우 받을 예상 점수 
# 구하기

# predict( ) 함수를 사용하여 아래처럼 예측값을 구핛 수도 있습니다.
predict(lm1,newdata=data.frame(x=c(125,125,125,125,125,125,125,125,125,125)))
# 1        2        3        4        5        6        7        8 
# 88.70224 78.63145 75.27451 85.34531 65.20372 77.28867 83.33115 71.91758 
# 9       10 
# 80.64560 82.65976

#------------------------------------------------------------------------
# 각 학생들이 학원을 5개 다닐 경우 예상 성적 구하기 
#  (다른 변수들은 바뀌지 않음)

# 회귀식 :  y =  4.953 x  + 69.488 
lm2 <- lm(성적~다니는학원수)
lm2
# Coefficients:
#   (Intercept)   다니는학원수  
#    69.488         4.953 

predict(lm2,newdata=data.frame(x=5))
# 1        2        3        4        5        6        7        8        9 
# 79.39535 74.44186 74.44186 79.39535 69.48837 84.34884 84.34884 74.44186 89.30233 
# 10 
# 79.39535 

#------------------------------------------------------------------------
# 다중 회귀 분석 : 독립변수가 2개 이상인 경우에 사용하는 분석 방법 

## 회귀식 구하기
lm3 <- lm(성적~IQ+다니는학원수+게임하는시간+TV시청시간)
lm3
# Coefficients:
#   (Intercept)     IQ      다니는학원수   게임하는시간    TV시청시간  
#    23.2992        0.4684  0.7179         -0.8390        -1.3854 

# 회귀식
# y(성적) = 23.2992 + 0.4684 x1 + 0.7179 x2 - 0.8390 x3- 1.3854 x4

# Q.IQ 가 130 (x1) 인 사람이 학원을 3개(x2) 다니고 게임을 2시간(x3) 하고 
#   TV를 1 시간(x4) 볼 경우 예상되는 성적은 얼마인가요?
y <- 23.2992 + (0.4684*130) + (0.7179 * 3) - (0.8390*2) - (1.3854*1)
y
# 83.2815       예상점수 


#--------------------------------------------------------------------------
# 기술 통계와 추론 통계

# • 기술 통계(Descriptive statistics)
# – 데이터를 요약해 설명하는 통계 기법
# – ex) 사람들이 받는 월급을 집계해 전체 월급 평균 구하기

# • 추론 통계(Inferential statistics)
# – 단순히 숫자를 요약하는 것을 넘어 어떤 값이 발생할 확률을 계산하는 
#   통계 기법
# – ex) 수집된 데이터에서 성별에 따라 월급에 차이가 있는 것으로 나타났을 때, #       이런 차이가 우연히 발생할 확률을 계산


# 통계적 가설 검정(Statistical hypothesis test)

# – 유의확률을 이용해 가설을 검정하는 방법
# • 유의확률(Significance probability, p-value)
# - 기준 : 5%, 0.05
# – 실제로는 집단 간 차이가 없는데 우연히 차이가 있는 데이터가 추출될 확률

# – 분석 결과 유의확률 보다 크게 나타났다면
# • '집단 간 차이가 통계적으로 유의하지 않다'고 해석
# • 실제로 차이가 없더라도 우연에 의해 이 정도의 차이가 관찰될 가능성이 
#   크다는 의미

# – 분석 결과 유의확률 보다 작게 나타났다면
# • '집단 간 차이가 통계적으로 유의하다'고 해석
# • 실제로 차이가 없는데 우연히 이 정도의 차이가 관찰될 가 능성이 작다, 
#   우연이라고 보기 힘들다는 의미

#------------------------------------------------------------------------
# t검정(t-test)
# : 두 집단의 평균에 통계적으로 유의한 차이가 있는지 알아볼때 사용하는
#   통계분석 방법

# compact 자동차와 suv 자동차의 도시 연비 t검정

# 데이터 준비하기
library(ggplot2)
mpg <- as.data.frame(ggplot2::mpg)
head(mpg)

# 전처리
library(dplyr)

mpg_diff <- mpg %>% 
  select(class, cty) %>% 
  filter(class %in% c("compact","suv"))

head(mpg_diff)
#    class  cty
# 1 compact  18
# 2 compact  21
# 3 compact  20
# 4 compact  21
# 5 compact  16
# 6 compact  18

# 빈도수 구하기
table(mpg_diff$class)
# compact     suv 
#  47         62 

# compact 자동차와 suv 자동차의 도시 연비 t검정
t.test(data = mpg_diff, cty ~ class, var.equal = T)

# Two Sample t-test
# 
# data:  cty by class
# t = 11.917, df = 107, p-value < 2.2e-16
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   5.525180 7.730139
# sample estimates:
#   mean in group compact     mean in group suv 
# 20.12766              13.50000 

# p-value : 유의수준 (기준값 : 0.05)
# compact 자동차와 suv 자동차의 도시연비는 p-value의 기준값인 0.05보다
# 작기 때문에 통계적으로 유의하다.

#------------------------------------------------------------------------
# 일반 휘발유와 고급 휘발유의 도시 연비 t검정 
# fl - 일반 휘발유 : regular
#      고급 휘발유 : premium

mpg_diff2 <- mpg %>% 
  select(fl, cty) %>% 
  filter(fl %in% c("r","p"))

head(mpg_diff2, 20)

# 빈도수 구하기
table(mpg_diff2$fl)
# p     r 
# 52    168

# 일반 휘발유와 고급 휘발유의 도시 연비 t검정
t.test(data = mpg_diff2, cty ~ fl, var.equal = T)
# Two Sample t-test
# 
# data:  cty by fl
# t = 1.0662, df = 218, p-value = 0.2875
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -0.5322946  1.7868733
# sample estimates:
#   mean in group p mean in group r 
# 17.36538        16.73810 

# 일반 휘발유와 고급 휘발유를 사용하는 자동차 간 도시연비 차이는 
# 통계적으로 유의하지 않다.

#---------------------------------------------------------------------
# 상관분석(Correlation Analysis)
# • 두 연속 변수가 서로 관련이 있는지 검정하는 통계 분석 기법
# • 상관계수(Correlation Coefficient)
# – 두 변수가 얼마나 관련되어 있는지, 관련성의 정도를 나타내는 값
# – 0~1 사이의 값을 지니고 1에 가까울수록 관련성이 크다는 의미
# – 상관계수가 양수면 정비례, 음수면 반비례 관계

# 실업자 수와 개인 소비 지출의 상관관계
# 데이터 준비
economics <- as.data.frame(ggplot2::economics)
head(economics)
#       date   pce    pop     psavert uempmed  unemploy
# 1 1967-07-01 506.7 198712    12.6     4.5     2944
# 2 1967-08-01 509.8 198911    12.6     4.7     2945
# 3 1967-09-01 515.6 199113    11.9     4.6     2958
# 4 1967-10-01 512.2 199311    12.9     4.9     3143
# 5 1967-11-01 517.4 199498    12.8     4.7     3066
# 6 1967-12-01 525.1 199657    11.8     4.8     3018

# 실업자수(unemploy)와 개인 소비 지출(pce)의 상관관계 분석

# 상관 관계분석
# cor.test(economics$unemploy, economics$pce)
# Pearson's product-moment correlation
# 
# data:  economics$unemploy and economics$pce
# t = 18.63, df = 572, p-value < 2.2e-16
# alternative hypothesis: true correlation is not equal to 0
# 95 percent confidence interval:
#  0.5608868 0.6630124
# sample estimates:
#       cor 
# 0.6145176 
# 실업자수와 개인 소비 지출의 상관관계가 통계적으로 유의하다.

# 상관계수 : 0.6145176 

#------------------------------------------------------------------
# 상관행렬 히트맵 만들기
# • 상관행렬(Correlation Matrix)
# – 여러 변수 간 상관계수를 행렬로 타나낸 표
# – 어떤 변수끼리 관련이 크고 적은지 파악할 수 있음

# 데이터 준비
head(mtcars)
# mpg cyl disp  hp drat    wt  qsec vs am gear carb
# Mazda RX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
# Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
# Datsun 710        22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
# Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
# Hornet Sportabout 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
# Valiant           18.1   6  225 105 2.76 3.460 20.22  1  0    3    1

View(mtcars)

# 상관행렬 만들기
car_cor <- cor(mtcars)      # 상관행렬 생성
round(car_cor, 2)           # 소수점 셋째 자리에서 반올림해서 출력

# 상관행렬 히트맵 만들기
# • 히트맵(heat map) : 값의 크기를 색깔로 표현한 그래프
install.packages("corrplot")
library(corrplot)

# 히트맵 그리기
corrplot(car_cor)

# 원대신 상관계수 표시
corrplot(car_cor, method = "number")

# 다양한 파라미터 지정하기
col <- colorRampPalette(c("#BB4444", "#EE9988", "#FFFFFF", "#77AADD", "#4477AA"))
corrplot(car_cor,
         method = 'color',
         col = col(200),
         type = 'lower',
         order = 'hclust',
         addCoef.col = 'black',
         tl.col = 'black',
         tl.srt = 45,
         diag = F)







































