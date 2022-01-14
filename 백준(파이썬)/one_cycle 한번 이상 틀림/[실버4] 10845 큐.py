import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque()
for i in range(n):
    data = input().split()
    if len(data) == 2:
        queue.append(int(data[1]))
    else:
        if data[0] == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif data[0] == 'size':
            print(len(queue))
        elif data[0] == 'empty':
            if queue:
                print(0)
            elif not queue:
                print(1)
        elif data[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif data[0] == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
