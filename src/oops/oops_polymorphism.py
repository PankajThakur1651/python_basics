class Flight:
    def __init__(self, engine): # dependency Injection
        print("Init is called")
        self.engine = engine

    def start_engine(self):
        self.engine.start();


class Air_bus_engine:
    def start(self):
        print("starting Airbus Engine")


class Boeing_engine:
    def start(self):
        print("starting Boeing engine ")


if __name__ == '__main__':
    abus_engine = Air_bus_engine()
    f = Flight(abus_engine)
    f.start_engine()

    boeing_engine = Boeing_engine()
    f = Flight(boeing_engine)
    f.start_engine()

