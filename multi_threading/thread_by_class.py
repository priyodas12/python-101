from threading import *
from time import *


class Alphabets(Thread):
    def run(self):
        for i in range(65, 90):
            print(chr(i))
            sleep(0.3)


t1 = Alphabets()
t1.start()
