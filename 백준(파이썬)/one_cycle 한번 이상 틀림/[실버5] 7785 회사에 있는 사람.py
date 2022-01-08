import sys

n = int(sys.stdin.readline())
result = {}

for i in range(n):
    name, status = sys.stdin.readline().strip().split(" ")
    if status == 'enter':
        result[name] = True
    else:
        result.pop(name)

print("\n".join(sorted(result, reverse=True)))