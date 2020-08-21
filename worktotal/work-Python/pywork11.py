# pywork11.py start
# <<강의 복습 4. 시작>>


# 파이썬의 함수
# 1. 파이썬에서 함수는 def 키워드로 정의한다.
# 2. 함수는 윗쪽에서 정의를 하고, 아랫쪽에 호출해야 한다.
#    만약, 순서가 바뀌면 오류가 발생한다.

# 사용자 정의 함수
def hello():
    print('함수 호출 성공1')
# 함수 호출
hello()

# 매개변수가 있는 함수 정의
# : 절대값을 구하는 함수
# 사용자 정의 함수
def abs(n):         # n : 매개변수(parameter)
    if n < 0:
        n = -n
    return  n       # return문: 함수를 호출한 곳에 값을 돌려주는 역할

# 함수 호출
abs(-30)
print('돌려 받은 값1:', abs(-30))
result = abs(-50)
print('돌려 받은값2:', result)

# 윤년과 평년 구분하기
# 1년 365.242374
# 평년 = 365일 (2월달 - 28일까지)
# 윤년 = 366일 (2월달 - 29일까지)

# 윤년의 정의
# 1. 해당 연도를 4로 나누어 떨어지면 윤년
# 2. 그 중에서 100으로 나누어 떨어지면 윤년이 아님
# 3. 그 중에서 400으로 나누어 떨어지면 윤년

# 윤년은 4의 배수이고 100배수는 아니거나 400의 배수이면 윤년
def yun(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print(year, "은(는) 윤년")
    else:
        print(year, "은(는) 평년")
year = int(input('연도를 입력'))
yun(year)

# 매개변수가 2개인 함수
# 최대값과 최소값을 구해주는 함수 만들기
# 최대값을 구해주는 함수
def max(n1, n2):
    if n1>n2:
        return n1
    else:
        return n2
# 최소값을 구해주는 함수
def min(n1, n2):
    if n1<n2:
        return  n1
    else:
        return n2
n1 = int(input('정수1을 입력하세요?'))
n2 = int(input('정수2를 입력하세요?'))
max = max(n1, n2)       # 함수 호출
min = min(n1, n2)       # 함수 호출
print('max:', max)
print('min:', min)

# 매개변수가 3개인 함수
# 키보드로 3개의 정수를 입력 받아서, 최대값과 최소값을 구하는 프로그램을 작성
# 최대값을 구해주는 함수
def max(n1, n2, n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3
# 최소값을 구해주는 함수
def min(n1, n2, n3):
    if n1<=n2 and n1<=n3:
        return n1
    elif n2<=n1 and n2<=n3:
        return n2
    else:
        return n3
n1 = int(input("정수1을 입력하세요?"))
n2 = int(input("정수2을 입력하세요?"))
n3 = int(input("정수3을 입력하세요?"))
max = max(n1, n2, n3)       # 함수 호출
min = min(n1, n2, n3)       # 함수 호출
print('max:', max)
print('min:', min)

# 1 ~ n까지 합을 구하는 프로그램 작성
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print('1 ~ ', n, '=', sum)
# 함수 호출
sum(5)                          # 1~ 5 = 15
sum(10)                         # 1~ 10 = 55
sum(30)                         # 1~ 30 = 465
sum(40)                         # 1~ 40 = 820
sum(100)                        # 1~ 100 = 5050

# 입력받은 매개변수에 따라 문자열을 반복 출력하는 함수
def str(text, cnt):
    for i in range(cnt):
        print(text, i+1)
# 함수 호출
str('안녕하세요', 3)
str('파이썬', 5)
str('자바', 3)
str('스프링')              # 오류 발생

# 기본값 매개변수(Default Argument Variable)
# 기본값 매개변수 cnt = 1로 정의
def str(text, cnt = 1):
    for i in range(cnt):
        print(text)
# 함수 호출
# 함수를 호출할때 2번째 매개변수를 생략하면, 기본값 매개변수 cnt=1이 사용됨
str('안녕하세요?')
str('안녕히 가세요.', 3)

# 가변 매개변수(Arbitary Argument Variable)
# 1. 매개변수 앞에 * 를 붙이면 가변 매개 변수가 된다.
# 2. 가변 매개변수는 입력 갯수가 달라져도 모두 받을 수 있다.
# 3. * 가 붙은 가변 매개변수는 입력받은 값들을 튜플(tuple)로 처리한다.
def merge_string(*text):
    print(type(text))               # tuple
    print(text)
    result=''
    for s in text:
        result = result + s
    return result
print(merge_string('나는'))
print(merge_string('나는', '학교에'))
print(merge_string('나는', '학교에', '간다'))
print(merge_string('아버지가', '방에', '들어 가신다'))

# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자
# 입력 개수에 상관없이 사용하기 위해 가변 매개변수 *n를 사용
def avg(*n):
    # sum = 0
    # for i in n:
    #     sum += i
    return sum(n) / len(n)
print(avg(1, 2))
print(avg(1, 2, 3))
print(avg(1, 2, 3, 4))
print(avg(1, 2, 3, 4, 5))

# 가변 매개변수(Arbitary Argument Variable)
# 1. 매개변수 앞에 ** 를 붙이면 가변 매개 변수가 된다.
# 2. 가변 매개변수는 입력 갯수가 달라져도 모두 받을 수 있다.
# 3. ** 가 붙은 가변 매개변수는 입력받은 값들을 딕셔너리(dict)로 처리한다.
# 가변 매개변수를 가진 함수 정의
def print_team(**players):
    print(type(players))               # 'dict'
    for k in players.keys():
        print('{0} = {1}'.format(k, players[k]))
# 함수 호출
print_team(카시야스='GK', 호날두='FW', 알론소='MF', 페페='DF')

# 일반 매개변수와 가변 매개변수가 같이 사용되는 함수
# : 일반 매개변수와 가변 매개변수를 같이 사용할 경우에는 일반 매개변수를 먼저 사용하고,
#   가변 매개변수는 가장 마지막에 사용해야 한다.
def print_args(n, *args):
    for i in range(n):
        print(args[i])
# 함수 호출
print_args(1, '파이썬')
print_args(2, '파이썬','자바')
print_args(3, '파이썬','자바','오라클')

# 일반 매개변수와 가변 매개변수가 같이 사용되는 함수
# 1. 일반 매개변수와 가변 매개변수를 같이 사용할 경우에는 일반 매개변수를
#    먼저 사용하고, 가변 매개변수를 가장 마지막에 사용해야 한다.
# 2. 일반 매개변수가 마지막에 오는 경우에는 키워드 매개변수로 호출해야 한다.
def print_args(*args, n):
    for i in range(n):
        print(args[i])
# 함수 호출
# print_args('파이썬', 1)                  # 오류 발생
print_args('파이썬', n=1)
print_args('파이썬','자바', n=2)
print_args('파이썬','자바','오라클', n=3)

# 지역변수와 전역변수
# 1. 함수 안에서 정의된 변수는 함수 안에서만 사용 가능한 지역 변수가 된다.
# 2. 함수 안에서 정의된 변수도 global 키워드를 붙이면 전역 변수가 된다.
# 3. 지역변수
#   1) 조건문, 반복문 안에서 정의된 변수
#   2) 함수 안에서 정의된 변수
#   3) 함수의 매개변수
a = 1                       # 전역 변수
def vartest(a):             # a:매개변수, 지역변수
    a = a + 1
    print(a)                # 2

# 함수 호출
vartest(a)
print(a)                    # 1
#---------------------------------------------------------------------
def scope():
    global b                # 전역변수
    b = 1
    print('b1=', b)         # b1= 1
b = 10
scope()                     # 함수 호출
print('b2=', b)             # b2= 1

# 함수를 변수에 담아서 사용하기

# 예1. 함수명을 변수에 담아서 사용하기
def something(a):
    print(a)

p = something           # 함수 이름을 변수 p에 저장
p(123)                  # 변수 p를 이용해서 something() 함수를 호출
p('abc')                # 변수 p를 이용해서 something() 함수를 호출

# 예2. 함수명을 리스트에 담아서 사용하기
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

first = [plus, minus]   # plus()함수와 minus()함수를 리스트에 저장함
print(first[0](1,2))    # first[0]은 plus()함수를 의미함
print(first[1](1,2))    # first[1]은 minus()함수를 의미함

# 예3. 함수명을 매개변수로 전달해서 사용하기
def hello_korean():
    print('안녕하세요')
def hello_english():
    print('Hello')
def greet(hello):       # 함수명을 매개변수로 전달
    hello()

greet(hello_korean)   # greet() 함수 호출
greet(hello_english)  # greet() 함수 호출

# 함수를 변수에 담아서 사용하기
# 예1. 함수명을 변수에 담아서 사용하기
def something(a):
    print(a)
p = something           # 함수 이름을 변수 p에 저장
p(123)                  # 변수 p를 이용해서 something() 함수를 호출
p('abc')                # 변수 p를 이용해서 something() 함수를 호출

# 예2. 함수명을 리스트에 담아서 사용하기
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
first = [plus, minus]   # plus()함수와 minus()함수를 리스트에 저장함
print(first[0](1,2))    # first[0]은 plus()함수를 의미함
print(first[1](1,2))    # first[1]은 minus()함수를 의미함

# 예3. 함수명을 매개변수로 전달해서 사용하기
def hello_korean():
    print('안녕하세요')
def hello_english():
    print('Hello')
def greet(hello):       # 함수명을 매개변수로 전달
    hello()
greet(hello_korean)   # greet() 함수 호출
greet(hello_english)  # greet() 함수 호출

# 중첩함수(Nested Function)
# : 함수 안에 정의된 함수
import math
def stddev(*n):                             # 표준 편차
    def mean():                             # 평균 : 중첩함수
        return sum(n) / len(n)
    def variance(m):                        # 분산 : 중첩함수
        total = 0
        for i in n:
            total += (i-m)**2
        return total/(len(n)-1)
    v = variance(mean())
    print('분산(v):', v)
    return math.sqrt(v)                 # SQRT(x): 숫자 x의 제곱근을 반환
                                        # 분산값을 표준편차로 변환
print('표준편차:', stddev(2.3, 1.7, 1.4, 0.7, 1.9))

# pass : 함수나 클래스의 구현을 잠시 미룰 경우에 사용함.
# 함수의 구현을 미루는 경우
def test():
    pass
# 클래스 구현을 미루는 경우
class myclass:
    pass

# 재귀함수(Recursive Function)
# : 함수 안에서 자기자신의 함수를 호출하는 함수를 재귀함수라고 한다.
def call():                 # 재귀함수
    print('무한출력')
    call()                  # 자기자신의 call() 함수 호출
# 외부에서 call() 함수
call()

# 재귀함수를 이용해서 팩토리얼을 구해보자?
#   ex)  5! = 5 x 4 x 3 x 2 x 1
# 팩토리얼을 구하는 재귀함수
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print('0!=', fact(0))
print('1!=', fact(1))
print('3!=', fact(3))
print('5!=', fact(5))
print('10!=', fact(10))
print('100!=', fact(100))
print('997!=', fact(997))

# lambda : 이름이 없는 한줄짜리 함수
#          일반적인 함수를 사용하기 힘든 경우에 사용함.
# 형식 : lambda  인자1, 인자2,....   :  실행코드(리턴값)
# 예1.
add = lambda x, y : x+y             # 람다(함수)를 add변수에 저장함
result = add(1, 3)
print('result:', result)
# 예2.
funcs = [ lambda x : x+'.pptx', lambda x : x+'.docx']
result1 = funcs[0]('Intro')
result2 = funcs[1]('Report')
print('result1:', result1)          # result1: Intro.pptx
print('result2:', result2)          # result2: Report.docx
# 예3.
# { '아기이름' : 출생아수 }
names = {'Mary':10999, 'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}
print(sorted(names.items()))        # 아기이름을 기준으로 오름차순 정렬
# [('Aimy', 9778), ('Bob', 5887), ('Kelly', 7855), ('Mary', 10999), ('Michale', 27115), ('Sams', 2111), ('Tom', 20245)]
# 1. 아기이름(key)을 기준으로 오름차순 정렬
print(sorted(names.items(), key=lambda x : x[0]))
# [('Aimy', 9778), ('Bob', 5887), ('Kelly', 7855), ('Mary', 10999),
# 2. 아기이름(key)을 기준으로 내림차순 정렬
print(sorted(names.items(), key=lambda x : x[0], reverse=True))
# [('Tom', 20245), ('Sams', 2111), ('Michale', 27115), ('Mary', 10999),
# 3. 출생아수(value)을 기준으로 오름차순 정렬
print(sorted(names.items(), key=lambda x : x[1]))
# [('Sams', 2111), ('Bob', 5887), ('Kelly', 7855), ('Aimy', 9778),
# 4. 출생아수(value)을 기준으로 내림차순 정렬
print(sorted(names.items(), key=lambda x : x[1], reverse=True))
# [('Michale', 27115), ('Tom', 20245), ('Mary', 10999), ('Aimy', 9778),

# map() 내장함수
# : 인자를 바꾸어가며 함수를 반복 호출하여 결과를 return 받는 함수
def f(x):
    return x*x
li = [1,2,3,4,5]
# 방법1.
print('반복문을 이용한 실행')
for i in li:
    print(f(i), end='\t')
print()
# 방법2.
print('map() 함수를 이용한 실행')
result = list(map(f, li))
print('result:', result)
# 방법3.
print('map() 함수와 lambda를 이용한 실행')
result2 = list(map(lambda x : x*x, li))
print('result2:', result2)

# filter() 내장 함수
# : 컬렉션과 lambda함수를 매개변수로 받아서 컬렉션의 모든 데이터를
#   lambda 함수의 매개변수로 대입해서 결과가 참인 경우에만 리턴하는 함수
li = [1,2,3,4,5]
print('lambda와 filter()함수를 이용한 실행')
result = list(filter(lambda x : x%2==0, li))
print('result:', result)

# 다음 리스트 [10, -2, 3, -5, 8, -3]에서 음수를 제거한후, 오름차순으로 정렬 시키는
# 프로그램을 작성하세요 ?
li = [10, -2, 3, -5, 8, -3]
result = list(filter(lambda x : x>0, li))
print('result:', result)
# sort()함수로 오름차순 정렬
result.sort()
print(result)
# sorted()함수로 오름차순 정렬
result2 = sorted(result)
print('reuslt2:', result2)
# print(sorted(result))

# 다음과 같은 정보가 있는 리스트에서 나이(age)를 기준으로 오름차순으로 정렬하는 프로그램을  작성 하세요?
people = [
    {'name': 'noah', 'age': 19},
    {'name': 'liam', 'age': 23},
    {'name': 'jacob', 'age': 9},
    {'name': 'mason', 'age': 21}
]
# 방법1.
people.sort(key=lambda x : x['age'])
print(people)
# 방법2.
result = sorted(people, key=lambda x : x['age'])
print(result)

# 다음과 같은 리스트에 원소중 최대값과 최대값의 위치(인덱스 번호)를 구하는
# 프로그램을 작성하세요?
# [17, 92, 18, 33, 58, 7, 33, 42]
v = [17, 92, 18, 33, 58, 7, 33, 42]
# 최대값 구하기
def find_max(a):
    n = len(a)
    max = a[0]
    for i in range(1, n):
        if a[i] > max:
            max = a[i]
    return max
print(find_max(v))
# 최대값의 위치 구하기
def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx
print(find_max_idx(v))

# 모듈.
# 모듈이란 함수나 변수 또는 클래스 들을 모아 놓은 파일이다
# • 일반적으로는 “독자적인 기능을 갖는 구성 요소”를 의미
# • 서로 연관된 작업을 하는 코드들의 모임으로 작성 중인 모듈의 크기가 어느 정도 커지
# 게 되면 일반적으로 관리 가능한 작은 단위로 다시 분할
# • 파이썬에서는 개별 소스 파일을 일컫는 말
# • 파이썬 프로그램으로 작성된 파일도 가능하고 C나 Fortran 등으로 만든 파이썬 확장파
# 일도 모듈이 될 수 있음

# 모듈의 종류
# 표준 모듈 : 파이썬 언어 패키지 안에 기본적으로 포함된 모듈 예) math, string
# 사용자 생성 모듈 : 프로그래머가 직접 작성한 모듈
# 서드 파티(3rd Party) 모듈 : 파이썬 재단도 프로그래머도 아닌 다른 프로그래머, 또는

# 업체에서 제공한 모듈
# 외부 모듈을 사용할 수 있도록 추가하는 방법은 import 파일명
# 확장자는 생략하고 파일에 있는 변수나 메소드는 파일명.변수 또는 파일명.함수()로 호출

# 자격(Qualified) 변수: 앞의 예에서 처럼 소속을 정확히 밝혀서 사용하는 변수
# 무자격(Unqualified) 변수: 소속을 밝히지 않고 사용하는 변수
# 파이썬은 모듈 가져오기를 수행하면 특별히 지정한 폴더에서 찾아가기 시작합니다.
# sys.path 변수에 그 순서가 기재되어 있습니다.
import sys
print(sys.path) #파이썬 모듈들이 저장되어 있는 위치를 구해줌

# 직접 검색할 위치를 추가: sys.path.append(“검색할 경로”)
# 윈도우의 환경 변수에 추가
# PYTHONPATH = 검색경로;
# 리눅스의 환경 변수에 추가
# C Shell 인 경우: setenv PYTHONPATH 검색경로
# bash Shell 인 경우: export PYTHONPATH =검색경로

# 절대 경로를 이용한 가져오기
import math
#: math 모듈처럼 모듈의 이름만 가져온 경우로 math.해서 사용
from math import sin, cos, pi
#: math 모듈에서 sin, cos, pi 만 가져온 경우로 math.을 생략하고 사용가능
from math import *
#: math 모듈의 모든 이름을 현재 위치로 가져옵니다.
import math as ma
#: math라는 모듈 이름 대신에 ma 사용
from math import pi as py
#: pi 대신에 py 사용
# • 하나의 모듈에서 여러 개의 이름을 가져올 때는 괄호 가능
# • 모듈 이름이 문자열로 되어 있는 경우 __import__(모듈이름) 으로 가져오는 것이 가능
# • 모듈은 한 번 가져오면 메모리에 적재된 상태가 되므로 다른 모든 모듈에서 사용이 가능

# 내장모듈.
# math 모듈
import math
from math import factorial   # math 모듈의 factorial함수만 import

# 원주율(pi) 구하기
print(math.pi)
# 2의 3승 구하기
print('2의 3승:', math.pow(2,3))
# 팩토리얼(fatorial) 구하기
print('3!=', math.factorial(3))
print('1000!=', math.factorial(1000))
print('5!=', factorial(5))
# ceil() 함수 : 올림기능
print(math.ceil(3.1))               # 4
# round() : 반올림기능 (내장함수)
print(round(3.5))                   # 4
# floor() : 내림기능
print(math.floor(3.9))              # 3
# sqrt() : 제곱근
print(math.sqrt(5))                 # 2.23606797749979

# calendar 모듈
import calendar

# calendar()함수는 해당 연도의 달력을 리턴함
cal = calendar.calendar(2020)
print(cal)
# prcal()함수는 2020년 달력을 출력해줌
calendar.prcal(2020)
# prmonth() : 특정 연도의 특정 월에 대한 달력을 출력함.
calendar.prmonth(2020, 6)
# weekday() : 날짜에 해당하는 요일 정보를 리턴
# 월(0), 화(1), 수(2), 목(3), 금(4), 토(5), 일(6)
weekday = calendar.weekday(2020,6,10)
print('weekday:', weekday)          # 2
# 숫자(0~6) 요일을 문자로 변환
week = ['월','화','수','목','금','토','일']
print(week[weekday],'요일')

# random 모듈을 이용한 난수 발생
import random

# random() : 0.0 ~ 1.0 사이의 난수 발생
r1 = random.random()
print('r1=', r1)
# randint(a, b) : a ~ b 사이의 정수 형태의 난수 발생
r2 = random.randint(1, 10)
print('r2=', r2)
# 1 ~ 45 사이의 난수 발생
r3 = random.randint(1, 45)
print('r3=', r3)
# choice() : 컬렉션의 원소를 random하게 선택해주는 함수
list = ['빨강','주황','노랑','초록','파랑','남색','보라']
r4 = random.choice(list)
print('r4=', r4)

# 1 ~ 45 사이의 정수를 6개를 추출하는 프로그램을 작성하세요?
# 단, 중복되지 않는 정수 6개를 추출하세요.
import random
lot = []                          # 비어있는 리스트

# lot.append(random.randint(1,45))
# print(lot)
while True:
    r = random.randint(1,45)       # 1 ~ 45 사이의 난수 발생
    if r not in lot:               # 발생된 난수가 list에 없으면 추가
        lot.append(r)
        if len(lot) == 6:          # list 에 6개의 난수가 저장되면
            break                  # 무한루프를 빠져나옴
print(sorted(lot))                 # list 를 오름차순으로 정렬해서 출력

# time 모듈
import time

#time()은 UTC(Universal Time Coordinated 협정 세계 표준시)를
# 이용하여 현재 시간을 실수 형태로 리턴하는 함수.
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴.
print(time.time())

#localtime()은 time()에 의해서 반환된 실수값을 이용해서
# 연도, 월, 일, 시, 분, 초,.. 의 형태로 바꾸어 주는 함수.
print(time.localtime(time.time()))

#asctime()은 localtime()에 의해서 반환된 튜플 형태의 값을
# 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수
print(time.asctime((time.localtime(time.time()))))

# Wed Jun 10 16:44:36 2020
# ctime()은 현재 시간을 간단하게 리턴하는 함수.
print(time.ctime())
# Wed Jun 10 16:46:29 2020

#strftime('출력할 형식 포맷 코드', time.localtime(time.time())))
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# sleep() 함수를 사용하면 일정 시간 간격을 두고 실행
for i in range(10):
    print(i)
    time.sleep(1)           # 1초 간격으로 실행

# webbrowser 모듈
import webbrowser

# webbrowser 모듈은 기본 웹브라우저가 자동으로 실행되게 해주는 모듈
webbrowser.open('http://www.google.com')
#open_new 함수는 이미 웹 브라우저가 실행된 상태이더라도
# 새로운 창으로 해당 주소가 열리도록 한다.
webbrowser.open_new('http://www.naver.com')

# 사용자 정의 모듈 파일
# filename: mymath.py
mypi = 3.14
def area(r):
    return mypi * r * r

# 사용자 정의 모듈 파일
# filename: calculator.py
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b                # 몫(실수형)

# calculator 모듈을 사용하는 파일
# import  모듈이름
# : calculator 모듈의 모든 변수와 함수를 사용할 수 있다.
import calculator
print(calculator.plus(10, 5))
print(calculator.minus(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))

# from  모듈명  import 변수 또는 함수명
from calculator import plus         # calculator 모듈의 plus함수를 import
from calculator import minus        # calculator 모듈의 minus함수를 import
print(plus(10, 5))
print(minus(10, 5))
print(multiply(10, 5))    # multiply함수는 import를 하지 않았기 때문에 사용할 수 없다.
print(divide(10, 5))      # divide함수는 import를 하지 않았기 때문에 사용할 수 없다.

# from  모듈명  import 변수 또는 함수명
# : 모듈 안에 들어있는 import한 변수나 함수만 사용 할 수 있다.
from calculator import plus, minus
# print(calculator.plus(10, 5))       # 오류발생
print(plus(10, 5))
print(minus(10, 5))
print(multiply(10, 5))    # multiply함수는 import를 하지 않았기 때문에 사용할 수 없다.
print(divide(10, 5))      # divide함수는 import를 하지 않았기 때문에 사용할 수 없다.

# 와일드카드(*)를 이용해서 모듈안에 들어 있는 모든 변수와 함수를 import
# from  모듈명  import  *
# : calculator 모듈의 모든 변수, 함수를 import 한다.
from calculator  import *
# print(calculator.plus(10, 5))           # 오류 발생
print(plus(10, 5))
print(minus(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

# import  모듈명  as  별칭
import calculator  as  c
# 별칭이 부여된 다음에는 별칭명만 사용할 수 있다.
print(calculator.plus(10,5))            # 오류 발생
print(c.plus(10,5))
print(c.minus(10,5))
print(c.multiply(10,5))
print(c.divide(10,5))

# my_package패키지 안의 calculator 모듈 파일 불러오기: 생략

# 방법1.
# from  패키지명  import  모듈파일명
from  my_package  import calculator
print(calculator.plus(10, 5))
print(calculator.minus(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))
# 방법2.
# import  패키지명.모듈명
import my_package.calculator
print(my_package.calculator.plus(10,5))
print(my_package.calculator.minus(10,5))
print(my_package.calculator.multiply(10,5))
print(my_package.calculator.divide(10,5))
# 방법3.
# import  패키지명.모듈명  as 별칭명
import my_package.calculator  as cal
print(cal.plus(10,5))
print(cal.minus(10,5))
print(cal.multiply(10,5))
print(cal.divide(10,5))

# 외부 모듈파일 불러오기
import numpy as np
import pandas as pd

# 1차원 배열
a = np.array([1,2,3,4,5])
print(a)
# 1차원 배열 : 한가지 자료형으로 처리
b = np.array([1, 2.0, 3, 4, 5])
print(b)            # [1. 2. 3. 4. 5.]

# 그래프 그리기
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1])
plt.ylabel('some numbers')
plt.show()


# <<강의 복습 4. 끝>>
# pywork11.py end
