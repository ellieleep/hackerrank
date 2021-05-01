numStamps = int(input())

stamps = set()

[stamps.add(input().strip()) for x in range(numStamps)]

print(len(stamps))