# comparisons
# Equal ==
# not Equal !=
#Greater than >
#less than <
# Greater or equal to >=
# object identity


Language = 'Java'

if Language is 'Python':
    print ("Language is Python")
elif Language is 'Java':
    print("Language is Java")
else:
    print("It is not python or Java")
    

user = "Admin"
logged_in =True
if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Bad Credentials")
     
First_person_name = "Raj"
second_person_name = "Thakur"

print (First_person_name is second_person_name)

# above statement is Equivalent of 

print(id(First_person_name) ==id(second_person_name))
