n = int(input())
for inputs in range(n):
    x, y = input().split(' ')
    try:
        print(int(x) // int(y))
    except ZeroDivisionError as eZero:
        print("Error Code:", eZero)
    except ValueError as eValue:
        print("Error Code:", eValue)
