class Student:
    def __init__(self, id, name, test_score):
        self.id =id
        self.name=name
        self.test_score= test_score

    def display(self):
        print(self.id, self.name, self.test_score, sep=" ")




