## 과제 3
#   데이터 : "7.세종시_아파트(전월세)_실거래가.csv"
#    1) 단지명 중  '해밀마을 2단지'인 row 삭제
#    2) new_시군구' 컬럼을 만들고 '세종특별자치시 고운동' => '세종특별자치시 해밀동' 으로 변경
#    3) 'Class'컬럼을 만든 뒤 전세면 True 아니면 False로 입력 (loc사용)
#    4) 전세이면서 보증금이 1억 이상인 데이터만을 추출
#    5) -10~0층 : 지하 , 1~5층 : 저층 6~15층 : 중층, 16층 이상 : 고층으로 할당하는 새로운 컬럼 생성

import pandas as pd
import numpy as np

df_t = pd.read_csv('C:/adp/2data_handling/data/7.세종시_아파트(전월세)_실거래가.csv')
df_t.tail(5)
df_t.info()

## 1) 단지명 중  '해밀마을 2단지'인 row 삭제
## 방법1
df_t.loc[df_t['단지명'] == '해밀마을 2단지']
idx = df_t[df_t['단지명'] == '해밀마을 2단지'].index
idx
df_t.drop(idx, inplace=True)
df_t

## 방법2
df_t2 = df_t
df_t2 = df_t2[df_t2.단지명 != '해밀마을 2단지']
df_t2.loc[df_t['단지명'] == '해밀마을 2단지']

## 2) 'new_시군구' 컬럼을 만들고 '세종특별자치시 고운동' => '세종특별자치시 해밀동' 으로 변경
df_t['new_시군구'] = df_t['시군구']
df_t['시군구'].head()
df_t.loc[df_t['시군구'] == '세종특별자치시 고운동', 'new_시군구'] = '세종특별자치시 해밀동'
df_t['new_시군구'].head()

## 3) 'Class'컬럼을 만든 뒤 전세면 True 아니면 False로 입력 (loc사용)
df_t['Class'] = False
df_t.loc[df_t['전월세구분'] == '전세', 'Class'] = True
df_t.tail(5)

## 4) 전세이면서 보증금이 1억 이상인 데이터만을 추출
df_t.loc[(df_t['전월세구분'] == '전세') & (df_t['보증금(만원)'] >= 10000)]

## 5) -10~0층 : 지하 , 1~5층 : 저층 6~15층 : 중층, 16층 이상 : 고층으로 할당하는 새로운 컬럼 생성
df_t['ele'] = '고층'
df_t.loc[df_t['층'] <= 0, 'ele'] = '지하'
df_t.loc[(df_t['층'] >= 1) & (df_t['층'] <= 5), 'ele'] = '저층'
df_t.loc[(df_t['층'] >= 6) & (df_t['층'] <= 15), 'ele'] = '중층'

df_t['ele'].value_counts()




