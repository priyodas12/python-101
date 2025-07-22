from threading import *
from time import *


def display(start, end):
    for i in range(start, end):
        print(chr(i))
        sleep(0.5)


t1 = Thread(target=display(65, 90), name="display alphabets: upper case")
t2 = Thread(target=display(97, 123), name="display alphabets: lower case")

t1.start()
t2.start()
