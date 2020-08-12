# pywork7.py start
# <<교재 8장 시작>>

# Q1 문자열 바꾸기
# 다음과 같은 문자열이 있다.
# a:b:c:d
# 문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오.
# a#b#c#d
a = 'a:b:c:d'
b = a.split(':')
b
c = '#'.join(b)
c

# Q2 딕셔너리 값 추출하기
# 다음은 딕셔너리의 a에서 'C'라는 key에 해당하는 value를 출력하는 프로그램이다.

a = {'A':90, 'B':80}
a['C']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'C'
# a 딕셔너리에는 'C'라는 key가 없으므로 위와 같은 오류가 발생한다.
# 'C'에 해당하는 key 값이 없을 경우 오류 대신 70을 얻을 수 있도록 수정하시오.
a.get('C', 70)

# Q3 리스트의 더하기와 extend 함수
# 다음과 같은 리스트 a가 있다.
a = [1, 2, 3]
# 리스트 a에 [4, 5]를 + 기호를 사용하여 더한 결과는 다음과 같다.
a = [1, 2, 3]
a = a + [4,5]
a
# [1, 2, 3, 4, 5]
# 리스트 a에 [4,5]를 extend를 사용하여 더한 결과는 다음과 같다.
a = [1, 2, 3]
a.extend([4, 5])
a
# [1, 2, 3, 4, 5]
# + 기호를 사용하여 더한 것과 extend한 것의 차이점이 있을까?
# 있다면 그 차이점을 설명하시오.
id(a)
# +: 두리스트가 더해진 새로운 주소 할당
# extend: 주소 값이 변하지 않음

# Q4 리스트 총합 구하기
# 다음은 A학급 학생의 점수를 나타내는 리스트이다.
# 다음 리스트에서 50점 이상 점수의 총합을 구하시오.
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0
while A:
    pop = A.pop()
    if pop >= 50:
        result = result + pop
print(result)
# 481

# Q5 피보나치 함수
# 첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때,
# 이후에 이어지는 항은 이전의 두 항을 더한 값으로 이루어지는 수열을
# 피보나치 수열이라고 한다.
0, 1, 1, 2, 3, 5, 8, 13, ...
# 입력을 정수 n으로 받았을 때, n 이하까지의
# 피보나치 수열을 출력하는 함수를 작성해 보자.
n = input('정수입력')
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))

# 다른 알고리즘
def fib(n):
    if n <=1:
        return n
    else:
        return fib(n-2) + fib(n-1)
for i in range(1,10):
    print(fib(i))
#
fib = []
for i in range(0,10):
    if i < 2:
        fib.append(1)
    else:
        fib.append(fib(i-2) + fib(i-1))
print(fib)
#
fib = [1,1]
[fib.append(a[i-2] + fib[i-1]) for i in range(0, 10) if i >= 2]
print(fib)
#
fib = [1,1]
[fib.append(fib[-1] + fib[-2]) for i in range(0,10)]
print(fib)
#
fib = lambda n : n if n < 2 else fib(n-1) + fib(n-2)
for i in range(1, 10):
    print(fib(i))

# Q6 숫자의 총합 구하기
# 사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을
# 구하는 프로그램을 작성하시오. (단 숫자는 콤마로 구분하여 입력한다.)
# 65,45,2,3,45,8
n = input('입력')
re = n.split(',')
re
type(re)
sum = 0
for i in re:
    sum = sum +int(i)
print(sum)

# Q7 한 줄 구구단
# 사용자로부터 2~9의 숫자 중 하나를 입력받아 해당 숫자의
# 구구단을 한 줄로 출력하는 프로그램을 작성하시오.
# 실행 예)
# 구구단을 출력할 숫자를 입력하세요(2~9): 2
# 2 4 6 8 10 12 14 16 18
inn = input('2~9')
n = int(inn)
for i in range(1,10):
    print(i*n, end=' ')

# Q8 역순 저장
# 다음과 같은 내용의 파일 abc.txt가 있다.
# AAA
# BBB
# CCC
# DDD
# EEE

# 이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.
# EEE
# DDD
# CCC
# BBB
# AAA

f = open('abc.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()

# Q9 평균값 구하기
# 다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다.
# sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후
# 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.

# 70
# 60
# 55
# 75
# 95
# 90
# 80
# 80
# 85
# 100

f = open('sample.txt')
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score
average = total / len(lines)

f = open('result.txt', 'w')
f.write(str(average))   #숫자 값은 result.txt 파일에 바로 쓸 수 없다
f.close()

# Q10 사칙연산 계산기
# 다음과 같이 동작하는 클래스 Calculator를 작성하시오.
# class Calculator:
#     def init (self, number):
#         self.number = number
#     def add(self):
#         result = 0
#         for i in self.number:
#             result += i
#         return result
#     def avg(self):
#         result = self.add()
#         return total / len(self.number)

class Calculator:
    def init (self, numberList):
        self.numberList = numberList

    def add(self):
        result = 0
        for num in self.numberList:
            result += num
        return result

    def avg(self):
        total = self.add()
        return total / len(self.numberList)

cal1 = Calculator([1,2,3,4,5])
cal1.sum() # 합계
15
cal1.avg() # 평균
3.0
cal2 = Calculator([6,7,8,9,10])
cal2.sum() # 합계
40
cal2.avg() # 평균
8.0


























# <<교재 8장 끝>>
# pywork7.py end