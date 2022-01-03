n = int(input())

data = [list(map(int, input().split())) for i in range(n)]

data.sort(key=lambda x: -x[2])
result = []


for i in data:
    cnt = 0
    for j in range(len(result)):
        if result[j][0] == i[0]:
            cnt += 1
    if cnt >= 2:
        continue
    if len(result) == 3:
        break
    result.append(i)
for j in result:
    print(j[0], j[1])