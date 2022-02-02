import sys
input = sys.stdin.readline
k = int(input())
result = 0
stack = []
for _ in range(k):
    number = int(input())
    if number == 0:
        if stack:
            stack.pop()
        else:
            continue
    else:
        stack.append(number)
print(sum(stack))
