n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    result = []
    for j in range(m):
        result.append(a[i][j] + b[i][j])
    print(" ".join(map(str, result)))