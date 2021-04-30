import itertools

string, combinations = input().split(' ')

for numComb in range(1, int(combinations)+1):
    combo = list(itertools.combinations(sorted(string), int(numComb)))
    for item in combo:
        print(''.join(item))