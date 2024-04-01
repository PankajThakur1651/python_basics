'''
LEGB
Local, Enclosing, Global, Builtin
'''
#can define x as global
x = 'global x'

def test():
    global x
    y = 'local y'
    print(y)
    
    
test()
print(x)

def change_global_variable():
    x = 'local x'
    print(x)
    
change_global_variable()
print(x)


#override minimum function defined in standard
def min():
    pass

#built in
# print(min(1,2))  This line will not compile now


# Enclosing one now
def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        # to change the x in outer scope one can use nonlocal x
        print(f"inner x is {x}")
        
    inner()
    print(x)
    

outer()