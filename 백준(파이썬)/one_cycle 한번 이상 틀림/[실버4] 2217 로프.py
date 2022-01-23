import sys
input = sys.stdin.readline
n = int(input())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)
weight = 0

for i in range(n):
    result = data[i] * (i+1)
    if weight < result:
        weight = result
print(weight)
