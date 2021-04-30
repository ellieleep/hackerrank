numM = [int(w) for w in input()]

M = [int(x) for x in input().split(' ')]

numN = [int(y) for y in input()]

N = [int(z) for z in input().split(' ')]

setM = set(M)

setN = set(N)

resultList = list(setM.difference(setN)) + list(setN.difference(setM))

resultList.sort()

for number in resultList:
    print(number)
