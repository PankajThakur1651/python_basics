try:
    f=open("test_folder/testfile.txt")
except FileNotFoundError:
    print("FileNotFoundError this file does not exists")
except Exception:
    print("Sorry something went wrong")
else:
    f_contents=f.read()
    print(f_contents)
finally:
    print("This will be executed forever !!!")


