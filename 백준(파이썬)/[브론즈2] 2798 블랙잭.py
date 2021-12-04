n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0
for i in range(n-2):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if data[i]+data[j]+data[k] > m :
                continue
            else :
                collect = data[i]+data[j]+data[k]
                if result < collect:
                    result = collect
print(result )
