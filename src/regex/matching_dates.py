import re

date_str = 'are you going on a date on 16-02-2025 or 16-03-2025 or 1-1-209'

regex = r'\d{1,2}-\d{1,2}-\d{4}'

print(re.findall(regex, date_str))
