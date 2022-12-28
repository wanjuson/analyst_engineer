## 4.4 범주형 데이터 전처리하기
# 연속형 변수 : 수치형 변수
# 범주형 변수 : 이산형 혹은 category 등
# 범주형 변수를 표현하는 데 가장 널리 쓰이는 방법 : 원-핫-인코딩(one-hot-encoding)
# 범주형 변수에 있는 원소를 columns로 변경 -> 해당 범주에 속하면 1, 아니면 0 으로 채우는 기법
#
# pd.get_dummies('범주형변수')
# pd.get_dummies(data,columns=['범주형1','범주형2'])

import pandas as pd
import numpy as np

df = pd.read_csv('C:/adp/2data_handling/data/빅분기_X_train.csv', encoding='cp949')
print(df.head())

df.info()

# 4.4.1 범주형변수를 인코딩하기¶
len(df['주구매상품'].unique())
df['주구매상품'].unique()
len(pd.get_dummies(df['주구매상품']).columns)
pd.get_dummies(df['주구매상품']).columns

pd.get_dummies(df['주구매상품'])

## 4.4.2  원본 데이터에서 범주형 변수를 대체하기
df_dum = pd.get_dummies(df,columns=['주구매상품','주구매지점'])
df_dum.info()

pd.concat([df,pd.get_dummies(df['주구매상품']),pd.get_dummies(df['주구매지점'])],axis=1).drop(columns=['주구매상품','주구매지점'])
df['주구매상품']


df2 = pd.read_csv('C:/adp/2data_handling/data/빅분기_X_test.csv', encoding='cp949')
df2

df_dum2 = pd.get_dummies(df2,columns=['주구매상품','주구매지점'])
df_dum2

df_dum2.columns
df_dum.columns[df_dum.columns.isin(df_dum2.columns)==False] # 머신러닝시 더미변수 숫자가 같아야 한다.
df_dum2['주구매상품_소형가전']=0
df_dum2


