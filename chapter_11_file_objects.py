import os

# with open("test.txt", 'r') as file:
#     # file.read() will read all line, 
#     #file.readlines will also read all lines
#     for line in file:
#         print(line, end='')


# file.seek set the file pointer to desired place
with open("test.txt", 'r') as file:
    size_to_read=10
    f_contents= file.read(size_to_read)
    obj = file.tell
    print(obj())    
    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents= file.read(size_to_read)
        
# MODES 
#r for read , w for write and r+ for read and write, a is for append

# read the contents of one file to the another file

with open("test.txt", 'r') as read_file:
    with open("test_2.txt", 'w') as write_file:
        size_to_read = 10
        f_contents=read_file.read(size_to_read)
        while len(f_contents) > 0:
            write_file.write(f_contents)
            f_contents=read_file.read(size_to_read)

