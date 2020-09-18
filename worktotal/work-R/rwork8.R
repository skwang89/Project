# 데이터 분석 프로젝트
# 한국복지패널데이터
# • 한국보건사회연구원 발간
# • 가구의 경제활동을 연구해 정책 지원에 반영할 목적
# • 2006~2015년까지 전국에서 7000여 가구를 선정해 매년 추적 조사
# • 경제활동, 생활실태, 복지욕구 등 수천 개 변수에 대한 정보로 구성

# 패키지 준비하기
install.packages('foreign')

library(foreign)
library(dplyr)
library(ggplot2)
library(readxl)

# 데이터 불러오기
raw_welfare <- read.spss(file='data/Koweps_hpc10_2015_beta1.sav',
                         to.data.frame = T)

# 복사본 데이터프레임 만들기
welfare <- raw_welfare
welfare

# 데이터 탐색하기
head(welfare)          # 앞에서 6개의 데이터 추출
tail(welfare)          # 뒤에서 6개의 데이터 추출  
View(welfare)          # 뷰어창으로 데이터를 출력 
dim(welfare)           # 데이터 차원 : 16664행   957열 
str(welfare)           # 각 변수의 데이터형 출력
summary(welfare)       # 통계적인 요약정보 출력 

# 변수명 변경하기
welfare <- rename(welfare,
                  sex = h10_g3,             # 성별   
                  birth = h10_g4,           # 태어난 연도
                  marriage = h10_g10,       # 혼인 상태
                  religion = h10_g11,       # 종교
                  income = p1002_8aq1,      # 월급
                  code_job = h10_eco9,      # 직종코드
                  code_region = h10_reg7 )  # 지역 코드 

View(welfare)

#---------------------------------------------------------------
# 1. 성별에 따른 월급 차이
#    : 성별에 따라 월급이 얼마나 다를까?

# 1) 성별(sex) 검토 
class(welfare$sex)      # sex변수의 데이터 형 
# "numeric"              숫자 데이터 

table(welfare$sex)      # sex변수의 빈도수 
# 1    2                # 1:남자, 2:여자  9:모름/무응답
# 7578 9086 

# 2) 전처리
# 이상치 데이터 확인
table(welfare$sex)     
# 1    2              # 이상치 데이터(9)가 없음 
# 7578 9086 

# 이상치 데이터를 결측 처리
welfare$sex <- ifelse(welfare$sex == 9, NA, welfare$sex)

# 결측치 확인
table(is.na(welfare$sex))
# FALSE 
# 16664 

# 성별(1, 2) 항목에 이름 부여 :  (1:male, 2:female)
welfare$sex <- ifelse(welfare$sex == 1, "male", "female")
table(welfare$sex)
# female   male 
# 9086     7578 

# 성별 빈도 그래프 
qplot(welfare$sex)

#3)월급(income) 변수 검토
class(welfare$income)
# "numeric"               숫자데이터 

#  월급(income) 변수의 빈도 구하기
table(welfare$income)

# 월급(income) 변수의 통계 요약정보 구하기
summary(welfare$income)
# Min. 1st Qu.  Median    Mean  3rd Qu.    Max.    NA's 
# 0.0   122.0   192.5    241.6   316.6    2400.0   12030

# 월급(income) 빈도 그래프
qplot(welfare$income)

# x축의 범위 설정 : 0 ~ 1000
qplot(welfare$income) + xlim(0, 1000)


# 4) 전치리 
# 이상치 데이터를 결측으로 처리
# income 의 범위 : 1 ~ 9998
# income 의 이상치 : 9999(모름/무응답)
welfare$income <- ifelse(welfare$income %in% c(0,9999), NA, welfare$income)

# 결측치 확인
table(is.na(welfare$income))
# FALSE  TRUE 
# 4620   12044 

# 5) 성별에 따른 월급 분석하기
#    성별에 따른 평균 월급 구하기
sex_income <- welfare %>% 
  filter(!is.na(income)) %>%     # 결측치 제거하기 
  group_by(sex) %>% 
  summarise(mean_income = mean(income))

sex_income
#  sex        mean_income
# <chr>        <dbl>
# 1 female        163.
# 2 male          312.


# 6) 막대 그래프로 시각화 
ggplot(data = sex_income, aes(x = sex, y = mean_income) ) + geom_col()

#---------------------------------------------------------------
# 2. 나이와 월급과의 관계
#    몇살때 월급을 가장 많이 받을까?

# 1) birth변수 검토하기
# birth 변수 : 태어난 연도가 저장된 변수
class(welfare$birth)
# "numeric"            숫자 데이터 

# birth 변수의 통계 요약 정보 구하기
summary(welfare$birth)
# Min.   1st Qu.  Median    Mean   3rd Qu.    Max. 
# 1907    1946     1966     1968    1988      2014

# birth 변수의 빈도 그래프 
qplot(welfare$birth)


# 2) 전처리
# 이상치 데이터 확인
# birth 변수의 정상 범위 : 1900 ~ 2014
# birth 변수의 이상치 : 9999 (모름/무응답)
summary(welfare$birth)
# Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
# 1907    1946    1966    1968    1988    2014 

# 결측치 확인
table(is.na(welfare$birth))
# FALSE 
# 16664 

# 이상치(9999) 데이터를 결측으로 처리
welfare$birth <- ifelse(welfare$birth == 9999, NA, welfare$birth)

# 결측치 확인
table(is.na(welfare$birth))
# FALSE 
# 16664

# 3) 파생변수 만들기 - 나이(age) 
welfare$age <- 2015 - welfare$birth + 1
summary(welfare$age)
# Min. 1st Qu.  Median    Mean  3rd Qu.    Max. 
# 2.00   28.00   50.00   48.43   70.00    109.00 

# 나이(age) 빈도 그래프
qplot(welfare$age)

# 4) 나이와 월급 관계 분석하기
#    나이에 따른 평균 월급 구하기
age_income <- welfare %>% 
  filter(!is.na(income)) %>%  # 결측치 제거하기 
  group_by(age) %>%           # 나이(age)별로 처리 
  summarise(mean_income = mean(income))

head(age_income, 10)       # 앞에서 부터 10개 데이터 구하기 

# 5) 선 그래프로 시각화
ggplot(data=age_income, aes(x=age, y=mean_income)) + geom_line()

#---------------------------------------------------------------
#  3. 연령대에 따른 월급 차이
#     어떤 연령대의 월급이 가장 많을까?
#  0  ~ 29 : young
#  30 ~ 59 : middle
#  60이상  : old

# 1) 파생변수 만들기 - 연령대(ageg)
welfare <- welfare %>% 
  mutate(ageg = ifelse(age<30, "young",
                       ifelse(age<=59,"middle", "old")))

# 각 연령대별 빈도수
table(welfare$ageg)
# middle    old    young 
# 6049      6281   4334 

# 연령대(ageg) 빈도 그래프
qplot(welfare$ageg)

# 2) 연령대별 평균 월급 구하기
ageg_income <- welfare %>% 
  filter(!is.na(income)) %>%  # 결측치 제거
  group_by(ageg) %>% 
  summarise(mean_income=mean(income))

# 연령대별 평균월급 출력
ageg_income
#  ageg         mean_income
# <chr>        <dbl>
# 1 middle        282.
# 2 old           125.
# 3 young         164.

# 3) 막대 그래프로 시각화
ggplot(data=ageg_income, aes(x=ageg, y=mean_income)) +         
  geom_col()

# x축의 출력 순서를 young - middle - old 순으로 출력
ggplot(data=ageg_income, aes(x=ageg, y=mean_income)) +         
  geom_col() +
  scale_x_discrete(limits=c("young","middle","old"))

#---------------------------------------------------------------
# 4. 연령대 및 성별 월급 차이 분석
#    각 연령대별, 성별 월급 차이 분석

#  0  ~ 29 : young
#  30 ~ 59 : middle
#  60이상  : old

# 1) 연령대 및 성별 평균 월급 구하기
sex_income <- welfare %>% 
  filter(!is.na(income)) %>%     # 결측치 제거
  group_by(ageg, sex) %>% 
  summarise(mean_income=mean(income))
sex_income  
# ageg     sex         mean_income
# <chr>    <chr>        <dbl>
# 1 middle female       188. 
# 2 middle male         353. 
# 3 old    female        81.5
# 4 old    male         174. 
# 5 young  female       160. 
# 6 young  male         171. 

# 2) 막대 그래프로 시각화
ggplot(data=sex_income, aes(x=ageg, y=mean_income, fill=sex)) +       
  geom_col() +
  scale_x_discrete(limits = c("young","middle","old"))


# 성별 막대 그래프 분리해서 시각화
ggplot(data=sex_income, aes(x=ageg, y=mean_income, fill=sex)) +       
  geom_col(position = "dodge") +
  scale_x_discrete(limits = c("young","middle","old"))

#------------------------------------------------------------------
# Q. 나이 및 성별 월급 차이분석
# 1) 연령별 성별 평균 월급 분석
sex_age <- welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age,sex)  %>% 
  summarise(mean_income = mean(income))
sex_age

# 2) 선그래프로 시각화
ggplot(data = sex_age, aes(x=age, y=mean_income, col=sex)) + 
  geom_line()

#------------------------------------------------------------------
# 5. 직업별 월급 차이
#    어떤 직업이 가장 많은 월급을 받을까?

# 1) 변수(code_job) 검토하기
class(welfare$code_job)
# "numeric"                숫자 데이터

# 빈도수 구하기
table(welfare$code_job)

# 2) 전처리
#   직종코드(code_job)와 직업(job) 정보를 가지고 있는 엑셀파일 
#   불러오기 
library(readxl)
list_job <- read_excel("data/Koweps_Codebook.xlsx",
                       col_names = T,
                       sheet = 2)

head(list_job)
dim(list_job)         # 149행 2열 
View(list_job)

# welfare와 list_job 데이터프레임  가로방향으로 합치기 
welfare <- left_join(welfare, list_job, by="code_job")

# 가로 방향으로 합쳐진 데이터프레임을 출력 
welfare %>% filter((!is.na(code_job))) %>%    # 결측치 제거
  select(code_job, job) %>% 
  head(10)

# 3) 직업별 평균 월급 구하기
job_income <- welfare %>% 
  filter(!is.na(job) & !is.na(income)) %>%  # 결측치 제거
  group_by(job) %>% 
  summarise(mean_income = mean(income))
head(job_income)

# 4) 월급을 많이 받는 상위 10개의 직업을 구하자 : 내림차순 정렬 
top10 <- job_income %>% 
  arrange(desc(mean_income)) %>%   # 평균월급을 내림차순 정렬 
  head(10)
top10

# 5) 그래프로 시각화
ggplot(data=top10, aes(x=reorder(job, mean_income), y=mean_income)) + 
  geom_col() +    # 막대 그래프
  coord_flip()    # x, y축이 바뀜 

# 6) 하위 10개 직업 추출 : 오름차순 정렬
bottom10 <- job_income %>% 
  arrange(mean_income) %>%     # 평균월급을 오름차순 정렬
  head(10)

bottom10

# 7) 그래프로 시각화
ggplot(data=bottom10, aes(x=reorder(job,-mean_income), y=mean_income)) + 
  geom_col() +    # 막대 그래프
  coord_flip()    # x, y축이 바뀜 

#-----------------------------------------------------------------
# 6. 성별 직업 빈도 구하기
#    성별로 어떤 직업이 가장 많을까?

# 1) 남성 직업 빈도 상위 10개 추출 
job_male <- welfare %>% 
  filter(!is.na(job) & sex == "male") %>% 
  group_by(job) %>% 
  summarise(n = n()) %>%   # 남성 직업의 빈도 구하기 
  arrange(desc(n)) %>%     # 빈도가 높은직업순으로 내림차순정렬 
  head(10)

job_male
#    job                        n
#    <chr>                    <int>
# 1 작물재배 종사자            640
# 2 자동차 운전원              251
# 3 경영관련 사무원            213
# 4 영업 종사자                141
# 5 매장 판매 종사자           132
# 6 제조관련 단순 종사원       104
# 7 청소원 및 환경 미화원       97
# 8 건설 및 광업 단순 종사원    95
# 9 경비원 및 검표원            95
# 10 행정 사무원                92

# 2) 그래프로 시각화
# 남성 직업 빈도 상위 10개 직업을 그래프 
ggplot(data=job_male, aes(x=reorder(job, n), y=n)) + 
  geom_col() +       # 막대 그래프 
  coord_flip()       # x, y축이 바뀜

# 3) 여성 직업 빈도 상위 10개 추출 
job_female <- welfare %>% 
  filter(!is.na(job) & sex == "female") %>% 
  group_by(job) %>% 
  summarise(n = n()) %>%  # 여성 직업의 빈도 구하기
  arrange(desc(n)) %>%    # 빈도가 높은직업순으로 내림차순정렬
  head(10)
job_female
#   job                            n
#   <chr>                        <int>
# 1 작물재배 종사자                680
# 2 청소원 및 환경 미화원          228
# 3 매장 판매 종사자               221
# 4 제조관련 단순 종사원           185
# 5 회계 및 경리 사무원            176
# 6 음식서비스 종사자              149
# 7 주방장 및 조리사               126
# 8 가사 및 육아 도우미            125
# 9 의료 복지 관련 서비스 종사자   121
# 10 음식관련 단순 종사원          104

# 4) 그래프로 시각화
# 여성 직업 빈도 상위 10개 직업을 그래프
ggplot(data=job_female, aes(x=reorder(job, n), y=n)) + 
  geom_col() +     # 막대 그래프 
  coord_flip()     # x, y축이 바뀜 

#-----------------------------------------------------------------
# 7. 종교 유무에 따른 이혼율 분석
#    종교가 있는 사람들이 이혼을 덜 할까?

# 1) 변수 검토 
#  religion : 종교유무 , marriage : 결혼여부   
class(welfare$religion)
# "numeric"                 숫자 데이터 

table(welfare$religion)    # 종교유무 
# 1     2                  # 1:종교있음, 2:종교없음, 9:모름/무응답 
# 8047  8617 

class(welfare$marriage)
# "numeric"                숫자 데이터 

table(welfare$marriage)    # 결혼여부                       
#  0    1    2    3     4    5     6 
# 2861 8431 2117  712   84  2433   26

# 0 : 비해당(18세 미만)
# 1 : 유배우자(결혼) 
# 2 : 사별 
# 3 : 이혼 
# 4 : 별거 
# 5 : 미혼(18세 이상, 미혼모 포함)
# 6 : 기타(사망 등)

# 2) 전처리
#  종교 유무 값 수정 
#  religion 변수의  1 -> yes, 2 -> no 수정 
welfare$religion <- ifelse(welfare$religion==1,"yes","no")
table(welfare$religion)
# no   yes 
# 8617 8047

# 이혼여부를 저장하는 파생변수 생성 : group_marriage
#  marriage 변수의  1(결혼)  -> marriage, 3(이혼) -> divorce
welfare$group_marriage <- ifelse(welfare$marriage==1, "marriage",
                                 ifelse(welfare$marriage==3, "divorce", NA))
table(welfare$group_marriage)
# divorce  marriage 
# 712      8431 

# 결측 데이터 확인 : marriage : 0, 2, 4, 5, 6
table(is.na(welfare$group_marriage))  #  TRUE : 7521
# FALSE  TRUE 
# 9143   7521 

# 빈도 그래프 출력
qplot(welfare$group_marriage)

# 3) 종교 유무에 따른 이혼율 분석하기
# 방법1.
religion_marriage <- welfare %>% 
  filter(!is.na(group_marriage)) %>%     
  group_by(religion, group_marriage) %>%
  summarise(n = n()) %>% 
  mutate(tot_group = sum(n)) %>% 
  mutate(pct = round(n/tot_group*100, 1))
religion_marriage
# religion  group_marriage    n   tot_group   pct
# <chr>      <chr>          <int>     <int> <dbl>
# 1 no       divorce          384      4602   8.3
# 2 no       marriage        4218      4602  91.7
# 3 yes      divorce          328      4541   7.2
# 4 yes      marriage        4213      4541  92.8

# 방법2.
religion_marriage <- welfare %>% 
  filter(!is.na(group_marriage)) %>% 
  count(religion, group_marriage) %>% 
  group_by(religion) %>% 
  mutate(pct= round(n/sum(100),1))
religion_marriage
#   religion group_marriage     n   pct
#   <chr>    <chr>          <int> <dbl>
# 1 no       divorce          384   3.8
# 2 no       marriage        4218  42.2
# 3 yes      divorce          328   3.3
# 4 yes      marriage        4213  42.1

# 이혼(divorce) 데이터 추출
divorce <- religion_marriage %>% 
  filter(group_marriage == 'divorce') %>% 
  select(religion, pct)

divorce
# religion     pct
# <chr>       <dbl>
# 1 no         8.3
# 2 yes        7.2

# 그래프로 시각화
ggplot(data = divorce, aes(x= religion, y=pct)) + geom_col()

# 4) 연령대(ageg)별 이혼율 분석 하기
#  연령대 (ageg)
#  0  ~ 29 : young
#  30 ~ 59 : middle
#  60이상  : old

ageg_marriage <- welfare %>% 
  filter(!is.na(group_marriage)) %>%      # 결측치 제거 
  group_by(ageg, group_marriage) %>% 
  summarise(n = n()) %>%                  # 빈도(인원수)구하기
  mutate(tot_group = sum(n)) %>%          # ageg별 합 구하기
  mutate(pct = round(n/tot_group*100, 1)) # 백분율 구하기 
ageg_marriage
#  ageg    group_marriage  n    tot_group   pct
#  <chr>   <chr>          <int>     <int>  <dbl>
# 1 middle divorce          437      4918   8.9
# 2 middle marriage        4481      4918  91.1
# 3 old    divorce          273      4165   6.6
# 4 old    marriage        3892      4165  93.4
# 5 young  divorce            2        60   3.3
# 6 young  marriage          58        60  96.7

# 이혼(divorce) 데이터 추출
ageg_divorce <- ageg_marriage %>% 
  filter(group_marriage == 'divorce') %>% 
  select(ageg, pct)

ageg_divorce
#   ageg     pct
#   <chr>   <dbl>
# 1 middle   8.9
# 2 old      6.6
# 3 young    3.3

#  그래프로 시각화
ggplot(data = ageg_divorce, aes(x=ageg, y=pct)) + geom_col()

# 5) 연령대 및 종교 유무에 따른 이혼율 분석하기
ageg_religion_marriage <- welfare %>% 
  filter(!is.na(group_marriage)) %>% 
  group_by(ageg, religion, group_marriage) %>% 
  summarise(n = n()) %>% 
  mutate(tot_group = sum(n)) %>% 
  mutate(pct = round(n/tot_group*100, 1))
ageg_religion_marriage
# ageg   religion  group_marriage   n     tot_group pct
# <chr>   <chr>     <chr>          <int>     <int>  <dbl>
# 1 middle no       divorce          260      2681   9.7
# 2 middle no       marriage        2421      2681  90.3
# 3 middle yes      divorce          177      2237   7.9
# 4 middle yes      marriage        2060      2237  92.1
# 5 old    no       divorce          123      1884   6.5
# 6 old    no       marriage        1761      1884  93.5
# 7 old    yes      divorce          150      2281   6.6
# 8 old    yes      marriage        2131      2281  93.4
# 9 young  no       divorce            1        37   2.7
# 10 young  no       marriage          36        37  97.3
# 11 young  yes      divorce            1        23   4.3
# 12 young  yes      marriage          22        23  95.7

# 이혼(divorce) 데이터 추출
df_divorce <- ageg_religion_marriage %>% 
  filter(group_marriage == 'divorce') %>% 
  select(ageg, religion, pct)

df_divorce
#  ageg    religion   pct
#  <chr>   <chr>     <dbl>
# 1 middle no         9.7
# 2 middle yes        7.9
# 3 old    no         6.5
# 4 old    yes        6.6
# 5 young  no         2.7
# 6 young  yes        4.3

# 그래프로 시각화
# 연령대 및 종교 유무에 따른 이혼율 그래프 
ggplot(data = df_divorce, aes(x=ageg, y=pct, fill=religion)) + geom_col()


# religion 유무에 따라 막대 그래프 분리
ggplot(data = df_divorce, aes(x=ageg, y=pct, fill=religion)) + 
  geom_col(position = "dodge")      # 막대 그래프 

#-----------------------------------------------------------------
# 8. 지역별 연령대 비율
#    노년층이 많은 지역은 어디일까?

# 지역코드 : code_region (1 ~ 7)
# 연령대 : ageg (young, middle, old)

# 1) 변수 검토하기
class(welfare$code_region)
# "numeric"                  숫자 데이터

table(welfare$code_region)
#   1    2    3    4    5    6    7 
# 2486 3711 2785 2036 1467 1257 2922 

# 2) 전처리 
# 1:서울, 2:수도권(인천,경기), 3:부산/경남/울산
# 4:대구/경북, 5:대전/충남, 6:강원/충북, 7:광주/전남/전북/제주도 

#  i) 지역코드와 지역명을 가진 데이터프레임 생성 : list_region
list_region <- data.frame(code_region = c(1:7),
                          region = c("서울",
                                     "수도권(인천,경기)",
                                     "부산/경남/울산",
                                     "대구/경북",
                                     "대전/충남",
                                     "강원/충북",
                                     "광주/전남/전북/제주도"))
list_region

#  ii) welfare와 list_region 데이터프레임을 가로방향으로 합치기
welfare <- left_join(welfare, list_region, by='code_region')

# 합쳐진 데이터프레임 확인 
welfare %>% select(code_region, region) %>% head()

# 3) 지역별, 연령대 비율 분석하기
region_ageg <- welfare %>% 
  group_by(region, ageg) %>% 
  summarise(n = n()) %>% 
  mutate(tot_group = sum(n)) %>% 
  mutate(pct = round(n/tot_group*100, 1))
region_ageg
View(region_ageg)
# region                 ageg       n tot_group   pct
#   <chr>                 <chr>   <int>     <int> <dbl>
# 1 강원/충북             middle   417      1257  33.2
# 2 강원/충북             old      555      1257  44.2
# 3 강원/충북             young    285      1257  22.7
# 4 광주/전남/전북/제주도 middle   947      2922  32.4
# 5 광주/전남/전북/제주도 old     1233      2922  42.2
# 6 광주/전남/전북/제주도 young    742      2922  25.4
# 7 대구/경북             middle   637      2036  31.3
# 8 대구/경북             old      928      2036  45.6
# 9 대구/경북             young    471      2036  23.1
# 10 대전/충남            middle   548      1467  37.4
#  ..............

# 노년층 비율이 낮은순으로 데이터 구하기
list_order_old <- region_ageg %>% 
  filter(ageg == 'old') %>%   # ageg가 old 정보 추출 
  arrange(pct)                # 오름 차순 정렬 
list_order_old
#  region                 ageg    n tot_group   pct
#  <chr>                 <chr> <int>     <int> <dbl>
# 1 수도권(인천,경기)     old    1109      3711  29.9
# 2 서울                  old     805      2486  32.4
# 3 대전/충남             old     527      1467  35.9
# 4 부산/경남/울산        old    1124      2785  40.4
# 5 광주/전남/전북/제주도 old    1233      2922  42.2
# 6 강원/충북             old     555      1257  44.2
# 7 대구/경북             old     928      2036  45.6

# 정렬된 지역명 순서를 저장하는 변수 만들기
order <- list_order_old
order

# 그래프로 시각화
ggplot(data=region_ageg, aes(x = region, y = pct, fill = ageg)) + 
  geom_col() +                       # 막대 그래프 
  coord_flip() +                     # x, y축을 바꿈 
  scale_x_discrete(limits = order)   # 노년층 비율이 높은지역부터 출력 

# scale_x_discrete(limits = order) 마지막줄 에러남 확인 바람

