numNums = input()
listNums = [int(x) for x in input().split()]
print(all([int(x) > 0 for x in listNums]) and (any([(sorted(str(y)) == sorted(str(y), reverse=True)) for y in listNums])))
