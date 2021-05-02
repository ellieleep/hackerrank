setLength = input()

s = set()

[s.add(int(x)) for x in input().split(' ')]

numCommnads = int(input())

for y in range(numCommnads):
    command = input().split(' ')
    mutationSet = set()
    [mutationSet.add(int(z)) for z in input().split(' ')]
    if command[0] == 'intersection_update':
        s.intersection_update(mutationSet)
    elif command[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(mutationSet)
    elif command[0] == 'difference_update':
        s.difference_update(mutationSet)
    elif command[0] == 'update':
        s.update(mutationSet)

print(sum(s))
