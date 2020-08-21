# rwork7.R start
# <<교재 8장 시작>>


# 데이터 시각화

# 정형 데이터를 시각화: 그래프
# 정형 데이터 예: 데이터베이스의 데이터, 엑셀파일, csv파일

# 비정형 데이터 시각화: wordcloud
# 비정형 데이터 예: text파일

# ggplot2 패키지 설치
install.packages("ggplot2")

# ggplot2 패키지 로딩
library(ggplot2)

# 1. 산점도
#    데이터를 x축과 y축에 점으로 표현한 그래프

# 1) 배경 설정하기 
#    x축 displ(배기량), hwy(고속도로 연비)
ggplot(data = mpg, aes(x=displ, y=hwy))


# 2) 산점도 그래프 그리기
ggplot(data = mpg, aes(x=displ, y=hwy)) + geom_point()

# 3) x축 범위(3~6), y축 범위(10~30)으로 설정
ggplot(data = mpg, aes(x=displ, y=hwy)) + 
  geom_point() +
  xlim(3, 6) +
  ylim(10, 30)

# ggplot() vs qplot()
# • qplot() : 전처리 단계 데이터 확인용 문법 간단, 기능 단순
# • ggplot() : 최종 보고용. 색, 크기, 폰트 등 세부 조작 가능

# ================================================================
# 혼자서 해보기
# mpg 데이터와 midwest 데이터를 이용해서 분석 문제를 해결해 보세요.
# • Q1. mpg 데이터의 cty(도시 연비)와 hwy(고속도로 연비) 간에 어떤
# 관계가 있는지 알아보려고 합니다.
# x 축은 cty, y 축은 hwy 로 된 산점도를 만들어 보세요.
library(ggplot2)
mpg <- as.data.frame(ggplot2::mpg)
ggplot(data=mpg, aes(x=cty, y=hwy)) +
  geom_point()

# • Q2. 미국 지역별 인구통계 정보를 담은 ggplot2 패키지의 midwest
# 데이터를 이용해서 전체 인구와 아시아인 인구 간에 어떤 관계가
# 있는지 알아보려고 합니다. x 축은 poptotal(전체 인구), y 축은
# popasian(아시아인 인구)으로 된 산점도를 만들어 보세요. 
# 전체 인구는 50 만 명 이하, 아시아인 인구는 1 만 명 이하인 지역만
# 산점도에 표시되게 설정하세요.
midwest <- as.data.frame(ggplot2::midwest)
ggplot(data=midwest, aes(x=poptotal, y=popasian)) +
  geom_point() +
  xlim(0, 500000) +
  ylim(0, 10000)
# ================================================================


# 2. 막대 그래프
#    데이터의 크기를 막대의 길이로 표현한 그래프 
#    성별 소득 차이처럼 집단 간 차이를 표현할 때 주로 사용

# 1) 데이터 불러오기
library(dplyr)
mpg <- as.data.frame(ggplot2::mpg)

#  drv(구동방식) : 4(4륜구동), f(전진구동), r(후진구동)
df_mpg <- mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy = mean(hwy))
df_mpg
#   drv     mean_hwy
# 1  4         19.2
# 2  f         28.2
# 3  r         21 

# 2) 막대 그래프 그리기
ggplot(data=df_mpg, aes(x=drv, y=mean_hwy)) + geom_col()

# 3) 막대 그래프의 크기 순으로 정렬하기
#    i)작은 크기에서 큰 크기 순으로 정렬
ggplot(data=df_mpg, aes(x=reorder(drv,mean_hwy), y=mean_hwy)) + 
  geom_col()

#   ii) 큰 크기에서 작은 크기 순으로 정렬
ggplot(data=df_mpg, aes(x=reorder(drv, -mean_hwy), y=mean_hwy)) + 
  geom_col()

# 3. 빈도 막대 그래프
#    : 값의 갯수를 막대의 길이로 표현한 그래프

# i) drv(구동방식) 빈도 막대 그래프 
# x축 : drv(구동방식), y축 : 빈도 
ggplot(data=mpg, aes(x=drv)) + geom_bar()

table(mpg$drv)      # drv 빈도 구하기

# 4   f    r 
# 103 106  25 

# ii) hwy(고속도로 연비) 빈도 막대 그래프
# x축 : hwy(고속도로 연비),  y : 빈도(자동차 대수)
ggplot(data=mpg, aes(x=hwy)) + geom_bar()

# geom_col() VS geom_bar()
# • 평균 막대 그래프 : 데이터를 요약한 평균표를 먼저 만든 후
# 평균표를 이용해 그래프 생성 - geom_col()
# • 빈도 막대 그래프 : 별도로 표를 만들지 않고 원자료를 이용해 바로
# 그래프 생성 - geom_bar()

# ================================================================
# 혼자서 해보기
# mpg 데이터를 이용해서 분석 문제를 해결해 보세요.
# • Q1. 어떤 회사에서 생산한 "suv" 차종의 도시 연비가 높은지
# 알아보려고 합니다. "suv" 차종을 대상으로 평균 cty(도시 연비)가
# 가장 높은 회사 다섯 곳을 막대 그래프로 표현해 보세요. 
# 막대는 연비 가 높은 순으로 정렬하세요.
df <- mpg %>% 
  filter(class == 'suv') %>% 
  group_by(manufacturer) %>% 
  summarise(mean_cty = mean(cty)) %>% 
  arrange(desc(mean_cty)) %>% 
  head(5)
ggplot(data = df, aes(x=reorder(manufacturer, -mean_cty), 
                      y=mean_cty)) + geom_col()
  

# • Q2. 자동차 중에서 어떤 class(자동차 종류)가 가장 많은지
# 알아보려고 합니다. 자동차 종류별 빈도를 표현한 막대 그래프를
# 만들어 보세요.
ggplot(data=mpg, aes(x=class)) +geom_bar()
# ================================================================

# 4. 선그래프 
#    : 데이터를 선으로 표현한 그래프
#      주가지수, 환율과 같이 시간적인 흐름에 따라 데이터가 달라지는
#      시계열 데이터를 시각화할때 선 그래프를 많이 사용한다.

# 1) 데이터 불러오기 
economics

# 2) 선그래프 그리기 
ggplot(data=economics, aes(x=date, y=unemploy)) +
  geom_line()

# ================================================================
# 혼자서 해보기
# economics 데이터를 이용해서 분석 문제를 해결해 보세요.
# • Q1. psavert(개인 저축률)가 시간에 따라서 어떻게 변해왔는지
# 알아보려고 합니다. 시간에 따른 개인 저축률의 변화를 나타낸 
# 시계열 그래프를 만들어 보세요.
ggplot(data = economics, aes(x=date, y=psavert)) +geom_line()
# ================================================================

# 5. 상자(박스) 그래프
#    : 데이터의 분포를 직사각형 상자 모양으로 표현한 그래프
#      상자 그래프는 데이터의 분포를 쉽게 확인 할 수 있는 그래프

# 1) drv(구동방식)에 따른 hwy(고속도로 연비) 정보를 
#    상자그래프로 출력
#    x축 : drv(구동방식), y축 : hwy(고속도로 연비)
ggplot(data=mpg, aes(x=drv, y=hwy)) + geom_boxplot()

# ================================================================
# 혼자서 해보기
# mpg 데이터를 이용해서 분석 문제를 해결해 보세요.
# • Q1. class(자동차 종류)가 "compact", "subcompact", "suv"인
# 자동차의 cty(도시 연비)가 어떻게 다른지
# 비교해보려고 합니다. 세 차종의 cty를 나타낸 상자 그림을 
# 만들어보세요.
df <- mpg %>% 
  filter(class %in% c('compact', 'subcompact', 'suv'))
ggplot(data=df, aes(x=class, y=cty)) + geom_boxplot()
# ================================================================

# 정리하기
# # 1.산점도
# ggplot(data = mpg, aes(x = displ, y = hwy)) + geom_point()
# # 축 설정 추가
# ggplot(data = mpg, aes(x = displ, y = hwy)) +
#   geom_point() +
#   xlim(3, 6) +
#   ylim(10, 30)

# # 2.평균 막대 그래프
# # 1 단계.평균표 만들기
# df_mpg <- mpg %>%
#   group_by(drv) %>%
#   summarise(mean_hwy = mean(hwy))
# # 2 단계.그래프 생성하기, 크기순 정렬하기
# ggplot(data = df_mpg, aes(x = reorder(drv, -mean_hwy), y = mean_hwy)) + geom_col()

# # 3.빈도 막대 그래프
# ggplot(data = mpg, aes(x = drv)) + geom_bar()

# # 4.선 그래프
# ggplot(data = economics, aes(x = date, y = unemploy)) + 
#         geom_line()

# # 5.상자 그림
# ggplot(data = mpg, aes(x = drv, y = hwy)) + geom_boxplot()


# <<교재 8장 끝>>
# rwork7.R end
