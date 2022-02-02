n = int(input())
count = 0
d = [5001]*(n+3)
d[3] = 1
d[5] = 1

for i in range(6, n+1):
    d[i] = min(d[i-3]+1, d[i-5]+1)

if d[n] >= 5001:
    print(-1)
else:
    print(d[n])

