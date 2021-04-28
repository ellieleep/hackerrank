from collections import defaultdict

n, m = [int(x) for x in input().split(' ')]

listN = [input() for inputN in range(n)]
listM = [input() for inputM in range(m)]

dictFromLists = defaultdict(lambda: -1)

for iM, wordM in enumerate(listM):
    for iN, wordN in enumerate(listN):
        if wordN == wordM and wordM not in dictFromLists.keys():
            dictFromLists[wordM] = [iN + 1]
        elif wordN == wordM and wordM in dictFromLists.keys():
            dictFromLists[wordM].append(iN + 1)

for word in listM:
    if word in dictFromLists.keys():
        print(*dictFromLists[word])
    else:
        print(dictFromLists[word])

