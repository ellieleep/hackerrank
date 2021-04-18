listObject = []
n = int(input())
for number in range(n):
    command = list(map(lambda x: x, input().split()))
    if command[0] == 'insert':
        listObject.insert(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(listObject)
    elif command[0] == 'remove':
        if int(command[1]) in listObject:
            listObject.remove(int(command[1]))
    elif command[0] == 'append':
        listObject.append(int(command[1]))
    elif command[0] == 'sort':
        listObject = sorted(listObject)
    elif command[0] == 'pop':
        listObject.pop()
    elif command[0] == 'reverse':
        listObject.reverse()
