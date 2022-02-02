from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
idxs = list(map(int, input().split()))
queue = deque([x for x in range(1, n+1)])
cnt = 0

for idx in idxs:
    while True:
        if queue[0] == idx:
            queue.popleft()
            break
        else:
            if queue.index(idx) <= len(queue)//2:
                while queue[0] != idx:
                    cnt += 1
                    queue.append(queue.popleft())
            else:
                while queue[0] != idx:
                    cnt += 1
                    queue.appendleft(queue.pop())
print(cnt)
