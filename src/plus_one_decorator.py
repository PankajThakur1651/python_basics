import functools

#  Defining Functions Inside other Functions
def plus_one(number):
    def add_one(number):
        return number + 1

    result = add_one(number)
    return result


# Passing Functions as Arguments to other Functions


def plus_one(number):
    return number + 1


def function_call(function):
    number_to_add = 10
    return function(number_to_add)


print(function_call(plus_one))

## Function returning functions
def return_function():
    def say_helllo():
        return "say Hello"

    return say_helllo


# Nested Functions have access to the Enclosing Function's Variable Scope
def print_message(message):
    "Enclosong Function"

    def message_sender():
        "Nested Function"
        print(message)

    message_sender()


def basic_before_getting_into_decorator():
    print(plus_one(4))
    print(function_call(plus_one))
    print(return_function()())
    print_message("Hello there ??")


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    return "Hello There"


def first_decorator():
    print(say_hi())




### Apply Two decorator to single function


if __name__ == "__main__":
    basic_before_getting_into_decorator()
    first_decorator()

