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































# <<교재 4장 끝>>
# pywork3.py end
