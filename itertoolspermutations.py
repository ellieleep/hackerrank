from itertools import permutations

string, length = input().split(' ')
for z in sorted(list(permutations(string, int(length)))):
    print(*z, sep='')
