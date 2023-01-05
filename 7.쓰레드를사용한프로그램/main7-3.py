#다수의 쓰레드를 동작시키는 코드 만들고 실행
import threading

def sum(name, value):
    for i in range(0, value):
        print(f"{name} : {i}")
        
t1 = threading.Thread(target=sum, args=('1번 쓰레드', 10)) #1번 쓰레드를 생성, name은 1번쓰레드 value는 10
t2 = threading.Thread(target=sum, args=('2번 쓰레드', 10)) #2번 쓰레드를 생성, name은 2번쓰레드 value는 10

t1.start()
t2.start()

print("Main Tread")