# pywork10.py start
# <<강의 복습 3. 시작>>


# 자료형.
# 문자열 자료형: '', "", ''', """
s1 = 'Hello World'
print(type(s1))              # <class 'str'>
print(s1)
s2 = "Python is fun"
print(type(s2))             # <class 'str'>
print(s2)
s3 = '''Life is too short, you need python.'''
print(type(s3))             # <class 'str'>
print(s3)
s4 = """Life is too short, you need python."""
print(type(s4))             # <class 'str'>
print(s4)

# 문자열 연산하기: +, *(반복)
head = 'Python'
tail = ' is fun'
str = head + tail
print(str)              # Python is fun
print(head + tail)      # Python is fun

s = 'python'
print(s * 2)            # 2번 반복 : pythonpython
print(s * 3)            # 3번 반복 : pythonpythonpython

print('='*50)           # 50번 반복
print('My Program')
print('='*50)           # 50번 반복

print('*'*1)
print('*'*2)
print('*'*3)
print('*'*4)
print('*'*5)

# 인덱싱 : 인덱스 번호를 이용해서 특정 문자를 추출 하는 것
# s[인덱스 번호]
s = 'Life is too short, you need python'
print(s)
print(s[0])         # 인덱스 0번 문자 추출 : L
print(s[3])         # 인덱스 3번 문자 추출 : e
print(s[-1])        # 마지막 문자를 추출 : n
print(s[-2])        # 끝에서 2번째 문자를 추출 : o

# 슬라이싱 : 문자열 중에서 시작 인덱스 번호부터 끝인덱스 번호까지 잘라서 추출 하는 것
# 형식 : 변수 [ 시작 인덱스 번호 : 끝 인덱스 번호 ]
# 시작 인덱스 번호부터 끝인덱스 번호-1번 까지 슬라이싱
s = 'Life is too short, you need python'
print(s[0:2])       # 인덱스 0번부터 1번까지 슬라이싱 : Li
print(s[0:5])       # 인덱스 0번부터 4번까지 슬라이싱 : Life
print(s[5:7])       # 인덱스 5번부터 6번까지 슬라이싱 : is
print(s[12:17])     # 인덱스 12번부터 16번까지 슬라이싱 : short
print(s[:7])        # 처음부터 인덱스 6번까지 슬라이싱 : Life is
print(s[5:])        # 인덱스 5번부터 끝까지 슬라이싱 : is too short, you need python
print(s[:])         # 처음부터 끝까지 슬라이싱

# 날짜와 날씨를 슬라이싱으로 분리
str = '20191024Rainy'
date = str[:8]              # 20191024
weather = str[8:]           # Rainy
print(date,':',weather)

# str변수의 년, 월, 일을 슬라이싱
year = str[:4]              # 2019
month = str[4:6]            # 10
day = str[6:8]              # 24
print(year, '년', month, '월', day, '일')  # 2019 년 10 월 24 일

str = 'korea'
print(str[0])       # 인덱스 0번 문자 추출 : k
print(str[-2])      # 끝에서 2번째 문자를 추출 : e
print(str[1:3])     # 인덱스 1번부터 2번까지 슬라이싱 : or
print(str[0:5:2])   # 인덱스 0번부터 4번까지 2씩 증가된 번호로 슬라이싱 : kra
print(str[:-1])     # 처음부터 끝에서 2번째 문자까지 슬라이싱 : kore
print(str[::-1])    # 반대로 출력 : aerok

# 키보드로 주민번호 13자리를 입력 받았을때 남자인지 여자인지를 판별하는 프로그램을 작성하세요?
# ex)  9501011234567
# 1.주민번호는 하이픈(-) 없이 13자리를 입력한다.
# 2.입력한 주민번호가 13자리가 아닌경우에 메세지를 출력한다.
jumin = input('주민번호 입력')
if len(jumin) !=13:
    print('13자리 입력')
elif jumin[6] == '1' or jumin[6] == '3':
    print('남자')
elif jumin[4] == '1' or jumin[6] == '4':
    print('여자')
else:
    print('제대로 입력')


# 문자 변경 : pithon  ->  python
s = 'pithon'
print(s[1])                 # i
# i  -> y 변경
# s[1] = 'y'                # 오류 발생
s = s[:1]  + 'y' + s[2:]    # python
print(s)

# 파이썬의 형변환 함수
# str(): 숫자(정수, 실수)를 문자로 변환해주는 함수    30     ->  '30'
# int(): 문자를 정수로 변환해주는 함수              '30'    ->  30
# float(): 문자를 실수로 변환 해주는 함수           '3.14'  ->  3.14
num1 = 1234; num2 = 3.14
print(type(num1))                   # <class 'int'>
print(type(num2))                   # <class 'float'>

# str() :  숫자(정수, 실수)를 문자로 변환
str1 = str(num1)
str2 = str(num2)
print(type(str1))                   # <class 'str'>
print(type(str2))                   # <class 'str'>
print('num1을 문자열로 변환한 값은 %s 입니다.' %str1)
print('num2을 문자열로 변환한 값은 %s 입니다.' %str2)

# 정수, 실수구분
numstr = input('숫자를 입력하세요?')
print(type(numstr))                             # <class 'str'>
try:
    num = int(numstr)                           # 문자를 정수로 변환
    print('당신이 입력한  숫자는 %d 입니다' %num)
except:
    try:
        num = float(numstr)                     # 문자를 실수로 변환
        print('당신이 입력한 숫자는 실수 %f입니다'%num)
    except:
        print('숫자를 입력하세요')

# escape 문자
# 1.이스케이프 문자는 프로그래밍을 할때 사용 할 수 있도록 미리 정의된 문자조합으로
#   출력물을 보기좋게 정렬하는 용도로 사용된다.
# 2. 이스케이프 문자는  '\' 로 시작한다.

#   이스케이프 문자                설명
#------------------------------------------------------
#      \n                     줄 바꾸기
#      \t                     탭 키로 간격 조절
#      \\                     문자 \ 를 출력
#      \'                     문자 ' 를 출력
#      \"                     문자 " 를 출력

print('나는 파이썬을 사랑합니다.\n 파이썬은 자바보다 쉽습니다.')
print('Name:John Simth\tSex:Male\tAge:22')
print('작은 따옴표(\')와 큰 따옴표(\")는 문자열을 정의할때 사용합니다.')
print('\'python\"')             # 'python"
print('\\자바\\')               # \자바\

# 문자열 포맷팅
# 문자열에서 변화는 값을 나타내는 포맷 문자열은 % 기호를 사용한다.

#   포맷 문자열                  설명
#------------------  문자열(string) 출력         --------------------------------
#     %s
#     %c                       문자나 기호 1개(character) 출력
#     %d                       정수 출력
#     %f                       실수 출력
#     %%                       '%' 라는 기호 자체를 출력

txt1 = '자바'; txt2 = '파이썬'
num1 = 5; num2 = 10

print('나는 %s보다 %s에 더 익숙합니다.' %(txt1, txt2))
print('%s은 %s보다 %d배 더 쉽습니다.' %(txt2,txt1,num1))
print('%d+%d=%d' %(num1,num2,num1+num2))
print('작년 세계 경제 성장률은 전년에 비해 %d%% 포인트 증가했다.'%num1)

# 문자열의 대소문자 변환 메서드
#  upper(): 대문자로 변환
#  lower(): 소문자로 변환
#  swapcase(): 대소문자 스위치
#  capitalize(): 첫 글자맊 대문자로 변환
#  title: 각 단어의 첫 글자를 대문자로 변환

# 문자열의 검색 관련 메서드
#  count(문자열): 문자열의 횟수
#  find(문자열): 문자열이 있을 때 오프셋 반홖
#  find(문자열, 숫자): 숫자 위치부터 문자열을 검색해서 오프셋 반환
#  찾는 문자열이 없을 때는 -1을 반환
#  rfind(문자열): 뒤에서부터 검색
#  index(문자열): 문자열이 없을 경우 예외 발생
#  rindex(문자열): 문자열을 뒤에서부터 검색하고 없으면 예외 발생
#  startswith(문자열): 문자열로 시작하는지 여부를 검사해서 bool로 리턴
#  endswith(문자열): 문자열로 끝나는지 여부를 검사
#  startswith(문자열, 숫자): 숫자에 해당하는 위치가 문자열로 시작하는지
#                               여부를 검사해서 bool로 리턴
#  endswith(문자열, 숫자1, 숫자2): 숫자1부터 숫자2까지의 문자열이
#                                   문자열로 끝나는지 여부를 검사

# 문자열의 편집과 치환 메서드
#  strip(): 좌우 공백 제거
#  rstrip(): 오른쪽 공백 제거
#  lstrip(): 왼쪽 공백 제거
#  strip('문자열'): 좌우의 문자열을 제거
#  replace(문자열1, 문자열2): 앞의 문자열을 뒤의 문자열로 치환

# 문자열의 분리와 결합 관련 메서드
#  split(): 공백으로 문자열을 분리해서 리스트로 반환
#  split('문자열'):문자열로 분리해서 리스트로 반환
#  split('문자열', 숫자):문자열로 분리하는데 숫자만큼만 분리해서 리스트로 반환
#  '문자열'.join(문자열 리스트): 문자열 리스트를 문자열을 각 요소 별로 문자열을
#                               추가해서 결합
#  splitlines(): 줄 단위로 분리
# 맞춤 관렦 메서드
#  center(숫자): 숫자 맊큼의 자리를 확보하고 가운데 맞춤
#  ljust(숫자): 왼쪽 맞춤
#  rjust(숫자): 오른쪽 맞춤
#  center(숫자, 문자열): 숫자 맊큼의 자리를 확보하고 가운데 맞춤한 후
#                       빈자리는 문자열로 찿움

# 탭 문자 변환 메서드
#  expandtabs(숫자): 숫자를 생략하면 탭을 8자 공백으로 변경하고 숫자를 대입하면
# 숫자만큼의 공백으로 변경

# 문자열 확인 메서드
#  isdigit()
#  isnumeric()
#  isdecimal()
#  isalpha()
#  isalnum()
#  islower()
#  isupper()
#  isspace()
#  istitle()
#  isidentifier()
#  isprintable()

# 문자열 매핑 메서드
#  maketrans()와 translate()를 이용하면 문자열 매핑 가능
#  maketrans()를 이용해서 치환할 문자열을 만들고 translate의 매개변수로 대입
# instr = 'abcdef'
# outstr = '123456'
# trans = ''.maketrans(instr, outstr)
# str = 'hello world'
# print(str.translate(trans))

# upper(), lower(), swapcase(), capitalize(), title()
txt = 'A lot of Things occur each day.'
result1 = txt.upper()           # A LOT OF THINGS OCCUR EACH DAY.
result2 = txt.lower()           # a lot of things occur each day.
result3 = txt.swapcase()        # a LOT OF tHINGS OCCUR EACH DAY.
result4 = txt.capitalize()      # A lot of things occur each day.
result5 = txt.title()           # A Lot Of Things Occur Each Day.
print('result1:', result1)
print('result2:', result2)
print('result3:', result3)
print('result4:', result4)
print('result5:', result5)

# count() : 문자열에서 특정 문자의 갯수를 구해주는 함수
txt = 'A lot of things occur each day, every day.'
count1 = txt.count('o')     # 영문 'o' 의 갯수 구함
count2 = txt.count('day')   # 영문 'day' 의 갯수 구함
count3 = txt.count(' ')     # 공백의 갯수를 구함
print('count1:', count1)
print('count2:', count2)
print('count3:', count3)

# len() : 문자열의 길이를 구해주는 함수
msg = input('임의의 문장을 입력하세요?')
print(type(msg))    # <class 'str'>
len = len(msg)      # 문자열의 길이를 구함(글자수)
print('당신이 입력한 문장의 길이는', len,'입니다.')
print('당신이 입력한 문장의 길이는 {} 입니다.'.format(len))
print('당신이 입력한 문장의 길이는 %d 입니다.'%len)

# find() :  특정 문자의 index번호를 구해주는 함수
txt = 'A lot of things occurs each day, every day.'
offset1 = txt.find('e')        # 가장 먼저 나오는 'e'의 인덱스번호를 리턴
offset2 = txt.find('day')      # 가장 먼저 나오는 'day'의 인덱스번호를 리턴
offset3 = txt.find('day', 30)  # 인덱스번호 30번 이후에 나오는 day의 인덱스번호를 리턴
offset4 = txt.find('j')        # 찾는 문자가 없을 경우에는 -1을 리턴
print('offset1:', offset1)     # offset1: 23
print('offset2:', offset2)     # offset2: 28
print('offset3:', offset3)     # offset3: 39
print('offset4:', offset4)     # offset4: -1

# isdigit() : 문자열이 숫자인지 판별할 때 사용되는 함수
# : 문자열을 구성하는 요소가 모두 숫자이면 True를 리턴
#   문자(영문자,특수문자)가 포함되어 있으면 False를 리턴
txt1 = '010-1234-5678'
txt2 = 'R2D2'
txt3 = '1212'
result1 = txt1.isdigit()
result2 = txt2.isdigit()
result3 = txt3.isdigit()
print('result1:', result1)      # False  : 하이픈('-')
print('result2:', result2)      # False  : 영문 알파벳
print('result3:', result3)      # True

# join() : 문자열을 특정 문자열로 결합할때 사용하는 함수
a = ','
s = 'abcd'
result = a.join(s)
print('result:', result)        # a,b,c,d

b = '_'
list = ['사과','배','포도','수박','키위','바나나']
result1 = b.join(list)
print('result1:', result1)     # 사과_배_포도_수박_키위_바나나
bond = ';'

loglist = ['2020/05/25 10:12:25','200','ok','이 또한 지나가리라']
result2 = bond.join(loglist)
print(type(result2))           # <class 'str'>
print('result2:', result2)     # 2020/05/25 10:12:25;200;ok;이 또한 지나가리라

# replace() : 특정 문자열을 다른 문자열로 치환할때 사용하는 함수
# replace('data1', 'data2') : data1을 data2로 치환
txt = 'My password is 1234'
result1 = txt.replace('1','0')          # '1'을 '0'으로 치환
result2 = txt.replace('1','python')     # '1'을 'python'으로 치환
print('result1:', result1)
print('result2:', result2)
txt1 ='매일 많은 일들이 일어납니다.'
result3 = txt1.replace('매일', '항상')  # '매일'을 '항상'으로 치환
result4 = txt1.replace('일', '사건')    # '일'을 '사건'으로 치환
print('result3:', result3)
print('result4:', result4)

# sorted() : 문자열을 정렬할때 사용하는 함수
#            특정 변수에 저장된 데이터를 오름차순으로 정렬해주는 함수
# 오름차순 정렬 : sorted( data )
# 내림차순 정렬 : sorted( data ,  reverse = True )

#        오름차순 정렬                  내림차순 정렬
#----------------------------------------------------------------
#  숫자   1, 2, 3,...                  10, 9, 8,....
#  문자   사전순 정렬(a,b,c...)         사전역순 정렬(z, y, x,...)

strdata = input('정렬할 문자열을 입력하세요?')  # python
# 오름차순 정렬
result1 = sorted(strdata)
print(type(result1))                # <class 'list'>
print(result1)                      # ['h', 'n', 'o', 'p', 't', 'y']
# 내림차순 정렬
result2 = sorted(strdata, reverse=True)
print(type(result2))                # <class 'list'>
print(result2)                      # ['y', 't', 'p', 'o', 'n', 'h']

# split() : 문자열을 특정 문자(구분기호)로 분리 시키는 함수
# split('구분기호')
s = 'Life is too short'
result = s.split(' ')       # 공백으로 파싱(parsing)
print(type(result))         # <class 'list'>
print(result)               # ['Life', 'is', 'too', 'short']

s1 = 'python:java:oracle:jsp:spring:tensorflow'
result1 = s1.split(':')     # 콜론(:)으로 파싱
print(result1)              # ['python', 'java', 'oracle', 'jsp', 'spring', 'tensorflow']
for i in result1:
    print(i)

# lstrip() : 문자열 좌측의 공백을 없애주는 역할
# rstrip() : 문자열 우측의 공백을 없애주는 역할
# strip() : 문자열 좌.우의 공백을 없애주는 역할
txt = '   양쪽에 공백이 있는 문자열입니다.   '
result1 = txt.lstrip()
result2 = txt.rstrip()
result3 = txt.strip()
print('<' + txt + '>')
print('<' + result1 + '>')
print('<' + result2 + '>')
print('<' + result3 + '>')

# 리스트.
# 1. 순차적인 자료구조 (인덱스 번호 순으로 저장)
# 2. 대괄호([ ])안에 데이터를 저장한다.
# 3. 리스트의 원소들은 수정이 가능하다.
# 4. 여러가지 자료형의 데이터를 혼용해서 저장할 수 있다.

# 방법1
a = []                          # 비어있는 리스트
b = [10, 20, 30]
c = ['파이썬','자바','오라클','JSP','Spring','tensorflow','keras']
d = [30, 3.14, True, False, 'java']
list1 = ['사과','포도','바나나','키위','복숭아', 30]
print(type(list1))              # <class 'list'>
print(list1)                    # ['사과', '포도', '바나나', '키위', '복숭아', 30]
print(list1[0])                 # 사과
print(list1[1])                 # 포도
list1[0] = 'apple'              # '사과'를 apple로 수정
print(list1[0])                 # apple

# 방법2
# list(), range() 함수를 이용해서 연속적인 데이터를 가진 리스트 생성
ls1 = list(range(10))           # 0 ~ 9
ls2 = list(range(1,11))         # 1 ~ 10
ls3 = list(range(1,11,2))       # 1, 3, 5, 7, 9
print('ls1:', ls1)              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('ls2:', ls2)              # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('ls3:', ls3)              # [1, 3, 5, 7, 9]

# 리스트의 인덱싱
s = ['자바','파이썬','오라클','스프링','텐서플로우']
print(s)
print(s[0])                 # '자바'
print(s[1])                 # '파이썬'
print(s[2])                 # '오라클'
print(s[3])                 # '스프링'
print(s[4])                 # '텐서플로우'
print(s[-1])                # 가장 마지막 원소를 인덱싱 : '텐서플로우'
print(s[-2])                # 끝에서 2번째 원소를 인덱싱 : '스프링'

# 1 ~ 12월을 3자리 약어로 출력하는 프로그램 작성
#  ex) January  ->  Jan
months = ['January','February','March','April','May','June',
          'July','August','September','October','November','December']
for i in range(len(months)):
    months[i] = months[i][:3]
print(months)

# 중첩 리스트
listdata = [1, 2, 'a', 'b', 'c', [4, 5, 6]]
data1 = listdata[1]
data2 = listdata[3]
data3 = listdata[5]
data4 = listdata[5][1]
data5 = listdata[-1]
print('data1:', data1)      # 2 출력
print('data2:', data2)      # b 출력
print('data3:', data3)      # [4, 5, 6] 출력
print('data4:', data4)      # 5 출력
print('data5:', data5)      # [4, 5, 6] 출력

# 삼중 리스트
list = [1, 2, ['a', 'b', ['Life', 'is']]]
data1 = list[2][2][0]
data2 = list[2][2][-1]
data3 = list[2][-1]
print('data1:', data1)        # Life
print('data2:', data2)        # is
print('data3:', data3)        # ['Life', 'is']

# 리스트의 슬라이싱
# [ 시작 index : 끝 index ]
# 시작 인덱스 부터 끝인덱스-1 까지 슬라이싱
s = ['자바','파이썬','오라클','스프링','텐서플로우']

# 인덱스 0~1번 원소 슬라이싱
print(s[0:2])                           # ['자바', '파이썬']
# 인덱스 1~2번 원소 슬라이싱
print(s[1:3])                           # ['파이썬', '오라클']
# 처음부터 인덱스 2번 원소까지 슬라이싱
print(s[:3])                            # ['자바', '파이썬', '오라클']
# 인덱스 2번부터 끝까지 슬라이싱
print(s[2:])                            # ['오라클', '스프링', '텐서플로우']

# 중첩 리스트에서 슬라이싱
s1 = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# 인덱스 2~4번까지 원소를 슬라이싱
print(s1[2:5])                          # [3, ['a', 'b', 'c'], 4]
print(s1[3][:2])                        # ['a', 'b']

import  numpy as np
s3 = [[1,2,3],[4,5,6],[7,8,9]]
a1 = np.array(s3)
print(a1)

# 리스트의 연산 : +, *(반복)
# 리스트의 연산 : +
data1 = ['a','b','c','d','e']
data2 = ['f','g','h','i','j','k']
result1 = data1 + data2
result2 = data2 + data1
print('result1:', result1)    # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
print('result2:', result2)    # ['f', 'g', 'h', 'i', 'j', 'k', 'a', 'b', 'c', 'd', 'e']

# 리스트의 연산 : *
listdata = list(range(3))     # [0, 1, 2]
print(listdata)

result = listdata * 3         # listdata를 3번 반복한 리스트
print('result:', result)      # [0, 1, 2, 0, 1, 2, 0, 1, 2]

# list 메서드
#  append(값): 마지막에 데이터 추가
#  insert(인덱스, 데이터): 인덱스 위치에 데이터를 삽입
#  index(데이터): 데이터의 위치를 검색
#  count(): 요소의 개수 리턴
#  sort(): 리스트를 정렬
#  reverse(): 리스트의 순서를 변경
#  remove(데이터): 데이터의 첫번째 것을 삭제
#  pop(인덱스): 인덱스를 생략하면 가장 마지막 데이터를 삭제하고 리턴하고 인덱스를
#                대입하면 인덱스 번째를 삭제하고 리턴
#  extend(리스트): 리스트를 추가

# Stack
#  나중에 삽입한 데이터를 먼저 꺼내도록 해주는 메모리 구조
#  LIFO(Last In First Out)구조의 메모리
#  데이터를 삽입하는 연산을 push라 하고 꺼내는 연산을 pop이라고 합니다.
#  리스트는 스택으로 사용할 수 있게 설계되었습니다.
#  push 연산은 append()를 이용하면 되고 pop 연산은 pop() 메서드를 이용하면 된다.
stack = [10,20,30,40,50]
stack.append(60) #push
print(stack)
data = stack.pop() #pop
print(data)
print(stack)

# Queue
#  먼저 삽입한 데이터를 먼저 꺼내도록 해주는 메모리 구조
#  FIFO(First In First Out)구조의 메모리
#  리스트는 큐로 사용할 수 있게 설계되었습니다.
#  push 연산은 append()를 이용하면 되고 pop 연산은 pop(0) 메서드를 이용하면 된다.
queue = [10,20,30,40,50]
queue.append(60) #push
print(queue)
data = queue.pop(0) #pop
print(data)
print(queue)

# sum() : 리스트의 모든 원소들의 합을 구해주는 함수
listdata = [2,2,1,3,8,5,7,6,3,6,2,3,9,4,4]
list = list(range(1,11))        # 1 ~ 10
result1 = sum(listdata)
result2 = sum(list)
print('result1:', result1)      # 65
print('result2:', result2)      # 55

# len() : 리스트에 있는 모든 원소의 갯수를 구해주는 함수
listdata = [2,2,1,3,8,5,7,6,3,6,2,9,4,4]
length = len(listdata)
print('원소의 갯수:', length)     # 14개의 원소

# count() : 리스트의 특정 원소의 갯수를 구해주는 함수
listdata = [2,2,1,3,8,5,7,6,3,2,9,4,4]
list = ['python','java','oracle','PYTHON','java','oracle','spring']
c1 = listdata.count(2)      # listdata에서 값이 2인 원소의 갯수를 구함
c2 = listdata.count(7)      # listdata에서 값이 7인 원소의 갯수를 구함
c3 = list.count('java')     # list에서 값이 'java'인 원소의 갯수를 구함
c4 = list.count('python')   # list에서 값이 'python'인 원소의 갯수를 구함
c5 = list.count('JAVA')     # list에서 값이 'JAVA'인 원소의 갯수를 구함
                            # 찾는 원소가 없을 경우에는 0을 리턴
print('c1:', c1)            # 3
print('c2:', c2)            # 1
print('c3:', c3)            # 2
print('c4:', c4)            # 1
print('c5:', c5)            # 0

# append() : 리스트에 새로운 원소를 추가 할때 사용하는 함수
a = [1, 2, 3]
a.append(4)              # 4 추가
print('a:', a)           # [1, 2, 3, 4]
a.append([5, 6])        # [5, 6] 추가
print('a:', a)          # [1, 2, 3, 4, [5, 6]]

# n 번째 피보나치 수열을 구하는 코드를 작성하시오
# (1,1,2,3,5,8,13.. f(n) = f(n-1) + f(n-2) 단,f(1)=1, f(2)=1)
'''
피보나치 수열: 첫번째와 두번째는 무조건 1
             세번째 부터는 앞의 2개의 합
    1, 1, 2, 3, 5, 8, 13, 21, 34....
    예측이나 그래프 등을 그릴 때 많이 사용하는 알고리즘
'''
n = int(input('n번째 피보나치 수열 찾기'))
a=[1, 1]
for p in range(2, n):
    a.append(1)
    a[p] = a[p-2] + a[p-1]
print(n, '번째 값: ', a[n-1])


#-------------------------------------------------------
listdata = []           # 비어있는 리스트
for i in range(3):      # 0 ~ 2
    txt = input('리스트에 추가할 값을 입력하세요?[%d/3]'%(i+1))
    listdata.append(txt)
    print(listdata)
print(listdata)

# index() : 리스트에서 특정 원소의 인덱스 번호를 구해주는 함수
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성','지구']
planet = '지구'

# 가장 먼저 나오는 '지구'의 인덱스 번호를 구함
pos = solarsys.index(planet)            # 인덱스 번호 : 3
print('%s은(는) 태양계에서 %d번째 위치하고 있습니다'%(planet, pos))

# 인덱스번호 5번 이후에 나오는 '지구'의 인덱스 번호를 구함
pos = solarsys.index(planet, 5)            # 인덱스 번호 : 9
print('%s은(는) 태양계에서 %d번째 위치하고 있습니다'%(planet, pos))

# 찾는 원소가 없는 경우에는 오류 발생
# pos = solarsys.index('명왕성')

# insert() : 리스트의 특정 위치에 원소를 삽입할때 사용하는 함수
# insert( 인덱스 번호, 데이터 )
a = [1, 2, 3]
# 인덱스 0번 위치에 4를 삽입
a.insert(0, 4)
print('a:', a)          # [4, 1, 2, 3]
# 인덱스 3번 위치에 5를 삽입
a.insert(3, 5)
print('a:', a)          # [4, 1, 2, 5, 3]

solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
pos = solarsys.index('목성')      # '목성' 의 인덱스 번호를 구함 : pos = 5
print('pos:', pos)
solarsys.insert(pos, '소행성')    # 인덱스 5번 위치에 '소행성' 을 삽입
print(solarsys)

# remove() : 리스트의 특정 원소를 삭제하는 함수
# remove('삭제할 데이터')
a = [1,2,3,1,2,3]
a.remove(3)         # 리스트에서 첫번째로 나오는 3을 삭제
print(a)            # [1, 2, 1, 2, 3]
a.remove(3)        # 리스트에서 두번째로 나오는 3을 삭제
print(a)            # [1, 2, 1, 2]

# del 명령 : 리스트의 특정 원소를 index번호로 삭제하는 명령
# del  a[index번호]
a = [1, 2, 3]
del a[1]                # 인덱스 1번 원소 삭제
print(a)                # [1, 3]

b = [1, 2, 3, 4, 5]
del b[2:]               # 인덱스 2번 원소부터 끝까지 삭제
print(b)                # [1, 2]

del b                   # 리스트 b를 메모리상에서 삭제
print(b)                # NameError: name 'b' is not defined

# pop() : 리스트의 마지막 원소를 삭제하고 리턴하는 함수
# pop() : 가장 마지막 원소 삭제하고 리턴
# pop(인덱스 번호) : 인덱스 번호의 원소 삭제하고 리턴
list = [10, 20, 30, 40, 50]
data1 = list.pop()              # 마지막 원소인 50을 삭제하고 50을 리턴
print('data1:', data1)          # data1: 50
print('list:', list)            # list: [10, 20, 30, 40]

data2 = list.pop(2)             # 인덱스 2번 원소(30)를 삭제하고 리턴
print('data2:', data2)          # data1: 30
print('list:', list)            # list: [10, 20, 40]

# 리스트에서 홀수, 짝수 슬라이싱
# [ start index : end index ]
# [ start index : end index : step ]
listdata = list(range(1,101))    # 1 ~ 100
print(listdata)                  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,

# 짝수 슬라이싱
evenlist = listdata[1 :  : 2]    # 인덱스 1번 부터 step 2 로 슬라이싱
print('evenlist:', evenlist)
# 홀수 슬라이싱
oddlist = listdata[ : : 2]       # 인덱스 0번 부터 step 2 로 슬라이싱
print('oddlist:', oddlist)

# shuffle() : 리스트의 원소들을 무작위로 섞어주는 역할을 하는 함수
#             실행 결과가 매번 달라진다.
# import  모듈명
import random
listdata = list(range(1,11))            # 1 ~ 10
print('listdata:', listdata)            # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(3):                      # 3번 루프를 돌린다.
    random.shuffle(listdata)
    print(listdata)

# sort() : 리스트에 있는 원소를 오름차순으로 정렬해주는 역할을 하는 함수
# 사용형식 : 리스트.sort()
# 오름차순 정렬 :  리스트.sort()
# 내림차순 정렬 :  리스트.sort( reverse = True )
# sort() 함수를 이용해서 정렬을 하면 원본 리스트가 변경된다.

#        오름차순 정렬                  내림차순 정렬
#---------------------------------------------------------------------------
#  숫자   1, 2, 3,...                  10, 9, 8,....
#  문자   사전순 정렬(a,b,c...)         사전역순 정렬(z, y, x,...)

namelist = ['Mary','Sams','Aimy','Tom','Michale','Bob','Kelly']
namelist.sort()                 # 오름차순 정렬
print('namelist:', namelist)    # ['Aimy', 'Bob', 'Kelly', 'Mary', 'Michale', 'Sams', 'Tom']
namelist.sort( reverse=True )   # 내림차순 정렬
print('namelist:', namelist)    # ['Tom', 'Sams', 'Michale', 'Mary', 'Kelly', 'Bob', 'Aimy']

# sorted() : 리스트에 있는 원소를 오름차순으로 정렬해주는 역할
# 사용형식 : sorted( 리스트 )
# 오름차순 정렬 : sorted( 리스트 )
# 내림차순 정렬 : sorted( 리스트, reverse = True )
# sorted() 함수를 이용해서 정렬을 하면 원본 리스트가 변경되지 않는다.

#        오름차순 정렬                  내림차순 정렬
#----------------------------------------------------------------
#  숫자   1, 2, 3,...                  10, 9, 8,....
#  문자   사전순 정렬(a,b,c...)         사전역순 정렬(z, y, x,...)

namelist = ['Mary','Sams','Aimy','Tom','Michale','Bob','Kelly']

result1 = sorted(namelist)                      # 오름차순 정렬
result2 = sorted(namelist, reverse=True)        # 내림차순 정렬
print(type(result1))                            # <class 'list'>
print(type(result2))

print('result1:', result1)   # ['Aimy', 'Bob', 'Kelly', 'Mary', 'Michale', 'Sams', 'Tom']
print('result2:', result2)   # ['Tom', 'Sams', 'Michale', 'Mary', 'Kelly', 'Bob', 'Aimy']

# sorted() 함수로 정렬하더라도 원래 namelist는 변경되지 않는다.
print('namelist:', namelist) # ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']

# reverse() : 리스트의 원소의 순서를 역순으로 바꾸어 주는 역할
# reverse() 함수는 원본 리스트 자체를 변경한다.
# 사용형식 : 리스트.reverse()
listdata = list(range(10))          # 0 ~ 9
print(listdata)                     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listdata.reverse()                  # listdata 역순으로 변경
print(listdata)                     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# [1, 3, 5, 4, 2] 라는 리스트를 [5, 4, 3, 2, 1]로 변경 하세요?
list = [1, 3, 5, 4, 2]

# 방법1. sort()
list.sort( reverse= True)               # 내림차순 정렬
print('list:', list)
# 방법2. sort(), reverse()
list.sort()                             # 오름차순 정렬
list.reverse()                          # 역순으로 정렬
print('list:', list)
# 방법3. sorted()
list3 = sorted(list, reverse=True)      # 내림차순 정렬
print('list3:', list3)
# 방법4. sorted(), reverse()
list4 = sorted(list)                    # 오름차순 정렬
list4.reverse()                         # 역순으로 정렬
print('list4:', list4)

# 튜플(tuple)
# 1. 순차적인 자료구조이다.
# 2. 튜플 데이터는 괄호() 안에 데이터를 저장한다.
# 3. 튜플 데이터는 수정 할 수 없다.
# 4. 튜플은 여러가지 자료형의 데이터를 혼용해서 저장할 수 있다.
t1 = ()                 # 비어있는 튜플
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a', 'b', 'c', ('ab', 'cd'))
print(type(t1))        # <class 'tuple'>
print(type(t2))        # <class 'tuple'>
print('t1:', t1)
print('t2:', t2)
print('t3:', t3)
print('t4:', t4)
print('t5:', t5)

# 1. 튜플의 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])                # 1
print(t1[1])                # 2
print(t1[2])                # a
print(t1[3])                # b
print(t1[-1])               # b

# 2. 튜플의 슬라이싱
# [ start index : end index ]
t2 = (10, 20, 30, 40, 50)
print(t2[1:3])             # 인덱스 1~2번까지 슬라이싱 : (20, 30)
print(t2[ :4])             # 처음부터 3번까지 슬라이싱 : (10, 20, 30, 40)
print(t2[1 :])             # 인덱스 1번부터 끝까지 슬라이싱 : (20, 30, 40, 50)

# 3. 튜플 더하기 : +
print(t1 + t2)            # (1, 2, 'a', 'b', 10, 20, 30, 40, 50)
print(t2 + t1)            # (10, 20, 30, 40, 50, 1, 2, 'a', 'b')

# 4. 튜플 곱하기 : * (반복)
print(t2 * 3)             # 튜플 t2의 원소를 3번 반복
                          # (10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

# 튜플에서 지원되는 함수
# 1. len() : 튜플 원소의 갯수를 구해주는 함수
t1 = (10, 20, 30, 40, 50)
print(len(t1))              # 튜플 원소의 갯수 : 5
print(t1)

# 2. count() : 튜플의 특정 원소의 갯수를 구해주는 함수
t2 = (1,100,2,100,3,100,4,100,5,100)
print(t2.count(100))        #  튜플의 원소 100의 갯수 : 5

# 3. index() : 튜플의 특정 원소의 인덱스 번호를 구해주는 함수
t3 = ('java','jsp','python','spring','R','tensorflow','keras')
print(t3.index('spring'))   # 'spring' 원소의 index번호 : 3

# 튜플은 원소의 값을 수정 할 수 없다.
t1 = (10,20,30,40,50)
print(t1)                # (10, 20, 30, 40, 50)
print(t1[0])             # 10
# t1[0] = 100            # 오류발생(인덱스 0번 원소를 100으로 수정할 수 없다.)

# 튜플 패킹(tuple packing) : 여러 데이터를 튜플로 묶는 것
t2 = 10, 20, 30
print(type(t2))         # <class 'tuple'>
print(t2)               # (10, 20, 30)

# 튜플 언패킹(tuple unpacking)
# : 튜플의 각 원소를 여러개의 변수에 할당하는 것
# : 튜플 원소의 갯수와 변수의 갯수가 일치되지 않으면 에러발생
one, two, three = t2
print('one:', one)
print('two:', two)
print('three:', three)

# 언패킹을 이용한 다중 할당
city, latitude, longitude = 'Seoul', 37.541, 126.986
print('city:', city)
print('latitude:', latitude)
print('longitude:', longitude)

# set.
#  데이터를 순서와 상관없이 중복 없이 모아놓은 자료형으로 set과 frozenset
# 두 가지 자료형을 제공
#  빈 객체 생성은 set()
#  처음부터 데이터를 가지고 있는 경우에는 {데이터 나열}
#  데이터가 없는 경우에는 { } 대싞 set()으로 생성하는 이유는 디셔너리와의 혼동의 문제
#  튜플, 문자열, 리스트 및 디셔너리로부터 생성이 가능
#  set의 원소로 변경이 가능한 데이터 타입은 불가하다.
hashset = set()
print(hashset)
hashset = {1,2,3}
print(hashset)
hashset = set((1,2,3,2))
print(hashset)
hashset = set('hello world')
print(hashset)
hashset = set([1,3,2])
print(hashset)

# set의 연산
#  데이터의 추가는 add(데이터), update[데이터 나열])
#  데이터의 복사는 copy()
#  데이터의 젂체 제거는 clear()
#  데이터의 한 개 제거는 discard(데이터) – 없으면 그냥 통과
#  데이터의 한 개 제거는 remove(데이터) – 없으면 예외
#  Pop(): 1개 제거

# set의 집합 연산
#  union(다른 set), intersection(다른 set), difference(다른 set),
# symmetric_difference(다른set)의 메서드가 제공되는데 결과를 리턴한다.
#  update(), intersection_update(), difference_update(),
#   symmetric_difference_update()는 호출하는 객체의 데이터를 변경

# 포함 관계 연산자
#  데이터 in set : 앞의 요소가 포함되어 있는지 리턴
#  데이터 not in set: 앞의 요소가 포함되어 있지 않은지 리턴
#  isupperset(다른 set): 다른 set을 포함하고 있는지 여부 리턴
#  issubset(다른 set): 다른 set의 서브셋인지 여부 리턴
#  isdisjoint(다른 set): 교집합이 공집합인지 여부 리턴

# set(집합) 자료형의 특징
# 1. 중복 데이터를 저장할 수 없다.
# 2. 순차적인 자료구조가 아니다.
#    순서있는 입.출력을 처리 할 수 없다.
s1 = set([1,2,3,4])
print(type(s1))         # <class 'set'>
print(s1)               # {1, 2, 3, 4}

s2 = set('Hello')
print(type(s2))         # <class 'set'>
print(s2)               # {'H', 'e', 'l', 'o'}

# set을 list로 변환 : list()함수
s3 = set([1,2,3])
print(type(s3))         # <class 'set'>
# print(s3[1])          # 오류 발생 : 인덱싱을 할 수 없다.

# s3 집합을 list로 변환
list1 = list(s3)
print(type(list1))      # <class 'list'>
print(list1)            # [1, 2, 3]
print(list1[0])         # 1
print(list1[1])         # 2
print(list1[2])         # 3

# set을 tuple로 변환 : tuple()
t1 = tuple(s3)
print(type(t1))         # <class 'tuple'>
print(t1)               # (1, 2, 3)
print(t1[0])            # 1
print(t1[1])            # 2
print(t1[2])            # 3

# 교집합 : &, intersection()
# 합집합 : |, union()
# 차집합 : -, difference()
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 1. 교집합
print(s1 & s2)                      # {4, 5, 6}
print(s1.intersection(s2))          # {4, 5, 6}
# 2. 합집합
print(s1 | s2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 3. 차집합
print(s1 - s2)                      # {1, 2, 3}
print(s1.difference(s2))            # {1, 2, 3}
print(s2 - s1)                      # {8, 9, 7}
print(s2.difference(s1))            # {8, 9, 7}


# 집합 자료형 관련 함수들
# 1. add() :  집합에 1개의 값을 추가
s1 = set([1,2,3])
s1.add(3)               # 중복된 값을 저장할 수 없다.
s1.add(4)
# s1.add([4,5])         # 오류발생
print(s1)               # {1, 2, 3, 4}

# 2. update() : 여러개의 값을 추가
s2 = set([1,2,3])
s2.update([4,5,6])
print(s2)               # {1, 2, 3, 4, 5, 6}

# 3. remove() : 특정 원소 삭제
s3 = set([1,2,3])
s3.remove(2)            # 원소 2 삭제
s3.remove(3)            # 원소 3 삭제
print(s3)               # {1}

#딕셔너리.
# dict
#  Key와 Value를 쌍으로 저장하는 자료형
#  {키:데이터, 키:값....}로 생성가능
#  Key의 순서는 없으며 Key의 값은 중복될 수 없다.
#  Key의 자료형에 제한은 없지만 거의 str
#  Key 값에 해당하는 데이터를 가져올 때는 디셔너리[키]
#  디셔너리[키] = 데이터 를 이용하면 키의 데이터가 없으면 삽입이 되고 있으면 수정
#  없는 키의 값을 호출하면 에러
#  len(디셔너리)는 키의 개수
#  del 디셔너리[키]는 키의 데이터 삭제
member = {'baseball':9, 'soccer':11,"volleyball":6}
print(member)
print(member['baseball'])
print(member['basketball'])

#  생성하는 다른 방법은 dict(키=데이터, 키=데이터)로 가능
#  키의 리스트나 값의 리스트가 존재하는 경우
#         dict(zip(키의 리스트, 값의 리스트))로 생성가능
#  사전을 for에 사용하면 키의 모든 리스트가 순서대로 대입됩니다.
keys = ['one', 'two', 'three']
values = (1,2,3)
dic = dict(zip(keys, values))
for key in dic:
    print(key,":", dic[key])

#  keys(): 키에 대한 모든 데이터를 리턴
#  values(): 값에 대한 모든 데이터를 리턴
#  items(): 모든 데이터 리턴
#  list()의 매개변수로 위 3개의 메서드 리턴값을 넣으면 list로 변홖
#  clear(): 모두 삭제
#  copy(): 복사
#  get(key [,x]): 값이 존재하면 값을 리턴하고 없으면 x 리턴
#  setdefault(key [,x]):get 과 동일하지맊 값이 존재하지 않으면 x로 설정
#  update(디셔너리): 디셔너리의 모든 항목을 설정
#  popitem(): 마지막 하나의 튜플을 반홖하고 제거
#  pop(key): key에 해당하는 데이터를 반홖하고 제거

# OrderedDict
#  키의 순서를 유지하는 디셔너리를 만들고자 할 때는 collections 모듈의 OrderedDict를 사용
#  dict와 동일하게 동작하지맊 데이터가 추가된 순서를 기억해서 데이터를 순서대로 처리할 수
# 있도록 해주는 자료형
from collections import OrderedDict
keys = ['one', 'two', 'three']
values = (1,2,3)
dic = dict(zip(keys, values))
for key in dic:
    print(key,":", dic[key])
print("=====================")
dic = OrderedDict(zip(keys, values))
for key in dic:
    print(key,":", dic[key])

# 딕셔너리(dictionary)
# 1. 딕셔너리에 데이터를 저장할 때는 key와 value(=data) 를 같이 저장한다.
#    ex) { '국어' : 80, '영어' : 90 }
# 2. 딕셔너리는 순차적인 자료구조가 아니다.
# 3. 딕셔너리의 데이터를 구해올때는 key를 이용해서 데이터를 구해온다.
# 4. 1개의 딕셔너리에 key는 1개만 사용가능하다.
#    1개의 딕셔너리에 동일한 이름을 가진 key가 여러개 존재하면, 가장 마지막 key만
#    사용이 가능하다.

# { '아기이름' : 출생아수 }
names = {'Mary':10999, 'Sams':2111,'Aimy':9778,'Tom':20245,'Michale':27115,
         'Bob':5887,'Kelly':7855,'Mary':100}
print(type(names))              # <class 'dict'>
print(names)
print(names['Aimy'])            # 9778
print(names['Tom'])             # 20245
print(names['Mary'])            # 100

# 딕셔너리에서 지원되는 함수
# { '아기이름' : 출생아수 }
names = {'Mary':10999, 'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}

# 1. keys() : 딕셔너리의 key를 구해주는 함수
for k in names.keys():
    print('Key:%s\t Value:%d'%(k, names[k]))
# 2. values() : 딕셔너리의 value 값을 구해오는 함수
vals = names.values()
print(type(vals))               # 'dict_values'
print(vals)                     # dict_values([10999, 2111, 9778, 20245, 27115, 5887, 7855])
vals_list = list(vals)          # 출생아수(value)를 리스트로 만들어 준다.
print(type(vals_list))          # 'list'
print(vals_list)                # [10999, 2111, 9778, 20245, 27115, 5887, 7855]
# 총 출생아수
result = sum(vals_list)
print('총 출생아수:%d'%result)   # 총 출생아수:83990

# 3. items() : 딕셔너리의 key와 value값을 모두 구해오는 함수
for item in names.items():
    print(item)                 # ('Mary', 10999)
                                # ('Sams', 2111)
                                #  ....
for k, v in names.items():
    print(k,':',v)              # Mary : 10999
                                # Sams : 2111
                                #  ....

# 딕셔너리의 값 수정
# { '아기이름' : 출생아수 }
names = {'Mary':10999, 'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}
print(names)
print(names['Aimy'])            # 9778
print(names.get('Aimy'))        # 9778

# 딕셔너리 값 수정 : Aimy 의 값을 9778에서 10000으로 수정
names['Aimy'] = 10000
print(names)
print(names['Aimy'])            # 10000

# 딕셔너리의 특정 데이터 삭제 : del 명령
# 딕셔너리의 모든 원소를 삭제 : clear()함수
# { '아기이름' : 출생아수 }
names = {'Mary':10999, 'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}

# 딕셔너리 names 중에서 key가 'Sams'인 원소 삭제
del names['Sams']
del names['Bob']
# 삭제 확인
print(names)
# 딕셔너리의 모든 원소를 삭제해서 비어있는 딕셔너리가 된다.
names.clear()
# 삭제 확인
print(names)            # 비어있는 딕셔너리 : {}

# 멤버연산자 in 을 이용하여 특정 값이 딕셔너리의 key로 존재하는지 확인하는 프로그램 작성
# { '아기이름' : 출생아수 }
names = {'Mary':10999, 'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}

k = input('아기이름을 입력하세요?')
if k in names:   # 키보드로 입력한 이름이 딕셔너리에 있으면 True 리턴
    print('이름이 %s인 출생아수는 %d명 입니다.'%(k, names[k]))
else:
    print('자료에 %s인 이름이 존재하지 않습니다.'%k)

# 딕셔너리의 정렬 : sorted() 함수
# 딕셔너리의 key(아기이름)를 이용해서 오름차순, 내림차순 정렬?
# 딕셔너리의 values(출생아수)를 이용해서 오름차순, 내림차순 정렬?

# { '아기이름' : 출생아수 }
names = {'Mary':10999, 'Sams':2111,'Aimy':9778,'Tom':20245,
         'Michale':27115,'Bob':5887,'Kelly':7855}
print(names)            # {'Mary': 10999, 'Sams': 2111, 'Aimy': 9778, 'Tom': 20245, 'Michale': 27115, 'Bob': 5887, 'Kelly': 7855}

#------------------------------------------------------------------------------
# 딕셔너리의 key를 return 함수 정의
def f1(x):
    return x[0]
# 딕셔너리의 value를 return 함수 정의
def f2(x):
    return x[1]

#1. 딕셔너리의 key를 이용해서 오름차순 정렬
result1 = sorted(names)             # 딕셔너리의 key로 오름차순 정렬
print('result1:', result1)          # ['Aimy', 'Bob', 'Kelly', 'Mary', 'Michale', 'Sams', 'Tom']
result2 = sorted(names.items(), key=f1)
print('result2:', result2)          # [('Aimy', 9778), ('Bob', 5887), ('Kelly', 7855), ('Mary', 10999)
#2. 딕셔너리의 key를 이용해서 내림차순 정렬
result3 = sorted(names.items(), key=f1, reverse=True)
print('result3:', result3)          # [('Tom', 20245), ('Sams', 2111), ('Michale', 27115), ('Mary', 10999)
#3. 딕셔너리의 value를 이용해서 오름차순 정렬
result4 = sorted(names.items(), key=f2)
print('result4:', result4)          # [('Sams', 2111), ('Bob', 5887), ('Kelly', 7855), ('Aimy', 9778)
#4. 딕셔너리의 value를 이용해서 내림차순 정렬
result5 = sorted(names.items(), key=f2, reverse=True)
print('result5:', result5)         # [('Michale', 27115), ('Tom', 20245), ('Mary', 10999), ('Aimy', 9778)


# <<강의 복습 3. 끝>>
# pywork10.py end
