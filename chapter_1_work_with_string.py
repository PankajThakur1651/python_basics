message = "hello World"

# Length of the string
print (len(message))

print(f"hello  appears {message.count('hello')} times")

print(message.find('W'))

msg = message.replace('World', 'universe')

print(f"after replace message is : {msg}")

# to see all the methods present for an object
print(dir(str))

print ("print help for all methods")
print(help(str.lower))
