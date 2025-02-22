import re


def match_escaped_dot(text):
    """Matches a literal dot (.) in a string."""
    pattern = r"\."
    return re.findall(pattern, text)


def match_any_character(text):
    """Matches any character except newline."""
    pattern = r"c.t"
    return re.findall(pattern, text)


def match_start(text):
    """Matches 'Hello' at the start of the string."""
    pattern = r"^Hello"
    return re.findall(pattern, text)


def match_end(text):
    """Matches 'world' at the end of the string."""
    pattern = r"world$"
    return re.findall(pattern, text)


def match_vowels(text):
    """Matches any vowel in the string."""
    pattern = r"[aeiou]"
    return re.findall(pattern, text)


def match_consonants(text):
    """Matches non-vowel characters."""
    pattern = r"[^aeiou]"
    return re.findall(pattern, text)


def match_group(text):
    """Finds occurrences of 'ab' in the string."""
    pattern = r"(ab)+"
    return re.findall(pattern, text)


def match_either_cat_or_dog(text):
    """Matches 'cat' or 'dog' in the string."""
    pattern = r"(cat|dog)"
    return re.findall(pattern, text)


def main():
    text = "Hello world. cat cut ababab dog"

    print("1. Escaped Dot:", match_escaped_dot(text))
    print("2. Any Character:", match_any_character(text))
    print("3. Match Start:", match_start(text))
    print("4. Match End:", match_end(text))
    print("5. Match Vowels:", match_vowels(text))
    print("6. Match Consonants:", match_consonants(text))
    print("7. Match Group (ab):", match_group(text))
    print("8. Match Either 'cat' or 'dog':", match_either_cat_or_dog(text))


if __name__ == "__main__":
    main()
