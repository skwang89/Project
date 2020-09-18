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

# 소수(prime number) 판별 프로그램 작성
'''
소수(prime number)
: 양의 약수가 1과 자기 자신 뿐인 1보다 큰 자연수로 정의

2보다 큰 정수를 입력받아서 소수인지 판별
소수는 2부터 자신의 절반이 되는 숫자까지 나누어서 한번도 나누어 떨어지지 않는 숫자
2,3,5,7,11,13 등이 소수
'''
pn = int(input('정수입력'))
max = pn // 2
#나누어 떨어지는지 아닌지 여부를 표시하기 위한 변수
flag = False
for i in range(1, max+1):
    if(pn % i == 0):
        flag = True
        break
if flag == False:
    print('소수')
else:
    print('소수가 아님')

# 반복문: while문
# while  조건식 :
#     조건식이 참인 경우에 실행될 문장

# '사랑해요' 메세지를 10번 출력
i = 1                       # 초기값
while  i <= 10:             # 조건식
    print(i, '사랑해요')
    # i = i + 1             # 증감식
    i += 1                  #  ++i(x), i++(x)

# 1 ~ 10까지 합을 구하는 프로그램 작성
i=1; sum=0              # 초기값
while i <= 10:          # 조건식
    sum += i
    i += 1              # 증감식 : i = i + 1

print('1~10까지 합:', sum)

# 1 ~ 100까지 홀수, 짝수의 합을 구하는 프로그램 작성
i = odd = even = 0          # 초기값
while i <= 100:             # 조건식
    if i%2 == 0:            # 짝수
        even += i
    else:                   # 홀수
        odd += i
    i += 1                  # 증감식 : i = i + 1
print('1~100까지 홀수의 합:', odd)
print('1~100까지 짝수의 합:', even)

# 키보드로 원하는 단을 입력 받아서 구구단 1개 단을 출력하는 프로그램 작성
dan = int(input('원하는 단을 입력'))
i = 1
while i <= 9:
    print(dan, '*', i, '=', dan*i)
    i += 1

# 구구단 2~9단 까지 출력하는 프로그램 작성
dan = 2
while dan <= 9:
    print('[ ', dan,'단 ]')
    i = 1
    while i <= 9:
        print(dan, '*', i, '=', dan*i)
        i += 1
    dan += 1
    print()

# 반복문: for문
# for  변수  in range() :
#    반복 실행할 문장

# range(초기값, 최종값, 증감값) : 초기값 ~ 최종값-1 까지 증감
for i in range(1, 10, 2):
    print(i, end=' ')               # 1 3 5 7 9
print()

# range(초기값, 최종값) : 초기값 ~ 최종값-1 까지
for i in range(1, 10):
    print(i, end=' ')               # 1 2 3 4 5 6 7 8 9
print()

# range(최종값) : 0 ~ 최종값-1 까지
for i in range(10):                 # 0 ~ 9
    print(i, end=' ')               # 0 1 2 3 4 5 6 7 8 9
print()

# 10부터 2까지 1씩 감소
for i in range(10, 1, -1):
    print(i, end=' ')               # 10 9 8 7 6 5 4 3 2

# '사랑해요' 메세지를 10번 출력하는 프로그램 작성
for i in range(10):  # 0 ~ 9
    print(i + 1, '사랑해요')
for i in range(1, 11):  # 1 ~ 10
    print(i, '사랑해요')
for i in range(1, 11, 1):  # 1 ~ 10
    print(i, '사랑해요')

# 1 ~ 10 까지 합을 구하는 프로그램 작성
sum = 0
for i in range(1, 11):
    sum = sum + i
    print('1~', i, '=', sum)
print('sum= ', sum)

# # 1 ~ 100 까지 홀수의 합과 짝수의 합을 구하는 프로그램 작성
# 단, for문을 1번만 사용해서 작성
odd = even = 0
for i in range(1, 101):
    if i%2==0:
        even += i
    else:
        odd += i
print('1~100까지 홀수의 합:', odd)
print('1~100까지 짝수의 합:', even)

# 키보드로 구구단 1개 단을 입력 받아서 해당 구구단을 출력하는 프로그램 작성
dan = int(input('원하는 단을 입력'))

print('[ ', dan, '단 ]')
for i in range(1, 10):
    # print(dan, '*', i, '=', dan*i)
    print('{0} * {1} = {2}'.format(dan, i, dan*i))

# 구구단 2~9단 까지 출력하는 프로그램 작성
for dan in range(2,10):                     # 단 : 2 ~ 9
    # print('[',dan,'단 ]')                 # 단 title
    print('[ {}단 ]'.format(dan))           # 단 title
    for i in range(1, 10):                  # 1 ~ 9
        # print(dan, '*', i, '=', dan*i)
        print('{0} * {1} = {2}'.format(dan, i, dan*i))
    print()

# 구구단 2~9단 까지 출력하는 프로그램 작성
# 각 단을 열방향으로 출력
for name in range(2, 10):
    print('[ ', name,'단 ] ', end="\t\t")
for i in range(1, 10):
    for d in range(2,10):
        print('{0} * {1} = {2}'.format(d, i, d*i), end="\t")
    print()

# 반복문 : for문
# for  변수  in  컬렉션:
# 리스트(list)
print(type(list))           # <class 'list'>
print(list)                 # ['사과', '딸기', '포도', '배', '키위', '바나나']
print(list[0])              # 사과

for f in list:
    print(f, end=' ')       # 사과 딸기 포도 배 키위 바나나
print()

# 튜플(tuple)
t = ('red','orange','yellow','green','blue','navy','violet')
print(type(t))              # <class 'tuple'>
print(t)                    # ('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'violet')
print(t[0])                 # red

for i in t:
    print(i, end=' ')       # red orange yellow green blue navy violet
print()

# 딕셔너리(dictionary) : { 'key' : 'value' }
dic = {'애플' : 'www.apple.com',
       '구글' : 'www.google.com',
       '네이버' : 'www.naver.com'}

print(type(dic))            # <class 'dict'>
print(dic)                  # {'애플': 'www.apple.com', '구글': 'www.google.com', '네이버': 'www.naver.com'}
print(dic['애플'])           # www.apple.com

for k, v  in dic.items():
    print(k,':',v)

# 1 ~ 12월 중에서 달(Month)에 'r'이 들어있는 달(Month)을 출력
# tuple
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")
# 방법1.
for i in months:
    if 'r' in i.lower():
        print(i)
# 방법2.
for i in months:
    if i.count('r')>0:
        print(i)

# 보조 제어문.
# break 문: 반복문을 빠져 나오는 역할
i = 1
while True:
    print(i, '무한출력')
    if i == 100: break
    i += 1

for i in range(1, 1001):        # 1 ~ 1000
    print(i, '출력')
    if i==100:
        print('루프를 빠져 나옴')
        break

# continue 문: 다시 반복문으로 돌아 가라는 의미로 사용됨
#              continue문 아래쪽 부분은 실행되지 않는다.
for i in range(1, 11):      # 1 ~ 10
    if i == 5:
        continue            # i = 5일 때 출력되지 않음
    print(i, '출력')

# continue 문을 이용해서 1 ~ 100 까지 홀수만 출력하는 프로그램 작성
for i in range(1, 101):         # 1 ~ 100
    if i%2 == 0:                # 짝수
        continue
    print('홀수:', i)

# continue 문을 이용해서 1 ~ 100 정수 중에서 5의 배수만 출력하는 프로그램 작성
for i in range(1, 101):  # 1 ~ 100
    if i % 5 != 0:  # 5의 배수가 아니면
        continue
    print('5의 배수:', i)


