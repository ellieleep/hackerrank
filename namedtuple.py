from collections import namedtuple

numStudents = int(input())

headings = input().split()

Student = namedtuple('Student', headings)

Students = []

for students in range(numStudents):
    dataLine = input().split()
    Students.append(Student(*dataLine))

totalScore = 0

for student in Students:
    totalScore += int(student.MARKS)

print(("{0:.2f}".format((totalScore / numStudents))))
