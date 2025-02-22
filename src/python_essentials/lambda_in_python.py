
def sum(a,b):
    print(a+b)
    
def func(recive_lambda):
    recive_lambda(11,12)
func(lambda x,y: sum(x,y))

