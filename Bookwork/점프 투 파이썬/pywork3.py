# pywork3.py start
# <<교재 4장 시작>>


# <4-1. 함수>
# 파이썬 함수의 구조
# def 함수명(매개변수):
#     <수행할 문장1>
#     <수행할 문장2>
#     ...
# 예.
def add(a, b):          # a, b는 매개변수
    return a + b        # 3, 4는 인수
a = 3
b = 4
c = add(a, b)
print(c)

# 입력값과 결괏값에 따른 함수의 형태
# 1. 일반적인 함수: 입력값과 결과값이 있는 함수
# 결괏값을 받을 변수 = 함수이름(입력인수1, 입력인수2, ...)
# def 함수이름(매개변수):
#     <수행할 문장>
#     ...
#     return 결과값
def add(a, b):
    result = a + b
    return result
a = add(3, 4)
print(a)


# 2. 입력값이 없는 함수: 입력값이 없고 결괏값만 있는 함수
# 결괏값을 받을 변수 = 함수이름()
def say():
    return 'Hi'
a = say()
print(a)

# 3. 결과값이 없는 함수: return값이 없다
# 함수이름(입력인수1, 입력인수2, ...)
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
a = add(3, 4)
a = add(3,4)
print(a)            # none : return 명령어로 돌려받은 값이 없기 때문

# 4. 입력값도 결괏값도 없는 함수
# 함수이름()
def say():
    print('Hi')
say()

# 매개변수 지정하여 호출하기
def add(a, b):
    return a+b
result = add(a=3, b=7)  # a에 3, b에 7을 전달
print(result)       # 10
result = add(b=5, a=3)  # b에 5, a에 3을 전달: 순서 상관없음
print(result)       # 8

# 입력값이 몇 개가 될지 모를 때
# def 함수이름(*매개변수):
#     <수행할 문장>
#     ...

# 여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
# *args:이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어 줌
# *args는 임의로 정한 변수 이름으로 아무 이름이나 써도 된다.
# 예) *pey, *python
# ※ args는 매개변수를 뜻하는 영어 단어 arguments의 약자이며
# 관례적으로 자주 사용한다.

result = add_many(1,2,3)
print(result)           # 6
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)           # 55

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result *i
    return result
result = add_mul('add', 1,2,3,4,5)
print(result)           # 15
result = add_mul('mul', 1,2,3,4,5)
print(result)           # 120

# 키워드 파라미터 kwargs: 매개변수 앞에 별 두 개(**)를 붙인다.
# **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는
# 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)                   # {'a': 1}
print_kwargs(name='foo', age=3)     # {'name': 'foo', 'age': 3}

# 함수의 결괏값은 언제나 하나이다
def add_and_nul(a,b):
    return a+b, a*b
result = add_and_nul(3,4)
result          # (7, 12)
# 튜플값 하나인 (a+b, a*b)로 돌려준다.

# 하나의 튜플 값을 2개의 결괏값처럼 받고 싶을 때
result1, result2 = add_and_nul(3,4)
result1         # 7
result2         # 12

# return의 또 다른 쓰임새: 특별한 상황일 때 함수를 빠져나가고 싶다면
# return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)
say_nick('야호')          # 나의 별명은 야호 입니다.
say_nick('바보')          # (출려되지 않고 함수를 빠져나옴)

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
# man=True -> 매개변수에 미리 값을 넣어 줌
# 함수의 매개변수에 들어갈 값이 항상 변하는 것이 아닐 경우에는
# 이렇게 함수의 초깃값을 미리 설정해 두면 유용하다.
say_myself('김파이', 32)
say_myself('김파이', True)
say_myself("박응선", 27, False)
# 주의:초깃값을 설정해 놓은 매개변수 뒤에 초깃값을 설정해 놓지 않은 매개변수는
# 사용할 수 없다

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)
# 매개변수 a는 함수 안에서만 사용하는 변수이지 함수 밖의 변수 a가 아니다

def vartest(a):
    a = a + 1
vartest(3)      # 4
print(a)        # 오류발생: a변수를 찾을 수 없음

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)                # 2

# 2. global 명령어 사용하기
a = 1
def vartest():
    global a    # 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻
    a = a+1
vartest()
print(a)                # 2

# lambda: 함수를 생성할 때 사용하는 예약어
# 보통 함수를 한줄로 간결하게 만들 때 사용한다.
add = lambda a, b: a+b
result = add(3,4)
print(result)           # 7
def add(a, b):
    return a+b
result = add(3, 4)
print(result)           # 7

# <4-2 사용장 입력과 출력>
# 사용자 입력: 사용자가 입력한 값을 변수에 대입하고 싶을 때
# input의 사용
a = input()
# Life is too short, you need python
a
# 'Life is too short, you need python'

# 프롬프트를 띄워서 사용자 입력 받기
# input()의 괄호 안에 질문을 입력하여 프롬프트를 띄워주면 된다.
number = input("숫자를 입력하세요:")
# 3
print(number)
# 3

# print 자세히 알기
a = 123
print(a)        # 123
a = 'Python'
print(a)        # Python
a = [1,2,3]
print(a)        # [1, 2, 3]

# 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다.
print("life" "is" "too short")
# lifeistoo short
print("life"+"is"+"too short")
# lifeistoo short

# 문자열 띄어쓰기는 콤마로 한다
print("life", "is", "too short")
# life is too short

# 한 줄에 결괏값 출력하기: 매개변수 end를 사용
for i in range(10):
    print(i, end=" ")
# 0 1 2 3 4 5 6 7 8 9

# <4-3 파일 읽고 쓰기>
# 파일 생성하기
f = open("C:\workspace-total\pythonworkspace\점프 투 파이썬\Bookwork\점프 투 파이썬/새파일.txt", 'w')
f.close()
# 파일열기모드	    설명
# r	            읽기모드 - 파일을 읽기만 할 때 사용
# w	            쓰기모드 - 파일에 내용을 쓸 때 사용
# a	            추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
# 파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우
# 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면
# 새로운 파일이 생성된다. 위 예에서는 디렉터리에 파일이 없는 상태에서
# 새파일.txt를 쓰기 모드인 'w'로 열었기 때문에
# 새파일.txt라는 이름의 새로운 파일이 현재 디렉터리에 생성되는 것이다.
# f.close()는 열려 있는 파일 객체를 닫아 주는 역할을 한다.
# close() 함수를 이용해서 직접 닫아 주는 것이 좋다.

# 파일을 쓰기 모드로 열어 출력값 적기
f = open("C:\workspace-total\pythonworkspace\점프 투 파이썬\Bookwork\점프 투 파이썬/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
# readline() 함수 이용하기
f = open("C:/doit/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()
# 파일.txt의 가장 첫 번째 줄이 화면에 출력됨

f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
# 파일.txt의 모든 줄이 화면에 출력됨
# 사용자의 입력을 받아서 그 내용을 출력하는 경우
while 1:
    data = input()
    if not data: break
    print(data)


# readlines 함수 사용하기
f = open("C:/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
# 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
# f.readlines()에서 f.readline()과 차이 유의

# read 함수 사용하기
f = open("C:/새파일.txt", 'r')
data = f.read()
print(data)
f.close()
# 파일의 내용 전체를 문자열로 돌려준다.

# 파일에 새로운 내용 추가하기: 파일 추가 모드('a')
f = open("C:/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
# 새파일.txt 파일을 추가 모드('a')로 열고
# write를 사용해서 결괏값을 기존 파일에 추가해 적는 예

# with문과 함께 사용하기: 파일을 열고 닫는 것을 자동으로 처리
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
# with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close된다
# sys 모듈로 매개변수 주기
# 명령 프롬프트 명령어 [인수1 인수2 ...]
# 파이썬에서는 sys 모듈을 사용하여 매개변수를 직접 줄 수있다.
# sys 모듈을 사용하려면 아래 예의 import sys처럼 import 명령어를 사용해야 한다.
import sys

args = sys.argv[1:]
for i in args:
    print(i)

# C:\>python sys1.py aaa bbb ccc
# aaa
# bbb
# ccc

import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
# 문자열 관련 함수인 upper()를 사용하여 명령 행에 입력된 소문자를
# 대문자로 바꾸어 주는 간단한 프로그램이다.
# 명령프롬프트 창에서 다음과 같이 입력해 보자.
#
# ※ sys2.py 파일이 C:\doit 디렉터리 안에 있어야만 한다.

# LIFE IS TOO SHORT, YOU NEED PYTHON

# <연습문제>
# Q1
# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
def odd_even(a):
    if a%2==0:
        return '짝수'
    else:
        return '홀수'
odd_even(4)
# 짝수
odd_even(11)
# 홀수

#람다와 조건부 표현식 사용한 해답
odd_even = lambda a: "짝수" if a%2==0 else "홀수"
odd_even(14)
# 짝수

# Q2
# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
# ※ 평균 값을 구할 때 len 함수를 사용해 보자.
def avg(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)
avg(1,2)            # 1.5
avg(1,2,3,4,5)      # 3.0

# Q3
# 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")
total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
# 이 프로그램을 수행해 보자.
# 첫번째 숫자를 입력하세요:3
# 두번째 숫자를 입력하세요:6
# 두 수의 합은 36 입니다
# 3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의
# 오류를 수정해 보자.
# ※ int 함수를 사용해 보자.
total = int(input1) + int(input2)
# 입력은 항상 문자열 이므로 숫자로 바꾸어 주어야 한다.

# Q4
# 다음 중 출력 결과가 다른 것 한 개를 골라 보자.
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))
# 1,2,4: youneedpython
# 3: you need python 콤마가 있는경우 공백이 삽입되어 더해진다

# Q5
# 다음은 "test.txt"라는 파일에 "Life is too short"
# 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
f1 = open("test.txt", 'w')
f1.write("Life is too short")
# f1.close()
f2 = open("test.txt", 'r')
print(f2.read())
# f2.close()
# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다.
# 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

# 일을 닫지 않은 상태에서 다시 열면 파일에 저장한 데이터를 읽을 수 없다.
# 따라서 열린 파일 객체를 close로 닫아준 후 다시 열어서 파일의 내용을 읽어야 한다.

# Q6
# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
# (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고
# 새로 입력한 내용을 추가해야 한다.)
user = input('입력')
f1 = open("test.txt", 'a')
f1 = write(user)
# f1 = write("\n")
f1.close()

# Q7
# 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중
# "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
#
# Life is too short
# you need java
# ※ replace 함수를 사용해 보자.
f = open('text.txt', 'r')
get = f.read()
f.close()
get = get.replace('java', 'python')
f = open('test.txt', 'w')
f.write(get)
f.close()


# <<교재 4장 끝>>
# pywork3.py end
