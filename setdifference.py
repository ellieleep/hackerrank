numEnglish = input()

englishNewspaper = set()

[englishNewspaper.add(x) for x in input().split(' ')]

numFrench = input()

frenchNewspaper = set()

[frenchNewspaper.add(y) for y in input().split(' ')]

print(len(englishNewspaper.difference(frenchNewspaper)))
