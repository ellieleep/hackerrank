numEnglish = input()

englishPapers = set()

[englishPapers.add(x) for x in input().split(' ')]

numFrench = input()

frenchPapers = set()

[frenchPapers.add(y) for y in input().split(' ')]

resultSet = set()

[resultSet.add(z) for z in frenchPapers.intersection(englishPapers)]

print(len(resultSet))
