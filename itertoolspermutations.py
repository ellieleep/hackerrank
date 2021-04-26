from itertools import permutations

string, length = map(lambda x: x, input().split(' '))
[print(*z, sep='') for z in sorted(list(permutations(string, int(length))))]
