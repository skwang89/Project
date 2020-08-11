# pywork.py start
# <<교재 2장 시작>>


# 2-1. 숫자형
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

# 2-2. 문자열 자료형
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






















