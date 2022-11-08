import pandas as pd

# path = 'C:/adp/2data_handling/data'
# pd.read_csv(path, 'iris.csv')

iris_data = pd.read_csv("C:/adp/2data_handling/data/iris.csv")
iris_data

iris_data.to_csv("C:/adp/2data_handling/example.csv", header=True, index = False, encoding = 'utf-8')
pd.read_csv("C:/adp/2data_handling/example.csv", encoding = 'utf-8')


## 데이터프레임
list_1 = [1,1,1,1]
list_1

pd.DataFrame(list_1) # 데이터 프레임 선언

# Series는 리스토아 비슷하지만 인텍스 값을 가지고 있음
Series_1 = pd.Series([1, 1, 1, 1])
Series_1

## 인덱스와 같이 선언하기
Series_2 = pd.Series([1, 1, 1, 1], index=['2021-09-15',2,"dd",43])
Series_2

## 1.5 DateFrame 출력
df.head()    # 처음 n개 출력, 미지정시 5개
df.tail()     # 마지막 n개 출력, 미지정시 5개