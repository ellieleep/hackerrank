studentRecords = []
scores = set()
second_lowest_names = []

for student in range(int(input())):
    name = input()
    score = float(input())
    studentRecords.append([name, score])
    scores.add(score)

second_lowest = sorted(scores)[1]

for name, score in studentRecords:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name)

