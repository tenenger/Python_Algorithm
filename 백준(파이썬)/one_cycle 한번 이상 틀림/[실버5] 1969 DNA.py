n, m = map(int, input().split())
data = [input() for _ in range(n)]
dna = ['A', 'C', 'G', 'T']
result = []
sum = 0

for j in range(m):
    column = []
    cnt = []
    for i in range(n):
        column.append(data[i][j])
    for k in range(4):
        cnt.append(column.count(dna[k]))
    result.append(dna[cnt.index(max(cnt))])
    sum += (n - max(cnt))
print("".join(result))
print(sum)
