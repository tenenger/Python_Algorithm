import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(1, n + 1)]
stack = []
result = []
idx = 0
for i in range(1, n+1):
    stack.append(i)
    result.append('+')
    while stack:
        if stack[-1] == arr[idx]:
            stack.pop()
            result.append('-')
            idx += 1
        else:
            break
if stack:
    print('NO')
else:
    print("\n".join(result))
