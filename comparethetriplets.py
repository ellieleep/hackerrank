listA = [int(x) for x in input().split(' ')]
listB = [int(y) for y in input().split(' ')]

aScore = 0
bScore = 0

for i in range(0, len(listA)):
    if listA[i] > listB[i]:
        aScore += 1
    elif listA[i] < listB[i]:
        bScore += 1
    elif listA[i] == listB[i]:
        pass

print(aScore, bScore, sep=' ')
