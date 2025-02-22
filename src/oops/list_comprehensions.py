'''lst =[]
for value in range (1,11):
    lst.append(value**3)

print(lst)'''

#### cube using a comprehensive list
values = []
values = [x ** 3 for x in range(1, 11) if x > 2]

print(values)

##### List to create only even numbers
roll_number_list = [1, 2, 3, 4]
even_list = [x for x in roll_number_list if x % 2 == 0]

print(even_list)

###### Product of numbers in a list
first_list = [1, 2, 3, 4]
second_list = [1, 2, 3, 4]
resultant_list = []

resultant_list = [first_list[index] * second_list[index] for index in range(len(first_list))]

print(resultant_list)

############ Common Numbers in a list
first = [1, 2, 3, 4, 5, 6]
second = [2, 4, 6]
result = []

result = [item for item in first if item in second]

print(result)
