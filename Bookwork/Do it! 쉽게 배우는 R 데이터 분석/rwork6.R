# rwork6.R start
# <<교재 7장 시작>>


# 결측치 제거하기
# 결측치(Missing Value)
# 1. 비어있는 데이터를 의미
# 2. 결측치가 있는 데이터는 통계적인 함수가 적용되지 않는다
# 3. 결측치를 제거하고 분석한다.
# 4. 결측치 데이터는 대문자로 NA 로 표기한다.

# 결측치가 있는 데이터 프레임 생성
df <-data.frame(sex = c('M', 'F', NA, 'M', 'F'),
                score = c(5,4,3,4,NA))
df

# 결측치를 확인하기: is.na()
is.na(df)
#      sex   score       # 결측치는  TRUE로 출력됨 
# [1,] FALSE FALSE
# [2,] FALSE FALSE
# [3,]  TRUE FALSE
# [4,] FALSE FALSE
# [5,] FALSE  TRUE

# 결측치 데이터 갯수 확인
table(is.na(df))        # 결측치 빈도 출력  
# FALSE  TRUE 
# 8       2             # 결측치 2개 있음 : TRUE(2) 

# 각 변수별로 결측치의 갯수 확인
# 1) sex 변수의 결측치 빈도 확인 
table(is.na(df$sex))    
# FALSE  TRUE 
#  4     1              # 결측치 1개 있음 : TRUE(1)  

# 2) score 변수의 결측치 빈도 확인
table(is.na(df$score))
# FALSE  TRUE TRUE(2) 
# 4       1            # 결측치 1개 있음 : TRUE(1)  

# 결측치가 포함된 데이터에 통계적인 함수 적용하기
# : 결측치가 포함된 데이터는 통계적인 함수가 적용되지 않고 NA로 
#   출력되기 떄문에 결측치를 제거하고 데이터 분석을 해야한다.
sum(df$score)
# [1] NA

mean(df$score)
# [1] NA

# 결측치 제거하기
library(dplyr)

# 방법1. filter() 함수
# 1) score 변수의 결측치 데이터 추출
df %>% filter(is.na(score))

# 2) score 변수의 결측치가 아닌 데이터 추출
df %>% filter(!is.na(score))

# 3) 결측치가 아닌 데이터를 df_nomiss 데이터 프레임에 저장
df_nomiss <- df %>% filter(!is.na(score))
df_nomiss

# 4) df_nomiss 데이터프레임을 이용해서 통계적인 정보 구하기 
#    score 변수에 결측치가 제거되었기 때문에 통계적인 함수가 잘 적용된다.
sum(df_nomiss$score)
# [1] 16

mean(df_nomiss$score)
# [1] 4

# 5) sex, score 변수에 결측치가 없는 데이터 추출 
df_nomiss <- df %>% filter(!is.na(sex)  & !is.na(score))
df_nomiss
#    sex score
# 1   M     5
# 2   F     4
# 3   M     4

# 방법2. omit() 함수
# 1) df 데이터 프레임의 모든 결측치를 제거: omit()
df_nomiss2 <- na.omit(df)
df_nomiss2

# 2) 통계적인 함수 적용하기
sum(df_nomiss2$score)
# [1] 13
mean(df_nomiss2$score)
# [1] 4.333333

# 방법3. na.rm = T
# 결측치가 있는 데이터를 제외하고 통계적인 함수 적용하기: na.rm = T
sum(df$score)
# [1] NA
sum(df$score, na.rm = T)    # 결측치 데이터를 제외하고 합 구하기 
# [1] 16
mean(df$score, na.rm = T)   # 결측치 데이터를 제외하고 평균 구하기 
# [1] 4

# 결측치를 제거하고 통계적인 함수를 적용하는 예제
# 1) 데이터 불러오기
exam <- read.csv('data/csv_exam.csv')
exam

# 2) exam 데이터프레임의 math변수의  3, 8, 15행 데이터를 결측으로 처리
exam[c(3, 8, 15), "math"] <- NA
exam

# 3) math 평균 구하기 
# 결측이 포함된 데이터는 통계적인 함수가 적용되지 않는다. 
mean(exam$math)
# [1] NA
exam %>% summarise(mean_math = mean(math))
#      mean_math
# 1        NA

mean(exam$math, na.rm = T)
exam %>% summarise(mean_math = mean(math, na.rm = T))

# 결측치를 제외한 데이터의 평균, 합, 중앙값 구하기 
exam %>% summarise(mean_math = mean(math, na.rm = T),     # 평균 
                   sum_math = sum(math, na.rm = T),       # 합
                   median_math = median(math, na.rm = T)) # 중앙값 
#    mean_math  sum_math  median_math
# 1  55.23529      939          50 

# 결측치 대체하기
# : 결측치가 많은 데이터셋의 경우에는 무조건 결측치를 제거하지 않고,
# 결측치를 대표값(평균, 최빈값)으로 대체해서 처리할 수 있다.

#    exam 데이터프레임의 math변수 3, 8, 15행은 결측치 
# 1) exam 데이터프레임의 math 변수의 평균 구하기
mean(exam$math, na.rm = T)
# [1] 55.23529

# 2) exam 데이터프레임의 math변수 3, 8, 15행 결측치를 평균값으로 대체하기
#   : math가 NA이면 평균값 55점을 할당하고 NA가 아니면 기존값을 할당 
exam$math <- ifelse(is.na(exam$math), 55, exam$math)
exam                         # NA가 평균값 55점으로 대체되어 있음 

table(is.na(exam$math))      # 결측이 없는 데이터만 출력됨 
# FALSE 
# 20 

# 3) math 변수의 통계적인 정보 하기
#   math 변수는 결측치(NA)가 평균값(55)으로 대체되어 평균을 구할수 있다.
mean(exam$math)
# [1] 55.2

# ================================================================
# 혼자서 해보기
# mpg 데이터를 이용해서 분석 문제를 해결해 보세요.
# mpg 데이터 원본에는결측치가 없습니다. 우선 mpg 데이터를 불러와 
# 몇 개의 값을 결측치로 만들겠습니다.
# 아래 코드를 실행하면 다섯 행의 hwy 변수에 NA가 할당됩니다.
mpg <- as.data.frame(ggplot2::mpg) # mpg 데이터 불러오기
mpg[c(65, 124, 131, 153, 212), "hwy"] <- NA # NA 할당하기

# 결측치가 들어있는 mpg 데이터를 활용해서 문제를 해결해보세요.
# • Q1. drv(구동방식)별로 hwy(고속도로 연비) 평균이 어떻게 다른지
# 알아보려고 합니다. 분석을 하기 전에
# 우선 두 변수에 결측치가 있는지 확인해야 합니다. drv 변수와 
# hwy 변수에 결측치가 몇 개 있는지 알아보세요.
table(is.na(mpg$drv))
table(is.na(mpg$hwy))

# • Q2. filter()를 이용해 hwy 변수의 결측치를 제외하고, 
# 어떤 구동방식의 hwy 평균이 높은지 알아보세요.
# 하나의 dplyr 구문으로 만들어야 합니다.
mpg %>%
  filter(!is.na(mpg$hwy)) %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy))
# ================================================================

# 이상치 정제하기
# 이상치(Outlier)
# 1. 정상범주를 크게 벗어나는 데이터를 의미
# 2. 이상치 데이터가 포함되어 있으면 데이터 분석을 왜곡 할 수 있다.
# 3. 이상치 데이터를 결측 데이터로 변환 후 결측치를 제거하는 방법을
#    이용해서 처리한다.

# 이상치 제거하기 - 1. 존재할 수 없는 값
# 1) 이상치가  포함된 데이터 프레임 생성 
#    sex : 1(남자), 2(여자)
#    score : 1 ~ 5
outlier <- data.frame(sex=c(1,2,1,3,2,1),
                      score=c(5,4,3,4,2,6))
outlier

# 2) 이상치 데이터 확인
table(outlier$sex)         # 3 : 이상치 
# 1 2 3             
# 3 2 1 

# 3) 이상치 데이터를 결측으로 처리하기
#    sex변수의 3을 결측치(NA)으로 처리 
outlier$sex <- ifelse(outlier$sex==3, NA, outlier$sex)
outlier

#   score변수의 6을 결측치(NA)으로 처리 
outlier$score <- ifelse(outlier$score==6, NA, outlier$score)
outlier

# 4) 결측치를 제거하고, 성별(sex) 평균 점수 구하기 
outlier %>% 
  filter(!is.na(sex) & !is.na(score)) %>%     # 결측제거 
  group_by(sex) %>%                           # 그룹으로 나눠서 처리 
  summarise(mean_score = mean(score))         # 평균 점수 
#     sex      mean_score
# 1     1          4
# 2     2          3

# 이상치 제거하기 - 2. 극단적인 값 


# 극단치 데이터 확인
# 1. 데이터 불러오기
library(ggplot2)
mpg <- as.data.frame(ggplot2::mpg)
head

# 2. 상자그래프  
boxplot(mpg$hwy)   # hwy: 고속도로 연비 

# 상자 그림           값            설명
# ---------------------------------------------------------
# 상자 아래 세로 점선 아래수염      하위 0~25% 내에 해당하는 값
# 상자 밑면           1사분위수(Q1) 하위 25% 위치 값
# 상자 내 굵은 선     2사분위수(Q2) 하위 50% 위치 값(중앙값)
# 상자 윗면           3사분위수(Q3) 하위 75% 위치 값
# 상자 위 세로 점선   윗수염        하위 75~100% 내에 해당하는 값
# 상자 밖 가로선      극단치 경계   Q1, Q3 밖 1.5 IQR 내 최대값
# 상자 밖 점 표식     극단치        Q1, Q3 밖 1.5 IQR을 벗어난 

# 3. 상자 그래프 통계치 출력
boxplot(mpg$hwy)$stats
#       [,1]
# [1,]   12          # 극단치 하단 경계 
# [2,]   18          # 1사분위 
# [3,]   24          # 2사분위 
# [4,]   27          # 3사분위 
# [5,]   37          # 극단치 상단 경계 
# attr(,"class")
# 1 
# "integer" 

# 4. 극단치 데이터를 결측치로 처리
#    hwy가 12 ~ 37을 벗어나면 극단치 데이터 
mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy)

# 5. 이상치(극단치) 데이터가 결측(NA)로 처리되었는지 확인 
table(is.na(mpg$hwy))   # 결측으로 처리된 데이터 : TRUE 3개  
# FALSE  TRUE 
# 231     3 

# 6. 결측치 데이터를 제외하고 분석하기 
library(dplyr)

mpg %>%
  summarise(mean_hwy = mean(hwy, na.rm = T))
#    mean_hwy
# 1  23.18615

mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy, na.rm = T))
#    drv      mean_hwy
# 1  4         19.2
# 2  f         27.7
# 3  r         21   

# ================================================================
# 혼자서 해보기
# mpg 데이터를 이용해서 분석 문제를 해결해 보세요.
# 우선 mpg 데이터를 불러와서 일부러 이상치를 만들겠습니다. 
# drv(구동방식) 변수의 값은 4(사륜구동),
# f(전륜구동), r(후륜구동) 세 종류로 되어있습니다. 몇 개의 행에
# 존재할 수 없는 값 k를 할당하겠습니다.
# cty(도시 연비) 변수도 몇 개의 행에 극단적으로 크거나 작은 값을
# 할당하겠습니다.
mpg <- as.data.frame(ggplot2::mpg) # mpg 데이터 불러오기
mpg[c(10, 14, 58, 93), "drv"] <- "k" # drv 이상치 할당
mpg[c(29, 43, 129, 203), "cty"] <- c(3, 4, 39, 42) # cty 이상치 할당

# 이상치가 들어있는 mpg 데이터를 활용해서 문제를 해결해보세요.
# 구동방식별로 도시 연비가 다른지 알아보려고 합니다. 분석을 하려면
# 우선 두 변수에 이상치가 있는지 확인하려고 합니다.
# • Q1. drv 에 이상치가 있는지 확인하세요. 이상치를 결측 처리한
# 다음 이상치가 사라졌는지 확인하세요. 결측 처리 할 때는 %in%
# 기호를 활용하세요.
table(mpg$drv)
# 4   f   k   r 
# 100 106   4  24 

mpg$drv <- ifelse(mpg$drv %in% c(4, 'f','r'), mpg$drv, NA)

table(mpg$drv)
# 4   f   r 
# 100 106  24

# • Q2. 상자 그림을 이용해서 cty 에 이상치가 있는지 확인하세요. 
# 상자 그림의 통계치를 이용해 정상 범위를 벗어난 값을 결측 처리한
# 후 다시 상자 그림을 만들어 이상치가 사라졌는지 확인하세요.
boxplot(mpg$cty)$stats
#       [,1]
# [1,]    9
# [2,]   14
# [3,]   17
# [4,]   19
# [5,]   26
# 9 ~ 26을 벗어나면 NA 할당
mpg$cty <- ifelse(mpg$cty < 9 | mpg$cty > 26, NA, mpg$cty)

boxplot(mpg$cty)

# • Q3. 두 변수의 이상치를 결측처리 했으니 이제 분석할 차례입니다.
# 이상치를 제외한 다음 drv 별로 cty 평균이 어떻게 다른지 알아보세요. 
# 하나의 dplyr 구문으로 만들어야 합니다.
mpg %>% 
  filter(!is.na(mpg$cty) & !is.na(mpg$drv)) %>% 
  group_by(drv) %>%
  summarise(mean_cty = mean(cty))
# ================================================================


# 정리하기
# # 1.결측치 정제하기
# # 결측치 확인
# table(is.na(df$score))
# # 결측치 제거
# df_nomiss <- df %>% filter(!is.na(score))
# # 여러 변수 동시에 결측치 제거
# df_nomiss <- df %>% filter(!is.na(score) & !is.na(sex))
# # 함수의 결측치 제외 기능 이용하기
# mean(df$score, na.rm = T)
# exam %>% summarise(mean_math = mean(math, na.rm = T))

# # 2.이상치 정제하기
# # 이상치 확인
# table(outlier$sex)
# # 결측 처리
# outlier$sex <- ifelse(outlier$sex == 3, NA, outlier$sex)
# # boxplot 으로 극단치 기준 찾기
# boxplot(mpg$hwy)$stats
# # 극단치 결측 처리
# mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy)


# <<교재 6장 끝>>
# rwork5.R end