################오류################
########파일xl을 못찾는거 같은데 ###
# ######zip파일??? 다시찾아보기 ####

import pandas as pd

file_path = r'13.로또번호시각화_EXCEL\lotto.xls'
df_from_excel = pd.read_excel(file_path,engine='openpyxl') #엔진은 openpyxl을 사용하여 판다스의 데이터프레임으로 엑셀을 불러옵니다.

df_from_excel = df_from_excel.drop(index=[0,1]) #0,1번 줄을 삭제합니다.

df_from_excel.columns = [
                        '년도','회차','추첨일','1등당첨자수',           #colums의 이름을 다시 정의 합니다.
                        '1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수',
                        '3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수',
                        '5등당첨금액','당첨번호1','당첨번호2','당첨번호3',
                        '당첨번호4','당첨번호5','당첨번호6','보너스'
                        ]
print(df_from_excel.head()) #앞부분의 데이터만 출력합니다.

print(df_from_excel['회차'].values) #회차를 출력합니다.

print(df_from_excel['1등당첨금액'].values) #1등당첨금액을 출력합니다.