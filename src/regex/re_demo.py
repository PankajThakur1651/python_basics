import re
string = "Take up one idea. one idea at a time"


def search_findall_match():
    result = re.search(r'o\w', string)
    print(result.group())
    # findall finds all the occurrences of regex in the str
    result = re.findall(r'o\w\w', string)
    print(result)
    # match finds all the occurrences of regex in the str
    result = re.match(r'o\w\w', string)
    if result is not None:
        print(f"Result is {result.group().upper()}")
    ## Substitute
    result = re.sub(r'one', 'two', string)
    print(f"Result is {result}")


def substitute_split():
    string = "1Take 234up one idea. 987one idea at a time"
    result = re.sub(r'one', 'two', string)
    print(f"Result is {result}")
    print(f"str is {string}")
    result = re.split(r'\d+', string)
    print(result)




if __name__ == '__main__':
    search_findall_match()
    substitute_split()
