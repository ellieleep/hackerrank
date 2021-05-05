import re

S = input()
k = input()

pattern = re.compile(k)
r = pattern.search(S)

print(r)