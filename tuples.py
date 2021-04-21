numInts = input()
intTuple = tuple(map(lambda x: int(x), input().split()))
print(hash(intTuple))
print(hash((1, 2)))
