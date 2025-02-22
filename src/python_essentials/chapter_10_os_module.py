import os

original_path=  os.getcwd()

print(f" CWD is: {os.getcwd()}")

print(os.stat("src/chapter_1_work_with_string.py"))
for dirpath, dirname, filenames in os.walk(os.getcwd()):
    print("current path", dirpath)
    print("dirname ", dirname)
    print("filenames", filenames)


# print JAVA_HOME
print(os.environ.get('JAVA_HOME'))

print(os.path.exists("/tmp/hello.txt"))

#print if it is directory
print(os.path.isdir("/tmp"))

#base name
print(os.path.basename("/tmp/hello.txt"))

holder=os.path.split("/tmp/hello.txt")
