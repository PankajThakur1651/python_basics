import os

original_path=  os.getcwd()

os.removedirs("Ths_is_created/hello")
os.makedirs("Ths_is_created/hello")
os.chdir("Ths_is_created/hello")

print(f" CWD is: {os.getcwd()}")

os.chdir(original_path);
print(f"Cwd is: {os.getcwd()}")

print(os.stat("chapter_1_work_with_string.py"))
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
print(type(holder))