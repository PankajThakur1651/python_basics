# Lambda syntax
 # lambda argument: expression
from functools import reduce
 
def square():
    f = lambda x: x*x
    result = f (10)
    print("Result is {}".format(result))
    
def even_or_odd():
    f = lambda x: True if (x %2==0) else False

    print(f(1))
    print(f(2))
    
def sum():
     func=  lambda x, y: x+y
     print("Sum is {}".format(func(11,12)))


def filter_usage():
    number_list= [1,2,3,4,5,6]
    result = filter(lambda x: x %2 ==0, number_list)
    print ("result is {}".format(list(result)))

def sum_using_reduce():
    number_list= [1,2,3,4,5,6]
    result = reduce(lambda x,y: x+y ,number_list)
    print(result)

# Use the map function and double the value of each element in the list
def double_every_value():
    number_list= [1,2,3,4,5,6]
    result = map(lambda x: x*2, number_list)
    print(list(result))
    
    
if __name__=="__main__":
    square()
    even_or_odd()
    sum()
    filter_usage()
    double_every_value()
    sum_using_reduce()