n, m = map(int, input().split())

array = [True for _ in range(m+1)]

for i in range(2, m+1):
    if array[i] == True:
        j = 2
        while i * j <= m:
            array[i*j] = False
            j += 1

for k in range(n, m):
    if array[k]:
        print(k, end=" ")