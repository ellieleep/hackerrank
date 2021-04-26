import itertools

[print(x, end=' ') for x in list(itertools.product(list(map(lambda x: int(x), input().split(' '))), list(map(lambda x: int(x), input().split(' ')))))]

