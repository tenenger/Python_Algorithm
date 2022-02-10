n = int(input())
if n == 0:
    print(0)
else:
    d = [0] * (n+1)
    d[1] = 1
    for i in range(2, n+1):
        d[i] = (d[i-2] + d[i-1]) % 1000000007
    print(d[n])
