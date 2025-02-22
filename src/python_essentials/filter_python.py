func = lambda x, y: print("Sum is {}".format(x + y))

func(11, 12)


def func():
    x = 11
    if x == 11:
        print(x)
        value = 12
    else:
        value = 13


try:
    print(value)
except Exception as err:
    print("Error is: {}".format(err))
func()
