# 데이터 프레임 만들기
# 데이터 프레임: 행과 열을 가진 2차원 표

# 1. 영어 점수 변수 생성
english <- c(90,80,60,70)
english
# [1] 90 80 60 70

# 2 수학 점수 변수 생성
math <- c(50,60,100,20)
math
# [1]  50  60 100  20

# 3. 데이터 프레임 생성
df_midterm <- data.frame(english, math)
df_midterm
#   english math
# 1      90   50
# 2      80   60
# 3      60  100
# 4      70   20

# 4. 반(클래스) 변수 생성
class <- c(1,1,2,2)
class
# [1] 1 1 2 2

# 5. 3개의 변수를 이용해서 데이터 프레임 생성
df_midterm <- data.frame(english, math, class)
df_midterm
#   english math class
# 1      90   50     1
# 2      80   60     1
# 3      60  100     2
# 4      70   20     2

# 6.english 점수의 평균값
df_midterm$english
# [1] 90 80 60 70
mean(df_midterm$english)
#[1] 75

# 7.math 점수의 평균값
df_midterm$math
# [1]  50  60 100  20
mean(df_midterm$math)
# [1] 57.5

# 데이터 프레임 한 번에 만들기
df_midterm <- data.frame(english = c(90,80,60,70),
                         math = c(50,60,100,20),
                         class = c(1,1,2,2))
df_midterm
#   english math class
# 1      90   50     1
# 2      80   60     1
# 3      60  100     2
# 4      70   20     2

# ================================================================
#   혼자서 해보기
# #Q1. data.frame()과 c()를 조합해서 표의 내용을 
# 데이터 프레임으로 만들어 출력해보세요.
# 제품 가격 판매량
# 사과 1800 24
# 딸기 1500 38
# 수박 3000 13
fruits <- data.frame(제품 = c('사과','딸기','수박'),
                       가격 = c(1800, 1500, 3000),
                       판매량 = c(24, 38, 13))
fruits
#   제품 가격 판매량
# 1 사과 1800     24
# 2 딸기 1500     38
# 3 수박 3000     13

# Q2. 앞에서 만든 데이터 프레임을 이용해서 
# 과일 가격 평균, 판매량 평균을 구해보세요.
mean(fruits$가격)
# [1] 2100
mean(fruits$판매량)
# [1] 25
# ================================================================

# 외부 데이터 이용하기
# readxl 패키지 설치
install.packages('readxl')

# readxl 패키지 로딩
library(readxl)

# 엑설 파일 읽어오기: 상대경로
df_exam <- read_excel("data/excel_exam.xlsx")
df_exam     # 데이터 프레임

# 엑설 파일 읽어오기: 절대경로
df_exam <- read_excel("C:/workspace-total/rworkspace/doitR/Bookwork/Do it! 쉽게 배우는 R 데이터 분석/data/excel_exam.xlsx")
df_exam     # 데이터 프레임

# 영어 성적의 평균
mean(df_exam$english)
# [1] 84.9
# 수학 성적의 평균
mean(df_exam$math)
# [1] 57.45
# 과학 성적의 평균
mean(df_exam$science)
# [1] 59.45

# 엑셀 파일 첫번째 행에 변수병이 없는 경우
df_exam_novar <- read_excel(path = 'data/excel_exam_novar.xlsx',
                            col_names = F)
df_exam_novar

# 엑셀 파일에 시트가 여러개 있는 경우: 3번 sheet에 데이터가 있음
df_exam_sheet <- read_excel('data/excel_exam_sheet.xlsx',
                            sheet = 3)
df_exam_sheet

# 2. CSV
# 1) CSV(comma separated value)
#    컴마(,)로 분리된 데이터를 의미함.
# 2) 용량이 작아서 많이 사용함
# 3) csv 파일을 읽어 올때는 read.csv()로 불러온다.
# 4) 데이터 프레임을 csv파일로 저장할때는 write.csv()로 저장한다.

# csv 파일 불러오기
df_csv_exam <- read.csv('data/csv_exam.csv')
df_csv_exam     # 데이터 프레임

# 데이터 프레임을 csv파일로 저장하기
# 1) 데이터 프레임 생성
df_midterm <- data.frame(english = c(90, 80, 60, 70),
                         math = c(50, 60, 100, 20),
                         class = c(1, 1, 2, 2))
df_midterm

# 2) 데이터 프레임을 csv 파일로 저장하기
write.csv(df_midterm, file = 'makefile/df_midterm.csv')

# 3. rda 파일
# 1) R전용 데이터 파일
# 2) 용량이 작아서 빠르게 사용할 수 있따.
# 3) 데이터 프레임을 rda 파일로 저장할 때 는 save()로 저장
# 4) rda 파일을 불러올 떄는 load()로 불러온다.

# 데이터 프레임을 RData파일(*.rda)로 저장하기
save(df_midterm, file = 'makefile/df_midterm.rda')

# rda 파일 불러오기
load('makefile/df_midterm.rda')
df_midterm
#   english math class
# 1      90   50     1
# 2      80   60     1
# 3      60  100     2
# 4      70   20     2

# [정리하기]
# # 1.변수 만들기, 데이터 프레임 만들기
# english <- c(90, 80, 60, 70) # 영어 점수 변수 생성
# math <- c(50, 60, 100, 20) # 수학 점수 변수 생성
# data.frame(english, math) # 데이터 프레임 생성

# # 2. 외부 데이터 이용하기
# # 엑셀 파일
# library(readxl) # readxl 패키지 로드
# df_exam <- read_excel("excel_exam.xlsx") # 엑셀 파일 불러오기
# # CSV 파일
# df_csv_exam <- read.csv("csv_exam.csv") # CSV 파일 불러오기
# write.csv(df_midterm, file = "df_midterm.csv") # CSV 파일로 저장하기
# # Rda 파일
# load("df_midterm.rda") # Rda 파일 불러오기
# save(df_midterm, file = "df_midterm.rda") # Rda 파일로 저장하기


