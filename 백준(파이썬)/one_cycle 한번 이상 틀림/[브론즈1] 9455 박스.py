t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(m)]
    result = 0
    while True:
        cnt = 0
        for i in range(m-1):
            for j in range(n):
                if arr[i][j] == 1 and arr[i+1][j] == 0:
                    arr[i][j] = 0
                    arr[i+1][j] = 1
                    cnt += 1
        result += cnt
        if cnt == 0:
            break
    print(result)