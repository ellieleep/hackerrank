numStairs = int(input())

for x in range(1, numStairs + 1):
    step = x*'#'
    print(step.rjust(numStairs))