n = int(input())
student_marks = {}
student_averages = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()


def average(lst):
    return sum(lst) / len(lst)


for student, scores in student_marks.items():
    student_averages[student] = (average(scores))

for name, average in student_averages.items():
    if query_name == name:
        print(("{0:.2f}".format((student_averages[name]))))
