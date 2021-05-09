lines = int(input())

list = []

for x in range(lines):
    row = [int(y) for y in input().split()]
    list.append(row)

sumArray = []
diagIndex = 0

for z in range(lines):
    sumArray.append(list[z][diagIndex])
    diagIndex += 1

differenceArray = []
diagIndex = len(list) - 1

for a in range(lines):
    differenceArray.append(list[a][diagIndex])
    diagIndex -= 1

print(abs(sum(sumArray) - sum(differenceArray)))
