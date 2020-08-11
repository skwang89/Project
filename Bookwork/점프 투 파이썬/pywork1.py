# pywork1.py start
# <<교재 2장 시작>>


# <2-1. 숫자형>
# 정수형
a = 123
a= -178
a = 0

# 실수형
# 소수점 표현 방식
a = 1.2
a = -3.45

# 지수 표현 방식
a = 4.24E10
b = 4.24e+10
# 42400000000.0
# 42400000000.0

# 8진수: 숫자'0' 알파벳'o'
a = 0o177

# 16진수: 숫자'0' 알파벳'x'
a = 0x8ff

# 사칙연산: +, -, /, *
a = 3
b = 4
print(a+b)      # 7
print(a-b)      # -1
print(a/b)      # 0.75
print(a*b)      #12

# x의 y제곱을 나타내는 ** 연산자
print(a**b)     # 81

# 나눗셈 후 나머지를 반환하는 % 연산자
print(a%b)      # 3

# 나눗셈 후 몫을 반환하는 // 연산자
print(a//b)     # 0

# <2-2. 문자열 자료형>
# 1. 큰따옴표(")로 양쪽 둘러싸기
print("Hello World")
# 2. 작은따옴표(')로 양쪽 둘러싸기
print('Python is fun')
# 3. 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""")
# 4. 작은따옴표 3개를 연속(''')으로 써서 양쪽 둘러싸기
print('''Life is too short, You need python''')

# 1. 문자열에 작은따옴표 (') 포함시키기
print("Python's favorite food is perl")
string = "Python's favorite food is perl"
print(string)
# Python's favorite food is perl

# 2. 문자열에 큰따옴표 (") 포함시키기
print('"Python is very easy." he says.')
# "Python is very easy." he says.

# 3. 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
string2 = 'Python\'s favorite food is perl'
string3 = "\"Python is very easy.\" he says."
print(string2)      #Python's favorite food is perl
print(string3)      #"Python is very easy." he says.

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
string = "Life is too short\nYou need python"
print(string)
# Life is too short
# You need python

# 2. 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 사용하기
string='''
... Life is too short
... You need python
... '''
print(string)
# ... Life is too short
# ... You need python
# ...

# 이스케이프 코드: 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자 조합"
# 코드	설명
# \n	문자열 안에서 줄을 바꿀 때 사용
# \t	문자열 사이에 탭 간격을 줄 때 사용
# \\	문자 \를 그대로 표현할 때 사용
# \'	작은따옴표(')를 그대로 표현할 때 사용
# \"	큰따옴표(")를 그대로 표현할 때 사용
# \r	캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f	폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a	벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
# \b	백 스페이스
# \000	널 문자

# 문자열 연산하기
# 문자열 더해서 연결하기
a = "Python"
b = " is fun!"
print(a+b)      # Python is fun!

# 문자열 곱하기
print(a*2)      # PythonPython

# 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)
# ==================================================
# My Program
# ==================================================

# 문자열 길이 구하기
a = 'Life is too short'
print(len(a))       # 17

# 문자열 인덱싱("가리킨다")과 슬라이싱("잘라낸다")
a = "Life is too short, You need Python"
# Life is too short, You need Python
# 0         1         2         3
# 0123456789012345678901234567890123
print(a[3])     # e 파이썬은 0부터 숫자를 센다.

# 문자열 인덱싱 활용하기
print(a[-1])    # n 뒤에서부터 세어 첫 번째가 되는 문자
print(a[-0])    # L a[-0]은 a[0]과 똑같은 값을 보여 준다.

# 문자열 슬라이싱
a = "Life is too short, You need Python"

# 단순 방법
b = a[0] + a[1] + a[2] + a[3]
print(b)        # Life
# a[0:4]  =>  0 <= a < 3
print(a[0:4])   # Life
# 공백 문자 역시 문자와 동일하게 취급
print(a[0:5])   # 'Life '
# a[시작 번호:끝 번호] 끝번호 부분을 생략시 시작 번호부터 그 문자열의 끝까지
print(a[19:])   # You need Python
# a[시작번호:끝번호-1] 시작번호 생략시 문자열의 처음부터 끝번호-1까지
print(a[:17])   # Life is too short
# a[시작번호:끝 번호] 시작 번호와 끝 번호를 생략시 문자열의 처음부터 끝까지
print(a[:])     # Life is too short, You need Python
# 마이너스(-) 기호를 사용할 수 있다.
print(a[19:-7]) # You need

# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

# 문자열 바꾸기
a = "Pithon"
# a[1] = 'y'      # 오류: 문자열 자료형은 그 요솟값을 변경할 수 없다.
print(a[:1] + 'y' + a[2:])

# 문자열 포매팅
# 1. 숫자 바로 대입
print("I eat %d apples." % 3)       # I eat 3 apples.

# 2. 문자열 바로 대입
print("I eat %s apples." % "five")  # I eat five apples.

# 3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)  # I eat 3 apples.

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
# I ate 10 apples. so I was sick for three days.

# 문자열 포맷 코드
# 코드	설명
# %s	문자열(String)
# %c	문자 1개(character)
# %d	정수(Integer)
# %f	부동소수(floating-point)
# %o	8진수
# %x	16진수
# %%	Literal % (문자 % 자체)

# %s 포맷 코드: 어떤 형태의 값이든 변환해 넣을 수 있다.
print("I have %s apples" % 3)       # I have 3 apples
print("rate is %s" % 3.234)         # rate is 3.234

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
# print('"Error is %d%." % 98')        # 에러발생
print('"Error is %d%%." % 98')         # "Error is %d%%." % 98

# 포맷 코드와 숫자 함께 사용하기
# 1. 정렬과 공백
print("%10s" % "hi")        # '        hi'
print("%-10sjane." % 'hi')  # 'hi        jane.'

# 2. 소수점 표현하기
print("%10.4f" % 3.42134234)    # '    3.4213'

# format 함수를 사용한 포매팅
# 숫자 바로 대입하기
print("I eat {0} apples".format(3))         # I eat 3 apples

# 문자열 바로 대입하기
print("I eat {0} apples".format("five"))    # I eat five apples

# 숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples".format(number))    # I eat 3 apples

# 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
# I ate 10 apples. so I was sick for three days.

# 이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
# I ate 10 apples. so I was sick for 3 days.

# 인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
# I ate 10 apples. so I was sick for 3 days.

# 왼쪽 정렬
print("{0:<10}".format("hi"))
# 'hi        '

# 오른쪽 정렬
print("{0:>10}".format("hi"))
# '        hi'

# 가운데 정렬
print("{0:^10}".format("hi"))
# '    hi    '

# 공백 채우기
print("{0:=^10}".format("hi"))
# ====hi====
print("{0:!<10}".format("hi"))
# hi!!!!!!!!

# 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
# '3.4213'
print("{0:10.4f}".format(y))
# '    3.4213'

# { 또는 } 문자 표현하기
print("{{ and }}".format())
# { and }

# f 문자열 포매팅: 파이썬 3.6 버전부터는 f 문자열 포매팅 기능을 사용할 수 있다.
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
# 나의 이름은 홍길동입니다. 나이는 30입니다.

# f 문자열 포매팅은 표현식을 지원한다: 변수와 +, -와 같은 수식을 함께 사용가능
print(f'나는 내년이면 {age+1}살이 된다.')
# 나는 내년이면 31살이 된다.

# 딕셔너리는 f 문자열 포매팅에서 다음과 같이 사용할 수 있다.
# 딕셔너리: Key와 Value라는 것을 한 쌍으로 갖는 자료형
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
# 나의 이름은 홍길동입니다. 나이는 30입니다.

# 정렬
print(f'{"hi":<10}') # 왼쪽 정렬)
# 'hi        '
print(f'{"hi":>10}') # 오른쪽 정렬)
# '        hi'
print(f'{"hi":^10}') # 가운데 정렬)
# '    hi    '

# 공백 채우기
print(f'{"hi":=^10}')  # 가운데 정렬하고 '=' 문자로 공백 채우기
# '====hi===='
print(f'{"hi":!<10}')  # 왼쪽 정렬하고 '!' 문자로 공백 채우기
# 'hi!!!!!!!!'

# 소수점 표현
y = 3.42134234
print(f'{y:0.4f}')  # 소수점 4자리까지만 표현
# '3.4213'
print(f'{y:10.4f}')  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
# '    3.4213'

# f 문자열에서 { } 문자를 표시
print(f'{{ and }}')
# { and }

# 문자열 관련 함수들
# 문자 개수 세기(count)
a = "hobby"
a.count('b')
# 2

# 위치 알려주기1(find)
a = "Python is the best choice"
a.find('b')
# 14
a.find('k')
# -1    # 존개하지 않음

# 위치 알려주기2(index)
a = "Life is too short"
a.index('t')
# 8
# a.index('k')      # 오류발생
# ValueError: substring not found

# 문자열 삽입(join):리스트나 튜플도 입력으로 사용할 수 있다
print(",".join('abcd'))
# a,b,c,d
print(",".join(['a', 'b', 'c', 'd']))
# a,b,c,d

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
a.upper()
# HI

# 대문자를 소문자로 바꾸기(lower)
a = "HI"
a.lower()
# hi

# 왼쪽 공백 지우기(lstrip)
a = " hi "
a.lstrip()
# 'hi '

# 오른쪽 공백 지우기(rstrip)
a= " hi "
a.rstrip()
# ' hi'

# 양쪽 공백 지우기(strip)
a = " hi "
a.strip()
# 'hi'

# 문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life", "Your leg")
# 'Your leg is too short'

# 문자열 나누기(split):아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준
a = "Life is too short"
a.split()
# 특정값을 줄때
b = "a:b:c:d"
b.split(':')
['a', 'b', 'c', 'd']

# <2-3. 리스트 자료형>
# 리스트: 리스트명 = [요소1, 요소2, 요소3, ...]
a = []      # 빈 리스트: a = list()로 생성할 수도 있다.
b = [1, 2, 3]                           # 숫자를 요숏값으로
c = ['Life', 'is', 'too', 'short']      # 문자열을 요솟값으로
d = [1, 2, 'Life', 'is']                # 숫자와 문자열
e = [1, 2, ['Life', 'is']]              # 리스트 자체를 요숏값으로

# 리스트의 인덱싱과 슬라이싱
# 리스트의 인덱싱
a = [1, 2, 3]
a               # [1, 2, 3]
a[0]            # 1
a[0] + a[2]     # 4
a[-1]           # 3

a = [1, 2, 3, ['a', 'b', 'c']]
a[0]            # 1
a[-1]           # ['a', 'b', 'c']
a[3]            # ['a', 'b', 'c']
a[-1][0]        # 'a'   4번째 요소 '리스트'의 처음 값 'a'
a[-1][1]        # 'b'
a[-1][2]        # 'c'

# 삼중 리스트에서 인덱싱하기
a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][2][0]      #'Life'

# 리스트의 슬라이싱: 문자열 슬라이싱과 동일
a = [1, 2, 3, 4, 5]
a[0:2]      # [1, 2]

a = "12345"
a[0:2]      # '12'

b = a[:2]
c = a[2:]
b       # [1, 2]
c       # [3, 4, 5]

# 중첩된 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
a[2:5]      # [3, ['a', 'b', 'c'], 4]
a[3][:2]    # ['a', 'b']

# 리스트 연산하기
# 리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
a + b           # [1, 2, 3, 4, 5, 6]

# 리스트 반복하기(*)
a = [1, 2, 3]
a * 3           # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 길이구하기: len() 함수 - 문자열, 리스트, 튜플, 디셔너리에서 사용
a = [1, 2, 3]
len(a)          # 3

# 초보자가 범하기 쉬운 리스트 연산 오류
a = [1, 2, 3]
# a[2] + "hi"
# 오류:TypeError: unsupported operand type(s) for +: 'int' and 'str'
# str() 함수: 문자열 형태로 바꾸어 줌
str(a[2]) + "hi"        # '3hi'

# 리스트의 수정과 삭제
# 리스트에서 값 수정하기
a = [1, 2, 3]
a[2] = 4
a       # [1, 2, 4]
# del 함수 사용해 리스트 요소 삭제하기
del a[1]
a       # [1, 4]
# del 함수는 모든 자료형에서 사용 가능
a = [1, 2, 3, 4, 5]
del a[2:]
a
# [1, 2]

# 리스트 관련 함수들
# 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)
a       # [1, 2, 3, 4]
a.append([5,6])
a       # [1, 2, 3, 4, [5, 6]]

# 리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort()
a       # [1, 2, 3, 4]
a = ['a', 'c', 'b']
a.sort()
a       # ['a', 'b', 'c']

# 리스트 뒤집기(reverse): 리스트 그대로 뒤집는다 (정렬 x)
a = ['a', 'c', 'b']
a.reverse()
a       # ['b', 'c', 'a']

# 위치 반환(index)
# index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다
a = [1, 2, 3]
a.index(3)      # 2
a.index(1)      # 0

a.index(0)      # 오류발생: ValueError: 0 is not in list

# 리스트에 요소 삽입(insert)
# insert(a,b): a번째 위치에 b를 삽입, 숫자는 0부터 센다
a = [1, 2, 3]
a.insert(0,4)
a           # [4, 1, 2, 3]
a.insert(3, 5)
a           # [4, 1, 2, 5, 3]

# 리스트 요소 제거(remove)
# remove(x): 리스트에서 첫 번째로 나오는 x를 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a           # [1, 2, 1, 2, 3]
a.remove(3)
a           # [1, 2, 1, 2]

# 리스트 요소 끄집어내기(pop)
# pop(): 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제
a = [1,2,3]
a.pop()
# 3
a
# [1, 2]

# pop(x): 리스트의 x번째 요소는 돌려주고 그 요소는 삭제
a = [1,2,3]
a.pop(1)
# 2
a
# [1, 3]

# 리스트에 포함된 요소 x의 개수 세기(count)
# count(x): 리스트 안에 x의 갯수를 돌려주는 함수
a = [1,2,3,1]
a.count(1)
# 2

# 리스트 확장(extend)
# extend(x): x에는 리스트만 올수 있으며, 리스트에 x 리스트를 더한다
a = [1, 2, 3]
a.extend([4,5])
a           # [1, 2, 3, 4, 5]
b = [6,7]
a.extend(b)
a           # [1, 2, 3, 4, 5, 6, 7]

# <2-4. 튜플 자료형>
#튜플: 리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
#      리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
t1 = ()
# 단지 1개의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙여야 한다
t2 = (1,)
t3 = (1, 2, 3)
# 괄호( )를 생략해도 무방하다
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# 튜플의 요소값은 삭제, 변경되지 않는다.
# 1. 튜플 요솟값을 삭제하려 할 때
t1 = (1, 2, 'a', 'b')
del t1[0]       # 오류발생: 'tuple' object doesn't support item deletion
# 2. 튜플 요솟값을 변경하려 할 때
t1[0] = 'c'     # 오류발생: 'tuple' object does not support item assignment

# 튜플 다루기
# 인덱싱하기
t1 = (1, 2, 'a', 'b')
t1[0]       # 1
t1[3]       # 'b'

# 슬라이싱하기
t1 = (1, 2, 'a', 'b')
t1[1:]
# (2, 'a', 'b')

# 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t1 + t2
# (1, 2, 'a', 'b', 3, 4)

# 튜플 곱하기
t2 = (3, 4)
t2 * 3
# (3, 4, 3, 4, 3, 4)

# 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
len(t1)
# 4

# <2-5. 딕셔너리 자료형>
# 딕셔너리[=연관 배열(Associative array) 또는 해시(Hash)]
# Key를 통해 Value를 얻는다.
# {Key:Value1, Key:Value2, Key:Value3, ...}

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
# 딕셔너리 dic의 정보
# key	│ value
# ──────┼─────────────
# name	│ pey
# phone	│ 01199993323
# birth	│ 1118

# Value에 문자열을 사용한 경우
a = {1: 'hi'}
# Value에 리스트를 넣을 수 있다.
a = { 'a':[1,2,3]}

# 딕셔너리 쌍 추가, 삭제하기





























# <2-6. 집합 자료형>

# <2-7. 불 자료형>

