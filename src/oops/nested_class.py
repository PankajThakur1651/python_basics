class Car:
    def __init__(self, make, year):
        self.make = make
        self.year= year

    class Engine:
        def __init__(self, number):
            self.number = number

        def start(self):
            print("Engine Started now")

        def __del__(self):
            print("Engine deleted now")

    def __del__(self):
        print("Car deleted now")


c = Car("BMW", 2017)
engine = c.Engine(123);
engine.start()