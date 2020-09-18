#  지도 활용하기
#  google API를 이용한 위치정보(위도, 경도) 구하기
#  Folium 라이브러리를 이용한 지도 만들기

# Google API 활용하기
# 구글 지오코딩(geocoding)이란 특정 위치나 주소를 입력하면 위도와 경도
# 좌표 정보를 제공해 주는 서비스 이다.
# 이 서비스를 이용하려면 사용자 인증 후에 google API 키를 발급 받아야 한다.
# google API 키를 발급 받는 과정에 본인의 신용카드 정보를 등록해야 한다.
# 구글 지오코딩 API를 이용하기 위해서는 구글 API키를 발급 받아야 되고,
# googlemaps 모듈을 설치해야 사용핛 수 있다.

# 1. 구글 API 키 발급 받기
# 2. googlemaps 모듈 설치하기
# pip install googlemaps

# 구글 지오코딩 API를 이용한 위치정보 구하기 예제
import googlemaps
import pandas as pd

# my_key = "본인이 발급받은 API키를 입력"
my_key = "AIzaSyC5S4zaVBJEG0Nh4ovde1Q6H-sFh16yRcg"
# 구글 맵스 객체 생성
maps = googlemaps.Client(my_key)
# 위도,경도 리스트 생성
lat = []
lng = []
# 위도, 경도를 구하기 위한 지역
places = ['서울시청','국립국악원','해운대해수욕장','제주도','독도','런던','seoul','london','한국','북한']
# 각 지역의 위도, 경도를 구해서 lat, lng 리스트에 저장
i = 0
for p in places:
    i = i + 1
    print(i, p )
    geo_location = maps.geocode(p)[0].get('geometry')
    lat.append(geo_location['location']['lat'])
    lng.append(geo_location['location']['lng'])
# 데이터 프레임 생성
df = pd.DataFrame({'위도':lat, '경도':lng}, index=places)
print(df)

# Folium 라이브러리를 이용한 지도 만들기
#  Folium 라이브러리는 지도를 시각화 할 때 유용한 도구이다.
#  세계 지도를 기본적으로 지원하고 다양핚 스타일의 지도 이미지를 제공하고 있다.
#  Folium은 웹 기반으로 지도를 만들기 때문에, PyCharm이나 스파이더(Spyder)
# 같은 IDE 프로그램에서 실행해도 지도가 표시되지 않는다.
# 지도를 보려면 지도 객체를 save() 함수로 HTML 파일로 저장하고, 웹브라우저로
# 저장된 HTML파일을 열어서 확인해야 한다.
# Jupyter Notebook 등 웹 기반 IDE 프로그램에서는 지도를 바로 확인 할 수 있다.

# 서울 지도 만들기
import folium
import webbrowser

# 서울 지도 만들기
seoul_map = folium.Map(location=[37.566535, 126.977969], zoom_start=11)
seoul = 'seoul.html'
# 서울 지도를 HTML 파일로 저장
seoul_map.save(seoul)
# 브라우저 실행
# webbrowser.open(seoul)
# 크롬으로 실행
Chrome = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register(name=Chrome, klass=None,
                    instance=webbrowser.BackgroundBrowser(Chrome),
                    preferred=True)
webbrowser.open(seoul)

#  서울 지도 만들기
#  지도 스타일 적용하기
# Map() 함수에 titles 옵션을 적용하면 지도 스타일을 변경핛 수 있다.
seoul_map2 = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain',
zoom_start=12)
seoul_map3 = folium.Map(location=[37.55,126.98], tiles='Stamen Toner',
zoom_start=15)

# 지도에 스타일 적용
import folium
# 서울 지도 만들기
seoul_map2 = folium.Map(location=[37.55,126.98], zoom_start=12,
                        tiles='Stamen Terrain')

seoul_map3 = folium.Map(location=[37.55,126.98], zoom_start=15,
                        tiles='Stamen Toner')
# 지도를 html파일로 저장
seoul_map2.save('seoul2.html')
seoul_map3.save('seoul3.html')

# 서울 지도 만들기 : 지도에 마커 표시하기
# 서울 시내 주요 대학교의 위치 데이터 파일(서울지역 대학교 위치.xlsx)을
# 읽어와서, 해당 대학교에 마커를 표시하고, 해당 대학교의 위치의 마커를
# 클릭했을 때 팝업 메시지가 나타난다.
#  라이브러리 설치하기
# pip install xlrd
# pip install pandas
# pip install folium
#  지도에 마커 표시하기
# for name, lat, lng in zip(df.collage, df.위도, df.경도):
# folium.Marker([lat, lng], popup=name).add_to(seoul_map)

# 서울에 위치한 대학교에 마커 표시하기
import pandas as pd
import folium
import webbrowser

# 대학교 목록 읽어오기
df = pd.read_excel('data1/서울지역 대학교 위치.xlsx')
print(df)
# 대학교명이 저장된 컬럼명이 없으므로  collage 컬럼 추가
df.columns = ['collage','위도','경도']
print(df)
# 서울 지도 만들기
seoul_map = folium.Map(location=[37.55, 126.98], zoom_start=12,
                       tiles='Stamen Terrain')
# 대학교 위치에 마커 표시
for name, lat, lng in zip(df.collage, df.위도, df.경도):
    folium.Marker([lat, lng], popup=name).add_to(seoul_map)
# 지도를 HTML 파일로 저장
seoul_map.save('seoul_collages.html')
# 웹브라우저로 지도 출력
webbrowser.open('seoul_collages.html')

# 서울에 위치한 대학교에 원형 마커 표시하기
import pandas as pd
import folium
import webbrowser

# 대학교 목록 읽어오기
df = pd.read_excel('../data1/서울지역 대학교 위치.xlsx')
print(df)
# 대학교명이 저장된 컬럼명이 없으므로  collage 컬럼 추가
df.columns = ['collage','위도','경도']
print(df)
# 서울 지도 만들기
seoul_map = folium.Map(location=[37.55, 126.98], zoom_start=12,
                       tiles='Stamen Terrain')
# 대학교 위치에 CircleMarker 표시
for name, lat, lng in zip(df.collage, df.위도, df.경도):
    folium.CircleMarker([lat, lng],
                        radius = 10,            # 원의 반지름
                        color = 'brown',        # 원의 둘레 색상
                        fill = True,
                        fill_color = 'coral',   # 원을 채우는 색
                        fill_opacity = 0.7,     # 투명도
                        popup=name).add_to(seoul_map)
# 지도를 html파일로 저장
seoul_map.save('seoul_colleges2.html')

# 크롬으로 실행
Chrome = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
webbrowser.register(name=Chrome, klass=None,
                    instance=webbrowser.BackgroundBrowser(Chrome),
                    preferred=True)
webbrowser.open('seoul_colleges2.html')

# 경기도 인구분포 단계구분도(Choropleth Map)
# 행정구역과 같이 지도 상의 어떤 경계에 둘러쌓인 영역에 색을 칠하거나 음영 등으로
# 정보를 나타내는 시각화 방법이다.
# 경기도 지역의 시굮구별 인구 변화 데이터(2007 ~ 2017년), 경기도 행정구역 경계
# 지리 정보를 이용하여 인구수에 따른 경계구분도로 시각화 핚다.
#  단계 구분도
folium.Choropleth(geo_data=geo_data, # 지도 경계
data = df[year], # 표시하려는 데이터
columns = [df.index, df[year]], # 열 지정
fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3,
threshold_scale=[10000, 100000, 300000, 500000, 700000],
key_on='feature.properties.name',
).add_to(g_map)

# 경기도 인구분포 단계구분도(Choropleth Map)
import pandas as pd
import folium
import json

# 경기도 인구 데이터 불러오기
df = pd.read_excel('data1/경기도인구데이터.xlsx',  index_col='구분')
print(df)
print(df.columns)               # 연도가 숫자형으로 출력됨
# 컬럼을 문자형으로 변환: 2017 -> '2017'
df.columns = df.columns.map(str)
# 경기도 시군구 경계 정보를 가진 json 파일 읽어오기
geo_data = json.load(open('data1/경기도행정구역경계.json', encoding='utf8'))
# 경기도 지도 만들기
g_map = folium.Map(location=[37.5502, 126.982], tiles='Stamen Terrain',
                   zoom_start=9)
# 출력할 연도 선택 (2007 ~ 2017년 중에서 선택)
year = '2017'
# Choropleth 함수로 단계구분도 표시하기
folium.Choropleth(geo_data=geo_data,                    # 지도 경계
                  data = df[year],                      # 표시하려는 데이터
                  columns = [df.index, df[year]],       # 열 지정
                  fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3,
                  threshold_scale=[10000, 100000, 300000, 500000, 700000],
                  key_on='feature.properties.name'
                  ).add_to(g_map)
# 지도를 HTML 파일로 저장하기
g_map.save('gyonggi_population_' + year + '.html')

# 데이터 분석
# Log 데이터 분석

# Apache weblog data 분석
# 우리는 인터넷 익스플로러나 크롬 등과 같은 읶터넷 웹브라우저로 웹서버에
# 접속하여 다양한 콘텐츠를 이용합니다. 웹서버는 웹브라우저의 요청에 대해
# 필요한 작업을 수행하고 HTML 페이지를 구성한 후 웹브라우저로 응답합니다.
# 이때 웹서버는 웹브라우저의 요청에 대한 응답 내용을 요약하여 접근로그
# (access log)파일에 기록합니다.
# 오픈 소스읶 아파치 웹서버는 많은 웹 사이트에서 사용하는 읶기 있는 웹서버
# 입니다. 아파치 웹서버가 기록하는 접근로그 파일의 일반적읶 로그 형식은 다음과
# 같습니다.

# Apache weblog data 형식
# 180.76.15.5 - - [15/Nov/2015:03:45:45 +0000] "GET / HTTP/1.1" 200 6812

# 항 목                             설 명
# 180.76.15.5                     웹서버로 요청한 클라이언트 ip주소
#                                 - 무시해도 됨
#                                 - HTTP읶증에 따른 요청 사용자 ID
# [15/Nov/2015:03:45:45 +0000]    웹서버가 응답한 시갂
# "GET / HTTP/1.1"                클라이언트의 요청내용
# 200                             HTTP 상태코드 ( 200 : 정상 응답)
# 6812                            웹서버가 제공한 콘텐츠 크기(byte)

# 1.총 페이지뷰 수 구하기
# Apache Web Server log 파일을 이용해서 사이트 방문자의 총 페이지뷰 수를
# 구해보자?
# 180.76.15.5 - - [15/Nov/2015:03:45:45 +0000] "GET / HTTP/1.1" 200 6812
# 방문자가 웹 사이트에 접속하여 하나의 웹 페이지를 볼 때마다 로그가 한줄 기록
# 되지만, HTTP 상태코드가 200번읶 경우 정상 응답 이기때문에, 접근 로그에서
# 상태코드가 200 읶 라읶을 모두 찾아서 더하면 방문자가 정상적으로 본 총페이지뷰
# 수가 구해진다.

pageviews = 0               # 총 페이지 뷰 수
with open('data1/access_log','r') as f:
    logs = f.readlines()                    # list로 리턴
    for log in logs:
        log = log.split()                   # 공백으로 파싱
        status = log[8]                     # 상태코드(200) 인덱스 8번
        if status == '200':
            pageviews += 1                  # 상태코드가 200이면 총페이지 뷰수 1증가
print('총 페이지뷰:[%d]' %pageviews)
# 총 페이지뷰:[327]

# 2. 고유 방문자 수 구하기
# Apache Web Server log 파읷을 이용해서 사이트 고유 방문자의 수를
# 구해보자?
# 180.76.15.5 - - [15/Nov/2015:03:45:45 +0000] "GET / HTTP/1.1" 200 6812
# 고유 방문자 수는 동읷한 IP를 가진 클라이언트가 웹 사이트에 10번을 접속해도
# 한 사람이 방문한 것으로 계산된다.
# 따라서 접근로그에 기록된 고유한 IP주소 개수를 세면, 고유 방문자 수를 구할
# 수 있다.

visit_ip = []                           # 비어있는 리스트
with open('data1/access_log', 'r') as f:
    logs = f.readlines()                #  list 리턴
    for log in logs:
        log = log.split()               # 공백으로 파싱
        ip = log[0]
        if ip not in visit_ip:          # visit_ip에 ip가 없으면 추가
            visit_ip.append(ip)
print('고유 방문자수:[%d]'%len(visit_ip))
# 고유 방문자수:[99]

# 3. 서비스한 컨텐츠의 총 용량 구하기
# Apache Web Server log 파읷을 이용해서 사이트에서 사용자에게 서비스한
# 컨텐츠의 총 용량을 구해보자?
# 180.76.15.5 - - [15/Nov/2015:03:45:45 +0000] "GET / HTTP/1.1" 200 6812
# 아파치 웹서버 접근로그를 처리하여 웹서버가 서비스한 컨텐츠의 총 용량을 계산한다.
# 웹서버 접근로그에 기록된 용량의 단위는 byte 이다.

total_service = 0
with open('data1/access_log', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        servicebyte = log[9]
        if servicebyte.isdigit():
            total_service += int(servicebyte)
total_service /= 1024       # KB 단위로 변환
print('총 서비스 용량: %dKB' %total_service)
# 총 서비스 용량: 29289KB

# 4. 사용자별 서비스 용량 구하기
# Apache Web Server log 파읷을 이용해서 사용자별 서비스한 데이터 용량을 구해보자?
# 180.76.15.5 - - [15/Nov/2015:03:45:45 +0000] "GET / HTTP/1.1" 200 6812
# 사용자별(사용자IP) 웹서버가 제공한 서비스 용량을 계산하고, 제공한 서비스 용량
# 기준으로 내림차순 정렬하여 ‘사용자IP – 서비스 용량’ 형식으로 출력

services = {}                        # 빈 딕셔너리 = { '사용자 IP' : '서비스 용량 ' }
with open('data1/access_log', 'r') as f:
    logs = f.readlines()            # 리스트로 리턴
    for log in logs:
        log = log.split()           # 공백으로 파싱
        ip = log[0]                 # ip주소
        servicebyte = log[9]        # 컨텐츠 용량(byte)
        if servicebyte.isdigit():   # 숫자 형태이면 True 리턴
            servicebyte = int(servicebyte)
        else:
            servicebyte = 0
        if ip not in services:          # services에 IP가 존재하지 않으면
            services[ip] = servicebyte  # { '사용자IP' : '서비스용량' }
        else:                           # services에 IP가 존재하면
            services[ip] += servicebyte # 사용자IP 별로 서비스용량을 누적
# 딕셔너리 출력
print(services)
# 서비스 용량을 기준으로 내림차순 정렬
result = sorted(services.items(), key=lambda x : x[1], reverse=True)
print('사용자IP - 서비스 용량')
for ip, b in result:
    print('[%s] - [%d]' %(ip,b))

# 기상청의 날씨 정보 구하기 : xml 파일 읽기
from bs4 import BeautifulSoup
import urllib.request as req
import os.path

url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnid=108'
savename = 'forecast.xml'
# url 저장
if not os.path.exists(savename):    # 현재 디렉토리에 forecast.xml이 없으면
    req.urlretrieve(url, savename)  # forecast.xml 파일 다운로드
# BeautifulSoup로 분석하기
xml = open(savename, 'r', encoding='utf8').read()
soup = BeautifulSoup(xml, 'html.parser')
# print(soup)
# 전국 날씨정보를 info딕셔너리에 저장
info = {}                   # info = { name : weather }
for location in soup.find_all('location'):
    name = location.find('city').string       # 도시명
    wf = location.find('wf').string         # 날씨
    tmx = location.find('tmx').string       # 최고기온
    tmn = location.find('tmn').string       # 최저기온

    weather = wf + ':' + tmn + '~' + tmx
    if name not in info:
        info[name] = []
    info[name].append(weather)
print(info)

# 각 지역의 날씨를 구분해서 출력
for name in info.keys():
    print('+', name)
    for weather in info[name]:
        print('|', weather)

# JSON (JavaScript Object Notation)
#  JSON은 JavaScript Object Notation 의 약어로 XML 데이터를 대신
# 하여 데이터 교환용으로 많이 사용되는 문서포맷이다.
#  JSON은 키와 값을 쌍으로 가지는 구조이다.
#  배열을 사용할 때는 대괄호([ ])안에 중괄호({ })를 사용하여 조합한다.

# 예)
# JSON (JavaScript Object Notation)
# [
# {
# "id": "1",
# "name": "레몬",
# "price": " 3000",
# "description": "레몬에 포함되어 있는 쿠엔산은 피로회복에 좋다. 비타민C도 풍부하다."
# },
# {
# "id": "2",
# "name": "키위",
# "price": " 2000",
# "description": "비타민C가 매우 풍부하다. 다이에트와 미용에도 매우 좋다."
# },
# {
# "id": "3",
# "name": "블루베리",
# "price": " 5000",
# "description": "블루베리에 포함된 anthocyanin(안토시아닌)은 눈피로에 효과가 있다."

# json 파일 읽기
import json

items = json.load(open('data/item.json', 'r', encoding='utf8'))
print(type(items))      # 'list'
print(items)            # [{'id': '1', 'name': '레몬', 'price': ' 3000’, ....
for item in items:
    print(item['id'] + '-' + item['name'] + '-' +
          item['price'] + '-' + item['description'])
# 1-레몬- 3000-레몬에 포함되어 있는 쿠엔산은 피로회복에 좋다. 비타민C도 풍부하다.
# 2-키위- 2000-비타민C가 매우 풍부하다. 다이에트와 미용에도 매우 좋다.
# 3-블루베리- 5000-블루베리에 포함된 anthocyanin(안토시아닌)은 눈피로에 효과가 있다.
# 4-체리- 5000-체리는 맛이 단 성분이 많고 피로회복에 잘 듣는다.
# 5-메론- 5000-메론에는 비타민A와 칼륨이 많이 포함되어 있다.
# 6-수박-15000-수분이 풍부한 과일이다.

# 깃허브에서 파일 읽기
import urllib.request as req
import os.path, random
import json

# JSON 데이터 내려받기
url = 'https://api.github.com/repositories'
savename = 'repo.json'
if not os.path.exists(url):
    req.urlretrieve(url, savename)
# JSON 파일 분석하기
items = json.load(open(savename, 'r', encoding='utf8'))
print(items)
# 출력하기
for item in items:
    print(item['name'] + '-' + item['owner']['login'])

