x, k = input().split(' ')

string = input()

if (eval(string, {'x': int(x)})) == int(k):
    print(True)
else:
    print(False)
