numSteps = int(input())

steps = [step for step in input()]

distanceFromLevel = 0

valleyCounter = 0

for step in steps:
    if distanceFromLevel == 0 and step == 'U':
        distanceFromLevel += 1
        continue
    elif distanceFromLevel == 0 and step == 'D':
        distanceFromLevel += -1
        valleyCounter += 1
        continue
    elif distanceFromLevel < 0 and step == 'U':
        distanceFromLevel += 1
        continue
    elif distanceFromLevel < 0 and step == 'D':
        distanceFromLevel -= 1
        continue
    elif distanceFromLevel > 0 and step == 'U':
        distanceFromLevel += 1
        continue
    elif distanceFromLevel > 0 and step == 'D':
        distanceFromLevel -= 1
        continue

print(valleyCounter)