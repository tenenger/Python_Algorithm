n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

for i in range(n):
    if data[i][0] == k:
        index = i
for i in range(n):
    if data[index][1:] == data[i][1:]:
        print(i+1)
        break