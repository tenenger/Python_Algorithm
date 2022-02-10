n = int(input())
if n <= 1:
    print(0)
elif n <= 2:
    print(2)
else:
    d = [0] * (n + 1)
    d[2], d[3] = 2, 3
    for i in range(4, n+1):
        d[i] = (d[i-1] + d[i-2]) % 10
    print(d[n])
