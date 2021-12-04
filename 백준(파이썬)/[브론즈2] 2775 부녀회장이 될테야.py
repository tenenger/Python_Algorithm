t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    floor = [i for i in range(1, n+1)]

    for j in range(k):
        for k in range(1, n):
            floor[k] += floor[k-1]
    print(floor[-1])