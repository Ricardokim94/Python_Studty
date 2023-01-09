import pandas as pd

filepath = r'14.전국의대학교위치시각화\고등교육기관 하반기 주소록(2021).xlsx'
df_from_excel = pd.read_excel(filepath, engine='openpyxl')

df_from_excel.columns = df_from_excel.loc[4].tolist() #5번째 위치의 데이터를 colums으로 설정. 데이터의 이름이다. 0부터 시작하므로 4의 위치가 5번째 위치이다.

df_from_excel = df_from_excel.drop(index=list(range(0,5)))

print(df_from_excel.head())

print(df_from_excel['학교명'].values)

print(df_from_excel['주소'].values)
