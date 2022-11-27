# 데이터 : "7.세종시_아파트(전월세)_실거래가.csv"
# 1) 세종시 데이터에서 컬럼 확인 후, unnamed 컬럼 제거
# 2) 전월세구분 컬럼에서 unique값 확인
# 3) index= 100~200, column = 전월세구분, 전용면적(㎡),보증금(만원)으로 이루어진 데이터프레임 추출
# 4) 0~200 index를 가진 행 삭제
# 5) 건축년도 컬럼 중복 제거 결과 출력

import pandas as pd

ap_data = pd.read_csv('C:/adp/2data_handling/data/7.세종시_아파트(전월세)_실거래가.csv')
ap_data.tail(5)

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
