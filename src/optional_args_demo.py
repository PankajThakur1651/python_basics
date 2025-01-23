def my_func(x, *shanu,  **pankaj):
    print(x)
    print("===============")
    pankaj['e_id'] =1000
    print(type(shanu))
    for val in shanu:
        print(val)
    
    for key, val in pankaj.items():
        print( "{} ==> {}".format(key,val))
    
my_func(10, 12,14,18, name = "Pankaj", sal=1000000)


