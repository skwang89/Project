# pywork14.py start
# <<강의 복습 7. 시작>>


# 정규 표현식
# ● 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어
# ● Programming Language나 Text Editor 등 에서 문자열의 검색과 치환을 위한 용도로 사용
# ● 입력한 문자열에서 특정한 조건을 표현할 경우 일반적인 조건문으로는 다소 복잡할 수도 있지맊,
#   정규 표현식을 이용하면 매우 간단하게 표현
# ● 코드가 간단한 맊큼 가독성이 떨어져서 표현식을 숙지하지 않으면 이해하기 힘들다는 문제점
# ● 파이썬에서 정규식은 re 모듈이 제공

# 정규표현식을 사용하지 않고 주민번호 뒷자리를 * 로 변경
data = """
 park 800905-1049118
 kim  700905-1059119
 """
result=[]
for line in data.split('\n'):           # line = "park 800905-1049118"
    word_result=[]                         # word = "park"
    for word in line.split(' '):           # word = "800905-1049118"
        if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6]+'-'+'*******'   # word = "800905-*******"
        word_result.append(word)            # word_result=["park","800905-*******"]
    result.append(" ".join(word_result))
print('\n'.join(result))

# 정규표현식을 사용하여 주민번호 뒷자리를 * 로 변경
import re
data = """
        park 800905-1049118
        kim  700905-1059119
       """
# 정규 표현식 생성
pat = re.compile('(\d{6})[-](\d{7})')
# sub( 바꿀 문자열, 대상 문자열 )
# g<그룹명> : 정규표현식의 첫번째 그룹을 참조함 (그룹번호는 1번부터 시작함)
# 주민번호 뒷자리를 * 문자로 변경
print(pat.sub("\g<1>-*******", data))
# 주민번호 앞자리를 * 문자로 변경
print(pat.sub("******-\g<2>", data))

# 전화번호 뒷자리를 * 문자로 변경
import re
s = """
    park 010-9999-9988
    kim 010-9909-7789
    lee 010-8789-7768
    """
pat = re.compile("(\d{3}[-]\d{4})[-](\d{4})")
result  = pat.sub("\g<2>-****", s)
print(result)

# 메타 문자(meta characters)
# 메타문자란 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용되는 문자를 의미한다.
# 정규 표현식에서 사용하는 메타문자의 종류
# . ^ $ * + ? { } [ ] \ | ( )
import re
# 문자 클래스 : [ ]
# [abc] : a,b,c 중 한개의 문자라도 있으면 매치
# 정규표현식 생성
p1 = re.compile('[abc]')
print(p1.match('a'))            # match='a'
print(p1.match('before'))       # match='b'
print(p1.match('dude'))         # None
p = re.match('[abc]', 'a')      # match='a'
print(p)

# dot : .
# a.b : a와 b사이에 줄바꿈 문자를 제외한 어떤 문자가 들어가도 모두 매치
p2 = re.compile('a.b')
print(p2.match('aab'))          # match='aab'
print(p2.match('a0b'))          # match='a0b'
print(p2.match('abc'))          # None

# 반복 : *
# ca*t : * 문자 바로 앞에 있는 a가 0번 이상 반복되면 매치
p3 = re.compile('ca*t')
print(p3.match('ct'))           # match='ct'
print(p3.match('cat'))          # match='cat'
print(p3.match('caaat'))        # match='caaat'

# 반복 : +
# + 는 최소 1번 이상 반복될때 사용한다.
# ca+t : +문자 바로 앞에 있는 a가 1번 이상 반복되면 매치
p4 = re.compile('ca+t')
print(p4.match('ca'))           # None
print(p4.match('cat'))          # match='cat'
print(p4.match('caaat'))        # match='caaat'

# 반복 : {m}
# ca{2}t : a가 2번 반복되면 매치
p5 = re.compile('ca{2}t')
print(p5.match('cat'))          # None
print(p5.match('caat'))         # match='caat'

# 반복 : {m, n}
# ca{2, 5}t : a가 2~5회 반복되면 매치
p6 = re.compile('ca{2,5}t')
print(p6.match('cat'))          # None
print(p6.match('caat'))         # match='caat'
print(p6.match('caaaaat'))      # match='caaaaat'

# 반복 : ?
# ? 메타문자가 의미하는 것은 {0,1} 이다.
# ab?c : a가 0~1번 사용되면 매치
p7 = re.compile('ab?c')
print(p7.match('ac'))           # match='ac'
print(p7.match('abc'))          # match='abc'
print(p7.match('abbc'))         # None

# re 모듈의 주요 함수
# complie(pattern[.flags]): 정규식 객체를 생성
# search(pattern, string[. flags])
# match(pattern, string[. flags])
# split(pattern, string[. maxsplit=0]): pattern을 기준으로 분리
# findall(pattern, string): pattern을 만족하는 모든 문자열을 추출
# sub(pattern, repl, string[, count=0]): pattern을 찾아서 repl로 치환하는데 count는 치환횟수를 제한

# Match 객체의 메소드
# group(): 매칭된 문자열 반환
# groups(): 매칭된 전체 그룹 문자열을 튜플 형식으로 반환
# start(): 매칭된 문자열의 시작 위치 리턴
# end(): 매칭된 문자열의 마지막 위치 리턴
# span: 매칭된 문자열의 (시작, 끝) 위치를 리턴

# Match()
import re
m1 = re.match('[0-9]', '1234')
print(m1)                           # match='1'
print(m1.group())                   # 1 : 매치된 문자열 반환
m2 = re.match('[0-9]', 'abc')
print(m2)                           # None : 매치되는 문자 없음
m3 = re.match('[0-9]+', '1234')
print(m3)                           # match='1234'
print(m3.group())                   # 1234
# 맨 앞에 공백이 있는 경우
m4 = re.match('[0-9]+', ' 1234')
print(m4)                           # None
# 맨 앞에 공백이 오는 경우에는 \s를 이용해야 한다.
m5 = re.match('\s[0-9]+', ' 1234')
print(m5)                           # match=' 1234'
print(m5.group())                   # 1234
# search()메소드는 문자열 전체를 검색하여 정규식과 매치되는지 검사한다.
m6 = re.search('[0-9]+', ' 1234')
print(m6)                           # match='1234'
print(m6.group())                   # 1234

# 정규표현식을 이용한 문자열 검색에 사용되는 함수

# 함수            기능
#-----------------------------------------------------------------------------------
# match()       문자열의 처음부터 정규식과 매치되는지 검사한다.
# search()      문자열 전체를 검색하여 정규식과 매치되는지 검사한다.
# findall()     정규식과 매치되는 모든 문자열을 리스트로 리턴한다.
# finditer()    정규식과 매치되는 모든 문자열을 iterator객체로 리턴한다.

import re
# 영문자(a~z) 정규식 생성
from sympy import primenu
p = re.compile('[a-z]+')

# 1. match()
# match() 함수는 정규식과 매치될때에는 match객체를 리턴하고
# 매치되지 않는 경우에는 None 을 리턴한다.
m1 = p.match('python')
print(m1)                       # match='python'
m2 = p.match('Python')
print(m2)                       # None
m3 = p.match('pythoN')
print(m3)                       # match='pytho'
m4 = p.match('pyThon')
print(m4)                       # match='py'
m5 = p.match('3 python')
print(m5)                       # None
print('----------------------------------------------')

# 2. search()
print('search()함수')
s1 = p.search('python')
s2 = p.search('Python')
s3 = p.search('pythoN')
s4 = p.search('pyThon')
s5 = p.search('3 python')
print(s1)                   # match='python'
print(s2)                   # match='ython'
print(s3)                   # match='pytho'
print(s4)                   # match='py'
print(s5)                   # match='python'
print('----------------------------------------------')

# 3. finaall() 함수
result1 = p.findall('life is too short')
print(type(result1))        # 'list'
print(result1)              # ['life', 'is', 'too', 'short']

result2 = p.findall('Life is tOo shorT')
print(result2)              # ['ife', 'is', 't', 'o', 'shor']
print('-----------------------------------------------------')

# 4. finditer() 함수
result3 = p.finditer('life is too short')
print(type(result3))        # 'callable_iterator'
print(result3)              # <callable_iterator object at 0x0000024DE862BB48>
for r in result3:
    print(r)

result4 = p.finditer('Life is tOo shorT')
for r in result4:
    print(r)

# 주민번호 형식 검사
import re

# 주민번호 정규식 생성
p = re.compile('(\d{6})[-](\d{7})')

num = input('주민번호를 입력하세요 (901001-1234123')
print(p.search(num))
if p.search(num) != None:
    print('올바른 형식')
else:
    print('틀린 형식')

# sub() 함수 : 문자열을 치환 해주는 함수
# 형식 : sub(바꿀 문자열, 대상 문자열)
import re

# 정규 표현식 생성
p =re.compile('blue|white|red')

# blue, white, red 라는 문자를 color로 치환
print(p.sub('color', 'blue socks and red shoes'))
# color socks and color shoes

# 치환하는 횟수 지정
# blue, white, red 라는 문자
# 를 color로 치환(1번만 치환함)
print(p.sub('color', 'blue socks and red shoes', count=1))
# color socks and red shoes


# <<강의 복습 7. 끝>>
# pywork14.py end