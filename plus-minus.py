numDigits = int(input())

digitList = [int(x) for x in input().split(' ')]

numPos = 0
numNeg = 0
numZero = 0

for y in digitList:
    if y > 0:
        numPos += 1
    elif y < 0:
        numNeg += 1
    else:
        numZero += 1

print('{0:.6f}'.format(numPos/numDigits))
print('{0:.6f}'.format(numNeg/numDigits))
print('{0:.6f}'.format(numZero/numDigits))
