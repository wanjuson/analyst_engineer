## 미션!! 아래의 과제를 수행하고 댓글에 올려주세요!!!
import pandas as pd

id_name = pd.DataFrame({'ID' : ['c01', 'c02', 'c03', 'c04', 'c05', 'c06', 'c07'],
                       'last_name': ['Lee', 'Kim', 'Choi', 'Park','Lim','Bae','Kim']})
id_name
id_number = pd.DataFrame({'id' : ['c03', 'c04', 'c05', 'c06', 'c07', 'c08', 'c09'],
                         'number' : [3, 1, 0, 7, 3, 4, 1]})
id_number

# 컬럼을 기준으로 두 테이블이 모두 공통된 값을 가지고 있는 경우에만 두 데이터(id_name, id_number)를 병합해보세요.
# inner join
pd.merge(id_name, id_number, how = 'inner', on = 'ID')

# 공통된 값이 없는 경우에도 데이터가 출력되도록 id 칼럼을 기준으로 두 데이터의 모든 행을 병합해보세요.
# Outer Join
pd.merge(id_name, id_number, how = 'outer', on = 'ID')

# id 칼럼을 기준으로 두 데이터를 병합하는데,
# 기준칼럼에 공통 값이 없는 경우에는 id_number 데이터를 기준으로 병합해보세요.
# Right Outer Join에 해당
pd.merge(id_name, id_number, how = 'right', on = 'ID')







