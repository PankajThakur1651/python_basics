from threading import Thread

class MyThread:
    def run(self):
        for i in range(1, 10):
            print(f"Value of i is {i}")



obj = MyThread()

t= Thread(target=obj.run)
t.start()

t.join()