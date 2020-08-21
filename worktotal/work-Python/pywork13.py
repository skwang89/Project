# pywork13.py start
# <<강의 복습 6. 시작>>


# 데이터베이스 연동: MySQL연동
import pymysql

# 데이터베이스 접속
con = pymysql.connect(host = 'localhost',
                      user = 'root',
                      passwd = '1234',
                      port = 3306,
                      db = 'mysql',
                      charset = 'utf8')
# 커서 생성
cursor = con.cursor()
# SQL 실행
cursor.execute('select * from user')
row = cursor.fetchone()         # 1개의 데이터를 구해옴
print(type(row))                # 'tuple'
print(row)
rows = cursor.fetchall()        # 모든 데
# 이터를 구해옴
print(type(rows))               # 'tuple'
print(rows)

for r in rows:
    print(r)

# MySQL: insert
# contact 테이블에 데이터 입력
import pymysql
try:
    # 데이터베이스 접속
    con = pymysql.connect(host = 'localhost',
                          user = 'jspid',
                          passwd = 'jsppass',
                          port = 3306,
                          db = 'jsptest',
                          charset = 'utf8')
    # 커서 생성
    cursor = con.cursor()
    #SQL문 실행
    sql = "insert into contact(name, phone) values('kim', '010-1111-2222')"
    cursor.execute(sql)
    con.commit()

    print('데이더 입력 성공')
except Exception as err:
    print(err)
finally:
    con.close()

# MySQL: insert_by_keyboard
# 키보드로 입력한 정보를 contact 테이블에 저장
import pymysql
try:
    con = pymysql.connect(host='localhost',
                          user='jspid',
                          passwd='jsppass',
                          port=3306,
                          db='jsptest',
                          charset='utf8')
    cursor = con.cursor()

    name = input('이름을 입력하세요')
    phone = input('전화번호를 입력하세요')

    cursor.execute("insert into contact(name, phone) values(%s, %s)", (name, phone))
    con.commit()
    print('입력 성공')
except Exception as err:
    print(err)
finally:
    con.close()
# 한글 입력시 오류가 날 경우 콘솔에서 MySQL로 들어가
# ALTER TABLE table_name convert to charset utf8; 을 입력하자

# MySQL: select_one
# contact 테이블의 데이터 1개 검색
import pymysql
try:
    con = pymysql.connect(host='localhost',
                          user='jspid',
                          passwd='jsppass',
                          port=3306,
                          db='jsptest',
                          charset='utf8')
    cursor = con.cursor()
    cursor.execute('select * from contact')
    row = cursor.fetchone()         # 데이터 1개를 구해옴
    print(type(row))                # 'tuple'
    print(row)                      # (1, '안화수', '010-1111-2222')
    for r in row:
        print(r)
except Exception as err:
    print(err)
finally:
    con.close()

# MySQL: select_all
# contact 테이블의 모든 데이터를 검색
import pymysql
try:
    con = pymysql.connect(host='localhost',
                          user='jspid',
                          passwd='jsppass',
                          port=3306,
                          db='jsptest',
                          charset='utf8')
    cursor = con.cursor()
    cursor.execute('select * from contact')
    rows = cursor.fetchall()        # 모든 데이터를 구해옴
    print(type(rows))               # 'tuple'
    print(rows)                     # cf. sqlite, oracle은 list로 처리됨
    for r in rows:
        print(r)
except Exception as err:
    print(err)
finally:
    con.close()

# MySQL: update
# contact 데이블의 데이터 수정
import pymysql
try:
    con = pymysql.connect(host='localhost',
                          user='jspid',
                          passwd='jsppass',
                          port=3306,
                          db='jsptest',
                          charset='utf8')
    cursor = con.cursor()
    # sql = "update contact set phone='1234' where num=1"
    # cursor.execute(sql)
    cursor.execute("update contact set phone='1234-1234' where num=1")
    con.commit()
    print('수정 성공')
except Exception as err:
    print(err)
finally:
    con.close()

# MySQL: delete
# contact 테이블의 데이터 삭제
try:
    con = pymysql.connect(host='localhost',
                          user='jspid',
                          passwd='jsppass',
                          port=3306,
                          db='jsptest',
                          charset='utf8')
    cursor = con.cursor()
    num = input('삭제할 회원번호를 입력하세요')
    # 데이터 삭제
    # sql = "delete from contact where num=%s"
    # cursor.execute(sql, num)
    cursor.execute("delete from contact where num=%s", num)
    print('회원 삭제')
    # 모든 데이터 검색
    cursor.execute("select * from contact")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    # 데이터 갯수 구하기
    cursor.execute('select count(*) from contact')
    count = cursor.fetchone()           # 총 데이터 갯수 구하기
    for c in count:
        print('총 데이터 객수:', c, '개')
    con.commit()
except Exception as err:
    print(err)
finally:
    con.close()

# sqlite, oracle, MongoDB 연동 생략


# <<강의 복습 6. 끝>>
# pywork13.py end
