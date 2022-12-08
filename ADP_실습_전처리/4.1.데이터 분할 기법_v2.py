## 4.1 데이터 샘플링
# 데이터 분석을 진행할 때, 전체 데이터를 모두 활용하는 것은 수많은 시간과 비용이 들 수 있다.
# 본 장에서는 데이터 샘플링의 방법과 python을 활용한 표본 추출에 대해 학습한다.
# 4.1.1 통계
# 통계란 특정집단을 대상으로 수행한 조사나 실험을 통해 나온 결과에 대한 요약된 형태의 표현이다.
# 조사 또는 실험을 통해 데이터를 확보하며, 조사대상에 따라 총조사와 표본조사로 구분한다.

# 4.1.2 통계자료의 흭득 방법
# 가. 총 조사/ 전수조사
# 총 조사란 대상 집단 모두를 조사하는 방법이며, 특별한 경우를 제외하고는 사용되지 않는다.

# 나. 표본조사
# 모집단(population) : 조사하고자 하는 대상 집단 전체
# 원소(element) : 모집단을 구성하는 개체
# 표본(sample) : 조사하기 위해 추출한 모집단의 일부 원소
# 모수(parameter) : 표본 관측에 의해 구하고자 하는 모집단에 대한 정보
# 모집단의 정의, 표본의 크기, 조사방법, 조사기간, 표본추출방법을 명확하게 정의해야 한다.

# 4.1.3 표본 추출 방법
# 표본조사에서 중요한 점은 모집단을 대표할 수 있는 표본의 추출이며, 표본 추출 방법에 따라 분석 결과의 해석은 큰 차이가 발생한다.
# 가. 단순 임의 추출법
# 각 개체에 번호를 부여하여 랜덤하게 n개를 추출하는 방법으로 모든 개체는 선택될 확률이 동일하다.
# 복원, 비복원 추출로 나누어진다.
# 나. 계통추출법
# 랜덤하게 정렬된 표본에서 시간 혹은 공간적으로 일정한 간격을 두고 표본을 추출하는 방법이다.
# 단순랜덤추출법의 변형된 방식으로 번호를 부여한 샘플을 나열하여 K개씩 n개의 구간으로 나누고 첫 구간에서 하나를 임의로 선택한 후에 K개씩 띄어서 표본을 선택한다. 즉 임의의 위치에서 매 k번째 항목을 추출하는 방법이다.
# 다. 집락추출법
# 군집을 구분하고 특정 군집을 먼저 선택한 후 해당 군집에서만 표본을 추출하는 방법이다.
# 라. 층화추출법
# 모집단이 이질적인 몇 개의 계층으로 이루어져 있을 때 모든 계층으로부터 원소를 임의로 추출하여 각 계층을 고루 대표할 수 있도록 랜덤하게 표본을 추출하는 방법이다.

# 4.1.4 Python을 이용한 표본 추출
# 4.1.4.1 단순 임의 추출
# 일반적으로 데이터를 training data와 test data로 분할할 때 가장 많이 사용하는 표본추출 방법이다.

#  함수사용법 : DataFrame.sample(frac=0.7, random_state=2000)
# n : 추출할 표본 개수
# frac : 추출할 표본 크기 비율
# replace : boolean, True이면 복원추출, False이면 비복원 추출

## [예제1] iris 데이터로 분석을 진행하기 위해 전체 데이터의 7:3 비율로 training data와 test data를 추출한 뒤 새로운 변수에 저장해보자
# ( 데이터 추출 방법은 단순 임의 추출을 이용한다.)
import pandas as pd
import numpy as np
iris = pd.read_csv('C:/adp/2data_handling/data/iris.csv')
iris.tail()
iris_train = iris.sample(frac = 0.7, replace = False, random_state=2000)
iris_test = iris.sample(frac = 0.3, replace = False, random_state=2000)

iris['target'].value_counts()
iris_train['target'].value_counts()
iris_test['target'].value_counts()

iris_train.index.isin(iris_test.index)
iris_train[iris_train.index.isin(iris_test.index)]
# iris_train와 iris_test에 동일변수 존재

# total - train = iris_test2
iris_test2 = iris[iris.index.isin(iris_train.index) == False]
iris_test2.info()

## 4.1.4.2 층화 임의 추출
# 특정 데이터가 여성 계층 70%, 남성 계층 30%로 구성되어 있다고 가정해보자.
# 각 계층을 고루 대표 할 수 있도록 표본을 추출하기 위해서는 여성과 남성 집단에 대해 0.7:0.3의 비율로 데이터를 뽑아야 한다.
# 이처럼 여성과 남성이라는 계층별로 표본을 추출하는 것을 층화 임의 추출이라고 한다.
from sklearn.model_selection import train_test_split
## 함수사용법 : X_train, X_test, y_train, y_test = train_test_split(
#                                                     X, y
#                                                     test_size=0.2,
#                                                     shuffle=True,
#                                                     stratify=변수,
#                                                     random_state=1004)
# * X: 데이터 테이블
# * test_size : 테스트 사이즈 비율
# * shuffle : True이면 무작위 추출, False이면 체계적 추출
# * random_state : 난수 // 임의의 번호 지정하면 되며 같은 번호라면 같은 값이 나온다.

iris["target"].value_counts()

# stratify를 설정해야 층화추출이 된다.
X_train, X_test = train_test_split(iris, test_size=0.7, shuffle=True, stratify=iris["target"], random_state=1004)
X_train["target"].value_counts()
X_test["target"].value_counts()
X_train[X_train.index.isin(X_test.index)]


## 5.1 언더 샘플링 & 오버 샘플링
# 5.1.1 언더샘플링
# 다수 클래스 의 샘플은 소수 클래스와 비교할 때 분포 비율과 일치하도록 무작위로 제거함.
# 2개의 클래스의 비율을 맞추기 위해 귀중한 정보를 잃어버리고 편향될 수 있기 때문에 일반적으로 선호되지 않음
# 5.1.2 오버 샘플링
# 소수 클래스의 샘플을 증가시켜 마이너 클래스와 메이저 클래스의 샘플 크기를 동일하게 만드는 기법
# 랜덤 오버샘플링(소수 샘플 복제)은 동일한 정보를 복사하여 오버피팅을 유발할 수 있음

## 5.1.3 SMOTE(Synthetic Minority Over-sampling Technique)
# KNN을 기반으로 샘플링함
# 소수 클래스의 기존 샘플을 사용하여 새로운 합성 관찰을 생성 하는 오버 샘플링 기법 소수 클래스에 대한 선형 보간법으로 가상 훈련 기록을 생성.
# 합성 훈련 기록은 소수 클래스의 각 예에 대해 k-최근접 이웃 중 하나 이상을 무작위로 선택하여 생성.
# 오버샘플링 과정을 거친 후 데이터를 재구성하고 처리된 데이터에 대해 여러 분류 모델을 적용할 수 있음
# 데이터의 특성에 따라 다르겠지만, 빅데이터 분석을 위해서는 많은 데이터 확보가 효과적이므로 오버샘플링 기법을 적용하는 것이 좋음.
# 기존의 데이터가 적은 새로운 사례의 데이터에서 사용하기 어려움.
df_t = pd.read_csv('C:/adp/2data_handling/data/titanic.csv')
from imblearn.over_sampling import SMOTE

df_t['survived'].value_counts()

# SMOTE는 결측치가 있으면 안된다.
df_t = df_t.dropna()
df_t

X = df_t[['age','sibsp','parch','fare']]
y = df_t['survived']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True, stratify=y, random_state=1004)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
X_train = scaler.fit_transform(X_train)

X_train.shape
X_train
y_train.value_counts()

# 모델설정
# sm = SMOTE(k_neighbors=5)
sm = SMOTE(k_neighbors = 4)

# train데이터를 넣어 복제함
X_resampled, y_resampled = sm.fit_resample(X_train,y_train)

print('After OverSampling, the shape of train_X: {}'.format(X_resampled.shape))
print('After OverSampling, the shape of train_y: {} \n'.format(y_resampled.shape))

print("After OverSampling, counts of label '1': {}".format(sum(y_resampled==1)))
print("After OverSampling, counts of label '0': {}".format(sum(y_resampled==0)))



