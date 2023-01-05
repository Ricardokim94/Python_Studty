import threading
import time

def tread_2():
    while True:
        print("쓰레드2 동작")
        time.sleep(1.0)
        
t1 = threading.Thread(target=tread_2) #쓰레드 설정
t1.daemon = True #쓰레들를 데몬쓰레드로 설정하여 메인동작이 실행될 때만 쓰레드를 실행하도록 한다.
t1.start()

while True:
    print("메인동작")
    time.sleep(2.0)