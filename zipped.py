numSubjects, numStudents = map(lambda x: x, input().split())
scores = []
studentIndex = [x for x in range(int(numSubjects))]
gradesDict = {}


def average(lst):
    return sum(lst) / len(lst)


for students in range(int(numStudents)):
    scores.append(list(map(float, input().split())))

studentScores = list(zip(studentIndex, *scores))

for sublist in studentScores:
    gradesDict[sublist[0]] = sublist[1:]

for student, scores in gradesDict.items():
    print("{0:.1f}".format(average(scores)))
