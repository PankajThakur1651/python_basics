s = input("Enter something ")
print(s)

rev_str = "".join(reversed(s))

print(rev_str)

"""
Reverse the words in a string
"""

sentence = "All the power is with in you"

temp_sentence = sentence.split()

print(temp_sentence)

result = []

index = len(temp_sentence) - 1

while index >= 0:
    result.append(temp_sentence[index])
    index = index - 1
print(result)


words_reversed = " ".join(result)

print("Reversed word is " + words_reversed)


#### Reverse the character in a string
str = "C++ is performance efficient"
splited_str = str.split()
new_str = []
i = 0
while i < len(splited_str):
    new_str.append(" ".join(reversed(splited_str[i])))
    i = i + 1


print(new_str)
