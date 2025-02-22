from threading import *


class BookMyBus:

    def __init__(self, available_seats):
        self.available_seats = available_seats
        self.lk = Lock()
        # self.sema = Semaphore()

    def buy(self, seat_requested):
        self.lk.acquire()
        if self.available_seats >= seat_requested:
            print("Confirming a seat")
            print("Processing the payment")
            print("printing the ticket")
            self.available_seats -= seat_requested
        else:
            print("==== All tickets are sold ===============")
        self.lk.release()


obj1 = BookMyBus(100)
t1 = Thread(target=obj1.buy, args=(3,))

t2 = Thread(target=obj1.buy, args=(4,))

t3 = Thread(target=obj1.buy, args=(3,))

t1.start()
t2.start()
t3.start()
