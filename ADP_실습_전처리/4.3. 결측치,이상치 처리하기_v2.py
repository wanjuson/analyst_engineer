## 4.3 결측치, 이상치 처리하기
## 4.3.1 결측치 인식
# dataframe.isna()
# 데이터의 요소가 결측치일 경우 TRUE 반환하고, 그렇지 않을 경우 FALSE 반환
# .isna() = .isnull()
# 변수별로 데이터의 각 행에 결측치가 있는지 확인 후 반환
# 합을 구해 결측치의 개수를 쉽게 파악 가능
# 4.3.1.1 결측치가 있는/없는 행 확인
# na가 있는 행들 저장 : df_row_with_na = df[df.isna().any(axis=1)]
# na가 없는 행들 저장 : df_row_without_na = df.dropna()

import pandas as pd
import numpy as np

air = pd.read_csv('C:/adp/2data_handling/data/airquality.csv')
print(air.head())

air.info()

# Ozone 변수에 존재하는 na의 개수 산출
air.isna()
air.isna().sum()
air['Ozone'].isna()  #isna()사용
air[air['Ozone'].isna()]

# Ozone 변수에서 na가 아닌 값과 na 값의 개수 비교
tb = air['Ozone'].isna().value_counts()
tb


## [예제 2]
# airquality 데이터에서 결측치가 하나라도 존재하는 행들을 air_na 변수에 저장하고
# 결측치를 하나도 가지지 않는 행들을 air_com 변수에 저장하기
len(air[air.isna().any(axis=1)])
air_na = air[air.isna().any(axis=1)]
air_na.tail()
# air[air.isna().any(axis=0)] # error

air_com = air.dropna()
air_com.head()


## 결측치 처리
# 결측치 대치법 이해
# 가. 단순 대치법
#
# complete analysis : 결측값이 존재하는 행 삭제
# 평균 대치법 : 관측 또는 실험을 통해 얻어진 데이터의 평균으로 결측치 대치
# 단순확률 대치법 : Hot-deck 방법, nearest neighbor 방법 등
# 나. 다중 대치법
#
# 단순 대치법을 m번 수행해 m개의 가상적 완전 자료를 만듦
# [대치] - [분석] - [결합] 단계

## [예제]
# airquality의 Ozone 변수값이 존재하지 않는 경우, Ozone 변수 값들의 평균으로 대치하기
air.info()
air['Ozone'].mean()
air2 = air

air2['Ozone'] = air2['Ozone'].fillna(air2['Ozone'].mean())
air2

## 4.3.2.4 사이킷런을 활용한 결측치 대치 - KNN
from sklearn.impute import KNNImputer
air = pd.read_csv('C:/adp/2data_handling/data/airquality.csv')
imputer = KNNImputer(n_neighbors = 2)

air_filled = imputer.fit_transform(air)
air_filled

pre_air = pd.DataFrame(air_filled, columns=air.columns)
pre_air

pre_air.isna().sum()

## 4.3.3 이상치 인식
## 4.3.3.1 사분위수
# 데이터명.describe()
# 결측치가 아닌 데이터행의 개수
# 평균/표준편차
# 최소/최댓값
# Q1, Q2, Q3 나타내줌
# IQR을 이용한 이상치 탐색 : 함수 생성

## PIL 패키지 설치가 안됨
# from PIL import Image
# image1 = Image.open("./box_plot.png")
# image1.resize((870,400))

# Ozone 변수에서 이상치를 박스플롯으로 확인
import seaborn as sns
sns.boxplot(x='Ozone', data=air)


# IQR 을 이용한 이상치 탐색 함수
def detect_outliers(df=None, column=None, weight=1.5):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    IQR_weight = IQR * weight
    outlier_idx = df[(df[column] < Q1 - IQR_weight) | (df[column] > Q3 + IQR_weight)].index
    return outlier_idx

# IQR로 이상치를 찾아 인덱스 저장되어 있음
out_index = detect_outliers(df=air, column='Ozone')
out_index

air.loc[out_index,'outlier'] = True
air[air['outlier']==True]

# outlier 대체 (중위 값 혹은 평균값으로)
air.loc[out_index,'Ozone'] = air['Ozone'].median()
air.loc[out_index,'Ozone']

sns.boxplot(x='Ozone', data=air)

out_index = detect_outliers(df=air, column='Ozone')
out_index

# outlier 제거
air_2 = air.drop(out_index).reset_index(drop=True)
air_2

sns.boxplot(x='Ozone', data=air_2)
air_2.boxplot()














