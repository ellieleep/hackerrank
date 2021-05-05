numClouds = int(input())
clouds = [int(cloud) for cloud in input().split(' ')]

numJumps = 0
currentPlatform = 0

while not currentPlatform == (len(clouds) - 1):
    try:
        if clouds[currentPlatform + 2] != 1 and (clouds[currentPlatform + 2] < len(clouds) - 1):
            currentPlatform += 2
            numJumps += 1
        elif clouds[currentPlatform + 2] == 1:
            currentPlatform += 1
            numJumps += 1
    except IndexError:
        currentPlatform += 1
        numJumps += 1

print(numJumps)
