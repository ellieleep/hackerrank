import itertools
import string
import numpy as np

s = input()
n = int(input())

alphabet = dict(zip(string.ascii_lowercase, [int(x) for x in range(1, 27)]))

stringArray = np.array([alphabet[x] for x in s])

letterCount = 0

for i, letter in enumerate(itertools.cycle(np.nditer(stringArray))):
    if letter == 1 and i < n:
        letterCount += 1
    elif i == n:
        print(letterCount)
        break
