student_1  = {"roll_no": 101, "name": "Ajay", "class": "12th"}
student_2  = {"roll_no": 102, "name": "Vijay", "class": "10th"}

print(type(student_1))


list_of_Students  = [student_1,student_2]

for student in list_of_Students:
    print ("=======================================")
    for key , value in student.items():
        print(f"key {key} ---> value {value}")
        

# to delete a key from a dictionary
del student_1["name"]

for student in list_of_Students:
    print ("=======================================")
    for key , value in student.items():
        print(f"key {key} ---> value {value}")

