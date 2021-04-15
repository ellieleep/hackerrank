studentRecords = []

for student in range(int(input())):
    name = input()
    score = float(input())
    studentRecords.append([name, score])

sortedRecords = sorted(studentRecords, reverse=True, key=lambda studentRec: studentRec[1])

lowest = sortedRecords[-1]
nextLowest = sortedRecords[-2]

for student in sortedRecords:
    if student[1] == lowest[1]:
        lowest = student[(student.index()-1)]
        nextLowest = student[(student.index()-2)]

for student in sortedRecords:
    if student[1] == nextLowest[1] and student[0] != nextLowest[0] and student[1] != lowest[1]:
        print(student[0])
