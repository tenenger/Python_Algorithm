t = int(input())
d = [0]*1001
for i in range(1, 1000):
    d[i] = d[i-1] + i

for i in range(t):
    a = int(input())

    for i in range(1, a+1):
        for j in range(1, a+1):
            for k in range(1, a+1):
                if d[i]+d[j]+d[k] > a:
                    break

                if a == d[i]+d[j]+d[k]:
                    a = 1
                    break
    print(1) if a == 1 else print(0)


