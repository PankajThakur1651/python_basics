list_1 = ["physics" , "chemistry", "math"]

list_1.append("CS")

print(type(list))

print (list_1[-1])

# first 2 value from the list
print(f"first two value from list {list_1[0:2]}")
# method to append (.append())
# method to insert at certain position (.insert(position, value))
# method to ad the value from other list (.extend())
list_2 = ['Science', 'Commerce']
list_1.extend(list_2)

print("Now contents are {}". format(list_1))
# To remove (.remove, .pop)

# Sort in  reverse order
num_list = [9,7,19,99,101,6,8]
num_list.sort(reverse=True)

print (num_list)

# find the index of some value in the list
print(f"index is -- {num_list.index(99)}")

#print index with value in for loop enumerate
for index, value in enumerate (num_list ,start=1):
    print (f"{index} ---> {value}")

courses  = ['Hindi', 'english', 'science']
# join courses with comma, opposite of join is split
x = " - ".join(list_1)

print (x)
# tuple_1 = ()
#tuples are immutable while list is mutable 
# list is created by var = [] or var =list()
# list is created by var = () or var =tuple

# sets now 

set_var = {1,2,3,4}
set_var_2  = {1,3,5,6}

print(set_var.intersection(set_var_2))

print(set_var.difference(set_var_2))

print(set_var.union(set_var_2))

