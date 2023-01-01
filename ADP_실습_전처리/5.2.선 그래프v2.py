## 선 그래프

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## 선 종류

x = np.linspace(0, 10, 11)
x

fig = plt.figure()
ax = plt.axes()

plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');

# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-')  # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':');  # dotted

## 직선 그래프
# y = ax+b 형태의 직선이나 y=h 형태의 가로선 혹은 x=v 형태의 세로선
# plt.plot(x축, 회귀식, data=데이터, c='color')  # y = ax+b 형태의 직선
# plt.hlines(y, xmin , xmax)  # y=h 형태의 수평선
# plt.vlines(x, ymin , ymax)  # x=v 형태의 수직선

## [예제]
# fifa 데이터에서 passing과 overall 사이의 선형회귀모형을 생성한 뒤, 직선 그래프로 표현하기
# 선형 회귀식에 대한 그래프는 passing과 overall에 대한 산점도 위에 나타내며, 색상은 빨강으로 지정하여 표현
# overall의 중위수는 수평선, passing의 중위수는 수직선으로 그리되 각각의 선은 점 스타일의 회색 선으로 지정

fifa = pd.read_csv('C:/adp/data/players_20.csv')
fifa.columns
feature = ['sofifa_id','short_name','passing','overall']
fifa = fifa[feature].head(100)
fifa.dropna(inplace=True)
fifa.head()
fifa.info()

## 회구분석
from sklearn.linear_model import LinearRegression

lr = LinearRegression() # 회귀모델 선언
x = fifa[['passing']]
lr.fit(x, fifa['overall']) # 회귀모델 생성
lr.predict(x)

plt.scatter(fifa['passing'], fifa['overall']) # 원 데이터 산포도
plt.plot(fifa['passing'], lr.predict(x), c = 'r' ,linestyle='-') # 회귀직선
plt.hlines(np.median(fifa['overall']),np.min(fifa['passing']),np.max(fifa['passing']), 'lightgrey', linestyles = ':') # passing의 중위수 수평선
plt.vlines(np.median(fifa['passing']),np.min(fifa['overall']),np.max(fifa['overall']), 'lightgrey', linestyles = ':') # overall의 중위수 수직선


plt.xlabel('passing', fontsize=12)
plt.ylabel('overall',fontsize=12)
plt.title('fifa data')
plt.show()


## 곡선 그래프
# [예제]
# 평균이 0이고 표준편차가 1인 확률밀도함수를 생성하고 그래프로 나타내기
# x축의 범위는 -3 ~ +3으로 한다

# import matplotlib.pyplot as plt
# import numpy as np
import scipy.stats as stats

# np.linspace(min, max, cnt) : 지정된 간격 동안 균등 한 간격의 숫자를 반환
# -3에서 3까지 100등분하여 값을 지정함
x = np.linspace(-3, 3, 100)
x
# stats.norm(mean, sd) : 확률밀도를 계산해주는 함수
y = stats.norm(0, 10).pdf(x)
y

plt.plot(x, y) # plot line 그래프
plt.xlabel("x") # x축 레이블 지정
plt.ylabel("y") # y축 레이블 지정
plt.grid() # 플롯에 격자 보이기
plt.title("Normal Distribution without scipy")
plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
import scipy.stats as stats

# np.linspace(min, max, cnt) : 지정된 간격 동안 균등 한 간격의 숫자를 반환
# -3에서 3까지 100등분하여 값을 지정함
x = np.linspace(-3, 3, 100)
# stats.norm(mean, sd) : 확률밀도를 계산해주는 함수
y = stats.norm(0, 1).pdf(x)

plt.scatter(x,y) # scatter 점 그래프

plt.xlabel("x") # x축 레이블 지정
plt.ylabel("y") # y축 레이블 지정
plt.grid() # 플롯에 격자 보이기
plt.title("Normal Distribution without scipy")
plt.show()


## 5.2.4 꺾은선 그래프
# 여러 범주에 대한 관측값을 비교하거나 시간의 흐름에 따른 데이터에서 추세를 파악하기 위해 사용
# X축은 정렬되어 있어야 함
# plt.plot(x축, y축, data=데이터, ls='-/--/-./:', lw=int_value, c='color') # ls: 선 스타일, lw:선 굵기
# plt.legend(['항목 이름1','항목 이름2'])

# [예시] Cars93에서 Wheelbase 따른 Type 별 Price의 관측값을 살펴보자
cars = pd.read_csv('C:/adp/data/Cars93.csv')
cars.head()
cars.Wheelbase.value_counts()

# 정렬하지 않고 plot 그리면 이상함
plt.plot('Wheelbase', 'Price', data=cars.loc[cars['Type']=='Small'] )

## 선형 그래프를 그릴때에는 X축 정렬을 해줘야 함
car_type =cars.Type.unique()
car_type
car_sorted = cars.sort_values(by=['Wheelbase'])

plt.plot('Wheelbase', 'Price', data=car_sorted.loc[car_sorted['Type']=='Small'])
plt.plot('Wheelbase', 'Price', data=car_sorted.loc[car_sorted['Type']=='Midsize'])

plt.legend(car_type)
plt.show()




