numEnglish = input()

englishNewspapers = set()

[englishNewspapers.add(x) for x in input().split(' ')]

numFrench = input()

frenchNewspapers = set()

[frenchNewspapers.add(y) for y in input().split(' ')]

print((len(englishNewspapers.symmetric_difference(frenchNewspapers))))
