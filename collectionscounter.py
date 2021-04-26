from collections import Counter

input()
shoesCounter = Counter(list(map(lambda x: int(x), input().split(' '))))
total = 0
for purchase in range(int(input())):
    size, price = map(lambda x: int(x), input().split(' '))
    if size in shoesCounter.keys() and shoesCounter[size] > 0:
        total += price
        shoesCounter[size] -= 1
    else:
        pass

print(total)
