import pandas as pd
import sqlite3

db_path = r"12.가상화폐 데이터 획득하여 디비에 저장\coin.db"
con = sqlite3.connect(db_path, isolation_level=None) # 데이터 베이스에 접속

readed_df = pd.read_sql("SELECT * FROM 'BTC", con, index_col='index') #판다스를 이용하여 BTC를 읽는다.

print(readed_df)