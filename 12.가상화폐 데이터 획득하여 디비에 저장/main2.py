import pyupbit
import sqlite3

ticker = 'KRW-BTC'
interval = 'minute1'
to = '2023-01-05 17:23'
count = 200
price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

de_path = r"12.가상화폐 데이터 획득하여 디비에 저장\coin.db" #12폴더에 coin.db이름으로 데이터베이스 저장 

con = sqlite3.connect(de_path, isolation_level=None) # 데이터 베이스를 생성
price_now.to_sql('BTC', con, if_exists='append') #BTC라는 이름으로 데이터를 생성후 데이터를 추가

con.close