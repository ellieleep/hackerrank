import re

rexp = re.compile(r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]?([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]+')
resultList = rexp.findall(input())
if not resultList:
    print(-1)
else:
    print(*resultList, sep='\n')
