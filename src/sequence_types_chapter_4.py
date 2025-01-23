# Basic Types

name = "You are Awesome"

print(name)
# get the 5th character

print("first character is {}".format(name[0]))

print("Length is: {}".format(len(name)))

## Slice a string

print(name[0:7])  # You are
print(name[0:])  # You are Awesome
print(name[-3:-1])  # -1 is index of last element

print(name[::-1])  # reverse a string


## Strip  a space
string_to_split = "    My Name is       I  do not know   "

print(string_to_split.strip())  # strip on both side of string
print(string_to_split.lstrip())  # strip on left side of string
print(string_to_split.rstrip())  # strip on right side of string

resultant_string = string_to_split.replace(" ", "")
print(resultant_string)


## Find in the string
print(name.find("Awe", 0, len(name)))  # find(sub, start from, until the length)
# few other functions are count, replace, upper, lower

print(name.title())


first_list = [1, "1.2", "Mr Richards"]
first_list.append("B.tech")

print(first_list)

del first_list[0]
print(first_list)


first_tuple = (1, 2, 2, 3, 4, "pankaj")
print("Elements in tuple are {}".format(first_tuple))


first_set = {10, 20, "xyz", 10}

first_set.update([99, 120])

print(first_set)

# frozen set
f = frozenset(first_set)
first_set.update("Thakur")

print(type(f))

### Range type
range_1 = range(0, 5)
print("range is {}".format(range_1))
for i in range(0, 20):
    print("i is {}".format(i))
