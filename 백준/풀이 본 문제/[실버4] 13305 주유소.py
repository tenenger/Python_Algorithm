import sys
input = sys.stdin.readline
n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = 0

cnt = cost[0]
for i in range(n-1):
    if cnt > cost[i]:
        cnt = cost[i]
    result += cnt * road[i]
print(result)
