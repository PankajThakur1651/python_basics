element_list = [10, 30, 20, 40]
print(type(element_list))
b = bytes(element_list)
print(type(b))

b_array = bytearray(element_list)
print(type(b_array))

print(b_array)


roll_no_dict = {1: "ABC", 2: "PQR", 3: "XYZ"}
print(roll_no_dict)

for key, value in roll_no_dict.items():
    print(" {}===>  {}".format(key, value))


### Imutable in Python

first_var = 10
second_var = 10

print(id(first_var))
print(id(second_var))

print(first_var is second_var)
