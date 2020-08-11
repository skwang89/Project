# pywork2.py start
# <<교재 3장 시작>>


# <3-1. if문>
# if문의 기본 구조

# if 조건문:
#     수행할 문장1
#     수행할 문장2
#     ...
# else:
#     수행할 문장A
#     수행할 문장B
#     ...

# 들여쓰기
# if 조건문:
#     수행할 문장1
#     수행할 문장2
#     수행할 문장3

# if 조건문:
#     수행할 문장1
# 수행할 문장2
#     수행할 문장3

# 비교연산자
# 비교연산자│설명
# ─────────┼─────────────────────
# x < y	x가│ y보다 작다
# x > y	x가│ y보다 크다
# x == y   │ x와 y가 같다
# x != y   │ x와 y가 같지 않다
# x >= y   │ x가 y보다 크거나 같다
# x <= y   │ x가 y보다 작거나 같다

# "만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
if money >= 3000:
    print('택시를 타라')
else:
    print('걸어가라')
# 걸어가라

# and, or, not
# 연산자	   │     설명
# ─────────┼─────────────────────
# x or y   │    x와 y 둘중에 하나만 참이어도 참이다
# x and y  │    x와 y 모두 참이어야 참이다
# not x	   │    x가 거짓이면 참이다

# "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
card = True
if money >= 3000 or card:
    print('택시를 타라')
else:
    print('걸어가라')
# 택시를 타라

# # x in s, x not in s
# in	      │  not in
# ────────────┼─────────────────────
# x in 리스트  │	x not in 리스트
# x in 튜플    │ x not in 튜플
# x in 문자열  │	x not in 문자열

1 in [1,2,3]
# True
1 not in [1,2,3]
# False

# "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라."
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('택시를 타라')
else:
    print('걸어가라')
# 택시를 타라

# 조건문에서 아무 일도 하지 않게 설정하고 싶을 때
# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라."
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
# pass가 수행되어 아무 결괏값도 보여주지 않는다.

# 다양한 조건을 판단하는 elif
# "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, " \
# "돈도 없고 카드도 없으면 걸어 가라."
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print('taxi')
else:
    if card:
        print('taxi')
    else:
        print('walk')
# taxi

# 위에 if문을 elif를 변경했을 때
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("taxi")
elif card:
    print("taxi")
else:
    print("walk")
# taxi

# elif 구조
# If <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     ...
# elif <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     ...
# elif <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     ...
# ...
# else:
#    <수행할 문장1>
#    <수행할 문장2>
#    ...

# if문을 한 줄로 작성하기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:pass
else:print("카드를 꺼내라")

# 조건부 표현식
score = 0
message = "success" if score >= 60 else "failure"

# <3-2. while문>
# while문의 기본 구조
# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
#     ...

# "열 번 찍어 안 넘어가는 나무 없다."
hit = 0
while hit <10:
    hit = hit +1
    print('나무를 %d번 찍었습니다.' %hit)
    if hit == 10:
        print('나무가 넘어 갑니다.')

# while문 만들기
# 여러 가지 선택지 중 하나를 선택해서 입력받는 예제
prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number"""

number = 0
while number !=4:
    print(prompt)
    number = int(input())

# while문 강제로 빠져나가기: break

# while문의 맨 처음으로 돌아가기: continue

# 무한 루프
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
# Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
# Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
# Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.
# ...

# <3-3. for문>
# for문의 기본 구조
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2
#     ...

# 예제를 통해 for문 이해하기
# 1. 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
...
# one
# two
# three

# 2. 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
...
# 3
# 7
# 11
# a 리스트의 요솟값이 튜플이기 때문에
# 각각의 요소가 자동으로 (first, last) 변수에 대입된다.

# 3. for문의 응용
# "총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. " \
# "합격인지 불합격인지 결과를 보여 주시오."
marks = [90, 25, 67,45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >=60:
        print('%d번 학생은 합격' %number)
    else:
        print('%d번 학생은 불합격' %number)

# for문과 continue
# while문에서 살펴본 continue문을 for문에서도 사용할 수 있다.
# 즉 for문 안의 문장을 수행하는 도중에 continue문을 만나면
# for문의 처음으로 돌아가게 된다.
for mark in marks:
    number = number + 1
    if mark >=60:
        print('%d번 학생은 합격' %number)
    else:
        continue

for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

# for문과 함께 자주 사용하는 range 함수
a = range(10)
a           # range(0, 10)
a = range(1, 11)
a
# range 함수의 예시 살펴보기
add = 0
for i in range(1, 11):
    add = add + i
print(add)

number = 0
marks = [90, 25, 67,45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 합격" %(number+1))

# for와 range를 이용한 구구단 결과 출력
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print()
# 2 4 6 8 10 12 14 16 18
# 3 6 9 12 15 18 21 24 27
# 4 8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54
# 7 14 21 28 35 42 49 56 63
# 8 16 24 32 40 48 56 64 72
# 9 18 27 36 45 54 63 72 81
# 매개변수 end: 다음줄로 넘기지 않고 그 줄에 계속해서 출력

# 리스트 내포 사용하기
# 사용전
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)
# [3, 6, 9, 12]

# 사용후
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)
# [3, 6, 9, 12]

# 리스트 내포: if 조건 사용
a = [1,2,3,4]
result = [num*3 for num in a if num%2==0]
print(result)
# [6 ,12]

# 리스트 내포 일반문법
# [표현식 for 항목 in 반복가능객체 if 조건문]
# for문을 2개 이상 사용한 리스트 내포 문법
# [표현식 for 항목1 in 반복가능객체1 if 조건문1
#             for 항목2 in 반복가능객체2 if 조건문2
#             ...
#             for 항목n in 반복가능객체n if 조건문n]

# 리스트 내포를 사용한 구구단 결과
result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)
# [2, 4, 6, 8, 10, 12, 14, 16, 18,
#  3, 6, 9, 12, 15, 18, 21, 24, 27,
#  4, 8, 12, 16, 20, 24, 28, 32, 36,
#  5, 10, 15, 20, 25, 30, 35, 40, 45,
#  6, 12, 18, 24, 30, 36, 42, 48, 54,
#  7, 14, 21, 28, 35, 42, 49, 56, 63,
#  8, 16, 24, 32, 40, 48, 56, 64, 72,
 # 9, 18, 27, 36, 45, 54, 63, 72, 81]

# <연습문제>
# Q1
# 다음 코드의 결괏값은 무엇일까?

a = "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# 가장 먼저 참이된 세번째 조건문 shirt가 출력된다.

# Q2
# while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
num = 0
result = 0
while num < 1000:
    num = num + 1
    if num%3==0:
        result = result + num

print(result)

# Q3
# while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
#
# *
# **
# ***
# ****
# *****
i = 0
while i < 5:
    i += 1
    print('*'*i)

# Q4
# for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
i = 0
for i in range(1, 101):
    print(i, end=" ")

# Q5
# A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# for문을 사용하여 A 학급의 평균 점수를 구해 보자.
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
t = 0
for i in A:
    t += i
print(t/len(A))

# Q6
# 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
numbers = [1, 2, 3, 4, 5]
result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)
# 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
result = [n*2 for n in numbers if n%2==1]
print(result)


# <<교재 3장 끝>>
# pywork2.py end
