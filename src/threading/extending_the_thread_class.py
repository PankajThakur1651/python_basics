from threading import Thread
from time import sleep


class MyThread(Thread):
    def run(self):
        for i in range(1, 10):
            print(f"Valur of i is {i}")


if __name__ == '__main__':
    t = MyThread()
    t.start()
