setSize = int(input())

s = set([int(x) for x in input().split(' ')])

commandNum = int(input())

for command in range(commandNum):
    cmd = input().split(' ')
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        try:
            s.remove(int(cmd[1]))
        except KeyError:
            pass

print(sum(s))
