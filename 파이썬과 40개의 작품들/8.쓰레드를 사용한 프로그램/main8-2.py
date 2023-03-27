import threading 
import time

# 메인코드가 동작할 때에만 쓰레드 동작하는 코드 만들기 

def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)
#데몬쓰레드로 설정하여 메인동작이 실행될 때만 쓰레드를 실행하도록 합니다.
t1.daemon = True
t1.start()

while True:
    print("메인동작")
    time.sleep(2.0)