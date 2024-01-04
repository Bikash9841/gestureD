from threading import Thread
import time

a = -1
b = -1
c = -1


def test():
    while True:
        time.sleep(2)
        print(a, b, c)


test_thread = Thread(target=test, daemon=True)
test_thread.start()

while True:
    a = a+1
    time.sleep(1)
    b = b-1
    time.sleep(1)
    print(f'Main{a},{b},{c}')
