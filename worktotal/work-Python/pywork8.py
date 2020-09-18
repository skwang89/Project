# 변수: 메모리사에 데이터를 저장하기 위한 기억공간의 이름
# 변수 만드는 형식:    변수명 =  값(데이터)

# 정수형 변수
i = 10
print('i=', i)
print(type(i))              # <class 'int'>

# 실수형 변수
r = 3.14
print('r=', r)
print(type(r))              # <class 'float'>

# 복소수형 변수
c = 3 + 5j
print('c=', c)
print(type(c))              # <class 'complex'>

# 논리형 변수
b1 = True                   # 첫 캐릭터를 대문자로 작성
b2 = False
print('b1=', b1)
print('b2=', b2)
print(type(b1))             # <class 'bool'>
print(type(b2))

# 문자형 변수
s1 = "파이썬"
s2 = 'python'
print('s1=', s1)
print('s2=', s2)
print(type(s1))                 # <class 'str'>
print(type(s2))

# 리스트(list)
list = ['빨강','주황','노랑','초록','파랑','남색','보라']
print(list[0])                  # 빨강
list[0] = 'red'                 # 빨강을 red 로 수정
print('list=', list)
print(type(list))               # <class 'list'>

# 튜플(tuple)
t = ('red','orange','yellow','green','blue','navy','purple')
print(t[0])                     # red
# t[0] = '빨강'                 # tuple은 원소의 값을 수정할 수 없다.
print('t=', t)
print(type(t))                  # <class 'tuple'>

# 집합(set)
s = set([1,2,3])
print('s=', s)
print(type(s))                  # <class 'set'>

# 딕셔너리(dictionary) :  { 'key' : 'value' }
d = {'네이버' : 'http://www.naver.com',
     '구글' : 'http://www.google.com',
     '애플' : 'http://www.apple.com'}
print('d=', d)
print(type(d))                  # <class 'dict'>

# 연산자.
# 대입 연산자: =
a = 10
x = y = z = 0
c, d = 10, 20
c, d = d, c     # 값 교환
c
d

# 산술 연산자
# +, -, *, /(몫:실수형), //(몫:정수형), %(나머지), **(거듭제곱)
a = 10; b = 3
result1 = a + b                     # 13
result2 = a - b                     # 7
result3 = a * b                     # 30
result4 = a / b                     # 몫 : 실수형 (3.3333333333333335)
result5 = a // b                    # 몫 : 정수형 (3)
result6 = a % b                     # 나머지 : 1
result7 = a ** b                    # 거듭제곱(10의 3승) : 1000

# 비교 연산자: ==, !=, >, >=, <, <=
# 비교 연산자의 결과가 참이면 True, 거짓이면 False를 리턴한다.
x = 10; y = 20
str1 = 'abc'
str2 = 'python'

print(x == y)                   # False
print(x != y)                   # True
print(x > y)                    # False
print(x >= y)                   # False
print(x < y)                    # True
print(x <= y)                   # True

print(str1 == str2)             # False
print(str2 == 'python')        # True
print(str1 < str2)              # True
# 문자열의 크기 비교는 사전순서로 비교한다.
# abc가 python 보다 사전 순서가 앞이므로 결과는 True가 출력된다.

# 논리 연산자 : and, or, not

#      논리 연산자        의미
#-------------------------------------------------------
#   A    and    B        A와 B가 모두 참인 경우에만 True
#   A    or     B        A와 B중 하나 이상이 참이면 True
#   not  A               A 논리값의 반대

b1=True; b2=False; b3=True; b4=False

print(b1 and b2)                # False
print(b1 and b3)                # True
print(b2 or b3)                 # True
print(b2 or b4)                 # False
print(not b1)                   # False
print(not b2)                   # True

# 논리 연산자
# 5과목의 점수를 입력 받아서 합격, 불합격을 판별하는 프로그램을 작성 하세요?
# 단, 과목당 과락은 40점이고, 평균 60점 이상이면 합격

# input(): 키보드로 입력을 받는 경우에 사용하는 함수
# int(): 문자를 정수형으로 형변환 해주는 함수 :  '50'  -->  50
# n = input('점수를 입력 하세요?')
# print(n)
# print(type(n))          # <class 'str'>
# n = int(n)              # 문자를 정수형으로 변환
# print(type(n))          # <class 'int'>

n1 = int(input('점수1을 입력하세요?'))
n2 = int(input('점수2를 입력하세요?'))
n3 = int(input('점수3을 입력하세요?'))
n4 = int(input('점수4를 입력하세요?'))
n5 = int(input('점수5를 입력하세요?'))

avg = (n1+n2+n3+n4+n5) / 5
print('avg=', avg)

if n1>=40 and n2>=40 and n3>=40 and n4>=40 and n5>=40 and avg>=60:
    print('합격')
else:
        print('불합격')

# 복합 대입 연산자 : +=, -=, */, /=, //=, %=
a = 0                   # 초기값

a += 1                  # a = a + 1
print('a=', a)          # a = 1

a -= 5                  # a = a - 5
print('a=', a)          # a = -4

a *= 2                  # a = a * 2
print('a=', a)          # a = -8

a /= 4                  # a = a / 4
print('a=', a)          # a = -2.0

# 멤버 연산자 : in, not in
# in: 해당 데이터가 컬렉션에 포함되어 있으면 True, 포함되어 있지 않으면 False를 리턴
# not in: 해당 데이터가 컬렉션에 포함되어 있지 않으면 True를 리턴
list = [10, 20, 30, 40]

result1 = 30 in list
result2 = 60 in list
print('result1=', result1)          # True
print('resul2=', result2)           # False

str = 'abcde'
result3 = 'c' in str
result4 = 'k' in str
print('resul3=', result3)           # True
print('resul4=', result4)           # False

# 입력받은 문자열에 'a'가 있는지 판별하기
msg = input('임의의 문장을 입력하세요?')
if 'a' in msg:
    print('당신이 입력한 문장에는 a가 있습니다.')
else:
    print('당신이 입력한 문장에는 a가 없습니다.')

# 내장 함수: 별도의 모듈의 추가없이 기본적으로 제공되는 함수
# : https://docs.python.org/3.7/library/functions.html

# 최대값: max()
print(max(10, 20))                      # 20
print(max(10, 20, 30, 40, 50))          # 50
print(max([10, 20, 30, 40, 50]))        # 50
print(max('hello world'))               # w

# 최소값: min()
print(min(10,20,30,40,50))              # 10
print(min([10,20,30]))                  # 10

# range() 함수
# range(초기값, 최종값, 증감값) : 초기값 ~ 최종값-1 까지 증감
# range(초기값, 최종값) : 초기값 ~ 최종값-1 까지
# range(최종값) : 0 ~ 최종값-1 까지
print(range(10))            # range(0, 10)\

print(list(range(10)))      # 0 ~ 9   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10)))    # 1 ~ 9   [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,2)))  # [1, 3, 5, 7, 9]

for i in range(1, 11):      # 1 ~ 10
    print(i)

for i in range(10):         # 0 ~ 9
    print(i)

for i in range(10,1,-1):   # 10 ~ 2까지 1씩 감소
    print(i)

# 내장 함수: input(), int(), type()
# input(): 키보드로 입력을 받는 경우에 사용하는 내장함수
# int(): 문자형을 정수형으로 변환해주는 내장 함수
# type(): 변수에 저장된 데이터의 자료형을 구해주는 내장함수
name = input('이름을 입력하세요?')
age = int(input('나이를 입력하세요?'))
print(type(name))               # <class 'str'>
print(type(age))                # <class 'int'>

if age >= 20 :
    print('성인 입니다.')
else:
    print('미성년 입니다.')

# 내장 함수: print()
print(1, 2)
print(3, 4)

# 한줄에 2개 이상의 명령을 사용할 경우에는 세미콜론(;)을 붙여야 한다.
print(1, 2); print(3, 4)

# 줄을 바꾸지 않으려면, print()함수 안에 end=''를 추가
print(1,2, end=' ');  print(3,4)            # 1 2 3 4

# 값 사이의 간격은 sep='\t' 를 추가
print(1,2,3,4,5)                            # 1 2 3 4 5
print(1,2,3,4,5, sep='  ')                  # 1  2  3  4  5
print(1,2,3,4,5, sep='\t')                  # 1	2	3	4	5
print(1,2,3,4,5, sep='\t\t')                # 1		2		3		4		5

# 내장 함수: format()

# format(데이터, 서식형식)
print(4)
print(format(4, '10d'))          # 정수를 출력하는 10자리
print(format(4.3, '10.3f'))      # 실수를 출력하는 전체 10자리, 소숫점 이하 3자리
print(format(42.195678, '.3f'))  # 소숫점 3자리까지 출력   42.196
print(format('안녕하세요', 's'))

# {숫자}와 format()함수를 이용한 데이터 매핑
print('{0} is {1}'.format('Python','fun'))    # Python is fun
print('{} is {}'.format('Python','fun'))      # Python is fun
print('{1} is {0}'.format('Python','fun'))    # fun is Python

# 키보드로 입력한 문자를 format()함수로 출력
name = input('이름을 입력하세요?')
job = input('직업을 입력하세요?')

print('{0} is a {1}'.format(name, job))         # 홍길동 is a 프로그래머
print('{} is a {}'.format(name, job))           # 홍길동 is a 프로그래머
print('{1} is a {0}'.format(name, job))         # 프로그래머 is a 홍길동
print('{j} is a {n}'.format(n=name, j=job))     # 프로그래머 is a 홍길동


