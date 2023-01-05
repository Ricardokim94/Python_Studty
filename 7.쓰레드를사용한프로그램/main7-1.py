import threading
import time

def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)   #thread_1함수로 1초마다 '쓰레드1동작'을 출력한다.
        
t1 = threading.Thread(target=thread_1) #쓰레드를 성정한다.
t1.start()

while True:
    print("메인동작")
    time.sleep(2.0) #메인코드로 "메인동작"을 2초마다 출력한다.

