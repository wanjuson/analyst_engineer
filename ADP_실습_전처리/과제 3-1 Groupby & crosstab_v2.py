## 과제 3-1 Groupby & crosstab
# 데이터 : "7.세종시_아파트(전월세)_실거래가.csv"
import pandas as pd

# iris 데이터 불러와서 데이터프레임으로 만들기
df_1 = pd.read_csv('C:/adp/2data_handling/data/7.세종시_아파트(전월세)_실거래가.csv')

# 전세의 보증금 평균 값을 구하세요 groupby 사용
df_1.tail()
df_1.info()
df_mean1 = df_1.groupby('전월세구분').mean()['보증금(만원)']
df_mean1['전세']

# 세종시 월세 평균 가격을 구하세요
df_1.groupby('전월세구분').mean()['월세(만원)']
df_mean1['월세']

# 계약년도별, 시군구별 평균 보증금 가격를 구하세요
df_1['계약년도'] = df_1['계약년월']//100;
print(df_1['계약년도'])

df_1.groupby(['계약년도', '시군구']).mean()['보증금(만원)']

# 계약년도별 전세 건수를 구하세요
df_cnt1 = df_1[df_1['전월세구분'] == '전세'].groupby(['계약년도']).count()
df_cnt1

# 인덱스에 시군구, 컬럼에는 전월세구분이 있는 도수분포표를 만드세요
pd.crosstab(df_1['시군구'], df_1['전월세구분'],  dropna = True)























