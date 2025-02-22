a, b = [int (x) for x in input("Enter two numbers ").split()]

try:
    result = a/b
    print(f"Result is {result}")
except ZeroDivisionError:
    print("Divide By Zero Exception")

else:
    print("No exception was thrown")

finally:
    print("Finally here no matter if exception happened or not")
    print("Cleanup Can be handled here")
