# 과제 2-1
# Q1. pandas를 import하고 data폴더 안에 있는 titanic.csv 파일 불러오세요
import pandas as pd
df_t = pd.read_csv("C:/adp/2data_handling/data/titanic.csv")
df_t.tail()

# Q2. 타이타닉 데이터의 결측치가 있는 변수를 확인하세요
df_t.info()
df_t.describe() # age 714

# Q3. 타이타닉 데이터에서 survived 변수 (생존 여부) 에서 생존자 수를 구하세요
df_t['survived'].sum()

# Q4. 타이타닉 데이터에 class변수의 unique 값을 구하세요
df_t['class'].unique()

# Q5. 타이타닉 데이터에 class변수의 value_counts값을 출력하세요
df_t['class'].value_counts()

# Q6. 타이타닉 데이터에서 class변수명을 CLASS로 변경하세요
df_t.rename({"class":"CLASS"},axis='columns',inplace=True)
df_t.tail()

# Q7. 타이타닉 데이터에 age 변수를를 int로 변경하세요
df_t['age'] = df_t['age'].fillna(-1).astype('int8').replace({-1: None})
df_t.tail()

#Q8. embarked변수를 index로 변경하세요
df_t.set_index('embarked', inplace =True)
df_t.tail()
