def hello_func():
   return "Hello_world"

print(hello_func().upper())

def hello_func_with_greeting(greeting ,name = "you"):
       return '{} {}. '.format(greeting, name)

print(hello_func_with_greeting("Hi", "Raj"))

# Now learn about **args and **kwargs
def Student_info(*args, **kwargs):
    print(f"Args {args}")
    print(f"kwArgs {kwargs}")
    
    
Student_info("Raj", "Thakur", name="Something", roll_number=14)

name_1 = ("Raj", "Thakur")
dict_1= {"Name": "Ajay", "last_name": 22}

Student_info(*name_1, **dict_1)

