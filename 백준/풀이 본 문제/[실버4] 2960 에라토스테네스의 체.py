n, k = map(int, input().split())
data = [True for x in range(n+1)]
data[0], data[1] = False, False

start = 2
cnt = 0
while k != cnt:
    for i in range(start, n+1, start):
        if data[i]:
            data[i] = False
            cnt += 1
            if k == cnt:
                result = i
                break
    start += 1
print(result)
