class Player:
    def __init__(self):
        self.__name = None # variable preceded by __ is private variable
        self.__matches = None

    def set_matches(self, matches):
        self.__matches = matches

    def get_matches(self):
        return  self.__matches

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return  self.__name

    def display(self):
        print(f"name :  {self.__name}")
        print(f"matches played are : {self.__matches}")


virat =  Player()
virat.set_matches(11)
virat.set_name("Virat")

virat.display();
