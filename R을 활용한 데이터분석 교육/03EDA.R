# 1. 패키지 설치하기와 로딩하기 ----
install.packages("readxl")
install.packages("writexl")
install.packages("tidyverse")   # 중급
install.packages("e1071")       # 분포의 모양을 볼 때 ; 왜도, 첨도
library(readxl)
library(writexl)
library(tidyverse)
library(e1071)


# 2. 작업공간 설정하기 ----
setwd("C:/KCISA/")
getwd()


# 3. 데이터 읽어오기 ----
culture <- readxl::read_excel(path      = "culture.xlsx",
                              sheet     = "DM",
                              col_names = TRUE)


# 4. EDA(Exploratory Data Analysis) = 탐색적 데이터 분석 ----
# 표, 그래프를 보고 데이터가 뭘 의미하는지 끄집어내는 단계 -> 철저히 봐야 한다!! ★★★

# 4.1 일변량 질적 자료의 분석 ----
# 일변량 : Uni-Variate
# 하나의 열 = 하나의 변수 = 하나의 Feature = 하나의 Label
# 질적 자료 = 범주형 자료 : 문자 또는 숫자(숫자의 의미 X)

# (1) 표 = 빈도표(Frequency Table) ----
# i.  빈도(Frequency)
# ii. 백분율(Percent) : (빈도/합계)*100

# SRCHWRD_NM
culture %>% 
  dplyr::count(SRCHWRD_NM, sort = TRUE) %>% 
  dplyr::mutate(percent = round((n/sum(n)) * 100, digits = 1)) %>% 
  writexl::write_xlsx(path = "SRCHWRD_NM.xlsx")

# (2) 그래프 ----
# i.  막대그래프
# ii. 원그래프

# LWPRT_CTGRY_NM
culture %>% 
  ggplot2::ggplot(mapping = aes(x = LWPRT_CTGRY_NM)) +
  ggplot2::geom_bar(fill = "purple") +
  ggplot2::theme_classic() +
  ggplot2::labs(title = "하위 카테고리명의 현황",
                x     = "하위 카테고리명",
                y     = "Frequency") +
  ggplot2::theme(plot.title = element_text(size  = 20,
                                           color = "red",
                                           face  = "bold",
                                           hjust = 0.5),
                 axis.title.x = element_text(size = 15,
                                             face = "italic"),
                 axis.title.y = element_text(size = 15,
                                             face = "bold.italic",
                                             angle = 0,
                                             vjust = 0.5)) +
  ggplot2::ggsave(filename = "LWPRT_CTGRY_NM.jpeg",
                  width    = 5,
                  height   = 5,
                  units    = "in")

# 참고 
# units : "in", "cm", "mm"
# "in" : inch


# 4.2 일변량 양적 자료의 분석 ----
# 양적 자료 : 수치형 자료(Numerical Data)
# (1) 표 = 빈도표 ----
# i.  구간의 빈도
# ii. 구간의 백분율

# 최소값, 최대값
min(culture$TOTAL_VALUE)
max(culture$TOTAL_VALUE)

# 범위 : 최대값 - 최소값
RANGE <- max(culture$TOTAL_VALUE) - min(culture$TOTAL_VALUE)

# 구간의 개수 : Sturge's Formula
INTERVAL_N <- 1 + 3.3*log10(length(culture$TOTAL_VALUE))

# 구간의 너비 : 범위 / 구간의 개수
INTERVAL_WIDTH <- RANGE / 13


culture %>% 
  dplyr::mutate(total_group = cut(TOTAL_VALUE,
                                  breaks = seq(from = 50, to = 3690, by = 260),
                                  right = FALSE)) -> culture
View(culture)

culture %>% 
  dplyr::count(total_group, sort = TRUE) %>% 
  dplyr::mutate(percent = round((n/sum(n)) * 100, digits = 1)) %>% 
  writexl::write_xlsx(path = "total_group.xlsx")


# (2) 그래프 ----
# i.  히스토그램(Histogram) ----
culture %>% 
  ggplot2::ggplot(mapping = aes(x = TOTAL_VALUE)) + 
  ggplot2::geom_histogram(fill = "red")

# 구간의 너비 : binwidth = 
culture %>% 
  ggplot2::ggplot(mapping = aes(x = TOTAL_VALUE)) + 
  ggplot2::geom_histogram(binwidth = 100)

# 구간의 개수 : bins = 
culture %>% 
  ggplot2::ggplot(mapping = aes(x = TOTAL_VALUE)) + 
  ggplot2::geom_histogram(bins = 100)

# 다양하게 그려보면서 분석해보는 게 중요하다!

# ii. 상자그림(Boxplot) ----
# 이상치(outlier)가 있는지를 파악하기 위해 작성함
culture %>% 
  ggplot2::ggplot(mapping = aes(y = TOTAL_VALUE)) + 
  ggplot2::geom_boxplot()


# (3) 기술통계량 = 요약통계량 ----
# i. 중심 = 대표값 ----
# : 평균(이상치의 영향을 많이 받음), 절사평균(절삭평균; 양끝단 일부를 제거), 중위수(중앙값; median), 최빈수(최빈값)
culture %>% 
  dplyr::summarise(n           = n(),
                   Mean        = mean(TOTAL_VALUE),
                   TrimmedMean = mean(TOTAL_VALUE, trim = 0.05),
                   Median      = median(TOTAL_VALUE))


# ii. 산포 = 퍼짐 = 다름 : 범위, 사분위범위, 표준편차, 중위수절대편차★★----
# "얼마나 다를까"에 대한 관심을 가져야 한다!!
# 그 다름의 양이 무시해도 될만한 건지, 무시하면 안되는 건지 따져야 한다!
# → 가설 검정
# 차이가 무시할 수 없을 정도의 '필연적'인 것이라면 
# 그 '원인'을 찾는 것이 매우매우 중요하다!

# 평균을 본다는 건 '다름을 고려하지 않겠다'는 강한 의미를 내포하고 있음
# 하지만, 데이터 분석가는 "다름을 고려해야 한다!"
# '평균'은 실제적으로 마케팅에 원하고자 하는 대상에 해당되지 않을 수 있다.

culture %>% 
  dplyr::summarise(Range = max(TOTAL_VALUE, na.rm = TRUE) - min(TOTAL_VALUE, na.rm = TRUE),
                   IQR   = IQR(TOTAL_VALUE),   # InterQuartile Range(3분위수 - 1분위수)
                   SD    = sd(TOTAL_VALUE),
                   MAD   = mad(TOTAL_VALUE))   # 중위수절대편차

# iii. 분포의 모양 : 왜도, 첨도 ----
# 패키지 : e1071
culture %>% 
  dplyr::summarise(SKEW = e1071::skewness(TOTAL_VALUE),
                   KURT = e1071::kurtosis(TOTAL_VALUE))


# 4.3 이변량 자료의 분석(질적 자료 VS 양적 자료) ----
# 이변량    : Bi-Variate
# 다변량    : Multi(ple)-Variate : 3개 이상
# 질적 자료 : 집단

# (1) 집단별 그래프 ----
# i.   집단별 히스토그램 ----
culture %>% 
  ggplot2::ggplot(mapping = aes(x = TOTAL_VALUE)) + 
  ggplot2::geom_histogram() + 
  ggplot2::facet_wrap(~LWPRT_CTGRY_NM)    # 집단 = facet

# ii.  집단별 상자그림 ----
culture %>% 
  ggplot2::ggplot(mapping = aes(y = TOTAL_VALUE)) + 
  ggplot2::geom_boxplot(outlier.color = "red") +  # outlier 색 넣기★
  ggplot2::facet_wrap(~LWPRT_CTGRY_NM)    # 집단 = facet, ~ + 질적자료(집단)

# iii. 집단별 바이올린그림 ----
# 데이터의 분호를 보기 좋게 시각화
culture %>% 
  ggplot2::ggplot(mapping = aes(x    = LWPRT_CTGRY_NM,
                                y    = TOTAL_VALUE,
                                fill = LWPRT_CTGRY_NM)) + 
  ggplot2::geom_violin()




# (2) 집단별 기술통계량 ----
culture %>% 
  dplyr::group_by(LWPRT_CTGRY_NM) %>% 
  dplyr::summarise(n      = n(),
                   Mean   = mean(TOTAL_VALUE),
                   Median = median(TOTAL_VALUE)) %>% 
  dplyr::arrange(desc(Mean)) %>% 
  writexl::write_xlsx(path = "statistics_by.xlsx")


culture %>% 
  dplyr::group_by(LWPRT_CTGRY_NM, SRCHWRD_NM) %>% 
  dplyr::summarise(n      = n(),
                   Mean   = mean(TOTAL_VALUE),
                   Median = median(TOTAL_VALUE)) %>% 
  dplyr::arrange(desc(Mean))    # descending 함수 안에 넣어줌







