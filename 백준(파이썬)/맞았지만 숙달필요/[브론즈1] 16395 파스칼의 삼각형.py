n, k = map(int,input().split())
arr = [[0]*32 for i in range(32)]

for i in range(1, n+1):
    for j in range(1, i+1):
        if i == j or j== 1:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
print(arr[n][k])