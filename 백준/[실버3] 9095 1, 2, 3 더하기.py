t = int(input())
d = [0] * 12
d[1], d[2], d[3] = 1, 2, 4
for _ in range(t):
    n = int(input())
    if n <= 3:
        print(d[n])
    else:
        for i in range(4, n + 1):
            d[i] = d[i-1] + d[i-2] + d[i-3]
        print(d[n])
