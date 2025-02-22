import threading
from time import sleep


def my_func():
    for i in range(1, 10):
        sleep(1)
        print(f"i ===>{i}")

        print(f"{threading.current_thread().name}===>{i}")
        print("--------------------------------")


if __name__ == '__main__':
    t = threading.Thread(target=my_func)
    t.start()

    print("Meanwhile main is also running")

    for i in range(1, 10):
        sleep(1)
        print(f" Main Thread===>{i}")
        print("================================")

    t.join()
