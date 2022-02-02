n, m = map(int, input().split())
a = [list(map(int, input().split()))for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]
result = [[0]*k for i in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j]+= a[i][l]*b[l][j]
for i in result:
    print(" ".join(map(str, i)), sep="\n")