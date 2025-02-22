class BMW:
    def __init__(self, make, model,year):
        self.make = make
        self.model = model
        self.year= year

    def start(self):
        print("Starting the car ......")

    def stop(self):
        print("Stopping the car.....")


class Three_series(BMW):
    def __init__(self, crusie_control_enabled,make, model,year):
        BMW.__init__(self, make, model,year)
        #super().__init__(make, model,year)  // super() can also be sued to invoke constructor of base class here, no need to pass self here
        self.crusie_control_enabled=crusie_control_enabled

    def start(self):
        print("Button start")


class Five_series(BMW):
    def __init__(self, parking_assist_enabled,make, model,year):
        BMW.__init__(self, make, model,year)
        self.parking_assist_enabled=parking_assist_enabled

    def start(self):
        print("Remote start")



three_series=  Three_series(True, "BMW", "328i", 2018)

print(f" three_series.crusie_control_enabled ===> {three_series.crusie_control_enabled}" )
print(f" three_series.model ===> {three_series.model}" )
print(f" three_series.make ===> {three_series.make}" )
print(f" three_series.year ===> {three_series.year}" )


five_series=  Five_series(True, "BMW", "328i", 2018)

print(f" five_series.parking_assist_enabled ===> {five_series.parking_assist_enabled}" )
print(f" five_series.model ===> {five_series.model}" )
print(f" five_series.make ===> {five_series.make}" )
print(f" five_series.year ===> {five_series.year}" )

five_series.start()
five_series.stop()

