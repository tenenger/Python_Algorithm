n, m = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
left, right = 0, 1
while True:
    if left > right or right > n:
        break
    total = sum(numbers[left:right])
    if total == m:
        cnt += 1
        right += 1
    elif total < m:
        right += 1
    else:
        left += 1
print(cnt)