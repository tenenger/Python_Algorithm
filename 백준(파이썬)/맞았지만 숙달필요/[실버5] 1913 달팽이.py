n = int(input())
m = int(input())
r, c = n//2, n//2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
arr = [[0]*n for _ in range(n)]
num = 1
arr[r][c] = num

i = 0
while r != 0 or c != 0:
    r += dx[i]
    c += dy[i]
    num += 1
    if arr[r][c] != 0:
        r -= dx[i]
        c -= dy[i]
        i -= 1
        r += dx[i]
        c += dy[i]
        arr[r][c] = num
    else:
        arr[r][c] = num
    i += 1
    if i == 4:
        i = 0
for j in arr:
    print(" ".join(map(str, j)))


# 2차원 리스트의 인덱스 값 구하기 외우기
result = [[i+1,j+1] for i in range(n) for j in range(n) if arr[i][j]==m]
for a in result:
    print(" ".join(map(str, a)))