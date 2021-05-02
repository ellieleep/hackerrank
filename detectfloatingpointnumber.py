import re

numInputs = int(input())

validFloatRe = re.compile(r'^[+-]?\d*\.\d+$')

for inputString in range(numInputs):
    mo = validFloatRe.match(input())
    if mo:
        print(True)
    else:
        print(False)
