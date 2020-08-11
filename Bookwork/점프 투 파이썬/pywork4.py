# pywork4.py start
# <<교재 5장 시작>>


# <5-1. 클래스>
# 사칙연산 클래스 만들기
# 1.클래스 구조 만들기
class FourCal:
    pass
# ※ pass는 아무것도 수행하지 않는 문법으로 임시로 코드를 작성할 때 주로 사용
a = FourCal()
type(a)
# __main__.FourCal
# ※ type 함수는 파이썬이 자체로 가지고 있는 내장 함수로 객체 타입을 출력한다.

# 2. 객체에 숫자 지정할 수 있게 만들기
a.setdata(4,2)
# 'FourCal' object has no attribute 'setdata'
# 위 문장을 수행하려면 다음과 같이 소스 코드를 작성한다.
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
# 클래스 안에 구현된 함수는 다른 말로 메서드(Method)라고 부른다.
# 일반적인 함수를 만들 때 다음과 같이 작성한다.
#
# def 함수명(매개변수):
#     수행할 문장
#     ...

# setdata 메서드를 다시 보면 다음과 같다.
# def setdata(self, first, second):   # ① 메서드의 매개변수
#     self.first = first              # ② 메서드의 수행문
#     self.second = second            # ② 메서드의 수행문

# ① setdata 메서드의 매개변수
# setdata 메서드는 매개변수로 self, first, second 3개 입력값을 받는다.
# 그런데 일반 함수와는 달리 메서드의 첫 번째 매개변수 self는 특별한 의미를 가진다.
a = FourCal()
a.setdata(4,2)
# ※ 객체를 통해 클래스의 메서드를 호출하려면
# a.setdata(4, 2)와 같이 도트(.) 연산자를 사용해야 한다.
# 변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달된다.
# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.

# ※ 메서드의 첫 번째 매개변수 self를 명시적으로 구현하는 것은 파이썬만의 독특한 특징이다.
# 예를 들어 자바 같은 언어는 첫 번째 매개변수 self가 필요없다.

# 메서드의 또 다른 호출 방법
a = FourCal()
FourCal.setdata(a, 4, 2)
# 위와 같이 클래스 이름.메서드 형태로 호출할 때는
# 객체 a를 첫 번째 매개변수 self에 꼭 전달해 주어야 한다.
# 반면에 다음처럼 객체.메서드 형태로 호출할 때는
# self를 반드시 생략해서 호출해야 한다.

# ② setdata 메서드의 수행문
# a.setdata(4, 2)처럼 호출하면 setdata 메서드의 매개변수 first, second에는
# 각각 값 4와 2가 전달되어 setdata 메서드의 수행문은 다음과 같이 해석된다.
# self.first = 4
# self.second = 2

# self는 전달된 객체 a이므로 다시 다음과 같이 해석된다.
a.first = 4
a.second = 2
# a.first = 4 문장이 수행되면 a 객체에 객체변수 first가 생성되고 값 4가 저장된다.
# a.second = 2 문장이 수행되면 a 객체에 객체변수 second가 생성되고 값 2가 저장된다.
# ※ 객체에 생성되는 객체만의 변수를 객체변수라고 부른다.

a = FourCal()
a.setdata(4,2)
print(a.first)
# 4
print(a.second)
# 2
# a 객체에 객체변수 first와 second가 생성되었음을 확인할 수 있다.

# 이번에는 다음과 같이 a, b 객체를 만들어 보자.
a = FourCal()
b = FourCal()
# 그리고 a 객체의 객체변수 first를 다음과 같이 생성한다.
a.setdata(4,2)
print(a.first)
# 4
b.setdata(3,7)
print(b.first)
# 3

print(a.first)
# a 객체의 first 값은 b 객체의 first 값에 영향받지 않고 원래 값을 유지하고있다.
# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.

# id 함수를 사용하면 객체변수가 독립적인 값을 유지한다는 점을 좀 더 명확하게 증명해 보일 수 있다.
a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,7)
id(a.first)         # 140737405559280
id(b.first)         # 140737405559248
# a 객체의 first 주소 값과 b 객체의 first 주소 값이 서로 다르므로
# 각각 다른 곳에 그 값이 저장된다는 것을 알 수 있다.

# 3. 더하기 기능 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
a = FourCal()
a.setdata(4,2)
print(a.add())
# 6

# def add(self):
#     result = self.first + self.second
#     return result
# add 메서드의 매개변수는 self이고 반환 값은 result이다.
# 반환 값인 result를 계산하는 부분은 다음과 같다.
# result = self.first + self.second
# a.add()와 같이 a 객체에 의해 add 메서드가 수행되면 add 메서드의 self에는
# 객체 a가 자동으로 입력되므로 위 내용은 다음과 같이 해석한다.
result = a.first + a.second
# a.add() 메서드 호출 전에 a.setdata(4, 2) 가 먼저 호출되어
# a.first = 4, a.second = 2 라고 이미 설정되었기 때문에
# 다시 다음과 같이 해석한다.
rsult = 4 + 2
print(a.add())
# 6

# 4. 곱하기, 빼기, 나누기 기능 만들기
class FourCal():
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
a.add()
# 6
a.mul()
# 8
a.sub()
# 2
a.div()
# 2.0
b.add()
# 11
b.mul()
# 24
b.sub()
# -5
b.div()
# 0.375

# 5. 생성자 (Constructor)
# 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.
a = FourCal()
a.add()
# 오류발생: 'FourCal' object has no attribute 'first'
# setdata 메서드를 수행해야 객체 a의 객체변수 first와 second가 생성되기 때문
# 객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은
# 메서드를 호출하여 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법
# 파이썬 메서드 이름으로 __init__를 사용하면 이 메서드는 생성자가 된다.
class FourCal():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

def __init__(self, first, second):
    self.first = first
    self.second = second
# __init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다.
# 단 메서드 이름을 __init__으로 했기 때문에 생성자로 인식되어
# 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.
a = FourCal()           # 오류발생
# __init__() missing 2 required positional arguments:
#                                       'first' and 'second'
# 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문

# first와 second에 해당되는 값을 전달하여 객체를 생성해야 오류가 해결된다.
a = FourCal(4,2)
# 위와 같이 수행하면 __init__ 메서드의 매개변수에는 각각 오른쪽과 같은 값이 대입된다.

# 매개변수   값
# self	    생성되는 객체
# first	    4
# second    2

# ※ __init__ 메서드도 다른 메서드와 마찬가지로
# 첫 번째 매개변수 self에 생성되는 객체가 자동으로 전달된다는 점을 기억하자.
print(a.first)
# 4
print(a.second)
# 2
a.add()
# 6
a.div()
# 2.0

# 6. 클래스의 상속: class 클래스 이름(상속할 클래스 이름)
# FourCal 클래스에 ab (a의 b제곱)을 구할 수 있는 기능을 추가
class MoreFourCal(FourCal):
    pass
a = MoreFourCal(4,2)
a.add()
# 6
a.mul()
# 8
a.sub()
# 2
a.div()
# 2.0

# 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면
# 상속을 사용해야 한다.
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4,2)
a.pow()
# 16

# 메서드 오버라이딩
a = FourCal(4, 0)
a.div()
# 에러발생: division by zero

# 0으로 나눌 때 오류가 아닌 0을 돌려주도록 만든다
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0    # 나눈는 값이 0인 경우 0을 리턴하도록 수정
        else:
            return self.first / self.second
# SafeFourCal 클래스는 FourCal 클래스에 있는 div 메서드를 동일한 이름으로
# 다시 작성하였다. 이렇게 부모 클래스(상속한 클래스)에 있는 메서드를
# 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(Overriding, 덮어쓰기)이라고
# 한다. 이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신
# 오버라이딩한 메서드가 호출된다.
a = SafeFourCal(4,0)
a.div()
# 0

# 클래스 변수
class Family:
    lastname = "김"
# Family 클래스에 선언한 lastname이 바로 클래스 변수이다.
# 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로
# 클래스 안에 변수를 선언하여 생성한다.
print(Family.lastname)
# 김

# 클래스 변수는 위 예와 같이 클래스이름.클래스 변수로 사용할 수 있다.
a = Family()
b = Family()
print(a.lastname)
# 김
print(b.lastname)
# 김

Family.lastname = '박'
print(a.lastname)
# 박
print(b.lastname)
# 박
# 클래스 변수 값을 변경했더니 클래스로 만든 객체의 lastname 값도 모두 변경된다.
# 즉 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다.

# d 함수를 사용하면 클래스 변수가 공유된다는 사실을 증명할 수 있다.
id(Family.lastname)
# 2620281444912
id(a.lastname)
# 2620281444912
id(b.lastname)
# 2620281444912
# id 값이 모두 같으므로 Family.lastname, a.lastname, b.lastname은
# 모두 같은 메모리를 가리키고 있다.

# <5-2. 모듈>
# 모듈: 함수나 변수 또는 클래스를 모아 놓은 파일
# 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일
# 다른 사람들이 이미 만들어 놓은 모듈을 사용할 수도 있고
# 우리가 직접 만들어서 사용할 수도 있다.

# 모듈 만들기
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 모듈 불러오기
# ※ 대화형 인터프리터를 실행

# import mod1
# print(mod1.add(3,4))
# 7
# print(mod1.sub(4,2))
# 2
# ※ import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된
# 디렉터리에 있는 모듈만 불러올 수 있다. 파이썬 라이브러리는 파이썬을 설치할 때
# 자동으로 설치되는 파이썬 모듈을 말한다.

# import의 사용 방법: import 모듈이름
# 모듈 이름 없이 함수 이름만 쓰고 싶은 경우:
#               from 모듈이름 import 모듈함수
# from mod1 import add
# add(3,4)
# 7

# add 함수와 sub 함수를 둘 다 사용하고 싶을 때
# from mod1 import add, sub
# from mod1 import *

# if __name__ == "__main__": 의 의미
# def add(a, b):
#     return a+b
#
# def sub(a, b):
#     return a-b

# print(add(1, 4))
# 5
# print(sub(4, 2))
# 2

# 명령 프롬프트 창
# C:\Users\pahkey> cd C:\doit
# C:\doit> python
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import mod1
# 5
# 2


def add(a, b):
    return a+b

def sub(a, b):
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))

# if __name__ == "__main__"을 사용하면 C:\doit>python mod1.py처럼
# 직접 이 파일을 실행했을 때는 __name__ == "__main__"이 참이 되어
# if문 다음 문장이 수행된다.
# 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는
# __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.

# __name__ 변수
# 파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.
# 만약 C:\doit>python mod1.py처럼 직접 mod1.py 파일을 실행할 경우
# mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.
# 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는
# mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.

# 클래스나 변수 등을 포함한 모듈
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def add(a, b):
    return a+b

# import mod2
# print(mod2.PI)
# 3.141592
#
# a = mod2.Math()
# print(a.solv(2))
# 12.566368
#
# print(mod2.add(mod2.PI, 4.4))
# 7.541592

# 다른 파일에서 모듈 불러오기: 생략

# <5-3. 패키지>
# 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다.
# 파이썬 패키지는 디렉터리와 파이썬 모듈로 이루어지며 구조는 다음과 같다.
# game/
#     __init__.py
#     sound/
#         __init__.py
#         echo.py
#         wav.py
#     graphic/
#         __init__.py
#         screen.py
#         render.py
#     play/
#         __init__.py
#         run.py
#         test.py
# game, sound, graphic, play는 디렉터리 이름이고
# 확장자가 .py인 파일은 파이썬 모듈이다.
# game 디렉터리가 이 패키지의 루트 디렉터리이고
# sound, graphic, play는 서브 디렉터리이다.

# 패키지 만들기: 생략
# 패키지 안의 함수 실행하기: 생략

# __init__.py 의 용도
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
# ※ python3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식한다(PEP 420).
# 하지만 하위 버전 호환을 위해 __init__.py 파일을 생성하는 것이 안전한 방법이다.

# relative 패키지: 생략

# <5-4. 예외처리>
# 파이썬은 try, except를 사용해서 예외적으로 오류를 처리할 수 있게 해준다.

# 자주 일어나는 오류
# 1. 없는 파일을 열려고 시도
# FileNotFoundError: [Errno 2] No such file or directory: 'file'
# 2. 0으로 다른 숫자를 나누는 경우
# ZeroDivisionError: division by zero
# 3. 리스트에서 얻을 수 없는 값
# IndexError: list index out of range

# 오류 예외 처리 기법
# try, except문
# try:
#     ...
# except [발생 오류[as 오류 메시지 변수]]:
#     ...
# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 하지만
# try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

# exception 구문:
# except [발생 오류 [as 오류 메시지 변수]]:

# 1. try, except만 쓰는 방법
# try:
#     ...
# except:
#     ...
# 이 경우는 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행한다.

# 2. 발생 오류만 포함한 except문
# try:
#     ...
# except 발생 오류:
#     ...
# 이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과
# 일치할 때만 except 블록을 수행한다는 뜻이다.

# 3. 발생 오류와 오류 메시지 변수까지 포함한 except문
# try:
#     ...
# except 발생 오류 as 오류 메시지 변수:
#     ...
# 이 경우는 두 번째 경우에서 오류 메시지의 내용까지 알고 싶을 때
# 사용하는 방법이다.

# 사용예: ZeroDivisionError
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
# 위처럼 4를 0으로 나누려고 하면 ZeroDivisionError가 발생하여
# xcept 블록이 실행되고 변수 e에 담기는 오류 메시지를 다음과 같이 출력한다.
# 결과값: division by zero

# try .. finally
# finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다.
# 보통 finally절은 사용한 리소스를 close해야 할 때에 많이 사용한다.
# f = open('foo.txt', 'w')
# try:
#     # 무언가를 수행한다.
# finally:
#     f.close()

# 여러개의 오류처리하기
# try:
#     ...
# except 발생 오류1:
#    ...
# except 발생 오류2:
#    ...

# 예 0으로 나누는 오류와 인덱싱 오류를 다음과 같이 처리할 수 있다.
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")
# "인덱싱할 수 없습니다."

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
# "list index out of range"

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# 오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass
# try문 안에서 FileNotFoundError가 발생할 경우 pass를 사용하여 오류를 회피

# 오류 일부러 발생시키기
# 파이썬은 raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다.

# 예를 들어 Bird 클래스를 상속받는 자식 클래스는 반드시
# fly라는 함수를 구현하도록 만들고 싶은 경우(강제로 그렇게 하고 싶은 경우)
# 가 있을 수 있다. 다음 예를 보자.
#
# class Bird:
#     def fly(self):
#         raise NotImplementedError

# ※ NotImplementedError는 파이썬 내장 오류로,
# 꼭 작성해야 하는 부분이 구현되지 않았을 경우
# 일부러 오류를 일으키기 위해 사용한다.

# class Eagle(Bird):
#     pass
#
# eagle = Eagle()
# eagle.fly()

# Eagle 클래스는 Bird 클래스를 상속받는다.
# 그런데 Eagle 클래스에서 fly 함수를 구현하지 않았기 때문에
# Bird 클래스의 fly 함수가 호출된다.
# 그리고 raise문에 의해 NotImplemented Error가 발생할 것이다.

# NotImplementedError가 발생되지 않게 하려면
# 다음과 같이 Eagle 클래스에 fly 함수를 반드시 구현해야 한다.
# class Eagle(Bird):
#     def fly(self):
#         print("very fast")
#
# eagle = Eagle()
# eagle.fly()

# 위 예처럼 fly 함수를 구현한 후 프로그램을 실행하면 오류 없이 다음 문장이 출력된다.
# very fast

# 예외 만들기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
say_nick('천사')
# 천사
say_nick('바보')
# Traceback (most recent call last):
#   File "", line 3331, in run_code
#     exec(code_obj, self.user_global_ns, self.user_ns)
#   File "<ipython-input-112-b251284280ef>", line 1, in <module>
#     say_nick('바보')
#   File "<ipython-input-110-b937db9042c4>", line 6, in say_nick
#     raise MyError()
# MyError

# 예외 처리 기법을 사용
try:
    say_nick('천사')
    say_nick('바보')
except MyError:
    print("허용되지 않는 별명입니다.")
# 천사
# 허용되지 않는 별명입니다.

# 오류 메시지를 사용하고 싶다면 다음처럼 예외 처리를 하면 된다.
try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)
# 하지만 프로그램을 실행해 보면 print(e)로 오류 메시지가 출력되지 않는 것을
# 확인할 수 있다. 오류 메시지를 출력했을 때 오류 메시지가 보이게 하려면
# 오류 클래스에 다음과 같은 __str__ 메서드를 구현해야 한다.
# __str__ 메서드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에
# 호출되는 메서드이다.

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

# <5-5. 내장함수>
# abs
# 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수
abs(3)
# 3
abs(-3)
# 3
abs(-1.2)
1.2

# all
# 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며
# 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
# ※ 반복 가능한 자료형이란 for문으로 그 값을 출력할 수 있는 것을 의미한다.
# 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.
all([1, 2, 3])
# True
all([1, 2, 3, 0])
# False: 요소 0은 거짓이므로 False
all([])
# True

# any
# x의 요소 중 하나라도 참이 있으면 True를 돌려주고,
# x가 모두 거짓일 때에만 False를 돌려준다.
any([1, 2, 3, 0])
# True
# 리스트 자료형 [1, 2, 3, 0] 중에서 1, 2, 3이 참이므로 True를 돌려준다.
any([0, ""])
# False
# 리스트 자료형 [0, ""]의 요소 0과 ""은 모두 거짓이므로 False를 돌려준다.
any([])
# False
# 만약 any의 입력 인수가 빈 값인 경우에는 False를 리턴한다.

# chr
# 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
chr(97)
# 'a'
chr(48)
# '0'

# dir
# 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다
dir([1,2,3])
dir([1, 2, 3])
# ['append', 'count', 'extend', 'index', 'insert', 'pop',...]
dir({'1':'a'})
# ['clear', 'copy', 'get', 'has_key', 'items', 'keys',...]

# divmod
# divmod(a, b)는 2개의 숫자를 입력으로 받는다.
# 그리고 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
divmod(7,3)
# (2, 1)

# enumerate
# enumerate는 "열거하다"라는 뜻이다.
# 이 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
# ※ 보통 enumerate 함수는 다음 예제처럼 for문과 함께 자주 사용한다.
for i, name in enumerate(['boby','foo','bar']):
    print(i,name)
# 0 body
# 1 foo
# 2 bar
# enumerate를 for문과 함께 사용하면
# 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.

# eval
# eval(expression )은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을
# 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다.
eval('1+2')
# 3
eval("'hi' + 'a'")
# 'hia'
eval('divmod(4, 3)')
# (1, 1)

# filter
# filter 함수는 첫 번째 인수로 함수 이름을,
# 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
# 그리고 두 번째 인수인 반복 가능한 자료형 요소가
# 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서(걸러 내서)
# 돌려준다.
# filter함수 없이 양수를 추출
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result
print(positive([1,-3,2,0,-5,6]))
# [1, 2, 6]

# filter함수 사용
def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
# [1, 2, 6]

# hex
# hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수이다.

hex(234)
# '0xea'
hex(3)
# '0x3'

# id
# 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.
a = 3
id(3)
135072304
id(a)
135072304
b = a
id(b)
135072304

# input
# nput([prompt])은 사용자 입력을 받는 함수이다.
# 매개변수로 문자열을 주면 다음 세 번째 예에서 볼 수 있듯이
# 그 문자열은 프롬프트가 된다.
a = input()
# hi
a
# 'hi'
b = input("Enter: ")
# Enter: hi
b
# 'hi'

# int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로,
# 정수를 입력으로 받으면 그대로 돌려준다.
int('3')
# 3
int(3.4)
# 3

# nt(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.
# 2진수로 표현된 11의 10진수 값은 다음과 같이 구한다.
int('11', 2)
# 3
# 16진수로 표현된 1A의 10진수 값은 다음과 같이 구한다.
int('1A', 16)
# 26

# isinstance
# 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여
# 참이면 True, 거짓이면 False를 돌려준다.
class Person: pass
...
a = Person()
isinstance(a, Person)
# True: a가 Person 클래스가 만든 인스턴스임을 확인시켜 준다.

b = 3
isinstance(b, Person)
# False: b는 Person 클래스가 만든 인스턴스가 아니므로 False를 돌려준다.

# len












# <<교재 5장 끝>>
# pywork4.py end
