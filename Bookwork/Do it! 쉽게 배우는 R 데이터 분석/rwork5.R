# rwork5.R start
# <<교재 6장 시작>>

# 데이터 전처리: dplyr 패키지
# 함수 기능
#----------------------------------------------------------
# filter()       행 추출 : 조건에 맞는 데이터 추출 
# select()       열(변수) 추출
# arrange()      정렬
# mutate()       변수 추가
# summarise()    통계치 산출
# group_by()     집단별로 나누기
# left_join()    데이터 합치기(열) : 가로방향으로 합치기 
# bind_rows()    데이터 합치기(행) : 세로방향으로 합치기 

# dplyr 패키지 설치
install.packages('dplyr')

# dplyr  패키지 로딩
library(dplyr)

# 데이터 불러오기
exam <- read.csv('data/csv_exam.csv')
exam

# 1. filter(): 조건에 맞는 데이터를 추출하는 역할

# 1) exam에서 class가 1인 데이터 추출
#    %>% : 단축키 (Ctrl + Shift + M)
#          오른쪽으로 전달하라는 의미로 사용됨
exam %>% filter(class == 1)

# 2) exam에서 class가 2반은 데이터 추출
exam %>% filter(class == 2)

# 3) 1반이 아닌 학생들 추출
exam %>% filter(class != 1)

# 4) 수학점수가 50을 초곽한 학생들 추출
exam %>% filter(math > 50)

# 5) 영어점수가 80점 이상인 학생들 추출
exam %>% filter(english >= 80)

# 6) 과학점수가 50점 이하인 학생 추출
exam %>% filter(science <= 50)

# 7) 1반 이면서 수학 점수가 50점 이상인 학생 추출 
exam %>% filter(class==1 & math>=50)

# 8) 수학 점수가 90점 이상이거나 영어점수가 90점 이상인 학생 추출
exam %>% filter(math>=90 | english>=90)

# 9) 영어 점수가 90점 미만이거나 과학 점수가 50점 미만인 학생 추출
exam %>% filter(english<90 | science<50)

# 10) class가 1반이거나 3반이거나 5반인 학생 추출 
exam %>% filter(class==1  | class==3  | class==5)

#  %in% : 매치 연산자
exam %>% filter(class %in% c(1, 3, 5))

# filter() 함수로 추출한 데이터를 새로운 변수에 저장하기
# 1) 1반 학생 데이터를 class1 변수에 저장
class1 <- exam %>% filter(class==1)
class1

# 2) 1반 학생들의 수학점수의 평균 구하기
mean(class1$math)
# [1] 46.25

# 1) 3반 학생 데이터를 class3 변수에 저장
class3 <- exam %>% filter(class==3)
class3

# 2) 3반 학생들의 영어점수의 평균 구하기
mean(class3$english)
# [1] 86.5

# ================================================================
# 혼자서 해보기
# mpg 데이터를 이용해 분석 문제를 해결해 보세요.
# • Q1. 자동차 배기량에 따라 고속도로 연비가 다른지 알아보려고
# 합니다. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중 
# 어떤 자동차의 hwy(고속도로 연비)가 
# 평균적으로 더 높은지 알아보세요.
library(ggplot2)
mpg <- as.data.frame(ggplot2::mpg)
mpg_test <- mpg %>% filter(displ <= 4)
mpg_test2 <- mpg %>% filter(displ >= 5)
mean(mpg_test$hwy)
# [1] 25.96319
mean(mpg_test2$hwy)
# [1] 18.07895

# • Q2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고
# 합니다. "audi"와 "toyota" 중 어느 
# manufacturer(자동차 제조 회사)의 cty(도시 연비)가 평균적으로 
# 더 높은지 알아보세요.
mpg_test <- mpg %>% filter(manufacturer == 'audi')
mpg_test2 <- mpg %>% filter(manufacturer == 'toyota')
mean(mpg_test$cty)
# [1] 17.61111
mean(mpg_test2$cty)
# [1] 18.52941


# • Q3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을
# 알아보려고 합니다. 이 회사들의 자동차를 추출한 뒤
# hwy 전체 평균을 구해보세요.
mpg_test <- mpg %>% filter(manufacturer %in% c('chevrolet', 'ford', 'honda'))
mean(mpg_test$hwy)
# [1] 22.50943
# ================================================================

# 2. select(): 특정 열(변수)에 저장된 데이터를 추출하는 역할
# 1) exam 데이터프레임의 math 변수의 값을 추출
exam %>% select(math)

# 2) exam 데이터프레임의 science 변수의 값을 추출
exam %>% select(science)

# 3) 여러변수 추출하기
exam %>% select(class, math, english)

# 4) 특정 변수 제외한 데이터 추출  : math 변수 제외
exam %>% select(-math)

# 5) 2개의 변수 제외 : math, english, science 변수 제외 
exam %>% select(-math, -english, -science)

# 6) 1반 학생들의 영어 점수를 추출 
exam %>% filter(class==1) %>% select(english)

# 가독성을 좋게하기 위한 표기 
exam %>% 
  filter(class==1) %>%       # 1반 학생들의 정보 추출    
  select(english)            # english 점수 추출 

# 7) exam 데이터프레임에서 id, math 변수의 데이터 6개만 추출 
exam %>% 
  select(id, math) %>%      # id, math 점수 추출 
  head()                    # 앞에서 6개의 데이터 추출 

# ================================================================
# 혼자서 해보기
# mpg 데이터를 이용해서 분석 문제를 해결해보세요.
# • Q1. mpg 데이터는 11 개 변수로 구성되어 있습니다. 
# 이 중 일부만 추출해서 분석에 활용하려고 합니다. mpg
# 데이터에서 class(자동차 종류), cty(도시 연비) 변수를 추출해
# 새로운 데이터를 만드세요. 새로 만든
# 데이터의 일부를 출력해서 두 변수로만 구성되어 있는지 확인하세요.
library(ggplot2)
mpg <- as.data.frame(ggplot2::mpg)
mpg_test <- mpg %>% select(class, cty)
head(mpg_test)

# • Q2. 자동차 종류에 따라 도시 연비가 다른지 알아보려고 합니다.
# 앞에서 추출한 데이터를 이용해서
# class(자동차 종류)가 "suv"인 자동차와 "compact"인 자동차 중 
# 어떤 자동차의 cty(도시 연비)가 더 높은지 알아보세요.
suv <- mpg_test %>% 
  filter(class == 'suv') 
compact <- mpg_test %>% 
  filter(class == 'compact') 
mean(suv$cty)
# [1] 13.5

mean(compact$cty)
# [1] 20.12766
# ================================================================

# 3. arrange(): 오름차순으로 정렬해주는 함수
#--------------------------------------------------
#  숫자   1, 2, 3....            10, 9, 8.....
#  문자   사전순 정렬            사전 역순 정렬 

# 1) exam 데이터프레임에서 math 성적을 오름차순 정렬
exam %>% arrange(math)        # 오름차순 정렬 : 작은 점수부터 출력 

# 2) exam 데이터프레임에서 math 성적을 내림차순 정렬
exam %>% arrange(desc(math))  # 내림차순 정렬 : 큰 점수부터 출력 

# 3) 정렬 기준 변수를 여러개 지정
#    exam 데이터프레임에서 class변수를 오름차순 정렬하고, 
#    math변수를 오름차순 정렬 
exam %>%  arrange(class, math)

#    exam 데이터프레임에서 class변수를 오름차순 정렬하고, 
#    math변수를 내림차순 정렬 
exam %>% arrange(class, desc(math))

# ================================================================
# 혼자서 해보기
# mpg 데이터를 이용해서 분석 문제를 해결해보세요.
# • "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 
# hwy(고속도로 연비)가 높은지 알아보려고 합니다.
# "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는 자동차의
# 데이터를 출력하세요.
mpg %>% filter(manufacturer=='audi') %>% 
  arrange(desc(hwy)) %>% 
  head(5)
# ================================================================

# 4. mutate(): 파생변수를 만들떄 사용되는 함수
# 파생변수: 기존변수를 이용해서 새로 생성되는 변수

# 1) exam 데이터 프레임에서 math, english, science 변수의 합을
# 저장하는 파생변수(total) 생성
# 방법1.
exam$total <- exam$math + exam$english + exam$science

# 방법2. mutate() 함수 이용
exam %>% 
  mutate(total = math + english + science) %>%  # total 파생변수 생성 
  head()                                        # 앞에서 6개 데이터 추출 

# 2) 여러개의 파생변수 생성 : total , mean 
exam %>% 
  mutate(total = math + english + science,     # total 파생변수 생성
         mean = total/3) %>%                   # mean 파생변수 생성
  head()                                       # 앞에서 6개 데이터 추출

# 3) 조건식을 만족하는 데이터를 가진 파생변수 생성 : test
#    exam 데이터프레임의 science점수가 60점 이상인 경우에 "pass",
#    60점 미만인 경우에는 "fail" 값을 가진 파생변수(test) 생성 
exam2 <-exam %>%                              
  mutate(test = ifelse(science>=60, "pass", "fail")) %>% 
  head()
exam2

# 4) total 파생변수를 기준으로 내림차순 정렬 
exam %>% 
  mutate(total = math + english + science) %>%  # total 파생변수 생성
  arrange(desc(total)) %>%                      # 내림차순 정렬 
  head()                                        # 앞에서 6개 데이터 추출

# ================================================================
# 혼자서 해보기
# mpg 데이터를 이용해서 분석 문제를 해결해보세요.
# mpg 데이터는 연비를 나타내는 변수가 hwy(고속도로 연비), 
# cty(도시 연비) 두 종류로 분리되어 있습니다. 두
# 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 
# 분석하려고 합니다.
# • Q1. mpg 데이터 복사본을 만들고, cty 와 hwy 를 더한 '합산 연비
# 변수'를 추가하세요.
mpg_v <- mpg
mpg_v <- mpg_v %>% mutate(total = cty+hwy)
mpg_v

# • Q2. 앞에서 만든 '합산 연비 변수'를 2 로 나눠 '평균 연비 변수'를
# 추가세요.
mpg_v <- mpg_v %>% mutate(avg = total/2)
mpg_v

# • Q3. '평균 연비 변수'가 가장 높은 자동차 3 종의 데이터를
# 출력하세요.
mpg_v %>%
  arrange(desc(avg)) %>% 
  head(3)


# • Q4. 1~3 번 문제를 해결할 수 있는 하나로 연결된 dplyr 구문을 
# 만들어 출력하세요. 데이터는 복사본 대신 mpg 원본을 이용하세요.
mpg %>% 
  mutate(total=cty+hwy, avg=total/2) %>% 
  arrange(desc(avg)) %>% 
  head(3)

# ================================================================

# 5. summarise(): 통계치 산출해주는 함수
# 6. group_by(): 집단별로 처리해주는 역할

# 1) exam 데이터 프레임의 math 성적의 평균점수 구하기
exam %>% 
  summarise(mean_math = mean(math))
#   mean_math
# 1     57.45

# cf.
exam %>% 
  mutate(mean_math = mean(math))

# 2) 각  class별 math 성적의 평균점수 구하기
# 방법1.
exam %>% filter(class==1) %>% summarise(mean_math=mean(math))
exam %>% filter(class==2) %>% summarise(mean_math=mean(math))
exam %>% filter(class==3) %>% summarise(mean_math=mean(math))
exam %>% filter(class==4) %>% summarise(mean_math=mean(math))
exam %>% filter(class==5) %>% summarise(mean_math=mean(math))

# 방법2. group_by() 함수 이용 
exam %>% 
  group_by(class) %>%                     # class별로 구분 
  summarise(mean_math = mean(math))       # 각 class별 math 평균 
# `summarise()` ungrouping output (override with `.groups` argument)
# # A tibble: 5 x 2
#   class mean_math
#   <int>     <dbl>
# 1     1      46.2
# 2     2      61.2
# 3     3      45  
# 4     4      56.8
# 5     5      78  

# 3) 여러개의 통계 요약정보 구하기 
#    각 class별 여러개의 통계 요약정보 구하기 
exam %>% 
  group_by(class) %>%                     # class별로 구분 
  summarise(mean_math = mean(math),       # class별 math 평균 
            sum_math = sum(math),         # class별 math 합
            median_math = median(math),   # class별 math 중앙값  
            n = n())                      # class별 학생수 
# `summarise()` ungrouping output (override with `.groups` argument)
# # A tibble: 5 x 5
#   class mean_math sum_math median_math     n
#     <int>     <dbl>    <int>       <dbl> <int>
# 1     1      46.2      185        47.5     4
# 2     2      61.2      245        65       4
# 3     3      45        180        47.5     4
# 4     4      56.8      227        53       4
# 5     5      78        312        79       4

# 4) 각 집단별로 다시 집단 나누기
mpg %>%
  group_by(manufacturer, drv) %>%     # 회사별, 구방방식별 분리
  summarise(mean_cty = mean(cty)) %>% # cty 평균 산출
  head(10)                            # 일부 출력
# `summarise()` regrouping output by 'manufacturer' (override with `.groups` argument)
# # A tibble: 10 x 3
# # Groups:   manufacturer [5]
#   manufacturer drv   mean_cty
#   <chr>        <chr>    <dbl>
# 1 audi         4         16.8
# 2 audi         f         18.9
# 3 chevrolet    4         12.5
# 4 chevrolet    f         18.8
# 5 chevrolet    r         14.1
# 6 dodge        4         12  
# 7 dodge        f         15.8
# 8 ford         4         13.3
# 9 ford         r         14.8
# 10 honda        f         24.4

# 5) dplyr 조합하기
# 
# 문제) 회사별로 "suv" 자동차의 도시 및 고속도로 
# 통합 연비 평균을 구해 내림차순으로 정렬하고, 1~5위까지 출력하기

# dplyr 조합하기
mpg %>%
  group_by(manufacturer) %>%           # 회사별로 분리
  filter(class == "suv") %>%          # suv 추출
  mutate(tot = (cty+hwy)/2) %>%       # 통합 연비 변수 생성
  summarise(mean_tot = mean(tot)) %>% # 통합 연비 평균 산출
  arrange(desc(mean_tot)) %>%         # 내림차순 정렬
  head(5)                             # 1~5 위까지 출력
# # A tibble: 5 x 2
#   manufacturer mean_tot
#    <chr>           <dbl>
# 1 subaru           21.9
# 2 toyota           16.3
# 3 nissan           15.9
# 4 mercury          15.6
# 5 jeep             15.6

# ================================================================
# 혼자서 해보기
# mpg 데이터를 이용해서 분석 문제를 해결해 보세요.
# • Q1. mpg 데이터의 class 는 "suv", "compact" 등 자동차를 
# 특징에 따라 일곱 종류로 분류한 변수입니다.
# 어떤 차종의 연비가 높은지 비교해보려고 합니다. class 별 
# cty 평균을 구해보세요.
mpg <- as.data.frame(ggplot2::mpg)
mpg %>% 
  group_by(class) %>% 
  summarise(mean_cty = mean(cty))
# # A tibble: 7 x 2
#   class      mean_cty
#   <chr>         <dbl>
# 1 2seater        15.4
# 2 compact        20.1
# 3 midsize        18.8
# 4 minivan        15.8
# 5 pickup         13  
# 6 subcompact     20.4
# 7 suv            13.5

# • Q2. 앞 문제의 출력 결과는 class 값 알파벳 순으로 정렬되어
# 있습니다. 어떤 차종의 도시 연비가 높은지 쉽게 알아볼 수 있도록
# cty 평균이 높은 순으로 정렬해 출력하세요.
mpg %>% 
  group_by(class) %>% 
  summarise(mean_cty = mean(cty)) %>% 
  arrange(desc(mean_cty))


# • Q3. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지
# 알아보려고 합니다. hwy 평균이 가장 높은 회사 세 곳을 출력하세요.
mpg %>% 
  group_by(manufacturer) %>% 
  summarise(mean_hwy = mean(hwy)) %>% 
  arrange(desc(mean_hwy)) %>%
  head(3)

# • Q4. 어떤 회사에서 "compact"(경차) 차종을 가장 많이 생산하는지
# 알아보려고 합니다. 각 회사별 "compact" 차종 수를 내림차순으로
# 정렬해 출력하세요.
mpg %>% 
  filter(class=='compact') %>% 
  group_by(manufacturer) %>% 
  summarise(count=n()) %>% 
  arrange(desc(count))
# # A tibble: 5 x 2
#   manufacturer count
#   <chr>        <int>
# 1 audi            15
# 2 volkswagen      14
# 3 toyota          12
# 4 subaru           4
# 5 nissan           2

# ================================================================

# 7. left_join() 데이터 합치기(열): 가로방향으로 합치기

# 1) 2개의 데이터 프레임 생성
# 중간고사 성적 데이터프레임
test1 <- data.frame(id = c(1, 2, 3, 4, 5),
                    midterm = c(60, 80, 70, 90, 85))
test1
#   id midterm
# 1  1      60
# 2  2      80
# 3  3      70
# 4  4      90
# 5  5      85

# 기말고사 성적 데이터프레임 
test2 <- data.frame(id = c(1, 2, 3, 4, 5),
                    final = c(70, 83, 65, 95, 80))
test2
#   id final
# 1  1    70
# 2  2    83
# 3  3    65
# 4  4    95
# 5  5    80

# 2) 2개의 데이터프레임을 가로방향으로 합치기 : id 열 기준
total <- left_join(test1, test2, by='id')
total
#   id midterm final
# 1  1      60    70
# 2  2      80    83
# 3  3      70    65
# 4  4      90    95
# 5  5      85    80

# 1) name 데이터프레임 생성
name <- data.frame(class = c(1,2,3,4,5),
                   teacher = c("kim","lee","park","choi","jung"))
name

# 2) exam, name 데이터프레임을 가로방향으로 합치기 : class 기준 합치기
exam_new <- left_join(exam, name, by='class')
exam_new
#     id class math english science teacher
# 1   1     1   50      98      50     kim
# 2   2     1   60      97      60     kim
# 3   3     1   45      86      78     kim
# 4   4     1   30      98      58     kim
# 5   5     2   25      80      65     lee
# 6   6     2   50      89      98     lee
# 7   7     2   80      90      45     lee
# 8   8     2   90      78      25     lee
# 9   9     3   20      98      15    park
# 10 10     3   50      98      45    park
# 11 11     3   65      65      65    park
# 12 12     3   45      85      32    park
# 13 13     4   46      98      65    choi
# 14 14     4   48      87      12    choi
# 15 15     4   75      56      78    choi
# 16 16     4   58      98      65    choi
# 17 17     5   65      68      98    jung
# 18 18     5   80      78      90    jung
# 19 19     5   89      68      87    jung
# 20 20     5   78      83      58    jung

# 8. bind_rows() 데이터 합치기(행): 세로방향으롤 합치기
# 1) 2개의 데이터프레임 생성
#    1~5번 학생의 시험 데이터를 가진 데이터프레임 생성
group_a <- data.frame(id = c(1, 2, 3, 4, 5),
                      test = c(60, 80, 70, 90, 85))
group_a
#    6~10번 학생의 시험 데이터를 가진 데이터프레임 생성
group_b <- data.frame(id = c(6, 7, 8, 9, 10),
                      test = c(70, 83, 65, 95, 80))
group_b

# 2) 2개의 데이터프레임을 세로방향으로 합치기 :  bind_rows()
group_all <- bind_rows(group_a, group_b)
group_all

# ================================================================
# 혼자서 해보기
# mpg 데이터를 이용해서 분석 문제를 해결해 보세요.
# mpg 데이터의 fl 변수는 자동차에 사용하는 연료(fuel)를 의미합니다.
# 아래는 자동차 연료별 가격을 나타낸
# 표입니다.
# fl 연료 종류 가격(갤런당 USD)
# c CNG 2.35
# d diesel 2.38
# e ethanol E85 2.11
# p premium 2.76
# r regular 2.22
# 우선 이 정보를 이용해서 연료와 가격으로 구성된 데이터 프레임을
# 만들어 보세요.
fuel <- data.frame(fl = c("c", "d", "e", "p", "r"),
                   price_fl = c(2.35, 2.38, 2.11, 2.76, 2.22),
                   stringsAsFactors = F)
fuel # 출력
##  fl price_fl
## 1 c 2.35
## 2 d 2.38
## 3 e 2.11
## 4 p 2.76
## 5 r 2.22
# • Q1. mpg 데이터에는 연료 종류를 나타낸 fl 변수는 있지만 연료
# 가격을 나타낸 변수는 없습니다. 위에서 만든 fuel 데이터를 이용해서
# mpg 데이터에 price_fl(연료 가격) 변수를 추가하세요.
mpg_join <- left_join(mpg, fuel, by='fl')
head(mpg_join)

# • Q2. 연료 가격 변수가 잘 추가됐는지 확인하기 위해서 
# model, fl, price_fl 변수를 추출해 앞부분 5 행을 출력해 보세요.
mpg_join %>%
  select(model, fl, price_fl) %>% 
  head(5)
# ================================================================

# 정리하기
# # 1.조건에 맞는 데이터만 추출하기
# exam %>% filter(english >= 80)
# # 여러 조건 동시 충족
# exam %>% filter(class == 1 & math >= 50)
# # 여러 조건 중 하나 이상 충족
# exam %>% filter(math >= 90 | english >= 90)
# exam %>% filter(class %in% c(1,3,5))

# # 2.필요한 변수만 추출하기
# exam %>% select(math)
# exam %>% select(class, math, english)
# 
# # 3.함수 조합하기, 일부만 출력하기
# exam %>%
#   select(id, math) %>%
#   head(10)

# # 4.순서대로 정렬하기
# exam %>% arrange(math) # 오름차순 정렬
# exam %>% arrange(desc(math)) # 내림차순 정렬
# exam %>% arrange(class, math) # 여러 변수 기준 오름차순 정렬

# # 5.파생변수 추가하기
# exam %>% mutate(total = math + english + science)
# # 여러 파생변수 한 번에 추가하기
# exam %>%
#   mutate(total = math + english + science,
#          mean = (math + english + science)/3)
# # mutate()에 ifelse() 적용하기
# exam %>% mutate(test = ifelse(science >= 60, "pass", "fail"))
# # 추가한 변수를 dplyr 코드에 바로 활용하기
# exam %>%
#   mutate(total = math + english + science) %>%
#   arrange(total)

# # 6.집단별로 요약하기
# exam %>%
#   group_by(class) %>%
#   summarise(mean_math = mean(math))
# # 각 집단별로 다시 집단 나누기
# mpg %>%
#   group_by(manufacturer, drv) %>%
#   summarise(mean_cty = mean(cty))
 
# # 7.데이터 합치기
# # 가로로 합치기
# total <- left_join(test1, test2, by = "id")
# # 세로로 합치기
# group_all <- bind_rows(group_a, group_b)

# ================================================================
# 분석 도전
# 미국 동북중부 437개 지역의 인구통계 정보를 담고 있는 midwest
# 데이터를 사용해 데이터 분석 문제를 해결해 보세요. 
# midwest는 ggplot2 패키지에 들어 있습니다.
# • 문제 1. popadults 는 해당 지역의 성인 인구, poptotal 은 
# 전체 인구를 나타냅니다. midwest 데이터에 
# '전체 인구 대비 미성년 인구 백분율' 변수를 추가하세요.
library(ggplot2)
midwest <- as.data.frame(ggplot2::midwest)
midwest_up <- midwest %>% 
  mutate(rate = (poptotal-popadults)/poptotal*100)

# • 문제 2. 미성년 인구 백분율이 가장 높은 상위 5 개 county(지역)의
# 미성년 인구 백분율을 출력하세요.
midwest_up %>% 
  arrange(desc(rate)) %>% 
  select(county, rate) %>% 
  head(5)

# • 문제 3. 분류표의 기준에 따라 미성년 비율 등급 변수를 추가하고,
# 각 등급에 몇 개의 지역이 있는지 알아보세요.
# 분류 기준
# ---------------------
# large 40% 이상
# middle 30% ~ 40% 미만
# small 30% 미만
# ---------------------
midwest_up <- midwest_up %>% 
  mutate(grade = ifelse(rate >= 40, "large",
                        ifelse(rate >=30, "middle","small")))
table(midwest_up$grade)

# • 문제4. popasian은 해당 지역의 아시아인 인구를 나타냅니다. 
# '전체 인구 대비 아시아인 인구 백분율'
# 변수를 추가하고, 하위 10개 지역의 state(주), county(지역명),
# 아시아인 인구 백분율을 출력하세요.
midwest_up %>% 
  mutate(arate = popasian/poptotal*100) %>% 
  arrange(arate) %>%
  select(state, county, arate)
  head(10)
# ================================================================

# <<교재 6장 끝>>
# rwork5.R end
