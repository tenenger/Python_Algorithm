n, k = map(int, input().split())
data = list(map(int, input().split()))
max_number = -9999
for i in range(n-k+1):
    max_number = max(max_number, sum(data[i:i+k]))
print(max_number)
