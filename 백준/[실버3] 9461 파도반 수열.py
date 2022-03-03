import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    d = [1] * (n + 5)
    d[3], d[4] = 2, 2

    for i in range(5, n + 1):
        d[i] = d[i-1] + d[i-5]
    print(d[n-1])
