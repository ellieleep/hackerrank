import re

romanNumerals = input()

rnRegex = re.compile(r'M{0,3}D?C{0,4}L?X{0,4}V{0,4}I{0,4}')

mo = re.match(rnRegex, romanNumerals)

if mo:
    print(True)
else:
    print(False)