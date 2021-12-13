n = int(input())
data = []
for i in range(n):
    data.append(input())

for j in data:
    if j[::-1] in data:
        print(len(j), j[len(j)//2])
        break