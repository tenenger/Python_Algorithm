import sys
input = sys.stdin.readline
n = int(input())
data = [int(input()) for _ in range(n)]
cnt = 0
data.sort(reverse=True)

for i in range(0, n, 3):
    result = data[i:i+3]

    if len(result) == 3:
        result.remove(min(result))
    cnt += sum(result)
print(cnt)
