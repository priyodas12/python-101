from threading import Thread, Lock
from time import sleep


# Mutex
def display(strings):
    l1.acquire()
    for x in strings:
        print(x)
        sleep(0.1)
    l1.release()


l1 = Lock()
t1 = Thread(target=display, args=("PYTHON",), name="print: str1")
t2 = Thread(target=display, args=("*******",), name="print: str2")

t1.start()
t2.start()

t1.join()
t2.join()
