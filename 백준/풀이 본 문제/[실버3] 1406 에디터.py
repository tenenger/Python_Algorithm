from collections import deque
import sys
input = sys.stdin.readline
stack = list(input().strip())
deque = deque()

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == "L":
        if stack:
            deque.appendleft(stack.pop())
    elif  command[0] == "D":
        if deque:
            stack.append(deque.popleft())
    elif command[0] == "P":
        stack.append(command[1])
    else:
        if stack:
            stack.pop()
print("".join(stack + list(deque)))
    