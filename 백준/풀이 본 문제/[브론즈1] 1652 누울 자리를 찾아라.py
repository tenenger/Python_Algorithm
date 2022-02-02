n = int(input())
arr = [input() for i in range(n)]
row_cnt = 0
column_cnt = 0
r_cnt  = 0
c_cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == '.':
            r_cnt += 1
        elif arr[i][j] == 'X':
            if r_cnt >= 2:
                row_cnt += 1
            r_cnt = 0
    if r_cnt >= 2:
        row_cnt += 1
    r_cnt = 0

    for k in range(n):
        if arr[k][i] == '.':
            c_cnt += 1
        elif arr[k][i] == 'X':
            if c_cnt >= 2:
                column_cnt += 1
            c_cnt = 0
    if c_cnt >= 2:
        column_cnt += 1
    c_cnt = 0
print(row_cnt, column_cnt)