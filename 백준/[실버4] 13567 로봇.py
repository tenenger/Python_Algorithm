m, n = map(int, input().split())
x, y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 1
error = 0
for _ in range(n):
    command, num = input().split()
    num = int(num)
    if command == 'MOVE':
        if x + dx[direction] * num > m or x + dx[direction] * num < 0 or y + dy[direction] * num > m or y + dy[direction] * num < 0:
            error += 1
            continue
        else:
            x += dx[direction] * num
            y += dy[direction] * num
    else:
        if num == 0:
            if direction - 1 < 0:
                direction = 3
            else:
                direction -= 1
        else:
            if direction + 1 > 3:
                direction = 0
            else:
                direction += 1
if error > 0:
    print(-1)
else:
    print(x, y)
