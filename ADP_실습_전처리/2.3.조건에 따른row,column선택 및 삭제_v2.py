## 1.3 조건에 따른 row/column 선택 및 삭제
## 1.3.1 조건에 따른 row 선택
# Series boolean selection 활용하기
# 조건이 하나일 때 : df[df['컬럼명'] >= 40]
# 조건이 두개 이상 : df[(조건1) & (조건2) & ((조건3) | (조건4)) ]
# ** 관계연산자의 우선순위를 모른다면 그냥 괄호를 많이 쓸 것

import pandas as pd
import numpy as np

df_t = pd.read_csv('C:/adp/2data_handling/data/titanic.csv')
df_t.tail(5)

## 하나의 조건문
df_t[df_t['survived']==1]
df_t[df_t['age']==26]

df_t['survived']==1


## 조건이 여러개  &가 | 보다 우선순위를 가짐 , 조건연산자의 순위를 모를 때에는 괄호로 묶자!
df_t[ (df_t["survived"]==1) | (df_t['fare']>30) & (df_t['class']=="First") ]
df_t.loc[(df_t["survived"]==1) | (df_t['fare']>30) & (df_t['class']=="First") ]

## 조건에 따른 column 추가, 변경
df_t.loc[df_t["survived"] == 1,'temp'] = 99999
df_t

df_t['temp2'] = "30대 미만"
df_t.loc[df_t.age >= 30,'temp2']
df_t.loc[df_t.age >= 30,'temp2'] = "30대 이상"
df_t

## 데이터 프레임으로 접근하여 값을 대입하면 오류가 남 // 데이터 프레임 접근은 복사본이므로 데이터에 직접 접근할 때에는 loc를 써야함
df_t[df_t["age"]>30]['temp2'] = True
df_t.loc[df_t.age >= 30, 'temp2']
df_t[df_t.age >= 30]['temp2']
df_t.drop(columns=['temp','temp2'],inplace=True)

## 1.3.2.1 np.where()
# 데이터 프레임 or 리스트 내 필드에 접근하고 수정하는 방법 . (loc or iloc를 두번 사용하는 것과 동일)
# np.where(condition, x, y)는 조건이 충족되면x를, 그렇지 않으면y를 반환합니다.
df_t['alive'] = np.where(df_t['survived']==1, 'Yes', 'No')
df_t.tail(10)

## 1.3.2.2 np.select()
# 데이터 프레임 or 리스트 내 필드에 접근하고 수정하는 방법 .
# 조건 목록과 선택 목록을 입력으로 받아서 조건에 따라 선택 목록의 요소로 구성된 배열을 반환합니다.
# 이 방법을 사용하면 두 개 이상의 조건이있을 때 Pandas의 주어진 조건을 기반으로 DataFrame 열을 만들 수 있습니다.
conditionlist = [
    (df_t['age'] >= 19) ,
    (df_t['age'] >= 8) & (df_t['age'] <19),
    df_t['age'] < 8]
conditionlist
choicelist = ['성인', '초중고등학생', '미취학아동']

df_t['status'] = np.select(conditionlist, choicelist, default = 'Not_Specified')
df_t.tail(10)










# 1) 세종시 데이터에서 컬럼 확인 후, unnamed 컬럼 제거
ap_data.info()
ap_data = ap_data.drop(columns=['Unnamed: 0'])
ap_data.info()

# 2) 전월세구분 컬럼에서 unique값 확인
ap_data['전월세구분'].unique()
ap_data['전월세구분'].nunique()
ap_data['전월세구분'].value_counts()

# 3) index= 100~200, column = 전월세구분, 전용면적(㎡),보증금(만원)으로 이루어진 데이터프레임 추출
ap_data2 = ap_data.loc[100:200, ['전월세구분', '전용면적(㎡)', '보증금(만원)']]
ap_data2

# 4) 0~200 index를 가진 행 삭제
ap_data3 = ap_data
ap_data3.info()
ap_data3.head()
dell = range(200)
ap_data3.drop(dell, inplace=True)
# ap_data3.drop(dell, inplace=False)
ap_data3.head()

# 5) 건축년도 컬럼 중복 제거 결과 출력
ap_data['건축년도'].value_counts()
