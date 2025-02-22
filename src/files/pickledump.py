import pickle

import student as st

wbh = open("student.dac", "wb")

s = st.Student(123, "George", 90)

pickle.dump(s, wbh)

wbh.close()

rbh = open("student.dac", "rb")
obj = pickle.load(rbh)
obj.display()

rbh.close()
