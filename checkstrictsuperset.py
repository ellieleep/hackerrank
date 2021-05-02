A = set()

[A.add(int(b)) for b in input().split(' ')]

numSets = int(input())

isStrictSuperSet = False

for setNum in range(numSets):
    testSet = set()
    [testSet.add(int(c)) for c in input().split(' ')]
    if (A.issuperset(testSet)) and (len(A.difference(testSet)) > 0):
        isStrictSuperSet = True
    else:
        isStrictSuperSet = False
        break

print(isStrictSuperSet)
