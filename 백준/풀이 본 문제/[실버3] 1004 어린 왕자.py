from math import sqrt
t = int(input())
for _ in range(t):
    start_x, start_y, land_x, land_y = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        result = 0
        circle_x, circle_y, radius = map(int, input().split())
        if sqrt(pow((start_x - circle_x), 2) + pow((start_y - circle_y), 2)) < radius:
            result += 1
        if sqrt(pow((land_x - circle_x), 2) + pow((land_y - circle_y), 2)) < radius:
            result += 1
        if result == 2:
            result = 0
        cnt += result
    print(cnt)