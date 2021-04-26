from itertools import permutations

string, length = map(lambda x: x, input().split(' '))
results = list(permutations(string, int(length)))
pass
