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
one
two
three



























# <<교재 3장 시작>>
# pywork2.py start

