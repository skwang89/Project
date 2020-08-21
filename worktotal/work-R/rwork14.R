# rwork13.R start
# <<MongoDB연동 시작>>


# 정형 데이터
# R과 오라클 연동

#  예1.

# 1. RJDBC패키지 설치
install.packages("RJDBC")

# 2. 패키지 로딩
library(RJDBC)

# 3. 드라이버 설정
jdbcDriver <- JDBC(driverClass = "oracle.jdbc.OracleDriver",
                   classPath = "c:/ojdbc6.jar")

# 4. 데이터 베이스 연결
con <- dbConnect(jdbcDriver,
                 "jdbc:oracle:thin:@localhost:1522/xe",
                 "scott",
                 "tiger")

# 5. 쿼리 만들기
myquery <- "select sal, comm from emp where comm is not null"

# 6. 쿼리 실행하고 결과를 변수에 저장
r <- dbGetQuery(con, myquery)
r

# 7. 그래프 그리기
plot(r)


#-----------------------------------------------------------------
# 예2. 각 부서별 평균 급여

# 1. RJDBC패키지 설치
install.packages("RJDBC")

# 2. 패키지 로딩
library(RJDBC)

# 3. 드라이버 설정
jdbcDriver <- JDBC(driverClass = "oracle.jdbc.OracleDriver",
                   classPath = "c:/ojdbc6.jar")

# 4. 데이터 베이스 연결
con <- dbConnect(jdbcDriver,
                 "jdbc:oracle:thin:@localhost:1522/xe",
                 "scott",
                 "tiger")

# 5. 쿼리 만들기
myquery <- "select deptno, count(*) cnt,avg(sal) avg,max(sal),min(sal) from emp group by deptno order by deptno"

# 6. 쿼리 실행
r <- dbGetQuery(con, myquery)
r

# 7. 부서별 사원수를 막대 그래프로 출력
barplot(r$CNT)

#8.위의 막대 그래프에 y축 범위를 늘리는 설정
barplot(r$CNT, ylim=c(0,8))

#9. 막대 그래프 하단에 라벨을 추가
barplot(r$CNT, ylim=c(0,8), names.arg=r$DEPTNO)

#10.색깔 입히기
barplot(r$CNT, ylim=c(0,8), names.arg=r$DEPTNO, 
        col=c("red", "green", "blue"))

#11.위의 결과에 제목과 y축 라벨 넣기
barplot(r$CNT, ylim=c(0, 8), names.arg=r$DEPTNO, 
        col=c("red", "green", "blue"), 
        main="부서별사원수", ylab="명")

#12.분석 대상을 부서별 평균 급여로 변경하기
barplot(r$AVG, ylim=c(0, 3000), names.arg=r$DEPTNO,
        col=c("red", "green", "blue"),
        main="부서별 평균급여", ylab="달러($)") 

#---------------------------------------------------------------------
# 예3.
# 1. 3개의 컬럼을 그래프에 추가하기 위해 데이터 추출
r2 <- r[, c(3:5)]

# 2. 데이터 확인
r2

# 3.그래프 그리기
barplot(as.matrix(r2), ylim=c(0, 5000), 
        beside=T,                           
        col=c("red", "green", "blue"))

#4.범례 추가
legend("topright", title="Count of product", 
       c("10","20","30"), 
       fill=c("red", "green","blue"),
       cex=0.7)                       # 범례의 글자 크기 


#--------------------------------------------------------------
# 예4.
#1.80-90 사이의 숫자를 30개 만들기
myquery <- "SELECT level as day, ceil(dbms_random.value(80, 90)) as amt FROM dual connect by level <= 30"

#2.쿼리 실행
r <- dbGetQuery(con, myquery)
r

#3.산점도 그리기
plot(r)

#4.y축 범위 설정
plot(r, ylim=c(50,100))

#5.line 만들기
plot(r, ylim=c(50, 100), type="l" , lty=2) 

#6.선 색상과 제목 만들기
plot(r, ylim=c(50, 100), type="o", lty=2, col="red", 
     main="월 매출 추이")

#-----------------------------------------------------------------
# 예5.
#1.
myquery <- "SELECT job, round(sum(sal)/(SELECT sum(sal) FROM emp), 2) ratio FROM emp GROUP BY job ORDER BY job "

#2.쿼리 실행
r <- dbGetQuery(con, myquery)
r

#3.pie 차트 그리기
pie(r$RATIO)

# 4.라벨 붙이기
pie(r$RATIO, labels = r$JOB)

#5.색상을 설정하기 위하여 직업의 종류 알아내기
query2 <- "SELECT count(distinct job) job_cnt FROM emp"

#6.쿼리 실행
r2 <- dbGetQuery(con, query2); r2

#7.색상 설정
pie(r$RATIO, labels=r$JOB, col=rainbow(r2$JOB_CNT), border="white")

#8.비율이 포함된 라벨을 만들기
job_labels <- sprintf("%s(%.2f%s)", r$JOB, r$RATIO*100, "%"); job_labels

#9. 라벨 붙이기
pie(r$RATIO, labels = job_labels , col=rainbow(r2$JOB_CNT), 
    border="white")

#10.비율을 다음 줄로 출력하기
job_labels <- paste(r$JOB, "\n", "(", r$RATIO*100,"%)"); job_labels

pie(r$RATIO, labels = job_labels , col=rainbow(r2$JOB_CNT), 
    border="white")

#----------------------------------------------------------------
# R에서 MySQL로 접속해서 연동

# 1.RJDBC 패키지 설치
install.packages("RJDBC")

# 2. 패키지 로딩
library(RJDBC)

# 3. 드라이버 설정
jdbcDriver <- JDBC(driverClass = "com.mysql.jdbc.Driver",
                   classPath = "c:/mysql-connector-java-5.1.47-bin.jar")

# 4.데이터베이스 연결
con <- dbConnect(jdbcDriver,
                 "jdbc:mysql://localhost:3306/jsptest",
                 "jspid",
                 "jsppass")
con

# 5. 쿼리 만들기
myquery <- "select * from board1"


# 6. 쿼리 실행
r <- dbGetQuery(con, myquery); r