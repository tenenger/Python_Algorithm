from collections import deque
queue = deque()
n, m = map(int, input().split())
world_map = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_type = ['상', '하', '좌', '우']

def bfs(x, y) :
    queue.append((x, y))
    while queue :
        x, y = queue.popleft()
        for _ in range(4) :
            nx = x + dx[_]
            ny = y + dy[_]
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 :
                continue
            if world_map[nx][ny] == 0 :
                continue
            if world_map[nx][ny] == 1 :
                world_map[nx][ny] = world_map[x][y] + 1
                queue.append((nx, ny))
    return world_map[n-1][m-1]

print(bfs(0,0))