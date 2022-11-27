## # 과제 2-5
##  players_19.csv와 players_20.csv 데이터를 행결합해서 master data를 만드세요
import pandas as pd

fifa_df19 = pd.read_csv('C:/adp/2data_handling/data/players_19.csv')
fifa_df20 = pd.read_csv('C:/adp/2data_handling/data/players_20.csv')

## fifa_df19 = players_19.csv에서 'sofifa_id','short_name','overall' 컬럼만 추출
fifa_df19_2 = fifa_df19.loc[:, ['sofifa_id','short_name','overall']]
fifa_df19_2

fifa_df19[fifa_df19['sofifa_id', 'short_name', 'overall']]

## fifa_df20 = players_20.csv 에서 sofifa_id와 overall만을 추출
fifa_df20_2 = fifa_df20.loc[:, ['sofifa_id', 'overall']]
fifa_df20_2

## sofifa_id를 key값으로  위의 두 테이블을 innerjoin 하세요
fifa_df_inner = pd.merge(fifa_df19_2, fifa_df20_2, how = 'inner')

## sofifa_id를 key값으로  위의 두 테이블을 outerjoin 하세요
fifa_df_outer = pd.merge(fifa_df19_2, fifa_df20_2, how = 'outer')

## outerjoin을 한 테이블 중 inner join을 한 테이블과 중복되는 행을 삭제하세요
fifa_df_inner
fifa_df_outer

fifa_df_union = pd.concat([fifa_df_inner, fifa_df_outer])
fifa_df_union

fifa_df_union2 = fifa_df_union.drop_duplicates()
fifa_df_union2


# 중복되는 행(Row) 확인하기 :: duplicated
fifa_df_dup = fifa_df_union.duplicated()
fifa_df_dup


