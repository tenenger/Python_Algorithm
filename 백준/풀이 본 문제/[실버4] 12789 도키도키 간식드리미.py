from collections import deque
n = int(input())
queue = deque(map(int, input().split()))
street = []
target = 1

while len(queue):
    if queue[0] == target:
        queue.popleft()
        target += 1
    else:
        street.append(queue.popleft())

    while len(street):
        if street[-1] == target:
            street.pop()
            target += 1
        else:
            break
if len(street) >= 1:
    print('Sad')
else:
    print('Nice')
