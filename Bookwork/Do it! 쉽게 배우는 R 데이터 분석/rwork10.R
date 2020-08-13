# rwork10.R start
# <<교재 11장 시작>>


# 단계 구분도(Choropleth Map)
# ● 지역별 통계치를 색깔의 차이로 표현한 지도
# ● 인구나 소득 같은 특성이 지역별로 얼마나 다른지 쉽게 이해할 수 있음

# 패키지 설치
install.packages("ggiraphExtra")
library(ggiraphExtra)

# 데이터 확인하기
str(USArrests)

# 상위 6개 데이터 확인
head(USArrests)
#              Murder Assault UrbanPop Rape
# Alabama      13.2     236       58 21.2
# Alaska       10.0     263       48 44.5
# Arizona       8.1     294       80 31.0
# Arkansas      8.8     190       50 19.5
# California    9.0     276       91 40.6
# Colorado      7.9     204       78 38.7

# 주(state)에 대한 변수 설정 : state
library(tibble)

crime <- rownames_to_column(USArrests, var = "stste")
head(crime)
#      state   Murder Assault UrbanPop Rape
# 1    Alabama   13.2     236       58 21.2
# 2     Alaska   10.0     263       48 44.5
# 3    Arizona    8.1     294       80 31.0
# 4   Arkansas    8.8     190       50 19.5
# 5 California    9.0     276       91 40.6
# 6   Colorado    7.9     204       78 38.7

# 주(state) 데이터를 소문자로 변경
crime$stste <- tolower(crime$stste)
head(crime)
#        state Murder Assault UrbanPop Rape
# 1    alabama   13.2     236       58 21.2
# 2     alaska   10.0     263       48 44.5
# 3    arizona    8.1     294       80 31.0
# 4   arkansas    8.8     190       50 19.5
# 5 california    9.0     276       91 40.6
# 6   colorado    7.9     204       78 38.7

crime <- rename(crime, 'state'='stste')
head(crime)


# map출력을 위한 패키지 설치
install.packages("maps")
library(maps)

# 미국 주(state)지도 데이터 불러오기
library(ggplot2)

state_map <- map_data("state")
str(state_map)
head(state_map)
state_map

# 단계 구분도
install.packages("mapproj")
library(mapproj)

ggChoropleth(data = crime,          # 지도에 표시할 데이터
             aes(fill = Murder,     # 색깔로 표현할 변수
                 map_id = state),   # 지역 기준 변수
             map = state_map)      # 지도 데이터

# 인터렉티브 단계 구분도
ggChoropleth(data = crime,
             aes(fill = Murder,
                 map_id = state),
             map = state_map,
             interactive = T)

#-------------------------------------------------------------
# 대한민국 시도별 인구 단계 구분도

# 패키지 설치하기
install.packages("stringi")

install.packages("devtools")
devtools::install_github("cardiomoon/kormaps2014")

library(kormaps2014)

# 대한민국 시도별 인구 데이터 준비하기

# kormaps2014 패키지 
# 데이터 이름       내용
#-------------------------------
# korpop1          시도별
# korpop2          시군구별
# korpop3          읍면동별 

# 대한민국 시도별 인구 데이터
# changeCode() : korpop1데이터의 UTF-8 데이터를 CP949로 변환
str(korpop1)
str(changeCode(korpop1))


# 변수명 변경 
# 총인구_명 -> pop
# 행정구역별_읍면동 -> name
library(dplyr)
korpop1 <- rename(korpop1,
                  pop = 총인구_명,
                  name = 행정구역별_읍면동)
head(korpop1)
dim(korpop1)      # 17행 25열
View(korpop1)
str(changeCode(korpop1))

# name 변수 깨지지 않도록 처리
korpop1$name <- iconv(korpop1$name, "UTF-8", "CP949")

# 단계 구분도
ggChoropleth(data = korpop1,       # 지도에 표현할 데이터
             aes(fill = pop,       # 색깔로 표현할 변수
                 map_id = code,    # 지역 기준 변수
                 tooltip = name),  # 지도위에 표시할 지역명 
             map = kormap1,        # 지도 데이터
             interactive = T)     # 인터랙티브 

#--------------------------------------------------------------
# 대한민국 시도별 결핵 환자수 단계 구분도 만들기
# kormaps2014 패키지 안에는 지역별 결핵환자수에 대한 정보를 
# 가지고 있는 tbc 데이터 활용 

# 데이터 확인
str(changeCode(tbc))
# name : 지역명
# NewPts : 결핵환자수 

# name변수 데이터 인코딩을  변환 : UTF-8  --> CP949 변환
tbc$name <- iconv(tbc$name, "UTF-8", "CP949")


# 단계 구분도 만들기
ggChoropleth(data = tbc,          # 지도에 표현할 데이터
             aes(fill = NewPts,   # 색깔로 표현할 변수(결핵환자수)
                 map_id = code,   # 지역 기준 변수
                 tooltip = name), # 지도 위에 표시할 지역명
             map = kormap1,       # 지도 데이터 
             interactive = T)     # 인터렉티브 


# <<교재 11장 끝>>
# rwork10.R end



