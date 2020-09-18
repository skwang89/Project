# 구글차트
install.packages('googleVis')
library(googleVis)

Fruits

plot(Fruits)

#--------------------------------------------------------------------
# 예. 서울 지하철 2호선 강남역 시간대별 승하차 현황
install.packages('googleVis')
library(googleVis)

line_2 <- read.csv("data/2호선_강남역_시간대별_승하차현황_세로.csv",
                   header=T, sep=",")
line_2

t1 <- gvisMotionChart(line_2, idvar="line_no", timevar="time",
                      option=list(width=1000, height=500))
plot(t1)

#--------------------------------------------------------------------
# 예. GoogleMap을 사용하여 지도상에 storm의 이동경로를 표시

install.packages("googleVis")
library(googleVis)

data(Andrew)
Andrew
storm1 <- gvisMap(Andrew, "LatLong", "Tip",
                  options = list(showTip=TRUE, showLine=TRUE,
                  enableScrollWheel=TRUE,
                  mapType='hybrid', useMapTypeControl=TRUE,
                  width=800, height=400))
plot(storm1)

#---------------------------------------------------------------------
# 예. GoogleMap을 이용해서 서울시 구청 위치를 지도에 표시
install.packages("googleVis")
library(googleVis)

loc <- read.csv("data/서울시구청위치정보_new.csv", header=T)
loc

hoffice <- gvisMap(loc, "LATLON", "name",
                   options=list(showTip=TRUE, showLine=TRUE,
                                enableScrollWheel=TRUE, mapType='normal',
                                useMapTypeControl=TRUE, width=1000,height=400))
hoffice$html$header <- gsub('charset=uts-8',
                            'charset=euc-kr',
                            hoffice$html$header)
plot(hoffice)

#---------------------------------------------------------------------
# seoul 지도 출력

# 패키지 설치
install.packages('ggmap')
install.packages('Rcpp')

# 패키지 로딩
library(ggmap)
library(Rcpp)

# APIkey를 라이브러리에 등록 : 본인의 key를 등록 해서 사용
register_google(key = 'AIzaSyC5S4zaVBJEG0Nh4ovde1Q6H-sFh16yRcg')

# 한글 지역명(시 단위)을 utf-8형식으로 위도와 경도로 변환
gc <- geocode(enc2utf8('런던'))
gc
#   lon   lat
#  <dbl> <dbl>
#1  127.  37.6

# 위도와 경도를 숫자형식으로 변환
cen <- as.numeric(gc)
cen
# 126.97797  37.56654

# 위도와 경도를 중심으로 하는 지도 정보 반환
# zoom : 지도 크기로서 3(대륙)~21(건물)의 정수(기본값:10)
# maptype : 출력되는 지도 유형
# : terrain(지형 정보기반 지도)
# : satellite(위성지도)
# : roadmap(도로명 표시)
# : hybrid(위성과 도로명)
map <- get_googlemap(center = cen, zoom = 10,
                     maptype = 'roadmap',
                     markers = gc)

# 지도 출력
# 지도 출력
# extent : 출력 창에서 지도가 차지하는 영역의 형태
# : 'normal', 'device', 'panel'의 3가지 형태로 설정.
# : 'panel' 타입이 디폴트
# : 'device'는 지도를 출력창에 여백없이 출력
ggmap(map, extent = 'panel')

#------------------------------------------------------------------
# 제주도 관광지 지도 출력 

# 패키지 설치
install.packages('ggmap')
install.packages('Rcpp')

# 패키지 로딩
library(Rcpp)
library(ggmap)

# APIkey를 라이브러리에 등록 : 본인의 key를 등록 해서 사용
register_google(key = 'AIzaSyC5S4zaVBJEG0Nh4ovde1Q6H-sFh16yRcg')

# 각 지역 이름
names <- c("용두암","성산일출봉","정방폭포",
           "중문관광단지","한라산1100고지","차귀도")

# 각 지역의 주소
addr <- c("제주시 용두암길 15",
          "서귀포시 성산읍 성산리",
          "서귀포시 동홍동 299-3",
          "서귀포시 중문동 2624-1",
          "서귀포시 색달동 산1-2",
          "제주시 한경면 고산리 125")

# 각 지역 주소의 위도, 경도 구하기
gc <- geocode(enc2utf8(addr))
gc
#    lon   lat
#    <dbl> <dbl>
# 1  127.  33.5
# 2  127.  33.5
# 3  127.  33.3
# 4  126.  33.3
# 5  126.  33.4
# 6  126.  33.3

# 각 지역명과 위도, 경도를 가진 데이터 프레임 생성
df <- data.frame(names, 
                 lon=gc$lon,
                 lat=gc$lat)
df

# 중심 좌표 계산
# : 데이터프레임에 있는 모든 경도와 위도에 대한 평균치
cen <- c(mean(df$lon), mean(df$lat))
cen
# 126.51905  33.36025

# 지도 생성
map <- get_googlemap(center = cen,
                     maptype = "roadmap",
                     zoom = 9,
                     # size = c(800, 800),
                     markers = gc)

# 지도 출력
ggmap(map) + geom_text(data = df, aes(x=lon, y=lat),
                       size=3, label=df$names)

