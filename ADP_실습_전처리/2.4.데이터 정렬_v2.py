## 1.4 데이터 정렬
# Index 기준 정렬
# df.sort_index() : df 객체 인덱스 기준으로 정렬
# default : 오름차순
# ascending = False : 내림차순

import pandas as pd
import numpy as np

df_t = pd.read_csv('C:/adp/2data_handling/data/titanic.csv')
df_t.tail(5)
df_t.info()

df_t.sort_index(axis=0, ascending=False)
df_t.sort_index(ascending=False)
df_t.sort_index(axis=0, ascending=True)


## 1.4.2 column 기준 정렬
# df.sort_index(axis=1) : df 객체 column 명으로 정렬
# default : 오름차순
# ascending = False : 내림차순

df_t.sort_index(axis=1, ascending = False)
df_t.sort_index(axis=1, ascending = True)

## 1.4.3 값 기준 정렬
# obj.sort_values() :시리즈 객체 값 기준으로 오름차순 정렬
# df.sort_values(by='컬럼명') : df객체를 지정한 컬럼의 값 기준으로 정렬
# df.sort_values(by=['컬럼명1','컬럼명2]) : df객체를 지정한 컬럼들의 값 기준으로 정렬
df_t.sort_values(by=['age', 'fare'], ascending = False).head(10)

df_t.sort_values( by=['survived', 'age'] ).head(10)


