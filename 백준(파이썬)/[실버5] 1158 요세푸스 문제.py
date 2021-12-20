from collections import deque
n, k = map(int, input().split())
arr = deque([i+1 for i in range(n)])
result = []
a = 1

while arr:
    if a % k != 0:
        arr.append(arr.popleft())
    else:
        result.append(arr.popleft())
        a = 0
    a += 1

print("<" + ", ".join(map(str, result)) + ">")