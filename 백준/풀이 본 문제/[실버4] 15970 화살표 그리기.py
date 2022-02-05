import sys
import math
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
result = 0
for i in range(n):
    min_distance = math.inf  # 양의 무한수
    target_location, target_color = data[i]
    for j in range(n):
        if i == j:
            continue
        if data[j][1] == target_color:
            min_distance = min(min_distance, abs(target_location-data[j][0]))
    result += min_distance

print(result)
