import sys
from collections import deque
input = sys.stdin.readline
deque = deque()
number = int(input())
for _ in range(number):
    data = list(input().split())
    if len(data) == 2:
        if data[0] == 'push_front':
            deque.appendleft(int(data[1]))
        elif data[0] == 'push_back':
            deque.append(int(data[1]))
    else:
        if data[0] == 'size':
            print(len(deque))
        elif data[0] == 'empty':
            if deque:
                print(0)
            else:
                print(1)
        elif data[0] == 'front':
            if deque:
                print(deque[0])
            else:
                print(-1)
        elif data[0] == 'back':
            if deque:
                print(deque[-1])
            else:
                print(-1)
        elif data[0] == 'pop_front':
            if deque:
                print(deque.popleft())
            else:
                print(-1)
        elif data[0] == 'pop_back':
            if deque:
                print(deque.pop())
            else:
                print(-1)
