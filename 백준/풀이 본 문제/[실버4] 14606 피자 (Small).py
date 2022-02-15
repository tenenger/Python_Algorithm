n = int(input())
d = [0] * 11
d[1], d[2] = 0, 1

for i in range(3, n+1):
    m = i // 2
    d[i] = m * (i-m) + d[m] + d[i-m]
print(d[n])
