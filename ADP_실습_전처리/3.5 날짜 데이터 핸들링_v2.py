## 날짜 데이터 핸들링
# 날짜 데이터 다루기
# 날짜와 시간을 다루기 위해서는 datetime 모듈을 이용한다.

# datetime 모듈

# 시간과 날짜를 표현하는 모듈
#datetime.today()	현재 날짜와 시간 산출
#datetime.today().year/month/day/hour	현재 연도/월/일/시각 산출
#datetime.strptime('날짜 문자열', '포맷')	문자열 데이터를 날짜 형식으로 변환
#datetime객체.strftime('포맷')	날짜 데이터를 원하는 형식으로 변환

# strftime() 메서드에 사용되는 서식
# %d	0을 채운 10진수 표기로 날짜를 표시
# %m	0을 채운 10진수 표기로 월을 표시
# %y	0을 채운 10진수 표기로 2자리 년도
# %Y	0을 채운 10진수 표기로 4자리 년도
# %H	0을 채운 10진수 표기로 시간 (24시간 표기)
# %I	0을 채운 10진수 표기로 시간 (12시간 표기)

import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta

# df_sejong = pd.read_csv('C:/adp/2data_handling/data/6.세종시_오피스텔(매매)_실거래가.csv')

# [예제]
# 현재 날짜와 시간 데이터를 생성하고, 각각 다른 변수에 저장하여 데이터 형식을 확인하라
today = datetime.today().strftime('%Y-  dwd   %m  -dwd %d')
print("today :", today)
print("today 변수 type :", type(today),'\n')

todaytime = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print("todaytime :", todaytime)
print("todaytime 변수 type :", type(todaytime))

datetime.today()
todaytime1 = todaytime.split(" ")[0]
todaytime1
todaytime.split(" ")[0]
todaytime.split(" ")[1]

# [예제]
# 문자열 데이터를 다시 날짜 형식으로 변환하자
datetime.strptime(todaytime1, '%Y-%m-%d')

# [예제]
# 현재 시간을 구하고 이를 time 변수에 저장하라
# 현재 시간의 연/월/일/시간/요일을 구하라
time = datetime.today()

print("연도 :", time.strftime('%Y'), "&", time.year)
print("월 :", time.strftime('%m'), "&", time.month)
print("일 :", time.strftime('%d'), "&", time.day)
print("시간 :", time.strftime('%H'), "&", time.hour)
print("요일 :", time.strftime('%A'), "&", time.weekday())

## 3.5.2 날짜 데이터의 연산
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# 두 날짜와 시간 사이의 차이를 계산할 때 사용함

# [예제] 현재 날짜로부터 100일 후의 날짜를 구하라
timedelta(days=100)

from datetime import timedelta

time = datetime.today()
print(time + timedelta(days=100)) # 날짜형
print((time - timedelta(days=100)).strftime('%Y-%m-%d %H:%M:%S')) # 문자열

## 3.5.3 데이터프레임 날짜 데이터 핸들링
# 3.5.3.1 문자열 => 날짜데이터로 변환
# pd.to_datetime(df['컬럼명'], format="%Y%m%d")
df_pur = pd.read_csv('C:/adp/2data_handling/data/구매내역.csv')
df_pur.tail()
df_pur.info()

## int => str 형식으로 변환
df_pur['datetime'] = df_pur['datetime'].astype(str)

df_pur.info()

## datetime으로 형변환
df_pur['datetime2'] = pd.to_datetime(df_pur['datetime'], format = "%Y%m%d")
df_pur.info()

# month 6,7,8 check
df_pur.datetime2.dt.month
df_pur[df_pur.datetime2.dt.month.isin([6,7,8])]

df_pur.info()

## 3.5.3.2 날짜데이터 => 문자열로 변환
# timeSeries.dt.strftime("%Y-%m-%d")
df_pur.info()
df_pur['datetime2'].dt.strftime("%Y-%m-%d")

df_pur['datetime2'].dt.strftime("%m") # Month만 추출










