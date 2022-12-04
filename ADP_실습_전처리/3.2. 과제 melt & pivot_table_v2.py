## 과제 3-2 melt & pivot table
# 1.1  데이터 : '식품소비.csv'
# 1.2  y값을 id_vars로 놓고 column들이 category로 바뀌도록 테이블을 구성하세요
# 1.3  아래와 같이 category, y 값에 따른 평균을 구하세요
# 1.4  아래와 같이 category, y 값에 따른 표준편차를 구하세요

import pandas as pd
import numpy as np

## 과제 3-2 melt & pivot table
# 1.1  데이터 : '식품소비.csv'
food = pd.read_csv('C:/adp/2data_handling/data/식품소비.csv')
food.tail()
food.info()

# y값을 id_vars로 놓고 column들이 category로 바뀌도록 테이블을 구성하세요
melt_food = pd.melt(food, id_vars=['y']
                    , value_vars=['fruits', 'noodle', 'bread', 'sea_meat_proc', 'seafood', 'vegetables'
                                , 'milk_product', 'drink', 'seasoned', 'alcohol', 'meat', 'snack'],
                 var_name='id_vars', value_name='category', ignore_index = True )
melt_food

# 1.3  아래와 같이 category, y 값에 따른 평균을 구하세요
pd.pivot_table(melt_food, index = 'y', columns = 'id_vars', values='category' ).head(10)

# 1.4  아래와 같이 category, y 값에 따른 표준편차를 구하세요
pd.pivot_table(melt_food, index = 'y', columns = 'id_vars', values='category', aggfunc = 'std'  ).head(10)





