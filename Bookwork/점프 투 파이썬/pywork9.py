# pywork9.py start
# <<강의 복습 2. 시작>>

# 제어문.
# 파이썬 코드 블록 작성 규칙
#     ● 가장 바깥쪽에 있는 블록의 코드는 반드시 1열부터 시작
#     ● 내부 블록은 같은 거리맊큼 들여쓰기
#     ● 블록은 { }, begin, end 등으로 구분하지 않고 들여쓰기만으로 구분
#     ● 탭과 공백을 함께 사용하는 것은 권장하지 않음
#     ● 들여쓰기 간격은 일정하기맊 하면 됩니다.

# 조건문 : if문
# if   조건식 :
#     조건식이 참인 경우에 실행될 문장
# 조건문 : if문
# if   조건식 :
#     조건식이 참인 경우에 실행될 문장

if True:
    print('항상 실행1')     # 들여쓰기
    print('항상 실행2')

if False:
    print('실행안됨1')
    print('실행안됨2')
print('무조건 실행됨')

if (3 > 5) :
    print('실행안됨')
print('항상실행3')
print('항상실행4')

# 키보드로 입력한 값이 양수인지 음수인지를 판별하는 프로그램 작성
n = input('정수를 입력')
print(type(n))
n = int(n)

if n>=0:
    print(n, '은(는) 양수')

if n<0:
    print(n, '은(는) 양수')

# 조건문 : if  else문
# if  조건식 :
#      조건식이 참인 경우에 실행될 문장
# else :
#      조건식이 거짓인 경우에 실행될 문장
# 키보드로 입력한 정수값이 양수인지 음수인지를 판별하는 프로그램 작성
try:
    n = int(input('정수 입력!'))

    if n >= 0:
        print(n, '은(는) 양수')
    else:
        print(n, '은(는) 음수')
except:
    print('정수만 입력가능')

# 키보드로 입력한 정수가 짝수, 홀수 인지를 판별하는 프로그램 작성
n = int(input('정수를 입력하세요?'))
if  n % 2 == 0 :                    # 짝수
    print(n, '은(는) 짝수')
else :                              # 홀수
    print(n, '은(는) 홀수')

# 키보드로 입력한 정수 2개 중에서 최대값과 최소값을 구하는 프로그램 작성
n1 = int(input('정수1을 입력하세요?'))
n2 = int(input('정수2를 입력하세요?'))

if n1 >= n2:
    max = n1
    min = n2
else:
    max = n2
    min = n1
print('max=', max)
print('min=', min)

# 조건문 :  if ~ elif  ~ else문
#  if  조건식1 :
#       실행문장
#  elif :
#       실행문장
#  else :
#       위의 조건식을 만족하지 않을 경우에 실행될 문장

# 3개의 정수값을 받아 최대값과 최소값을 판별하기
n1 = int(input('정수1을 입력하세요?'))
n2 = int(input('정수2을 입력하세요?'))
n3 = int(input('정수3을 입력하세요?'))

if n1 >= n2 and n1>=n3:
    max = n1
    if n2>=n3:
        min = n3
    else:
        min = n2
else:
    if n2>=n1 and n2>=n3:
        max = n2
        if n1 >= n3:
            min = n3
        else:
            min = n1
    else:
        max = n3
        if n1 >= n2:
            min = n2
        else:
            min = n1
print('max:', max)
print('min:', min)

# 키보드로 점수(0~100점)를 입력 했을때, 입력한 점수가 어느 학점에 해당되는지 판별하는
# 프로그램 작성
#  90점 이상       A학점
#  80~89점        B학점
#  70~79점        C학점
#  60~69점        D학점
#  60점 미만       F학점
s = int(input('점수를 입력하세요?'))        # s = 95

if s >= 90:
    print('A학점')
elif s >= 80:
    print('B학점')
elif s >= 70:
    print('C학점')
elif s >= 60:
    print('D학점')
else:
    print('F학점')

# 반복문 : while문
# while  조건식 :
#     조건식이 참인 경우에 실행될 문장

# '사랑해요' 메세지를 10번 출력
i = 1                       # 초기값
while  i <= 10:             # 조건식
    print(i, '사랑해요')
    # i = i + 1             # 증감식
    i += 1                  #  ++i(x), i++(x)

# 1 ~ 10까지 합을 구하는 프로그램 작성






























# <<강의 복습 2. 끝>>
# pywork9.py end