## 날짜 데이터 전처리 과제
# 데이터 : "6.세종시_오피스텔(매매)_실거래가.csv"

import pandas as pd
import numpy as np
import datetime as datetime
# from datetime import datetime
# from datetime import timedelta

df_sejong = pd.read_csv('C:/adp/2data_handling/data/6.세종시_오피스텔(매매)_실거래가.csv')
df_sejong.info()
df_sejong.tail()

### 아래와 같이 계약년월을 datetime으로 변경하세요.
df_sejong['계약년월일'] = df_sejong['계약년월']*100 + df_sejong['계약일']
df_sejong['계약년월일'] = df_sejong['계약년월일'].astype(str)
df_sejong.info()

pd.to_datetime(df_sejong['계약년월일'], format = "%Y-%m-%d")
df_sejong['계약년월일'] = pd.to_datetime(df_sejong['계약년월일'], format = "%Y-%m")
df_sejong.tail()

## 계약년월을 아래와 같이 문자열로 다시 변경하세요.
df_sejong['계약년월일2'] = df_sejong['계약년월일']
df_sejong['계약년월일2'] = df_sejong['계약년월일2'].dt.strftime("%Y_%m_%d")

## 6월 데이터만 추출해보세요
df_sejong[df_sejong['계약년월일'].dt.strftime("%m") == '06']

## 날짜순으로 데이터를 정렬해보세요
df_sejong.sort_values(['계약년월일'], ascending=True)










