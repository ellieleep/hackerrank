import re

s = input()
result = re.split(r'(^|,|\.)(\d*)', s)
for x in result:
    if not x == '' and not x == ',' and not x == '.':
        print(x)