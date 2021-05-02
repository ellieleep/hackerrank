numEnglishPapers = input()

englishPapers = set()

[englishPapers.add(x) for x in input().split(' ')]

numFrenchPapers = input()

frenchPapers = set()

[frenchPapers.add(y) for y in input().split(' ')]

resultSet = set()

[resultSet.add(z) for z in englishPapers.union(frenchPapers)]

print(len(resultSet))
