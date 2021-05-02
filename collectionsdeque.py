from collections import deque

numCommands = int(input())

d = deque()

for cmd in range(numCommands):
    command = input().split(' ')
    if command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'appendleft':
        d.appendleft(int(command[1]))
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()

print(*d, sep=' ')
