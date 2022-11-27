## 과제 2-4
## players_20.csv데이터에서 height_cm, weight_kg 의 중위값(median)을 출력하세요.
# df.sort_index() : df 객체 인덱스 기준으로 정렬

import pandas as pd
import numpy as np

df_t = pd.read_csv('C:/adp/2data_handling/data/players_20.csv')
df_t.tail(5)
df_t.info()
height_cm_med = df_t.loc[:, ['height_cm']].median()
height_cm_med[0]
weight_kg_med =  df_t.loc[:, ['weight_kg']].median()
weight_kg_med[0]

## 데이터셋의 height_cm, weight_kg 이 중위값(median)보다 큰 선수를 출력하세요
df_t.loc[[height_cm >= height_cm_med[0]]]
df_t.loc[(df_t["height_cm"]>= height_cm_med[0]) & (df_t["weight_kg"]>= weight_kg_med[0])]

## height_cm 기준으로 내림차순 정렬하세요
df_t.loc[:, ['height_cm']].sort_values( by=['height_cm'], ascending = False ).head(10)

## weight_kg 기준으로 내림차순 정렬하세요
df_t.loc[:, ['weight_kg']].sort_values( by=['weight_kg'], ascending = False ).head(10)

## height_cm 와 weight_kg 를 기준으로 오름차순 정렬하세요
df_t.loc[:, ['height_cm', 'weight_kg']].sort_values( by=['height_cm', 'weight_kg'], ascending = True ).head(10)


