# pywork5.py start
# <<교재 6장 시작>>


# <6-1. 구구단 2단 만들기>
# 함수 이름 GuGu
# 입력받는 값 2
# 출력하는 값 2단(2, 4, 6, 8, …, 18)
# 결과는 리스트로 저장
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i = i +1
    return result
print(GuGu(2))
# [2, 4, 6, 8, 10, 12, 14, 16, 18]

# <6-2. 3과 5의 배수 합하기>
# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다.
# 이들의 총합은 23이다.
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

# 1000미만의 자연수 구하기
n =1
while n < 1000:
    print(n)
    n += 1
for n in range(1,1000):
    print(n)

# 3의 배수 찾기
for n in range(1,1000):
    if n%3 == 0:
        print(n)

# 최종 결과
result = 0
for n in range(1, 1000):
    if n%3 == 0 or n%5 == 0:
        result += n
print(result)

# <6-3. 게시판 페이징하기>
# 함수 이름: getTotalPage
# 입력 받는 값 :게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
# 출력하는 값: 총 페이지수

# 총 페이지수 = (총 건수 / 한 페이지당 보여 줄 건수) + 1
# 한 페이지당 10건식 예) 5 = (49/10) + 1
def getTotalPage(m, n):
    return m // n + 1
print(getTotalPage(5, 10))    # 1
print(getTotalPage(15, 10))   # 2
print(getTotalPage(25, 10))   # 3
print(getTotalPage(30, 10))   # 4

# 총페이지가 0, 페이지 나눈 값이 0 일 때 오류 해결
def getTotalPage(m, n):
    if m == 0:
        print('게시물이 없습니다.')
    elif m % n ==0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(0, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))

# <6-4. 간단한 메모장 만들기> : 생략

# <6-5. 탭을 4개의 공백을 바꾸기> : 생략

# <6-6. 하위 디렉토리 검색하기>
# 1. 디렉토리 파일을 검색
import os
def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        print (full_filename)
search("c:/")
# os.listdir를 사용하면 해당 디렉터리에 있는 파일들의 리스트를 구할 수 있다.
# 파일 리스트는 파일 이름만 포함되어 있으므로 경로를 포함한 파일 이름을
# 구하기 위해서는 입력으로 받은 dirname을 앞에 덧붙여 주어야 한다.
# os 모듈에는 디렉터리와 파일 이름을 이어 주는 os.path.join 함수가 있으므로
# 이 함수를 사용하면 디렉터리를 포함한 전체 경로를 쉽게 구할 수 있다.

# 2.확장자가 .py인 파일만을 출력
import os
def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.py':
            print(full_filename)
search("c:/")

# os.path.splitext는 파일 이름을 확장자를 기준으로 두 부분으로 나누어 준다.
# os.path.splitext(full_filename)[-1]은 해당 파일의 확장자 이름이 된다.

# 3. 하위 디렉토리도 검색
def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)   # 재귀
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass
search("c:/")
# try ... except PermissionError로 함수
# os.listdir를 수행할 때 권한이 없는 디렉터리에 접근하더라도
# 프로그램이 오류로 종료되지 않고 그냥 수행되도록 하기 위해서이다.

# full_filename이 디렉터리인지 파일인지 구별하기 위하여
# os.path.isdir 함수를 사용하였고 디렉터리일 경우
# 해당 경로를 입력받아 다시 search 함수를 호출하였다.

# 참고. 하위 디렉터리 검색을 쉽게 해주는 os.walk
import os
for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" %(path, filename))

# <6-7. 파이보>
# 파이보 : https://pybo.kr
# 질문 답변 게시판

# <6-8. 코딩도장>
# 코딩도장 : http://codingdojang.com
# 코딩 문제 사이트


# <<교재 6장 끝>>
# pywork5.py end