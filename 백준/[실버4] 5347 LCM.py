import math
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = math.lcm(n, m)
    print(result)
