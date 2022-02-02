
n = int(input())
m = int(input())
gredient = list(map(int, input().split()))
gredient.sort()
cnt = 0
start, end = 0, n-1
while start < end:
    sum = gredient[start] + gredient[end]
    if sum == m:
        start += 1
        end -= 1
        cnt += 1
    elif sum < m:
        start += 1
    elif sum > m:
        end -= 1
print(cnt)
