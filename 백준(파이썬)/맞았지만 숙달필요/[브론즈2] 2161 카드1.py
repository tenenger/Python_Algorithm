from collections import deque
queue = deque([i for i in range(1, int(input())+1)])
result = []
save = 0
while True:
    result.append(queue.popleft())
    if len(queue) == 0:
        break
    save = queue.popleft()
    queue.append(save)
print(" ".join(map(str, result)))