## 1.2 row/column 선택, 추가, 삭제
## 1.2.1 row/column 선택
# df['컬럼명'] : 하나의 컬럼을 Series 형식으로 출력
# df[['컬럼명1,',"컬럼명2"]] : 여러 개의 컬럼을 DataFrame 형식으로 출력
# df.loc[row_list,col_list] : 행과 열을 지정하여 출력 (모든 행 또는 열을 출력할 때는 콜론 : 사용
# df.iloc[row위치, col위치] : 행과 열 위치를 지정하여 출력 (index 접근)
# loc :  레이블별 선택을 위한 순전히 레이블 위치 기반 인덱서
# iloc : 위치별 선택을 위한 순수한 정수 위치 기반 인덱싱

import pandas as pd

iris_data = pd.read_csv('C:/adp/2data_handling/data/iris.csv')
iris_data.head(5)

iris_data[['sepal length','sepal width']].head(2)

iris_data.loc[[0,2,4],['sepal length','target']]

example_data = iris_data.loc[4:10,['sepal length','sepal width','target']]
example_data.index = ["사","구","육","칠",8,9,10]
example_data

example_data.loc["사":"칠",:]

example_data.loc[["사", 9],:]

example_data.iloc[0:7, 0:2]

example_data.iloc[0::, 0:2]

## 1.2.2 column 추가 / 삭제
# 컬럼 추가 : df['컬럼명'] = 선언할 값
# 컬럼 삭제 : df.drop(columns = ['컬럼명1', '컬럼명2'], inplace=True)

# 컬럼 추가
iris_data['temp'] = range(0, 150)
iris_data['temp2'] = "iris"
iris_data['count'] = 1

iris_data.head()

# 컬럼 삭제
iris_data = iris_data.drop(columns=['temp','temp2'])
iris_data.tail()

## 1.3 row 추가 / 삭제
# 추가 : df.append(df와 컬럼명이 같은 데이터프레임)
# 행 삭제 : df.drop(인덱스 리스트)

# 결측 데이터 삭제 : df.dropna(inpace=True)
# 중복 데이터 삭제 : df.drop_duplicates()

import numpy as np
temp = pd.DataFrame([[1,1,1,1,1,1],
                     [2,2,2,2,2,np.nan],
                     [1,np.nan,np.nan,np.nan,np.nan,np.nan]
                    ],columns=iris_data.columns)
temp

iris_data = iris_data.append(temp)
iris_data

iris_data.reset_index(drop=True,inplace=True)
iris_data.tail()

## 인덱스로 삭제, 차후 조건문을 이용한 행 삭제
drop_idx = [150,151]
iris_data.drop(drop_idx,inplace=True)
iris_data.tail()

iris_data.info()

## 결측치가 있는 모든 행 삭제
iris_data.dropna(inplace=True)
iris_data

iris_data.info()

## 중복 제거
iris_data[['target','count']].drop_duplicates()

