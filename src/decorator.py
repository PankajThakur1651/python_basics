def decorfunc(fun):
    def inner():
        result= fun()
        return result*2
    
    return inner
    
@decorfunc
def fun():
    return 2


def how_are_you(func):
    def inner(name):
        return func(name) + " how are you"
    
    return inner

@how_are_you
def hello(name):
    return "Hello " + name


def half(func):
    def inner():
        return func()/2
    
    return inner

def double(func):
    def inner():
        return func()*2
    
    return inner

@double
@half
def number():
    print("How many times")
    return 10
     
if __name__ == "__main__":
    print(fun())
    print(hello("Pankaj"))
    print(number())