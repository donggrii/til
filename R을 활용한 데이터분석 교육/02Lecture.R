# 데이터 분석의 전반적인 흐름
# a. 데이터 읽어오기
# b. 데이터 분석에 맞도록 데이터를 처리하고 변환하기
# c. 데이터 시각화
# d. 모형 만들기
# e. 데이터 분석 보고서 작성
# f. 의사결정(Communication)


# Ctrl + Shift + n : 새로운 R script 만들기
# 1. 패키지 설치하기와 로딩하기 ----
install.packages("readxl")
install.packages("writexl")
install.packages("tidyverse")   # 중급
library(readxl)
library(writexl)
library(tidyverse)


# 2. 작업공간 설정하기 ----
setwd("C:/KCISA/")
getwd()


# 3. 데이터 읽어오기 ----
culture <- readxl::read_excel(path      = "culture.xlsx",
                              sheet     = "DM",
                              col_names = TRUE)


# 4. 데이터 전체 보기 ----
# View(data)
View(culture)


# 5. 데이터 일부 보기 ----
# 콘솔에 출력이 됨
# 5.1 head(data, n = 6) ----
head(culture)
head(culture, n = 10)


# 5.2 tail(data, n = 6) ----
tail(culture)
tail(culture, n = 10)


# 6. 데이터의 구조(Structure) ----
# dplyr::glimpse(data)
# <dbl> : double, <chr> : character
dplyr::glimpse(culture)



# 7. 입력오류 체크하기 ----
# summary(data)
summary(culture)

# summary에서 "문자열"에 대한 내용은 나오지 않음
# vector를 factor로 바꿔서 문자열의 내용도 summary에 나오도록 만들기
# 해당 문자열 범주에서의 각각 빈도수 출력
culture$SRCHWRD_NM     <- as.factor(culture$SRCHWRD_NM)
culture$UPPER_CTGRY_NM <- as.factor(culture$UPPER_CTGRY_NM)
culture$LWPRT_CTGRY_NM <- as.factor(culture$LWPRT_CTGRY_NM)


# 8. 데이터의 속성 ----
# 데이터 : 2차원 구조의 데이터
# 행과 열로 구성되어 있음
# data.frame, tibble, data.table(데이터 양이 너무 클 때 table로 변환; 속도 빠름)
# 참고 : 패키지 중 data.table이 있음
# 참고 : SQL(DB와 바로 커뮤니케이션하는 것; 속도 빠름)

# 8.1 행의 개수 ----
# nrow(data)
nrow(culture)

# 8.2 열(Column) = 변수(Variable) = Feature = Label ----
# ncol(data)
ncol(culture)

# 8.3 열의 이름 ----
# colnames(data)
colnames(culture)


# 9. 데이터 슬라이싱(Data Slicing) ----
# 9.1 열 ----
# dplyr::select(data, variable)

# Ctrl + Shift + m : %>%(Pipe; data를 function 안에 넣어주는 역할)
# data %>% dplyr::select(variable)   # 중급

# data %>% function()
# (1) x %>% f() => f(x)
# (2) x %>% f(y) => f(x,y)
# (3) x %>% f()
#       %>% g() => g(f(x))
culture %>% 
  dplyr::select(RANK)

culture %>% 
  dplyr::select(RANK, SCCNT_SM_VALUE)

culture %>% 
  dplyr::select(RANK:SCCNT_SM_VALUE)

culture %>% 
  dplyr::select(-RANK)

culture %>%
  dplyr::select(-c(RANK, SCCNT_SM_VALUE))

# 변수명에 "특정한 패턴"이 있는 경우----
# i. 변수명에 'P'라는 문자가 있는 경우 : contains
culture %>%
  dplyr::select(contains("P"))

# ii. 변수명이 'S'라는 문자로 시작하는 경우 : starts_with
culture %>% 
  dplyr::select(starts_with("S"))

# iii. 변수명이 'E'라는 문자로 끝나는 경우 : ends_with
culture %>% 
  dplyr::select(ends_with("E"))


# 9.2 행 ----
# dplyr::filter(data, 조건)
# data %>% dplyr::filter(조건)  # 중급

# (1) RANK가 5이하인 data
culture %>% 
  dplyr::filter(RANK <= 5)

# (2) LWPRT_CTGRY_NM이 "연극"인 data
culture %>% 
  dplyr::filter(LWPRT_CTGRY_NM == "연극")

# (3) RANK가 5이하이고, LWPRT_CTGRY_NM은 "연극"인 data
# , 가 & 역할
culture %>% 
  dplyr::filter(RANK <= 5, LWPRT_CTGRY_NM == "연극")

# (4) RANK가 5이하이거나 또는 LWPRT_CTGRY_NM은 "연극"인 data
culture %>% 
  dplyr::filter(RANK <= 5 | LWPRT_CTGRY_NM == "연극") %>%
  View()


# 9.3 행과 열 ----
# RANK가 5이하이고, LWPRT_CTGRY_NM은 "연극"인 data의
# 'E'라는 문자로 끝나는 열
# 행과 열을 슬라이싱할 때는 select(열)보다 filter(행)이 항상 먼저 나와야 한다!
culture %>%
  dplyr::filter(RANK <= 5, LWPRT_CTGRY_NM == "연극") %>% 
  dplyr::select(ends_with("E")) -> culture2

# Pipe를 쓰는 게 왜 좋을까?!
# (1) 단계별로 어떤 작업을 하는지 나타낼 수 있고, 
# (2) 중간중간에 데이터를 저장할 필요가 없기 때문에!


# 10. 새로운 변수 만들기 ----
# dplyr::mutate(new_variable = )
# 10.1 연산 ----
culture %>% 
  dplyr::mutate(TOTAL_VALUE = MOBILE_SCCNT_VALUE + PC_SCCNT_VALUE + SCCNT_SM_VALUE) -> culture
# "-> culture"로 해야 변수에 저장까지 된다! 
# %>% 은 콘솔창에서 보여주는 것까지

# 10.2 변환 ----
# <Box-Cox Transformation>
# (1) 로그 변환
# (2) 루트 변환
# (3) 역수 변환
# 대칭을 확보하기 위해서
culture %>% 
  dplyr::mutate(total_log10   = log10(TOTAL_VALUE),
                total_root    = sqrt(TOTAL_VALUE),
                total_inverse = 1/TOTAL_VALUE) -> culture

# 10.3 범주 줄이기 ----
# ggplot2 패키지에서 제공하는 diamonds 데이터 사용
summary(diamonds)
dplyr::glimpse(diamonds)

# (1) 범주형 자료 ----
# i. 5개의 범주를 갖는 cut을 2개의 범주를 갖는 cut_group1 만들기
diamonds %>% 
  dplyr::mutate(cut_group1 = ifelse(cut == "Ideal", 
                                    "Ideal", 
                                    "NonIdeal")) -> diamonds

diamonds$cut_group1 <- as.factor(diamonds$cut_group1)
summary(diamonds)

# ii. 5개의 범주를 갖는 cut을 3개의 범주를 갖는 cut_group2 만들기
diamonds %>% 
  dplyr::mutate(cut_group2 = ifelse(cut == "Ideal",
                                    "Ideal",
                                    ifelse(cut == "Premium",
                                           "Premium",
                                           "ETC"))) -> diamonds
diamonds$cut_group2 <- as.factor(diamonds$cut_group2)
summary(diamonds)

# (2) 수치형 자료 ----
# i. 수치형 자료를 2개의 범주를 갖는 범주형 자료로 만들기
diamonds %>% 
  dplyr::mutate(carat_group1 = ifelse(carat >= 1,
                                      "Heavy",
                                      "Not Heavy")) -> diamonds
diamonds$carat_group1 <- as.factor(diamonds$carat_group1)

# ii. 수치형 자료를 3개의 범주를 갖는 범주형 자료로 만들기
# carat이 0이상~2미만이면 "Light", 2이상~4미만이면 "Medium", 4이상~6미만이면 "Heavy"를 갖는 carat_group2 변수
diamonds %>% 
  dplyr::mutate(carat_group2 = cut(carat,
                                   breaks = c(0, 2, 4, 6),
                                   right  = FALSE,
                                   labels = c("Light", "Medium", "Heavy"))) -> diamonds

summary(diamonds)

# (3) 대체(Imputation) ----
# 결측치를 대체하는 여러가지 방법이 있지만, 여기서는 결측치를 제외한 '평균'으로 대체하는 방법
diamonds %>% 
  dplyr::mutate(carat_nonna = ifelse(is.na(carat),
                                     mean(carat, na.rm = TRUE),
                                     carat)) -> diamonds

# 메모리에 있는 데이터 목록 보기
# ls() : list segment
ls()

# 메모리에 있는 데이터 삭제하기
# (1) 일부 데이터 삭제하기
# rm(데이터1, 데이터2, 데이터3)

# (2) 모든 데이터 삭제하기
# rm(list = ls())


# 11. 데이터 정렬하기 ----
# dplyr 패키지의 arrange() 함수
# (1) carat을 기준으로 오름차순
diamonds %>% 
  dplyr::arrange(carat)

# (2) carat을 기준으로 내림차순
diamonds %>% 
  dplyr::arrange(desc(carat))

# (3) cut을 기준으로 오름차순, carat을 기준으로 오름차순
diamonds %>% 
  dplyr::arrange(cut, carat)

# (4) cut을 기준으로 오름차순, carat을 기준으로 내림차순
diamonds %>% 
  dplyr::arrange(cut, desc(carat))


# 12. 데이터 합치기 ----
# (1) binding ----
# i. 행을 기준으로 binding
# 두 개 이상의 데이터의 변수명, 변수명의 위치가 동일해야 함
diamonds %>% 
  dplyr::slice(1:5) %>% 
  dplyr::select(x:z) -> d1

diamonds %>% 
  dplyr::slice(6:10) %>% 
  dplyr::select(x:z) -> d2

d3 <- dplyr::bind_rows(d1, d2)

# ii. 열을 기준으로 binding
diamonds %>% 
  dplyr::slice(1:5) %>% 
  dplyr::select(carat, cut) -> d4

diamonds %>% 
  dplyr::slice(1:5) %>% 
  dplyr::select(x:z) -> d5

d6 <- dplyr::bind_cols(d4, d5)


# (2) mutating joins ----
# 데이터에 동일한 이름의 primary key가 있어야 함

d7 <- data.frame(id = 1:3, gender = c("M", "M", "F"))
d8 <- data.frame(id = c(1, 2, 4, 5), age = c(10, 20, 40, 50))

# i. inner join
d9 <- dplyr::inner_join(d7, d8)

# ii. full join
d10 <- dplyr::full_join(d7, d8)

# iii. left join
d11 <- dplyr::left_join(d7, d8)

# iv. right join
d12 <- dplyr::right_join(d7, d8)


# 13. 텍스트 데이터 전처리 ----
# stringr 패키지 활용
# (1) 문자열 잘라내기 ----
song <- "Yesterday all my troubles seemed so far away"
stringr::str_sub(string = song, start = 1, end = 9)

# (2) 문자열 나누기 ----
stringr::str_split(string = song, pattern = " ")

# (3) 문자열 바꾸기 ----
song <- "Yesterday all my troubles seemed so far away 1234!!!"
stringr::str_replace_all(string      = song,
                         pattern     = "Yesterday",
                         replacement = "Today")

stringr::str_replace_all(string      = song,
                         pattern     = "[:digit:]",
                         replacement = " ")

stringr::str_replace_all(string      = song,
                         pattern     = "[:punct:]",
                         replacement = " ")

# (4) 공백 제거하기 ----
# 문자열 양 끝에 있는 공백 제거
song <- " Yesterday all my troubles seemed so far away "
stringr::str_trim(string = song, side = "left")
stringr::str_trim(string = song, side = "right")
stringr::str_trim(string = song, side = "both")



