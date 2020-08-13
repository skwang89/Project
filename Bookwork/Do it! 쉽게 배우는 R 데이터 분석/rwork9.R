# rwork9.R start
# <<교재 10장 시작>>


# 텍스트 마이닝
# 형태소 분석 : 명사
# 비정형 데이터 시각화 : wordcloud

# 환경 구축
# 1. 패키지 설치

# 의존성 패키지 설치
install.packages(c('stringr', 'hash', 'tau', 'Sejong', 'RSQLite', 'devtools'), type = "binary")

# github 버전 설치
install.packages("remotes")

# 64bit 에서만 동작합니다.
remotes::install_github('haven-jeon/KoNLP', upgrade = "never", INSTALL_opts=c("--no-multiarch"))

install.packages("vctrs")
library(vctrs)


install.packages("rJava")
install.packages("memoise")
#install.packages("KoNLP")
install.packages("dplyr")

# 2. 패키지 로딩
library(rJava)
library(memoise)
library(KoNLP)
library(dplyr)

# java 폴더 경로 설정
Sys.setenv(JAVA_HOME="C:/Program Files/Java/jre1.8.0_231/")


# 사전 설정하기 
useNIADic()

# 데이터 불러오기
# 인코딩이 ANSI 타입으로 저장된 파일은 encoding = "CP949" 읽어옴 
txt <- readLines("data/hiphop.txt", encoding = "UTF-8")
txt
# 인코딩이 UTF-8 타입으로 저장된 파일은 encoding = "UTF-8" 읽어옴 
txt <- readLines("data/hong.txt", encoding = "UTF-8")
head(txt)
View(txt)

# 특수문자 제거
install.packages("stringr")
library(stringr)

# 특수 문자를 공백으로 수정
txt <- str_replace_all(txt, "\\W", " ")

# 명사 추출
nouns <- extractNoun(txt)
nouns

# 추출한 명사 list를 문자열 벡터로 변환, 단어별 빈도 구하기
wordcount <- table(unlist(nouns))
wordcount

# 데이터 프레임으로 변환
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
head(df_word)

# 변수명 수정 : Var1 -> word, Freq -> freq
df_word <- rename(df_word,
                  word = Var1,     
                  freq = Freq)
head(df_word)


# 2글자 이상 단어 추출
df_word <- filter(df_word, nchar(word) >= 2)
df_word


# 빈도수가 높은 단어 상위 20개 추출
top20 <- df_word %>% 
  arrange(desc(freq)) %>%   # 내림차순 정렬 
  head(20)
top20


# 워드 클라우스 만들기
#  패키지 설치
install.packages("wordcloud")

# 패키지 로딩
library(wordcloud)
library(RColorBrewer)

# 단어 색상 목록 생성
pal <- brewer.pal(8, "Dark2")
# pal <- brewer.pal(9, "Blues")


# 난수 고정
set.seed(1234)

# 워드 클라우드 만들기
wordcloud(words = df_word$word,    # 단어
          freq = df_word$freq,     # 빈도
          min.freq = 2,            # 최소 2단어 이상 
          max.words = 200,         # 최대 표현 단어수
          random.order = F,        # 고빈도 단어를 중앙배치 
          rot.per = .1,            # 회전 단어 비율 
          scale = c(3, 0.2),       # 단어 크기 범위 : 원모양 
          colors = pal)            # 색상표 


#-------------------------------------------------------------
# 국정원 트윗 텍스트 마이닝

# 데이터 로딩
twitter <- read.csv("data/twitter.csv",      
                    header = T,              # 헤드 사용
                    stringsAsFactors = F,    # 문자로 읽어옴 
                    fileEncoding = "utf-8")  # utf-8로 읽어옴 
twitter

# 변수명 수정 
twitter <- rename(twitter,
                  no = 번호,
                  id = 계정이름,
                  date = 작성일,
                  tw = 내용 )
twitter


# 특수 문자 제거
library(stringr)

twitter$tw <- str_replace_all(twitter$tw, "\\W", " ")
head(twitter$tw)

# 명사 추출
nouns <- extractNoun(twitter$tw)
nouns

# 추출한 명사 list를 문자열 벡터로 변환, 단어별 빈도 구하기
wordcount <- table(unlist(nouns))
wordcount

# 데이터 프레임으로 변환
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
df_word

# 변수명 수정 : Var1 -> word, Freq -> freq
df_word <- rename(df_word,
                  word = Var1,
                  freq = Freq)
head(df_word)

# 2글자 이상의 단어 추출
df_word <- filter(df_word, nchar(word) >= 2)
df_word

# 빈도수가 높은 상위 20개 단어 추출
top20 <- df_word %>% 
  arrange(desc(freq)) %>%  #빈도수를 기준으로 내림차순 정렬 
  head(20)
top20

# top20 단어를 빈도 막대 그래프로 출력
library(ggplot2)

ggplot(data = top20, aes(x=word, y=freq)) + geom_col()


# 워드 클라우드 만들기
# 패키지 로딩 
library(wordcloud)
library(RColorBrewer)

# 색상표
pal <- brewer.pal(8, "Dark2")
# pal <- brewer.pal(8, "Blues")

# 난수 고정
set.seed(1234)

# 워드클라우드
wordcloud(words = df_word$word,
          freq = df_word$freq,
          min.freq = 1,
          max.words = 300,
          random.order = F,
          rot.per = .1,
          scale = c(6, 0.1),
          colors = pal )



# <<교재 10장 끝>>
# rwork9.R end
