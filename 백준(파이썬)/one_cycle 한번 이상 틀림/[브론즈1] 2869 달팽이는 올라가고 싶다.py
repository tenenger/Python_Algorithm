A, B, V = map(int, input().split())
import math
cnt = 1
cnt += math.ceil((V-A)/(A-B))
print(cnt)