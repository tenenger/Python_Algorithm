# 구간 합 알고리즘

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
sum_value = 0

for i in numbers:
    sum_value += i
    prefix_sum.append(sum_value)

for j in range(m):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start-1])