# pywork12.py start
# <<강의 복습 5. 시작>>


# 클래스.
# class: 관련있는 저장공간과 기능을 하나로 묶은 것 - Encapsulation
# class Object: 클래스와 동일한 의미로 사용하는데 어떤 클래스를 구체적으로 지정하기 위해 사용
# class instance: 클래스를 호출하여 생성된 객체
# method: 클래스 안에 정의된 함수
# member variable: 클래스 안에 정의된 변수
# attribute: 클래스 안에 있는 모든 것
# Inheritance: 하위 클래스가 상위 클래스의 모든 속성을 물려받는 것
# Super Class: Base Class라고도 하는데 다른 클래스의 상위 클래스
# Sub Class: Derived Class라고도 하는데 다른 클래스로부터 속성을 물려받는 클래스
# Multiple Inheritance: 2개 이상의 클래스로부터 상속받는 것
# Polymorphism: 동일한 코드가 상황에 따라 다르게 반응하는 것
# 객체(Object) = 속성(Attribute) + 기능(Method)

# 메소드 생성
# • 메소드를 클래스 내부에 선언할 때는 첫번째 매개변수는 무조건 현재 클래스의 객체가 되어야 한다.
# • 관습적으로 self 라는 단어를 이용한다.
# • 두번째 매개변수 부터는 사용자가 정의할 수 있다.
# • 메소드를 호출하는 방법
#   ●클래스 이름을 이용한 호출(언바운드 호출)
#       클래스이름.메소드이름(인스턴스이름, 매개변수)
#   ●인스턴스 이름을 이용한 호출(바운드 호출)
#       인스턴스이름.메소드이름(매개변수)
#   ●클래스 내부에서 자신의 클래스에 속한 메소드를 호출
#       self.메소드이름(매개변수)

# 클래스 내의 변수 생성
# • 메소드 외부에서 선언하면 클래스 변수: 클래스 내부에 1개만 만들어지며 클래스 이름으로 접근할
# 수 있고 객체 이름으로도 접근해서 사용할 수 있게 된다.
# • 메소드 내부에서 self와 함께 선언되면 인스턴스 변수: 각 객체 내부에 각각 만들어지면 객체 이름으
# 로만 접근해서 사용할 수 있다.
# • 메소드 내부에서 self. 과 함께 변수를 선언하지 않으면 그 변수는 메소드의 지역변수가 된다.

# 생성자: __init__()
# • 객체가 생성된 후 가장 먼저 호출되는 메소드
# • “초기화하다”는 뜻의 initialize를 줄여서 붙여진 이름
# • 첫번째 매개변수는 self 이며 이후에 매개변수 추가 가능
# • self 이외의 매개변수가 있는 생성자를 만들면 인스턴스를 생성할 때 매개변수를 넘겨 주어야 한다.
# • 멤버 변수의 초기화 코드를 주로 작성한다.
# 소멸자:__del__()
# • 객체가 소멸될 때 호출되는 메소드
# • 외부 자원을 사용하는 경우 해제하는 코드를 주로 작성
# • self 이외의 매개변수를 받지 않는다.

# 정적 메소드
# • 인스턴스를 생성하지 않고 클래스를 이용해서 직접 호출할 수 있는 메소드
# • 메소드 내에서 멤버 변수를 호출할 수 없습니다.
# • 클래스 변수는 호출할 수 있습니다.
# • @staticmethod 데코레이터로 수식
# • self 키워드 없이 정의
# 클래스 메소드
# • @classmethod 데코레이터로 수식
# • 정적 메소드와 유사하지만 첫번째 매개변수로 클래스 객체가 전달되는 것이 다릅니다.
# • cls 매개변수 사용

# private 멤버 명명 규칙
# • private 멤버는 클래스 내부에서는 접근이 가능하지만 클래스 외부(인스턴스)에서 접근이 되지 않는 멤버
# • 이와 반대되는 개념으로 public이 있는데 public 멤버는 클래스 외부(인스턴스)에서 접근이 가능한 멤버이다.
# • python의 모든 멤버는 기본적으로 public
# • 문법적으로 지원하지는 않고 이름을 이용해서 private 이라는 의미만 전달
# • 두 개의 밑줄 __ 이 접두사여야 한다.
# • 접미사는 밑줄이 한 개까지만 허용된다.
# • 접미사의 밑줄이 두 개 이상이면 public으로 간주한다.
# Property
# • 변수를 호출하는 것 처럼 사용하지만 실제로는 getter 와 setter 메소드를 호출하는 것으로 처리되는 속성
# • 변수명 = property(fget=None, fset=None, fdel=None, doc=None)
# • fget은 getter, fset은 setter, fdel은 삭제할 때 사용할 메소드

# 상속(Inheritance)
# • 한 클래스가 다른 클래스로부터 데이터 속성과 메소드를 물려받는 것
# • 상속하는 클래스를 기반(Base)클래스 또는 상위(Super)클래스라고 하고 상속을 받는 클
# 래스를 파생(Derived)클래스, 하위(Sub)클래스라고 한다.
class 기반 클래스:
# 멤버 정의
class 파생 클래스(기반 클래스)
# 아무 멤버를 정의하지 않아도 기반 클래스의 모든 것을 물려받아 갖게 된다.
# private 멤버(__로 시작되는 이름을 갖는 멤버)는 상속은 되지만 접근할 수 없다.

# 상속 - super()
# super()는 부모 클래스의 객체 역할을 하는 프록시(Proxy)를 반환하는 내장함수
# • super() 함수의 반환 값을 상위클래스의 객체로 간주하고 코딩.
# • 객체 내의 어떤 메소드에서든 부모 클래스에 정의되어 있는 메소드를 호출하고 싶으면
# super()를 이용.

# 상속 - overrloding(재정의)
# Overriding은 부모 클래스에 있는 메소드를 하위 클래스에서 다시 정의하는 것
# •상위 클래스의 기능이 부족해서 기능을 추가하기 위한 목적과 다형성 구현을 위해서 사용한다.
# •자신이 만든 클래스가 아닌 클래스를 상속받아서 메소드를 오버라이딩 할 때는
#   대부분 상위 클래스의 메소드를 호출하고 새로운 내용을 추가
# •프레임워크에서 제공하는 클래스의 메소드 들은 본연의 기능이 있으므로
#   그 기능을 수행하고 다른 기능을 추가해야 하는 경우가 있다.
# • Overriding을 이용해서 Polymorphism(다형성)을 구현할 수 있는 있는데
#   Polymorphism 이란 동일한 메시지에 대하여 다르게 반응하는 성질을 의미하는데
#   오버라이딩이나 함수 포인터를 이용해서 구현한다.

# 상속 - 다중 상속
# 다중상속은 자식 하나가 여러 부모(?!)로부터 상속을 받는 것
# • 파생 클래스의 정의에 기반 클래스의 이름을 콤마(,)로 구분해서 쭉 적어주면
# 다중상속이 이루어짐.

# 위임(Delegation)
# 어떤 객체가 자신이 처리할 수 없는 메시지를 받으면 해당 메시지를
#   처리할 수 있는 다른 객체에 전달하는 기법
# __getattr__()를 구현하면 되는데 이 메소드의 매개변수는
#   name 매개변수를 추가로 갖습니다.
# name은 참조하는 속성 이름이 넘어가게 됩니다.

# 데코레이터
# 데코레이터는 __call__() 메소드를 구현하는 클래스
# • __call__() 메소드는 객체를 함수 호출 방식으로 사용하게 만드는 마법 메소드

# 이터레이터
# 파이썬에서 for문을 실행할 때 가장먼저 하는 일은 순회하려는 객체의
# __iter__() 메소드를호출하는 것.
# • __iter__() 메소드는 이터레이터(Iterator)라고 하는 특별한 객체를
#   for문에게 반환(이터레이터는 __next__() 메소드를 구현하는 객체)
# • for문은 매 반복을 수행할 때마다 바로 이 __next__() 메소드를 호출하여
#   다음 요소를 얻어냄.
# range() 함수가 반환하는 객체도 순회가능한 객체.

# 제너레이터
# 제네레이터(Generator)는 yield문을 이용하여 이터레이터보다 더 간단한 방법으로 순회가
# 능한 객체를 만들게 해줌.
# • yield문은 return문처럼 함수를 실행하다가 값을 반환하지만, return문과는 달리 함수를
#   종료시키지는 않고 중단시켜 놓기만 함.

# 메타 클래스(Meta Class)
# • 클래스를 만들어내는 클래스
# • 파이썬은 클래스도 하나의 객체로 취급해서 변수에 치환을 할 수 있고 복사도 가능하고
# 속성 값을 동적으로 추가할 수 있고 함수의 매개변수로 대입할 수 있다.
# • 객체이므로 다른 코드 블록 내에서 생성이 가능
# type() 함수
# • 매개변수로 객체를 대입하면 객체의 자료형을 리턴한다.
# • 다른 용도로는 클래스의 기능을 동적으로 확장하는 역할을 한다.
# • 클래스를 만들 때는 첫번째 매개변수는 클래스이름이고 두번째 매개변수는 상위 클래스
# 이름이고 세번째 매개변수는 속성과 값을 디셔너리로 대입하면 된다.

# 추상 클래스
# 추상 클래스(Abstract Class)
# • 하위 클래스들의 특징을 소유하고 있는 클래스
# • 추상 클래스를 정의할 때는 abc 모듈의 ABCMeta 클래스를 상속받아야 한다.
# • Metaclass를 상속받을 때는 metaclass=메타클래스이름
# • 추상 메소드는 이름만 존재하고 내용이 없는 메소드
# • 추상 메소드는 @abstractmethod 데코레이터를 이용
# • 추상 클래스는 자신의 객체를 생성할 수 없다.
# • 상속을 받아서 하위 클래스에서 메소드를 재정의해서 사용한다.

# 싱글톤(Singleton)
# Singleton Class
# • 객체를 1개만 만들 수 있는 클래스
# • 공유 데이터를 소유하는 클래스나 관리자 클래스 또는 서버 측에서 클라이언트의 요청
# 을 처리하는 클래스를 Singleton으로 만드는 경우가 많다.

# final Class
# • 상속을 하지 못하는 클래스


# 사용자 정의 클래스
# 클래스 = 멤버변수 + 멤버함수(생성자, 메소드)
class Animal:
    name = 'dog'            # 멤버변수
    age = 5
# 객체 생성
a1 = Animal()
# print(name)               # 오류발생
print(a1.name)              # dog
print(a1.age)               # 5
a1.name = 'cat'             # 멤버변수 name값을 cat으로 수정
a1.age = 10                 # 멤버변수 age값을 10으로 수정
print(a1.name)              # cat
print(a1.age)               # 10
a2 = Animal()
print(a2.name)              # dog
print(a2.age)               # 5

# if __name__=='__main__':
# 1. __name__은 현재 모듈 이름을 가진 내장변수
# 2. 외부에서 import해서 사용하지 못하고, 현재의 인터프리터에 의해서
#    직접 실행하고 싶은 경우에 사용한다.
class InstanceVar:
    def __init__(self):                 # 생성자
        self.text_list = []             # 멤버변수 : 비어있는 리스트
    def add(self, *text):               # 메소드 : 리스트에 값을 추가하는 역할
        self.text_list.append(text)
    def print_list(self):               # 메소드 : 리스트를 출력하는 역할
        print(self.text_list)

if __name__=='__main__':
    a = InstanceVar()                   # 객체 생성 : 생성자 호출
    print(a.text_list)                  # [] : 비어있는 리스트
    a.add('파이썬','오라클','스프링')
    a.print_list()                      # [('파이썬', '오라클', '스프링')]

    b = InstanceVar()                   # 객체 생성 : 생성자 호출
    b.add('자바')
    b.print_list()                      # [('자바',)]
    print(b.text_list)                  # [('자바',)]

# 사용자 정의 클래스
# 클래스 = 멤버변수 + 멤버함수(생성자, 메소드)
class Car:
    # 생성자는 객체가 생성될때 호출된다.
    # 생성자는 멤버변수를 초기화 시키는 역할을 한다.
    def __init__(self):                 # 생성자(Constructor)
       self.color = 'red'               # 바디의 색깔
       self.wheel_size = 16             # 바퀴의 크기
       self.displacement = 2000         # 배기량

    def forward(self):                  # 메소드
        print('전진')
    def backward(self):
        print('후진')
    def turn_left(self):
        print('좌회전')
    def turn_right(self):
        print('우회전')

# 객체 생성
car1 = Car()
# 멤버변수에 접근
print(car1.color)
print(car1.wheel_size)
print(car1.displacement)
# 메서드 호출
car1.forward()
car1.backward()
car1.turn_left()
car1.turn_right()

# if __name__=='__main__':
# 1. __name__은 현재 모듈 이름을 가진 내장변수
# 2. 외부에서 import해서 사용하지 못하고, 현재의 인터프리터에 의해서
#    직접 실행하고 싶은 경우에 사용한다.
# mode1.py로 파일을 작성했다 가정
def add(a, b):
    return a+b
def sub(a,b):
    return a-b
print(add(20, 10))              # 30
print(sub(20, 10))              # 10
# mode2.py로 파일을 작성했다 가정
def add(a, b):
    return a+b
def sub(a,b):
    return a-b
if __name__=='__main__':
    print(add(20, 10))          # 30
    print(sub(20, 10))          # 10

# call1.py에서 mode1.py를 불러오기
import mode1
# call2.py에서 mode2.py를 불러오기
import mode2

# 매개변수가 있는 생성자
class ContactInfo:
    def __init__(self, name, email):  # 매개변수가 있는 생성자
        self.name = name  # name = '홍길동'
        self.email = email  # email = 'test@naver.com'
    def print_info(self):  # 멤버변수를 출력하기 위한 메소드
        print('{0} : {1}'.format(self.name, self.email))

if __name__ == '__main__':
    ahn = ContactInfo('홍길동', 'test@naver.com')
    print(ahn.name)
    print(ahn.email)
    ahn.print_info()
    ca = ContactInfo('choongang', 'master@gmail.com')
    print(ca.name)
    print(ca.email)
    ca.print_info()

# 정적 메소드(static method)
# 1. 정적 메소드는 공유를 목적으로 하는 경우에 사용한다.
# 2. 정적 매소드를 만들기 위해서는 메소드 위에 @staticmethod 데코레이터를
#    붙어서 만든다.
# 3. 정적 메소드는 객체를 생성하지 않고, 클래스명.정적메소드 형식으로 호출한다.
# 4. 정적 메소드는 self를 사용하지 않는다.
class Calculator:
    @staticmethod
    def plus(a,b):                  # 정적 메소드
        return a+b
    @staticmethod
    def minus(a,b):                 # 정적 메소드
        return a-b
    @staticmethod
    def multiply(a,b):              # 정적 메소드
        return a*b
    @staticmethod
    def divide(a,b):                # 정적 메소드
        return a/b

if __name__=='__main__':            # 정적 메소드 호출
    print('{0}+{1}={2}'.format(7,4, Calculator.plus(7,4)))
    print('{0}-{1}={2}'.format(7,4, Calculator.minus(7,4)))
    print('{0}*{1}={2}'.format(7,4, Calculator.multiply(7,4)))
    print('{0}/{1}={2}'.format(7,4, Calculator.divide(7,4)))

# 상속(Inheritance)
# : 부모 클래스의 메소드는 상속된다.
class Base:  # 부모 클래스, 기반 클래스
    def base_method(self):
        print('부모 메소드')

# Base 클래스를 상속 받는다
class Derived(Base):  # 자식 클래스, 파생 클래스
    pass

base = Base()  # 부모 클래스로 객체 생성
base.base_method()  # 메소드 호출
derived = Derived()  # 자식 클래스로 객체 생성
derived.base_method()  # 상속 받는 메소드 호출

# 클래스의 상속
class Add:                      # 부모 클래스, 기반 클래스
    def add(self, n1, n2):
        return n1 + n2
# Add 클래스를 상속 받는다.
class Calculator(Add):          # 자식 클래스, 파생 클래스
    def sub(self, n1, n2):
        return n1 - n2

# 부모 클래스로 객체 생성
ob = Add()
print(ob.add(100, 200))         # 300
# print(ob.sub(100, 200))       # 오류발생 (자식 클래스의 sub()메소드는 접근할 수 없다.)

# 자식클래스로 객체 생성
obj = Calculator()
print(obj.add(10, 20))          # 30 : add()메소드는 상속을 받아서 사용함
print(obj.sub(10, 20))          # -10

# 메소드 오버라이딩(Method Overriding)
# 1. 부모클래스로 부터 상속받은 메소드를 자식클래스에서 재정의 해서 사용하는 것을 의미한다.
# 2. 부모클래스의 메소드 이름과 형식을 그대로 가지면서, 내용만 다르게 기술하는 것을 의미한다.
# 3. 메소드 오버라이딩을 하면, 메소드 오버라이딩된 메소드만 호출된다.
# 4. 부모클래스의 은닉된 메소드를 호출하려면, 자식클래스의 메소드 안에서 super()를 이용해서
#     호출하면 된다.  ex) super().mymethod()










































all = [var for var in globals() if var[0] != "_"]
for var in all:
    del globals()[var]
del(all)
del(var)

import sys
sys.modules[__name__].__dict__.clear()


# <<강의 복습 5. 끝>>
# pywork12.py end
