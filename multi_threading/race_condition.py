from threading import Thread
from time import sleep


def display(strings):
    for x in strings:
        print(x)
        sleep(0.1)


t1 = Thread(target=display, args=("PYTHON",), name="print: str1")
t2 = Thread(target=display, args=("*******",), name="print: str2")

t1.start()
t2.start()

t1.join()
t2.join()
