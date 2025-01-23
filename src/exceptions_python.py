try:
    print(x)
except NameError:
    print("An Exception is occured")
except:
    print("Something Else went wrong")
finally:
    print("Nothing Went Wrong")


try:
    f = open("demofile.txt")
    try:
        f.write("This will be written into demofile.txt ")
    except:
        print("Something went wrong while writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


class MyException(Exception):
    def __init__(self, str):
        print("Constructor")


# raise an exception


def my_function(x: int):
    if x < 0:
        raise TypeError("sorry , no number below zero")


try:
    my_function(-2)
except TypeError:
    print("TypeError Exception")
except MyException:
    print("MyException is thrown")
