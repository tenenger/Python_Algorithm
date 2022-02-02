n = int(input())
students = []
older = []
young = []

for _ in range(n):
    student = input().split()
    student[1:] = map(int, student[1:])
    students.append(student)

students.sort(key= lambda x: (x[-1], x[-2], x[-3]))

print(students[-1][0], students[0][0], sep="\n")