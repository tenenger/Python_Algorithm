import sys
input = sys.stdin.readline

board = [[0]*101 for _ in range(101)]
testcase = int(input())
for _ in range(testcase):
    x, y = map(int, input().split())
    for j in range(y, y+10):
        for i in range(x, x+10):
            board[j][i] = 1
cnt = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            for k in range(4):
                x = j+dx[k]
                y = i+dy[k]
                if board[y][x] == 0:
                    cnt += 1
print(cnt)
