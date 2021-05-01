import re

numRegex = int(input())

regexList = []

for x in range(numRegex):
    regexList.append(input())

for regex in regexList:
    try:
        re.compile(regex)
        print('True')
    except Exception:
        print('False')
