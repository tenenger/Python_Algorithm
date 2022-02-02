import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque()
for _ in range(n):
    command = input().split()
    if len(command) == 2:
        queue.append(command[1])
    else:
        if command[0] == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif command[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif command[0] == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
