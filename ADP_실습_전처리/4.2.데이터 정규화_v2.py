## 4.3 데이터 표준화, 정규화
# sklearn에서는 다양한 종류의 스케일러를 제공함
#
# 데이터 변환이 필요한 이유
# 데이터의 단위와 평균과 표준편차가 모두 다르다면, 우리가 학습시키는 머신이 그 단위를 인지하지 못함
# 즉, 우리는 머신에 학습을 시킬 때, 유사한 단위를 맞춰 줘야 합니다.
# 또한 통계는 표본집단의 평균과 분산으로 모집단의 분산을 설명하는 학문인데, 차원마다 범위가 다르면, 스케일이 큰 집단의 영향을 많이 받습니다. 그렇기 때문에 차원의 스케일을 맞춰줄 필요가 있습니다.

import pandas as pd
import numpy as np

# 4.2.1 StandardScaler
# 기본 스케일. 평균과 표준편차 사용
# 평균을 0, 분산을 1로 모든 데이터를 변환하는 방법
from sklearn.preprocessing import StandardScaler
data = [[0, 0], [0, 0], [1, 1], [1, 1]]
scaler = StandardScaler()

scaler.fit(data) # fit으로 수식 생성
print(scaler.mean_)
print(scaler.var_)
scaler.transform(data) # transform 으로 수식 적용


## 실스2
df_iris = pd.read_csv('C:/adp/2data_handling/data/iris.csv')
scaler = StandardScaler()
scaler.fit(df_iris.iloc[:,0:4]) # 명목형, 범주형 변수는 StandardScaler 불가
df_iris.iloc[:,0:4]

scaler.mean_
scaler.var_

scaler.transform(df_iris.iloc[:,0:4]) # 정규화
pd.DataFrame(scaler.transform(df_iris.iloc[:, 0:4]), columns = df_iris.columns[0:4])


## 4.2.2 MinMaxScaler
# 최대/최소값이 각각 1, 0이 되도록 스케일링
#
# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
# X_scaled = X_std * (max - min) + min
from sklearn.preprocessing import MinMaxScaler
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
scaler2 = MinMaxScaler()
scaler2.fit(data)
scaler2.transform(data)


scaler3 = MinMaxScaler()
scaler3.fit(df_iris.iloc[:,0:4])
scaler3.transform(df_iris.iloc[:,0:4])

## model에 fit 된 데이터를 기반으로 학습되며, 추가 데이터에는 비율이 적용됨
print(scaler3.transform([[2 ,2 ,40 ,450]]))

scaler3.fit_transform(df_iris.iloc[:,0:4])
scaler2.fit_transform(data)

## 4.2.3 MaxAbsScaler
# 이 추정기는 훈련 세트에 있는 각 기능의 최대 절대값이 1이 되도록 각 기능을 개별적으로 확장하고 변환합니다.
# 데이터를 이동/중앙에 배치하지 않으므로 희소성을 파괴하지 않습니다.
class sklearn.preprocessing.MaxAbsScaler(*, copy=True)


from sklearn.preprocessing import MaxAbsScaler

X = [[1., -1., 2.],
     [2., 0., 0.],
     [0., 1., -1.]]
transformer = MaxAbsScaler().fit(X)
transformer
MaxAbsScaler()
transformer.transform(X)


## 4.2.4 RobustScaler
# 중앙값(median)과 IQR(interquartile range) 사용. 아웃라이어의 영향을 최소화
# 이상값에 대해 강력한 통계를 사용하여 기능을 확장합니다.
# 이 스케일러는 중앙값을 제거하고 분위수 범위(기본값은 IQR: 사분위수 범위)에 따라 데이터를 조정합니다.
# IQR은 1사분위수(25분위수)와 3사분위수(75분위수) 사이의 범위입니다.
# 데이터 세트의 표준화는 많은 기계 학습 추정기의 공통 요구 사항입니다.
# 일반적으로 이것은 평균을 제거하고 단위 분산으로 스케일링하여 수행됩니다.
# 그러나 이상치는 종종 표본 평균/분산에 부정적인 영향을 미칠 수 있습니다.
# 이러한 경우 중앙값과 사분위수 범위가 더 나은 결과를 제공하는 경우가 많습니다.

from sklearn.preprocessing import RobustScaler
X = [[ 1., -2.,  2.],
    [ -2.,  1.,  3.],
    [ 4.,  1., -2.]]
transformer = RobustScaler().fit(X)
transformer
transformer.transform(X)

# 다른방법 실습
transformer2 = RobustScaler()
transformer2.fit_transform(X)


