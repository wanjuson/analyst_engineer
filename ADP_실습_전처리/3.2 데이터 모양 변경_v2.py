## 3.2 데이터 모양 변경
# 3.2.1 데이터 재구조화(melt)
# pd.melt(df, id_vars=['A', 'D'], value_vars=['B', 'E'],
# var_name='myVarname', value_name='myValname', ignore_index=False)

import pandas as pd
import numpy as np

df_student = pd.DataFrame({'id':['S01', 'S02', 'S03', 'S04','S05'],
                        'kor':[80,75,56,69,90],
                         'math' :[84,70,90,60,45],
                         'eng' : [55,90,85,90,80]})
df_student
df_student.info() # object 명목형 또는 범주형

# melt
melt_st= pd.melt(df_student, id_vars=['id'], value_vars=['kor','math','eng'],
                 var_name='subject', value_name='score', ignore_index=True ) # ignore_index Default가 True임
melt_st

## 3.2.2 데이터 재구조화(pivot_table)
# pd.pivot_table(data, index, columns, values, aggfunc, margins)
pd.pivot_table(melt_st, index='id', columns='subject', values='score').head(10)

df_fruits = pd.read_csv('C:/adp/2data_handling/data/Fruits.csv')
df_fruits

melt_fruits = pd.melt(df_fruits, id_vars = ['Fruit'], value_vars=['Sales','Expenses','Profit'])
melt_fruits

melt_fruits2 = pd.melt(df_fruits, id_vars = ['Fruit'], value_vars=['Year','Location'])
melt_fruits2


melt_fruits.pivot_table(index=['Fruit'], columns='variable', values='value', aggfunc= 'mean', margins=False)

melt_fruits.pivot_table(index=['variable'], columns='Fruit', values='value', aggfunc='sum', margins=True)
# margins : 전체합계 표시 여부


# 3.2.3 데이터 행, 열 변경(transpose)
# 데이터의 행, 열 변경
df_fruits
df_fruits.transpose()

melt_fruits.pivot_table(index=['Fruit'], columns='variable', values='value', aggfunc='sum', margins=True)
melt_fruits.pivot_table(index=['Fruit'], columns='variable', values='value', aggfunc='sum', margins=True).transpose()













df_iris.groupby(['target']).sum()
df_iris.groupby(['target']).mean()

df_iris.groupby(['sepal length']).mean() # 집계가 될수없는 변수는 삭제된다.

df_iris.target.unique()
df_iris.groupby('target').mean().reset_index()

# Q1. iris 데이터에서 종별 Sepal.Width의 평균 구하기
df_iris.groupby('target').mean()[['sepal width']]
df_iris[['target', 'sepal width']].groupby('target').mean()

# Q2. iris 데이터에서 종별 Sepal.Width와 Petal.Width의 평균을 구해보자
avg2 = df_iris.groupby('target').mean()[['sepal width', 'petal width']]
avg2


## 3.1.2 범주형변수의 도수분포표, 이원분할표
## 3.1.2.1 기준이 하나일 때 도수분포표
# np.unique(df['기준열'], return_counts=True)
# pd.Series(df['기준열']).value_counts()

# Titanic 데이터 불러오기
df_t = pd.read_csv('C:/adp/2data_handling/data/titanic.csv')
df_t['survived'].value_counts()

# pandas를 이용한 도수분포표
class_count = df_t['class'].value_counts()
class_count

pd.DataFrame(class_count)

df_t['embark_town'].value_counts() # null은 제외되고 count됨

## 3.1.2.2 기준이 두개일 때
# pd.crosstab(Series1, Series2, dropna = , nomalize = )  
# dropna = True이면, 항목이 모두 NaN인 열은 포함하지 않음 

# Titanic 에서 좌석등급과 생존여부의 관계를 살펴보기 위해 Class 변수에 따른 Survived 변수의 도수를 표 형태로 나타내기
pd.DataFrame(df_t[['class','survived']].value_counts())

pd.crosstab(df_t['class'],df_t['survived'], dropna=True)

## 3.1.2.3 범주형 변수에 대한 상대도수비율
# pd.crosstab(index,columns, dropna = , normalize = )
# normalize = True이면 모든 값에 대해 정규화
#             'index'를 전달하면 행에 대해 정규화
#             'columns'를 전달하면 열별로 정규화
# Titanic 데이터의 sex 변수는 성별을 나타냄.
# sex 변수에 따른 생존여부의 관계를 전체에 대한 비율, 행별비율, 열별 비율로 살피기

pd.crosstab(df_t['sex'], df_t['survived'])
pd.crosstab(df_t['sex'], df_t['survived'], dropna=True)

pd.crosstab(df_t['sex'], df_t['survived'], normalize=True) # 비율
0.090909+0.261504+0.525253+0.122334

pd.crosstab(df_t['sex'], df_t['survived'],normalize = 1)
pd.crosstab(df_t['sex'], df_t['survived'],normalize = 'columns')

pd.crosstab(df_t['sex'], df_t['survived'],normalize = 0)
pd.crosstab(df_t['sex'], df_t['survived'],normalize = 'index')

























