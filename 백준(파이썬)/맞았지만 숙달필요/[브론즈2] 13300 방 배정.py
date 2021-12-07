import math
n, k = map(int, input().split())
data = [list(map(int ,input().split())) for i in range(n)]
w = []
m = []

for i in range(n):
    if data[i][0] == 1:
        w.append(data[i][1])
    else:
        m.append(data[i][1])

result = 0
for i in range(1, 6+1):
    result += math.ceil(m.count(i)/k)
    result += math.ceil(w.count(i)/k)
print(result)