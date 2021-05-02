import itertools

string, combinations = input().split(' ')

resultList = list(itertools.combinations_with_replacement(sorted(string), int(combinations)))
for item in resultList:
    print(''.join(item), sep='')
