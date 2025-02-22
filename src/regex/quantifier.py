import re


def one_or_more():
    pattern = r"\d+"
    text = "Order 123, Code 4567, Item 9"
    matches = re.findall(pattern, text)
    print(matches)  # Output: ['123', '4567', '9']


def zero_or_more():
    pattern = r"a*"
    text = "baaaac"
    matches = re.findall(pattern, text)
    print(matches)  # Output: ['', 'aaaa', '', '']


def zero_or_one():
    pattern = r"colou?r"
    text = "color and colour are correct"
    matches = re.findall(pattern, text)
    print(matches)  # Output: ['color', 'colour']

def exactly_m_times():
    pattern = r"\d{3}"
    text = "Order 123, Code 456, Item 78"
    matches = re.findall(pattern, text)
    print(matches)  # Output: ['123', '456']

if __name__ == '__main__':
    one_or_more()
    zero_or_more()
    zero_or_one()
    exactly_m_times()
