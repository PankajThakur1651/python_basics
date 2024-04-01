import os, sys
module_path = os.getcwd()
print("Current Directory", module_path)
sys.path.append(module_path)

import modules.chapter_9_module as mm
from modules.chapter_9_module import find_index
from modules.chapter_9_module import my_var
import sys
import os
import datetime
import calendar


str="Raj Thakur"
target ="T"

print(mm.find_index(str, target))
print(find_index("Ajay Thakur", 'T'))

print(f"My Variable is {my_var}")


print(calendar.isleap(2020))
