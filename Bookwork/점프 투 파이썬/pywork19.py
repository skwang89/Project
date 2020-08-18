# pywork19.py start
# <<강의 복습 12. 시작>>


# 크롤링(Crawling)
# 크롤링(Crawling)이란 프로그램이 웹 사이트를 정기적으로 돌며 정보를 추출 하는 기술.
# 크롤링하는 프로그램을 “크롤러(Crawler)” 또는 “스파이더(Spider)” 라고 한다.
# 예를 들어, 검색엔짂을 구현할 때 사용하는 크롤러는 웹 사이트의 링크를 타고
# 웹 사이트를 돌아 다닌다. 그리고 웹 사이트의 데이터를 모아서 데이터베이스에 저장한다.

# 스크레이핑(Scraping)
# 스크레이핑(Scraping)이란 웹 사이트에 있는 특정 정보를 추출하는 기술을 의미 한다.
# 스크레이핑을 이용하면 웹 사이트에 있는 정보를 쉽게 수집할 수 있다.
# 웹에 공개된 정보는 대부붂 HTML 형식. 이를 가져와서 데이터베이스에
# 저장 하려면 데이터 가공이 필요하다.
# 광고 등의 불필요한 정보를 제거하고, 필요한 정보만 가져오려면 사이트 구조를
# 분석해야 한다. 따라서 스크레이핑이라는 기술은 웹에서 데이터를 추출하는 것
# 뿐만 아니라 그러한 구조를 분석하는 것도 포함됨.
# 또한 최근에는 로그인을 해야만 유용한 정보에 접근할 수 있는 사이트도 많다.
# 이 경우 단순히 URL을 알고 있는 것만으로는 유용한 정보에 접근할 수 없다.
# 따라서 제대로 스크레이핑을 하려면 로그인 해서 필요한 웹 페이지에 접근하는
# 기술도 알아야 한다.

# 웹상의 정보를 추출하는 방법
# 1. 파이썬은 웹 사이트에 있는 데이터를 추출하기 위해 "urllib" 라이브러리를
# 사용합니다. 이 라이브러리를 이용하면 HTTP 또는 FTP를 사용해 데이터를
# 다운로드 할 수 있습니다.
# 2. urllib 라이브러리는 URL을 다루는 모듈을 모아 놓은 패키지 입니다.
# 3. 그 중에서도 urllib.request 모듈은 웹 사이트에 있는 데이터에 접근하는 기능을
# 제공합니다. 또한 읶증, 리다이렉트, 쿠키(Cookie) 처럼 인터넷을 이용한 다양한
# 요청과 처리를 지원합니다.
# 4. BeautifulSoup 라이브러리를 이용하면 갂단하게 HTML과 XML에서 정보를
# 추출할 수 있습니다.

# urllib.request를 이용한 다운로드 : urlretrieve( ) 함수
# 파일을 다운로드할 때는 urllib.request 모듈에 있는 urlretrieve( ) 함수를
# 사용한다. 이 함수를 사용하면 직접 파읷을 다운로드 할 수 있다.
import urllib.request as req
# url = "https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png"
url = "https://www.daum.net/"
#다운로드
# req.urlretrieve(url, 'daum.png')
req.urlretrieve(url, 'daum.html')
print('저장 성공')

# urllib.request를 이용한 다운로드 : urlopen( ) 함수
# 이번에는 파일을 다운로드할 때는 urllib.request 모듈에 있는 urlopen( ) 함수를 이용해
# 메모리 상에 데이터를 올리고, 그 이후에 파일에 저장해 본다.
import urllib.request as req
url = "https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png"
# 다운로드
mem = req.urlopen(url).read()
# 파일로 저장: w: 쓰기 모드, b: 바이너리 모드
with open('daumlog.png', mode='wb') as f:
    f.write(mem)
    print('저장 성공')

# 기상청의 RSS 서비스
# 기상청의 RSS서비스는 아래 URL에 지역번호를 지정하면 해당 지역의 기상
# 정보를 제공해 준다.
# http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp
# http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=지역번호

# 지역        지역번호  지역          지역번호
# 전국        108      전라북도       146
# 서울/경기도  109      전라남도       156
# 강원도      105      경상북도       143
# 충청북도    131      경상남도        159
# 충청남도    133      제주특별자치도  184

# 기상청의 RSS 서비스
import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
# 매개변수를 URL 인코딩
values = {'stnId': '108'}        # 전국
params = urllib.parse.urlencode(values)
# 요청 전용 URL을 생성
url = API + "?" + params
url = API + "?stnId=108"
print("url=", url)
# xml파일을 읽어와서 출력함
data = urllib.request.urlopen(API).read()
text = data.decode("utf-8")
print(text)
# forecast.xml 파읷로 저장하기 ( w: 쓰기모드 )
with open("forecast.xml", mode="w", encoding="utf-8") as f:
f.write(text)
print("저장되었습니다...!")

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

# BeautifulSoup 모듈로 스크레이핑하기
# 1. 스크레이핑이란 웹 사이트에서 데이터를 추출하고, 원하는 정보를 추출하는 것입니다.
# 최근에는 읶테넷에 데이터가 너무 맋으므로 스크레이핑을 잘 홗용하는 것이 중요합니다.
# 2. 파이썬으로 스크레이핑할 때 빼놓을 수 없는 라이브러리가 바로 “ BeautifulSoup “ 입니다.
# 이 라이브러리를 이용하면 갂단하게 HTML과 XML에서 정보를 추출할 수 있습니다.
# 3. 최근 스크레이핑 라이브러리는 다운로드부터 HTML 붂석까지 모두 해주는 경우가 맋은데,
# BeautifulSoup 라이브러리는 어디까지나 HTML과 XML을 붂석해주는 라이브러리 입니다.
# BeautifulSoup 자체에는 다운로드 기능이 없습니다.

# BeautifulSoup 모듈 설치 확인
# C:\> pip list
# BeautifulSoup 모듈 설치
# C:\> pip install beautifulsoup4

# BeautifulSoup 모듈 사용법
# find('태그명') : 특정 태그 1개만 추출하는 역할
# find(‘태그명').string : 특정 태그 안에 있는 텍스트를 추출하는 역할
# find(‘태그명').text : 특정 태그 안에 있는 텍스트를 추출하는 역할
# find(‘태그명').get_text() : 특정 태그 안에 있는 텍스트를 추출하는 역할
# find('태그명' , {'class' : 'class명'} ) : class 값을 이용해서 추출
# find('태그명' , {'id' : 'id명'} ) : id명을 이용해서 특정 태그를 구함
# find( id = 'id명' ) : id명을 이용해서 특정 태그를 구함
# findAll('태그명') : 지정된 모든 태그를 리스트 형태로 추출하는 역할
# find_all('태그명') : 지정된 모든 태그를 리스트 형태로 추출하는 역할

from bs4 import BeautifulSoup

html_str = '<html><div>hello</div></html>'
soup = BeautifulSoup(html_str, 'html.parser')
print(soup)                         # <html><div>hello</div></html>
print(soup.find('div'))             # <div>hello</div>
print(soup.find('div').text)        # hello
print(soup.find('div').string)      # hello
print(soup.find('div').get_text())  # hello

html_str = '''
    <html>
        <body>
            <ul>
                <li>hello</li>
                <li>bye</li>
                <li>welcome</li>
            </ul>
        </body>
    </html>
'''
bs = BeautifulSoup(html_str, 'html.parser')
ul = bs.find('ul')
print(ul)
# <ul>
#   <li>hello</li>
#   <li>bye</li>
#   <li>welcome</li>
# </ul>
li = ul.find('li')          # 가장 먼저 나오는 li 태그 검색
print(li)                   # <li>hello</li>
print(li.text)              # hello

# findAll() : 지정된 모드 태그를 리스트 형태로 추출하는 역할
# find_all() : 지정된 모드 태그를 리스트 형태로 추출하는 역할
from bs4 import BeautifulSoup

html_str ='''
    <html>
        <body>
            <ul>
                <li>hello</li>
                <li>bye</li>
                <li>welcome</li>
            </ul>
        </body>
    </html>
'''

bs = BeautifulSoup(html_str, 'html.parser')
ul = bs.find('ul')
print(ul)
# <ul>
#   <li>hello</li>
#   <li>bye</li>
#   <li>welcome</li>
# </ul>
list = ul.findAll('li')     # 리스트로 리턴
print(list)                 # [<li>hello</li>, <li>bye</li>, <li>welcome</li>]
for l in list:
    # print(l)
    # print(l.text)
    print(l.string)

# class 속성으로 데이터 접근하기
# find('태그명 , {'class' : class명} ) : class 값을 이용해서 추출
from bs4 import BeautifulSoup

html_str = '''
    <html>  
        <body>
            <ul class = 'greet'>
                <li>hello</li>
                <li>bye</li>
                <li>welcome</li>
            </ul>
            <ul class = 'reply'>
                <li>ok</li>
                <li>no</li>
                <li>sure</li>
            </ul>
        </body>
    </html>
'''
bs = BeautifulSoup(html_str, 'html.parser')
ul = bs.find('ul', {'class' : 'reply' })    # class 속성값이 reply 태그 추출
print(ul)
# <ul class="reply">
# <li>ok</li>
# <li>no</li>
# <li>sure</li>
# </ul>
list = ul.find_all('li')
print(list)
for l in list:
    print(l.text)

# 속성을 이용해서 속성값 추출
from bs4 import  BeautifulSoup

html_str = '''
    <html>
        <body>
            <ul class='ko'>
                <li><a href='https://www.naver.com'>네이버</a></li>
                <li><a href='https://www.daum.net'>다음</a></li>
            </ul>
            <ul class='sns'>
                <li><a href='https://www.google.com'>구글</a></li>
                <li><a href='https://www.facebook.com'>페이스북</a></li>
            </ul>
        </body>
    </html>
'''
# bs = BeautifulSoup(html_str, 'html.parser')     # html.parser 설치 안해도됨
bs = BeautifulSoup(html_str, 'lxml')              # lxml 모듈 추가 설치
atag = bs.find('a')             # 첫번째 anchor 태그를 구해옴
print(atag)                     # <a href="https://www.naver.com">네이버</a>
print(atag['href'])             # href 속성으로 속성값을 추출
# https://www.naver.com

# id 속성으로 태그 추출
from bs4 import  BeautifulSoup

html = '''
    <html>
        <body>
            <h1 id='title'>스크레이핑이란?</h1>
            <p id='p1'>웹페이지 분석</p>
            <p id='p2'>원하는 부분을 추출하는 것</p>
        </body>
    </html>
'''
soup = BeautifulSoup(html, 'html.parser')
title = soup.find(id='title')
print(title)                        # <h1 id="title">스크레이핑이란?</h1>
print(title.text)                   # 스크레이핑이란?
p1 = soup.find(id='p1')
print(p1)                           # <p id="p1">웹페이지 분석</p>
print(p1.string)                    # 웹페이지 분석
p2 = soup.find(id='p2')
print(p2)                           # <p id="p2">원하는 부분을 추출하는 것</p>
print(p2.get_text())                # 원하는 부분을 추출하는 것

# id 속성으로 태그 추출
from bs4 import BeautifulSoup

html = '''
    <html>
        <head>
            <title>작품과 작가 모음</title>
        </head>
        <body>
            <h1>책정보</h1>
            <p id='book_title'>토지</p>
            <p id='author'>박경리</p>

            <p id='book_title'>태백산맥</p>
            <p id='author'>조정래</p>

            <p id='book_title'>감옥으로 부터의 사색</p>
            <p id='author'>신영복</p>        
        </body>
    </html>
'''
soup = BeautifulSoup(html, 'html.parser')
# id값이 book_title인 태그 추출
title = soup.find('p', {'id':'book_title'}).text
title = soup.find(id = 'book_title').text
print(title)                    # 토지
# id값이 author인 태그 추출
author = soup.find('p', {'id':'author'}).text
author = soup.find(id = 'author').text
print(author)                   # 박경리
# id값이 book_title인 모든 태그 추출
title2 = soup.find_all(id='book_title')
print(title2)                   # 리스트로 리턴
                                # [<p id="book_title">토지</p>, <p id="book_title">태백산맥</p>, <p id="book_title">감옥으로 부터의 사색</p>]
for t in title2:
    print(t.text)
# 토지
# 태백산맥
# 감옥으로 부터의 사색

# BeautifulSoup 기본 사용법 : id로 요소를 찾는 방법
# id 값이 book_title 인 첫번째 p태그를 구해옴
title = soup.find('p', {"id":"book_title"}).text
print('title:', title) # title: 토지
# id값이 author 인 첫번째 p태그를 구해옴
author = soup.find('p', {"id":"author"}).text
print('author:', author) # author: 박경리
# id 값이 book_title 인 모든 p태그를 구해와서 리스트로 리턴
title2 = soup.find_all('p', {"id":"book_title"})
print('title2:', title2)
for t2 in title2:
    print(t2.text)
# id값이 author 인 모든 p태그를 구해와서 리스트로 리턴
author2 = soup.find_all('p', {"id":"author"})

print('author2:', author2)
for a2 in author2:
    print(a2.text)

# CSS 선택자 사용하기
# BeautifulSoup는 자바스크립트 라이브러리읶 jQuery처럼 CSS선택자를 지정해서 원하는
# 요소를 추출하는 기능도 제공합니다.
# 메소드 설명
# soup.select_one(선택자) CSS 선택자로 요소 하나를 추출
# soup.select(선택자) CSS 선택자로 요소 여러 개를 리스트로 추출

# css 선택자를 이용해서 데이터 추출
from bs4 import BeautifulSoup

html = '''
    <html>
        <body>
        <div id='meigen'>
            <h1>중앙 도서</h1>
            <ul class = 'items'>
                <li>유니티 게임 이펙트 입문</li>
                <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인 정석</li>
            </ul>
        </div>
        </body>
    </html>
'''
# HTML 분석하기
soup = BeautifulSoup(html, 'html.parser')
# 필요한 부분을 CSS 쿼리로 추출하기
# 타이틀 부분 추출하기
h1 = soup.select_one("div#meigen > h1").string
print("h1 =", h1)
# 목록 부분 추출하기
li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
    print("li =", li.string)

# 네이버 금융에서 시장지표 추출하기
from bs4 import BeautifulSoup
import urllib.request as req
from sympy import primenu

url = 'http://finance.naver.com/marketindex/'
result = req.urlopen(url)

soup = BeautifulSoup(result, 'html.parser')
print(soup)

# 원-달러 환율 정보 추출
price = soup.select_one('div.head_info > span.value').text
price = soup.select_one('a.head.usd span.value').text
print('원-달러:', price)
# 원-달러: 1,184.60
# 엔-달러 환율 정보 추출
yen = soup.select_one('a.head.jpy_usd span.value').text
print('엔-달러:', yen)
# 엔-달러: 106.0600
# wti 정보 추출
wti = soup.select_one('a.head.wti span.value').text
print('wti:', wti)
# wti: 42.89
# 국제금 정보 추출
int_gold = soup.select_one('a.head.gold_inter span.value').text
print('국제금:', int_gold)
국제금: 1985.0
# 국내금 정보 추출
dom_gold = soup.select_one('a.head.gold_domestic span.value').text
print('국내금:', dom_gold)

# 기상청의 날씨 정보 구해오기
# 기상청의 날씨 정보(기온, 습도) 구해오는 예제
import requests
from bs4 import BeautifulSoup

# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듬
response = requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp')
# print(response)
# HTML 분석하기
soup = BeautifulSoup(response.content, 'html.parser')
# <table class="table_develop3">을 찾음
table = soup.find("table", {'class':'table_develop3'})
print(table)
# 리스트 생성
data = []               # 비어있는 리스트: 지역, 기온, 습도
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
# print(tds)
    for td in tds:
        if td.find('a'):
            point = td.find('a').text           # 지역명
            temp = tds[5].text                  # 기온
            humidity = tds[9].text              # 습도
            data.append([point, temp, humidity])
print(data)

print('[지역, 기온, 습도]')
for w in data:
    print(w)

# 로그인이 필요한 사이트에서 정보 구하기

# requests 모듈
# request 모듈은 로그인이 필요한 사이트에서 쿠키와 세션 정보를 구해오기
# 위해서 사용되는 모듈입니다.
# requests 모듈 설치 확읶
c:\> pip list
# requests 모듈 설치
c:\> pip install requests
# 네이버나 다음 같은 검색 포털 사이트들은 검색 프로그램(로봇)이 쉽게
# 로그인할 수 없게 보안적으로 막혀 있습니다.
# 한빛 출판네트워크
# - 로그인 페이지 : http://www.hanbit.co.kr/member/login.html
# - 마이페이지 : http://www.hanbit.co.kr/myhanbit/myhanbit.html

# requests 모듈을 이용해서 현재 시갂에 대한 테이터를 추출하고, 추출한 데이터를
# 텍스트 형식과 바이너리 형식으로 출력하는 예제
import requests

r = requests.get('http://api.aoikujira.com/time/get.php')
print(r)                    # <Response [200]>
text = r.text
print(text)                 # 2020/07/07 15:51:46
print(type(text))
bin = r.content
print(bin)                  # b'2020/07/07 15:51:46'
print(type(bin))

# requests 모듈을 이용해서 바이너리 데이터의 이미지를 다운로드 받아서 저장하는 예제
import requests

r = requests.get('https://t1.daumcdn.net/daumtop_chanel/op/20170315064553027.png')
text = r.text
print(text)
print(type(text))
# 이미지 저장
with open('daum.png', 'wb') as f:
    f.write(r.content)
print('저장 성공')

# 파이썬으로 로그인하기
import requests
from bs4 import BeautifulSoup
# 아이디와 비밀번호 지정하기[자신의 것을 사용]
USER = "id"
PASS = "password"

# 세션 시작하기
session = requests.session()
# 파이썬 프로그램으로 로그읶하기
login_info = {
"m_id": USER, # 아이디 지정
"m_passwd": PASS # 비밀번호 지정
}
url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info) # URL에 post 요청을 수행
# 로그인이 완료되면 마이페이지에 접근
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
# BeautifulSoup 인스턴스 생성하기 - 텍스트 형식으로 데이터 추출
soup = BeautifulSoup(res.text, "html.parser")
# 마일리지와 이코인 가져오기
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("마일리지: " + mileage)
print("이코인: " + ecoin)

# 웹 브라우저 원격조작에 사용하는 selenium
# 자바스크립트를 맋이 사용하는 웹 사이트의 경우에는 앞에서 소개한 requests
# 모듈로 필요한 데이터를 스크레이핑 하기 힘들다. 이런 경우에 웹 브라우저를
# 원격 조작할때 사용하는 도구로 selenium 이 있습니다.
# 일반적으로 selenium 은 웹 애플리케이션 테스트를 자동화할 때 사용하지만,
# 스크레이핑을 할 때도 유용하게 사용할 수 있습니다. selenium 을 이용하면
# 자동으로 URL을 열고 클릭할 수 있으며, 스크롤하거나, 문자를 입력하는 등의
# 다양한 조작을 자동화 할 수 있습니다.
# 또한 화면을 캡쳐해서 이미지로 저장하거나 HTML의 특정 부분을 추출하는 것도
# 가능하고, 구글 크롬, 파이어폭스, 인터넷익스플로러, 오페라 등의 다양한
# 웹브라우저를 원격으로 조작할 수 있습니다.

# selenium + chrome 환경구축
# 1. selenium 설치
# c:\> pip install selenium
# 2. 브라우저 Driver 설치
# selenium을 사용하기 위해서는 브라우저 별로 driver를 다운로드 해야 한다.
# selenium의 기능중에서는 컴퓨터가 직접 웹 브라우저를 띄운 후 코드를
# 쳐서 동작시킬 수 있도록 webdriver라는 api를 제공한다.
# 컴퓨터가 webdriver api로 브라우저를 직접 제어할 수 있도록 도와주는
# driver를 설치해주어야 한다. 크롬, 엣지, 파이어폭스, 사파리에서 driver를 제공한다.
# 자싞의 운영체제에 맞는 버젂으로 드라이버 파일을 다운로드 받도록 하자.
# 다운로드 받은 파일을 압축 해제 후 아래 위치에 저장한다.
# selenium 다운로드
# 1.chrome
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# 2.firefox
# https://github.com/mozilla/geckodriver/releases
# 3.edge
# https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# 4.Safari
# https://webkit.org/blog/6900/webdriver-support-in-safari-10/















































all = [var for var in globals() if var[0] != "-"]
for var in all:
    del globals()[var]
del(all)
del(var)

import sys
sys.modules[__name__].__dict__.clear()


# <<강의 복습 12. 끝>>
# pywork19.py end