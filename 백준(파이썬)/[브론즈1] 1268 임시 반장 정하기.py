n = int(input())
data = [list(map(int, input().split())) for i in range(n)]
max = 0
ID = 0
for i in range(n):
    cnt = 0
    result = [[0]*5 for i in range(n)]

    for j in range(5):
        for k in range(n):
            if k == i: 
                continue
            else:
                if data[i][j] == data[k][j]: 
                    result[k][j] = 1
    for l in result:
        if 1 in l:
            cnt += 1
    if max < cnt:
        max = cnt
        ID = i
print(ID+1)


