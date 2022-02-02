n, m =map(int, input().split())
arr = [input() for _ in range(n)]
a,b =0,0
for i in range(n):
    row_cnt = []
    for j in range(m):
        row_cnt.append(arr[i][j])
    if 'X' not in row_cnt:
        a += 1
for i in range(m):
    column_cnt = []
    for j in range(n):
        column_cnt.append(arr[j][i])
    if 'X' not in column_cnt:
        b += 1

print(max(a,b))
