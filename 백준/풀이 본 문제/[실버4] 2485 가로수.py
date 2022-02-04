import sys
import math
from functools import reduce
input = sys.stdin.readline
n = int(input())
data = [int(input()) for _ in range(n)]
min_number = 1000000000
result = []
start = True

cnt = 0
for i in range(1, n):
    diff = data[i] - data[i-1]
    result.append(diff)
    min_number = min(min_number, diff)


def diff_gcd(list):
    x = reduce(math.gcd, list)
    return x


diff_gcd_num = diff_gcd(result)

for i in result:
    cnt += int(i/diff_gcd_num - 1)
print(cnt)
