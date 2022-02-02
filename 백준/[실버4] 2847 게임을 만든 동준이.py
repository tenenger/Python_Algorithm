n = int(input())
data = [int(input()) for _ in range(n)]
result = 0
for i in range(n-2, -1, -1):
    if data[i] >= data[i+1]:
        cnt = data[i] - data[i+1] + 1
        data[i] -= cnt
        result += cnt
print(result)
