import sys
input = sys.stdin.readline
n = int(input())
tips = [int(input()) for _ in range(n)]
tips.sort(reverse=True)
result = 0
for i in range(n):
    rank = i + 1
    tip = tips[i] - (rank - 1)
    if tip <= 0:
        continue
    else:
        result += tip
print(result)
