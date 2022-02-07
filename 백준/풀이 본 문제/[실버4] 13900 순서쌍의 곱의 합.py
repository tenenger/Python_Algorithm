import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
result, total = 0, sum(data)

for i in range(n):
    element = data[i]
    case = element * (total - element)
    result += case
print(result // 2)
