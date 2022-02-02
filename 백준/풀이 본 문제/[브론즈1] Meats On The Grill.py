t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    grill = [list(input()) for _ in range(h)]
    for row in reversed(grill):
        print("".join(row))

