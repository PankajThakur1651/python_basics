import  threading

if __name__ =='__main__':
    print(f"Current Thread name is {threading.current_thread().name}")


if threading.current_thread() == threading.main_thread():
    print("Main Thread")
else:
    print("Some Other thread")