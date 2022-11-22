## EDA 및 시각화를 시작하기에 앞서
# 이 장에서는 matplotlib과 seaborn 라이브러리를 이용하여 데이터를 시각화하는 기술을 습득해야 합니다.
# 데이터 전처리를 진행하였어도, 데이터가 의미하는 것을 온전히 파악하기는 어렵습니다.
# 데이터를 보다 쉽게 이해하고 설명하기 위해서 시각화를 할 수 있어야합니다.

# ADP 시험에서는 시각화 문제가 출제됩니다.

## 산점도
# 두 개의 연속형 변수간의 관계를 알아볼 수 있도록 좌표평면 상에 관측점을 찍어 나타낸 그래프
# 좌표형면 상의 관측점은 두 변수를 의미하는 x, y의 점으로 나타냄
# 산점도 그리기 기본
#
# plt.scatter(x, y, c, s, alpha)
# x, y : x축과 y축
# c: 색
# s: 마커의 면적
# alpha: 마커색의 투명도


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# [예제]
# cars93데이터의 length와 weight 변수에 대한 산점도 그리기

cars = pd.read_csv('C:/adp/2data_handling/data/Cars93.csv', encoding='cp949')
print(cars.head())

cars[['Length','Weight']]

plt.scatter(x=cars['Length'], y=cars['Weight'], c = 'b', s=100, alpha=0.5)
plt.show()

# 5.1 산점도 함수 옵션
# 5.1.1 축이름, 그래프 제목
# plt.xlabel('x축 이름')
# plt.ylabel('y축 이름')
# plt.title('그래프 제목', fontdict, loc, pad)
# fontdict 은 딕셔너리형태로 폰트에 대한 설정을 입력함
# fontsize 는 숫자단위를 입력하거나 'smaller', 'x-large' 등의 상대적인 설정 가능
# fontweight 는 'normal', 'bold', 'heavy', 'light', 'ultrabold', 'ultralight' 설정 가능
# loc는 위치. "left", "center", "right" 중 선택 가능
# pad는 타이틀과 그래프와의 간격(오프셋)을 포인트단위로 설정

# [예제]
# Cars93의 Length와 Weight 변수에 대한 산점도에 제목과 축 이름을 지정하기
plt.title('Cars93', loc='right', pad=20) ## 오른쪽위
title_font = {
    'fontsize':16,
    'fontweight': 'bold'
}
plt.scatter(x=cars['Length'], y=cars['Weight'], alpha=0.5)
plt.xlabel("Length")
plt.ylabel("Weight")
plt.title('Cars93', fontdict = title_font, loc='left', pad=20) ## 왼쪽 위 타이틀
plt.show()

# 5.2 좌표축 범위
# plt.axis([xmin, xmax, ymin, ymax])
# 입력값이 없으면 데이터에 맞게 자동으로 범위를 지정해줌

# [예제]
# Cars93의 Length와 Weight 변수에 대해 각각 최솟값, 최댓값을 구하고 적절한 축 범위를 지정하여 산점도 그리기

# length와 weight의 범위 구하기
a, b = cars['Length'].min(), cars['Length'].max()
print("Length의 최소값: %d, 최댓값: %d"%(a, b))
print('\n')
c, d = cars['Weight'].min(), cars['Weight'].max()
print("Weight의 최소값: %d, 최댓값: %d"%(c, d))

## x축과 y축 범위를 지정하여 산점도 그리기
# x축 범위 (130, 230), y 축 범위 (1600, 4400)으로 지정
plt.scatter(x=cars['Length'], y=cars['Weight'], alpha=0.5)
plt.axis([0, 230, 0, 4400])

title_font = {
    'fontsize':20,
    'fontweight': 'bold'
}

plt.xlabel("Length")
plt.ylabel("Weight")
plt.title('Cars93', fontdict = title_font, loc='left', pad=20)
plt.show()

## 산점도 활용
cars.tail()

# 5.3 범주별로 색과 스타일을 구분하기
# 그리기
import seaborn as sns #범주형 변수를 나타내기 좋음 seaborn
sns.scatterplot(x='Length',
               y='Weight',
               hue='AirBags',  #범주별로 색을 다르게지정하겠다는 뜻
               style='AirBags', #범주별로 스타일을 다르게 지정하겠다는 뜻
               s=50,
               data=cars)
plt.show()

# 그리기
iris = pd.read_csv('C:/adp/2data_handling/data/iris.csv')
iris.info()

sns.scatterplot(x='sepal length',
               y='sepal width',
               hue='target',  #범주별로 색을 다르게지정하겠다는 뜻
               style='target', #범주별로 스타일을 다르게 지정하겠다는 뜻
               s=100,
               data = iris)












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


