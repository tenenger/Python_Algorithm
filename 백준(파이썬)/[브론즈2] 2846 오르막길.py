n = int(input())
data = list(map(int, input().split()))
result = 0
for i in range(n-1):
    for j in range(i+1, n):
        if data[i] < data[j] and data[j-1] < data[j]:
            a = data[j] - data[i]
            if result < a:
                result = a
        elif data[j-1] >= data[j]:
            break
print(result)