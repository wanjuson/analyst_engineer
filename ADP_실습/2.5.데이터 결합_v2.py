## 1.5 데이터 결합
# R과 다른점 : 결합하려는 데이터프레임의 행과 열의 개수가 맞지 않아도 NaN값이 채워짐
# 1.5.1 행결합
# 1.5.1.1 데이터프레임 붙이기 : pd.concat()
# 행인덱스와 열인덱스가 다른 데이터프레임 합치기
# * pd.concat([df1, df2, ...], axis=0)
# ignore_index=True를 붙이면 인덱스 재배열 가능

import pandas as pd
import numpy as np

# df_t = pd.read_csv('C:/adp/2data_handling/data/7.세종시_아파트(전월세)_실거래가.csv')
customer1 = pd.DataFrame({'id':['c01', 'c02', 'c03', 'c04'],
                        'last_name':["Lee","Kim","Choi","Park"]},
                        index = [0,1, 2,3])
customer1

customer2 = pd.DataFrame({'Id':['c05','c06','c07'],
                         'Last_name':['Lim', 'Bae', 'Kim'],
                         'age':[23, 34, 45]},
                        index = [0, 1, 2])
customer2

pd.concat([customer1, customer2]) # 컬럼네임이 달라서 잘못붙음
customer2.columns
customer1.columns

# 컬럼네임 변경
customer2.columns = ['id', 'last_name', 'age']
customer2.columns

# default 값으로 axis=0이 적용되어 행방향으로 데이터프레임을 붙임
# customer1에는 age열이 없으므로 NaN값이 채워짐
pd.concat([customer1, customer2])

customer = pd.concat([customer1, customer2]).reset_index(drop = True)
customer

pd.concat([customer1, customer2]).reset_index(drop = False)

## reset_index를 쓰지 않고 바로 인덱스 재배열 하는 방법
result = pd.concat([customer1, customer2],ignore_index=True)
result


## 1.5.2 열결합
# 1.5.2.1 데이터프레임 붙이기 : pd.concat()
# 행인덱스와 열인덱스가 다른 데이터프레임 합치기
# pd.concat([df1, df2, ...], axis=1)
# axis=1은 열방향으로 데이터프레임을 붙임
# customer2에는 index 3행이 없으므로 NaN값이 채워짐

result2 = pd.concat([customer2, customer1], axis=1)
result2

# 1.5.2.2 시리즈를 데이터프레임에 붙이기 : pd.concat()
# 시리즈 객체를 생성할 때 name은, 이 시리즈가 데이터프레임이 결합되었을 때의 열이름을 나타냄
grade = pd.Series(['A', 'B', 'C','A', 'D', 'C', 'B'], name='grade')
grade2 = pd.Series(['A', 'B', 'C','A', 'D', 'C'], name='grade')
grade
grade2

result3 = pd.concat([grade, grade2], axis=1)
result3

# 1.5.2.3 시리즈끼리 붙이기 : pd.concat()
sr1 = pd.Series(['e0','e1','e2','e3'], name = 'e')
sr2 = pd.Series(['g0','g1','g2','g3'], name = 'g')
sr1
sr2

# 열방향으로 시리즈를 연결하면 데이터프레임이 됨
result4 = pd.concat([sr1, sr2], axis=1)
print(result4)
print(type(result4), '\n')

#행방향으로 시리즈를 연결하면 시리즈 타입 유지
result5 = pd.concat([sr1, sr2], ignore_index=True)
print(result5)
print(type(result5))

# 1.5.2.4 merge
# 두 데이터프레임에 존재하는 고유값(Key)를 기준으로 병합
# pd.merge(df_left, df_right, how='inner', on=None) 이 default
# how에 들어갈 수 있는 매개변수 : 'inner' , 'outer', 'left', 'right'
id_name = pd.DataFrame({'ID' : ['c01', 'c02', 'c03', 'c04', 'c05', 'c06', 'c07'],
                       'last_name': ['Lee', 'Kim', 'Choi', 'Park','Lim','Bae','Kim']})
id_name
id_number = pd.DataFrame({'id' : ['c03', 'c04', 'c05', 'c06', 'c07', 'c08', 'c09'],
                         'number' : [3, 1, 0, 7, 3, 4, 1]})
id_number

id_number.columns = ['ID','number']
id_number.columns

pd.concat([id_name, id_number], axis=1)
pd.concat([id_name, id_number])

# merge
pd.merge(id_name, id_number, how='right', on='ID')
pd.merge(id_name, id_number, how='left', on='ID')
pd.merge(id_name, id_number, how='inner', on='ID')
pd.merge(id_name, id_number, how='outer', on='ID')










