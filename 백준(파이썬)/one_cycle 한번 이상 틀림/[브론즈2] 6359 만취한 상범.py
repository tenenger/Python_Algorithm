t = int(input())

for i in range(t):
    n = int(input())
    d = [1]*n
    for j in range(1, n):
        for k in range(j, n, j+1):
            if d[k] == 0:
                d[k] = 1
            else:
                d[k] = 0
    print(sum(d))