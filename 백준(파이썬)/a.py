n, score, p = map(int, input().split())
if n == 0:
    print(1)
else:
    data = list(map(int, input().split()))
    if n == p and score <= data[-1]:
        print(-1)
    else:
        rank = n + 1
        for i in range(n):
            if data[i] <= score:
                rank = i +1
                break
        print(rank)