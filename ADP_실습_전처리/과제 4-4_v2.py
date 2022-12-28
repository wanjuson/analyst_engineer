## 과제 5
# 타이타닉 데이터의 결측치를 확인하세요.
# age의 결측값은 중위 값으로 대체하세요.
# embark_town의 결측 값은 최빈값으로 대체하세요.
# embarked 결측치는 embark_town의 첫 글자로 대체하세요
# deck 결측치는 backfill로 5개만 대체하세요. limit = 5
# df_t내에 범주형 변수를 원 핫 인코딩하여 더미변수로 만드세요

import pandas as pd
import numpy as np

df = pd.read_csv('C:/adp/2data_handling/data/titanic.csv')


## 1. 타이타닉 데이터의 결측치를 확인하세요
df.info()
df[df.isna().any(axis = 1)]

## 2. age의 결측값은 중위 값으로 대체하세요.
sum(df.age.isna())
df.age.median()
df.age = df.age.fillna(df.age.median())
sum(df.age.isna())

## 3. embark_town의 결측 값은 최빈값으로 대체하세요.
sum(df.embark_town.isna())
df.embark_town = df.embark_town.fillna(df.embark_town.describe()['top'])
sum(df.embark_town.isna())

## 4. embarked 결측치는 embark_town의 첫 글자로 대체하세요
sum(df.embarked.isna())
df['embarked'] = df['embarked'].fillna(df['embark_town'].str[0])
sum(df.embarked.isna())

## 5. df_t내에 범주형 변수(embark_town,class) 를 원 핫 인코딩하여 더미변수로 만드세요
df2 = df
df2 = pd.get_dummies(df2, columns = ['embark_town', 'class'])
df2 = pd.get_dummies(df2, columns = ['embark_town', 'class'])
df2.info()



