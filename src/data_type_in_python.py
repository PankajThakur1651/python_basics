# Five Data Types

"""
1. None Type: an object Does not contain any Value
2. Numeric Types: int , float, complex
3. Sequence : str, bytes, bytearray, list, tuple, range
4. sets 
5. mapping
"""


def numeric_types():
    a = 12
    b = 11
    c = -10
    print(type(c))

    print(a, c)


def func():
    no_value = None
    print("no value : ".format(no_value))


def complex_binary_and_hexadecimal_boolean_types():
    d = 3 + 4j
    print(type(d))

    bin_literal = 0b1010
    print(bin_literal)

    hex_literal = 0xFF
    print(hex_literal)

    # Hex
    oct_literal = 0o123
    print(oct_literal)

    g = True
    print("bool is ".format(g))
    print(type(g))


if __name__ == "__main__":
    numeric_types()
    func()
    complex_binary_and_hexadecimal_boolean_types()
