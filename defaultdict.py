from collections import defaultdict

n, m = [int(x) for x in input().split(' ')]

listN = [input() for inputN in range(n)]
listM = [input() for inputM in range(m)]

dictFromLists = defaultdict(list)

[dictFromLists['listN'].append(wordN) for wordN in listN]
[dictFromLists['listM'].append(wordM) for wordM in listM]

for wordM in dictFromLists['listM']:
    for i, wordN in enumerate(dictFromLists['listN']):
        if wordM not in dictFromLists['listN']:
            print(-1, end='')
            break
        if wordM == wordN:
            print(i+1, end=' ')
    print()

