import sys
from collections import deque
number = int(sys.stdin.readline())
data = deque([x for x in range(1, number+1)])
while len(data) >= 2:
    data.popleft()
    a = data.popleft()
    data.append(a)
print(data.popleft())
