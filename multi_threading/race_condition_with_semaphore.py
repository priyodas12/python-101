from threading import Thread, Semaphore
from time import sleep


def display(strings):
    l1.acquire()
    for x in strings:
        print(x)
        sleep(0.2)
    l1.release()


l1 = Semaphore(2)
t1 = Thread(target=display, args=("PYTHON",), name="print: str1")
t2 = Thread(target=display, args=("*******",), name="print: str2")
t3 = Thread(target=display, args=("#######",), name="print: str3")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
