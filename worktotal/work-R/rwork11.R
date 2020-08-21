# rwork11.R start
# <<교재 12장 시작>>


# plotly 패키지로 인터랙티브 그래프 만들기

# 패키지 준비하기
install.packages("plotly")
library(plotly)

# ggplot2로 그래프 그리기
library(ggplot2)

p <- ggplot(data=mpg, aes(x=displ, y=hwy, col=drv)) + 
  geom_point()     # 산점도 

# 인터렉티브 그래프 그리기
ggplotly(p)

# 인터렉티브 막대 그래프 그리기
p <- ggplot(data = diamonds, aes(x = cut, fill = clarity)) +
  geom_bar(position = "dodge")


# 인터렉티브 그래프 그리기
ggplotly(p)

# ----------------------------------------------------------------
# cf. ggThemeAssist 패키지 활용하기
ggThemeAssistGadget(p)

# ggThemeAssist 패키지 : 그래프 옵션들을 쉽게 설정
install.packages("ggThemeAssist")
library(ggThemeAssist)
# ggThemeAssist Tab기능 설명: 
# 출처:https://m.blog.naver.com/youji4ever/221508769676

# Settings
# width와 Height로 가로와 세로 크기가 최대 10과 5로 기본 설정되어 있다.
# General options에 Multiline results에 체크 하면 두 줄로 코드가 분리된다.
# 이렇게 하면 코드를 한 줄로 결합하지 않고, plot.subtitle설정과
# plot.caption의 설정을 따로따로 분리하여 생성한다.
# 코드가 분리되면 처리 과정의 최적화는 부족할 수 있으나 
# 코드 파악이 쉽고 응용하기도 수월하다.

# Panel&Background
# -Plot Background: 배경 설정
#   fill: 그래프 배경색
#   type: 테두리 종류 
#   size: 테두리 선 굵기
#   colour: 테두리 선 색상
# - Panel Background: 그래프 영역 설정
# 그래프 안쪽 영역(panel)의 배경 설정. 그래프 배경색과 달리 그래프
# 안의 분석된 결과를 강조하고 싶을 때 설정한다.
# - Grid Magor: x, y축 경계 영역 설정
# x축과 y축의 주 눈금선(grid magor), 즉 경계 영역을 강조하여 경계 값을
# 뚜렷하게 표현하고자 할 때 설정한다.
# - Grid Miner: x, y축 경계 보조 영역 설정
# 주 눈금선을 보조하는 보조 눈금선이라고 생각하면 된다.  주 눈금선이
# 너무 눈에 띈다든가 해서 시각화로 구분이 어려울 경우 보조하는 의미다.

# Axis
# - Axis text: x, y축 텍스트
# x축과 y축의 텍스트를 하나의 옵션으로 동일하게 설정한다.
# - Axis text x, y: x, y축 각각 텍스트 설정
# 앞에 방법이 x축과 y축의 텍스트를 하나의 옵션으로 동일하게 설정하다면
# 이 옵션은 Axis text x, Axis text y로 각각 따로 설정할 수 있다.
# - Axis line, Axis ticks: x, y축 설정
# Axis.line과 Axis ticks로 각각 x축과 y축 선을 강조하도록 설정할 수 있다.

# Title and label 
# Lable에서 그래프 제목과 x축 이름, y축 이름을 설정하고 범례 텍스트 등을 
# 설정할 수 있다. 
# Plot Title에서 그래프 제목의 텍스트 서식을 지정할 수있으며,
# Axis Lables는 x, y축 이름 텍스트의 서식을 지정한다.
# 둘다 폰트 종류, 크기, 색상, 위치, 기울기 등을 설정할 수 있다.
ggThemeAssistGadget(p)
# Legend
# 범례위치·제목·배경·키 요소들을 상세하게
# 설정할 수 있다.

# Subtitle and Caption
# 그래프제목 아래 부제목과 설명문을 추가할 있다. 이미지를 직접 워드나
# 파워포인트에 추가하여 다른 편집없이 R에서 보고서를 작성하거나, 
# R 마크다운으로 웹 보고서를 자동화할 때 부족한 그래프 설명을
# 첨부할 수 있다.
# -------------------------------------------------------------------

# dygraphs 패키지로 인터랙티브 시계열 그래프 만들기

# 패키지 준비하기
install.packages("dygraphs")
library(dygraphs)

# 데이터 준비하기
economics <- ggplot2::economics
head(economics)
# A tibble: 6 x 6
# date         pce    pop psavert uempmed unemploy
# <date>     <dbl>  <dbl>   <dbl>   <dbl>    <dbl>
#   1 1967-07-01  507. 198712    12.6     4.5     2944
# 2 1967-08-01  510. 198911    12.6     4.7     2945
# 3 1967-09-01  516. 199113    11.9     4.6     2958
# 4 1967-10-01  512. 199311    12.9     4.9     3143
# 5 1967-11-01  517. 199498    12.8     4.7     3066
# 6 1967-12-01  525. 199657    11.8     4.8     3018

# 시간 순서 속성을 지니는 xts 데이터 타입으로 변경
library(xts)
eco <- xts(economics$unemploy, order.by = economics$date)
head(eco)
#            [,1]
# 1967-07-01 2944
# 1967-08-01 2945
# 1967-09-01 2958
# 1967-10-01 3143
# 1967-11-01 3066
# 1967-12-01 3018

eco

# 인터렉티브 시계열 그래프 그리기
dygraph(eco)

# 그래프 아래에 날짜 범위 선택 기능 추가
dygraph(eco) %>% dyRangeSelector()

# 저축률과 실업자수의 관계를 인터렉티브 그래프로 출력 
# 저축률
eco_a <- xts(economics$psavert, order.by = economics$date)

# 실업자 수: 1000으로 나눠서 100만명 단위로 설정
eco_b <- xts(economics$unemploy/1000, order.by = economics$date)

# 합치기
eco2 <- cbind(eco_a, eco_b)   # 데이터 결합

# 변수명 바꾸기: eco_a -> psavert, eco_b -> unemploy
colnames(eco2) <- c("psavert", "unemploy")
head(eco2)
#             psavert unemploy
# 1967-07-01     12.6    2.944
# 1967-08-01     12.6    2.945
# 1967-09-01     11.9    2.958
# 1967-10-01     12.9    3.143
# 1967-11-01     12.8    3.066
# 1967-12-01     11.8    3.018

# 저축률과 실업자수 관계를 인터렉티브 시계열 그래프 그리기
dygraph(eco2) %>% dyRangeSelector()


# <<교재 12장 끝>>
# rwork11.R end
