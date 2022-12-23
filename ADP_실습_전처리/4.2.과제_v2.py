## 과제 4-2
# sklearn에서는 다양한 종류의 스케일러를 제공함
#
### 과제 4-2
import pandas as pd
import numpy as np
import six
from sklearn.model_selection import train_test_split
from sklearn
X = pd.read_csv('C:/adp/data/빅분기_X_train.csv', encoding='cp949')
X2 = X
y = pd.read_csv('C:/adp/data/빅분기_y_train.csv', encoding='cp949')
X.tail()

## 빅분기 X_train, 빅분기 y_train 데이터의 cust_id를 인덱스로 설정하세요
X.index = X['cust_id']
y.index = y['cust_id']
X = X.drop('cust_id', axis = 1)
y = y.drop('cust_id', axis = 1)

# 컬럼으로 index 변경
X2.tail()
X2.set_index('cust_id', inplace = True)
X2.tail()

# X_train과 y_train데이터를 y값을 기준으로 층화추출하여 7:3으로 데이터를 나누세요 (X_train, X_val, y_train,y_val)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True, stratify=y, random_state=1004)

## X_train과 X_val의 수치형 변수들만 StandardScaler를 이용하여 표준화 시키세요.
X_train = X_train[['총구매액', '최대구매액', '내점일수', '내점당구매건수', '주말방문비율', '구매주기']]
X_test = X_test[['총구매액', '최대구매액', '내점일수', '내점당구매건수', '주말방문비율', '구매주기']]
nomailize = preprocessing.StandardScaler()
nomailize

X_train2 = nomailize.fit_transform(X_train)
X_test2 = nomailize.fit_transform(X_test)

X_train2
X_test2


## test
X.tail()
y.tail()
