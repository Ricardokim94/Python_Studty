import pandas as pd
import matplotlib.pyplot as plt         #그래프를 읽기위해 matplotlib를 불러옴
import matplotlib
from matplotlib import font_manager, rc

file_path = r'13.로또번호시각화EXCEL\excel.xlsx'
df_from_excel = pd.read_excel(file_path,engine='openpyxl') #엔진은 openpyxl을 사용하여 판다스의 데이터프레임으로 엑셀을 불러옵니다.

df_from_excel = df_from_excel.drop(index=[0,1]) #0,1번 줄을 삭제합니다.

df_from_excel.columns = [
                        '년도','회차','추첨일','1등당첨자수',           #colums의 이름을 다시 정의 합니다.
                        '1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수',
                        '3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수',
                        '5등당첨금액','당첨번호1','당첨번호2','당첨번호3',
                        '당첨번호4','당첨번호5','당첨번호6','보너스'
                        ]

df_from_excel['1등당첨금액'] = df_from_excel['1등당첨금액'].str.replace(pat=r'[ㄱ-ㅎ|가-힣,]+', repl=r'', regex=True) #엑셀파일을 확인하면 당첨금액이 숫자+.+원
df_from_excel['2등당첨금액'] = df_from_excel['2등당첨금액'].str.replace(pat=r'[ㄱ-ㅎ|가-힣,]+', repl=r'', regex=True) #형태로 되어있다.(,와 원을 제거한다.)
df_from_excel['3등당첨금액'] = df_from_excel['3등당첨금액'].str.replace(pat=r'[ㄱ-ㅎ|가-힣,]+', repl=r'', regex=True)
df_from_excel['4등당첨금액'] = df_from_excel['4등당첨금액'].str.replace(pat=r'[ㄱ-ㅎ|가-힣,]+', repl=r'', regex=True)
df_from_excel['5등당첨금액'] = df_from_excel['5등당첨금액'].str.replace(pat=r'[ㄱ-ㅎ|가-힣,]+', repl=r'', regex=True)

df_from_excel['1등당첨금액'] = pd.to_numeric(df_from_excel['1등당첨금액'])   #값을 숫자형태로 다시 데이터프레임에 저장합니다.
df_from_excel['2등당첨금액'] = pd.to_numeric(df_from_excel['2등당첨금액'])   #엑셀 파일이 수정되는게 아닌 불러온 데이터프레임 형식에서 수정됩니다.
df_from_excel['3등당첨금액'] = pd.to_numeric(df_from_excel['3등당첨금액'])
df_from_excel['4등당첨금액'] = pd.to_numeric(df_from_excel['4등당첨금액'])
df_from_excel['5등당첨금액'] = pd.to_numeric(df_from_excel['5등당첨금액'])

print( df_from_excel[['1등당첨금액','2등당첨금액','3등당첨금액','4등당첨금액','5등당첨금액']])

font_path = "C:/Windows/Fonts/H2GTRM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name() #그래프의 이름을 표시할때 한글을 사용하기 위한 폰트를 설정
matplotlib.rc('font',family=font)
# rc('font', family=font)

x = df_from_excel['회차'].iloc[:100].values #회차의 마지막 축을 x축으로 사용한다.
price = df_from_excel['1등당첨금액'].iloc[:100].values / 100000000 #당첨금액의 마지막100개의 데이터만y축으로 사용한다. 단위는 억원으로 표시하기 위해 /1억을 한다.

plt.figure(figsize=(10,6))   #그래프의 초기표시 크기 
plt.xlabel('회차')                  #x축 라벨
plt.ylabel('당첨금액(단위:억원)')   #y축 라벨

plt.bar(x, price, width=0.4)
plt.savefig('test.png')
plt.show
