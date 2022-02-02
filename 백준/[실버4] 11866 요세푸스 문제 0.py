from collections import deque
n, k = map(int, input().split())
data = deque([x for x in range(1, n+1)])
cnt = 0
result = []
while data:
    if cnt+1 == k:
        result.append(data.popleft())
        cnt = 0
    else:
        data.append(data.popleft())
        cnt += 1
print('<' + ", ".join(map(str, result)) + '>')
