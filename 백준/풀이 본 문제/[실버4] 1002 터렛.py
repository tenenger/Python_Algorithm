import math
t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)**2 + (y1 - y2)**2)
    if d == 0 and r1 == r2:
        print(-1)
    elif d == r1 + r2 or max(r1, r2) == d + min(r1, r2):
        print(1)
    elif d > r1 + r2 or max(r1, r2) > d + min(r1, r2):
        print(0)
    elif d < r1 + r2:
        print(2)
