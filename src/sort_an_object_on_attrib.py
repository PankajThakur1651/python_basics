class Employee:
    def __init__(self, name, salary, age) -> None:
        self.name =name
        self.age=age
        self.salary=salary
    def __repr__(self):
        return f" {self.name}-{self.salary}-{self.age}" 
        


emp_1= Employee('Pankaj', 10000, 34)
emp_2= Employee('Arun', 20000, 35)

emp_list = [emp_1,emp_2]

def e_sort(employee):
    return employee.age

new_list = sorted(emp_list, key=e_sort)
#also one can use sort using lambda
new_list= sorted(emp_list, key=lambda l: l.name)

print(new_list)


