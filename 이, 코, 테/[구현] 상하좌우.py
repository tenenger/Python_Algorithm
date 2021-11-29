# [구현] 상하좌우.txt

n = int(input())
data = input().split()
x, y = 1, 1
nx, ny = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['L', 'R', 'U', 'D']

for i in data :
    for j in range(len(move_types)) :
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
        if nx == 0 or ny == 0 or nx == n+1 or ny == n+1 :
            continue
        x, y = nx, ny
print(x, y)
