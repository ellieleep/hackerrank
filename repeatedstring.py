import itertools

s = input()
n = int(input())

lettercount = 0

for i, letter in enumerate(itertools.cycle(list(s))):
    if letter == 'a' and i < n:
        lettercount += 1
    elif i == n:
        print(lettercount)
        break
