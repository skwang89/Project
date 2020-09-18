# <<교재 7장 시작>>


# <7-1. 정규 표현식 살펴보기>
# 주민등록번호를 포함하고 있는 텍스트가 있다.
# 이 텍스트에 포함된 모든 주민등록번호의 뒷자리를 * 문자로 변경해 보자.
# 정규식을 사용하지 않을 때
data = """
park 800905-1049118
kim  700905-1059119
"""
result = []
for line in data.split("\n"):
    word_reuslt = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_reuslt.append(word)
    result.append(" ".join(word_reuslt))
print("\n".join(result))

# 정규식을 사용할 때
import re
data = """
park 800905-1049118
kim  700905-1059119
"""
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

# <7-2. 정규 표현식 시작하기>
# 정규 표현식의 기초, 메타 문자
# ※ 메타 문자란 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자
# . ^ $ * + ? { } [ ] \ | ( )

# 문자 클래스 [ ]
# 문자 클래스로 만들어진 정규식은 "[ ] 사이의 문자들과 매치"라는 의미를 갖는다.
# ※ 문자 클래스를 만드는 메타 문자인 [ ] 사이에는 어떤 문자도 들어갈 수 있다.

# 정규 표현식이 [abc]라면 이 표현식의 의미는 "a, b, c 중 한 개의 문자와 매치"를 뜻한다.
# "a", "before", "dude"
# "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
# "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
# "dude"는 정규식과 일치하는 문자인 a, b, c 중
# 어느 하나도 포함하고 있지 않으므로 매치되지 않음
# [From - To]
# [a-zA-Z] : 알파벳 모두
# [0-9] : 숫자

# [자주 사용하는 문자 클래스]

# [0-9] 또는 [a-zA-Z] 등은 무척 자주 사용하는 정규 표현식이다.
# 이렇게 자주 사용하는 정규식은 별도의 표기법으로 표현할 수 있다.
# 다음을 기억해 두자.
# \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다.
#     맨 앞의 빈 칸은 공백문자(space)를 의미한다.
# \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
# \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
# \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치,
#   [^a-zA-Z0-9_]와 동일한 표현식이다.
# 대문자로 사용된 것은 소문자의 반대임을 추측할 수 있다.

# Dot(.)
# 정규 표현식의 Dot(.) 메타 문자는 줄바꿈 문자인
# \n을 제외한 모든 문자와 매치됨을 의미한다.
# ※ 나중에 배우겠지만 정규식을 작성할 때 re.DOTALL 옵션을 주면
# \n 문자와도 매치된다.

#"aab", "a0b", "abc"
# "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 .과 일치하므로
# 정규식과 매치된다.
# "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 .과 일치하므로
# 정규식과 매치된다.
# "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는있어야 하는
# 이 정규식과 일치하지 않으므로 매치되지 않는다.
# a[.]b
# 이 정규식의 의미는 다음과 같다.
# "a + Dot(.)문자 + b"
# 따라서 정규식 a[.]b는 "a.b" 문자열과 매치되고,
# "a0b" 문자열과는 매치되지 않는다.
# ※ 만약 앞에서 살펴본 문자 클래스([]) 내에 Dot(.) 메타 문자가 사용된다면
# 이것은 "모든 문자"라는 의미가 아닌 문자 . 그대로를 의미한다.

# 반복 (*)
# 0부터 무한대로 반복
# ca*t
# 정규식	문자열	Match 여부	설명
# ca*t	ct	    Yes	        "a"가 0번 반복되어 매치
# ca*t	cat	    Yes	        "a"가 0번 이상 반복되어 매치 (1번 반복)
# ca*t	caaat	Yes	        "a"가 0번 이상 반복되어 매치 (3번 반복)

# 반복 (+)
# 최소 1번 이상 반복
# # ca+t
# 정규식	문자열	Match 여부	설명
# ca+t	ct	    No	        "a"가 0번 반복되어 매치되지 않음
# ca+t	cat	    Yes	        "a"가 1번 이상 반복되어 매치 (1번 반복)
# ca+t	caaat	Yes	        "a"가 1번 이상 반복되어 매치 (3번 반복)

# 반복 ({m,n}, ?)
# 반복 횟수가 m부터 n까지 매치
# {1,}은 +와 동일하고, {0,}은 *와 동일하다.
# 1. {m}
# ca{2}t: "c + a(반드시 2번 반복) + t"
# 정규식	문자열	Match 여부	설명
# ca{2}t	cat	    No	        "a"가 1번만 반복되어 매치되지 않음
# ca{2}t	caat	Yes	        "a"가 2번 반복되어 매치

# 2. {m, n}
#
# ca{2,5}t: "c + a(2~5회 반복) + t"
# 정규식	    문자열	Match 여부	설명
# ca{2,5}t	cat	    No	        "a"가 1번만 반복되어 매치되지 않음
# ca{2,5}t	caat	Yes     	"a"가 2번 반복되어 매치
# ca{2,5}t	caaaaat	Yes     	"a"가 5번 반복되어 매치

# 3. ?
# ? 메타문자가 의미하는 것은 {0, 1} 이다.
# ab?c: "a + b(있어도 되고 없어도 된다) + c"
# 정규식	문자열	Match 여부	설명
# ab?c	abc	    Yes	        "b"가 1번 사용되어 매치
# ab?c	ac	    Yes	        "b"가 0번 사용되어 매치

# 파이썬에서 정규 표현식을 지원하는 re 모듈
import re
p = re.compile('[a-z]+')

# 정규식을 이용한 문자열 검색
# match()	    문자열의 처음부터 정규식과 매치되는지 조사한다.
# search()	    문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
# findall()	    정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
# finditer()	정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.
# match, search는 정규식과 매치될 때는 match 객체를 돌려주고,
# 매치되지 않을 때는 None을 돌려준다.


# match
# 문자열의 처음부터 정규식과 매치되는지 조사
m= p.match("python")
print(m)
# <re.Match object; span=(0, 6), match='python'>
m = p.match("3 python")
print(m)
# None

# match의 결괏값이 있을 때만 그다음 작업을 수행하고 싶을때 프로그램
# p = re.compile(정규표현식)
# m = p.match('string goes here')
# if m:
#     print('Match found', m.group())
# else:
#     print('No Match')

# search
# 문자열 전체를 검색
m = p.search("python")
print(m)
# <re.Match object; span=(0, 6), match='python'>
m = p.search("3 python")
print(m)
# <re.Match object; span=(0, 6), match='python'>

# findall
result = p.findall("life is too short")
print(result)
# 문자열의 'life', 'is', 'too', 'short'
# 단어를 각각 [a-z]+ 정규식과 매치해서 리스트로 돌려준다.
# ['life', 'is', 'too', 'short']

# finditer
result = p.finditer("life is too short")
print(result)
# <callable_iterator object at 0x0000026214DC6B88>
for r in result: print(r)
# <re.Match object; span=(0, 4), match='life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>

# finditer는 findall과 동일하지만 그 결과로 반복 가능한 객체(iterator object)를 돌려준다.
# 반복 가능한 객체가 포함하는 각각의 요소는 match 객체이다.

# match 객체의 메서드
# 어떤 문자열이 매치되었는가?
# 매치된 문자열의 인덱스는 어디서부터 어디까지인가?
# group()	매치된 문자열을 돌려준다.
# start()	매치된 문자열의 시작 위치를 돌려준다.
# end()	    매치된 문자열의 끝 위치를 돌려준다.
# span()	매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.

m = p.match('python')
m.group()
# 'python'
m.start()
# 0
m.end()
# 6
m.span()
(0, 6)
m = p.search('3 python')
m.group()
# 'python'
m.start()
# 2
m.end()
# 8
m.span()
(2, 8)

# 모듈 단위로 수행하기
p = re.compile('[a-z]+')
m = p.match("python")

# 축약
m =re.match('[a-z]+', "python")

# 컴파일 옵션
# DOTALL(S)       - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
# IGNORECASE(I)   - 대소문자에 관계없이 매치할 수 있도록 한다.
# MULTILINE(M)    - 여러줄과 매치할 수 있도록 한다.
#                 (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
# VERBOSE(X)      - verbose 모드를 사용할 수 있도록 한다.
#                 (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)

# VERBOSE, X
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)

# 백슬래시 문제: Raw String 규칙
p = re.compile('\\\\section')
p = re.compile(r'\\section')

# <7-3. 강력한 정규 표현식의 세계로>
# 메타문자
# |
# or과 동일한 의미로 사용
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)
# <re.Match object; span=(0, 4), match='Crow'>

# ^
# 문자열의 맨 처음과 일치함을 의미
# 옵션 re.MULTILINE을 사용할 경우에는 여러 줄의 문자열일 때 각 줄의 처음과 일치
print(re.search('^Life', 'Life is too short'))
# <re.Match object; span=(0, 4), match='Life'>
print(re.search('^Life', 'My Life'))
# None

# $
#
print(re.search('short$', 'Life is too short'))
# <re.Match object; span=(12, 17), match='short'>
print(re.search('short$', 'Life is too short, you need python'))
# None

# ※ ^ 또는 $ 문자를 메타 문자가 아닌 문자 그 자체로 매치하고 싶은 경우
# \^, \$ 로 사용

# \A
# 문자열의 처음과 매치됨을 의미
# ^ 메타 문자와 동일한 의미이지만
# re.MULTILINE 옵션을 사용할 경우에는 다르게 해석
# ^은 각 줄의 문자열의 처음과 매치
# \A는 줄과 상관없이 전체 문자열의 처음

# \Z
# 문자열의 끝과 매치됨을 의미
# re.MULTILINE 옵션을 사용할 경우
# $ 메타 문자와는 달리 전체 문자열의 끝과 매치

# \b
# 단어 구분자(Word boundary)이다. 보통 단어는 whitespace에 의해 구분된다
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
# <re.Match object; span=(3, 8), match='class'>
# \bclass\b: 앞뒤가 whitespace로 구분된 class라는 단어와 매치됨을 의미
print(p.search('the declassified algorithm'))
# None
# whitespace로 구분된 단어가 아니므로 매치되지 않는다.
print(p.search('one subclass is'))
# None
# class 앞에 sub 문자열이 더해져 있으므로 매치되지 않음

# 주의: 파이썬 리터럴 규칙에 의하면 백스페이스(BackSpace)를 의미
# Raw string임을 알려주는 기호 r을 반드시 붙여 주어야 한다.
# r'\bclass\b'

# \B
# \b 메타 문자와 반대
# whitespace로 구분된 단어가 아닌 경우에만 매치
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
# None

# 그루핑
# 그룹을 만들어 주는 메타 문자는 바로 ( )
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
# <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group())
# ABCABCABC

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
# \w+\s+\d+[-]\d+[-]\d+은 이름 + " " + 전화번호

# ‘이름’ 부분만 뽑아내려 할때
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))
# park

# group(인덱스)	설명
# group(0)	    매치된 전체 문자열
# group(1)	    첫 번째 그룹에 해당되는 문자열
# group(2)	    두 번째 그룹에 해당되는 문자열
# group(n)	    n 번째 그룹에 해당되는 문자열

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))
# 010
# (\w+)\s+((\d+)[-]\d+[-]\d+)처럼 그룹을 중첩되게 사용하는 것도 가능

# 그루핑된 문자열 재참조하기
p = re.compile(r'(\b\w+)\s+\1')
p.search('Paris in the the spring').group()
# 'the the'
# (\b\w+)\s+\1은 (그룹) + " " + 그룹과 동일한 단어 와 매치됨을 의미
# ※ 두 번째 그룹을 참조하려면 \2

# 그루핑된 문자열에 이름 붙이기
# (?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
# (\w+) --> (?P<name>\w+)
# (?...) 표현식은 정규 표현식의 확장 구문
# (?P<그룹명>...)

# 그룹에 이름을 지정하고 참조
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))
# park

# 그룹이름을 정규식 안에서 재참조
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
p.search('Paris in the the spring').group()
# 'the the'

# 전방 탐색
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
# http:
# 정규식 .+:과 일치하는 문자열로 http:를 돌려주었다.

# 긍정형 전방 탐색
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())
# http
# :에 해당하는 부분에 긍정형 전방 탐색 기법을 적용하여 (?=:)으로 변경
# 기존 정규식과 검색에서는 동일한 효과를 발휘하지만
# : 에 해당하는 문자열이 정규식 엔진에 의해 소비되지 않아
# (검색에는 포함되지만 검색 결과에는 제외됨)
# 검색 결과에서는 :이 제거된 후 돌려주는 효과가 있다.

# .*[.].*$
# 파일 이름 + . + 확장자를 나타내는 정규식
# "bat인 파일은 제외해야 한다"는 조건을 추가
# .*[.][^b].*s
# b라는 문자로 시작하면 안 된다는 의미 .bat .bar ... 제외
# .*[.]([^b].. | .[^a]. | ..[^t])$
# 주정혀 전방 탐색 사용
# .*[.](?!bat$).*$
# 확장자가 bat가 아닌 경우에만 통과된다는 의미이다.
# bat 문자열이 있는지 조사하는 과정에서 문자열이 소비되지 않으므로
# bat가 아니라고 판단되면 그 이후 정규식 매치가 진행된다.

# exe 역시 제외하라는 조건이 추가되더라도 다음과 같이 간단히 표현할 수 있다.
# .*[.](?!bat$|!exe$).*$

# 문자열 바꾸기
# sub 메서드를 사용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있다.
p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')
# 'colour socks and colour shoes'
# 바꾸기 횟수를 제어하려면 다음과 같이 세 번째 매개변수로 count 값을 넘기면 된다.
p.sub('colour', 'blue socks and red shoes', count =1)

# sub 메서드와 유사한 subn 메서드
# subn 역시 sub와 동일한 기능을 하지만 반환 결과를 튜플로 돌려준다는 차이가 있다
# 튜플의 첫 번째 요소: 변경된 문자열
# 두 번째 요소: 바꾸기가 발생한 횟수
p = re.compile('(blue|white|red)')
p.subn( 'colour', 'blue socks and red shoes')
# ('colour socks and colour shoes', 2)

# sub 메서드 사용 시 참조 구문 사용하기
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
# 010-1234-1234 park
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))
# 010-1234-1234 park

# sub 메서드의 매개변수로 함수 넣기
def hexrepl(match):
    value = int(match.group())
    return hex(value)
p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
# 'Call 0xffd2 for printing, 0xc000 for user code.'

# Greedy vs Non-Greedy
s = '<html><head><title>Title</title>'
len(s)
# 32
print(re.match('<.*>', s).span())
# (0, 32)
print(re.match('<.*>', s).group())
# <html><head><title>Title</title>
# non-greedy 문자인 ?를 사용하면 *의 탐욕을 제한
print(re.match('<.*?>', s).group())
# <html>

# non-greedy 문자인 ?는 *?, +?, ??, {m,n}?와 같이 사용할 수 있다.
# 가능한 한 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다.

# <<교재 7장 끝>>
