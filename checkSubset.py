numTestCases = int(input())

for a in range(numTestCases):
    numSetA = input()
    setA = set()
    [setA.add(int(b)) for b in input().split(' ')]
    numSetB = input()
    setB = set()
    [setB.add(int(c)) for c in input().split(' ')]
    if setA.issubset(setB):
        print(True)
    else:
        print(False)
