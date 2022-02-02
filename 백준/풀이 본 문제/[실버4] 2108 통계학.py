import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
data = [int(input()) for _ in range(N)]
data.sort()

average = sum(data) / N
middle = data[N//2]
rangeNumber = max(data) - min(data)
if N == 1:
    frequency = data[0]
else:
    tmp = Counter(data).most_common(2)
    if tmp[0][1] == tmp[1][1]:
        frequency = tmp[1][0]
    else:
        frequency = tmp[0][0]
print('{:.0f}'.format(average), f'{middle}',
      f'{frequency}', f'{rangeNumber}', sep='\n')
